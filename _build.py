#!/usr/bin/env python3
"""Generate all TSBR website pages with unified design and rich content."""

import json
from html import escape as hescape
from pathlib import Path

from _content import (
    ABOUT_TIMELINE,
    ABOUT_VALUES,
    AI_NEWS_ARTICLES,
    AUDIT_INCLUDES,
    BLOG_ARTICLES,
    CASE_STUDIES,
    FAQ_ITEMS,
    INDUSTRIES,
    LOCATION_RICH,
    PROCESS_STEPS,
    SERVICE_RICH,
    TESTIMONIALS,
    WHY_TSBR,
    case_study_html,
    faq_html,
    testimonials_html,
    quote_cards_html,
    gmb_reviews_html,
    founder_bio_html,
    FOUNDER,
)
from _content_extra import (
    ARLINGTON_PATHWAY,
    COMPARISON_ROWS,
    EEAT_CREDENTIALS,
    ENGAGEMENT_MONTHS,
    EXTRA_FAQ,
    FOUNDER_BIO_HTML,
    GMB_SIGNALS,
    KEYWORD_INTENTS,
    MEDIA_GALLERY,
    VIDEO_ASSETS,
)
from _config import FORMSPREE_ENDPOINT, GA_MEASUREMENT_ID, GOOGLE_MAPS_EMBED

HOME_FAQ = FAQ_ITEMS[:6]
FULL_FAQ = FAQ_ITEMS + EXTRA_FAQ

LOCATION_KEYWORD_MARKET = {
    "arlington-tx-seo-marketing-consultant.html": "DFW / Arlington",
    "dallas-tx-seo-marketing-consultant.html": "DFW / Arlington",
    "fort-worth-tx-seo-marketing-consultant.html": "DFW / Arlington",
    "plano-frisco-dfw-north-tx-seo-marketing-consultant.html": "DFW / Arlington",
    "houston-tx-seo-marketing-consultant.html": "Houston",
    "the-woodlands-katy-tx-seo-marketing-consultant.html": "Houston",
    "austin-tx-seo-marketing-consultant.html": "Austin",
    "round-rock-cedar-park-georgetown-tx-seo-marketing-consultant.html": "Austin",
    "san-antonio-tx-seo-marketing-consultant.html": "San Antonio",
    "texas-statewide-seo-marketing-consultant.html": None,
}

ROOT = Path(__file__).parent
PHONE = "(682) 206-4178"
PHONE_TEL = "+16822064178"
EMAIL = "hello@tsbrenterprises.com"
ADDRESS = "518 Brynmawr Ct, Arlington, TX 76014"
DOMAIN = "https://tsbrenterprises.com"
YEAR = "2026"
OG_IMAGE = f"{DOMAIN}/assets/images/hero-branded-aggressive-10.jpg"
GEO_LAT = 32.7357
GEO_LON = -97.1081
SITEMAP_LASTMOD = "2026-06-19"

BLOG_SERVICE_MAP = {
    "GMB": "gmb-optimization.html",
    "Guide": "gmb-optimization.html",
    "Local SEO": "local-seo-texas.html",
    "AI": "ai-search-optimization.html",
    "Citations": "local-seo-texas.html",
    "Technical": "local-seo-texas.html",
    "B2B": "b2b-lead-generation.html",
    "Content": "ai-search-optimization.html",
}

SERVICE_META = {
    "gmb-optimization.html": {
        "title": "GMB Optimization | Texas Map Pack Experts",
        "meta_desc": "Elite Google Business Profile optimization for top-3 Map Pack positions across Texas B2B markets.",
        "eyebrow": "Google Business Profile",
        "h1": "GMB optimization that actually moves the needle",
        "lead": "We engineer every Google signal so your Texas B2B company owns the Map Pack and gets cited in AI Overviews.",
    },
    "ai-search-optimization.html": {
        "title": "AI Search Optimization | Texas AI Overview Experts",
        "meta_desc": "Generative Engine Optimization for Texas B2B — get cited in Google AI Overviews and AI-powered search.",
        "eyebrow": "AI Search",
        "h1": "Get cited when buyers ask AI",
        "lead": "We build entity authority and structured content so generative search recommends your business as the trusted answer.",
    },
    "local-seo-texas.html": {
        "title": "Local SEO Texas | B2B Search Dominance",
        "meta_desc": "Full local SEO services for Texas B2B companies — citations, on-page, content, and technical optimization.",
        "eyebrow": "Local SEO",
        "h1": "Full local SEO built for Texas",
        "lead": "From citations to content silos, we build the complete local search foundation your B2B company needs.",
    },
    "b2b-lead-generation.html": {
        "title": "B2B Lead Generation | Texas Search-Driven Leads",
        "meta_desc": "Search-driven B2B lead systems for Texas companies — qualified commercial inquiries, not vanity traffic.",
        "eyebrow": "B2B Leads",
        "h1": "Leads that close, not clicks that bounce",
        "lead": "We optimize for the keywords and profiles that generate high-value commercial inquiries for Texas B2B companies.",
    },
}

LOCATION_META = {
    "arlington-tx-seo-marketing-consultant.html": {"short": "Arlington / DFW", "city": "Arlington, Texas", "title": "Arlington TX SEO Consultant", "meta_desc": "Expert GMB and local SEO for B2B companies in Arlington and DFW.", "lead": "Our home base. We know DFW search behavior inside and out.", "areas": ["Arlington", "Dallas", "Fort Worth", "Grand Prairie", "Mansfield", "Euless", "Bedford", "Irving"]},
    "dallas-tx-seo-marketing-consultant.html": {"short": "Dallas", "city": "Dallas, Texas", "title": "Dallas TX SEO Consultant", "meta_desc": "GMB optimization and local SEO for Dallas B2B companies.", "lead": "Dominate North Texas commercial search with Map Pack and AI visibility.", "areas": ["Dallas", "Uptown", "Deep Ellum", "Oak Cliff", "Lake Highlands", "Preston Hollow"]},
    "fort-worth-tx-seo-marketing-consultant.html": {"short": "Fort Worth", "city": "Fort Worth, Texas", "title": "Fort Worth TX SEO Consultant", "meta_desc": "Local SEO for Fort Worth industrial and trade B2B companies.", "lead": "West DFW industrial, trade, and professional services ranked in Maps and AI.", "areas": ["Fort Worth", "Stockyards", "West 7th", "Alliance", "Benbrook", "Keller"]},
    "houston-tx-seo-marketing-consultant.html": {"short": "Houston", "city": "Houston, Texas", "title": "Houston TX SEO Consultant", "meta_desc": "Greater Houston B2B local SEO and GMB optimization.", "lead": "Greater Houston B2B visibility from the Energy Corridor to The Woodlands and Katy.", "areas": ["Houston", "The Woodlands", "Katy", "Sugar Land", "Pearland", "Cypress"]},
    "austin-tx-seo-marketing-consultant.html": {"short": "Austin", "city": "Austin, Texas", "title": "Austin TX SEO Consultant", "meta_desc": "Austin metro local SEO for B2B and professional services.", "lead": "Central Texas growth markets — tech, professional services, and commercial B2B search.", "areas": ["Austin", "Round Rock", "Cedar Park", "Georgetown", "Pflugerville", "Leander"]},
    "san-antonio-tx-seo-marketing-consultant.html": {"short": "San Antonio", "city": "San Antonio, Texas", "title": "San Antonio TX SEO Consultant", "meta_desc": "San Antonio B2B local SEO and Google Business Profile experts.", "lead": "South and Central Texas B2B search — Map Pack, organic, and AI visibility.", "areas": ["San Antonio", "New Braunfels", "Boerne", "Schertz", "Seguin", "Universal City"]},
    "plano-frisco-dfw-north-tx-seo-marketing-consultant.html": {"short": "Plano / Frisco", "city": "North DFW", "title": "Plano & Frisco SEO Consultant", "meta_desc": "North DFW corporate corridor local SEO for B2B.", "lead": "Plano, Frisco, McKinney, Allen, and the North DFW growth corridor.", "areas": ["Plano", "Frisco", "McKinney", "Allen", "Prosper", "Richardson"]},
    "round-rock-cedar-park-georgetown-tx-seo-marketing-consultant.html": {"short": "Austin Metro North", "city": "Austin Metro North", "title": "Round Rock & Cedar Park SEO", "meta_desc": "North Austin suburbs local SEO for B2B companies.", "lead": "Round Rock, Cedar Park, Georgetown, and Leander commercial search dominance.", "areas": ["Round Rock", "Cedar Park", "Georgetown", "Leander", "Pflugerville", "Hutto"]},
    "the-woodlands-katy-tx-seo-marketing-consultant.html": {"short": "The Woodlands / Katy", "city": "Greater Houston", "title": "The Woodlands & Katy SEO", "meta_desc": "North and west Houston suburbs local SEO.", "lead": "The Woodlands, Katy, Cypress, and Tomball B2B search visibility.", "areas": ["The Woodlands", "Katy", "Cypress", "Tomball", "Spring", "Conroe"]},
    "texas-statewide-seo-marketing-consultant.html": {"short": "Statewide", "city": "Texas Statewide", "title": "Texas Statewide SEO", "meta_desc": "Multi-market Texas local SEO for statewide B2B operations.", "lead": "Multi-market Texas coverage for B2B companies across every major metro.", "areas": ["DFW", "Houston", "Austin", "San Antonio", "Corpus Christi", "El Paso", "Lubbock", "Tyler"]},
}


def join_text(val):
    if isinstance(val, list):
        return " ".join(val)
    return val


def prefix(depth=0):
    return "../" * depth


def page_url(path=""):
    if not path or path in ("/", "index.html"):
        return DOMAIN + "/"
    return f"{DOMAIN}/{path.lstrip('/')}"


def json_ld_script(data):
    return (
        '    <script type="application/ld+json">\n    '
        + json.dumps(data, ensure_ascii=False)
        + "\n    </script>"
    )


def schema_extra(*nodes):
    if not nodes:
        return ""
    if len(nodes) == 1:
        return "\n" + json_ld_script(nodes[0])
    return "\n" + json_ld_script({"@context": "https://schema.org", "@graph": list(nodes)})


def schema_organization():
    return {
        "@type": ["Organization", "LocalBusiness", "ProfessionalService"],
        "@id": f"{DOMAIN}/#organization",
        "name": "The Stone Builders Rejected",
        "alternateName": ["TSBR Enterprises", "TSBR"],
        "url": DOMAIN,
        "logo": OG_IMAGE,
        "image": OG_IMAGE,
        "telephone": PHONE,
        "email": EMAIL,
        "description": "Texas B2B local SEO, Google Business Profile optimization, and AI search visibility agency.",
        "foundingDate": "2014",
        "founder": {"@type": "Person", "@id": f"{DOMAIN}/#founder", "name": FOUNDER["short_name"]},
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "518 Brynmawr Ct",
            "addressLocality": "Arlington",
            "addressRegion": "TX",
            "postalCode": "76014",
            "addressCountry": "US",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": GEO_LAT, "longitude": GEO_LON},
        "areaServed": {"@type": "State", "name": "Texas"},
        "priceRange": "$$",
        "knowsAbout": [
            "Local SEO", "Google Business Profile", "AI Search Optimization",
            "Generative Engine Optimization", "B2B Lead Generation", "Citation Building",
        ],
    }


def schema_website():
    return {
        "@type": "WebSite",
        "@id": f"{DOMAIN}/#website",
        "url": DOMAIN,
        "name": "The Stone Builders Rejected",
        "publisher": {"@id": f"{DOMAIN}/#organization"},
        "inLanguage": "en-US",
    }


def schema_breadcrumb(items):
    elements = []
    for i, (name, href) in enumerate(items, 1):
        el = {"@type": "ListItem", "position": i, "name": name}
        if href:
            clean = href.replace("../", "")
            el["item"] = page_url(clean)
        elements.append(el)
    return {"@type": "BreadcrumbList", "itemListElement": elements}


def schema_faq(items):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in items
        ],
    }


def schema_service(name, description, url):
    return {
        "@type": "Service",
        "name": name,
        "description": description,
        "url": url,
        "provider": {"@id": f"{DOMAIN}/#organization"},
        "areaServed": {"@type": "State", "name": "Texas"},
        "serviceType": name,
    }


def schema_article(title, description, url, date_published, tag=""):
    return {
        "@type": "Article",
        "headline": title,
        "description": description,
        "url": url,
        "datePublished": date_published,
        "dateModified": date_published,
        "author": {
            "@type": "Person",
            "@id": f"{DOMAIN}/#founder",
            "name": FOUNDER["short_name"],
        },
        "publisher": {"@id": f"{DOMAIN}/#organization"},
        "image": OG_IMAGE,
        "articleSection": tag,
        "inLanguage": "en-US",
        "about": {"@type": "Thing", "name": "Texas B2B Local SEO"},
    }


