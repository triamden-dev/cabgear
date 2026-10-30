"""Build the TriAmden Cab Gear static site.
Outputs:
  ../site/      full HTML documents, ready to upload to any static host
  ../artifact/  same pages; index.html as a fragment for the Artifact preview
"""
import os, re, shutil
from art import ART as ILLUS, hero_scene

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "..", "site")
ART = os.path.join(ROOT, "..", "artifact")
DRAFT = False  # shows the preview banner and noindex; set False to go live
GA_ID = "G-15KT55Z8TT"  # GA4 property: TriAmden Cab Gear

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400'
         '&family=Overpass:wght@500;600;700;800&family=Overpass+Mono:wght@500;600'
         '&family=Bebas+Neue&family=Permanent+Marker&display=swap">')

# --- Amazon links ---------------------------------------------------------
# Plain product links until the Associates account is approved.
# On approval: set ASSOCIATE_TAG (e.g. "triamden-20") and rebuild. Every Amazon
# link gets the tag, and every disclosure switches to Amazon's required sentence.
ASSOCIATE_TAG = None
PRODUCTS = {
    "High Road visor organizer": "B0000UZ528",
    "WYNEX MOLLE visor organizer": "B0DXF93V4W",
    "XERGUR steering wheel tray": "B07Z92Y8JV",
    "HOTLOGIC Mini 12V": "B074TZKCCV",
    "TRAVELISIMO 100W": "B0D22TGD88",
    "Feelfunn 40QT dual zone": "B0FLX846J2",
}
if ASSOCIATE_TAG:
    DISCLOSURE = "As an Amazon Associate I earn from qualifying purchases."
    DISCLOSURE_LONG = ("TriAmden Cab Gear is a participant in the Amazon Associates program. "
                       "As an Amazon Associate I earn from qualifying purchases. Buying through our links costs you nothing extra.")
    FOOTER_NOTE = "Links to Amazon on this site may earn us a commission at no extra cost to you."
    FOOTER_SHORT = "As an Amazon Associate I earn from qualifying purchases."
    AFFILIATE_PAGE = ("<p>TriAmden Cab Gear participates in the Amazon Associates Program, an affiliate advertising program "
                      "that lets sites earn fees by linking to Amazon.com. When you click a link on this site and buy something "
                      "on Amazon, we may earn a commission. The price you pay is the same.</p>")
else:
    DISCLOSURE = "TriAmden Cab Gear plans to join affiliate programs, including Amazon Associates."
    DISCLOSURE_LONG = ("TriAmden Cab Gear plans to join affiliate programs, including Amazon Associates. "
                       "When it does, some links may earn us a commission at no extra cost to you. Right now, our Amazon links earn us nothing.")
    FOOTER_NOTE = "Our Amazon links don't earn commissions yet. If that changes, we'll say so here and on every article."
    FOOTER_SHORT = "Our Amazon links don't earn commissions yet."
    AFFILIATE_PAGE = ("<p>Right now, the Amazon links on this site are ordinary product links. We don't earn anything when you use them.</p>"
                      "<p>We plan to join the Amazon Associates Program, an affiliate advertising program that lets sites earn fees by "
                      "linking to Amazon.com. When we're accepted, some links will earn us a commission when you buy, at no extra cost "
                      "to you, and this page and every article will say so.</p>")

AMAZON_TERMS = ("We don't sell the products we link to. Orders placed on Amazon are sold and shipped by Amazon or its sellers, "
                "and returns, shipping, warranties and refunds follow Amazon's policies and the seller's terms. "
                "Contact Amazon or the seller for help with an order.")

FB_URL = "https://www.facebook.com/TriAmdenMarketing/"
IG_URL = "https://www.instagram.com/triamden/"
YT_URL = "https://www.youtube.com/@TriAmdenMarketing"
YT_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 8.2a3 3 0 0 0-2.1-2.1C18 5.6 12 5.6 12 5.6s-6 0-7.9.5A3 3 0 0 0 2 8.2 31 31 0 0 0 1.6 12 31 31 0 0 0 2 15.8a3 3 0 0 0 2.1 2.1c1.9.5 7.9.5 7.9.5s6 0 7.9-.5a3 3 0 0 0 2.1-2.1c.4-1.2.4-3.8.4-3.8s0-2.6-.4-3.8zM10 15V9l5.2 3z"/></svg>'
FB_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v6h4v-6H16l.6-4h-3.1V9c0-.6.4-1 1-1z"/></svg>'
IG_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.2"/></svg>'
SOCIAL = (f'<a class="soc" href="{FB_URL}" target="_blank" rel="noopener me" aria-label="TriAmden on Facebook">{FB_SVG}</a>'
          f'<a class="soc" href="{IG_URL}" target="_blank" rel="noopener me" aria-label="TriAmden on Instagram">{IG_SVG}</a>'
          f'<a class="soc" href="{YT_URL}" target="_blank" rel="noopener me" aria-label="TriAmden on YouTube">{YT_SVG}</a>')

