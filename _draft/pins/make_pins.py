from PIL import Image,ImageDraw,ImageFont
import textwrap
F='/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf';R=F.replace('Bold','Regular')
BG=(31,33,36);G=(224,170,62);W=(245,245,240)
P=[("pin1-dear-epu-mug","share/dear-epu-mug.jpg","FUNNY TRUCKER MUG","Dear EPU, Please Let Me Sleep","A gift for any driver with an EPU","triamdenmarketing.etsy.com"),
("pin2-mug-lineup","GRID","GIFTS FOR TRUCK DRIVERS","Funny Mugs by a|Working CDL-A Driver","EPU, HOS, cab rules, reheated meals","triamdenmarketing.etsy.com"),
("pin3-reheat-tumbler","shop/tumbler-i-dont-cook-i-reheat.jpg","20OZ TRUCKER TUMBLER","I Don't Cook.|I Reheat.","Black 20oz insulated. Free US shipping.","triamdenmarketing.etsy.com"),
("pin4-epu-article","epu-panel.jpg","FROM THE CAB","My EPU Keeps Waking Me Up","What living with one is really like","cabgear.triamden.com"),
("pin5-eat-on-road","meals-microwave.jpg","TRUCK DRIVER MEALS","How I Eat on the Road","My setup, plus the backup plan","cabgear.triamden.com")]
def fit(d,t,f,s,w):
    while True:
        ft=ImageFont.truetype(f,s);ls=[];cur=''
        for x in t.split():
            n=(cur+' '+x).strip()
            if d.textlength(n,font=ft)<=w:cur=n
            else:ls.append(cur);cur=x
        ls.append(cur)
        if len(ls)<=3:return ft,ls
        s-=4
for n,src,k,h,sub,foot in P:
    im=Image.new('RGB',(1000,1500),BG);d=ImageDraw.Draw(im);y=70
    d.text((60,y),k,font=ImageFont.truetype(F,34),fill=G);y+=62
    ft,ls=(ImageFont.truetype(F,84),h.split('|')) if '|' in h and max(d.textlength(x,font=ImageFont.truetype(F,84)) for x in h.split('|'))<=880 else (ImageFont.truetype(F,72),h.split('|')) if '|' in h else fit(d,h,F,84,880)
    for l in ls:d.text((60,y),l,font=ft,fill=W);y+=int(ft.size*1.2)
    y+=20
    if src=='GRID':
        ks=['epu-dear-epu-let-me-sleep','i-dont-cook-i-reheat','my-patience-has-an-hos-limit','my-cab-my-rules','my-office-has-18-wheels-truck','no-kettle-no-coffee-no-problem']
        HH=1290-y;rh=HH//3;rw=int(rh*640/480)
        first=Image.open(f'shop/{ks[0]}.jpg').convert('RGB');a=Image.new('RGB',(1000,HH),first.getpixel((5,5)))
        for i,q in enumerate(ks):
            m=Image.open(f'shop/{q}.jpg').convert('RGB').resize((rw,rh),Image.LANCZOS);a.paste(m,(60+i%2*(880-rw) if i%2 else 60,i//2*rh))
    else: a=Image.open(src).convert('RGB')
    top=y;bot=1500-210;H=bot-top;w=1000
    s=max(w/a.width,H/a.height);a=a.resize((int(a.width*s),int(a.height*s)),Image.LANCZOS)
    x0=(a.width-w)//2;y0=(a.height-H)//2;im.paste(a.crop((x0,y0,x0+w,y0+H)),(0,top))
    d.text((60,bot+30),sub,font=ImageFont.truetype(R,40),fill=W)
    d.text((60,bot+100),foot,font=ImageFont.truetype(F,34),fill=G)
    im.save(f'_draft/pins/{n}.jpg',quality=90)
ims=[Image.open(f'_draft/pins/{p[0]}.jpg').resize((400,600)) for p in P]
sh=Image.new('RGB',(2040,600),(255,255,255))
for i,m in enumerate(ims):sh.paste(m,(i*410,0))
sh.save('_draft/pins/contact-sheet.jpg',quality=88)