def schema_webpage(name, description, url):
    return {
        "@type": "WebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": name,
        "description": description,
        "isPartOf": {"@id": f"{DOMAIN}/#website"},
        "about": {"@id": f"{DOMAIN}/#organization"},
        "inLanguage": "en-US",
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": [".lead", ".aeo-answer", ".faq-body", "h1", ".highlight-box"],
        },
    }


def schema_item_list(name, entries):
    return {
        "@type": "ItemList",
        "name": name,
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i,
                "name": label,
                "url": page_url(href),
            }
            for i, (label, href) in enumerate(entries, 1)
        ],
    }


def breadcrumb_html(items, depth=0):
    p = prefix(depth)
    parts = ['<nav class="breadcrumb" aria-label="Breadcrumb"><ol>']
    for i, (label, href) in enumerate(items):
        if href:
            parts.append(f'<li><a href="{p}{href}">{label}</a></li>')
        else:
            parts.append(f'<li aria-current="page">{label}</li>')
    parts.append("</ol></nav>")
    return "\n        ".join(parts)


def silo_nav_html(heading, links, depth=0):
    p = prefix(depth)
    items = "".join(
        f'<li><a href="{p}{href}">{label}</a></li>' for label, href in links
    )
    return f"""
        <section class="section section-alt silo-nav" aria-label="{heading}">
            <div class="container">
                <h2 class="silo-nav-title">{heading}</h2>
                <ul class="silo-nav-list">{items}</ul>
            </div>
        </section>"""


def aeo_summary_html(text):
    return f'<p class="aeo-answer" role="doc-abstract">{text}</p>'


def service_silo(filename):
    others = [(SERVICE_META[f]["h1"], f) for f in SERVICE_META if f != filename]
    return {
        "heading": "Explore the TSBR service silo",
        "links": [("All services", "services.html")] + others[:3] + [
            ("Texas service areas", "locations.html"),
            ("Case studies", "case-studies.html"),
            ("Free audit", "contact.html"),
        ],
    }


def location_silo(filename):
    others = [(LOCATION_META[f]["short"], f) for f in LOCATION_META if f != filename]
    return {
        "heading": "Texas location silo",
        "links": [("All locations", "locations.html")] + others[:4] + [
            ("GMB optimization", "gmb-optimization.html"),
            ("Local SEO Texas", "local-seo-texas.html"),
            ("AI search optimization", "ai-search-optimization.html"),
        ],
    }


def blog_silo(article):
    related = [
        (a["title"][:52], f"blog/{a['slug']}")
        for a in BLOG_ARTICLES
        if a["slug"] != article["slug"]
    ][:4]
    svc = BLOG_SERVICE_MAP.get(article["tag"], "services.html")
    svc_label = SERVICE_META.get(svc, {}).get("h1", "Services")
    return {
        "heading": "Related in this content silo",
        "links": [("Blog hub", "blog.html"), (svc_label, svc)] + related,
    }


def head(title, description, depth=0, canonical=None, og_type="website", og_image=None, extra=""):
    p = prefix(depth)
    can = canonical or page_url()
    t = hescape(title)
    d = hescape(description)
    img = og_image or OG_IMAGE
    fonts = (
        "https://fonts.googleapis.com/css2?"
        "family=Exo+2:ital,wght@0,400;0,500;0,600;0,700;1,400"
        "&family=Orbitron:wght@500;600;700;800&display=swap"
    )
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t}</title>
    <meta name="description" content="{d}">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="author" content="Mike Kaswatuka">
    <meta name="geo.region" content="US-TX">
    <meta name="geo.placename" content="Arlington, Texas">
    <meta name="geo.position" content="{GEO_LAT};{GEO_LON}">
    <meta name="ICBM" content="{GEO_LAT}, {GEO_LON}">
    <meta name="theme-color" content="#030508">
    <link rel="canonical" href="{can}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="{fonts}">
    <link rel="stylesheet" href="{p}css/site.css">
{favicon_links(depth)}
{analytics_snippet()}
    <meta property="og:type" content="{og_type}">
    <meta property="og:site_name" content="The Stone Builders Rejected">
    <meta property="og:locale" content="en_US">
    <meta property="og:title" content="{t}">
    <meta property="og:description" content="{d}">
    <meta property="og:url" content="{can}">
    <meta property="og:image" content="{img}">
    <meta property="og:image:alt" content="The Stone Builders Rejected — Texas B2B Local SEO">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{t}">
    <meta name="twitter:description" content="{d}">
    <meta name="twitter:image" content="{img}">
{extra}
</head>"""


def header(depth=0, active="", body_class=""):
    p = prefix(depth)
    links = [
        ("index.html", "Home", "home"),
        ("services.html", "Services", "services"),
        ("testimonials.html", "Reviews", "testimonials"),
        ("case-studies.html", "Results", "results"),
        ("locations.html", "Locations", "locations"),
        ("blog.html", "Blog", "blog"),
        ("ai-news.html", "AI News", "ainews"),
        ("about.html", "About", "about"),
    ]
    nav = ""
    for href, label, key in links:
        cls = ' style="color:var(--gold);font-weight:600"' if key == active else ""
        nav += f'                <a href="{p}{href}"{cls}>{label}</a>\n'
    mnav = "".join(f'            <a href="{p}{href}">{label}</a>\n' for href, label, _ in links)

    body_attr = f' class="{body_class}"' if body_class else ""
    return f"""<body{body_attr}>
    <a href="#main" class="skip-link">Skip to content</a>

    <div class="top-bar">
        <div class="container">
            <div>
                <a href="tel:{PHONE_TEL}">{PHONE}</a>
                &nbsp;&middot;&nbsp;
                <a href="mailto:{EMAIL}">{EMAIL}</a>
            </div>
            <div>Arlington, Texas &middot; Serving statewide</div>
        </div>
    </div>

    <header class="site-header">
        <div class="container">
            <div class="header-inner">
                <a href="{p}index.html" class="logo">
                    <span class="logo-mark">TSBR</span>
                    <span class="logo-text">The Stone Builders Rejected</span>
                </a>
                <nav class="nav-desktop" aria-label="Main navigation">
{nav}                    <a href="{p}contact.html" class="btn btn-primary">Free Audit</a>
                </nav>
                <button class="nav-toggle" id="nav-toggle" aria-label="Open menu" aria-expanded="false">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
                </button>
            </div>
            <nav class="nav-mobile" id="nav-mobile" aria-label="Mobile navigation">
{mnav}                <a href="{p}contact.html">Free Audit</a>
            </nav>
        </div>
    </header>"""


def footer(depth=0):
    p = prefix(depth)
    return f"""
    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="{p}index.html" class="logo">
                        <span class="logo-mark">TSBR</span>
                        <span class="logo-text">The Stone Builders Rejected</span>
                    </a>
                    <p>Texas local SEO and Google Business Profile experts helping B2B companies become the obvious choice in search &mdash; Maps, organic, and AI Overviews. Founded by Mike Kaswatuka in Arlington.</p>
                </div>
                <div class="footer-col">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="{p}gmb-optimization.html">GMB Optimization</a></li>
                        <li><a href="{p}ai-search-optimization.html">AI Search</a></li>
                        <li><a href="{p}local-seo-texas.html">Local SEO</a></li>
                        <li><a href="{p}b2b-lead-generation.html">B2B Leads</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="{p}about.html">About</a></li>
                        <li><a href="{p}testimonials.html">Client Reviews</a></li>
                        <li><a href="{p}case-studies.html">Case Studies</a></li>
                        <li><a href="{p}blog.html">Blog</a></li>
                        <li><a href="{p}ai-news.html">AI News</a></li>
                        <li><a href="{p}resources.html">Resources</a></li>
                        <li><a href="{p}contact.html">Contact</a></li>
                        <li><a href="{p}privacy.html">Privacy Policy</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
                        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
                        <li>{ADDRESS}</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <span>&copy; 2014&ndash;{YEAR} The Stone Builders Rejected. All rights reserved. &middot; <a href="{p}privacy.html">Privacy Policy</a></span>
                <span><a href="{p}locations.html">Texas Service Areas</a> &middot; <a href="{p}arlington-tx-seo-marketing-consultant.html">Arlington</a></span>
            </div>
        </div>
    </footer>
    <script src="{p}js/site.js" defer></script>
</body>
</html>"""


def write(path, content):
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {path.name}")


def page_template(
    title, description, eyebrow, h1, lead, body,
    active="", canonical=None, depth=0, hero_class="page-hero", extra="",
    breadcrumbs=None, aeo_summary=None, silo_nav=None, og_type="website",
):
    bc = breadcrumb_html(breadcrumbs, depth) if breadcrumbs else ""
    aeo = aeo_summary_html(aeo_summary) if aeo_summary else ""
    silo = silo_nav_html(silo_nav["heading"], silo_nav["links"], depth) if silo_nav else ""
    return (
        head(title, description, depth, canonical, og_type=og_type, extra=extra)
        + header(depth, active)
        + f"""
    <main id="main">
        {bc}
        <section class="{hero_class}">
            <div class="container">
                <div class="eyebrow">{eyebrow}</div>
                <h1>{h1}</h1>
                <p class="lead">{lead}</p>
                {aeo}
            </div>
        </section>
        {body}
        {silo}
    </main>
"""
        + footer(depth)
    )


def industries_html():
    return '<div class="industry-grid">' + "".join(f'<span class="industry-pill">{i}</span>' for i in INDUSTRIES) + "</div>"


def audit_list_html():
    return '<ul class="feature-list">' + "".join(f'<li><span class="check">&#10003;</span><span>{item}</span></li>' for item in AUDIT_INCLUDES) + "</ul>"


def form_open(subject, css_class=""):
    cls = f' class="{css_class}"' if css_class else ""
    if FORMSPREE_ENDPOINT:
        return (
            f'<form action="{hescape(FORMSPREE_ENDPOINT)}" method="POST"{cls}>'
            f'<input type="hidden" name="_subject" value="{hescape(subject)}">'
        )
    return (
        f'<form action="#" method="POST"{cls} data-tsbr-form="fallback" data-tsbr-email="{EMAIL}">'
        f'<input type="hidden" name="_subject" value="{hescape(subject)}">'
    )


def form_privacy_note():
    return (
        '<p class="form-privacy-note" style="font-size:0.8125rem;color:var(--text-muted);margin-top:0.75rem">'
        'By submitting you agree to our <a href="privacy.html">privacy policy</a>. '
        'We never sell your information.</p>'
    )


def analytics_snippet():
    if not GA_MEASUREMENT_ID:
        return ""
    gid = hescape(GA_MEASUREMENT_ID)
    return f"""    <script async src="https://www.googletagmanager.com/gtag/js?id={gid}"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{gid}');</script>"""


def favicon_links(depth=0):
    p = prefix(depth)
    return f"""    <link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
    <link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.svg">"""


def comparison_table_html():
    rows = "".join(
        f"<tr><th>{hescape(feature)}</th><td>{hescape(tsbr)}</td><td>{hescape(other)}</td></tr>"
        for feature, tsbr, other in COMPARISON_ROWS
    )
    return (
        '<div class="comparison-table-wrap"><table class="comparison-table">'
        "<thead><tr><th>Feature</th><th>TSBR</th><th>Typical agency</th></tr></thead>"
        f"<tbody>{rows}</tbody></table></div>"
    )


def gmb_signals_html(limit=None):
    items = GMB_SIGNALS[:limit] if limit else GMB_SIGNALS
    return (
        '<ul class="signal-list">'
        + "".join(f'<li><span class="check">&#10003;</span><span>{hescape(s)}</span></li>' for s in items)
        + "</ul>"
    )


def keyword_intents_html(markets=None, depth=0):
    if markets is None:
        data = KEYWORD_INTENTS
    elif isinstance(markets, str):
        data = {markets: KEYWORD_INTENTS.get(markets, [])}
    else:
        data = markets
    parts = []
    for market, keywords in data.items():
        kws = "".join(f'<span class="keyword-pill">{hescape(k)}</span>' for k in keywords)
        parts.append(f'<div class="keyword-market"><h3>{hescape(market)}</h3><div class="keyword-grid">{kws}</div></div>')
    return '<div class="keyword-intents">' + "".join(parts) + "</div>"


def engagement_timeline_html():
    return (
        '<div class="engagement-timeline">'
        + "".join(
            f'<div class="engagement-phase"><div class="phase-label">{hescape(phase)}</div><p>{hescape(desc)}</p></div>'
            for phase, desc in ENGAGEMENT_MONTHS
        )
        + "</div>"
    )