SHOP_URL = "https://www.etsy.com/shop/TriAmdenMarketing"
MUGS = {
 "epu-dear-epu-let-me-sleep": ("Dear EPU, Please Let Me Sleep", "4606492649/dear-epu-please-let-me-sleep-mug-funny"),
 "epu-every-peaceful-unrest": ("Every Peaceful Unrest", "4606494609/every-peaceful-unrest-epu-mug-funny"),
 "epu-exhausted-pissed-unrested": ("Exhausted, Pissed, Unrested", "4606495551/exhausted-pissed-unrested-epu-mug-funny"),
 "my-office-has-18-wheels-truck": ("My Office Has 18 Wheels", "4606496415/my-office-has-18-wheels-mug-funny"),
 "i-dont-cook-i-reheat": ("I Don't Cook. I Reheat.", "4606516096/i-dont-cook-i-reheat-mug-funny-trucker"),
 "my-kitchen-travels-at-65-mph": ("My Kitchen Travels at 65 MPH", "4606497269/my-kitchen-travels-at-65-mph-mug-funny"),
 "no-kettle-no-coffee-no-problem": ("No Kettle. No Coffee. No Problem.", "4606517152/no-kettle-no-coffee-no-problem-mug-funny"),
 "my-cab-my-rules": ("My Cab. My Rules.", "4606517822/my-cab-my-rules-mug-funny-trucker-coffee"),
 "my-cab-is-cleaner-than-your-office": ("My Cab Is Cleaner Than Your Office", "4606499171/my-cab-is-cleaner-than-your-office-mug"),
 "keep-it-clean-keep-it-rolling": ("Keep It Clean. Keep It Rolling.", "4606519264/keep-it-clean-keep-it-rolling-mug-funny"),
 "leaf-blower-clean-certified": ("Leaf Blower Clean Certified", "4606500615/leaf-blower-clean-certified-mug-funny"),
 "a-place-for-everything": ("A Place for Everything", "4606520638/a-place-for-everything-mug-funny-trucker"),
 "organized-chaos-is-still-chaos": ("Organized Chaos Is Still Chaos", "4606501907/organized-chaos-is-still-chaos-mug-funny"),
 "my-patience-has-an-hos-limit": ("My Patience Has an HOS Limit", "4606522064/my-patience-has-an-hos-limit-mug-funny"),
 "my-other-home-has-a-sleeper": ("My Other Home Has a Sleeper", "4606504001/my-other-home-has-a-sleeper-mug-funny"),
 "real-gear-real-miles-real-life": ("Real Gear. Real Miles. Real Life.", "4606523776/real-gear-real-miles-real-life-mug-funny"),
 "living-life-one-load-at-a-time": ("Living Life One Load at a Time", "4606524484/living-life-one-load-at-a-time-mug-funny"),
 "heavy-hauls-lighter-me": ("Heavy Hauls. Lighter Me.", "4606505299/heavy-hauls-lighter-me-mug-funny-trucker"),
 "shakes-bars-and-diesel": ("Shakes, Bars & Diesel", "4606525576/shakes-bars-and-diesel-mug-funny-trucker"),
 "shaking-my-way-across-america": ("Shaking My Way Across America", "4606526318/shaking-my-way-across-america-mug-funny"),
 "and-im-cute-too": ("And I'm Cute Too", "4606526978/and-im-cute-too-mug-funny-trucker-coffee"),
 "whats-your-position": ("What's Your Position?", "4606507803/whats-your-position-mug-funny-trucker"),
}
PAGE_MUGS = {
 "index.html": ("From the Cab Gear shop", ["epu-dear-epu-let-me-sleep", "i-dont-cook-i-reheat", "my-office-has-18-wheels-truck", "my-patience-has-an-hos-limit"]),
 "epu-vs-idling.html": ("Mugs for every driver your EPU has woken up", ["epu-dear-epu-let-me-sleep", "epu-every-peaceful-unrest", "epu-exhausted-pissed-unrested"]),
 "how-i-eat-on-the-road.html": ("For the cab kitchen", ["i-dont-cook-i-reheat", "my-kitchen-travels-at-65-mph", "no-kettle-no-coffee-no-problem"]),
 "cab-organization-zones.html": ("For the organized cab", ["a-place-for-everything", "organized-chaos-is-still-chaos", "my-cab-is-cleaner-than-your-office"]),
 "protein-snacks-for-truck-drivers.html": ("For drivers eating clean on the road", ["shakes-bars-and-diesel", "shaking-my-way-across-america", "heavy-hauls-lighter-me"]),
 "cab-kitchen-clutter-guide.html": ("For drivers who keep a clean cab", ["my-cab-is-cleaner-than-your-office", "leaf-blower-clean-certified", "keep-it-clean-keep-it-rolling"]),
 "12v-lunch-box-hotlogic-vs-travelisimo.html": ("For the cab kitchen", ["i-dont-cook-i-reheat", "my-kitchen-travels-at-65-mph", "no-kettle-no-coffee-no-problem"]),
 "12v-fridge-buying-checklist.html": ("For the cab kitchen", ["my-kitchen-travels-at-65-mph", "i-dont-cook-i-reheat", "shakes-bars-and-diesel"]),
 "about.html": ("Designed by a working driver", ["real-gear-real-miles-real-life", "my-other-home-has-a-sleeper", "living-life-one-load-at-a-time", "my-cab-my-rules"]),
}

def shop_strip(slug):
    if slug not in PAGE_MUGS: return ""
    head, keys = PAGE_MUGS[slug]
    cards = "".join(
        f'<li><a href="https://www.etsy.com/listing/{MUGS[k][1]}" target="_blank" rel="noopener">'
        f'<img src="shop/{k}.jpg" alt="Black mug with the {MUGS[k][0]} design" width="640" height="480" loading="lazy">'
        f'<span>{MUGS[k][0]}</span><em>Mug on Etsy</em></a></li>' for k in keys)
    return (f'<section class="shop-strip"><div class="wrap"><div class="section-head"><h2>{head}</h2>'
            f'<a href="{SHOP_URL}" target="_blank" rel="noopener">See all designs on Etsy</a></div>'
            f'<ul class="shop-cards">{cards}</ul>'
            f'<p class="shop-note">Our own designs, sold in the TriAmden Marketing Etsy shop. We earn from these sales.</p></div></section>')

NAV = [("index.html", "Home"), ("cab-kitchen-clutter-guide.html", "Gear guide"),
       ("cab-organization-zones.html", "Organize"), ("about.html", "About"), (SHOP_URL, "Shop")]


def note(text):
    return f'<div class="note"><strong>Clifford adds:</strong> {text}</div>' if DRAFT else ""


def buy(name):
    url = f"https://www.amazon.com/dp/{PRODUCTS[name]}"
    rel = "noopener nofollow"
    if ASSOCIATE_TAG:
        url += f"?tag={ASSOCIATE_TAG}"
        rel += " sponsored"
    return f'<a class="buy" href="{url}" target="_blank" rel="{rel}">View {name} on Amazon</a>'


TONES = {
    "epu-vs-idling.html": "tone-warm", "how-i-eat-on-the-road.html": "tone-warm",
    "protein-snacks-for-truck-drivers.html": "tone-warm",
    "cab-kitchen-clutter-guide.html": "tone-cool", "12v-lunch-box-hotlogic-vs-travelisimo.html": "tone-cool",
    "12v-fridge-buying-checklist.html": "tone-cool", "cab-organization-zones.html": "tone-cool",
}


def body_class(slug):
    if slug == "index.html":
        return "home"
    if slug == "about.html":
        return "about-page"
    return "road-page " + TONES.get(slug, "tone-plain")


BASE = "https://cabgear.triamden.com/"

def page(slug, title, desc, body, current=None):
    url = BASE + ("" if slug == "index.html" else slug)
    mimg = re.search(r'src="([^"]+\.(?:jpg|png|webp))"', ILLUS.get(slug, "")) if slug != "index.html" else None
    ogimg = BASE + (mimg.group(1) if mimg else "og-default.jpg")
    og = (f'<link rel="canonical" href="{url}">\n'
          f'<meta property="og:type" content="{"website" if slug == "index.html" else "article"}">\n'
          f'<meta property="og:site_name" content="TriAmden Cab Gear">\n'
          f'<meta property="og:title" content="{title}">\n'
          f'<meta property="og:description" content="{desc}">\n'
          f'<meta property="og:url" content="{url}">\n'
          f'<meta property="og:image" content="{ogimg}">\n'
          f'<meta name="twitter:card" content="summary_large_image">')
    # card illustrations
    for k, svg in ILLUS.items():
        body = body.replace(f'<li class="card"><a href="{k}">', f'<li class="card"><a href="{k}"><div class="card-art">{svg}</div><div class="card-body">', 1)
    body = re.sub(r'(<li class="card">.*?</p>)(</a></li>)', lambda m: m.group(1) + ('</div>' if 'card-body' in m.group(1) else '') + m.group(2), body, flags=re.S)
    # article header art
    if slug in ILLUS and slug != "index.html":
        body = body.replace('<article class="article"><div class="wrap">', f'<div class="art-band"><div class="wrap art-band-inner">{ILLUS[slug]}</div></div><article class="article"><div class="wrap">', 1)
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == (current or slug) else ""}>{t}</a>' for h, t in NAV)
    draft = ('<div class="draft"><div class="wrap">Preview. This site is not public yet.</div></div>') if DRAFT else ""
    ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>'
          f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}'
          f'gtag("js",new Date());gtag("config","{GA_ID}");</script>') if GA_ID else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex">' if DRAFT else og}
{FONTS}
<meta name="p:domain_verify" content="aeaeca8c26ca3080610c8a4b63c0a5b9">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="stylesheet" href="styles.css">
{ga}
</head>
<body class="{body_class(slug)}">
<header class="masthead"><div class="wrap">
  <a class="brand" href="index.html"><img class="brand-logo" src="logo.png" alt="TriAmden Marketing, home of Cab Gear" width="360" height="128"></a>
  <nav class="nav" aria-label="Main">{nav}<span class="socials">{SOCIAL}</span></nav>
