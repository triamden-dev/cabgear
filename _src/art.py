"""Original flat illustrations for TriAmden Cab Gear (drawn in code, no third-party art).
Colors come from CSS classes so they follow the light/dark theme."""

def _svg(inner, label):
    return (f'<svg class="art" viewBox="0 0 320 180" role="img" aria-label="{label}" '
            f'preserveAspectRatio="xMidYMid slice"><rect class="a-bg" width="320" height="180"/>{inner}</svg>')

ART = {}

# Visor organizer: windshield edge + visor with pockets, cards, pen
ART["cab-kitchen-clutter-guide.html"] = _svg("""
<path class="a-glass" d="M0 0h320v70Q160 40 0 70z"/>
<rect class="a-ink" x="70" y="34" width="180" height="96" rx="10"/>
<rect class="a-sign" x="80" y="44" width="160" height="76" rx="6"/>
<rect class="a-paper" x="92" y="54" width="60" height="44" rx="3" transform="rotate(-4 122 76)"/>
<rect class="a-amber" x="162" y="58" width="34" height="22" rx="3"/>
<rect class="a-paper" x="200" y="58" width="30" height="22" rx="3"/>
<rect class="a-amber" x="214" y="40" width="6" height="58" rx="3" transform="rotate(12 217 69)"/>
<rect class="a-ink" x="88" y="100" width="144" height="14" rx="4"/>
<circle class="a-amber" cx="160" cy="150" r="9"/><path class="a-stroke" d="M120 150h80"/>
""", "Illustration of a sun visor organizer holding paperwork and cards")

# 12V lunch boxes with steam and a lightning bolt
ART["12v-lunch-box-hotlogic-vs-travelisimo.html"] = _svg("""
<rect class="a-ink" x="40" y="80" width="105" height="62" rx="12"/><rect class="a-sign" x="48" y="88" width="89" height="20" rx="6"/>
<rect class="a-ink" x="175" y="72" width="105" height="70" rx="12"/><rect class="a-amber" x="183" y="80" width="89" height="22" rx="6"/>
<path class="a-steam" d="M80 66q-8-12 0-24t0-24M105 66q-8-12 0-24t0-24M215 58q-8-12 0-24t0-24M240 58q-8-12 0-24t0-24"/>
<path class="a-amber" d="M162 96l-14 24h12l-6 22 20-30h-12l8-16z"/>
<rect class="a-ink" x="20" y="150" width="280" height="6" rx="3"/>
""", "Illustration of two 12-volt heated lunch boxes with steam")

# Dual-zone fridge with snowflake, lock
ART["12v-fridge-buying-checklist.html"] = _svg("""
<rect class="a-ink" x="85" y="40" width="150" height="112" rx="14"/>
<rect class="a-sign" x="95" y="52" width="62" height="88" rx="8"/>
<rect class="a-amber" x="163" y="52" width="62" height="88" rx="8"/>
<g class="a-snow"><path d="M126 76v40M106 96h40M112 82l28 28M140 82l-28 28"/></g>
<rect class="a-paper" x="178" y="84" width="32" height="26" rx="4"/>
<path class="a-lockring" d="M184 84v-8a10 10 0 0 1 20 0v8"/>
<circle class="a-ink" cx="194" cy="97" r="4"/>
<rect class="a-ink" x="100" y="152" width="20" height="8" rx="2"/><rect class="a-ink" x="200" y="152" width="20" height="8" rx="2"/>
""", "Illustration of a dual-zone 12-volt fridge with a locking door")

# Cab floor plan, five zones
ART["cab-organization-zones.html"] = _svg("""
<rect class="a-ink" x="40" y="22" width="240" height="136" rx="18"/>
<rect class="a-sign" x="52" y="34" width="70" height="52" rx="8"/>
<rect class="a-amber" x="128" y="34" width="70" height="52" rx="8"/>
<rect class="a-paper" x="204" y="34" width="64" height="52" rx="8"/>
<rect class="a-glass2" x="52" y="92" width="216" height="54" rx="8"/>
<g class="a-num"><text x="87" y="68">1</text><text x="163" y="68">2</text><text x="236" y="68">3</text><text x="160" y="126">4</text></g>
<rect class="a-amber" x="282" y="70" width="22" height="40" rx="4"/><text class="a-num2" x="293" y="96">5</text>
""", "Illustration of a truck cab floor plan divided into numbered zones")