def media_gallery_html(depth=0, limit=None):
    p = prefix(depth)
    items = MEDIA_GALLERY[:limit] if limit else MEDIA_GALLERY
    cells = "".join(
        f'<figure class="gallery-cell"><img src="{p}{src}" alt="{hescape(alt)}" loading="lazy" width="400" height="300"></figure>'
        for src, alt in items
    )
    return f'<div class="media-gallery">{cells}</div>'


def video_showcase_html(depth=0, limit=None):
    p = prefix(depth)
    items = VIDEO_ASSETS[:limit] if limit else VIDEO_ASSETS
    cards = ""
    for src, poster, caption in items:
        cards += (
            f'<figure class="video-card"><video controls preload="metadata" poster="{p}{poster}" width="640" height="360">'
            f'<source src="{p}{src}" type="video/mp4"></video>'
            f"<figcaption>{hescape(caption)}</figcaption></figure>"
        )
    return f'<div class="video-showcase">{cards}</div>'


def eeat_grid_html():
    return (
        '<div class="eeat-grid">'
        + "".join(
            f'<div class="eeat-item"><strong>{hescape(stat)}</strong><span>{hescape(desc)}</span></div>'
            for stat, desc in EEAT_CREDENTIALS
        )
        + "</div>"
    )


def maps_embed_html():
    return (
        f'<div class="maps-embed"><iframe src="{hescape(GOOGLE_MAPS_EMBED)}" width="100%" height="360" '
        'style="border:0" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" '
        'title="TSBR Arlington office on Google Maps"></iframe></div>'
    )


def service_extra_sections(filename):
    if filename == "gmb-optimization.html":
        return f"""
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">20 GMB signals we engineer</h2>
                {gmb_signals_html()}
            </div>
        </section>"""
    if filename == "local-seo-texas.html":
        return f"""
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">Buyer-intent keywords by Texas metro</h2>
                <p class="text-center" style="max-width:42rem;margin:0 auto 2rem;color:var(--text-muted)">Commercial searches we optimize for Texas B2B companies.</p>
                {keyword_intents_html()}
            </div>
        </section>"""
    if filename == "b2b-lead-generation.html":
        return f"""
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">90-day engagement roadmap</h2>
                {engagement_timeline_html()}
            </div>
        </section>"""
    if filename == "ai-search-optimization.html":
        ai_faqs = [item for item in EXTRA_FAQ if "AI" in item[0]][:4]
        return f"""
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">AI search FAQ</h2>
                <div class="faq-list">{faq_html(ai_faqs)}</div>
            </div>
        </section>"""
    return ""


def build_index():
    home_url = page_url()
    schema = schema_extra(
        schema_organization(),
        schema_website(),
        schema_webpage(
            "The Stone Builders Rejected | Texas Local SEO & GMB Experts",
            "Mike Kaswatuka helps Texas B2B companies dominate Google Maps, local search, and AI Overviews.",
            home_url,
        ),
        schema_faq(HOME_FAQ + EXTRA_FAQ[:4]),
        schema_item_list("TSBR Services", [(SERVICE_META[f]["h1"], f) for f in SERVICE_META]),
        schema_item_list("Texas Service Areas", [(LOCATION_META[f]["short"], f) for f in LOCATION_META]),
    )

    process_html = "".join(
        f'<div class="step"><div class="step-num">{i}</div><h3>{s["title"]}</h3><p>{s["paragraph"]}</p></div>'
        for i, s in enumerate(PROCESS_STEPS, 1)
    )
    why_html = "".join(
        f'<div class="card"><h3>{w["title"]}</h3><p>{w["paragraph"]}</p></div>'
        for w in WHY_TSBR[:3]
    )
    case_previews = "".join(case_study_html(c, full=False) for c in CASE_STUDIES[:2])
    blog_cards = "".join(
        f'<a href="blog/{a["slug"]}" class="card card-link blog-card"><div class="tag">{a["tag"]}</div>'
        f'<h3 style="margin-top:0.75rem">{a["title"]}</h3><p>{a["desc"]}</p>'
        f'<span class="link-arrow">Read article &rarr;</span></a>'
        for a in BLOG_ARTICLES[:3]
    )
    loc_cards = "".join(
        f'<a href="{fn}" class="card card-link"><h3>{LOCATION_META[fn]["short"]}</h3>'
        f'<p>{join_text(LOCATION_RICH[fn]["local_intro"])[:120]}...</p><span class="link-arrow">View market &rarr;</span></a>'
        for fn in list(LOCATION_RICH)[:6]
    )

    content = head(
        "The Stone Builders Rejected | Texas Local SEO & GMB Experts",
        "Mike Kaswatuka helps Texas B2B companies dominate Google Maps, local search, and AI Overviews. GMB optimization, local SEO, and lead generation across DFW, Houston, Austin, and statewide.",
        canonical=home_url,
        extra=schema,
    ) + header(active="home") + f"""
    <main id="main">
        {breadcrumb_html([("Home", None)])}
        <section class="hero">
            <div class="container">
                <div class="hero-grid">
                    <div>
                        <span class="hero-eyebrow">Texas B2B Local Search &middot; Arlington HQ</span>
                        <h1>Turn overlooked companies into market cornerstones.</h1>
                        <p class="hero-lead">Michael Kaswatuka and The Stone Builders Rejected help serious Texas B2B businesses rank in Google Maps, win organic local search, and get cited in AI Overviews &mdash; so commercial buyers find you first, not your competitors.</p>
                        {aeo_summary_html("The Stone Builders Rejected (TSBR) is a Texas B2B local SEO agency in Arlington that optimizes Google Business Profiles, builds citation and content silos, and engineers AI Overview visibility so commercial buyers find your company first across DFW, Houston, Austin, San Antonio, and statewide.")}
                        <div class="hero-actions">
                            <a href="contact.html" class="btn btn-primary">Get Your Free Audit</a>
                            <a href="case-studies.html" class="btn btn-secondary">See Results</a>
                        </div>
                    </div>
                    <div class="hero-video-wrap">
                        <video autoplay muted loop playsinline preload="metadata" poster="assets/images/hero-branded-8.jpg" width="640" height="360">
                            <source src="assets/videos/hero-branded-stone-1.mp4" type="video/mp4">
                        </video>
                        <div class="overlay"><span>Mike Kaswatuka &middot; The Stone Builders Rejected &middot; Arlington, TX</span></div>
                    </div>
                </div>
            </div>
        </section>

        <div class="trust-bar">
            <div class="container trust-items">
                <div><strong>12+</strong><span>Years Texas local SEO</span></div>
                <div><strong>500+</strong><span>B2B companies served</span></div>
                <div><strong>10</strong><span>Major Texas metros</span></div>
                <div><strong>90 days</strong><span>Avg. Map Pack dominance</span></div>
                <div><strong>4.3&times;</strong><span>Avg. lead volume lift</span></div>
            </div>
        </div>

        <section class="section" id="services">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">What We Do</div>
                    <h2>Local search systems built for Texas B2B</h2>
                    <p>Every strategy is engineered around how commercial buyers actually search in Texas &mdash; not generic national playbooks. GMB is the foundation; AI visibility is the future; leads are the outcome.</p>
                </div>
                <div class="card-grid card-grid-2">
                    <a href="gmb-optimization.html" class="card card-link">
                        <div class="card-icon">&#128205;</div>
                        <h3>Google Business Profile Optimization</h3>
                        <p>Complete GMB engineering &mdash; 50+ photos, weekly posts, review velocity, category optimization, and Map Pack signals that move you into the top 3 across DFW, Houston, Austin, and beyond.</p>
                        <span class="link-arrow">Full GMB service &rarr;</span>
                    </a>
                    <a href="ai-search-optimization.html" class="card card-link">
                        <div class="card-icon">&#10022;</div>
                        <h3>AI Overview &amp; Generative Search</h3>
                        <p>Entity strength, structured content, FAQ schema, and authority signals so Google AI Overviews and generative search cite your business as the trusted Texas answer.</p>
                        <span class="link-arrow">AI search service &rarr;</span>
                    </a>
                    <a href="local-seo-texas.html" class="card card-link">
                        <div class="card-icon">&#9678;</div>
                        <h3>Local SEO for Texas</h3>
                        <p>70+ citations, NAP consistency, location pages, content silos, and technical SEO tailored to every Texas metro you serve.</p>
                        <span class="link-arrow">Local SEO service &rarr;</span>
                    </a>
                    <a href="b2b-lead-generation.html" class="card card-link">
                        <div class="card-icon">&#8599;</div>
                        <h3>B2B Lead Generation Systems</h3>
                        <p>Search-driven lead systems that deliver qualified commercial inquiries &mdash; industrial buyers, project managers, and procurement teams, not vanity traffic.</p>
                        <span class="link-arrow">B2B leads service &rarr;</span>
                    </a>
                </div>
            </div>
        </section>

        <section class="section section-alt">
            <div class="container media-section">
                <div>
                    <div class="eyebrow">Why TSBR</div>
                    <h2>Built for the companies big agencies ignore</h2>
                    <p>The name comes from Psalm 118:22 &mdash; the stone the builders rejected became the cornerstone. We turn overlooked Texas B2B companies into the dominant, trusted choice in their markets.</p>
                    <p>Direct access to Mike Kaswatuka. Map Pack positions, AI citations, and qualified leads &mdash; not vanity metrics.</p>
                    <a href="about.html" class="btn btn-secondary" style="margin-top:1rem">Our story</a>
                </div>
                <div class="media-frame">
                    <img src="assets/images/hero-branded-aggressive-10.jpg" alt="The Stone Builders Rejected Texas local SEO agency" width="800" height="600" loading="lazy" decoding="async">
                </div>
            </div>
        </section>

        <section class="section section-alt" id="process">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">How It Works</div>
                    <h2>A clear path from invisible to dominant</h2>
                    <p>Our five-phase framework has delivered consistent Map Pack and AI Overview results for industrial suppliers, contractors, manufacturers, and professional services firms across Texas.</p>
                </div>
                <div class="steps" style="grid-template-columns:1fr">
                    {process_html}
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Differentiators</div>
                    <h2>Why Texas B2B companies choose TSBR</h2>
                </div>
                <div class="card-grid card-grid-3">
                    {why_html}
                </div>
            </div>
        </section>

        <section class="section section-alt">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Case Studies</div>
                    <h2>Real outcomes for Texas B2B companies</h2>
                </div>
                {case_previews}
                <p class="text-center" style="margin-top:2rem"><a href="case-studies.html" class="btn btn-secondary">All case studies</a></p>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Texas Markets</div>
                    <h2>Where we deliver results</h2>
                    <p>Headquartered in Arlington. Serving every major Texas metro.</p>
                </div>
                <div class="card-grid card-grid-3">
                    {loc_cards}
                </div>
                <p class="text-center" style="margin-top:2rem"><a href="locations.html" class="btn btn-secondary">All service areas</a></p>
            </div>
        </section>

        <section class="section section-alt">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Client Voices</div>
                    <h2>What Texas business owners say</h2>
                </div>
                <div class="card-grid card-grid-3">
                    {testimonials_html(TESTIMONIALS[:3])}
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Insights</div>
                    <h2>Latest from the blog</h2>
                </div>
                <div class="card-grid card-grid-3">
                    {blog_cards}
                </div>
                <p class="text-center" style="margin-top:2rem"><a href="blog.html" class="btn btn-secondary">All articles</a></p>
            </div>
        </section>

        <section class="section section-alt">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Authority</div>
                    <h2>Why Texas B2B companies trust TSBR</h2>
                </div>
                {eeat_grid_html()}
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">In action</div>
                    <h2>See the GMB Velocity System at work</h2>
                </div>
                {video_showcase_html(limit=3)}
            </div>
        </section>

        <section class="section section-alt">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Gallery</div>
                    <h2>Texas B2B search dominance in practice</h2>
                </div>
                {media_gallery_html(limit=8)}
            </div>
        </section>

        <section class="section section-alt" id="faq">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">FAQ</div>
                    <h2>Common questions</h2>
                </div>
                <div class="faq-list">
                    {faq_html(HOME_FAQ + EXTRA_FAQ[:4])}
                </div>
                <p class="text-center" style="margin-top:1.5rem"><a href="contact.html">More questions? Get in touch &rarr;</a></p>
            </div>
        </section>

        <section class="bg-image-section" style="background-image:url('assets/images/estimation-bg.jpg')">
            <div class="container two-col two-col-wide">
                <div>
                    <h2>Your free audit includes everything.</h2>
                    <p>Every audit request gets a personal review of your local search landscape across Texas.</p>
                    {audit_list_html()}
                </div>
                <div class="form-card">
                    <h3 style="margin-top:0">Request your free audit</h3>
                    <p style="color:var(--text-muted);font-size:0.9375rem">Custom estimate within 24 hours on weekdays.</p>
                    <a href="contact.html" class="btn btn-primary" style="width:100%;margin-top:1rem">Go to contact form</a>
                    <p style="text-align:center;margin:1rem 0 0;font-size:0.875rem">Or call <a href="tel:{PHONE_TEL}">{PHONE}</a></p>
                </div>
            </div>
        </section>

        <section class="cta-band" id="contact">
            <div class="container">
                <h2>Ready to become the cornerstone of your market?</h2>
                <p>Request a free audit of your Google Business Profile, local visibility, and AI Overview potential.</p>
                <a href="contact.html" class="btn btn-primary">Request Free Audit</a>
            </div>
        </section>
    </main>
""" + footer()
    write(ROOT / "index.html", content)