</div></header>
{draft}
<main>
{body}
{shop_strip(slug)}
</main>
<footer class="footer"><div class="wrap">
  <p style="margin:0">{FOOTER_SHORT} {AMAZON_TERMS}</p>
  <nav aria-label="Footer"><a href="privacy.html">Privacy</a><a href="contact.html">Contact</a><a href="about.html">About</a><a href="{FB_URL}" target="_blank" rel="noopener me">Facebook</a><a href="{IG_URL}" target="_blank" rel="noopener me">Instagram</a><a href="{YT_URL}" target="_blank" rel="noopener me">YouTube</a></nav>
  <p style="margin:0">© 2026 TriAmden Marketing. Cab Gear is written for professional drivers by a working CDL-A driver.</p>
</div></footer>
</body>
</html>
"""


# ---------- HOS grid graphic (home hero) ----------
def hos_svg():
    x0, w, rowh = 46, 24 * 18, 26
    rows = ["OFF", "SB", "D", "ON"]
    parts = [f'<svg class="hos" viewBox="0 0 {x0 + w + 8} {rowh * 4 + 30}" role="img" '
             'aria-label="Sample duty-status grid showing a day of off-duty, sleeper, driving and on-duty time">']
    for i, r in enumerate(rows):
        y = 18 + i * rowh
        parts.append(f'<text x="0" y="{y + 17}">{r}</text>')
        for h in range(24):
            parts.append(f'<rect class="cell" x="{x0 + h * 18}" y="{y}" width="18" height="{rowh}"/>')
    for h in range(0, 25, 6):
        parts.append(f'<text x="{x0 + h * 18 - 4}" y="12">{h if h < 24 else ""}</text>')
    # illustrative day: SB 0-5, ON 5-5.5, D 5.5-11, OFF 11-11.5, D 11.5-16, ON 16-17, SB 17-24
    seq = [(0, 1), (5, 3), (5.5, 2), (11, 0), (11.5, 2), (16, 3), (17, 1), (24, 1)]
    pts, prev = [], None
    for t, r in seq:
        y = 18 + r * rowh + rowh / 2
        x = x0 + t * 18
        if prev is not None:
            pts.append(f"{x},{prev}")
        pts.append(f"{x},{y}")
        prev = y
    parts.append(f'<polyline class="trace" points="{" ".join(pts)}"/></svg>')
    return "".join(parts)


PAGES = {}

PAGES["index.html"] = ("TriAmden Cab Gear", "Cab organization and in-cab kitchen gear for over-the-road truck drivers.", f"""
<section class="hero hero-photo">
  <div class="hero-media"><img class="hero-img" src="hero-truck.jpg" alt="An orange TriAmden Transportation semi truck on a mountain highway at sunset" width="1108" height="687"></div>
  <div class="wrap hero-copy">
    <h1 class="hero-logo"><img src="cabgear-logo.webp" alt="TriAmden Cab Gear" width="1000" height="315"></h1>
    <p class="tagline">Gear for a <em>safer, cleaner,</em><br><em>more comfortable</em> road ahead.</p>
    <p class="hero-sub">Real advice from a working CDL-A driver.</p>
    <ul class="hero-icons">
      <li><a href="epu-vs-idling.html"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 3v9a2 2 0 0 0 2 2h6M8 14l-1 7M16 14l2 7M6 21h14M16 14v-3h3"/></svg><span>Cab comfort</span></a></li>
      <li><a href="cab-organization-zones.html"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="7" height="7" rx="1"/><rect x="13" y="4" width="7" height="7" rx="1"/><rect x="4" y="13" width="7" height="7" rx="1"/><rect x="13" y="13" width="7" height="7" rx="1"/></svg><span>Organization</span></a></li>
      <li><a href="how-i-eat-on-the-road.html"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 10h16v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5zM2 10h20M9 6c0-1 1-1 1-2M14 6c0-1 1-1 1-2"/></svg><span>Cab kitchen</span></a></li>
      <li><a href="cab-kitchen-clutter-guide.html"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6z"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/></svg><span>Gear that works</span></a></li>
    </ul>
  </div>
</section>
<section class="guides"><div class="wrap">
  <div class="section-head"><h2>Guides</h2><a href="cab-kitchen-clutter-guide.html">Start with the gear guide</a></div>
  <ul class="cards">
    <li class="card"><a href="cab-kitchen-clutter-guide.html"><span class="tag">Buying guide</span><h3>Cab Kitchen &amp; Clutter Control: 5 Gear Picks</h3><p>Why a visor organizer beats a seat-back one, plus two 12V lunch boxes, a dual-zone fridge and a steering wheel tray.</p></a></li>
    <li class="card"><a href="12v-lunch-box-hotlogic-vs-travelisimo.html"><span class="tag">Comparison</span><h3>HOTLOGIC Mini vs. TRAVELISIMO 100W</h3><p>Which 12V heated lunch box fits how you drive, and what to check before you buy either.</p></a></li>
    <li class="card"><a href="12v-fridge-buying-checklist.html"><span class="tag">Checklist</span><h3>12V Fridge Buying Checklist for Truck Drivers</h3><p>Space, power, battery protection and carrier rules to settle before spending a few hundred dollars.</p></a></li>
    <li class="card"><a href="cab-organization-zones.html"><span class="tag">How-to</span><h3>Organize Your Cab by Zone</h3><p>Driver's reach, passenger seat, bunk and storage: what belongs where, including the documents that must stay in the cab.</p></a></li>
    <li class="card"><a href="protein-snacks-for-truck-drivers.html"><span class="tag">Driver's take</span><h3>The Protein Snacks That Get Me Through a Shift</h3><p>What I keep within reach, what it really costs per week, and the Doritos I'm not giving up.</p></a></li>
    <li class="card"><a href="how-i-eat-on-the-road.html"><span class="tag">Driver's take</span><h3>How I Eat on the Road</h3><p>A week of home-cooked meals, a moved-from-truck-to-truck microwave, and the backup plan when the food runs out.</p></a></li>
    <li class="card"><a href="epu-vs-idling.html"><span class="tag">Driver's take</span><h3>My EPU Keeps Waking Me Up</h3><p>Why a quiet electric power unit still costs me sleep, what idling really costs, and what I'd tell a new driver.</p></a></li>
  </ul>
</div></section>
""")

PAGES["cab-kitchen-clutter-guide.html"] = ("Cab Kitchen & Clutter Control", "Five gear picks for over-the-road truck drivers: organization, hot meals and cold storage.", f"""
<article class="article"><div class="wrap">
<p class="eyebrow">Buying guide</p>
<h1>Cab Kitchen &amp; Clutter Control: 5 Gear Picks for Over-the-Road Drivers</h1>
<p class="byline">By Clifford Cruickshank, CDL-A driver · Updated October 2026</p>
<p class="disclosure"><strong>Disclosure:</strong> {DISCLOSURE_LONG}</p>
<p>A truck cab is your office, kitchen and bedroom in less floor space than most closets. Two things decide whether a long week out feels manageable: whether you can find what you need without digging, and whether you can eat something other than truck-stop food. This guide covers both.</p>
<p>I've driven commercially since 2017, OTR and regional, hauling reefer and dry van freight. I run a 2022 Kenworth T680 sleeper with a built-in fridge, and I reheat home-cooked meals in a microwave. If your truck doesn't have those, the gear below is how you get close.</p>
<div class="disclosure"><strong>How I picked these:</strong> I haven't tested these five products myself. I chose them from their Amazon listings, published specs and the number of customer reviews, and I've noted what to check before you buy. When I use one, I'll update this page with what I find.</div>