# EPU: battery, Zzz, engine spark
ART["epu-vs-idling.html"] = _svg("""
<rect class="a-ink" x="60" y="62" width="120" height="70" rx="10"/><rect class="a-ink" x="180" y="84" width="12" height="26" rx="3"/>
<rect class="a-amber" x="70" y="72" width="22" height="50" rx="4"/><rect class="a-glass2" x="98" y="72" width="22" height="50" rx="4"/><rect class="a-glass2" x="126" y="72" width="22" height="50" rx="4"/><rect class="a-glass2" x="154" y="72" width="16" height="50" rx="4"/>
<g class="a-z"><text x="214" y="70" font-size="34">Z</text><text x="246" y="46" font-size="26">z</text><text x="270" y="28" font-size="20">z</text></g>
<path class="a-amber" d="M238 110l-16 26h13l-7 26 23-34h-14l9-18z"/>
""", "Illustration of a low battery, a sleeping Z, and an engine-start spark")

# Meals: containers, plate, microwave
ART["how-i-eat-on-the-road.html"] = _svg("""
<rect class="a-ink" x="180" y="46" width="110" height="80" rx="10"/><rect class="a-glass2" x="190" y="56" width="66" height="60" rx="6"/>
<circle class="a-amber" cx="272" cy="66" r="5"/><circle class="a-paper" cx="272" cy="84" r="5"/><rect class="a-paper" x="266" y="98" width="12" height="14" rx="2"/>
<ellipse class="a-paper" cx="98" cy="128" rx="70" ry="18"/><ellipse class="a-amber" cx="98" cy="122" rx="46" ry="11"/>
<rect class="a-sign" x="40" y="56" width="56" height="40" rx="8"/><rect class="a-ink" x="40" y="52" width="56" height="10" rx="4"/>
<rect class="a-amber" x="104" y="64" width="50" height="32" rx="8"/><rect class="a-ink" x="104" y="60" width="50" height="9" rx="4"/>
<path class="a-steam" d="M86 104q-6-9 0-18M110 104q-6-9 0-18"/>
""", "Illustration of home-cooked meal containers, a plate and a microwave")

# Protein: shaker bottle + bar
ART["protein-snacks-for-truck-drivers.html"] = _svg("""
<path class="a-ink" d="M96 40h56l-6 112a10 10 0 0 1-10 10h-24a10 10 0 0 1-10-10z"/>
<rect class="a-amber" x="92" y="28" width="64" height="16" rx="5"/><rect class="a-ink" x="114" y="14" width="20" height="16" rx="4"/>
<path class="a-sign" d="M101 96h46l-3 56a6 6 0 0 1-6 6h-28a6 6 0 0 1-6-6z"/>
<g transform="rotate(-14 228 112)"><rect class="a-sign" x="168" y="94" width="124" height="38" rx="8"/><rect class="a-amber" x="196" y="94" width="68" height="38"/></g>
<path class="a-stroke" d="M30 168h260"/>
""", "Illustration of a protein shaker bottle and a protein bar")

# About: steering wheel
ART["about.html"] = _svg("""
<circle class="a-ring" cx="160" cy="92" r="58"/><circle class="a-amber" cx="160" cy="92" r="16"/>
<path class="a-spoke" d="M104 92h40M176 92h40M160 108v42"/>
<rect class="a-sign" x="220" y="128" width="78" height="34" rx="6"/><text class="a-num2" x="259" y="151">CDL-A</text>
""", "Illustration of a truck steering wheel and a CDL-A badge")