def build_about():
    timeline = "".join(f'<div class="timeline-item"><h3>{y}</h3><p>{e}</p></div>' for y, e in ABOUT_TIMELINE)
    values = "".join(f'<div class="card"><h3>{v["title"]}</h3><p>{v["description"]}</p></div>' for v in ABOUT_VALUES)
    body = f"""
        <section class="section">
            <div class="container two-col two-col-wide">
                <div class="prose-wide">
                    <h2>Founded on Texas grit &amp; biblical truth</h2>
                    <p>The name &ldquo;The Stone Builders Rejected&rdquo; comes from Psalm 118:22 and Matthew 21:42 &mdash; the stone tossed aside that became the cornerstone of the building.</p>
                    <p>That is exactly what we see every day in Texas business. Great companies with incredible expertise, hard-working owners, and real value for other businesses are completely overlooked by Google because their online presence is weak, outdated, or managed by agencies that do not understand B2B local search.</p>
                    <p>Since 2012, we have specialized in turning those rejected stones into dominant players in their local markets &mdash; particularly in the high-stakes B2B space where commercial leads are worth thousands of dollars each.</p>
                    <p>We are not a generalist marketing agency. We do one thing exceptionally well: make Texas B2B companies the most visible, trusted, and cited business in their market across Google Maps, organic search, and AI Overviews.</p>
                </div>
                <div class="card">
                    <div class="eyebrow" style="font-size:0.75rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent)">Founder &amp; Principal</div>
                    <h2 style="margin-top:0.5rem">Mike Kaswatuka</h2>
                    <p style="color:var(--text-muted);margin-bottom:1rem">Arlington, Texas</p>
                    <p>Mike has spent over a decade studying and executing local search strategy exclusively for Texas businesses. He has personally guided hundreds of B2B companies to the top of Google Maps and into AI-generated answers.</p>
                    <p>Clients work directly with Mike &mdash; not a junior account manager. That direct access is a core part of how we deliver results faster than traditional agencies.</p>
                    <div style="margin-top:1.25rem;display:flex;flex-wrap:wrap;gap:0.5rem">
                        <span class="badge">Google Business Profile Strategy</span>
                        <span class="badge">Entity &amp; AI Optimization</span>
                        <span class="badge">B2B Local Lead Systems</span>
                        <span class="badge">Multi-Market Texas SEO</span>
                    </div>
                </div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">Our timeline</h2>
                <div class="timeline" style="max-width:40rem;margin:0 auto">
                    {timeline}
                </div>
            </div>
        </section>
        <section class="section">
            <div class="container">
                <h2 class="text-center mb-lg">Our values</h2>
                <div class="card-grid card-grid-2">
                    {values}
                </div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">Our approach</h2>
                <div class="card-grid card-grid-3">
                    <div class="card"><h3>Deep Texas market intelligence</h3><p>We do not use generic national playbooks. Every strategy is built around how buyers actually search in DFW, Houston, Austin, San Antonio, and secondary Texas markets.</p></div>
                    <div class="card"><h3>Google Business Profile as the foundation</h3><p>GMB is the single highest-ROI asset for most Texas B2B companies. We obsess over every signal: photos, posts, products, services, Q&amp;A, reviews, and categories.</p></div>
                    <div class="card"><h3>Future-proof for AI</h3><p>We build content, citations, and entity strength so your business becomes the source Google AI Overviews and other models trust and cite.</p></div>
                </div>
            </div>
        </section>
        <section class="section">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Founder</div>
                    <h2>Meet Michael K. Kaswatuka</h2>
                </div>
                {founder_bio_html()}
                <div class="prose-wide" style="margin-top:2rem">
                    {FOUNDER_BIO_HTML}
                </div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">E-E-A-T credentials</h2>
                {eeat_grid_html()}
            </div>
        </section>
        <section class="section">
            <div class="container">
                <h2 class="text-center mb-lg">TSBR vs. typical agencies</h2>
                <p class="text-center" style="max-width:42rem;margin:0 auto 2rem;color:var(--text-muted)">Why Texas B2B companies choose a specialist over a generalist marketing firm.</p>
                {comparison_table_html()}
            </div>
        </section>
        <section class="cta-band">
            <div class="container">
                <h2>We are builders of cornerstones.</h2>
                <p>If you are a serious Texas B2B company ready to stop being overlooked and start owning your market, we would like to talk.</p>
                <a href="contact.html" class="btn btn-primary">Get in Touch</a>
            </div>
        </section>"""
    about_url = page_url("about.html")
    about_schema = schema_extra(
        schema_organization(),
        schema_webpage(
            "About The Stone Builders Rejected",
            "Learn the story behind TSBR Enterprises founded by Mike Kaswatuka in Arlington, Texas.",
            about_url,
        ),
        {
            "@type": "Person",
            "@id": f"{DOMAIN}/#founder",
            "name": FOUNDER["name"],
            "jobTitle": FOUNDER["title"],
            "worksFor": {"@id": f"{DOMAIN}/#organization"},
            "image": page_url(FOUNDER["image"]),
            "description": "Founder of TSBR Enterprises. Texas local SEO and Google Business Profile expert.",
            "knowsAbout": ["Local SEO", "Google Business Profile", "AI Search Optimization"],
        },
        schema_breadcrumb([("Home", "index.html"), ("About", None)]),
    )
    write(ROOT / "about.html", page_template(
        "About The Stone Builders Rejected | Mike Kaswatuka | Texas Local SEO",
        "Learn the story behind TSBR Enterprises. Founded by Mike Kaswatuka in Arlington, Texas. 12+ years helping Texas B2B companies dominate Google Maps and AI Overviews.",
        "Our Story", "The stone the builders rejected has become the cornerstone.",
        "We started in Arlington with one mission: help the good local businesses that big agencies ignore become the most visible and trusted companies in their Texas markets.",
        body, active="about", canonical=about_url,
        breadcrumbs=[("Home", "index.html"), ("About", None)],
        aeo_summary="The Stone Builders Rejected is a Texas B2B local SEO agency founded by Mike Kaswatuka in Arlington. Since 2012, TSBR helps overlooked industrial and commercial companies dominate Google Maps, organic search, and AI Overviews statewide.",
        silo_nav={
            "heading": "Explore TSBR",
            "links": [
                ("Services", "services.html"), ("Case studies", "case-studies.html"),
                ("Client reviews", "testimonials.html"), ("Contact", "contact.html"),
            ],
        },
        extra=about_schema,
    ))


def build_services():
    cards = ""
    for fn, svc in SERVICE_RICH.items():
        meta = SERVICE_META[fn]
        cards += f"""
                    <a href="{fn}" class="card card-link">
                        <h3>{meta["h1"]}</h3>
                        <p>{join_text(svc["intro"])[:220]}...</p>
                        <span class="link-arrow">View full service &rarr;</span>
                    </a>"""
    deliverables_sample = "".join(f"<li>{d}</li>" for d in SERVICE_RICH["gmb-optimization.html"]["deliverables"][:6])
    body = f"""
        <section class="section">
            <div class="container">
                <div class="prose-wide" style="max-width:48rem;margin:0 auto 3rem;text-align:center">
                    <p>Four integrated services. One outcome: your company becomes the obvious choice when Texas B2B buyers search on Google, Maps, or AI.</p>
                </div>
                <div class="card-grid card-grid-2">
                    {cards}
                </div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container two-col two-col-wide">
                <div>
                    <h2>What every engagement includes</h2>
                    <ul>{deliverables_sample}</ul>
                    <p>Plus competitive analysis, custom strategy, direct founder access, monthly reporting, and ongoing optimization.</p>
                </div>
                <div class="stat-band">
                    <div><strong>28&ndash;67</strong><span>Days to first Map Pack movement</span></div>
                    <div><strong>45&ndash;75</strong><span>Days to AI Overview visibility</span></div>
                    <div><strong>4.3&times;</strong><span>Avg. qualified lead increase</span></div>
                    <div><strong>90</strong><span>Days to dominant positions</span></div>
                </div>
            </div>
        </section>
        <section class="section">
            <div class="container">
                <h2 class="text-center mb-lg">Our five-phase process</h2>
                <div class="steps">
                    {"".join(f'<div class="step"><div class="step-num">{i}</div><h3>{s["title"]}</h3><p>{s["paragraph"]}</p></div>' for i, s in enumerate(PROCESS_STEPS, 1))}
                </div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">90-day engagement roadmap</h2>
                {engagement_timeline_html()}
            </div>
        </section>
        <section class="section">
            <div class="container">
                <h2 class="text-center mb-lg">TSBR vs. typical agencies</h2>
                {comparison_table_html()}
            </div>
        </section>
        <section class="cta-band">
            <div class="container">
                <h2>Not sure which service you need?</h2>
                <p>We will audit your current visibility and recommend the highest-impact starting point for your Texas markets.</p>
                <a href="contact.html" class="btn btn-primary">Request Free Audit</a>
            </div>
        </section>"""
    services_url = page_url("services.html")
    services_schema = schema_extra(
        schema_organization(),
        schema_webpage(
            "TSBR Services — Texas GMB, AI Search & Local SEO",
            "Google Business Profile optimization, AI Overview engineering, local SEO, and B2B lead systems for Texas companies.",
            services_url,
        ),
        schema_item_list("TSBR Services", [(SERVICE_META[f]["h1"], f) for f in SERVICE_META]),
        schema_breadcrumb([("Home", "index.html"), ("Services", None)]),
    )
    write(ROOT / "services.html", page_template(
        "Services | Texas GMB, AI Search & Local SEO | TSBR",
        "Google Business Profile optimization, AI Overview engineering, local SEO, and B2B lead systems for Texas companies. Full deliverables and timelines.",
        "Services", "Everything you need to own local search in Texas",
        "Four core services, one goal: make your company the obvious choice when buyers search.",
        body, active="services", canonical=services_url,
        breadcrumbs=[("Home", "index.html"), ("Services", None)],
        aeo_summary="TSBR offers four integrated Texas B2B services: Google Business Profile optimization, AI search and generative engine optimization, full local SEO, and B2B lead generation — engineered to win Map Pack, organic, and AI Overview visibility.",
        silo_nav={
            "heading": "Service silo — dive deeper",
            "links": [(SERVICE_META[f]["h1"], f) for f in SERVICE_META] + [
                ("Texas locations", "locations.html"), ("Free audit", "contact.html"),
            ],
        },
        extra=services_schema,
    ))


