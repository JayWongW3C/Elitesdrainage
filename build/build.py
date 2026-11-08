"""Builds the whole website into the public/ folder.

Run from the project folder:   python3 build/build.py
Needs only Python 3 (no extra packages). Images are prepared separately by build/images.py.
"""
import json, os, re, html, datetime
from business import BUSINESS as B, AREAS, NAV
from services import SERVICES, GROUPS, FEATURED

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OUT = os.path.join(ROOT, 'public')
IMG = os.path.join(OUT, 'img')
TODAY = datetime.date.today().isoformat()
SITE = B['url']
PAGES = []  # (path, lastmod, priority) for sitemap
SVC = {s['slug']: s for s in SERVICES}
esc = html.escape

# --------------------------------------------------------------------------- helpers

def img_sizes(name):
    """Return list of (width, file) available for a photo."""
    out = []
    for w in (480, 960, 1600):
        f = f'{name}-{w}.webp'
        if os.path.exists(os.path.join(IMG, f)):
            out.append((w, f))
    return out

def dims(file):
    with open(os.path.join(IMG, file), 'rb') as fh:
        d = fh.read(40)
    # WebP VP8 / VP8L / VP8X header parsing for width/height
    if d[12:16] == b'VP8 ':
        w = int.from_bytes(d[26:28], 'little') & 0x3fff; h = int.from_bytes(d[28:30], 'little') & 0x3fff
    elif d[12:16] == b'VP8L':
        b = int.from_bytes(d[21:25], 'little'); w = (b & 0x3fff) + 1; h = ((b >> 14) & 0x3fff) + 1
    else:  # VP8X
        w = int.from_bytes(d[24:27], 'little') + 1; h = int.from_bytes(d[27:30], 'little') + 1
    return w, h

def picture(name, alt, sizes='(min-width: 960px) 50vw, 100vw', eager=False, cls=''):
    s = img_sizes(name)
    if not s:
        raise SystemExit(f'Missing image {name}')
    srcset = ', '.join(f'/img/{f} {w}w' for w, f in s)
    mid = s[min(1, len(s) - 1)][1]
    w, h = dims(mid)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    return (f'<img{c} src="/img/{mid}" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" '
            f'alt="{esc(alt)}" {load}>')

def tel(text=None, cls='btn btn-call'):
    return f'<a class="{cls}" href="tel:{B["phone_tel"]}">{ICON["phone"]}<span>{text or "Call " + B["phone_display"]}</span></a>'

ICON = {
    'phone': '<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.3 0 .7-.2 1z"/></svg>',
    'mail': '<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M20 4H4a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
    'pin': '<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"/></svg>',
    'clock': '<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 10.4 3.5 2.1-.8 1.3L11 13V7h2z"/></svg>',
    '24': '<svg aria-hidden="true" viewBox="0 0 48 48" width="40" height="40"><circle cx="24" cy="24" r="20" fill="none" stroke="currentColor" stroke-width="3"/><text x="24" y="30" text-anchor="middle" font-size="16" font-weight="700" fill="currentColor" font-family="system-ui,sans-serif">24/7</text></svg>',
    'shield': '<svg aria-hidden="true" viewBox="0 0 24 24" width="40" height="40"><path fill="none" stroke="currentColor" stroke-width="1.6" d="M12 2.5 4 5.5v6c0 5 3.4 8.9 8 10 4.6-1.1 8-5 8-10v-6z"/><path fill="none" stroke="currentColor" stroke-width="1.8" d="m8.5 12 2.5 2.5 4.5-5"/></svg>',
    'quote': '<svg aria-hidden="true" viewBox="0 0 24 24" width="40" height="40"><rect x="5" y="2.5" width="14" height="19" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path stroke="currentColor" stroke-width="1.6" d="M8 7h8M8 11h8M8 15h5"/></svg>',
    'star': '<svg aria-hidden="true" viewBox="0 0 24 24" width="40" height="40"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" d="m12 3 2.7 5.6 6.1.8-4.5 4.2 1.1 6L12 16.8 6.6 19.6l1.1-6L3.2 9.4l6.1-.8z"/></svg>',
    'heart': '<svg aria-hidden="true" viewBox="0 0 24 24" width="40" height="40"><path fill="none" stroke="currentColor" stroke-width="1.6" d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>',
    'check': '<svg aria-hidden="true" viewBox="0 0 24 24" width="40" height="40"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.6"/><path fill="none" stroke="currentColor" stroke-width="1.8" d="m8 12.5 2.8 2.8L16.5 9"/></svg>',
    'camera': '<svg aria-hidden="true" viewBox="0 0 24 24" width="40" height="40"><rect x="2.5" y="6" width="13" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path fill="none" stroke="currentColor" stroke-width="1.6" d="m15.5 10 6-3v10l-6-3"/></svg>',
    'leaf': '<svg aria-hidden="true" viewBox="0 0 24 24" width="40" height="40"><path fill="none" stroke="currentColor" stroke-width="1.6" d="M5 19C5 9 11 4 20 4c0 9-5 15-15 15zm0 0 8-8"/></svg>',
    'jet': '<svg aria-hidden="true" viewBox="0 0 24 24" width="40" height="40"><path fill="none" stroke="currentColor" stroke-width="1.6" d="M2 12h9m0-3v6l4-3zM16 8l5-2M16 12h6M16 16l5 2"/></svg>',
}

# --------------------------------------------------------------------------- schema

ADDRESS = {"@type": "PostalAddress", "addressLocality": B['town'], "addressRegion": B['county'], "addressCountry": "GB"}
if B['street']: ADDRESS['streetAddress'] = B['street']
if B['postcode']: ADDRESS['postalCode'] = B['postcode']