def hero_scene():
    """Night highway with an original semi-truck silhouette and moving lane lines."""
    return """
<svg class="hero-scene" viewBox="0 0 1200 420" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1a2b"/><stop offset="1" stop-color="#173a4a"/></linearGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffe9a8" stop-opacity=".55"/><stop offset="1" stop-color="#ffe9a8" stop-opacity="0"/></linearGradient>
  </defs>
  <rect width="1200" height="420" fill="url(#sky)"/>
  <g fill="#fff" opacity=".7"><circle cx="120" cy="60" r="1.6"/><circle cx="260" cy="110" r="1.2"/><circle cx="410" cy="40" r="1.4"/><circle cx="560" cy="90" r="1"/><circle cx="700" cy="50" r="1.5"/><circle cx="820" cy="120" r="1.1"/><circle cx="960" cy="70" r="1.3"/><circle cx="1100" cy="40" r="1.6"/><circle cx="1040" cy="130" r="1"/></g>
  <circle cx="1010" cy="92" r="34" fill="#f4eccf"/><circle cx="1024" cy="84" r="30" fill="#14304a"/>
  <path d="M0 290 Q180 220 360 270 T720 255 T1200 240 V420 H0z" fill="#10283a"/>
  <path d="M0 315 Q240 270 480 300 T960 292 T1200 300 V420 H0z" fill="#0d2131"/>
  <rect y="330" width="1200" height="90" fill="#1b2026"/>
  <rect y="330" width="1200" height="4" fill="#f2b233"/>
  <line class="lane" x1="0" y1="378" x2="1200" y2="378" stroke="#ffffff" stroke-width="5" stroke-dasharray="46 40"/>
  <rect y="414" width="1200" height="4" fill="#ffffff" opacity=".8"/>
  <g transform="translate(380 236)">
    <path d="M520 104 L760 104 L760 112 L520 112z" fill="url(#beam)" transform="translate(-10 -2)"/>
    <rect x="0" y="0" width="330" height="96" rx="4" fill="#d9dee3"/>
    <rect x="0" y="0" width="330" height="10" fill="#0f5e3c"/>
    <text x="165" y="62" text-anchor="middle" font-family="Overpass, Arial Narrow, sans-serif" font-weight="800" font-size="30" fill="#0f5e3c">TRIAMDEN</text>
    <rect x="338" y="10" width="72" height="86" rx="6" fill="#0f5e3c"/>
    <path d="M410 18 h40 q14 0 20 14 l14 36 q4 10 22 12 l12 2 q8 2 8 10 v4 h-116z" fill="#147a4f"/>
    <path d="M418 26 h30 q8 0 11 8 l10 26 h-51z" fill="#9cc7dc"/>
    <rect x="512" y="78" width="10" height="8" rx="2" fill="#ffe9a8"/>
    <rect x="330" y="96" width="200" height="8" fill="#2a3036"/>
    <g fill="#111"><circle cx="40" cy="104" r="16"/><circle cx="76" cy="104" r="16"/><circle cx="270" cy="104" r="16"/><circle cx="306" cy="104" r="16"/><circle cx="372" cy="104" r="16"/><circle cx="476" cy="104" r="16"/></g>
    <g fill="#9aa3ab"><circle cx="40" cy="104" r="6"/><circle cx="76" cy="104" r="6"/><circle cx="270" cy="104" r="6"/><circle cx="306" cy="104" r="6"/><circle cx="372" cy="104" r="6"/><circle cx="476" cy="104" r="6"/></g>
  </g>
</svg>"""


# Photo replacements (supplied by Clifford)
ART["cab-kitchen-clutter-guide.html"] = ('<img class="art art-photo" src="visor-organizer.jpg" '
    'alt="A visor organizer in a truck cab holding paperwork, pens, a charging cable and sunglasses" '
    'width="1448" height="1086" loading="lazy">')

ART["12v-lunch-box-hotlogic-vs-travelisimo.html"] = ('<img class="art art-photo" src="lunchbox-compare.jpg" '
    'alt="A HOTLOGIC Mini heated lunch box beside a TRAVELISIMO electric lunch box at a truck stop" '
    'width="1348" height="698" loading="lazy">')