def build_contact():
    body = f"""
        <section class="section">
            <div class="container two-col two-col-wide">
                <div>
                    <h2>Let&rsquo;s make your company the obvious choice in Texas.</h2>
                    <p>Fill out the form or call us directly. We will perform a complete audit of your current Google Business Profile, website authority, citations, review velocity, AI visibility, and competitor landscape across your Texas service areas.</p>
                    <h3>Your free audit includes:</h3>
                    {audit_list_html()}
                    <dl class="contact-info" style="margin-top:2rem">
                        <dt>Phone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd>
                        <dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
                        <dt>Office</dt><dd>{ADDRESS}</dd>
                    </dl>
                    <p style="font-size:0.875rem;color:var(--text-muted)">We typically respond to audit requests within 4 business hours on weekdays. Custom detailed estimate within 24 hours.</p>
                </div>
                <div class="form-card">
                    {form_open("TSBR Free Audit Request")}
                        <div class="form-grid form-grid-2">
                            <div class="form-group"><label>Your Name</label><input type="text" name="name" required></div>
                            <div class="form-group"><label>Business Name</label><input type="text" name="business" required></div>
                            <div class="form-group"><label>Phone</label><input type="tel" name="phone" required></div>
                            <div class="form-group"><label>Website</label><input type="url" name="website" placeholder="https://"></div>
                        </div>
                        <div class="form-group" style="margin-top:1rem">
                            <label>Primary City / Metro in Texas</label>
                            <select name="city" required>
                                <option value="">Select...</option>
                                <option>Arlington / DFW</option><option>Dallas</option><option>Fort Worth</option>
                                <option>Plano / Frisco</option><option>Houston</option><option>The Woodlands / Katy</option>
                                <option>Austin</option><option>Round Rock / Cedar Park</option>
                                <option>San Antonio</option><option>Other Texas market</option><option>Statewide / Multi-market</option>
                            </select>
                        </div>
                        <div class="form-group" style="margin-top:1rem">
                            <label>Industry</label>
                            <input type="text" name="industry" placeholder="e.g. Industrial equipment, commercial contracting">
                        </div>
                        <div class="form-group" style="margin-top:1rem">
                            <label>Services of interest</label>
                            <div class="checkbox-grid">
                                <label><input type="checkbox" name="interest" value="GMB"> Google Business Profile</label>
                                <label><input type="checkbox" name="interest" value="AI"> AI Overview Optimization</label>
                                <label><input type="checkbox" name="interest" value="Local SEO"> Local SEO</label>
                                <label><input type="checkbox" name="interest" value="Leads"> B2B Lead Generation</label>
                            </div>
                        </div>
                        <div class="form-group" style="margin-top:1rem">
                            <label>What is your biggest local search challenge?</label>
                            <textarea name="message" rows="5" placeholder="Tell us about your business, target markets, and goals..."></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width:100%;margin-top:1.25rem">Request Free Audit</button>
                        {form_privacy_note()}
                    </form>
                </div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container two-col two-col-wide">
                <div>
                    <h2>Visit our Arlington headquarters</h2>
                    <p>On-site consultations available for DFW B2B companies. Schedule through the form or call directly.</p>
                    <dl class="contact-info">
                        <dt>Address</dt><dd>{ADDRESS}</dd>
                        <dt>Phone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd>
                    </dl>
                </div>
                <div>{maps_embed_html()}</div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">What happens after you submit</h2>
                <div class="steps">
                    <div class="step"><div class="step-num">1</div><h3>Within 4 business hours</h3><p>We acknowledge your request and schedule a strategy call with Mike Kaswatuka or a senior strategist.</p></div>
                    <div class="step"><div class="step-num">2</div><h3>Within 24 hours</h3><p>You receive a written audit summary covering GMB health, Map Pack snapshot, citations, competitors, and AI visibility.</p></div>
                    <div class="step"><div class="step-num">3</div><h3>Within 48 hours</h3><p>Custom scope recommendation with 90-day roadmap, deliverables, timeline, and investment range — no obligation.</p></div>
                </div>
            </div>
        </section>
        <section class="section">
            <div class="container">
                <h2 class="text-center mb-lg">Questions before you reach out?</h2>
                <div class="faq-list">{faq_html(FULL_FAQ[:10])}</div>
                <p class="text-center" style="margin-top:1.5rem"><a href="index.html#faq">More FAQs on homepage</a></p>
            </div>
        </section>"""
    contact_url = page_url("contact.html")
    contact_schema = schema_extra(
        schema_organization(),
        schema_webpage(
            "Contact TSBR — Free Texas GMB & Local SEO Audit",
            f"Contact TSBR Enterprises in Arlington, Texas. Request your free Google Business Profile audit. Call {PHONE}.",
            contact_url,
        ),
        schema_faq(FULL_FAQ[:10]),
        schema_breadcrumb([("Home", "index.html"), ("Contact", None)]),
    )
    write(ROOT / "contact.html", page_template(
        "Contact | Free Texas GMB & Local SEO Audit",
        f"Contact TSBR Enterprises in Arlington, Texas. Request your free Google Business Profile audit. Call {PHONE}.",
        "Contact", "Request your free local search audit",
        "No obligation. We review your GMB profile, rankings, citations, competitors, and AI visibility &mdash; then tell you exactly what to fix.",
        body, canonical=contact_url, extra=contact_schema,
        breadcrumbs=[("Home", "index.html"), ("Contact", None)],
        aeo_summary=f"Contact The Stone Builders Rejected at {PHONE} or hello@tsbrenterprises.com for a free Texas B2B local SEO audit covering Google Business Profile health, Map Pack rankings, citations, competitors, and AI Overview visibility.",
        silo_nav={
            "heading": "Before you contact us",
            "links": [
                ("Services overview", "services.html"), ("Case studies", "case-studies.html"),
                ("Client reviews", "testimonials.html"), ("FAQ on homepage", "index.html#faq"),
            ],
        },
    ))


def estimation_form_html():
    return f"""
                    {form_open("TSBR Estimation Request", "estimation-form")}
                        <div class="form-grid form-grid-2">
                            <div class="form-group"><label>Your Name</label><input type="text" name="name" required></div>
                            <div class="form-group"><label>Business Name</label><input type="text" name="business" required></div>
                            <div class="form-group"><label>Phone</label><input type="tel" name="phone" required></div>
                            <div class="form-group"><label>Email</label><input type="email" name="email" required></div>
                        </div>
                        <div class="form-group" style="margin-top:1rem">
                            <label>Texas Metro / Service Area</label>
                            <select name="city" required>
                                <option value="">Select...</option>
                                <option>Arlington / DFW</option><option>Houston</option><option>Austin</option>
                                <option>San Antonio</option><option>Statewide</option>
                            </select>
                        </div>
                        <div class="form-group" style="margin-top:1rem">
                            <label>Project scope &amp; goals</label>
                            <textarea name="message" rows="4" placeholder="Tell us about your markets, services, and visibility goals..." required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary btn-crimson" style="width:100%;margin-top:1.25rem">Request Custom Estimate</button>
                        {form_privacy_note()}
                    </form>"""


def contact_form_html():
    return f"""
                    {form_open("TSBR Contact — Testimonials Page")}
                        <div class="form-group"><label>Your Name</label><input type="text" name="name" required></div>
                        <div class="form-group" style="margin-top:1rem"><label>Email</label><input type="email" name="email" required></div>
                        <div class="form-group" style="margin-top:1rem"><label>Phone</label><input type="tel" name="phone"></div>
                        <div class="form-group" style="margin-top:1rem">
                            <label>Message</label>
                            <textarea name="message" rows="4" placeholder="How can we help your Texas B2B business?" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary btn-crimson" style="width:100%;margin-top:1.25rem">Send Message</button>
                        {form_privacy_note()}
                    </form>"""


def build_testimonials():
    meta_title = "Client Success & Reviews | TSBR Enterprises Authority"
    meta_desc = (
        "Read verified client reviews and success stories from TSBR Enterprises. "
        "Texas B2B companies trust The Stone Builders Rejected for GMB optimization, "
        "AI search visibility, and measurable local SEO results across DFW, Houston, and Austin."
    )
    h1 = "Proven results from Texas B2B leaders"
    tldr = (
        "See how we&rsquo;ve transformed local search visibility for industrial, contracting, "
        "and professional services firms across Texas &mdash; turning overlooked companies into "
        "Map Pack cornerstones with documented lead growth."
    )

    reviews_url = page_url("testimonials.html")
    review_nodes = [
        {
            "@type": "Review",
            "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
            "author": {"@type": "Person", "name": t["author"]},
            "reviewBody": t["quote"][:200],
        }
        for t in TESTIMONIALS[:6]
    ]
    biz_with_reviews = schema_organization()
    biz_with_reviews["aggregateRating"] = {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "reviewCount": str(len(TESTIMONIALS)),
        "bestRating": "5",
    }
    biz_with_reviews["review"] = review_nodes
    schema = schema_extra(
        biz_with_reviews,
        {
            "@type": "Person",
            "@id": f"{DOMAIN}/#founder",
            "name": FOUNDER["name"],
            "jobTitle": FOUNDER["title"],
            "worksFor": {"@id": f"{DOMAIN}/#organization"},
            "image": page_url(FOUNDER["image"]),
            "description": "Founder of TSBR Enterprises. Texas local SEO and Google Business Profile expert.",
        },
        schema_webpage(meta_title, meta_desc, reviews_url),
        schema_breadcrumb([("Home", "index.html"), ("Reviews", None)]),
    )

    service_cards = ""
    for fn, svc in SERVICE_RICH.items():
        meta = SERVICE_META[fn]
        service_cards += f"""
                    <a href="{fn}" class="card card-link">
                        <h3>{meta["h1"]}</h3>
                        <p>{join_text(svc["intro"])[:200]}...</p>
                        <span class="link-arrow">Explore service &rarr;</span>
                    </a>"""

    benefits = "".join(
        f'<div class="benefit-item"><span class="benefit-icon">&#10003;</span>'
        f'<div><strong>{w["title"]}</strong><p>{w["paragraph"][:160]}...</p></div></div>'
        for w in WHY_TSBR[:4]
    )

    loc_cards = "".join(
        f'<a href="{fn}" class="card card-link"><h3>{LOCATION_META[fn]["short"]}</h3>'
        f'<p>{join_text(LOCATION_RICH[fn]["local_intro"])[:100]}...</p></a>'
        for fn in list(LOCATION_RICH)[:6]
    )

    portfolio = "".join(
        f'<article class="portfolio-card">'
        f'<div class="portfolio-img"><img src="assets/images/hero-branded-{8 + i}.jpg" alt="{CASE_STUDIES[i]["title"]}" loading="lazy"></div>'
        f'<div class="portfolio-body"><span class="tag">{CASE_STUDIES[i]["tag"]}</span>'
        f'<h3>{CASE_STUDIES[i]["title"]}</h3>'
        f'<p>{CASE_STUDIES[i]["challenge"][:140]}...</p>'
        f'<a href="case-studies.html" class="link-arrow">View case study &rarr;</a></div></article>'
        for i in range(min(3, len(CASE_STUDIES)))
    )

    process_html = "".join(
        f'<div class="step"><div class="step-num">{i}</div><h3>{s["title"]}</h3><p>{s["paragraph"][:200]}...</p></div>'
        for i, s in enumerate(PROCESS_STEPS, 1)
    )

    body = f"""
        <section class="section">
            <div class="container">
                <div class="tldr-box">
                    <strong>TL;DR</strong>
                    <p>{tldr}</p>
                </div>
            </div>
        </section>

        <section class="section section-alt" id="gmb-reviews">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Google Reviews</div>
                    <h2>Verified Google Business Profile reviews</h2>
                    <p>Real feedback from Texas B2B clients who partnered with The Stone Builders Rejected.</p>
                </div>
                <div class="gmb-widget">
                    <div class="gmb-widget-header">
                        <span class="gmb-logo">G</span>
                        <div>
                            <strong>The Stone Builders Rejected</strong>
                            <span class="gmb-rating">5.0 &middot; {len(TESTIMONIALS)}+ reviews on Google</span>
                        </div>
                        <a href="https://www.google.com/maps/search/?api=1&amp;query=The+Stone+Builders+Rejected+Arlington+TX" class="btn btn-secondary btn-sm" target="_blank" rel="noopener">View on Google</a>
                    </div>
                    <div class="gmb-reviews-grid">
                        {gmb_reviews_html(TESTIMONIALS, 6)}
                    </div>
                </div>
            </div>
        </section>

        <section class="section" id="client-quotes">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Client Success</div>
                    <h2>What Texas business leaders say</h2>
                    <p>Large-format testimonials from industrial, contracting, and professional services firms across the Lone Star State.</p>
                </div>
                <div class="quote-cards-grid">
                    {quote_cards_html(TESTIMONIALS)}
                </div>
            </div>
        </section>

        <section class="section section-alt" id="founder">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Authority Behind the Results</div>
                    <h2>Meet the founder</h2>
                </div>
                {founder_bio_html()}
            </div>
        </section>

        <div class="trust-bar">
            <div class="container trust-items">
                <div><strong>12+</strong><span>Years Texas local SEO</span></div>
                <div><strong>500+</strong><span>B2B companies served</span></div>
                <div><strong>10</strong><span>Major Texas metros</span></div>
                <div><strong>4.3&times;</strong><span>Avg. lead volume lift</span></div>
                <div><strong>5.0</strong><span>Google review rating</span></div>
            </div>
        </div>

        <section class="section" id="services">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Services</div>
                    <h2>Digital marketing &amp; local search authority</h2>
                    <p>Four integrated services engineered for Texas B2B companies ready to own Maps, organic search, and AI Overviews.</p>
                </div>
                <div class="card-grid card-grid-2">
                    {service_cards}
                </div>
            </div>
        </section>

        <section class="section section-alt" id="benefits">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Why Clients Choose TSBR</div>
                    <h2>Service features &amp; benefits</h2>
                </div>
                <div class="benefits-grid">
                    {benefits}
                </div>
            </div>
        </section>

        <section class="section" id="areas">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Service Areas</div>
                    <h2>Texas markets we dominate</h2>
                </div>
                <div class="card-grid card-grid-3">
                    {loc_cards}
                </div>
                <p class="text-center" style="margin-top:2rem"><a href="locations.html" class="btn btn-secondary">All Texas service areas</a></p>
            </div>
        </section>

        <section class="section section-alt" id="about">
            <div class="container two-col two-col-wide">
                <div class="prose-wide">
                    <div class="eyebrow">Company Overview</div>
                    <h2>The Stone Builders Rejected</h2>
                    <p>TSBR Enterprises is a Texas-authority digital marketing and local search agency headquartered in Arlington. We specialize in Google Business Profile optimization, AI Overview engineering, and B2B lead systems for commercial and industrial companies statewide.</p>
                    <p>The name comes from Psalm 118:22 &mdash; the stone the builders rejected became the cornerstone. That is our mission: turn overlooked businesses into the most visible, trusted, and cited company in their market.</p>
                    <p>Founded by {FOUNDER["short_name"]}, TSBR combines forensic SEO audits, strategic media placement, weekly GMB velocity, and entity authority building into one measurable operating system.</p>
                </div>
                <div class="card">
                    <h3>Trust signals</h3>
                    <ul class="feature-list">
                        <li><span class="check">&#10003;</span><span>Direct founder access on every engagement</span></li>
                        <li><span class="check">&#10003;</span><span>Map Pack &amp; AI citation reporting</span></li>
                        <li><span class="check">&#10003;</span><span>Qualified lead attribution, not vanity metrics</span></li>
                        <li><span class="check">&#10003;</span><span>Texas-only B2B specialization since 2012</span></li>
                    </ul>
                    <a href="about.html" class="btn btn-secondary" style="width:100%;margin-top:1rem">Full company story</a>
                </div>
            </div>
        </section>

        <section class="section section-alt" id="media">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Client work</div>
                    <h2>Results in motion</h2>
                </div>
                {video_showcase_html(limit=2)}
                {media_gallery_html(limit=6)}
            </div>
        </section>

        <section class="section" id="portfolio">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Recent Projects</div>
                    <h2>Portfolio &amp; case highlights</h2>
                    <p>Documented outcomes from Texas B2B engagements across industrial, contracting, and professional services.</p>
                </div>
                <div class="portfolio-grid">
                    {portfolio}
                </div>
                <p class="text-center" style="margin-top:2rem"><a href="case-studies.html" class="btn btn-secondary">Full case studies</a></p>
            </div>
        </section>

        <section class="section section-alt" id="process">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">Our Process</div>
                    <h2>From audit to market dominance</h2>
                </div>
                <div class="steps">
                    {process_html}
                </div>
            </div>
        </section>

        <section class="section" id="faq">
            <div class="container">
                <div class="section-header">
                    <div class="eyebrow">FAQ</div>
                    <h2>Questions from prospective clients</h2>
                </div>
                <div class="faq-list">
                    {faq_html(HOME_FAQ)}
                </div>
            </div>
        </section>

        <section class="section section-alt" id="estimate">
            <div class="container two-col two-col-wide">
                <div>
                    <div class="eyebrow">Free Estimation</div>
                    <h2>Request your custom visibility estimate</h2>
                    <p>Every estimate includes a GMB health scan, Map Pack snapshot, competitor review, and 90-day action outline.</p>
                    {audit_list_html()}
                </div>
                <div class="form-card form-card-premium">
                    <h3 style="margin-top:0">Estimation form</h3>
                    {estimation_form_html()}
                </div>
            </div>
        </section>

        <section class="section" id="contact-form">
            <div class="container two-col two-col-wide">
                <div class="form-card form-card-premium">
                    <h3 style="margin-top:0">Contact us</h3>
                    <p style="color:var(--text-muted);font-size:0.9375rem;margin-bottom:1.25rem">Prefer email? Reach out directly and we respond within 4 business hours.</p>
                    {contact_form_html()}
                </div>
                <div>
                    <div class="eyebrow">Get in Touch</div>
                    <h2>Arlington headquarters</h2>
                    <dl class="contact-info">
                        <dt>Phone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd>
                        <dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
                        <dt>Office</dt><dd>{ADDRESS}</dd>
                    </dl>
                    <p style="color:var(--text-muted);font-size:0.875rem">Serving DFW, Houston, Austin, San Antonio, and statewide multi-location B2B operations.</p>
                </div>
            </div>
        </section>

        <section class="cta-band cta-authority" id="cta">
            <div class="container">
                <div class="cta-emblem">TSBR</div>
                <h2>The Stone Builders Rejected</h2>
                <p>Become the cornerstone your market was overlooking. Partner with Texas&rsquo;s authority in GMB optimization, AI search visibility, and B2B lead generation.</p>
                <div class="hero-actions" style="justify-content:center;margin-top:1.5rem">
                    <a href="contact.html" class="btn btn-primary btn-crimson">Request Free Audit</a>
                    <a href="tel:{PHONE_TEL}" class="btn btn-secondary btn-gold-outline">Call {PHONE}</a>
                </div>
            </div>
        </section>"""

    content = (
        head(meta_title, meta_desc, canonical=reviews_url, extra=schema)
        + header(active="testimonials", body_class="testimonials-page")
        + f"""
    <main id="main">
        {breadcrumb_html([("Home", "index.html"), ("Reviews", None)])}
        <section class="page-hero testimonials-hero">
            <div class="container">
                <div class="eyebrow">Client Success &amp; Reviews</div>
                <h1>{h1}</h1>
                <p class="lead">Texas B2B leaders trust TSBR Enterprises for measurable Map Pack dominance, AI Overview citations, and qualified commercial lead growth.</p>
                {aeo_summary_html("TSBR client reviews document verified Texas B2B outcomes: Map Pack dominance in 74 days, 4.3x lead volume increases, AI Overview citations, and five-star Google reviews from industrial, contracting, and professional services firms across DFW, Houston, and Austin.")}
            </div>
        </section>
        {body}
        {silo_nav_html("Reviews silo — explore proof", [
            ("Case studies", "case-studies.html"),
            ("Services", "services.html"),
            ("GMB optimization", "gmb-optimization.html"),
            ("Request free audit", "contact.html"),
        ])}
    </main>
"""
        + footer()
    )
    write(ROOT / "testimonials.html", content)