<h2>Organization</h2>
<section class="pick">
  <h3>Skip the seat-back organizer. Get a visor organizer.</h3>
  <p>Seat-back organizers are sold everywhere as trucker gear, and I think they're a waste of money. In a truck the seats are usually pushed all the way back, so getting behind one to pull something out is impractical. A visor organizer puts the same things right above you, where you can reach them.</p>
  <p class="meta">Pick: High Road visor organizer and document holder · Alternative: WYNEX MOLLE visor organizer</p>
  <p>The High Road model is built around paperwork and cards, with a document pocket and smaller slots, which suits logs, bills of lading and fuel cards. The WYNEX uses a MOLLE panel if you'd rather clip on pouches. Both are sold for cars and trucks, and semi visors are larger than car visors, so check the strap length against your visor before buying.</p>
  {buy("High Road visor organizer")} {buy("WYNEX MOLLE visor organizer")}
</section>
<section class="pick">
  <h3>XERGUR 2-in-1 steering wheel tray</h3>
  <p class="meta">Brand: XERGUR · Fits on the steering wheel or a headrest</p>
  <p>A flat surface for a meal or paperwork while you're parked. Check the product dimensions against your own steering wheel before you buy: semi wheels are larger and sit flatter than car wheels, and this tray is designed around passenger vehicles. Use it only when the truck is parked.</p>
  {buy("XERGUR steering wheel tray")}
</section>

<h2>Hot meals on the road</h2>
<p>My routine: my wife cooks a week of meals before I head out, they go in the truck's fridge, and I reheat them in the microwave. When they run out, it's a Walmart rotisserie chicken and potato salad, or Subway for a change. That keeps me off truck-stop food most of the week. No microwave in your truck? A 12V heated lunch box plugs into the cab's power socket and warms food you packed or bought at a grocery store. The two below are the most-reviewed options we found. The <a href="12v-lunch-box-hotlogic-vs-travelisimo.html">full comparison</a> goes deeper.</p>
<div class="table-wrap"><table>
  <thead><tr><th></th><th>HOTLOGIC Mini 12V</th><th>TRAVELISIMO 100W</th></tr></thead>
  <tbody>
    <tr><td>Power (per listing)</td><td>12V</td><td>12V, 24V and 110V</td></tr>
    <tr><td>Best fit</td><td>Drivers who only heat food in the truck</td><td>Drivers who also want to use it at home or in a motel</td></tr>
  </tbody>
</table></div>
{buy("HOTLOGIC Mini 12V")} {buy("TRAVELISIMO 100W")}

<h2>Keeping food cold</h2>
<section class="pick">
  <h3>Feelfunn 40QT dual-zone 12V fridge/freezer</h3>
  <p class="meta">Brand: Feelfunn · 40 quarts · Two temperature zones · 12/24V DC and AC power (per listing)</p>
  <p>A compressor fridge that runs on the truck's DC power. The two zones let you freeze in one side and refrigerate in the other, so one grocery run can cover more of the week. A 12V fridge is a bigger purchase than anything else here, so read the <a href="12v-fridge-buying-checklist.html">fridge checklist</a> before you buy any model.</p>
  {buy("Feelfunn 40QT dual zone")}
</section>

<h2>Where to start</h2>
<ul>
  <li><strong>Lowest cost:</strong> a visor organizer.</li>
  <li><strong>Biggest daily difference:</strong> a heated lunch box.</li>
  <li><strong>Biggest investment:</strong> a 12V fridge. Measure your space and check your power setup first.</li>
</ul>
</div></article>
""", "cab-kitchen-clutter-guide.html")

PAGES["12v-lunch-box-hotlogic-vs-travelisimo.html"] = ("HOTLOGIC vs TRAVELISIMO", "Comparing two popular 12V heated lunch boxes for truck drivers.", f"""
<article class="article"><div class="wrap">
<p class="eyebrow">Comparison</p>
<h1>HOTLOGIC Mini vs. TRAVELISIMO 100W: Which 12V Lunch Box?</h1>
<p class="byline">By Clifford Cruickshank, CDL-A driver · Updated October 2026</p>
<p class="disclosure"><strong>Disclosure:</strong> {DISCLOSURE}</p>
<p>Both of these plug into your cab's 12V socket and heat a packed meal while you drive or wait at a dock. They solve the same problem in different ways, so the right pick depends on where else you want to use it.</p>

<h2>Side by side</h2>
<div class="table-wrap"><table>
  <thead><tr><th></th><th>HOTLOGIC Mini 12V</th><th>TRAVELISIMO 100W</th></tr></thead>
  <tbody>
    <tr><td>Power sources (per listing)</td><td>12V</td><td>12V, 24V, 110V</td></tr>
    <tr><td>Listed wattage</td><td>Check the current listing</td><td>100W</td></tr>
    <tr><td>Listed capacity</td><td>Check the current listing</td><td>1.5 liters</td></tr>
    <tr><td>Container (per listing)</td><td>Check the current listing</td><td>Stainless steel</td></tr>
    <tr><td>Choose it if</td><td>You only heat food in the truck</td><td>You split time between truck, home and motels</td></tr>
  </tbody>
</table></div>
<p>Where a cell says to check the listing, the detail wasn't stated clearly enough for us to repeat it. Specs and prices change, so confirm them on Amazon before you buy.</p>

<h2>Power draw in plain numbers</h2>
<p>On a 12V system, current is watts divided by volts. A 100-watt heater pulls a little over 8 amps (100 ÷ 12 ≈ 8.3). Check the fuse rating of the socket you plan to use, and don't share that socket with another high-draw device through a splitter.</p>

<h2>Which one</h2>
<ul>
  <li><strong>HOTLOGIC Mini</strong> if the truck is the only place you'll use it and you want something simple.</li>
  <li><strong>TRAVELISIMO 100W</strong> if you also want to plug it into a wall outlet at home or in a motel.</li>
</ul>
<p>{buy("HOTLOGIC Mini 12V")} {buy("TRAVELISIMO 100W")}</p>
<p class="disclosure"><strong>Where this comes from:</strong> I haven't used either one. My truck has a microwave, so I reheat meals that way. This comparison is built from the product listings and specs, for drivers who don't have a microwave.</p>
</div></article>
""", "cab-kitchen-clutter-guide.html")

PAGES["12v-fridge-buying-checklist.html"] = ("12V Fridge Checklist", "What truck drivers should check before buying a 12V refrigerator for the cab.", f"""
<article class="article"><div class="wrap">
<p class="eyebrow">Checklist</p>
<h1>12V Fridge Buying Checklist for Truck Drivers</h1>
<p class="byline">By Clifford Cruickshank, CDL-A driver · Updated October 2026</p>
<p class="disclosure"><strong>Disclosure:</strong> {DISCLOSURE}</p>
<p>A good 12V fridge can cut what you spend on food and give you better choices on the road. It's also a few hundred dollars and a permanent piece of your living space. Work through this list before you pick a model.</p>

<h2>1. Space</h2>
<ul class="check">
  <li>Measure the spot: width, depth and height, plus room for the lid to open.</li>
  <li>Leave clearance around the vents. Compressor fridges need airflow to run efficiently.</li>
  <li>Plan how you'll secure it. Anything loose in a cab moves in a hard stop.</li>
  <li><strong>A door or lid that locks.</strong> Truck movement and vibration can pop a fridge open while you're driving and dump the contents across the cab. A secure latch or lock is the first thing I'd look for.</li>