BUSINESS_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "@id": f"{SITE}/#business",
    "name": B['name'],
    "description": "Drainage contractor in Waterlooville, Hampshire: blocked drain clearing, CCTV drain surveys, drain repairs, no-dig relining, drainage installation and specialist systems.",
    "url": f"{SITE}/",
    "telephone": B['phone_tel'],
    "email": B['email'],
    "logo": f"{SITE}/img/elite-drainage-services-logo.png",
    "image": f"{SITE}/img/og-elite-drainage-services.jpg",
    "address": ADDRESS,
    "geo": {"@type": "GeoCoordinates", "latitude": B['lat'], "longitude": B['lng']},
    "areaServed": [{"@type": "City", "name": a['name']} for a in AREAS],
    "knowsAbout": [s['name'] for s in SERVICES],
    "hasOfferCatalog": {
        "@type": "OfferCatalog", "name": "Drainage services",
        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s['name'], "url": f"{SITE}/services/{s['slug']}/"}} for s in SERVICES],
    },
}
if B['open_24_7']:
    BUSINESS_SCHEMA["openingHoursSpecification"] = [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "opens": "00:00", "closes": "23:59"}]

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script>'

def breadcrumb_schema(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(crumbs)]}

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

# --------------------------------------------------------------------------- layout

def header(path):
    links = []
    for name, url in NAV:
        cur = ' aria-current="page"' if (url == path or (url != '/' and path.startswith(url))) else ''
        links.append(f'<li><a href="{url}"{cur}>{name}</a></li>')
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap topbar-in">
<span>{ICON["clock"]} <span class="hide-sm">{esc(B["hours_text"])}</span><span class="show-sm">Open 24/7 for emergencies · <a href="tel:{B["phone_tel"]}">{B["phone_display"]}</a></span></span>
<span class="hide-sm">{ICON["pin"]} Based in {B["town"]}, covering Havant, Portsmouth and South East Hampshire</span>
</div></div>
<header class="site-header"><div class="wrap header-in">
<a class="brand" href="/" aria-label="{B["name"]} home">
<img src="/img/elite-drainage-services-logo-96.webp" srcset="/img/elite-drainage-services-logo-96.webp 1x, /img/elite-drainage-services-logo-192.webp 2x" width="97" height="96" alt="{B["name"]} logo">
<span class="brand-text"><strong>Elite Drainage</strong><small>Services · {B["town"]}</small></span>
</a>
<nav class="nav" aria-label="Main">
<button class="nav-toggle" aria-expanded="false" aria-controls="nav-list"><span class="bars" aria-hidden="true"></span><span class="sr">Menu</span></button>
<ul id="nav-list">{"".join(links)}</ul>
</nav>
<a class="header-phone" href="tel:{B["phone_tel"]}">{ICON["phone"]}<span><small>Call us 24/7</small>{B["phone_display"]}</span></a>
</div></header>'''

def footer():
    svc = ''.join(f'<li><a href="/services/{s["slug"]}/">{esc(s.get("short", s["name"]))}</a></li>' for s in SERVICES)
    areas = ''.join(f'<li><a href="/areas/#{a["name"].lower()}">{a["name"]}</a></li>' for a in AREAS)
    year = datetime.date.today().year
    return f'''<section class="cta-band"><div class="wrap cta-in">
<div><h2>Drain problem? Talk to us now.</h2><p>Free, upfront estimates. {esc(B["hours_text"])}.</p></div>
<div class="cta-btns">{tel()}<a class="btn btn-ghost" href="/contact/">Request a call back</a></div>
</div></section>
<footer class="site-footer"><div class="wrap footer-grid">
<div>
<img src="/img/elite-drainage-services-logo-192.webp" width="97" height="96" alt="" loading="lazy">
<p><strong>{B["name"]}</strong><br>Drainage contractor in {B["town"]}, {B["county"]}.</p>
<ul class="contact-list">
<li>{ICON["phone"]}<a href="tel:{B["phone_tel"]}">{B["phone_display"]}</a></li>
<li>{ICON["mail"]}<a href="mailto:{B["email"]}">{B["email"]}</a></li>
<li>{ICON["pin"]}<span>{(B["street"] + ", ") if B["street"] else ""}{B["town"]}, {B["county"]}{(" " + B["postcode"]) if B["postcode"] else ""}</span></li>
<li>{ICON["clock"]}<span>{esc(B["hours_text"])}</span></li>
</ul>
</div>
<div><h2>Services</h2><ul>{svc}</ul></div>
<div><h2>Areas we cover</h2><ul>{areas}</ul></div>
<div><h2>Company</h2><ul><li><a href="/about/">About us</a></li><li><a href="/blog/">Blog</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy/">Privacy policy</a></li><li><a href="/legal/">Legal notice</a></li></ul></div>
</div>
<div class="wrap footer-base"><p>© {year} {B["name"]}. All rights reserved.</p></div>
</footer>
<div class="mobile-bar">{tel("Call now", "mb-call")}<a class="mb-quote" href="/contact/">Free estimate</a></div>
<script src="/js/site.js" defer></script>'''

def page(path, title, meta, body, schema=(), crumbs=None, og_image=None, og_type='website', priority='0.7', noindex=False):
    canonical = SITE + path
    og_img = og_image or f'{SITE}/img/og-elite-drainage-services.jpg'
    bc = ''
    schemas = [BUSINESS_SCHEMA] + list(schema)
    if crumbs:
        schemas.append(breadcrumb_schema(crumbs))
        items = []
        for i, (n, u) in enumerate(crumbs):
            items.append(f'<li><a href="{u}">{esc(n)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{esc(n)}</li>')
        bc = f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'
    robots = '<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    doc = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta)}">
{robots}
<link rel="canonical" href="{canonical}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0a1f44">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{B["name"]}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(meta)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="GB-HAM">
<meta name="geo.placename" content="{B["town"]}">
<meta name="geo.position" content="{B["lat"]};{B["lng"]}">
<link rel="stylesheet" href="/css/style.css">
{"".join(ld(s) for s in schemas)}
</head>
<body>
{header(path)}
{bc}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
    out = os.path.join(OUT, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(OUT, path.strip('/'))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(doc)
    if not noindex:
        PAGES.append((path, priority))

# --------------------------------------------------------------------------- shared blocks

def service_cards(slugs, heading_level='h3'):
    cards = []
    for slug in slugs:
        s = SVC[slug]
        cards.append(f'''<article class="card">