def build_case_studies():
    studies = "".join(case_study_html(c, full=True) for c in CASE_STUDIES)
    body = f"""
        <section class="section section-alt">
            <div class="container prose-wide">
                <h2>Our measurement methodology</h2>
                <p>Every case study below tracks four dimensions: Map Pack position movement for agreed commercial keyword clusters, qualified lead volume (calls and forms attributed to Maps/organic/AI), review velocity, and AI Overview citation appearances. We do not report vanity traffic. B2B pipeline impact is the standard.</p>
                <p>Timelines reflect full GMB Velocity System implementation with client cooperation on review requests and photo deployment. Partial implementation produces slower results — we document both in audits.</p>
            </div>
        </section>
        <section class="section">
            <div class="container">
                <p style="max-width:42rem;margin:0 auto 2.5rem;text-align:center;color:var(--text-muted)">Actual outcomes from Texas B2B companies. Names anonymized where requested; metrics verified.</p>
                {studies}
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">Client testimonials</h2>
                <div class="card-grid card-grid-3">{testimonials_html(TESTIMONIALS[:3])}</div>
            </div>
        </section>
        <section class="section">
            <div class="container">
                <h2 class="text-center mb-lg">Typical 90-day engagement</h2>
                {engagement_timeline_html()}
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">TSBR vs. typical agencies</h2>
                {comparison_table_html()}
            </div>
        </section>
        <section class="cta-band">
            <div class="container">
                <h2>Ready for results like these?</h2>
                <p>Request a free audit and we will map your path to Map Pack dominance and AI visibility in your Texas markets.</p>
                <a href="contact.html" class="btn btn-primary">Get Your Free Audit</a>
            </div>
        </section>"""
    cases_url = page_url("case-studies.html")
    cases_schema = schema_extra(
        schema_organization(),
        schema_webpage(
            "Texas B2B Local SEO Case Studies",
            "Real Map Pack, AI Overview, and lead generation results for Texas B2B companies.",
            cases_url,
        ),
        schema_breadcrumb([("Home", "index.html"), ("Case Studies", None)]),
    )
    write(ROOT / "case-studies.html", page_template(
        "Case Studies | Texas B2B Local SEO Results",
        "Real results for Texas B2B companies. Map Pack dominance, AI Overview citations, and measurable lead growth across DFW, Houston, Austin, and San Antonio.",
        "Results", "Real Texas B2B outcomes",
        "Four detailed case studies with challenge, solution, metrics, and client quotes.",
        body, active="results", canonical=cases_url,
        breadcrumbs=[("Home", "index.html"), ("Case Studies", None)],
        aeo_summary="TSBR case studies document verified Texas B2B outcomes: Map Pack dominance in 74 days, 4.3x lead volume lifts, AI Overview citations, and measurable commercial pipeline growth across DFW, Houston, Austin, and San Antonio.",
        silo_nav={
            "heading": "See how we deliver these results",
            "links": [
                ("GMB optimization", "gmb-optimization.html"),
                ("AI search optimization", "ai-search-optimization.html"),
                ("Client reviews", "testimonials.html"),
                ("Request free audit", "contact.html"),
            ],
        },
        extra=cases_schema,
    ))


def build_locations():
    loc_links = "".join(
        f'<a href="{fn}" class="card card-link"><h3>{LOCATION_META[fn]["short"]}</h3>'
        f'<p>{join_text(LOCATION_RICH[fn]["local_intro"])[:160]}...</p><span class="link-arrow">View &rarr;</span></a>'
        for fn in LOCATION_RICH
    )
    body = f"""
        <section class="section">
            <div class="container">
                <div class="card-grid card-grid-2">
                    <div class="card">
                        <h3>Dallas&ndash;Fort Worth Metroplex</h3>
                        <span class="badge" style="margin-bottom:0.75rem;display:inline-block">Primary Market &middot; Arlington HQ</span>
                        <p>Arlington, Dallas, Fort Worth, Plano, Frisco, Irving, Carrollton, Richardson, Grapevine, Southlake, Grand Prairie, Mansfield, Euless, Bedford</p>
                    </div>
                    <div class="card">
                        <h3>Greater Houston</h3>
                        <p>Houston, The Woodlands, Katy, Sugar Land, Cypress, Pearland, League City, Pasadena, Conroe, Tomball, Spring</p>
                    </div>
                    <div class="card">
                        <h3>Austin Metro</h3>
                        <p>Austin, Round Rock, Cedar Park, Leander, Georgetown, Pflugerville, Buda, Kyle, Hutto</p>
                    </div>
                    <div class="card">
                        <h3>San Antonio &amp; Central/South Texas</h3>
                        <p>San Antonio, New Braunfels, Boerne, Schertz, Seguin, Universal City</p>
                    </div>
                </div>
                <div class="alert-box" style="margin-top:2rem">
                    <strong>Statewide capability:</strong> We also serve Corpus Christi, El Paso, Lubbock, Amarillo, Tyler, Longview, Waco, College Station, Beaumont, and smaller Texas markets. If you do business in Texas, we can help you own the local search landscape.
                </div>
                <div class="card-grid card-grid-3" style="margin-top:2.5rem">
                    {loc_links}
                </div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">Industries we serve statewide</h2>
                {industries_html()}
            </div>
        </section>
        <section class="section">
            <div class="container">
                <h2 class="text-center mb-lg">Buyer-intent keywords by metro</h2>
                <p class="text-center" style="max-width:42rem;margin:0 auto 2rem;color:var(--text-muted)">How Texas B2B buyers search in your market — and how we optimize for those terms.</p>
                {keyword_intents_html()}
            </div>
        </section>
        <section class="cta-band">
            <div class="container">
                <h2>Request a strategy for your specific Texas city</h2>
                <a href="contact.html" class="btn btn-primary">Get Free Audit</a>
            </div>
        </section>"""
    loc_hub_url = page_url("locations.html")
    loc_schema = schema_extra(
        schema_organization(),
        schema_webpage(
            "Texas Service Areas — TSBR Local SEO",
            "TSBR serves DFW, Houston, Austin, San Antonio, and statewide B2B local SEO markets.",
            loc_hub_url,
        ),
        schema_item_list("Texas Service Areas", [(LOCATION_META[f]["short"], f) for f in LOCATION_META]),
        schema_breadcrumb([("Home", "index.html"), ("Locations", None)]),
    )
    write(ROOT / "locations.html", page_template(
        "Texas Service Areas | Local SEO Agency",
        "TSBR serves DFW, Houston, Austin, San Antonio, and statewide. Google Business Profile and local SEO for Texas B2B.",
        "Locations", "Local SEO experts serving every major Texas market",
        "We live in Texas. We study Texas search behavior. We deliver results for B2B companies across the Lone Star State.",
        body, active="locations", canonical=loc_hub_url,
        breadcrumbs=[("Home", "index.html"), ("Locations", None)],
        aeo_summary="The Stone Builders Rejected serves every major Texas B2B market from Arlington HQ — DFW, Houston, Austin, San Antonio, and statewide multi-location accounts — with localized GMB, citation, and AI search silos per metro.",
        silo_nav={
            "heading": "Location silo — select your market",
            "links": [(LOCATION_META[f]["short"], f) for f in LOCATION_META],
        },
        extra=loc_schema,
    ))