</ul>

<h2>2. Cooling type</h2>
<ul class="check">
  <li><strong>Compressor</strong> fridges hold a set temperature and many can freeze.</li>
  <li><strong>Thermoelectric</strong> coolers only cool a certain amount below the air around them, so they struggle in a hot cab.</li>
  <li>Dual-zone models let you run a freezer and a fridge side at once.</li>
</ul>

<h2>3. Power while parked</h2>
<ul class="check">
  <li>Know how your truck handles power during your 10-hour break: APU, battery bank, shore power or idling.</li>
  <li>Anti-idling rules vary by state and city. Don't plan on idling to run the fridge.</li>
  <li>Look for <strong>low-voltage battery protection</strong> so the fridge shuts off before it drains your batteries.</li>
  <li>Check whether the model runs on both 12V and 24V DC, and whether it has an AC adapter for home.</li>
</ul>

<h2>4. Living with it</h2>
<ul class="check">
  <li>Noise: you'll sleep next to it. Look for stated noise levels and read reviews that mention them.</li>
  <li>Drain plug and removable baskets make cleaning easier.</li>
  <li>App control is optional. A clear physical display matters more.</li>
  <li>Warranty: check how long it lasts and whether it covers the compressor, the most expensive part to replace.</li>
</ul>

<h2>5. Your carrier</h2>
<ul class="check">
  <li>Some fleets limit appliances, inverters or how equipment is mounted. Ask before you buy if you drive a company truck.</li>
</ul>

<h2>Models covered on this site</h2>
<p>We currently cover the <a href="cab-kitchen-clutter-guide.html">Feelfunn 40QT dual-zone</a> as a mid-priced option. Premium models from brands such as ICECO cost considerably more.</p>
<p>My own Kenworth came with a built-in fridge, so I haven't bought a portable one. If I were shopping, I'd weigh capacity, power draw, dimensions, cooling performance and reliability, and I wouldn't buy one without a locking door.</p>
</div></article>
""", "cab-kitchen-clutter-guide.html")

PAGES["cab-organization-zones.html"] = ("Organize Your Cab", "A zone-by-zone system for organizing a truck cab, including the documents that must stay in the cab.", f"""
<article class="article"><div class="wrap">
<p class="eyebrow">How-to</p>
<h1>Organize Your Cab by Zone</h1>
<p class="byline">By Clifford Cruickshank, CDL-A driver · Updated October 2026</p>
<p>Clutter in a cab costs time, and loose items become hazards in a hard stop. The fix is a home for everything, decided by how often you need it and whether you need it while driving.</p>

<h2>Zone 1: Driver's reach</h2>
<p>Only what you need while the truck is moving, and all of it secured.</p>
<ul>
  <li>Phone in a mount. Federal rules prohibit CMV drivers from holding a mobile phone while driving, so set it up for hands-free use.</li>
  <li>Sunglasses, a drink in a holder, toll and fuel cards somewhere you can reach without looking.</li>
  <li>High-protein snacks within reach. You sit for hours, and protein keeps you full longer, which makes it easier to skip the junk at every stop.</li>
</ul>

<h2>Zone 2: Passenger seat and dash</h2>
<p>This is where clutter collects. Give it a container, such as a front-seat organizer, and empty it at every fuel stop. Skip seat-back organizers: with truck seats pushed all the way back, you can't reach them. Paperwork and cards are easier to grab from a visor organizer.</p>

<h2>Zone 3: Paperwork and required documents</h2>
<p>If your truck uses an ELD, FMCSA requires you to keep these in the cab:</p>
<ul>
  <li>The ELD user's manual</li>
  <li>An instruction sheet for transferring ELD records to an officer</li>
  <li>An instruction sheet for reporting ELD malfunctions</li>
  <li>A supply of blank driver's records of duty status graph-grids, enough for at least 8 days</li>
</ul>
<p>Keep them together with your registration, insurance card and bills of lading in one labeled folder or a visor organizer, so you can hand them over quickly at an inspection.</p>

<h2>Zone 4: Sleeper and bunk</h2>
<ul>
  <li>Clothes in soft bags or bins sized to your cabinets.</li>
  <li>Food and the fridge together, so the kitchen is in one place.</li>
  <li>A small trash bag you change daily.</li>
</ul>

<h2>Zone 5: Side storage</h2>
<p>Water, tools, gloves, straps, a tire gauge, a flashlight and anything you use rarely go in the side cabinets. Anything dirty belongs in the outside side boxes, not in your living space.</p>

<h2>Keeping it clean</h2>
<p>My rule is a place for everything and everything in its place. Organizing and cleaning go together, but they're different jobs. Organizing means every item has a home, so nothing piles up. Cleaning is quick because there's less in the way.</p>
<p>My cleaning kit is short: a leaf blower to clear dust and crumbs out of the cab fast, wet wipes, and Amway Home L.O.C. Multi-Purpose Cleaner for the interior surfaces.</p>
<p class="disclosure"><strong>Disclosure:</strong> I'm an independent Amway business owner, so I can earn money from Amway sales. I mention that cleaner because it's what I use.</p>
<p>Gear that helps with each zone is in our <a href="cab-kitchen-clutter-guide.html">gear guide</a>.</p>
</div></article>
""")

PAGES["epu-vs-idling.html"] = ("My EPU Keeps Waking Me Up", "A truck driver's take on factory electric power units, idling and getting real sleep on a 10-hour break.", f"""
<article class="article"><div class="wrap">
<p class="eyebrow">Driver's take</p>
<h1>My EPU Keeps Waking Me Up: A Driver's Take on Electric Power Units vs. Idling</h1>
<p class="byline">By Clifford Cruickshank, CDL-A driver · Updated October 2026</p>
<p>My 2022 Kenworth T680 came with a factory-installed EPU, an electric power unit. On paper it's the right answer to overnight idling. In practice, every two to three hours the truck starts its own engine to recharge the batteries, and that startup jolts me out of my sleep.</p>
<p>A quiet EPU isn't much use if the truck keeps waking you up to recharge it.</p>

<h2>How the system works</h2>
<p>An EPU is a battery-powered system. While the engine is off, the batteries run the cab's power, and air conditioning can be tied into the system as well. When the batteries drop low enough, the truck starts the engine automatically to recharge them, then shuts back down.</p>
<p>I'm not certain of the exact model on my truck, and I haven't timed how long each charging cycle runs. What I do know is how often it happens: roughly every two to three hours, which can mean several wake-ups during a 10-hour break.</p>

<h2>It's not the noise. It's the interruption.</h2>
<p>The problem isn't just sound. It's being pulled out of sleep, over and over, when you're trying to get real rest before another day behind the wheel. Federal hours-of-service rules give property-carrying drivers a 10-hour off-duty break so they can recover. A break broken up every few hours isn't the rest it's supposed to be.</p>
<p>I haven't found any driver-accessible setting that changes how the auto-start works, such as the battery threshold or charging interval. If one exists on my truck, I haven't found it.</p>

<h2>It could be worse</h2>
<p>About a year ago I drove a Freightliner that did the same automatic restarts, with an extra problem: every time the engine started to charge, the air conditioning blasted cold air no matter what temperature I had set. When the engine shut off, the system brought the cab back to my setting. My Kenworth doesn't do that. My only complaint with it is the repeated engine starts.</p>