<a class="card-img" href="/services/{slug}/" tabindex="-1" aria-hidden="true">{picture(s["images"][0], s["name"], "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}</a>
<div class="card-body"><{heading_level}><a href="/services/{slug}/">{esc(s["name"])}</a></{heading_level}>
<p>{esc(s["card"])}</p>
<a class="more" href="/services/{slug}/">{esc(s.get("short", s["name"]))} details<span aria-hidden="true"> →</span></a></div>
</article>''')
    return '<div class="cards">' + ''.join(cards) + '</div>'

WHY = [
    ('24', 'Round-the-clock service', 'We are always prepared to deal with emergency drainage problems, day or night.'),
    ('shield', 'Licensed and insured', 'Our team is fully licensed and insured, including public liability insurance, for every job we take on.'),
    ('quote', 'Free, transparent estimates', 'Upfront, no-obligation prices with no hidden costs, so you can budget without surprises.'),
    ('star', 'Over 30 years’ experience', 'Our founders have decades of drainage experience behind every job.'),
    ('check', 'Fixed first time', 'We aim to find the cause and fix it correctly on the first visit.'),
    ('heart', 'Discounts for seniors', 'We offer a discount for senior customers. Ask for details when you call.'),
]

def why_grid():
    return '<div class="why">' + ''.join(
        f'<div class="why-item"><span class="why-ic">{ICON[i]}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in WHY) + '</div>'

def faq_block(faqs, heading='Frequently asked questions'):
    items = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faqs)
    return f'<section class="faq"><h2>{heading}</h2>{items}</section>'

def contact_form(compact=False):
    opts = ''.join(f'<option>{esc(s["name"])}</option>' for s in SERVICES)
    return f'''<form class="form{' form-compact' if compact else ''}" name="contact" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="company">
<input type="hidden" name="form-name" value="contact">
<p class="hp"><label>Leave this empty <input name="company" tabindex="-1" autocomplete="off"></label></p>
<div class="row2">
<label>Your name<input name="name" autocomplete="name" required></label>
<label>Phone number<input name="phone" type="tel" autocomplete="tel" required></label>
</div>
<div class="row2">
<label>Email<input name="email" type="email" autocomplete="email"></label>
<label>Postcode<input name="postcode" autocomplete="postal-code" placeholder="e.g. PO7"></label>
</div>
<label>What do you need?<select name="service"><option value="">Choose a service (optional)</option>{opts}<option>Something else</option></select></label>
<label>Tell us about the problem<textarea name="message" rows="{3 if compact else 5}" required></textarea></label>
<p class="small">We only use your details to reply to your enquiry. See our <a href="/privacy/">privacy policy</a>.</p>
<button class="btn btn-primary" type="submit">Send enquiry</button>
</form>'''

def area_strip():
    return '<ul class="area-pills">' + ''.join(f'<li><a href="/areas/#{a["name"].lower()}">{a["name"]}</a></li>' for a in AREAS) + '</ul>'

# --------------------------------------------------------------------------- pages

def build_home():
    gallery = [
        ('drain-jetting-machine-blocked-drain-patio', 'High-pressure drain jetting machine set up on a patio'),
        ('cctv-drain-survey-monitor-at-manhole', 'CCTV drain survey camera and monitor at an inspection chamber'),
        ('no-dig-patch-liner-drain-repair', 'No-dig patch liner repair inside a drain pipe'),
        ('mini-digger-drainage-installation-garden', 'Mini digger excavating a trench for new drainage in a garden'),
        ('channel-drain-in-block-paving', 'Channel drain installed in block paving'),
        ('tanker-emptying-septic-tank', 'Tanker crew lifting a manhole cover to empty a tank'),
    ]
    g = ''.join(f'<figure>{picture(n, a, "(min-width: 960px) 33vw, 50vw")}<figcaption>{esc(a)}</figcaption></figure>' for n, a in gallery)
    body = f'''<section class="hero">
<div class="hero-bg">{picture("drainage-team-lifting-manhole-cover-tanker", "Elite Drainage Services team lifting a manhole cover beside a tanker", "100vw", eager=True)}</div>
<div class="wrap hero-in">
<p class="eyebrow">Drainage contractor in {B["town"]}, Hampshire</p>
<h1>Blocked Drains and Drainage Services in Waterlooville</h1>
<p class="slogan">Unclogging your troubles, one drain at a time.</p>
<p class="lead">Blocked drain clearing, CCTV drain surveys, drain repairs and installations across Waterlooville, Havant, Portsmouth and South East Hampshire. Available 24/7, with free upfront estimates.</p>
<div class="hero-btns">{tel()}<a class="btn btn-ghost" href="/contact/">Get a free estimate</a></div>
<ul class="hero-points"><li>24/7 emergency call-outs</li><li>Licensed and insured</li><li>Over 30 years' experience</li></ul>
</div>
</section>

<section class="section wrap intro">
<div class="intro-text">
<h2>Pioneers of seamless drain solutions</h2>
<p>Welcome to Elite Drainage Services, serving Waterlooville and the South of England with care and expertise. We specialise in solving drainage problems effectively and efficiently, offering services tailored to each property in areas including Waterlooville, Havant and Portsmouth.</p>
<p>We use modern technology, including CCTV inspection cameras, high-pressure water jetting and no-dig repair techniques, to give reliable results with minimal disruption. Our pricing is transparent and we prioritise environmentally responsible methods.</p>
<p><a class="btn btn-primary" href="/services/">Browse all services</a></p>
</div>
<div class="intro-img">{picture("drainage-engineers-at-open-manhole", "Drainage engineers inspecting an open manhole")}</div>
</section>

<section class="section alt"><div class="wrap">
<h2 class="center">Our main drainage services</h2>
<p class="center sub">From a blocked sink to a collapsed sewer, we handle drainage for homes, landlords and businesses.</p>
{service_cards(FEATURED + ["homebuyer-drain-survey", "drain-cleaning", "drainage-installation"])}
<p class="center"><a class="btn btn-outline" href="/services/">See all 11 services</a></p>
</div></section>

<section class="section wrap">
<h2 class="center">Why choose Elite Drainage Services</h2>
<p class="center sub">Professional drainage services built on experience, reliability and a straightforward approach.</p>
{why_grid()}
</section>

<section class="section alt"><div class="wrap split">
<div>
<h2>Homebuyer drain surveys for £299</h2>
<p>Moving home? Do not invest in your biggest purchase without checking what is under the ground. Our full HD CCTV drain survey inspects the whole drainage system and gives you a written report before you commit, so you can negotiate or walk away if there is a problem.</p>
<p><a class="btn btn-primary" href="/services/homebuyer-drain-survey/">About the homebuyer survey</a></p>
</div>
<div>{picture("cctv-drain-camera-screen-pipe-view", "CCTV drain camera screen showing the inside of a pipe")}</div>
</div></section>

<section class="section wrap">
<h2 class="center">Drainage work we carry out</h2>
<div class="gallery">{g}</div>
</section>

<section class="section alt"><div class="wrap">
<h2 class="center">Areas we cover</h2>
<p class="center sub">Based in {B["town"]}, we cover the PO7, PO8 and PO9 postcodes, Portsmouth and the surrounding towns and villages.</p>
{area_strip()}
<p class="center"><a href="/areas/">See all areas we cover</a></p>
</div></section>

<section class="section wrap split">
<div>
<h2>Get a free estimate</h2>
<p>Tell us what is happening and we will get back to you. For emergencies, please call us on <a href="tel:{B["phone_tel"]}">{B["phone_display"]}</a>.</p>
<h3>Discover our story</h3>
<p>Founded by two experienced drainage professionals, Elite Drainage Services brings over three decades of know-how to every job. <a href="/about/">Read about us</a>.</p>
</div>
{contact_form(compact=True)}
</section>'''
    faqs = [
        ("Do you offer a 24-hour emergency drainage service?", "Yes. We are available round the clock for emergency drainage problems such as blocked toilets, overflowing manholes and sewage backing up. Call 0330 633 0336."),
        ("Which areas do you cover?", "We are based in Waterlooville and cover Cowplain, Purbrook, Denmead, Horndean, Havant, Portsmouth and the surrounding areas of South East Hampshire."),
        ("Do you charge for estimates?", "No. Our estimates are free and upfront, so you know the price before any work starts."),
        ("Are you insured?", "Yes. Our team is fully licensed and insured, including public liability insurance."),
    ]
    body += f'<div class="wrap">{faq_block(faqs)}</div>'
    page('/', 'Blocked Drains & Drainage Services Waterlooville | Elite Drainage',
         'Elite Drainage Services: blocked drains, CCTV drain surveys, drain repairs and installations in Waterlooville, Havant and Portsmouth. 24/7, free estimates. Call 0330 633 0336.',
         body, schema=[faq_schema(faqs), {"@context": "https://schema.org", "@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": B['name'], "publisher": {"@id": f"{SITE}/#business"}}],
         priority='1.0')

def build_services_hub():
    groups = ''
    for g in GROUPS:
        slugs = [s['slug'] for s in SERVICES if s['group'] == g]
        groups += f'<h2>{g}</h2>{service_cards(slugs)}'
    body = f'''<section class="page-head"><div class="wrap">
<h1>Drainage Services in Waterlooville and Hampshire</h1>
<p class="lead">Every drainage service your home or business needs, from emergency unblocking to CCTV surveys, no-dig repairs and new installations.</p>
<div class="hero-btns">{tel()}<a class="btn btn-ghost" href="/contact/">Get a free estimate</a></div>
</div></section>
<section class="section wrap">
<div class="callout">
<h2>Homebuyer surveys: a must for all movers</h2>
<p>Are you moving home? For just £299 our full HD CCTV homebuyer drain survey inspects the whole drainage system before you buy, and could save you thousands. <a href="/services/homebuyer-drain-survey/">Find out more</a>.</p>
</div>
{groups}
</section>
<section class="section alt"><div class="wrap">
<h2 class="center">The technology we use</h2>
<p class="center sub">Modern diagnostic and repair technology, including CCTV inspections, no-dig solutions and high-pressure jetting, for accurate results with minimal disruption.</p>
<div class="why">
<div class="why-item"><span class="why-ic">{ICON["camera"]}</span><h3>CCTV diagnostics and reporting</h3><p>High-resolution CCTV gives a thorough inspection and a precise condition report, so problems are diagnosed accurately and fixed cost-effectively from the first visit.</p></div>
<div class="why-item"><span class="why-ic">{ICON["leaf"]}</span><h3>No-dig repair technology</h3><p>CiPP lining and patch repairs restore damaged pipes from the inside, cutting disruption and cost without traditional excavation.</p></div>
<div class="why-item"><span class="why-ic">{ICON["jet"]}</span><h3>High-pressure jetting</h3><p>Water jetting clears even the toughest blockages, restores flow and extends the life of your drainage system.</p></div>
</div>
</div></section>'''
    page('/services/', 'Drainage Services Waterlooville | Elite Drainage Services',
         'All drainage services in Waterlooville and Hampshire: blocked drains, drain cleaning, CCTV surveys, drain repair, installation, sewer, stormwater, septic tanks and pump stations.',
         body, crumbs=[('Home', '/'), ('Services', '/services/')], priority='0.9')

def build_service(s):
    imgs = s['images']
    sections = ''.join(f'<section><h2>{esc(h)}</h2>{c}</section>' for h, c in s['sections'])
    intro = ''.join(f'<p>{esc(p)}</p>' for p in s['intro'])
    others = [x['slug'] for x in SERVICES if x['slug'] != s['slug'] and x['group'] == s['group']][:3]
    side_links = ''.join(f'<li><a href="/services/{x["slug"]}/"{" aria-current=page" if x["slug"] == s["slug"] else ""}>{esc(x.get("short", x["name"]))}</a></li>' for x in SERVICES)
    extra_imgs = ''.join(f'<figure>{picture(n, s["name"] + " – " + n.replace("-", " "), "(min-width: 960px) 30vw, 100vw")}</figure>' for n in imgs[1:3])
    body = f'''<section class="page-head"><div class="wrap">
<p class="eyebrow">{esc(s["group"])}</p>
<h1>{esc(s["h1"])}</h1>
<div class="hero-btns">{tel()}<a class="btn btn-ghost" href="/contact/">Get a free estimate</a></div>
</div></section>
<div class="wrap content-grid section">
<article class="prose">
<figure class="lead-img">{picture(imgs[0], s["name"] + " by Elite Drainage Services", "(min-width: 960px) 66vw, 100vw", eager=True)}</figure>
{intro}
{sections}
<section><h2>Areas we cover for {esc(s.get("short", s["name"]).lower())}</h2>
<p>We provide {esc(s.get("short", s["name"]).lower())} across {", ".join(a["name"] for a in AREAS[:-1])} and {AREAS[-1]["name"]}.</p>
{area_strip()}</section>
{faq_block(s["faqs"])}
{('<div class="gallery two">' + extra_imgs + '</div>') if extra_imgs else ''}
</article>
<aside class="sidebar">
<div class="side-box side-cta"><h2>Need help now?</h2><p>{esc(B["hours_text"])}. Free, upfront estimates.</p>{tel()}<a class="btn btn-outline" href="/contact/">Send an enquiry</a></div>
<div class="side-box"><h2>Our services</h2><ul class="side-links">{side_links}</ul></div>
</aside>
</div>
<section class="section alt"><div class="wrap"><h2 class="center">Other ways we can help</h2>{service_cards(others)}</div></section>'''
    service_schema = {"@context": "https://schema.org", "@type": "Service", "name": s['name'], "serviceType": s['name'],
                      "description": s['meta'], "url": f"{SITE}/services/{s['slug']}/",
                      "provider": {"@id": f"{SITE}/#business"},
                      "areaServed": [{"@type": "City", "name": a['name']} for a in AREAS],
                      "image": f"{SITE}/img/{img_sizes(imgs[0])[-1][1]}"}
    if s['slug'] == 'homebuyer-drain-survey':
        service_schema['offers'] = {"@type": "Offer", "price": "299", "priceCurrency": "GBP"}
    page(f'/services/{s["slug"]}/', s['title'], s['meta'], body,
         schema=[service_schema, faq_schema(s['faqs'])],
         crumbs=[('Home', '/'), ('Services', '/services/'), (s.get('short', s['name']), f'/services/{s["slug"]}/')],
         og_image=f"{SITE}/img/{img_sizes(imgs[0])[-1][1]}", priority='0.8')

def build_areas():
    blocks = ''.join(f'''<section class="area" id="{a["name"].lower()}">
<h2>Drainage services in {a["name"]} <span class="pc">{a["postcodes"]}</span></h2>
<p>{esc(a["text"])}</p>
<p>Services in {a["name"]} include <a href="/services/blocked-drain-clearing/">blocked drain clearing</a>, <a href="/services/cctv-drain-inspection/">CCTV drain surveys</a>, <a href="/services/drain-repair/">drain repairs</a> and <a href="/services/homebuyer-drain-survey/">homebuyer drain surveys</a>.</p>
</section>''' for a in AREAS)
    body = f'''<section class="page-head"><div class="wrap">
<h1>Areas We Cover: Waterlooville, Havant, Portsmouth and Nearby</h1>
<p class="lead">Elite Drainage Services is based in {B["town"]} and covers South East Hampshire. If your town is not listed, call us; we may still be able to help.</p>
<div class="hero-btns">{tel()}</div>
</div></section>
<div class="wrap section areas-grid">
<div>{blocks}</div>
<aside class="sidebar"><div class="side-box side-cta"><h2>Check we cover you</h2><p>Call or send us your postcode.</p>{tel()}<a class="btn btn-outline" href="/contact/">Send an enquiry</a></div></aside>
</div>'''
    page('/areas/', 'Drainage Services Waterlooville, Havant, Portsmouth | Areas',
         'Elite Drainage Services covers Waterlooville, Cowplain, Purbrook, Denmead, Horndean, Havant and Portsmouth (PO1 to PO9). Blocked drains, CCTV surveys and repairs.',
         body, crumbs=[('Home', '/'), ('Areas we cover', '/areas/')], priority='0.8')

def build_about():
    body = f'''<section class="page-head"><div class="wrap">
<h1>About Elite Drainage Services</h1>
<p class="lead">A drainage contractor in {B["town"]}, founded by two experienced colleagues with over 30 years in the trade.</p>
</div></section>
<div class="wrap section split">
<div class="prose">
<h2>Exceptional drainage services in Waterlooville</h2>
<p>Elite Drainage Services is a drainage contractor based in Waterlooville. We offer everything from unblocking and CCTV inspections to repairs and new installations, so your property stays protected. Our experienced technicians deliver quality work backed by a satisfaction guarantee. Call us on <a href="tel:{B["phone_tel"]}">{B["phone_display"]}</a> for reliable drainage expertise.</p>
<h2>Our story</h2>
<p>Elite Drainage Services was founded by two seasoned colleagues who combined decades of experience to offer careful, trusted drainage work. By refining what they had learned over their careers, they created a service focused on reliability and value for money. Our story is one of dedication and continuous learning, and we bring that experience to every job.</p>
<h2>Committed to customer satisfaction</h2>
<p>We keep pricing transparent and aim to solve the problem on the first visit. We use no-dig technology and environmentally responsible methods wherever possible, and we treat every home and business with care.</p>
</div>
<div>{picture("drainage-engineer-arriving-at-customer-home", "Drainage engineer arriving at a customer's home")}</div>
</div>
<section class="section alt"><div class="wrap">
<h2 class="center">The principles that drive us</h2>
<p class="center sub">Ethical standards, quality service and environmental responsibility.</p>
<div class="why">
<div class="why-item"><span class="why-ic">{ICON["star"]}</span><h3>Commitment to excellence</h3><p>With over 30 years' experience, we bring precision and care to every drainage job.</p></div>
<div class="why-item"><span class="why-ic">{ICON["leaf"]}</span><h3>Environmental responsibility</h3><p>Our eco-conscious techniques, such as no-dig repairs, keep environmental impact to a minimum.</p></div>
<div class="why-item"><span class="why-ic">{ICON["quote"]}</span><h3>Transparency and trust</h3><p>Transparent pricing with no hidden costs, so you know exactly what to expect from the start.</p></div>
</div></div></section>
<section class="section wrap"><h2 class="center">Why customers choose us</h2>{why_grid()}</section>'''
    page('/about/', 'About Us | Elite Drainage Services, Waterlooville',
         'Elite Drainage Services is a licensed, insured drainage contractor in Waterlooville, founded by two engineers with over 30 years of drainage experience.',
         body, crumbs=[('Home', '/'), ('About us', '/about/')])

def build_contact():
    body = f'''<section class="page-head"><div class="wrap">
<h1>Contact Elite Drainage Services</h1>
<p class="lead">Get expert help with your drainage problem. Call us for emergencies, or send a message and we will get back to you.</p>
</div></section>
<div class="wrap section split contact">
<div>
<h2>Call or email</h2>
<ul class="contact-list big">
<li>{ICON["phone"]}<span><strong>Phone</strong><br><a href="tel:{B["phone_tel"]}">{B["phone_display"]}</a></span></li>
<li>{ICON["mail"]}<span><strong>Email</strong><br><a href="mailto:{B["email"]}">{B["email"]}</a></span></li>
<li>{ICON["pin"]}<span><strong>Location</strong><br>{(B["street"] + ", ") if B["street"] else ""}{B["town"]}, {B["county"]}{(" " + B["postcode"]) if B["postcode"] else ""}</span></li>
<li>{ICON["clock"]}<span><strong>Hours</strong><br>{esc(B["hours_text"])}</span></li>
</ul>
<h2>Areas we cover</h2>
{area_strip()}
</div>
<div><h2>Send us a message</h2>{contact_form()}</div>
</div>'''
    page('/contact/', 'Contact Us | Elite Drainage Services Waterlooville | 0330 633 0336',
         'Contact Elite Drainage Services in Waterlooville. Call 0330 633 0336, 24/7, or send an enquiry for a free estimate on blocked drains, CCTV surveys and repairs.',
         body, crumbs=[('Home', '/'), ('Contact', '/contact/')], priority='0.8')

POSTS = [
    {"slug": "how-cctv-drain-inspections-prevent-costly-repairs",
     "title": "How CCTV Drain Inspections Prevent Costly Repairs",
     "meta": "How a CCTV drain inspection works, what it finds, and how a drain condition report helps you avoid expensive repairs. From Elite Drainage Services, Waterlooville.",
     "date": "2026-01-02", "image": "cctv-drain-camera-screen-pipe-view", "image_alt": "CCTV drain camera view inside a pipe",
     "headings": {0: "How a CCTV drain inspection works", 1: "Why early detection saves money", 2: "An example: root ingress found early", 6: "Putting it into practice"},
     "related": ["cctv-drain-inspection", "homebuyer-drain-survey", "drain-repair"]},
    {"slug": "no-dig-drain-repairs-faster-fixes-with-less-disruption",
     "title": "No-Dig Drain Repairs: Faster Fixes With Less Disruption",
     "meta": "How no-dig drain repairs work: CiPP lining and patch repairs fix cracked and leaking drains without digging up your garden or driveway. Elite Drainage Services.",
     "date": "2026-01-16", "image": "no-dig-patch-liner-drain-repair", "image_alt": "No-dig patch liner inside a drain pipe",
     "headings": {0: "What is trenchless (no-dig) drain repair?", 1: "Advantages of CiPP lining", 2: "Environmental benefits", 6: "Why no-dig repairs are increasingly preferred"},
     "related": ["drain-repair", "cctv-drain-inspection", "drain-cleaning"]},
]

def clean_post_text(t):
    t = t.replace('[email protected]', B['email'])
    t = re.sub(r'\b0?330 633 0336\b', B['phone_display'], t)
    t = t.replace(' .', '.').replace(' ,', ',').replace('—let’s', '. Let’s')
    return t

def fmt_date(d):
    return datetime.date.fromisoformat(d).strftime('%-d %B %Y')

def build_blog():
    src = json.load(open(os.path.join(os.path.dirname(__file__), 'blog_source.json'), encoding='utf-8'))
    cards = ''
    for p in POSTS:
        items = src[p['slug']]
        paras, html_parts, pi = [], [], 0
        for tag, text in items:
            text = clean_post_text(text)
            if tag in ('h2', 'h3'):
                html_parts.append(f'<h2>{esc(text)}</h2>')
                continue
            if pi in p['headings']:
                html_parts.append(f'<h2>{esc(p["headings"][pi])}</h2>')
            html_parts.append(f'<p>{esc(text)}</p>')
            paras.append(text); pi += 1
        # Link service names in the text to the service pages
        body_html = '\n'.join(html_parts)
        for phrase, url in [('CCTV drain inspections', '/services/cctv-drain-inspection/'), ('drain patch repairs', '/services/drain-repair/'),
                            ('Elite Drainage Services', '/about/'), ('drainage diagnostics', '/services/cctv-drain-inspection/')]:
            body_html = body_html.replace(phrase, f'<a href="{url}">{phrase}</a>', 1)
        rel = service_cards(p['related'])
        body = f'''<article class="wrap section post">
<header class="post-head">
<p class="eyebrow"><time datetime="{p["date"]}">{fmt_date(p["date"])}</time> · Elite Drainage Services</p>
<h1>{esc(p["title"])}</h1>
</header>
<figure class="lead-img">{picture(p["image"], p["image_alt"], "(min-width: 960px) 800px, 100vw", eager=True)}</figure>
<div class="prose">{body_html}</div>
<div class="callout"><h2>Need advice on your drains?</h2><p>Call <a href="tel:{B["phone_tel"]}">{B["phone_display"]}</a> or <a href="/contact/">send us a message</a> for a free estimate.</p></div>
</article>
<section class="section alt"><div class="wrap"><h2 class="center">Related services</h2>{rel}</div></section>'''
        img = f"{SITE}/img/{img_sizes(p['image'])[-1][1]}"
        art = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p['title'], "description": p['meta'],
               "datePublished": p['date'], "dateModified": p['date'], "image": img,
               "author": {"@type": "Organization", "name": B['name'], "url": f"{SITE}/"},
               "publisher": {"@id": f"{SITE}/#business"}, "mainEntityOfPage": f"{SITE}/blog/{p['slug']}/"}
        page(f'/blog/{p["slug"]}/', p['title'] + ' | Elite Drainage', p['meta'], body, schema=[art],
             crumbs=[('Home', '/'), ('Blog', '/blog/'), (p['title'], f'/blog/{p["slug"]}/')], og_image=img, og_type='article', priority='0.6')
        excerpt = paras[0][:220].rsplit(' ', 1)[0] + '…'
        cards += f'''<article class="card">
<a class="card-img" href="/blog/{p["slug"]}/" tabindex="-1" aria-hidden="true">{picture(p["image"], p["image_alt"], "(min-width: 960px) 50vw, 100vw")}</a>
<div class="card-body"><p class="eyebrow"><time datetime="{p["date"]}">{fmt_date(p["date"])}</time></p><h2><a href="/blog/{p["slug"]}/">{esc(p["title"])}</a></h2><p>{esc(excerpt)}</p><a class="more" href="/blog/{p["slug"]}/">Read the article<span aria-hidden="true"> →</span></a></div>
</article>'''
    body = f'''<section class="page-head"><div class="wrap"><h1>Drainage Advice and News</h1>
<p class="lead">Practical guides on drain problems, surveys and repairs from the Elite Drainage Services team.</p></div></section>
<section class="section wrap"><div class="cards two">{cards}</div></section>'''
    page('/blog/', 'Drainage Advice Blog | Elite Drainage Services',
         'Drainage advice from Elite Drainage Services in Waterlooville: CCTV drain inspections, no-dig repairs and how to avoid costly drain problems.',
         body, crumbs=[('Home', '/'), ('Blog', '/blog/')], priority='0.6')

def build_legal():
    addr = f'{(B["street"] + ", ") if B["street"] else ""}{B["town"]}, {B["county"]}{(" " + B["postcode"]) if B["postcode"] else ""}, United Kingdom'
    body = f'''<section class="page-head"><div class="wrap"><h1>Legal Notice</h1></div></section>
<div class="wrap section prose">
<table class="kv"><tbody>
<tr><th>Business name</th><td>{B["name"]}</td></tr>
<tr><th>Address</th><td>{addr}</td></tr>
<tr><th>Phone</th><td><a href="tel:{B["phone_tel"]}">{B["phone_display"]}</a></td></tr>
<tr><th>Email</th><td><a href="mailto:{B["email"]}">{B["email"]}</a></td></tr>
</tbody></table>
<h2>Payment</h2><p>Payment methods accepted will be confirmed with your quote.</p>
<p>See also our <a href="/privacy/">privacy policy</a>.</p>
</div>'''
    page('/legal/', 'Legal Notice | Elite Drainage Services', f'Legal and company information for {B["name"]}, {B["town"]}.', body,
         crumbs=[('Home', '/'), ('Legal notice', '/legal/')], priority='0.2')
    body = f'''<section class="page-head"><div class="wrap"><h1>Privacy Policy</h1></div></section>
<div class="wrap section prose">
<p>This policy explains how {B["name"]} ("we", "us") uses personal information collected through this website. Last updated {fmt_date(TODAY)}.</p>
<h2>Who we are</h2><p>{B["name"]}, {B["town"]}, {B["county"]}. Contact: <a href="mailto:{B["email"]}">{B["email"]}</a>, {B["phone_display"]}.</p>
<h2>What we collect</h2><p>When you send an enquiry we collect the details you give us: your name, phone number, email address, postcode and a description of your drainage problem.</p>
<h2>Why we use it</h2><p>We use these details only to reply to your enquiry, give you a quote and carry out any work you ask us to do. Our lawful basis is taking steps at your request before entering into a contract, and our legitimate interest in responding to enquiries.</p>
<h2>Who we share it with</h2><p>We do not sell your information. Enquiry forms are processed by our website host (Netlify, Inc.) so that the message can be delivered to us. We may share details with a subcontractor only where needed to carry out your job.</p>
<h2>How long we keep it</h2><p>Enquiries that do not lead to work are deleted within 12 months. Records of work carried out are kept for as long as needed for guarantees, accounting and legal purposes.</p>
<h2>Cookies</h2><p>This website does not use advertising or tracking cookies.</p>
<h2>Your rights</h2><p>You can ask to see, correct or delete the personal information we hold about you by contacting us using the details above. You also have the right to complain to the Information Commissioner's Office (ico.org.uk).</p>
</div>'''
    page('/privacy/', 'Privacy Policy | Elite Drainage Services', f'How {B["name"]} uses the personal information you send through this website.', body,
         crumbs=[('Home', '/'), ('Privacy policy', '/privacy/')], priority='0.2')

def build_utility():
    page('/thank-you/', 'Thank You | Elite Drainage Services', 'Your enquiry has been sent.', f'''<section class="page-head"><div class="wrap">
<h1>Thank you, your message has been sent</h1>
<p class="lead">We will get back to you as soon as possible. If it is an emergency, please call us now.</p>
<div class="hero-btns">{tel()}<a class="btn btn-ghost" href="/">Back to the home page</a></div></div></section>''', noindex=True)
    page('/404.html', 'Page Not Found | Elite Drainage Services', 'This page could not be found.', f'''<section class="page-head"><div class="wrap">
<h1>Sorry, we cannot find that page</h1>
<p class="lead">It may have moved when we updated our website. Try one of these:</p>
<div class="hero-btns"><a class="btn btn-ghost" href="/services/">Our services</a><a class="btn btn-ghost" href="/contact/">Contact us</a>{tel()}</div></div></section>''', noindex=True)

# --------------------------------------------------------------------------- SEO files

def build_seo_files():
    urls = ''.join(f'<url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n' for p, pr in PAGES)
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nDisallow: /thank-you/\n\nSitemap: {SITE}/sitemap.xml\n')
    # 301 redirects from the old UENI website addresses, so existing Google rankings and links carry over
    lines = ['# Old UENI addresses -> new pages (301 = permanent)',
             '/about-us        /about/     301', '/about-us/       /about/     301',
             '/contact-us      /contact/   301', '/contact-us/     /contact/   301',
             '/legal-notice    /legal/     301', '/merchant-policies /legal/   301',
             '/blog/how-cctv-drain-inspections-prevent-costly-repairs  /blog/how-cctv-drain-inspections-prevent-costly-repairs/  301',
             '/blog/no-dig-drain-repairs-faster-fixes-with-less-disruption  /blog/no-dig-drain-repairs-faster-fixes-with-less-disruption/  301']
    for s in SERVICES:
        for o in s['old']:
            lines.append(f'{o}  /services/{s["slug"]}/  301')
    lines += ['/services/drain-maintenance/*  /services/  301', '/services/drainage-solutions/*  /services/  301',
              '# www -> main domain',
              'https://www.elitedrainage.uk/*  https://elitedrainage.uk/:splat  301!']
    open(os.path.join(OUT, '_redirects'), 'w').write('\n'.join(lines) + '\n')
    open(os.path.join(OUT, '_headers'), 'w').write('''/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=()
/img/*
  Cache-Control: public, max-age=31536000, immutable
/css/*
  Cache-Control: public, max-age=604800
/js/*
  Cache-Control: public, max-age=604800
''')

def build_vercel_config():
    """vercel.json: the same redirects and headers as the Netlify files, for hosting on Vercel."""
    redirects = []
    def r(src, dst):
        for v in {src.rstrip('/'), src.rstrip('/') + '/'}:
            redirects.append({"source": v, "destination": dst, "permanent": True})
    r('/about-us', '/about/'); r('/contact-us', '/contact/'); r('/legal-notice', '/legal/'); r('/merchant-policies', '/legal/')
    for s in SERVICES:
        for o in s['old']:
            r(o, f'/services/{s["slug"]}/')
    redirects += [{"source": "/services/drain-maintenance/:path*", "destination": "/services/", "permanent": True},
                  {"source": "/services/drainage-solutions/:path*", "destination": "/services/", "permanent": True}]
    cfg = {
        "$schema": "https://openapi.vercel.sh/vercel.json",
        "framework": None, "outputDirectory": "public",
        "trailingSlash": True,
        "redirects": redirects,
        "headers": [
            {"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"},
                                             {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                                             {"key": "X-Frame-Options", "value": "SAMEORIGIN"}]},
            {"source": "/img/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
        ],
    }
    open(os.path.join(ROOT, 'vercel.json'), 'w').write(json.dumps(cfg, indent=2) + '\n')

if __name__ == '__main__':
    build_home(); build_services_hub()
    for s in SERVICES: build_service(s)
    build_areas(); build_about(); build_contact(); build_blog(); build_legal(); build_utility(); build_seo_files(); build_vercel_config()
    print(f'Built {len(PAGES)} indexable pages into public/')