def build_blog_index():
    cards = ""
    for a in BLOG_ARTICLES:
        cards += f"""
                    <a href="blog/{a['slug']}" class="card card-link blog-card">
                        <div class="tag">{a['tag']}</div>
                        <h3 style="margin-top:0.75rem">{a['title']}</h3>
                        <p>{a['desc']}</p>
                        <span style="font-size:0.8125rem;color:var(--text-muted)">{a['read_time']} read</span>
                        <span class="link-arrow">Read article &rarr;</span>
                    </a>"""
    body = f"""
        <section class="section">
            <div class="container">
                <div class="prose-wide" style="margin-bottom:2.5rem">
                    <p>In-depth articles on Google Business Profile optimization, AI Overviews, local SEO, citations, and B2B lead generation &mdash; written specifically for Texas commercial and industrial companies. Every article is authored by Mike Kaswatuka based on real client work across DFW, Houston, Austin, San Antonio, and statewide markets.</p>
                </div>
                <div class="card-grid card-grid-2">
                    {cards}
                </div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">Written by Texas local search authority</h2>
                {eeat_grid_html()}
            </div>
        </section>
        <section class="cta-band">
            <div class="container">
                <h2>Want a custom strategy for your business?</h2>
                <a href="contact.html" class="btn btn-primary">Request Free Audit</a>
            </div>
        </section>"""
    blog_url = page_url("blog.html")
    blog_schema = schema_extra(
        schema_organization(),
        schema_webpage(
            "TSBR Blog — Texas Local SEO & GMB Insights",
            "Expert insights on Texas B2B SEO, Google Business Profile optimization, and AI Overview strategies.",
            blog_url,
        ),
        schema_item_list("Blog Articles", [(a["title"], f"blog/{a['slug']}") for a in BLOG_ARTICLES]),
        schema_breadcrumb([("Home", "index.html"), ("Blog", None)]),
    )
    write(ROOT / "blog.html", page_template(
        "Blog | Texas Local SEO & GMB Insights",
        "Expert insights on Texas B2B SEO, Google Business Profile optimization, and AI Overview strategies.",
        "Blog", "Insights for Texas B2B growth",
        "Actionable strategies for dominating local search, Maps, and AI Overviews in Texas.",
        body, active="blog", canonical=blog_url,
        breadcrumbs=[("Home", "index.html"), ("Blog", None)],
        aeo_summary="The TSBR blog publishes Texas B2B local SEO playbooks on Google Business Profile optimization, citation building, AI Overview visibility, and search-driven lead generation — authored by Mike Kaswatuka from real client work.",
        silo_nav={
            "heading": "Blog content silo",
            "links": [(a["title"][:52], f"blog/{a['slug']}") for a in BLOG_ARTICLES] + [
                ("AI News", "ai-news.html"), ("Resources", "resources.html"),
            ],
        },
        extra=blog_schema,
    ))


def build_resources():
    cards = "".join(
        f'<a href="blog/{a["slug"]}" class="card card-link blog-card"><div class="tag">{a["tag"]}</div>'
        f'<h3 style="margin-top:0.75rem">{a["title"]}</h3><p>{a["desc"]}</p><span class="link-arrow">Read guide &rarr;</span></a>'
        for a in BLOG_ARTICLES
    )
    body = f"""
        <section class="section">
            <div class="container">
                <div class="prose-wide" style="margin-bottom:2rem">
                    <p>Our resource hub collects every in-depth guide, playbook, and framework we publish for Texas B2B companies. Use these alongside a <a href="contact.html">free audit</a> to understand exactly where your local search gaps are.</p>
                </div>
                <div class="card-grid card-grid-2">
                    {cards}
                </div>
                <div class="alert-box" style="margin-top:2.5rem">
                    <strong>Also explore:</strong> <a href="ai-news.html">AI News</a> for generative search updates &middot; <a href="services.html">Services overview</a> &middot; <a href="case-studies.html">Case studies</a> with real Texas B2B metrics
                </div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">90-day engagement roadmap</h2>
                {engagement_timeline_html()}
            </div>
        </section>"""
    res_url = page_url("resources.html")
    res_schema = schema_extra(
        schema_organization(),
        schema_webpage(
            "Texas Local SEO Resources",
            "In-depth guides for Texas B2B companies on GMB, AI Overviews, local SEO, and citations.",
            res_url,
        ),
        schema_item_list("Resource Guides", [(a["title"], f"blog/{a['slug']}") for a in BLOG_ARTICLES]),
        schema_breadcrumb([("Home", "index.html"), ("Resources", None)]),
    )
    write(ROOT / "resources.html", page_template(
        "Resources | Texas Local SEO Guides",
        "In-depth guides for Texas businesses on GMB optimization, AI Overviews, local SEO, citation building, and B2B lead generation.",
        "Resources", "Texas local SEO &amp; AI resources",
        "Actionable guides written specifically for B2B companies operating in the Lone Star State.",
        body, canonical=res_url,
        breadcrumbs=[("Home", "index.html"), ("Resources", None)],
        aeo_summary="TSBR resources collect every in-depth Texas B2B local SEO guide — GMB Velocity, citation building, AI-first content architecture, and generative search optimization — as a structured knowledge silo for commercial buyers.",
        silo_nav={
            "heading": "Resource silo navigation",
            "links": [(a["title"][:52], f"blog/{a['slug']}") for a in BLOG_ARTICLES] + [
                ("Blog hub", "blog.html"), ("AI News", "ai-news.html"), ("Services", "services.html"),
            ],
        },
        extra=res_schema,
    ))


def build_ai_news():
    articles = ""
    for a in AI_NEWS_ARTICLES:
        articles += f"""
                <article class="case-study">
                    <div class="tag">{a['date']}</div>
                    <h2>{a['title']}</h2>
                    <p style="color:var(--text-muted)">{a['summary']}</p>
                    <div class="prose-wide" style="margin-top:1rem">{a['body_html']}</div>
                </article>"""
    body = f"""
        <section class="section">
            <div class="container">
                <div class="prose-wide" style="margin-bottom:2.5rem">
                    <p>AI News from The Stone Builders Rejected tracks how generative search, Google AI Overviews, and entity-based ranking are changing local visibility for Texas B2B companies. Updated analysis from Mike Kaswatuka based on live client data and search behavior across Arlington, DFW, Houston, Austin, and statewide markets.</p>
                </div>
                {articles}
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">AI search FAQ</h2>
                <div class="faq-list">{faq_html([item for item in EXTRA_FAQ if "AI" in item[0]])}</div>
            </div>
        </section>
        <section class="cta-band">
            <div class="container">
                <h2>Want AI visibility for your Texas business?</h2>
                <a href="ai-search-optimization.html" class="btn btn-primary">AI Search Optimization</a>
                <a href="contact.html" class="btn btn-secondary" style="margin-left:0.5rem">Free Audit</a>
            </div>
        </section>"""
    ain_url = page_url("ai-news.html")
    ain_schema = schema_extra(
        schema_organization(),
        schema_webpage(
            "AI News — Generative Search for Texas B2B",
            "Latest AI search news and generative engine optimization analysis for Texas B2B companies.",
            ain_url,
        ),
        schema_breadcrumb([("Home", "index.html"), ("AI News", None)]),
    )
    write(ROOT / "ai-news.html", page_template(
        "AI News | Generative Search & AI Overviews for Texas B2B",
        "Latest AI search news and analysis for Texas B2B companies. Google AI Overviews, generative engine optimization, and local entity strategy.",
        "AI News", "Generative search intelligence for Texas B2B",
        "How AI Overviews and generative search are reshaping local visibility for Texas commercial businesses.",
        body, active="ainews", canonical=ain_url,
        breadcrumbs=[("Home", "index.html"), ("AI News", None)],
        aeo_summary="TSBR AI News tracks how Google AI Overviews and generative search change local B2B visibility in Texas — with actionable GEO and AEO guidance on entity signals, FAQ schema, GMB alignment, and citation consistency.",
        silo_nav={
            "heading": "AI & GEO silo",
            "links": [
                ("AI search optimization service", "ai-search-optimization.html"),
                ("AI-first content guide", "blog/ai-first-content-architecture-texas.html"),
                ("AI Overviews guide", "blog/optimizing-for-ai-overviews-texas-businesses.html"),
                ("Blog hub", "blog.html"), ("Free audit", "contact.html"),
            ],
        },
        extra=ain_schema,
    ))


def build_blog_posts():
    blog_dir = ROOT / "blog"
    blog_dir.mkdir(exist_ok=True)
    for a in BLOG_ARTICLES:
        toc = "".join(
            f'<li><a href="#{tid}">{label}</a></li>'
            for tid, label in a["toc"]
        )
        related = "".join(
            f'<a href="{o["slug"]}">{o["title"][:48]}</a>'
            for o in [x for x in BLOG_ARTICLES if x["slug"] != a["slug"]][:5]
        )
        body = f"""
        <section class="section">
            <div class="container prose-wide">
                <div class="blog-meta">
                    <span class="badge">{a['tag']}</span>
                    <span>By Mike Kaswatuka</span>
                    <span>The Stone Builders Rejected</span>
                    <span>Arlington, TX</span>
                    <span>{a['read_time']} read</span>
                </div>
                <div class="toc">
                    <h4>In this article</h4>
                    <ol>{toc}</ol>
                </div>
                {a['body_html']}
                <div class="highlight-box">
                    <strong>Ready to implement this for your Texas business?</strong>
                    <p style="margin:0.5rem 0 0"><a href="../contact.html">Request a free GMB and local visibility audit &rarr;</a></p>
                </div>
                <div class="related-links">
                    <span style="font-weight:600;color:var(--cyan);margin-right:0.5rem">Related:</span>
                    {related}
                </div>
            </div>
        </section>"""
        post_path = f"blog/{a['slug']}"
        post_url = page_url(post_path)
        pub_date = a.get("published", "2026-01-15")
        post_schema = schema_extra(
            schema_organization(),
            schema_article(a["title"], a["desc"], post_url, pub_date, a["tag"]),
            schema_webpage(a["title"], a["desc"], post_url),
            schema_breadcrumb([("Home", "../index.html"), ("Blog", "../blog.html"), (a["title"], None)]),
        )
        write(blog_dir / a["slug"], page_template(
            f"{a['title']} | TSBR",
            a["desc"],
            "Blog", a["title"], a["desc"], body, active="blog", depth=1,
            canonical=post_url, og_type="article",
            breadcrumbs=[("Home", "../index.html"), ("Blog", "../blog.html"), (a["title"], None)],
            aeo_summary=a["desc"],
            silo_nav=blog_silo(a),
            extra=post_schema,
        ))


def build_service_pages():
    for filename, svc in SERVICE_RICH.items():
        meta = SERVICE_META[filename]
        intro = join_text(svc["intro"])
        deliverables = "".join(f'<div class="deliverable-item"><span class="icon">&#10003;</span><span>{d}</span></div>' for d in svc["deliverables"])
        faqs = faq_html(svc["faqs"][:4])
        body = f"""
        <section class="section">
            <div class="container two-col two-col-wide">
                <div class="prose-wide">
                    <p>{intro}</p>
                    <h2>What you get</h2>
                    <div class="deliverables-grid">{deliverables}</div>
                    <div class="alert-box" style="margin-top:1.5rem"><strong>Timeline:</strong> {svc["timeline"]}</div>
                    <p style="margin-top:1rem"><em>{svc["note"]}</em></p>
                </div>
                <div class="card">
                    <h3>Why this wins in Texas</h3>
                    <p>Most commercial buyers in Texas still start with a Google search. The businesses that own the Map Pack, organic local results, and AI Overviews capture the vast majority of high-intent B2B leads.</p>
                    <p>We control every signal &mdash; photos, posts, reviews, citations, content, and entity data &mdash; for our clients.</p>
                    <a href="contact.html" class="btn btn-primary" style="margin-top:1rem;width:100%">Request Free Audit</a>
                    <a href="case-studies.html" class="btn btn-secondary" style="margin-top:0.75rem;width:100%">See case studies</a>
                </div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">Related case study</h2>
                {case_study_html(CASE_STUDIES[0], full=False)}
            </div>
        </section>
        {service_extra_sections(filename)}
        <section class="section">
            <div class="container">
                <h2 class="text-center mb-lg">Frequently asked questions</h2>
                <div class="faq-list">{faqs}</div>
            </div>
        </section>
        <section class="cta-band">
            <div class="container">
                <h2>Let&rsquo;s build your local search dominance</h2>
                <a href="contact.html" class="btn btn-primary">Get Started</a>
            </div>
        </section>"""
        svc_url = page_url(filename)
        svc_schema = schema_extra(
            schema_organization(),
            schema_service(meta["h1"], meta["meta_desc"], svc_url),
            schema_webpage(meta["title"], meta["meta_desc"], svc_url),
            schema_faq(svc["faqs"][:4]),
            schema_breadcrumb([("Home", "index.html"), ("Services", "services.html"), (meta["h1"], None)]),
        )
        write(ROOT / filename, page_template(
            f"{meta['title']} | TSBR",
            meta["meta_desc"],
            meta["eyebrow"], meta["h1"], meta["lead"], body,
            canonical=svc_url,
            breadcrumbs=[("Home", "index.html"), ("Services", "services.html"), (meta["h1"], None)],
            aeo_summary=intro[:280] + ("..." if len(intro) > 280 else ""),
            silo_nav=service_silo(filename),
            extra=svc_schema,
        ))