<h2>So I often idle instead</h2>
<p>My carrier prefers that I don't idle, and I understand why. Idling burns fuel, adds engine wear and raises operating costs. Even so, when it comes down to sleep, I'll idle. A rested driver matters more than a few extra gallons of diesel, and I'm sure my carrier would rather pay for some maintenance than have a tired driver cause a crash.</p>
<p>Idling isn't free, though, and you should know what it costs:</p>
<ul>
  <li><strong>Fuel.</strong> My boss estimates that idling over a seven-day stretch can run about $600 a week in diesel, roughly $86 a day. That's his number, not one I've measured, and your cost depends on your engine, how long you idle and the price of diesel.</li>
  <li><strong>Emissions system wear.</strong> Extended idling can cause problems with the diesel particulate filter (DPF) and other emissions parts, including NOx sensor faults.</li>
  <li><strong>Downtime.</strong> When an emissions repair is needed, the bill isn't only parts and labor. It's also the money you don't make while the truck sits in the shop.</li>
  <li><strong>Local rules.</strong> Many states and cities limit how long a truck may idle. The rules vary by place, so check before you idle overnight somewhere new. The American Transportation Research Institute keeps a <a href="https://truckingresearch.org/" rel="noopener">compendium of state and local idling regulations</a>.</li>
</ul>
<p>You're not alone in this. The U.S. Department of Energy says <a href="https://afdc.energy.gov/conserve/idle_reduction_heavy.html" rel="noopener">more than one million long-haul trucks idle during required rest periods every day</a>.</p>

<h2>What EPUs get right</h2>
<p>To be fair, electric power units have real advantages. They're quiet while running on battery power. They're designed to need less maintenance than diesel-powered APUs. And they cut unnecessary idling, which saves fuel and reduces emissions. My issue isn't with electric power. It's that a system meant to improve life on the road shouldn't keep interrupting the driver's sleep.</p>

<h2>What would change my mind</h2>
<p>Personally, I think diesel-powered APUs are the better solution today. If an electric system could reliably give about 12 hours of standby power without restarting the engine, I'd change my opinion. Until then, I want a system that delivers steady power and comfort without waking me up.</p>

<h2>What I'd tell a new driver with an EPU</h2>
<ul>
  <li><strong>Learn how your truck is set up.</strong> Some carriers program trucks to shut down after only a few minutes of idling. In that case you may not have a choice.</li>
  <li><strong>Pay attention to your sleep.</strong> Some drivers sleep right through the auto-starts. Others, like me, don't.</li>
  <li><strong>Know your carrier's policy</strong> and the idling rules where you park.</li>
  <li><strong>Don't ignore it if it's costing you rest.</strong> If the system is keeping you from adequate sleep, raise it with your carrier or shop. Fatigue is the bigger risk.</li>
</ul>
<p>Have a truck whose EPU lets you sleep through the night? I'd like to hear about it: <strong>contact@triamden.com</strong>.</p>
</div></article>
""", "index.html")

PAGES["how-i-eat-on-the-road.html"] = ("How I Eat on the Road", "How a working truck driver eats on the road: home-cooked meals, a truck microwave and fridge, and a backup plan.", f"""
<article class="article"><div class="wrap">
<p class="eyebrow">Driver's take</p>
<h1>How I Eat on the Road (Without Living on Truck-Stop Food)</h1>
<p class="byline">By Clifford Cruickshank, CDL-A driver · Updated October 2026</p>
<p class="disclosure"><strong>Disclosure:</strong> {DISCLOSURE} This article has no product links, but other pages on this site do.</p>
<p>Truck-stop food is easy, and that's the trap. Two or three meals a day add up fast, in money and in what they do to you. Here's how I actually eat during a week out, including the parts I'm not proud of.</p>

<h2>The home-cooked week</h2>
<p>Before I head out, my wife, Nicole, cooks enough food to last about a week. The rotation includes fried rice or pelau, baked or stewed chicken, baked or stewed pork, macaroni pie, lasagna, chunky vegetables, and sometimes beef and spinach patties.</p>
<p>It's packed in bulk containers, not single portions labeled by day. At mealtime I take out what I want and heat my plate. The goal is a week, but some dishes run out sooner than others.</p>

<h2>My truck kitchen</h2>
<p>Two appliances do the work: the fridge and a microwave.</p>
<ul>
  <li><strong>Fridge.</strong> My 2022 Kenworth T680 came with a built-in refrigerator. If your truck doesn't have one, start with our <a href="12v-fridge-buying-checklist.html">12V fridge buying checklist</a>.</li>
  <li><strong>Microwave.</strong> Not factory-installed. I bought it years ago and it has moved with me from truck to truck. It runs off the truck's inverter. A microwave pulls a lot of power, so check your inverter's rating before you plug one in. No microwave? A <a href="12v-lunch-box-hotlogic-vs-travelisimo.html">12V heated lunch box</a> is the usual alternative.</li>
</ul>
<p>No kettle or coffee maker here. I'm not a hot-drinks person, which is probably to my detriment.</p>

<h2>Keeping it safe</h2>
<p>Different foods keep for different lengths of time, so know what you're putting in the fridge. In my experience the home-cooked food doesn't make it past a week, and anything that sits longer gets a hard look before I eat it.</p>
<p>For the official numbers, USDA guidance is that cooked leftovers keep <a href="https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/leftovers-and-food-safety" rel="noopener">3 to 4 days in a refrigerator at 40°F or below</a>, or 3 to 4 months frozen, and should be reheated to 165°F. That's shorter than a full week out, so if your fridge has a freezer section, freezing the meals you'll eat later in the week is the safer way to make home food last.</p>
<p>I also keep a bag of frozen Birds Eye potatoes as a backup for when the home-cooked meals run out.</p>

<h2>When the home food runs out</h2>
<p>I'm not much of a cook, and at my age I have no plans to change that. So my backup is prepared food that's easy to get:</p>
<ul>
  <li><strong>Walmart rotisserie chicken and potato salad.</strong> Many Walmart locations make room for trucks, so I can park and shop.</li>
  <li><strong>Subway</strong> when I want something different.</li>
</ul>

<h2>Snacks: the honest version</h2>
<p>To stay full between meals I keep protein within reach: Nutrilite Organics Plant Protein Powder in chocolate, and XS Sports Protein Bars in Chocolate Peanut Butter and Chocolate Berry. And I'll admit it: I also eat Doritos. I'm trying to make better choices, but I'm not going to pretend I eat perfectly.</p>
<p class="disclosure"><strong>Disclosure:</strong> Nutrilite and XS are Amway brands. I'm an independent Amway business owner, so I can earn money from Amway sales. I mention these because they're what I actually eat.</p>
<p>The protein matters because you sit for hours. Food that keeps you full longer makes it easier to skip the impulse buys at every fuel stop.</p>

<h2>My advice: don't make truck-stop food your staple</h2>
<p>I'm not saying never buy food at a truck stop. I do it myself when I need to. Just don't live on it. It usually costs more and is often less healthy than food you prepared yourself, and buying two or three meals a day adds up over a year.</p>
<ul>
  <li>Plan ahead and bring meals from home when you can.</li>
  <li>Have a backup for when the home food runs out.</li>
  <li>Keep filling snacks in reach so hunger doesn't make the decision for you.</li>
