#!/usr/bin/env python3
"""Builds the CIEA static site (island and routes direction) from shared partials. Output: /mnt/project-files/ciea-website/*.html"""
import os, re

OUT = os.path.dirname(os.path.abspath(__file__))
PHONE = "+1 (246) 232-5864"
WA = "https://wa.me/12462325864"
EMAIL = "info@ciea-barbados.com"

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="i-check" viewBox="0 0 24 24"><path d="M5 12.5l4.2 4.2L19 7"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M4 12h15M13 6l6 6-6 6"/></symbol>
<symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
<symbol id="i-camera" viewBox="0 0 24 24"><path d="M4 8.5A1.5 1.5 0 0 1 5.5 7h2.2l1.6-2.2h5.4L16.3 7h2.2A1.5 1.5 0 0 1 20 8.5v9a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 17.5z"/><circle cx="12" cy="12.8" r="3.4"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h10"/></symbol>
<symbol id="i-close" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></symbol>
<symbol id="i-chat" viewBox="0 0 24 24"><path d="M4.5 19.5l1.3-3.6A7.5 7.5 0 1 1 8.6 18.6z"/><path d="M9 10.5c.4 1.8 2.3 3.6 4.4 4.1l1.3-1.3-1.8-1-1 .6c-.8-.4-1.5-1.1-1.9-1.9l.6-1-1-1.8z"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M6.6 3.5h2.6l1.4 4.1-1.9 1.3a11 11 0 0 0 6.4 6.4l1.3-1.9 4.1 1.4v2.6a2 2 0 0 1-2.1 2A16.5 16.5 0 0 1 4.6 5.6a2 2 0 0 1 2-2.1z"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><rect x="3.5" y="5.5" width="17" height="13" rx="1.5"/><path d="M4 6.5l8 6 8-6"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></symbol>
<symbol id="i-cap" viewBox="0 0 24 24"><path d="M2.5 9.5L12 5l9.5 4.5L12 14z"/><path d="M6.5 11.5v4c1.5 1.4 3.4 2 5.5 2s4-.6 5.5-2v-4M21.5 9.5v5"/></symbol>
<symbol id="i-file" viewBox="0 0 24 24"><path d="M14 3.5H7A1.5 1.5 0 0 0 5.5 5v14A1.5 1.5 0 0 0 7 20.5h10a1.5 1.5 0 0 0 1.5-1.5V8z"/><path d="M14 3.5V8h4.5M9 14l2 2 4-4"/></symbol>
<symbol id="i-passport" viewBox="0 0 24 24"><rect x="5.5" y="3" width="13" height="18" rx="1.5"/><circle cx="12" cy="10.5" r="3"/><path d="M9 10.5h6M12 7.5c-1 1.6-1 4.4 0 6M12 7.5c1 1.6 1 4.4 0 6M9 17h6"/></symbol>
<symbol id="i-home" viewBox="0 0 24 24"><path d="M3.5 11L12 4l8.5 7"/><path d="M6 9.5v10h12v-10M10 19.5v-5h4v5"/></symbol>
<symbol id="i-plane" viewBox="0 0 24 24"><path d="M10.5 13.5l-6-2.2 1.3-1.3 7.2.6 4-4c.9-.9 2.3-1.1 2.8-.6s.3 1.9-.6 2.8l-4 4 .6 7.2-1.3 1.3-2.2-6-3 3v2.2l-1.2 1.2-1.3-3.3-3.3-1.3L4.6 16h2.2z"/></symbol>
<symbol id="i-users" viewBox="0 0 24 24"><circle cx="9" cy="8.5" r="3.2"/><path d="M3 19.5c.5-3.3 2.9-5.5 6-5.5s5.5 2.2 6 5.5"/><circle cx="17" cy="9.5" r="2.5"/><path d="M16.5 14.2c2.4.2 4 2 4.5 4.6"/></symbol>
<symbol id="i-steth" viewBox="0 0 24 24"><path d="M6 3.5v5a4 4 0 0 0 8 0v-5"/><path d="M10 12.5v2a5 5 0 0 0 10 0v-1.5"/><circle cx="20" cy="11" r="2"/></symbol>
<symbol id="i-award" viewBox="0 0 24 24"><circle cx="12" cy="9" r="5.5"/><path d="M8.6 13.4L7 20.5l5-2.5 5 2.5-1.6-7.1"/></symbol>
<symbol id="i-tag" viewBox="0 0 24 24"><path d="M3.5 12.2V4.5a1 1 0 0 1 1-1h7.7l8.3 8.3a1 1 0 0 1 0 1.4l-7.3 7.3a1 1 0 0 1-1.4 0z"/><circle cx="8" cy="8" r="1.6"/></symbol>
</svg>"""

def ic(name, cls="icon"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

def ph(text, kind="Photo"):
    return (f'<div class="ph" role="img" aria-label="{kind} placeholder: {text}">{ic("camera")}'
            f'<span class="ph-k">{kind} placeholder</span><span class="ph-t">{text}</span></div>')

def stamp(inner, color="c-sun", label=None, cls=""):
    """Rounded photo window; the colour drives the sun disc behind it."""
    chip = ""
    if label:
        text = label[0] if isinstance(label, tuple) else label
        chip = f'<span class="chip"><i></i>{text}</span>'
    return f'<div class="frame-wrap {color} {cls}"><div class="frame">{inner}{chip}</div></div>'

ISLAND = "M220.7 151.0 C213.0 153.2 200.2 169.7 195.5 178.8 C190.9 187.9 191.8 196.2 192.6 205.6 C193.4 215.1 198.4 225.5 200.4 235.4 C202.3 245.3 203.8 254.9 204.2 265.2 C204.7 275.5 202.2 287.1 203.3 297.0 C204.4 306.9 209.4 314.9 211.0 324.8 C212.6 334.7 210.2 346.3 213.0 356.6 C215.7 366.8 224.7 377.9 227.5 386.4 C230.2 394.8 225.4 403.1 229.4 407.2 C233.4 411.3 244.7 409.4 251.6 411.2 C258.6 413.0 263.7 416.0 271.0 418.1 C278.2 420.3 287.6 420.3 295.2 424.1 C302.7 427.9 310.0 440.1 316.4 441.0 C322.9 441.8 322.9 440.1 333.9 429.1 C344.8 418.0 369.8 391.8 382.2 374.4 C394.6 357.1 407.8 338.0 408.3 324.8 C408.8 311.5 399.9 305.3 385.1 295.0 C370.3 284.7 335.6 274.5 319.3 263.2 C303.1 252.0 297.1 239.6 287.4 227.5 C277.8 215.4 268.9 201.0 261.3 190.7 C253.7 180.5 248.7 172.5 242.0 165.9 C235.2 159.3 228.4 148.9 220.7 151.0 Z"
CITIES = [("MONTREAL", 205, 34, "out"), ("TORONTO", 96, 82, "in"), ("NEW YORK", 52, 172, "out"), ("MIAMI", 44, 268, "in"),
          ("LONDON", 548, 62, "out"), ("ACCRA", 584, 214, "in"), ("LAGOS", 578, 300, "out")]

def routes(legend=True):
    cx, cy, k = 336, 250, 0.72
    bx, by = cx + k * (227.5 - 300), cy + k * (386.4 - 295)
    def iso(scale, cls):
        return f'<path class="{cls}" d="{ISLAND}" transform="translate({cx} {cy}) scale({scale}) translate(-300 -295)" vector-effect="non-scaling-stroke"/>'
    contours = "".join(iso(k * f, "contour") for f in (1.3, 1.65))
    arcs, cities = [], []
    for name, x, y, d in CITIES:
        mx, my = (bx + x) / 2, (by + y) / 2
        dx, dy = x - bx, y - by
        qx, qy = mx - dy * 0.22, my + dx * 0.22
        if qy > my: qx, qy = mx + dy * 0.22, my - dx * 0.22
        path = f"M{bx:.0f} {by:.0f} Q{qx:.0f} {qy:.0f} {x} {y}"
        arcs.append(f'<path class="arc" d="{path}"/><path class="flow {d}" d="{path}"/>')
        cities.append(f'<g class="city"><circle cx="{x}" cy="{y}" r="5"/><text x="{x}" y="{y - 14}" text-anchor="middle">{name}</text></g>')
    leg = '<span class="legend">Based in Barbados \u00b7 Serving the world</span>' if legend else ""
    return f'''<div class="routes">{leg}<svg viewBox="0 0 620 470" role="img" aria-label="Map of Barbados with direct flight routes from Bridgetown to London, Toronto, Montreal, New York, Miami, Lagos and Accra">
<g>{contours}</g>{"".join(arcs)}{iso(k, "island")}{iso(k, "coast")}{"".join(cities)}
<circle class="home-ring" cx="{bx:.0f}" cy="{by:.0f}" r="8"/><circle class="home-dot" cx="{bx:.0f}" cy="{by:.0f}" r="7"/>
<text class="sea-label" x="560" y="430" text-anchor="middle">Atlantic Ocean</text><text class="sea-label" x="110" y="430" text-anchor="middle">Caribbean Sea</text>
<text class="home-label" x="{bx - 14:.0f}" y="{by + 30:.0f}" text-anchor="end">BRIDGETOWN</text>
</svg></div>'''

def seal(text="CO-CREATORS OF BARBADOS STUDY TOURS · "):
    return f'''<div class="seal" aria-hidden="true"><svg viewBox="0 0 200 200">
<defs><path id="sealp" d="M100 100 m-74 0 a74 74 0 1 1 148 0 a74 74 0 1 1 -148 0"/></defs>
<text style="font-size:15.5px"><textPath href="#sealp" textLength="458" lengthAdjust="spacing">{text}</textPath></text>
<text x="100" y="111" text-anchor="middle" style="font-size:34px;font-weight:800">CIEA</text>
</svg></div>'''

NAV = [("study-in-barbados.html", "Study in Barbados"), ("programs.html", "Programs"), ("services.html", "Services"),
       ("about.html#families", "For Parents"), ("about.html", "About")]

def header(active):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner">
<a class="brand" href="index.html" aria-label="Caribbean International Education Agency, home">
<img src="assets/ciea-logo.png" alt="" width="52" height="52">
<span class="brand-name">Caribbean International<span>Education Agency</span></span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">{ic("menu","icon i-menu")}<svg class="icon i-close" hidden aria-hidden="true"><use href="#i-close"/></svg></button>
<nav class="nav" id="site-nav" aria-label="Main">{links}<a class="btn btn-primary" href="contact.html">Book Free Consultation</a></nav>
</div></header>'''

def envelope(h="Ready to Start Your Education Journey?", p="Book a free consultation with our expert team today.", trust=False):
    t = ""
    if trust:
        t = f'''<ul class="trust"><li>{ic("check")}Free consultation, no obligation</li><li>{ic("check")}Response within 24 hours</li><li>{ic("check")}Family-centred approach</li></ul>'''
    return f'''<section class="envelope-section" aria-labelledby="env-h"><div class="wrap">
<div class="envelope">
<div class="body"><h2 id="env-h">{h}</h2><p>{p}</p>
<div class="btn-row"><a class="btn btn-primary" href="contact.html">Book Free Consultation {ic("arrow")}</a>
<a class="btn btn-line" href="{WA}" target="_blank" rel="noopener">{ic("chat")}WhatsApp Us</a></div>{t}</div>
{routes(legend=False)}
</div></div></section>'''

FOOTER = f'''<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div class="foot-brand"><img src="assets/ciea-logo.png" alt="Caribbean International Education Agency logo" width="84" height="84">
<p>Your one-stop shop for international education in the Caribbean. Co-creators of Barbados Study Tours.</p>
<p><a href="{WA}" target="_blank" rel="noopener">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>Bridgetown, Saint Michael, Barbados</p></div>
<div class="foot-col"><h3>Study in Barbados</h3><ul>
<li><a href="study-in-barbados.html#why">Why Barbados?</a></li><li><a href="study-in-barbados.html#uwi">UWI Cave Hill</a></li>
<li><a href="study-in-barbados.html#ross">Ross University</a></li><li><a href="study-in-barbados.html#aub">American Univ. of Barbados</a></li>
<li><a href="study-in-barbados.html#bcc">BCC</a></li><li><a href="index.html#faq">Visa Process</a></li></ul></div>
<div class="foot-col"><h3>Programs</h3><ul>
<li><a href="programs.html#summer-camps">Summer Programs</a></li><li><a href="programs.html#gap-year">Gap Year</a></li>
<li><a href="programs.html#faculty-led">Study Tours/Immersions</a></li></ul></div>
<div class="foot-col"><h3>Services</h3><ul>
<li><a href="index.html#programs">Medical School Advising</a></li><li><a href="services.html#placement">University Placement</a></li>
<li><a href="services.html#family">Parent/Family Support</a></li></ul></div>
<div class="foot-col"><h3>Company</h3><ul>
<li><a href="about.html">About Us</a></li><li><a href="about.html#families">For Parents</a></li>
<li><a href="index.html#faq">FAQ</a></li><li><a href="contact.html">Contact</a></li></ul></div>
</div>
<div class="foot-base"><span>&copy; 2025 Caribbean International Education Agency. All rights reserved.</span></div>
</div></footer>'''

def page(fname, title, desc, active, body, cta=True, cta_kwargs=None):
    env = envelope(**(cta_kwargs or {})) if cta else ""
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1c4f6c">
<link rel="icon" href="assets/ciea-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800&family=Figtree:ital,wght@0,400..800;1,400..600&display=swap">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
{SPRITE}
{header(active)}
<main id="main">
{body}
{env}
</main>
{FOOTER}
<script src="assets/site.js"></script>
</body>
</html>
'''
    assert "—" not in html and "–" not in html, f"dash found in {fname}"
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)
    print("wrote", fname, len(html))

def label(t):
    return f'<p class="label"><i></i>{t}</p>'

def page_hero(h1, sub, ph_text, color="c-sun"):
    return f'''<section class="hero page-hero"><canvas class="water" aria-hidden="true"></canvas><div class="wrap hero-grid">
<div class="hero-copy"><h1>{h1}</h1><p class="lede">{sub}</p></div>
{stamp(ph(ph_text), color, cls="float")}
</div></section>'''

def checks(items, cls=""):
    return f'<ul class="checks {cls}">' + "".join(
        f'<li><span class="tick">{ic("check")}</span><span>{i}</span></li>' for i in items) + "</ul>"

def reasons(lst, cls=""):
    return f'<ul class="reasons {cls}">' + "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in lst) + "</ul>"

# ------------------------------------------------------------------ HOME (copy verbatim from the content doc; em dashes replaced)
programs_cards = [
    ("c-sun", "Summer &amp; Gap Year Programs",
     "We can design and organize gap year and summer programmes that meet students' unique interests and needs. Whether you want to explore the Caribbean, develop a skill, or prepare for university, we create an experience tailored to you.",
     "programs.html#gap-year"),
    ("c-sea", "College and University Admission",
     "Expert guidance for Barbadians pursuing degrees in Canada, UK, Australia and Africa and for international students to study in the Caribbean, from application to arrival day and beyond.",
     "services.html#placement"),
    ("c-hib", "Medical School Advising",
     "Specialized pathway guidance for medical school in Barbados and the Caribbean",
     "study-in-barbados.html#aub"),
    ("c-palm", "Faculty-Led Immersion Programs",
     "Full-service logistics and in-country support for institutions organizing education abroad programs to Barbados and select other Caribbean countries.",
     "programs.html#faculty-led"),
    ("c-flame", "Volunteer &amp; Service Learning",
     "Connect with meaningful volunteer opportunities in Barbados aligned with your areas of interest and passion.",
     "programs.html#volunteer"),
    ("c-sun", "Student Relocation &amp; Support",
     "Airport pickup, accommodation assistance, banking assistance, SIM cards, and full settlement support for international students coming to Barbados.",
     "services.html#arrival"),
]
sheet = "".join(
    f'''<article class="prog {c}"><h3>{t}</h3><p>{p}</p><a class="more" href="{h}">Learn more {ic("arrow")}<span class="visually-hidden"> about {t}</span></a></article>'''
    for c, t, p, h in programs_cards)

reasons6 = [
    ("Fully English-Speaking", "No language barrier. Barbados has a highly educated, English-speaking population with deep ties to the UK and the Americas."),
    ("Safe &amp; Politically Stable", "Ranked as one of the most stable democracies in the world and consistently among the safest countries in the Caribbean."),
    ("Year-round Sunshine", 'Average <span class="fig">28&deg;C</span> year-round. Stunning beaches, a vibrant social scene, and an outdoor lifestyle that supports student wellbeing.'),
    ("Excellent Healthcare", "The Queen Elizabeth Hospital provides public healthcare and several private clinics ensure students have access to quality medical care."),
    ("Affordable Tuition", "Tuition and living costs are significantly lower than equivalent programs in North America or the UK, without sacrificing quality."),
    ("World-Class Institutions", "Home to The University of the West Indies, Ross University School of Medicine, and the American University of Barbados School of Medicine, all internationally accredited."),
]

faqs = [
    ("Do international students need a visa to study in Barbados?", "Most international students require a Student Visa to study in Barbados. Citizens of several countries may enter visa-free initially. We advise on the full visa process."),
    ("Can CIEA help me get a scholarship?", "Yes. We offer dedicated scholarship search support and advice based on our institutional connections. Our team knows what opportunities exist and how to make your application competitive."),
    ("How long does the university application process take?", "Application timelines vary by institution and program. Generally, plan for 3 to 6 months from initial consultation to receiving an offer letter. We recommend starting as early as possible. Contact us to map out your timeline."),
    ("Is Barbados safe for international students?", "Barbados is consistently ranked as one of the safest destinations in the Caribbean. It has stable governance, low violent crime, excellent healthcare, and a culture that is welcoming toward international visitors and students."),
    ("What is included in the Barbados Study Tours support?", "We provide end-to-end support: program content aligned with learning outcomes, accommodation, airport pickup, on-ground transportation, cultural and heritage tours, glass-bottom boat tours, nature hikes, activity bookings, and facilitated meetings with local officials, academics, and practitioners."),
    ("Can students work while studying in Barbados?", "International students on a Student Visa in Barbados may apply for work authorization under specific conditions. We advise on legal work opportunities."),
    ("Can you help Barbadian students apply to universities in Canada or the UK?", "Yes, this is one of our core services. We guide Barbadian students through the full process: choosing the right school and program, preparing a strong application, understanding visa and study permit requirements, applying for scholarships, and preparing for departure."),
    ("Do you help with accommodation in Barbados?", "Absolutely. We arrange on-campus housing subject to availability and connect students with vetted off-campus options that are safe, affordable, and well-located."),
    ("What makes CIEA different from other education consultants?", "We are based in Barbados. We know the island, its institutions, and its people intimately. Our advisors also have intimate, first-hand knowledge of study in Canada, the UK and Australia. We are co-creators with you of Barbados Study Tours, with a deep network across education and tourism. We offer genuine end-to-end support: not just advice, but on-the-ground logistics, in-country relationships, and ongoing student care."),
]
faq_html = "".join(
    f'<details><summary>{q}<span class="pm">{ic("plus")}</span></summary><div class="answer"><p>{a}</p></div></details>' for q, a in faqs)

services_tags = ["Accommodation sourcing and review", "On-island Transportation", "Boat Tours and Snorkeling", "Nature Hikes",
                 "Cultural Tours", "Activity Bookings", "Expert/Speaker Connections"]
ticker_items = [t for _, t, _, _ in programs_cards]
ticker = "".join(f'<span>{t}</span><i aria-hidden="true"></i>' for t in ticker_items)

home = f'''
<section class="hero hero-water"><canvas class="water" aria-hidden="true"></canvas><div class="wrap hero-grid">
<div class="hero-copy">
<p class="badge"><i></i>Based in Barbados &middot; Serving the World</p>
<h1><span>Your Caribbean</span> <span>Education Journey</span> <em>Starts Here</em></h1>
<p class="lede">Caribbean International Education Agency is your one-stop shop for information and support to make your dream of studying in the Caribbean a reality.</p>
<p class="hero-small">We connect students and institutions across the globe with educational opportunities in the Caribbean, with a focus on Barbados; and Barbadian students with opportunities abroad, from summer immersions and cultural experiences to full degree programs.</p>
<div class="btn-row"><a class="btn btn-primary" href="contact.html">Book Free Consultation {ic("arrow")}</a><a class="btn btn-ghost" href="programs.html">Explore Programs</a></div>
</div>
<div class="float-stack">
{stamp(ph("Students laughing together on a Barbados beach or campus"), "c-sun", cls="float f1")}
{stamp(ph("Bridgetown street or a colourful chattel house"), "c-hib", cls="float f2")}
{stamp(ph("Turquoise water at Carlisle Bay"), "c-palm", cls="float f3")}
</div>
</div></section>
<div class="ticker" aria-hidden="true"><div class="ticker-band"><div class="ticker-track">{ticker}{ticker}</div></div></div>

<section class="section" aria-labelledby="who-h"><div class="wrap split">
<div class="figure-stamp">{stamp(ph("An advisor meeting a student and parent, warm and natural"), "c-palm")}{seal()}</div>
<div class="stack">
{label("About CIEA")}
<h2 id="who-h">A One-Stop Shop for Caribbean International Education</h2>
<p>We are based on the beautiful, safe, and sophisticated island of Barbados, where most of our programs and services are anchored. Our many years of combined experience in international education and tourism, and our extensive network of connections across the Caribbean, position us to offer truly multi-country experiences.</p>
<p>Whether you're an international student coming to Barbados for a summer immersion or a full degree, a Barbadian family navigating the path to a Canadian, UK or Australian university, or an international institution looking to bring a group to the Caribbean, CIEA is your trusted partner.</p>
<div class="mt-2">{checks(["Barbados-based &amp; on-the-ground", "Institutional &amp; individual clients", "Multi-country Caribbean coverage", "Years of experience facilitating international education"], "two")}</div>
</div></div></section>

<section class="section bg-tissue" id="programs" aria-labelledby="prog-h"><div class="wrap">
<div class="head">{label("What We Offer")}<h2 id="prog-h">Programs &amp; Services</h2><p>From one-week cultural immersions to full medical school placement. Expert guidance and on-the-ground support at every stage.</p></div>
<div class="sheet">{sheet}</div>
</div></section>

<section class="section bg-sun" aria-labelledby="why-h"><div class="wrap reasons-layout">
<div class="reasons-aside">
{label("Why Choose Barbados?")}
<h2 id="why-h">A Caribbean Island Unlike Any Other</h2>
<p>Barbados offers world-class education in one of the most beautiful, safe, and sophisticated environments on the planet.</p>
<div><a class="btn btn-ink" href="study-in-barbados.html#institutions">Explore Barbados Institutions {ic("arrow")}</a></div>
<div class="postcard">{stamp(ph("Wide shot of the Barbados west coast or Carlisle Bay"), "c-sea", cls="no-disc")}</div>
</div>
{reasons(reasons6)}
</div></section>

<section class="section" id="one-service" aria-labelledby="one-h"><div class="wrap one-service">
<div class="stack">{label("Miscellaneous Stand-Alone Services")}<h2 id="one-h">Perhaps You Only Need <em>ONE</em> Service.</h2>
<p class="lede">We offer individual services for institutions and individuals who need specific support without a full package commitment.</p></div>
<ul class="tags">{"".join(f'<li class="tag {["c-sun","c-palm","c-flame","c-sea"][n % 4]}"><span class="dot">{ic("check")}</span>{t}</li>' for n, t in enumerate(services_tags))}</ul>
</div></section>

<section class="section bg-tissue" id="faq" aria-labelledby="faq-h"><div class="wrap faq-layout">
<div class="head">{label("Common Questions")}<h2 id="faq-h">Frequently Asked Questions</h2></div>
<div class="faq">{faq_html}</div>
</div></section>
'''
page("index.html", "Caribbean International Education Agency",
     "Barbados-based education agency connecting students and institutions with study, summer and degree opportunities in the Caribbean and abroad.",
     "index.html", home,
     cta_kwargs=dict(h="Ready to Make Your Move?", p="Whether you're exploring, planning, or ready to apply, a free consultation with our team is the best first step.", trust=True))

# ------------------------------------------------------------------ ABOUT
values = [
    ("c-flame", "Student-First", "Every decision we make is filtered through one question: what is genuinely best for this student?"),
    ("c-sea", "Integrity", "We give honest advice, even when it's not what a family wants to hear. Your trust is our most valuable asset."),
    ("c-palm", "Global Perspective", "We think internationally while acting locally. Our Barbados roots give us an advantage no overseas consultant can replicate."),
    ("c-sun", "Family-Centred", "Parents are partners in the process. We keep families informed, involved, and at ease throughout every stage."),
    ("c-hib", "Education First", "We believe access to quality education is transformative, for individuals, families, and communities."),
    ("c-sea", "Excellence", "We hold ourselves to the highest professional standards in every consultation, application, and program we deliver."),
]
about = page_hero("Rooted in Barbados. Reaching the World.",
    "We are the Caribbean International Education Agency, a Barbados-based team passionate about connecting students and institutions to world-class education opportunities on both sides of the ocean.",
    "The CIEA team in Bridgetown", "c-palm") + f'''
<section class="section" aria-labelledby="story-h"><div class="wrap story">
<div class="prose">
{label("Our Story")}
<h2 id="story-h">Why We Started CIEA</h2>
<p>Caribbean International Education Agency was founded by professionals with extensive experience in both higher education and Caribbean tourism, two worlds that, when combined, create something unique and powerful.</p>
<p>Over many years working with students, families, and institutions, our founder knows the challenges: talented students from across Africa and North America and Europe who wanted to experience education in Barbados but didn't know where to begin. Barbadian families seeking to send their children to university abroad with little guidance on the process. International universities wanting to bring students to the Caribbean for unique educational experiences but lacking the on-the-ground connections to make it work.</p>
<p>CIEA was established to close that gap. We are co-creators of Barbados Study Tours, a program that brings students from around the world to experience the Caribbean, and that experience forms the backbone of everything we do.</p>
<p>What makes CIEA different is simple: We are here, not a consultant in an overseas office advising on Barbados from afar. We live here, work here, and have deep relationships with the institutions, officials, academics, and communities that make Barbados and the wider Caribbean such extraordinary places to study and grow. We offer everything from a single activity booking to full end-to-end education migration and placement services.</p>
</div>
<aside>
{stamp(ph("Portrait of Patricia Atherley"), "c-sun")}
<blockquote class="quote"><p>My goal is simple: to help students enrich their learning and achieve their goals through international education.</p>
<footer><b>Patricia Atherley</b>Founder &amp; Director, CIEA</footer></blockquote>
</aside>
</div></section>

<section class="section bg-mist" id="families" aria-labelledby="fam-h"><div class="wrap split">
<div class="stack"><h2 id="fam-h">What Families Trust Us With</h2></div>
{checks(["Guiding their children through the most important decision of their lives", "Managing every detail of a complex international education process", "Being available on-the-ground when it matters most", "Providing honest advice without hidden agendas or commission pressure", "Ensuring safe, supported transitions to a new country and culture"])}
</div></section>

<section class="section" aria-labelledby="val-h"><div class="wrap">
<div class="head"><h2 id="val-h">Our Values</h2><p>The principles that guide every consultation, every application, and every student journey we support.</p></div>
<ul class="values">{"".join(f'<li class="{c}"><h3>{t}</h3><p>{p}</p></li>' for c, t, p in values)}</ul>
</div></section>
'''
page("about.html", "About CIEA", "Meet the Barbados-based team behind the Caribbean International Education Agency.", "about.html", about)

# ------------------------------------------------------------------ STUDY IN BARBADOS
reasons9 = [
    ("Fully English-Speaking", "No language barrier. Barbados has a highly educated, English-speaking population and a culture deeply connected to the UK and the Americas."),
    ("Safe &amp; Politically Stable", "Barbados ranks as one of the most stable democracies in the world and consistently among the safest countries in the Caribbean. Parents feel comfortable. Students feel at home."),
    ("Year-Round Sunshine", 'Average temperature of <span class="fig">28&deg;C</span> year-round. Stunning beaches, a vibrant social scene, and an outdoor lifestyle that supports student wellbeing.'),
    ("Excellent Healthcare", "The Queen Elizabeth Hospital provides public healthcare, and there are several private clinics. International students have access to quality medical care."),
    ("More Affordable Than You Think", "Tuition costs in Barbados are significantly lower than equivalent programs in North America or the United Kingdom, without sacrificing quality."),
    ("Globally Connected", "Direct flights to and from London, Miami, New York, Toronto, Montreal, Lagos, Accra, and across the Caribbean. Barbados is geographically and logistically accessible from almost anywhere."),
    ("Internationally Accredited Institutions", "The University of the West Indies, Ross University, and the American University of Barbados all carry international accreditation and globally recognized qualifications."),
    ("Rich Culture &amp; Heritage", "A vibrant arts scene, UNESCO-listed capital city, annual festivals, and a warm, welcoming Bajan culture that makes students feel part of a community."),
    ("Extraordinary Lifestyle", "Glass-bottom boat tours, surfing and snorkeling, year-round nature hikes, cricket, rum distillery tours. Barbados offers an experience no campus in a cold climate can match."),
]
insts = [
    ("uwi", "c-sea", "Flagship University", "University of the West Indies, Cave Hill Campus", "UWI Cave Hill",
     "International reputation across law, medicine, business, computer science, and the social sciences. Hundreds of undergraduate and graduate programs attracting students from across the globe. Exchange programs with universities worldwide.",
     ["Law", "Medicine", "Business Administration", "Computer Science", "International Relations", "Natural Sciences", "Cultural Studies"],
     ["Study Abroad Programs", "Exchange Programs", "Hundreds of Degree Programs"], "UWI Cave Hill campus"),
    ("bcc", "c-palm", "Community College", "Barbados Community College", "BCC",
     "Offers degree, diploma, certificate, and transfer pathways across multiple disciplines. An excellent gateway for students looking to earn credentials in Barbados or transfer to a four-year university abroad.",
     ["Hospitality &amp; Tourism", "Technology &amp; Computing", "Health Sciences", "Business Studies", "Fine Arts", "Liberal Arts"],
     ["Transfer Pathways", "Diploma Programs", "Certificate Courses"], "Barbados Community College campus"),
    ("aub", "c-sun", "Medical University", "American University of Barbados", "AUB",
     "Attracts students from many countries with a recognized Doctor of Medicine program structured around the USMLE pathway for those seeking US residency. An internationally oriented medical education environment.",
     ["Doctor of Medicine (MD)", "Pre-Medical Sciences", "Allied Health"],
     ["USMLE Pathway", "International Students", "American Curriculum"], "Medical students in a lab or lecture"),
    ("ross", "c-hib", "Medical School", "Ross University School of Medicine", "Ross University",
     "One of the largest Caribbean medical schools, with its main campus in Barbados. A major pathway for North American students seeking a Caribbean medical education with a focus on US licensing and residency matching.",
     ["Doctor of Medicine (MD)", "Basic Sciences", "Clinical Sciences"],
     ["US Residency Pathway", "Caribbean Medical School", "Barbados Campus"], "Ross University Barbados campus"),
]
inst_html = "".join(f'''<article class="inst {c}" id="{i}">
{stamp(ph(phs), c, cls="no-disc")}
<div class="inst-main"><div><span class="inst-type">{ty}</span></div>
<h3>{n}<small>{sn}</small></h3><p class="desc">{d}</p>
<div class="inst-meta"><h4>Programs</h4><ul class="inst-progs">{"".join(f"<li>{x}</li>" for x in pr)}</ul></div>
<ul class="tags small" aria-label="Highlights">{"".join(f'<li class="tag">{x}</li>' for x in tg)}</ul>
</div></article>''' for i, c, ty, n, sn, d, pr, tg, phs in insts)

study = page_hero("The Caribbean's Premier Education Destination",
    "World-class universities. A safe and sophisticated island environment. English-speaking. Affordable. Barbados ticks every box.",
    "Aerial view of Bridgetown and the Careenage", "c-sun") + f'''
<section class="section bg-sun" id="why" aria-labelledby="why9-h"><div class="wrap">
<div class="head"><h2 id="why9-h" class="visually-hidden">Why Barbados</h2></div>
{reasons(reasons9, "three")}
</div></section>

<section class="section bg-tissue" id="institutions" aria-labelledby="inst-h"><div class="wrap">
<div class="head"><h2 id="inst-h">Featured Institutions</h2><p>Barbados is home to a remarkable range of accredited higher education institutions, from a flagship regional university to internationally recognized medical schools.</p></div>
<div class="inst-list">{inst_html}</div>
<ul class="more-inst" style="margin-top:clamp(3.5rem,6vw,5rem)" aria-label="Additional institutions">
<li><b>UWI Open Campus (Global Campus)</b><span>Distance and blended learning across the Caribbean</span></li>
<li><b>Codrington Theological College</b><span>One of the oldest institutions in the Caribbean, offering theology and arts</span></li>
<li><b>Samuel Jackman Prescod Institute of Technology</b><span>Technical and vocational training</span></li>
</ul>
</div></section>
'''
page("study-in-barbados.html", "Study in Barbados with CIEA", "Why Barbados is the Caribbean's premier education destination, and the institutions you can study at.", "study-in-barbados.html", study)

# ------------------------------------------------------------------ PROGRAMS
progs = [
    ("gap-year", "c-sun", "Gap Year &amp; Summer/Winter Abroad",
     "We design and organize gap year and summer programmes that meet students' unique interests and needs. Whether you want to explore the Caribbean, develop a skill, volunteer, or prepare for university, we create an experience tailored to you.",
     ["Fully customized itinerary based on your interests", "Dance, theatre, music, environment, sports &amp; more", "Accommodation arrangements in Barbados", "Airport pickup and on-island transportation", "Cultural and heritage tours", "Multi-week or semester-length options"],
     "Young people hiking or exploring the Barbados east coast"),
    ("summer-camps", "c-flame", "Summer Camps",
     "We facilitate enrolment in local summer camps in collaboration with partners, in areas that students are passionate about. From the performing arts to environmental conservation, our camps combine learning with an unforgettable Caribbean experience.",
     ["Partner camps in dance, theatre, and music", "Environmental and conservation programs", "Sports camps including cricket, swimming, and more", "Ages 8 to 18", "Host accommodation", "Caribbean cultural integration"],
     "Children at a cricket, dance or swimming camp"),
    ("faculty-led", "c-sea", "Faculty-Led Education Abroad Programs",
     "We provide comprehensive information, program design and planning support, logistical services, and in-country support for international institutions seeking to organize study abroad programmes to Barbados.",
     ["Program content design aligned with learning outcomes", "Accommodation arrangements for groups", "Airport pickup and on-ground transportation", "Cultural, heritage, and educational tours", "Meetings with local officials, academics &amp; experts", "Glass-bottom boat tours, nature hikes &amp; activities", "Ongoing in-country support during the program"],
     "A university group on a heritage tour with a local guide"),
    ("volunteer", "c-palm", "Volunteer &amp; Service Learning",
     "We connect students with meaningful volunteer opportunities and service learning experiences in Barbados. Choose from education, environment, community development, healthcare, and more.",
     ["Volunteer placement matched to your interests", "Education, environment, community development", "Healthcare and social service opportunities", "Accommodation and logistics support", "Certificate of service completion", "Cultural immersion alongside your placement"],
     "Students volunteering at a beach clean-up or community project"),
]
prog_html = "".join(f'''<article class="program" id="{i}">
<div class="figure-stamp">{stamp(ph(phs), c)}</div>
<div class="copy"><h2>{t}</h2><p>{d}</p><h3>What's included</h3>{checks(inc)}</div>
</article>''' for i, c, t, d, inc, phs in progs)

programs = page_hero("Education Beyond the Classroom",
    "From a week-long cultural immersion to a full semester at The UWI, we facilitate education experiences in Barbados that change perspectives and open doors.",
    "Students snorkeling or on a glass-bottom boat", "c-flame") + f'''
<section class="section"><div class="wrap">{prog_html}</div></section>
<section class="section bg-sun" aria-labelledby="custom-h"><div class="wrap custom-band">
<div><h2 id="custom-h">Don't See Exactly What You're Looking For?</h2>
<p>We specialize in custom program design. Tell us your goals, interests, and timeline, and we'll create something tailored just for you.</p></div>
<div><a class="btn btn-ink" href="contact.html">Request a Custom Program {ic("arrow")}</a></div>
</div></section>
'''
page("programs.html", "CIEA Programs", "Gap year, summer camps, faculty-led study abroad and volunteer programs in Barbados.", "programs.html", programs)

# ------------------------------------------------------------------ SERVICES
core = [
    ("placement", "c-sun", "cap", "University Placement", "End-to-end guidance from school selection to offer acceptance. We know which programs fit your profile and how to make your application stand out."),
    ("review", "c-palm", "file", "Application Review", "Expert review of every component of your application (personal statements, CVs, reference letters) before submission."),
    ("visa", "c-flame", "passport", "Student Visa Assistance", "Full documentation support and application management for student visas and study permits across major destinations."),
    ("accommodation", "c-sea", "home", "Accommodation Support", "We help identify, vet, and arrange safe, suitable student housing where needed."),
    ("arrival", "c-hib", "plane", "Student Arrival Support", "Airport pickup and on-the-ground help during your first critical days."),
    ("family", "c-sun", "users", "Parent/Family Support Service", "We remain a point of contact and support for parents and families"),
]
def svc_badge(c, i):
    style = ' style="color:#fff"' if c in ("c-sea", "c-hib") else ""
    return f'<span class="badge {c}"{style}>{ic(i)}</span>'
core_html = "".join(f'<li id="{a}">{svc_badge(c, i)}<div><h3>{t}</h3><p>{p}</p></div></li>' for a, c, i, t, p in core)

services = page_hero("Expert Support at Every Stage",
    "From a single application review to full end-to-end placement and relocation, choose the level of support that's right for you.",
    "An advisor reviewing an application with a student", "c-sea") + f'''
<section class="section" aria-labelledby="core-h"><div class="wrap">
<h2 id="core-h" class="visually-hidden">Core Services</h2>
<ul class="services">{core_html}</ul>
</div></section>
'''
page("services.html", "CIEA Services", "University placement, application review, visa, accommodation, arrival and family support.", "services.html", services)

# ------------------------------------------------------------------ CONTACT
interests = ["Study in Barbados: College or University Placement", "Study Abroad (Barbadian students) (Study in Canada / UK / Australia)",
             "Medical School Advising", "Summer or Gap Year Program", "Faculty-Led Program Support", "Parent/Family Support Service", "General Inquiry"]
contact = page_hero("Let's Talk About Your Future",
    "Book your free 30-minute consultation. No pressure, no obligation. Just expert advice tailored to your situation.",
    "A friendly advisor on a video call", "c-palm") + f'''
<section class="section"><div class="wrap contact-grid">
<div class="label-card">
<dl>
<div><dt>{ic("chat")}</dt><dd><b>Phone / WhatsApp</b><span>{PHONE}</span></dd></div>
<div><dt>{ic("mail")}</dt><dd><b>Email</b><span>{EMAIL}</span></dd></div>
<div><dt>{ic("pin")}</dt><dd><b>Location</b><span>Bridgetown, Saint Michael, Barbados</span></dd></div>
<div><dt>{ic("clock")}</dt><dd><b>Office Hours</b><span>Mon to Fri: 9:00am to 5:00pm AST</span></dd></div>
</dl>
<div><a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">{ic("chat")}WhatsApp Us</a></div>
</div>

<div>
<form class="form" id="consult-form" novalidate>
<div class="row">
<div class="field"><label for="f-name">Full Name <span class="req" aria-hidden="true">*</span></label><input id="f-name" name="name" autocomplete="name" required><span class="err">Please enter your name.</span></div>
<div class="field"><label for="f-email">Email Address <span class="req" aria-hidden="true">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required><span class="err">Please enter an email address like name@example.com.</span></div>
</div>
<div class="row">
<div class="field"><label for="f-phone">Phone / WhatsApp</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
<div class="field"><label for="f-country">Country of Residence <span class="req" aria-hidden="true">*</span></label><input id="f-country" name="country" autocomplete="country-name" required><span class="err">Please tell us where you live.</span></div>
</div>
<div class="field"><label for="f-interest">I'm interested in... <span class="req" aria-hidden="true">*</span></label>
<select id="f-interest" name="interest" required><option value="">Choose one</option>{"".join(f"<option>{o}</option>" for o in interests)}</select><span class="err">Please choose what you're interested in.</span></div>
<div class="field"><label for="f-msg">Tell us about your situation <span class="req" aria-hidden="true">*</span></label><textarea id="f-msg" name="message" required></textarea><span class="err">Please tell us a little about your situation.</span></div>
<div class="form-foot"><button class="btn btn-primary" type="submit">Send My Inquiry</button><span class="note">Free consultation. No obligation. Response within 24 hours.</span></div>
</form>
<div class="success" id="form-success" hidden tabindex="-1">
<h2>Message Received!</h2>
<p>Thank you. We'll be in touch within 24 hours. For faster response, WhatsApp us directly.</p>
<a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">{ic("chat")}WhatsApp Us</a>
</div>
</div>
</div></section>
'''
page("contact.html", "Contact CIEA", "Book a free 30-minute consultation with the Caribbean International Education Agency.", "contact.html", contact, cta=False)