def build_location_pages():
    for filename, loc in LOCATION_RICH.items():
        meta = LOCATION_META[filename]
        industries = '<div class="industry-grid">' + "".join(f'<span class="industry-pill">{i}</span>' for i in loc["industries"]) + "</div>"
        local_faq = faq_html(loc["local_faq"][:4])
        kw_market = LOCATION_KEYWORD_MARKET.get(filename)
        if kw_market:
            keyword_section = f"""
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">High-intent keywords in {meta["short"]}</h2>
                {keyword_intents_html(kw_market)}
            </div>
        </section>"""
        else:
            keyword_section = f"""
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">Buyer-intent keywords across Texas</h2>
                {keyword_intents_html()}
            </div>
        </section>"""
        arlington_extra = ""
        if filename == "arlington-tx-seo-marketing-consultant.html":
            arlington_extra = f"""
        <section class="section section-alt">
            <div class="container two-col two-col-wide">
                <div class="prose-wide">
                    <h2>Arlington Pathway</h2>
                    {ARLINGTON_PATHWAY["intro"]}
                    <p><strong>{ARLINGTON_PATHWAY["proof"]}</strong></p>
                </div>
                <div class="card">
                    <h3>Pathway steps</h3>
                    <ol>
                        {"".join(f"<li><strong>{t}</strong> — {d}</li>" for t, d in ARLINGTON_PATHWAY["steps"])}
                    </ol>
                </div>
            </div>
        </section>"""
        body = f"""
        <section class="section">
            <div class="container two-col two-col-wide">
                <div class="prose-wide">
                    <p>{join_text(loc["local_intro"])}</p>
                    <p>{loc["search_behavior"]}</p>
                    <h2>Industries we dominate in {meta["short"]}</h2>
                    {industries}
                    <h2>Areas we serve</h2>
                    <p>{", ".join(meta["areas"])}</p>
                </div>
                <div class="card">
                    <h3>What you get</h3>
                    <ul class="feature-list">
                        <li><span class="check">&#10003;</span><span>Complete GMB audit and optimization</span></li>
                        <li><span class="check">&#10003;</span><span>Competitor mapping in your market</span></li>
                        <li><span class="check">&#10003;</span><span>Citation and NAP consistency fixes</span></li>
                        <li><span class="check">&#10003;</span><span>AI Overview visibility strategy</span></li>
                        <li><span class="check">&#10003;</span><span>Location-specific content silos</span></li>
                        <li><span class="check">&#10003;</span><span>Monthly reporting and optimization</span></li>
                        <li><span class="check">&#10003;</span><span>Direct access to Mike Kaswatuka</span></li>
                    </ul>
                    <a href="contact.html" class="btn btn-primary" style="margin-top:1rem;width:100%">Free {meta["short"]} Audit</a>
                </div>
            </div>
        </section>
        <section class="section section-alt">
            <div class="container">
                <h2 class="text-center mb-lg">{meta["short"]} local SEO FAQ</h2>
                <div class="faq-list">{local_faq}</div>
            </div>
        </section>
        <section class="section">
            <div class="container">
                <h2 class="text-center mb-lg">Results in {meta["short"]}</h2>
                {testimonials_html([t for t in TESTIMONIALS if meta["short"].split("/")[0].strip() in t["city"] or meta["short"] in t["city"]][:2] or TESTIMONIALS[:2])}
            </div>
        </section>
        {keyword_section}
        {arlington_extra}
        <section class="cta-band">
            <div class="container">
                <h2>Own {meta["short"]} local search</h2>
                <p>Request a free audit tailored to your market.</p>
                <a href="contact.html" class="btn btn-primary">Request Free Audit</a>
            </div>
        </section>"""
        loc_url = page_url(filename)
        loc_intro = join_text(loc["local_intro"])
        loc_schema = schema_extra(
            schema_organization(),
            schema_webpage(f"{meta['short']} SEO & GMB", meta["meta_desc"], loc_url),
            schema_faq(loc["local_faq"][:4]),
            schema_breadcrumb([
                ("Home", "index.html"), ("Locations", "locations.html"), (meta["short"], None),
            ]),
        )
        write(ROOT / filename, page_template(
            f"{meta['title']} | GMB & Local SEO",
            meta["meta_desc"],
            meta["city"], f"{meta['short']} SEO &amp; GMB experts",
            meta["lead"], body, hero_class="location-hero",
            canonical=loc_url,
            breadcrumbs=[("Home", "index.html"), ("Locations", "locations.html"), (meta["short"], None)],
            aeo_summary=loc_intro[:300] + ("..." if len(loc_intro) > 300 else ""),
            silo_nav=location_silo(filename),
            extra=loc_schema,
        ))


def build_privacy():
    body = f"""
        <section class="section">
            <div class="container prose-wide">
                <p><strong>Effective date:</strong> June 19, 2026</p>
                <p>The Stone Builders Rejected (TSBR Enterprises) respects your privacy. This policy explains how we collect, use, and protect information submitted through our website at {DOMAIN}.</p>
                <h2>Information we collect</h2>
                <p>When you submit a contact form, estimation request, or audit request, we collect the information you provide: name, business name, phone, email, website, city or metro, industry, service interests, and message content.</p>
                <h2>How we use your information</h2>
                <ul>
                    <li>Respond to your inquiry and deliver your free audit or estimate</li>
                    <li>Schedule strategy calls with Mike Kaswatuka or our team</li>
                    <li>Improve our services and website experience</li>
                </ul>
                <p>We do not sell, rent, or trade your personal information to third parties.</p>
                <h2>Form processing</h2>
                <p>Form submissions may be processed through Formspree or a comparable secure form service when configured. If no form backend is configured, submissions open your email client with a pre-filled message to {EMAIL}.</p>
                <h2>Analytics</h2>
                <p>We may use Google Analytics or similar tools to understand aggregate website traffic. You can opt out via browser extensions or Google's opt-out tools.</p>
                <h2>Cookies</h2>
                <p>Our site uses minimal cookies primarily from analytics providers when enabled. The site functions without accepting cookies.</p>
                <h2>Data retention</h2>
                <p>We retain inquiry data as long as needed to serve your request and maintain business records, typically up to three years unless you request deletion sooner.</p>
                <h2>Your rights</h2>
                <p>You may request access, correction, or deletion of your data by emailing <a href="mailto:{EMAIL}">{EMAIL}</a> or calling <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>
                <h2>Contact</h2>
                <p>The Stone Builders Rejected<br>{ADDRESS}<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
            </div>
        </section>"""
    privacy_url = page_url("privacy.html")
    privacy_schema = schema_extra(
        schema_organization(),
        schema_webpage("Privacy Policy", "TSBR Enterprises privacy policy for website visitors and form submissions.", privacy_url),
        schema_breadcrumb([("Home", "index.html"), ("Privacy Policy", None)]),
    )
    write(ROOT / "privacy.html", page_template(
        "Privacy Policy | TSBR Enterprises",
        "Privacy policy for The Stone Builders Rejected website. How we handle contact form data and analytics.",
        "Legal", "Privacy policy",
        "How TSBR collects, uses, and protects information you submit through our website.",
        body, canonical=privacy_url,
        breadcrumbs=[("Home", "index.html"), ("Privacy Policy", None)],
        extra=privacy_schema,
    ))


def build_404():
    body = """
        <section class="section">
            <div class="container text-center">
                <div class="eyebrow">404</div>
                <h2 style="font-size:2.5rem;margin:1rem 0">Page not found</h2>
                <p style="max-width:32rem;margin:0 auto 2rem;color:var(--text-muted)">This page may have moved or no longer exists. Explore our services, Texas locations, or request a free local SEO audit.</p>
                <div class="hero-actions" style="justify-content:center">
                    <a href="index.html" class="btn btn-primary">Home</a>
                    <a href="services.html" class="btn btn-secondary">Services</a>
                    <a href="contact.html" class="btn btn-secondary">Free Audit</a>
                </div>
            </div>
        </section>"""
    write(ROOT / "404.html", page_template(
        "Page Not Found | TSBR",
        "The page you requested was not found. Return to The Stone Builders Rejected Texas local SEO website.",
        "404", "Page not found",
        "We could not find the page you were looking for.",
        body, canonical=page_url("404.html"),
        breadcrumbs=[("Home", "index.html"), ("404", None)],
    ))


def build_sitemap():
    pages = [
        ("index.html", "daily", "1.0"),
        ("about.html", "monthly", "0.8"),
        ("services.html", "weekly", "0.9"),
        ("contact.html", "monthly", "0.9"),
        ("privacy.html", "yearly", "0.3"),
        ("testimonials.html", "weekly", "0.85"),
        ("case-studies.html", "weekly", "0.85"),
        ("locations.html", "weekly", "0.9"),
        ("blog.html", "weekly", "0.85"),
        ("resources.html", "weekly", "0.8"),
        ("ai-news.html", "weekly", "0.8"),
    ]
    pages += [(f, "weekly", "0.88") for f in SERVICE_META]
    pages += [(f, "weekly", "0.88") for f in LOCATION_META]
    pages += [(f"blog/{a['slug']}", "monthly", "0.8") for a in BLOG_ARTICLES]

    entries = []
    for path, freq, priority in pages:
        loc = page_url(path)
        entries.append(
            f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{SITEMAP_LASTMOD}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries)
        + "\n</urlset>\n"
    )
    write(ROOT / "sitemap.xml", xml)


def build_robots():
    robots = f"""User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

Sitemap: {page_url("sitemap.xml")}
"""
    write(ROOT / "robots.txt", robots)


def update_readme():
    readme = f"""# The Stone Builders Rejected (TSBR Enterprises)

Texas B2B local SEO & Google Business Profile agency website.

### Build
```bash
python _build.py
```
Regenerates all HTML from `_content.py` (rich content), `_content_extra.py` (supplementary blocks), and `_build.py` (templates).

### Preview
```bash
python -m http.server 8080
```
Open http://localhost:8080

### Configuration
Copy `.env.example` to `.env` and fill in values. `_config.py` loads `.env` automatically.

| Variable | Purpose |
|----------|---------|
| `TSBR_FORMSPREE_ENDPOINT` | Formspree form URL (e.g. `https://formspree.io/f/xxxxx`) |
| `FORMSPREE_DEPLOY_KEY` | Formspree CLI deploy key (alternative to pasting endpoint) |
| `TSBR_GA_MEASUREMENT_ID` | Google Analytics 4 ID (e.g. `G-XXXXXXXXXX`) |

### Formspree setup
```powershell
.\scripts\setup-formspree.ps1 -Endpoint "https://formspree.io/f/YOUR_ID"
# OR with CLI deploy key in .env:
.\scripts\setup-formspree.ps1 -Deploy
```

### Deploy
```powershell
.\scripts\deploy.ps1 -Method preview   # local preview
.\scripts\deploy.ps1 -Method copy       # copy to deploy.config.json path
.\scripts\deploy.ps1 -Method ftp        # FTP upload
```

### Visual audit
```powershell
.\scripts\deploy.ps1 -Method preview    # in one terminal
cd scripts && npm install && npm run visual-audit
```

### Business Info
- **Founder:** Mike Kaswatuka
- **Address:** {ADDRESS}
- **Phone:** {PHONE}
- **Email:** {EMAIL}

Rebuilt {YEAR} — galactic theme, full Texas B2B content silo.
"""
    write(ROOT / "README.md", readme)


def main():
    print("Building TSBR website (galactic theme)...")
    build_index()
    build_about()
    build_services()
    build_contact()
    build_testimonials()
    build_case_studies()
    build_locations()
    build_blog_index()
    build_resources()
    build_ai_news()
    build_blog_posts()
    build_service_pages()
    build_location_pages()
    build_privacy()
    build_404()
    build_sitemap()
    build_robots()
    update_readme()
    print("Done.")


if __name__ == "__main__":
    main()