</ul>
<p>You don't need to give up convenience. You just need to stop depending on it for every meal.</p>
</div></article>
""", "index.html")

PAGES["protein-snacks-for-truck-drivers.html"] = ("Protein Snacks for Drivers", "The protein shakes and bars a working truck driver keeps in the cab, what they cost per week, and how they fit his routine.", f"""
<article class="article"><div class="wrap">
<p class="eyebrow">Driver's take</p>
<h1>The Protein Snacks That Get Me Through a Shift</h1>
<p class="byline">By Clifford Cruickshank, CDL-A driver · Updated October 2026</p>
<p class="disclosure"><strong>Disclosure:</strong> Nutrilite and XS are Amway brands. I'm an independent Amway business owner, so I can earn money when people buy Amway products. That's part of why I use them, and I'll tell you the rest below. This is my own routine, not medical or nutrition advice.</p>
<p>I usually eat one full meal a day, sometimes two. Protein shakes and bars carry me through the rest of a long shift, so I'm not pulling off for another meal or grabbing whatever's by the register.</p>

<h2>What I keep in the cab</h2>
<section class="pick">
  <h3>Nutrilite Organics Plant Protein Powder, Chocolate</h3>
  <p>Two scoops and a bottle of water in a shaker cup. It tastes good enough on its own, but I also carry a mixer so I can blend in fruit, usually blueberries, strawberries or bananas. I drink one or two shakes per shift.</p>
  <p>I've tried other protein powders and found them grainy and unpleasant. This one is smoother and tastes better to me.</p>
  <p><strong>Cab tip:</strong> the original packaging gets messy when you scoop from it on the road. I pour the powder into a wide-mouth storage container and refill it as needed.</p>
</section>
<section class="pick">
  <h3>XS Sports Protein Bars, Chocolate Peanut Butter and Chocolate Berry</h3>
  <p>One of each per shift. I've tried other protein bars and they're okay, but I love these. I can't imagine life on the road without them.</p>
  <p><strong>Cab tip:</strong> heat affects them, especially the Chocolate Peanut Butter. Keep them in the fridge or somewhere cool, not on the dash.</p>
</section>
<p>Why these two? I'll be straight with you: I'm an Amway business owner, so I want to support my own business. But I've tried the alternatives, and these are the ones I actually like.</p>

<h2>What it costs</h2>
<p>At Amway retail prices when I wrote this (October 2026):</p>
<div class="table-wrap"><table>
  <thead><tr><th>Product</th><th>Retail price</th><th>Per serving</th></tr></thead>
  <tbody>
    <tr><td>Nutrilite Chocolate Plant Protein Powder</td><td>$49.50 for 15 servings</td><td>$3.30</td></tr>
    <tr><td>XS Chocolate Peanut Butter bars</td><td>$48.25 for 12</td><td>$4.02</td></tr>
    <tr><td>XS Chocolate Berry bars</td><td>$48.25 for 12</td><td>$4.02</td></tr>
  </tbody>
</table></div>
<p>Two bars plus one or two shakes comes to about <strong>$11.34–$14.64 per shift</strong>, or roughly <strong>$79–$102 for a seven-shift week</strong>.</p>

<h2>How I think about that price</h2>
<p>I don't look at the price of a bar by itself. I compare it to what I'd otherwise spend staying fed through a long shift. Here's a rough comparison, using my own estimates for meal prices:</p>
<div class="table-wrap"><table>
  <thead><tr><th>Instead of protein, I'd buy…</th><th>Per day</th><th>Per week</th><th>My routine saves about</th></tr></thead>
  <tbody>
    <tr><td>Two extra Walmart meals</td><td>$19.94</td><td>$139.58</td><td>$37–$60 a week</td></tr>
    <tr><td>Two extra truck-stop meals</td><td>$24–$36</td><td>$168–$252</td><td>$66–$173 a week</td></tr>
    <tr><td>Two Walmart meals plus $5–$10 of snacks</td><td>$24.94–$29.94</td><td>$174.58–$209.58</td><td>$72–$130 a week</td></tr>
    <tr><td>Two truck-stop meals plus $5–$10 of snacks</td><td>$29–$46</td><td>$203–$322</td><td>$101–$243 a week</td></tr>
  </tbody>
</table></div>
<p>These are what-if numbers, not measured savings. I can't say exactly how many extra meals or snacks I'd buy without the protein. And shakes and bars aren't a replacement for complete meals. They fit into my routine and help me manage my appetite.</p>

<h2>What's changed for me</h2>
<p>I'm on a weight-loss journey, and I've lost over 50 pounds. I changed several things at once: I stopped relying on truck-stop meals, I switched to prepared food from Walmart, and I added protein shakes and bars, which weren't part of my diet before. I also cut out belVita biscuits, which I used to snack on all the time until I realized how fast their calories added up.</p>
<p>I can't credit the weight loss to any single product. It's the overall change that's working, and I'm encouraged by it. Your results will depend on your own habits, and if you're making big diet changes, check with your doctor.</p>

<h2>The honest part</h2>
<p>I still eat Doritos, usually on long stretches of driving. I enjoy them and I'm not going to pretend otherwise. Other things I snack on: peanut butter pretzels, and sometimes bread and cheese from Walmart.</p>
<p>What doesn't work for me: I've tried beef jerky and don't like it, and I'm not a fan of Greek yogurt. If those work for you, great. Find the protein you'll actually eat.</p>

<h2>Downsides</h2>
<p>I haven't found any big ones. The main thing is planning. You don't want to run out of what you rely on halfway through a trip, so pack enough before you leave.</p>

<h2>Where it starts</h2>
<p>None of this works until you decide to change. Nobody can make that decision for you.</p>
<p>Interested in the products I use? Email me at <strong>contact@triamden.com</strong>.</p>
</div></article>
""", "index.html")

PAGES["about.html"] = ("About Cab Gear", "Who writes TriAmden Cab Gear and how products are chosen.", f"""
<section class="ab-hero">
  <div class="ab-hero-media"><img src="about-truck.jpg" alt="A black Kenworth T680 sleeper truck on a highway at sunset. Callout: Gear, organization, food on the road, real solutions." width="974" height="326"></div>
  <div class="wrap ab-hero-copy">
    <img class="ab-logo" src="cabgear-logo.webp" alt="TriAmden Cab Gear" width="1000" height="315">
    <p class="ab-tagline">Real gear. Real miles. Real life.</p>
  </div>
</section>
<section class="ab-body">
  <div class="wrap ab-grid">
    <figure class="ab-photo"><img src="about-clifford.jpg" alt="Clifford Cruickshank, arms crossed, in a TriAmden Transportation polo with his truck behind him" width="532" height="1002"><figcaption class="ab-motto">Built for <span>the long run.</span></figcaption></figure>
    <div class="ab-text">
      <p class="ab-eyebrow">Real Gear. Real Miles. Real Life.</p>
      <h1 class="ab-title">About Cab Gear</h1>
      <p>Life on the road isn't just about driving. It's about making a truck feel like home, staying organized, eating well, getting proper rest, and finding ways to make every mile a little more comfortable.</p>
      <p>I'm Clifford Cruickshank, a long-haul truck driver and founder of the TriAmden Group of Companies.</p>
      <p>My journey didn't begin behind the wheel. I spent over 16 years working in the oil and gas industry in Trinidad and Tobago before moving to the United States in December 2016. In 2017, I began my trucking career with Knight Transportation.</p>
      <p>Since then, I've driven for several carriers, hauling container, refrigerated and dry van freight on OTR and regional routes across the country. Today, my home away from home is a 2022 Kenworth T680 sleeper.</p>
      <p>Over the years, I've learned that the little things make a big difference. A well-organized cab, the right equipment, a decent meal, or something as simple as getting an uninterrupted night's sleep can completely change your experience on the road.</p>
      <p>That's why I created Cab Gear, published by TriAmden Marketing.</p>
      <p>This isn't just another website listing trucking accessories. It's a place to share practical ideas, useful gear, firsthand experiences, and honest opinions about what works, what doesn't, and what could be better.</p>
      <p>From cab organization and food storage to cooking, comfort, and everyday life behind the wheel, the goal is simple: help fellow drivers make smarter choices without wasting time or money.</p>
      <p>I don't claim to have all the answers, and I certainly haven't tried every product out there. But with over a million miles behind the wheel, I've picked up plenty of lessons worth passing along.</p>
      <p class="ab-signoff">No gimmicks. No unnecessary hype. Just real-world trucking experience, one mile at a time.</p>
      <p class="ab-follow">Follow along on the road: <a href="{FB_URL}" target="_blank" rel="noopener me">Facebook</a> · <a href="{IG_URL}" target="_blank" rel="noopener me">Instagram @triamden</a> · <a href="{YT_URL}" target="_blank" rel="noopener me">YouTube</a></p>
    </div>
    <ul class="ab-badges" aria-label="Topics">
      <li><a href="cab-organization-zones.html"><img src="about-badge-org.jpg" alt="Organization" width="190" height="200"></a></li>
      <li><a href="protein-snacks-for-truck-drivers.html"><img src="about-badge-food.jpg" alt="Food on the road" width="210" height="200"></a></li>
      <li><a href="how-i-eat-on-the-road.html"><img src="about-badge-cook.jpg" alt="In-cab cooking" width="200" height="200"></a></li>
      <li><a href="cab-kitchen-clutter-guide.html"><img src="about-badge-guides.jpg" alt="Gear guides" width="200" height="200"></a></li>
    </ul>
  </div>
  <div class="wrap ab-how">
    <h2 class="ab-h2">How we choose products</h2>
    <ul>
      <li>We look for gear that solves a real problem drivers have in the cab.</li>
      <li>We describe products from their listings and published specifications, and we say when something needs checking.</li>
      <li>Every review page says whether I've personally used the product. I only describe hands-on use when I have.</li>
      <li>I'm also an independent Amway business owner. When I mention an Amway product, I say so.</li>
      <li>{"We earn a commission on some purchases, which never changes what you pay." if ASSOCIATE_TAG else "Our Amazon links don't earn commissions yet. When that changes, every page will say so."}</li>
    </ul>
  </div>
</section>
""")

# Disclosure page returns once Amazon approves (ASSOCIATE_TAG set).
if ASSOCIATE_TAG:
  PAGES["affiliate-disclosure.html"] = ("Affiliate Disclosure", "How TriAmden Cab Gear earns money.", f"""
<article class="article"><div class="wrap">
<h1>Affiliate disclosure</h1>
<p><strong>{DISCLOSURE}</strong></p>
{AFFILIATE_PAGE}
<h2>Orders, returns and warranties</h2>
<p>{AMAZON_TERMS}</p>
<p>Separately, Clifford is an independent Amway business owner and can earn money from Amway sales. Any article that mentions an Amway product says so.</p>
<p>Commissions don't decide what we cover. We write about gear we believe is useful to drivers, and we say plainly when we haven't tested something ourselves.</p>
<p>Product prices and availability change. Always check the current price and details on Amazon before you buy.</p>
</div></article>
""")

PAGES["privacy.html"] = ("Privacy Policy", "Privacy policy for TriAmden Cab Gear.", f"""
<article class="article"><div class="wrap">
<h1>Privacy policy</h1>
<p>Effective: October 30, 2026</p>
<h2>What we collect</h2>
<p>We use Google Analytics to understand where visitors come from, which pages they read and how they move around the site. It collects standard information such as pages visited, referring site, approximate location and device type. IP addresses are not stored. We don't sell personal information and we don't run an email list.</p>
<p>You can opt out of Google Analytics on every site with Google's <a href="https://tools.google.com/dlpage/gaoptout" rel="noopener">browser add-on</a>. See <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">how Google uses data from sites that use its services</a>.</p>
<h2>Cookies and third parties</h2>
<p>When you click a link to Amazon, Amazon may set cookies to track the referral, under Amazon's own privacy notice. Our analytics provider may also use cookies.</p>
<h2>Contact</h2>
<p>Questions about this policy: see our <a href="contact.html">contact page</a>.</p>
</div></article>
""")

PAGES["contact.html"] = ("Contact Cab Gear", "How to reach TriAmden Cab Gear.", f"""
<article class="article"><div class="wrap">
<h1>Contact</h1>
<p>Have a gear question, a correction or a product you think drivers should know about?</p>
<p>Email: <strong>contact@triamden.com</strong></p>
</div></article>
""")


def build():
    for d in (SITE, ART):
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d)
    for slug, data in PAGES.items():
        title, desc, body = data[0], data[1], data[2]
        current = data[3] if len(data) > 3 else None
        html = page(slug, title, desc, body, current)
        open(os.path.join(SITE, slug), "w").write(html)
        if slug == "index.html":
            head = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
            head = re.sub(r'<meta charset="utf-8">\s*|<meta name="viewport"[^>]*>\s*', "", head)
            body_ = re.search(r"<body[^>]*>(.*)</body>", html, re.S).group(1)
            open(os.path.join(ART, slug), "w").write(head.strip() + "\n" + body_)
        else:
            open(os.path.join(ART, slug), "w").write(html)
    for d in (SITE, ART):
        shutil.copy(os.path.join(ROOT, "styles.css"), d)
        shutil.copy(os.path.join(ROOT, "hero-truck.jpg"), d)
        shutil.copy(os.path.join(ROOT, "cabgear-logo.webp"), d)
        shutil.copy(os.path.join(ROOT, "visor-organizer.jpg"), d)
        shutil.copy(os.path.join(ROOT, "lunchbox-compare.jpg"), d)
        shutil.copy(os.path.join(ROOT, "cab-zones.jpg"), d)
        shutil.copy(os.path.join(ROOT, "fridge-checklist.jpg"), d)
        shutil.copy(os.path.join(ROOT, "meals-microwave.jpg"), d)
        shutil.copy(os.path.join(ROOT, "protein-snacks.jpg"), d)
        shutil.copy(os.path.join(ROOT, "epu-panel.jpg"), d)
        for f in os.listdir(ROOT):
            if f.startswith("about-") and f.endswith(".jpg"): shutil.copy(os.path.join(ROOT, f), d)
        if os.path.exists(os.path.join(ROOT, "logo.png")): shutil.copy(os.path.join(ROOT, "logo.png"), d)
        shutil.copy(os.path.join(ROOT, "og-default.jpg"), d)
        shutil.copytree(os.path.join(ROOT, "shop"), os.path.join(d, "shop"), dirs_exist_ok=True)
        for fv in ("favicon.ico", "favicon-32.png", "apple-touch-icon.png", "favicon-512.png"): shutil.copy(os.path.join(ROOT, fv), d)
    import datetime
    today = datetime.date.today().isoformat()
    urls = "".join(f"  <url><loc>{BASE + ('' if s == 'index.html' else s)}</loc><lastmod>{today}</lastmod></url>\n" for s in PAGES)
    open(os.path.join(SITE, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    open(os.path.join(SITE, "robots.txt"), "w").write(("User-agent: *\nDisallow: /\n" if DRAFT else "User-agent: *\nAllow: /\n\nSitemap: " + BASE + "sitemap.xml\n"))
    print("built", len(PAGES), "pages")


if __name__ == "__main__":
    build()
