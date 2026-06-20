"""Rich website content for The Stone Builders Rejected (TSBR).

Texas B2B local SEO agency founded by Mike Kaswatuka in Arlington, TX.
Imported by _build.py to generate unified site pages.
"""

from html import escape


# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

def faq_html(items):
    """Return HTML string of details.faq-item elements."""
    parts = []
    for question, answer in items:
        q = escape(question)
        a = escape(answer)
        parts.append(
            f'<details class="faq-item"><summary>{q}</summary>'
            f'<div class="faq-body">{a}</div></details>'
        )
    return "\n".join(parts)


def testimonials_html(items, limit=None):
    """Return HTML for testimonial blocks."""
    subset = items[:limit] if limit else items
    parts = []
    for t in subset:
        quote = escape(t["quote"])
        author = escape(t["author"])
        company = escape(t["company"])
        city = escape(t["city"])
        parts.append(
            f'<div class="testimonial">'
            f'<blockquote>"{quote}"</blockquote>'
            f'<cite>&mdash; {author}, {company}, {city}</cite>'
            f'</div>'
        )
    return "\n".join(parts)


def quote_cards_html(items, limit=None):
    """Large-format premium quote cards for testimonials page."""
    subset = items[:limit] if limit else items
    parts = []
    for t in subset:
        quote = escape(t["quote"])
        author = escape(t["author"])
        company = escape(t["company"])
        city = escape(t["city"])
        stars = t.get("stars", 5)
        star_str = "★" * stars + "☆" * (5 - stars)
        parts.append(
            f'<article class="quote-card">'
            f'<div class="quote-mark" aria-hidden="true">&ldquo;</div>'
            f'<div class="quote-stars" aria-label="{stars} out of 5 stars">{star_str}</div>'
            f'<blockquote>{quote}</blockquote>'
            f'<footer class="quote-footer">'
            f'<strong>{author}</strong>'
            f'<span>{company} &middot; {city}</span>'
            f'</footer></article>'
        )
    return "\n".join(parts)


def gmb_reviews_html(items, limit=6):
    """Google-style review cards for GMB widget area."""
    subset = items[:limit]
    parts = []
    for t in subset:
        quote = escape(t["quote"][:180] + ("…" if len(t["quote"]) > 180 else ""))
        author = escape(t["author"])
        company = escape(t["company"])
        parts.append(
            f'<div class="gmb-review">'
            f'<div class="gmb-review-head">'
            f'<span class="gmb-avatar" aria-hidden="true">{author[0]}</span>'
            f'<div><strong>{author}</strong><span class="gmb-meta">Google Review &middot; {company}</span></div>'
            f'<span class="gmb-stars" aria-label="5 stars">★★★★★</span>'
            f'</div>'
            f'<p>{quote}</p></div>'
        )
    return "\n".join(parts)


FOUNDER = {
    "name": "Michael K. Kaswatuka",
    "short_name": "Mike Kaswatuka",
    "title": "Founder & Principal Strategist",
    "company": "The Stone Builders Rejected (TSBR Enterprises)",
    "location": "Arlington, Texas",
    "image": "assets/images/michael-kaswatuka-founder.png",
    "image_alt": "Michael K. Kaswatuka, Founder of TSBR Enterprises and The Stone Builders Rejected",
    "bio": [
        (
            "Michael K. Kaswatuka founded The Stone Builders Rejected in Arlington, Texas with a "
            "single conviction: the best B2B companies are often the most overlooked online. For "
            "more than a decade he has engineered local search dominance for Texas commercial "
            "and industrial businesses — turning invisible profiles into cornerstone Map Pack "
            "positions, AI Overview citations, and measurable lead pipelines."
        ),
        (
            "Mike works directly with every client. No handoffs to junior account managers. He "
            "personally audits Google Business Profiles, maps competitor landscapes, and designs "
            "the GMB Velocity System that has moved hundreds of Texas companies from page nine "
            "to top-three local rankings across DFW, Houston, Austin, San Antonio, and statewide "
            "multi-location operations."
        ),
        (
            "His approach blends forensic SEO, strategic media placement, entity authority "
            "engineering, and conversion-focused profile optimization. Clients trust Mike because "
            "he reports on qualified commercial leads and pipeline impact — not vanity traffic — "
            "and because he treats every engagement as building a cornerstone, not checking boxes."
        ),
    ],
    "credentials": [
        "Google Business Profile Strategy",
        "AI Overview & Generative Search",
        "Texas Multi-Market Local SEO",
        "B2B Lead Attribution Systems",
        "Entity & Citation Engineering",
    ],
}


def founder_bio_html(image_prefix=""):
    """Founder author bio block with photo."""
    img = f'{image_prefix}{FOUNDER["image"]}'
    creds = "".join(f'<span class="badge badge-gold">{escape(c)}</span>' for c in FOUNDER["credentials"])
    paras = "".join(f"<p>{escape(p)}</p>" for p in FOUNDER["bio"])
    return (
        f'<div class="founder-bio">'
        f'<div class="founder-photo">'
        f'<img src="{img}" alt="{escape(FOUNDER["image_alt"])}" loading="lazy" width="400" height="520">'
        f'</div>'
        f'<div class="founder-copy">'
        f'<div class="eyebrow">Founder &amp; Author</div>'
        f'<h2>{escape(FOUNDER["name"])}</h2>'
        f'<p class="founder-title">{escape(FOUNDER["title"])} &middot; {escape(FOUNDER["location"])}</p>'
        f'{paras}'
        f'<div class="founder-creds">{creds}</div>'
        f'</div></div>'
    )


def case_study_html(study, full=True):
    """Render a case study in full or preview mode."""
    metrics_html = "".join(
        f'<div><strong>{escape(m["value"])}</strong>'
        f'<span>{escape(m["label"])}</span></div>'
        for m in study["metrics"]
    )
    tag = escape(study["tag"])
    title = escape(study["title"])
    quote = escape(study["quote"])
    cite = escape(study["cite"])

    body = (
        f'<div class="case-study">'
        f'<div class="tag">{tag}</div>'
        f'<h2>{title}</h2>'
        f'<div class="case-metrics">{metrics_html}</div>'
    )

    if full:
        challenge = escape(study["challenge"])
        solution = escape(study["solution"])
        results = study["results"]
        if isinstance(results, list):
            results_html = "".join(f"<p>{escape(p)}</p>" for p in results)
        else:
            results_html = f"<p>{escape(results)}</p>"
        body += (
            f'<h3>The challenge</h3><p>{challenge}</p>'
            f'<h3>Our solution</h3><p>{solution}</p>'
            f'<h3>Results</h3>{results_html}'
        )

    body += (
        f'<p>"{quote}"</p>'
        f'<cite style="font-size:0.875rem;color:var(--muted)">&mdash; {cite}</cite>'
        f'</div>'
    )
    return body


# ---------------------------------------------------------------------------
# FAQ
# ---------------------------------------------------------------------------

FAQ_ITEMS = [
    (
        "How long until we see Google Map Pack movement?",
        "Most Texas B2B clients see meaningful Map Pack movement within 30 to 60 days when they "
        "implement our full GMB Velocity System. Dominant top-3 positions across primary service "
        "areas typically arrive within 74 to 90 days. Timeline depends on your starting profile "
        "health, review velocity, citation consistency, and competitive density in your metro."
    ),
    (
        "Do you optimize for Google AI Overviews and generative search?",
        "Yes. AI Overview optimization is a core service, not an add-on. We build entity authority, "
        "structured FAQ content, schema markup, and corroborating citations so generative search "
        "models cite your business when Texas buyers ask for local recommendations. Clients in "
        "Houston and Austin have reached top-3 AI citation positions within 75 days."
    ),
    (
        "What industries do you specialize in for Texas B2B?",
        "We focus on high-value B2B verticals: industrial equipment, commercial contracting, "
        "manufacturing, civil engineering, HVAC and mechanical contractors, logistics, professional "
        "services, healthcare B2B, wholesale distribution, and multi-location service firms. If your "
        "average deal size justifies serious local search investment, we are a fit."
    ),
    (
        "Do you work outside Arlington and DFW?",
        "Absolutely. While our headquarters is in Arlington, we serve every major Texas metro "
        "including Dallas, Fort Worth, Houston, Austin, San Antonio, and statewide multi-location "
        "accounts. We study search behavior market by market because DFW buyers search differently "
        "than Houston energy corridor buyers or Austin tech procurement teams."
    ),
    (
        "How do you price local SEO and GMB services?",
        "We do not publish one-size-fits-all packages. After your free audit, Mike Kaswatuka "
        "recommends a scope based on your markets, competitive landscape, and revenue goals. "
        "Engagements are structured around measurable outcomes: Map Pack positions, qualified lead "
        "volume, review velocity, and AI citation growth. You always know what you are paying for "
        "and what success looks like before you commit."
    ),
    (
        "Can you manage multiple Google Business Profile locations?",
        "Yes. Multi-location GMB management is one of our strengths. We standardize NAP data, "
        "deploy location-specific content calendars, build review systems per branch, and prevent "
        "listing duplication or suppression. Texas companies with 3 to 50 locations use our "
        "framework to rank each service area without cannibalizing the others."
    ),
    (
        "What is included in the free audit?",
        "Your audit covers Google Business Profile completeness and suppression risks, Map Pack "
        "and organic ranking snapshot, top competitor analysis, citation and NAP consistency scan, "
        "review profile assessment, AI Overview visibility check, and a prioritized 90-day action "
        "plan. You receive a written report even if you do not hire us."
    ),
    (
        "How is TSBR different from a typical SEO agency?",
        "Three differences: we work exclusively with Texas B2B companies, we combine traditional "
        "local SEO with AI Overview engineering, and you work directly with founder Mike Kaswatuka "
        "instead of a rotating junior account manager. We measure success in qualified commercial "
        "leads and pipeline, not vanity traffic metrics."
    ),
    (
        "Do you require long-term contracts?",
        "We recommend a minimum 6-month engagement because local search compounding takes time, "
        "especially in competitive DFW and Houston markets. Month-to-month options exist after "
        "the initial term for clients who want ongoing Map Pack defense and AI visibility "
        "monitoring. We earn renewals with results, not lock-in clauses."
    ),
    (
        "How do you track leads from Google Maps and local search?",
        "We implement call tracking, UTM-tagged URLs, GMB insights analysis, and CRM-aligned "
        "lead source fields so your sales team can attribute every inquiry to Maps, organic, or "
        "AI Overview touchpoints. B2B lead quality matters more than volume, so we optimize for "
        "keywords and profile signals that attract buyers ready to request quotes."
    ),
    (
        "Will you write content and manage Google Posts for us?",
        "Yes. Content is part of the system, not optional. We produce keyword-aligned Google "
        "Posts, Q&A seeding, service descriptions, and website location pages that reinforce "
        "your entity signals. Texas commercial buyers respond to proof: project photos, "
        "certifications, fleet shots, and facility tours published consistently."
    ),
    (
        "What if our Google Business Profile was suspended or has duplicates?",
        "Profile recovery and deduplication are included in our audit phase. We identify the "
        "authoritative listing, merge or remove duplicates, resolve policy flags, and rebuild "
        "trust signals safely. Rushing reinstatement without fixing root NAP or category issues "
        "causes repeat suspensions. We fix the foundation first."
    ),
]


# ---------------------------------------------------------------------------
# Testimonials
# ---------------------------------------------------------------------------

TESTIMONIALS = [
    {
        "quote": "We went from page 9 to owning 17 Map Pack positions in 74 days. Our sales team is now overwhelmed with high-quality commercial leads.",
        "author": "Director of Operations",
        "company": "Precision Machine Works",
        "city": "Irving, TX",
    },
    {
        "quote": "The GMB work plus AI optimization put us in conversations we were never part of before. We are now the default recommendation in greater Houston.",
        "author": "Owner",
        "company": "Gulf Coast Commercial Construction",
        "city": "Houston, TX",
    },
    {
        "quote": "TSBR understood our civil engineering practice better than any agency we interviewed. Austin metro visibility changed our bid pipeline within one quarter.",
        "author": "James K., Managing Partner",
        "company": "Lone Star Civil Engineering",
        "city": "Austin, TX",
    },
    {
        "quote": "Map pack dominance in San Antonio translated directly into quote requests. We saw 3.2x more RFQs from manufacturers who found us on Google first.",
        "author": "VP of Sales",
        "company": "Alamo Industrial Supply",
        "city": "San Antonio, TX",
    },
    {
        "quote": "Mike personally audited our five DFW locations and found suppression issues our last agency missed for two years. Within 60 days every branch hit the top 3.",
        "author": "Regional Manager",
        "company": "TexPro Mechanical Services",
        "city": "Arlington, TX",
    },
    {
        "quote": "We are a B2B logistics firm, not a consumer brand. TSBR optimized for the searches freight managers actually use. Qualified inbound calls doubled.",
        "author": "Director of Business Development",
        "company": "Lone Star Freight Solutions",
        "city": "Dallas, TX",
    },
    {
        "quote": "The free audit alone was more actionable than a paid strategy we bought elsewhere. We signed on immediately and have not looked back.",
        "author": "President",
        "company": "Fort Worth Fabrication Group",
        "city": "Fort Worth, TX",
    },
    {
        "quote": "AI Overview citations were a black box until TSBR mapped our entity gaps. Now we appear when procurement teams ask ChatGPT and Google for Texas vendors.",
        "author": "Marketing Director",
        "company": "Hill Country Commercial HVAC",
        "city": "Round Rock, TX",
    },
    {
        "quote": "North DFW is brutally competitive for commercial contractors. TSBR got us into the Map Pack in Plano and Frisco while our website organic rankings climbed in parallel.",
        "author": "Estimator",
        "company": "Northline Build Partners",
        "city": "Plano, TX",
    },
]


# ---------------------------------------------------------------------------
# Case studies
# ---------------------------------------------------------------------------

CASE_STUDIES = [
    {
        "tag": "DFW - Industrial Equipment",
        "title": "From page 9 to 17 Map Pack positions in 74 days",
        "metrics": [
            {"value": "+620%", "label": "Commercial quote requests"},
            {"value": "41", "label": "New B2B accounts in 5 months"},
            {"value": "17", "label": "#1 local rankings"},
            {"value": "91", "label": "Reviews generated"},
        ],
        "challenge": (
            "Precision Machine Works in Irving had best-in-class CNC capabilities and a loyal "
            "referral base, but was invisible on Google. Their Google Business Profile was "
            "incomplete, photos were outdated, and competitors with weaker facilities dominated "
            "the Map Pack across DFW industrial corridors. Organic rankings sat on page 9 for "
            "high-intent terms like commercial machine shop Irving and industrial CNC DFW."
        ),
        "solution": (
            "TSBR deployed the GMB Velocity System: full profile reconstruction, 78 geo-tagged "
            "facility and equipment photos, weekly Google Posts aligned to manufacturing buyer "
            "intent, systematic review requests after project delivery, and citation cleanup "
            "across 80+ directories. We built supporting service-area pages and FAQ schema on "
            "their site to reinforce entity signals for AI Overviews."
        ),
        "results": [
            "Within 74 days Precision Machine Works held 17 #1 Map Pack positions across Irving, "
            "Grand Prairie, Arlington, and Dallas industrial zones.",
            "Commercial quote requests increased 620% compared to the prior six-month baseline.",
            "The sales team closed 41 new B2B accounts in five months, with the majority "
            "self-reporting Google as the first touchpoint.",
            "Review velocity reached 91 authentic five-star reviews with keyword-rich project "
            "descriptions that strengthened both Maps and AI citation trust.",
        ],
        "quote": "We had been invisible despite having the best equipment and service in North Texas. TSBR completely transformed our visibility.",
        "cite": "Director of Operations, Precision Machine Works, Irving",
    },
    {
        "tag": "Houston - Commercial Contracting",
        "title": "4.3x lead volume after dominating Maps and AI Overviews",
        "metrics": [
            {"value": "4.3x", "label": "Qualified project leads"},
            {"value": "Top 3", "label": "AI Overview citations"},
            {"value": "89", "label": "Reviews in 90 days"},
            {"value": "$1.8M", "label": "New pipeline attributed"},
        ],
        "challenge": (
            "Gulf Coast Commercial Construction served greater Houston with strong project "
            "credentials but relied almost entirely on bid networks and word of mouth. Their "
            "Google presence was thin, categories were misaligned, and they were absent from AI "
            "generated answers when facility managers searched for commercial contractors in "
            "Houston, Katy, and The Woodlands."
        ),
        "solution": (
            "We rebuilt their Google Business Profile around commercial contracting categories, "
            "deployed project showcase posts weekly, and implemented a field-team review workflow "
            "after substantial completion milestones. Parallel AI optimization added structured "
            "project case content, LocalBusiness schema, and entity reinforcement across "
            "industry directories. Competitor gap analysis targeted Map Pack keywords with the "
            "highest bid-value in their service mix."
        ),
        "results": [
            "Qualified project leads increased 4.3x within 90 days of launch.",
            "Gulf Coast now appears in the top three AI Overview citations for multiple Houston "
            "metro commercial construction queries.",
            "Eighty-nine new reviews in 90 days established social proof that shortened sales "
            "cycles with procurement teams.",
            "Attribution tracking tied $1.8M in new pipeline directly to Google Maps and "
            "organic local touchpoints.",
        ],
        "quote": "The combination of GMB work plus AI optimization put us in conversations we were never part of before.",
        "cite": "Owner, Gulf Coast Commercial Construction",
    },
    {
        "tag": "Austin - Civil Engineering",
        "title": "Dominant Austin metro visibility and AI citations",
        "metrics": [
            {"value": "12", "label": "Top-3 Map Pack markets"},
            {"value": "Top 5", "label": "AI citation queries"},
            {"value": "2.8x", "label": "RFP invitations"},
            {"value": "64", "label": "Reviews in 4 months"},
        ],
        "challenge": (
            "Lone Star Civil Engineering had deep expertise in Austin metro transportation and "
            "site development but lost discoverability to national firms with larger marketing "
            "budgets. Location pages were thin, the GMB profile underrepresented their service "
            "footprint across Round Rock, Cedar Park, and Georgetown, and AI models rarely cited "
            "them for civil engineering recommendations in Central Texas."
        ),
        "solution": (
            "TSBR engineered a multi-city local SEO architecture: dedicated landing pages for "
            "each Austin metro submarket, consistent NAP across municipal and industry directories, "
            "and a GMB content calendar featuring project milestones and permitting expertise. "
            "AI-first content blocks answered procurement questions directly, supported by FAQ "
            "and Service schema. Review outreach targeted general contractors and developers after "
            "successful project closeout."
        ),
        "results": [
            "Lone Star achieved top-3 Map Pack visibility in 12 Austin metro markets within one "
            "quarter.",
            "RFP invitations increased 2.8x as developers found them through Google before "
            "bid lists were issued.",
            "AI citation monitoring showed top-5 placement for core civil engineering queries "
            "across Austin and Williamson County.",
            "Sixty-four reviews in four months established E-E-A-T signals that differentiated "
            "them from generic national competitors.",
        ],
        "quote": "TSBR made us the obvious local choice for civil engineering in Austin. Our partners now find us before we find them.",
        "cite": "James K., Managing Partner, Lone Star Civil Engineering",
    },
    {
        "tag": "San Antonio - Manufacturing Supplier",
        "title": "Map Pack dominance and 3.2x quote requests",
        "metrics": [
            {"value": "3.2x", "label": "Quote requests"},
            {"value": "8", "label": "#1 Map Pack rankings"},
            {"value": "76", "label": "Reviews generated"},
            {"value": "54 days", "label": "To first top-3 position"},
        ],
        "challenge": (
            "A San Antonio industrial supplier serving South Texas manufacturers had strong "
            "inventory and fulfillment capabilities but minimal digital presence. Competitors "
            "with smaller warehouses outranked them in Google Maps for critical RFQ searches. "
            "Inconsistent NAP data across legacy directories suppressed their primary listing."
        ),
        "solution": (
            "We consolidated duplicate listings, standardized NAP across 75 citations, and "
            "rebuilt the profile with product-category-aligned services, warehouse photography, "
            "and weekly posts highlighting stock availability and lead times. B2B keyword mapping "
            "targeted terms procurement teams use: industrial supplier San Antonio, manufacturing "
            "parts near me, and MRO distributor South Texas. Landing page optimization closed "
            "the loop between Maps clicks and quote form submissions."
        ),
        "results": [
            "Quote requests increased 3.2x within the first 90 days.",
            "Eight #1 Map Pack rankings across San Antonio and surrounding industrial corridors.",
            "First top-3 Map Pack position arrived in 54 days after profile relaunch.",
            "Seventy-six reviews from plant managers and maintenance supervisors provided "
            "keyword-rich credibility that improved both rankings and conversion.",
        ],
        "quote": "We stopped losing RFQs to smaller competitors who simply showed up first on Google. TSBR fixed that fast.",
        "cite": "VP of Sales, Alamo Industrial Supply, San Antonio",
    },
]


# ---------------------------------------------------------------------------
# Industries
# ---------------------------------------------------------------------------

INDUSTRIES = [
    "Industrial equipment and machine shops",
    "Commercial general contracting",
    "Manufacturing and fabrication",
    "Civil engineering and land development",
    "Mechanical and commercial HVAC",
    "Electrical contractors (commercial)",
    "Plumbing and pipefitting (B2B)",
    "Wholesale industrial distribution",
    "Logistics and freight services",
    "Commercial roofing and exterior",
    "Aerospace and defense suppliers",
    "Oil and gas field services",
    "Environmental and remediation services",
    "IT managed services (B2B)",
    "Commercial real estate services",
    "Architecture and design firms",
    "Staffing and workforce solutions",
    "Medical and dental B2B suppliers",
    "Fleet maintenance and heavy equipment",
    "Security and commercial systems integrators",
]


# ---------------------------------------------------------------------------
# Process steps
# ---------------------------------------------------------------------------

PROCESS_STEPS = [
    {
        "title": "Audit",
        "paragraph": (
            "Every engagement begins with a forensic audit of your Google Business Profile, "
            "citations, website local signals, competitor Map Pack positions, and AI Overview "
            "visibility. We document suppression risks, NAP inconsistencies, category gaps, and "
            "quick wins versus structural fixes. You receive a written report with a prioritized "
            "90-day roadmap before any implementation begins. This is the same audit we offer "
            "prospects for free because strategy without diagnosis is guesswork."
        ),
    },
    {
        "title": "Strategy",
        "paragraph": (
            "Mike Kaswatuka builds a market-specific plan based on how your buyers search in "
            "each Texas metro you serve. We map commercial keyword intent, estimate competitive "
            "difficulty, align GMB categories and services, and define success metrics: Map Pack "
            "rankings, review velocity, qualified lead volume, and AI citation targets. "
            "Multi-location clients receive a branch-by-branch rollout sequence that prevents "
            "listing conflict and cannibalization."
        ),
    },
    {
        "title": "Foundation Build",
        "paragraph": (
            "We fix the structural layer first: profile completeness, photo and video deployment, "
            "service and product entries, citation cleanup, on-page location optimization, and "
            "schema markup. Texas B2B buyers trust what they see. Facility tours, fleet imagery, "
            "certifications, and project proof published across GMB and your website establish "
            "the entity strength that both Google Maps and AI models reward."
        ),
    },
    {
        "title": "Launch",
        "paragraph": (
            "The GMB Velocity System goes live: weekly Google Posts, Q&A seeding, review "
            "acceleration workflows, and competitor monitoring. Content aligns with seasonal "
            "demand and regional terminology. DFW industrial buyers, Houston energy corridor "
            "procurement teams, and Austin tech vendors search differently. Launch creative and "
            "keyword targeting reflect those differences rather than applying a generic national "
            "playbook."
        ),
    },
    {
        "title": "Grow and Defend",
        "paragraph": (
            "Local search is not set-and-forget. Competitors react, algorithms shift, and AI "
            "Overviews expand into new query types. Ongoing management strengthens your signals, "
            "expands into adjacent service areas, reports ranking and lead attribution monthly, "
            "and defends Map Pack positions you earned. Clients who stay through the compounding "
            "phase see the largest ROI because authority accumulates across reviews, citations, "
            "content, and entity corroboration."
        ),
    },
]


# ---------------------------------------------------------------------------
# Why TSBR differentiators
# ---------------------------------------------------------------------------

WHY_TSBR = [
    {
        "title": "Texas-only B2B focus",
        "paragraph": (
            "We do not chase restaurants, salons, or national e-commerce brands. Every process, "
            "case study, and keyword framework is built for Texas commercial buyers with high "
            "deal values and long sales cycles. That specialization means faster diagnosis and "
            "strategies that speak the language of plant managers, estimators, and procurement "
            "officers."
        ),
    },
    {
        "title": "GMB as the revenue engine",
        "paragraph": (
            "Google Business Profile is the highest-ROI asset for most Texas B2B companies "
            "because buyers start on Maps. We treat GMB as an engineering project, not a "
            "checklist. Photos, posts, reviews, categories, and Q&A work together as a system "
            "that moves profiles from suppressed or invisible to top-3 Map Pack dominance."
        ),
    },
    {
        "title": "AI Overview engineering",
        "paragraph": (
            "Generative search is already shaping B2B vendor discovery. We build entity "
            "authority, structured answer content, and corroborating citations so AI models "
            "recommend your business by name. Clients appear in Google AI Overviews and other "
            "AI-powered answers while competitors still debate whether AI SEO is real."
        ),
    },
    {
        "title": "Direct founder access",
        "paragraph": (
            "You work with Mike Kaswatuka, not a rotating account coordinator. Mike has led "
            "Texas local search strategy since 2012 and personally audits competitive landscapes "
            "before recommending scope. That accountability shortens decision cycles and keeps "
            "strategy aligned with revenue goals."
        ),
    },
    {
        "title": "Measured on qualified leads",
        "paragraph": (
            "Rankings matter only when they produce pipeline. We track call volume, form "
            "submissions, quote requests, and CRM-sourced attribution. Vanity traffic and "
            "informational clicks that waste sales time are deliberately deprioritized in favor "
            "of commercial-intent keywords with proven close rates."
        ),
    },
    {
        "title": "Multi-location expertise",
        "paragraph": (
            "Texas B2B firms often serve multiple metros from a handful of branches. We "
            "standardize NAP, prevent duplicate listings, deploy location-specific content, and "
            "rank each market without internal competition. Statewide coverage from Arlington "
            "HQ means you have one partner for DFW, Houston, Austin, San Antonio, and beyond."
        ),
    },
]


# ---------------------------------------------------------------------------
# Free audit includes
# ---------------------------------------------------------------------------

AUDIT_INCLUDES = [
    "Complete Google Business Profile health scan",
    "Listing suppression and duplicate detection",
    "Primary category and service alignment review",
    "Map Pack ranking snapshot for top 20 keywords",
    "Organic local ranking baseline",
    "Top five competitor profile teardown",
    "Citation and NAP consistency analysis (50+ sources)",
    "Review profile velocity and sentiment assessment",
    "Photo and post activity benchmark vs competitors",
    "Website on-page local SEO evaluation",
    "Schema markup and structured data check",
    "AI Overview and generative search visibility audit",
    "Multi-location conflict identification (if applicable)",
    "Lead attribution and tracking gap analysis",
    "Written 90-day prioritized action plan",
]


# ---------------------------------------------------------------------------
# Service page rich content
# ---------------------------------------------------------------------------

SERVICE_RICH = {
    "gmb-optimization.html": {
        "intro": [
            (
                "Google Business Profile is the front door for Texas B2B revenue. When a plant "
                "manager in Irving searches industrial equipment repair near me or a Houston "
                "facilities director looks for commercial HVAC contractors, the Map Pack decides "
                "who gets the call. TSBR engineers every GMB signal so your profile earns top-3 "
                "positions and feeds clean entity data into AI Overviews."
            ),
            (
                "Our GMB Velocity System goes beyond filling out fields. We deploy photo "
                "campaigns, weekly posts, review acceleration, Q&A seeding, and competitor "
                "monitoring as an integrated system. Mike Kaswatuka has refined this framework "
                "across DFW, Houston, Austin, and San Antonio B2B markets since 2012. Average "
                "time to first Map Pack movement for our clients: 28 to 67 days."
            ),
        ],
        "deliverables": [
            "Full profile audit and duplicate listing resolution",
            "Primary and secondary category optimization",
            "Service and product catalog build-out with keyword alignment",
            "50 to 90+ professional geo-tagged photos and video",
            "Weekly Google Posts with Texas buyer-intent themes",
            "Q&A seeding and monitoring for trust signals",
            "Review request systems and response templates",
            "UTM tracking and call attribution setup",
            "Competitor Map Pack monitoring dashboard",
            "Citation and NAP consistency remediation",
            "Monthly performance reporting with ranking deltas",
            "AI Overview entity reinforcement via profile and site sync",
            "Seasonal campaign calendars for Texas demand cycles",
            "Multi-location rollout and cannibalization prevention",
        ],
        "timeline": (
            "Weeks 1-2: audit, cleanup, and foundation build. Weeks 3-8: Velocity System "
            "launch with posts, reviews, and photo velocity. Weeks 8-12: Map Pack movement "
            "and optimization based on performance data. Ongoing: weekly management and "
            "competitor defense."
        ),
        "faqs": [
            (
                "How is GMB optimization different from claiming my profile?",
                "Claiming a profile is step zero. Optimization is the ongoing engineering of "
                "categories, content, reviews, photos, and citations that actually moves rankings. "
                "Most Texas B2B profiles are claimed but under-optimized and suppressed."
            ),
            (
                "Can you fix a suspended Google Business Profile?",
                "Yes. We identify policy violations, duplicate conflicts, and NAP issues, then "
                "execute a safe reinstatement path. Fixing root causes prevents repeat suspensions."
            ),
            (
                "How many reviews do we need to rank in Texas metros?",
                "There is no universal number. We benchmark against Map Pack competitors in "
                "your specific market and build velocity targets. Most clients aim for 2 to 4 new "
                "reviews per week with detailed project context."
            ),
            (
                "Do you manage Google Posts for us?",
                "Yes. Weekly posts are core to the Velocity System. We handle copy, offers, "
                "project spotlights, and keyword alignment unless you prefer a collaborative "
                "approval workflow."
            ),
            (
                "Will GMB optimization help AI Overviews too?",
                "Absolutely. Your profile is a primary entity signal. We sync GMB data with "
                "website schema and citations so generative search models trust and cite your brand."
            ),
        ],
        "note": (
            "Average time to first Map Pack movement: 28-67 days for Texas B2B clients who "
            "implement the full Velocity System."
        ),
    },
    "ai-search-optimization.html": {
        "intro": [
            (
                "Texas procurement teams increasingly ask AI before they ask Google. When someone "
                "queries Which commercial contractor serves Houston energy corridor projects? or "
                "Best industrial supplier in San Antonio, generative answers decide which vendors "
                "enter the shortlist. AI search optimization ensures your company is the cited "
                "answer."
            ),
            (
                "TSBR builds entity authority through structured content, FAQ and Service schema, "
                "corroborating citations, review sentiment, and answer-first page architecture. "
                "We monitor AI Overview appearances and refine signals continuously. Clients "
                "typically see first AI citation movement within 45 to 75 days as entity strength "
                "compounds."
            ),
        ],
        "deliverables": [
            "Entity mapping across website, GMB, and directories",
            "Brand knowledge panel and consistency audit",
            "FAQ schema deployment on high-intent pages",
            "HowTo and Service structured data implementation",
            "Answer-first content blocks for buyer questions",
            "Topical cluster architecture for AI parsing",
            "E-E-A-T enhancement: case studies, credentials, founder bio",
            "Citation corroboration across authoritative sources",
            "Review sentiment optimization for trust signals",
            "AI Overview appearance monitoring and reporting",
            "Competitor AI citation gap analysis",
            "Internal linking strategy for entity reinforcement",
            "Content refresh calendar for generative search freshness",
            "Integration with GMB and local SEO signal stack",
        ],
        "timeline": (
            "Month 1: entity audit and schema foundation. Month 2: content engineering and "
            "citation corroboration. Month 3: AI visibility monitoring and iteration. Ongoing: "
            "monthly citation tracking and content updates as AI query patterns evolve."
        ),
        "faqs": [
            (
                "What is AI search optimization for local B2B?",
                "It is the practice of strengthening your business entity so generative models "
                "cite you in answers to local commercial queries. It combines schema, content "
                "structure, citations, and authority signals."
            ),
            (
                "Does this replace traditional SEO?",
                "No. AI optimization layers on top of local SEO and GMB. The strongest results "
                "come when Maps, organic, and AI signals tell the same story."
            ),
            (
                "How do you measure AI visibility?",
                "We track Google AI Overview appearances, branded mentions in generative answers, "
                "and referral patterns from AI-assisted search journeys alongside traditional "
                "ranking reports."
            ),
            (
                "Which Texas industries benefit most?",
                "High-consideration B2B categories: contracting, engineering, manufacturing, "
                "industrial supply, and professional services where buyers research vendors deeply "
                "before contacting."
            ),
            (
                "How fast can we appear in AI Overviews?",
                "Most clients see initial citation movement in 45-75 days. Competitive metros "
                "like Houston and Dallas may require longer entity compounding."
            ),
        ],
        "note": (
            "AI Overview visibility typically begins within 45-75 days as entity signals strengthen."
        ),
    },
    "local-seo-texas.html": {
        "intro": [
            (
                "Local SEO for Texas B2B requires more than a handful of directory listings. "
                "Buyers search with metro-specific intent: commercial electrician Plano, civil "
                "engineering firm Round Rock, industrial distributor DFW. Your site, citations, "
                "and content must reinforce every market you serve while maintaining flawless NAP "
                "consistency."
            ),
            (
                "TSBR delivers full-stack local SEO: citation building across 70+ sources, "
                "location and service page optimization, technical fixes, content silos, and "
                "local link acquisition. We align organic rankings with GMB Map Pack positions "
                "so prospects find you whether they click Maps or blue-link results. Serving "
                "every major Texas metro from our Arlington headquarters."
            ),
        ],
        "deliverables": [
            "NAP audit and remediation across all listings",
            "70+ citation builds on authoritative directories",
            "Google, Bing, and Apple Maps verification support",
            "Location page creation for each Texas service area",
            "Service page on-page optimization with local modifiers",
            "Technical SEO: speed, mobile, crawl, indexation",
            "Content silo architecture for topical authority",
            "Internal linking strategy across locations and services",
            "Local and industry-relevant link acquisition",
            "GBP-to-website consistency and cross-linking",
            "Monthly ranking reports for Maps and organic",
            "Competitor gap analysis by metro",
            "Duplicate listing suppression and monitoring",
            "Lead attribution alignment with CRM fields",
        ],
        "timeline": (
            "Month 1: citation cleanup and on-page foundation. Month 2: content silos and "
            "location expansion. Month 3: link building and ranking acceleration. Ongoing: "
            "monthly optimization, new market rollout, and citation monitoring."
        ),
        "faqs": [
            (
                "Why do Texas B2B companies need local SEO if they are not retail?",
                "B2B buyers still search locally. Even national accounts choose vendors they "
                "perceive as established in their metro. Local SEO builds that trust and "
                "discoverability."
            ),
            (
                "How many location pages do we need?",
                "One quality page per market you genuinely serve. We avoid thin doorway pages "
                "and build substantive content with local proof points."
            ),
            (
                "Are citations still important in 2026?",
                "Yes. Citations corroborate your NAP entity. Inconsistent data suppresses "
                "rankings and confuses AI models. We treat citations as foundational, not legacy."
            ),
            (
                "Can you rank us in multiple Texas metros?",
                "Yes. Multi-market strategy is a core competency. Each metro gets tailored "
                "keyword research, citations, and content without cannibalizing sister locations."
            ),
            (
                "How does local SEO connect to lead generation?",
                "Organic local rankings capture buyers who scroll past the Map Pack. Combined "
                "with GMB, you own the full SERP real estate for high-intent commercial queries."
            ),
        ],
        "note": (
            "We serve every major Texas metro and many secondary markets statewide from Arlington HQ."
        ),
    },
    "b2b-lead-generation.html": {
        "intro": [
            (
                "B2B lead generation through search is not about traffic volume. It is about "
                "qualified commercial inquiries from buyers ready to request quotes, schedule "
                "site visits, or issue RFQs. Texas industrial and contracting firms waste sales "
                "time on informational clicks when keywords are misaligned. TSBR optimizes for "
                "intent that closes."
            ),
            (
                "We map the exact searches your buyers use across Google Maps, organic results, "
                "and AI Overviews, then engineer conversion paths: profile CTAs, landing pages, "
                "call tracking, and CRM-ready lead routing. Clients average 4.3x increase in "
                "qualified lead volume within 90 days when the full local search stack is deployed."
            ),
        ],
        "deliverables": [
            "Commercial keyword intent mapping by metro",
            "Buyer persona and search journey documentation",
            "GMB CTA and messaging optimization for lead capture",
            "Landing page build or optimization for quote requests",
            "Call tracking with source attribution",
            "Form optimization and friction reduction",
            "UTM structure for Maps, organic, and paid alignment",
            "CRM integration and lead source field setup",
            "Sales team lead quality scoring framework",
            "Monthly lead volume and close-rate reporting",
            "Negative keyword and content deprioritization plan",
            "Multi-channel funnel: Maps + organic + AI touchpoints",
            "Review and proof assets that shorten sales cycles",
            "Quarterly strategy review with Mike Kaswatuka",
        ],
        "timeline": (
            "Weeks 1-3: intent mapping and tracking setup. Weeks 4-8: profile and landing page "
            "conversion optimization. Weeks 8-12: lead volume scaling and quality tuning. "
            "Ongoing: monthly attribution reporting and keyword refinement."
        ),
        "faqs": [
            (
                "How is B2B lead gen different from B2C?",
                "B2B searches use commercial modifiers, higher specificity, and longer consideration "
                "cycles. We target quote-ready intent, not tire-kicker informational queries."
            ),
            (
                "Can you guarantee a number of leads?",
                "We guarantee process and measurable improvement targets agreed in scope. Lead "
                "volume varies by market competitiveness and your offer strength."
            ),
            (
                "Do you run Google Ads?",
                "Our focus is organic local search, GMB, and AI visibility. Those channels "
                "deliver compounding ROI. We can coordinate with your paid team on keyword alignment."
            ),
            (
                "How do you prevent low-quality leads?",
                "Intent mapping, keyword exclusion, and profile messaging filter out consumer and "
                "informational traffic. Sales feedback loops refine targeting monthly."
            ),
            (
                "What does 4.3x lead volume mean in practice?",
                "It is our client average for qualified inquiries within 90 days, measured against "
                "pre-engagement baselines with call and form attribution."
            ),
        ],
        "note": (
            "Our clients average 4.3x increase in qualified lead volume within 90 days."
        ),
    },
}


# ---------------------------------------------------------------------------
# Location page rich content
# ---------------------------------------------------------------------------

LOCATION_RICH = {
    "arlington-tx-seo-marketing-consultant.html": {
        "local_intro": [
            (
                "Arlington is home base for The Stone Builders Rejected. From our office on "
                "Brynmawr Court we serve the full DFW Metroplex with deep knowledge of how "
                "industrial buyers, contractors, and B2B service firms search across Arlington, "
                "Grand Prairie, Irving, Mansfield, and the greater Mid-Cities corridor."
            ),
            (
                "DFW is one of the most competitive local search markets in the country. Profiles "
                "that look complete still get suppressed without citation consistency, review "
                "velocity, and AI-ready entity signals. We help Arlington-area B2B companies "
                "become the cornerstone result in Google Maps and AI Overviews."
            ),
        ],
        "industries": [
            "Industrial equipment and machine shops",
            "Commercial contracting",
            "Logistics and warehousing",
            "Aerospace suppliers",
            "Automotive manufacturing support",
        ],
        "local_faq": [
            (
                "Why hire a local Arlington SEO consultant vs a national agency?",
                "National agencies apply generic playbooks. We live in DFW, audit competitors "
                "block by block, and know which industrial corridors generate the highest-value "
                "Map Pack clicks."
            ),
            (
                "Do you meet clients in person in Arlington?",
                "Yes. We offer on-site consultations for Arlington and DFW clients who want "
                "facility walkthroughs for photo and content strategy."
            ),
            (
                "How fast can Arlington B2B companies see Map Pack results?",
                "Most clients see movement in 30-60 days and top-3 positions in 74-90 days "
                "with full Velocity System implementation."
            ),
        ],
        "search_behavior": (
            "DFW commercial buyers search with metro and corridor modifiers: near DFW airport, "
            "industrial Arlington TX, Grand Prairie machine shop. They compare Map Pack results "
            "on mobile during site visits and often call directly from the listing. AI-assisted "
            "searches are rising among procurement staff researching vendors before RFP issuance."
        ),
    },
    "dallas-tx-seo-marketing-consultant.html": {
        "local_intro": [
            (
                "Dallas anchors North Texas commerce. B2B companies compete for visibility from "
                "Uptown corporate headquarters to industrial districts along I-35 and I-45. "
                "TSBR helps Dallas firms dominate Google Maps and organic local results for "
                "high-value commercial keywords."
            ),
            (
                "Dallas search competition rewards completeness and velocity: fresh photos, weekly "
                "posts, consistent NAP across dozens of directories, and website content that "
                "corroborates your GMB entity. We engineer all three layers so you capture "
                "buyers whether they click Maps, organic links, or AI-generated answers."
            ),
        ],
        "industries": [
            "Commercial construction",
            "Professional services",
            "Financial B2B services",
            "Technology and IT services",
            "Wholesale distribution",
        ],
        "local_faq": [
            (
                "Is Dallas Map Pack competition harder than suburban DFW?",
                "Generally yes. We prioritize category precision, review velocity, and targeted "
                "service-area pages to win Dallas proper plus priority suburbs."
            ),
            (
                "Can you rank us in Dallas if our office is in Arlington?",
                "Yes. Service-area businesses rank in Dallas through proper GMB configuration, "
                "citations, and location content without violating Google guidelines."
            ),
            (
                "What Dallas industries see the fastest ROI?",
                "Commercial contracting, industrial supply, and B2B professional services with "
                "high average contract values."
            ),
        ],
        "search_behavior": (
            "Dallas buyers often search by neighborhood and corridor: Uptown, Deep Ellum, "
            "Design District, and logistics hubs near I-20. Mobile Map Pack clicks drive calls "
            "during business hours. Enterprise buyers research vendors on desktop and increasingly "
            "through AI Overviews before shortlisting for procurement."
        ),
    },
    "fort-worth-tx-seo-marketing-consultant.html": {
        "local_intro": [
            (
                "Fort Worth blends industrial heritage with rapid west DFW growth. Manufacturing, "
                "fabrication, logistics, and trade contractors serve Alliance corridor, Stockyards "
                "district businesses, and expanding suburban markets in Keller and Benbrook."
            ),
            (
                "Fort Worth B2B search behavior differs from Dallas: more industrial and "
                "trade-focused queries, stronger emphasis on fleet and facility proof, and "
                "buyers who value local reputation signals. TSBR tailors GMB and content "
                "strategy to how Fort Worth commercial buyers actually decide."
            ),
        ],
        "industries": [
            "Manufacturing and fabrication",
            "Industrial equipment",
            "Commercial roofing",
            "Fleet and transportation services",
            "Oil and gas field services",
        ],
        "local_faq": [
            (
                "Do Fort Worth and Dallas require separate SEO strategies?",
                "Often yes. Keyword competition, buyer language, and Map Pack competitors differ. "
                "We build market-specific plans rather than one DFW blanket approach."
            ),
            (
                "Can you help Alliance area industrial companies?",
                "Yes. Alliance and north Fort Worth industrial zones are a core focus for "
                "equipment, logistics, and manufacturing clients."
            ),
            (
                "How important are reviews for Fort Worth trade contractors?",
                "Critical. Trade buyers read reviews for reliability and safety. Systematic "
                "review velocity is non-negotiable for Map Pack dominance."
            ),
        ],
        "search_behavior": (
            "Fort Worth searches emphasize industrial and trade terms: fabrication Fort Worth, "
            "commercial roofer west DFW, machine shop near Alliance. Buyers review photos of "
            "facilities and fleet before calling. Weekend searches are lower than Dallas corporate "
            "markets; weekday business-hour visibility is paramount."
        ),
    },
    "houston-tx-seo-marketing-consultant.html": {
        "local_intro": [
            (
                "Greater Houston is Texas largest B2B market. Energy corridor firms, commercial "
                "contractors, industrial suppliers, and port logistics companies compete for "
                "visibility across Houston proper, Katy, Sugar Land, Pearland, and The Woodlands."
            ),
            (
                "Houston local search demands hurricane-season relevance, sprawling geography "
                "coverage, and entity strength that survives AI Overview scrutiny. TSBR clients "
                "like Gulf Coast Commercial Construction have achieved 4.3x lead growth through "
                "combined GMB and AI optimization."
            ),
        ],
        "industries": [
            "Commercial contracting",
            "Energy and petrochemical services",
            "Industrial supply and MRO",
            "Port and logistics",
            "Environmental remediation",
        ],
        "local_faq": [
            (
                "How do you handle Houston sprawl in local SEO?",
                "We map priority service radii, build location pages for key suburbs, and "
                "configure GMB service areas without diluting the primary listing."
            ),
            (
                "Is Houston more competitive than DFW for contractors?",
                "In many contracting verticals, yes. Review velocity and project proof content "
                "separate winners from invisible incumbents."
            ),
            (
                "Do you serve The Woodlands and Katy from Houston strategy?",
                "Yes. North and west Houston suburbs have distinct search patterns we address "
                "with dedicated content and citation targets."
            ),
        ],
        "search_behavior": (
            "Houston buyers search by freeway and suburb: Energy Corridor, Katy Freeway, "
            "Ship Channel industrial. Hurricane and weather-related service spikes require "
            "seasonal GMB posts. Facilities managers increasingly use AI to build vendor "
            "shortlists before formal RFP processes."
        ),
    },
    "austin-tx-seo-marketing-consultant.html": {
        "local_intro": [
            (
                "Austin combines tech-sector procurement with booming commercial construction "
                "and civil infrastructure growth. B2B firms compete across Austin proper, "
                "Round Rock, Cedar Park, Georgetown, and the entire I-35 growth corridor."
            ),
            (
                "Austin buyers research deeply. They read reviews, compare credentials, and ask "
                "AI for recommendations before engaging vendors. TSBR helped Lone Star Civil "
                "Engineering achieve dominant metro visibility through multi-city content "
                "architecture and AI citation engineering."
            ),
        ],
        "industries": [
            "Civil engineering",
            "Commercial construction",
            "Technology B2B services",
            "Environmental consulting",
            "Architecture and design",
        ],
        "local_faq": [
            (
                "How fast is Austin local search growing?",
                "Rapidly. New entrants flood Map Packs monthly. Early entity and review "
                "investment prevents later catch-up costs."
            ),
            (
                "Should we target Round Rock and Cedar Park separately?",
                "If you serve those markets, yes. Dedicated pages and citations improve "
                "rankings versus a single Austin-only focus."
            ),
            (
                "Does Austin tech culture affect B2B search?",
                "Yes. Buyers expect polished digital presence, fast sites, and authoritative "
                "content. Thin profiles underperform even with strong offline reputation."
            ),
        ],
        "search_behavior": (
            "Austin searches blend tech and trades: commercial contractor Austin, SaaS "
            "implementation partner Round Rock, civil engineering firm Central Texas. "
            "Mobile Map Pack usage is high among site supervisors. AI Overview adoption "
            "among procurement teams is above the Texas average."
        ),
    },
    "san-antonio-tx-seo-marketing-consultant.html": {
        "local_intro": [
            (
                "San Antonio and South Texas industrial corridors rely on local discoverability "
                "for manufacturing supply, defense contractors, and commercial trades. Buyers "
                "across San Antonio, New Braunfels, Schertz, and Seguin search Google first "
                "when sourcing vendors."
            ),
            (
                "Map Pack dominance in San Antonio translated to 3.2x quote requests for our "
                "manufacturing supplier clients. TSBR builds citation consistency, review "
                "systems, and product-aligned GMB services that match how plant managers "
                "issue RFQs."
            ),
        ],
        "industries": [
            "Manufacturing supply and MRO",
            "Defense and aerospace contractors",
            "Commercial HVAC and mechanical",
            "Healthcare B2B services",
            "Food and beverage industrial supply",
        ],
        "local_faq": [
            (
                "Is San Antonio less competitive than Houston or DFW?",
                "In some niches, yes, but industrial supply and defense sectors are fiercely "
                "contested. Speed to top-3 still requires systematic optimization."
            ),
            (
                "Do you cover New Braunfels and corridor cities?",
                "Yes. We build South and Central Texas coverage through service-area strategy "
                "and dedicated location content."
            ),
            (
                "How do reviews affect San Antonio industrial rankings?",
                "Plant managers trust peer reviews mentioning lead times, inventory depth, and "
                "delivery reliability. Keyword-rich reviews accelerate Map Pack movement."
            ),
        ],
        "search_behavior": (
            "San Antonio buyers search with military and manufacturing context: industrial "
            "supplier San Antonio, defense contractor near Randolph, MRO parts South Texas. "
            "Many RFQs begin with a Maps search from the plant floor on mobile devices."
        ),
    },
    "plano-frisco-dfw-north-tx-seo-marketing-consultant.html": {
        "local_intro": [
            (
                "Plano, Frisco, McKinney, Allen, and Prosper form the corporate growth engine "
                "of north DFW. Headquarters operations, professional services, and commercial "
                "vendors compete for visibility among affluent B2B buyers with high expectations."
            ),
            (
                "North DFW Map Packs favor profiles with corporate polish: professional imagery, "
                "consistent posting, strong review counts, and website authority that matches "
                "the premium positioning of the market. TSBR delivers that standard for "
                "Texas B2B firms targeting the corporate corridor."
            ),
        ],
        "industries": [
            "Professional services",
            "IT managed services",
            "Commercial construction",
            "Staffing and workforce solutions",
            "Financial B2B services",
        ],
        "local_faq": [
            (
                "Why is north DFW different from central Dallas SEO?",
                "Buyer demographics, average contract values, and competitor sets differ. "
                "Suburban corporate buyers search with city-specific modifiers like Plano and Frisco."
            ),
            (
                "Can one GMB listing cover Plano and Frisco?",
                "Service-area configuration can cover both, but dedicated content and citations "
                "for each city improve multi-market rankings."
            ),
            (
                "What results have you seen in Plano/Frisco?",
                "Clients have achieved multi-city top-3 Map Pack positions within 90 days using "
                "the Velocity System and location page architecture."
            ),
        ],
        "search_behavior": (
            "North DFW searches emphasize city names: commercial contractor Frisco, IT support "
            "Plano, staffing agency McKinney. Desktop research during business hours is common "
            "among corporate procurement. Reviews mentioning responsiveness and enterprise "
            "experience influence shortlist decisions."
        ),
    },
    "round-rock-cedar-park-georgetown-tx-seo-marketing-consultant.html": {
        "local_intro": [
            (
                "North Austin metro suburbs are among the fastest-growing B2B markets in Texas. "
                "Round Rock, Cedar Park, Georgetown, Leander, and Pflugerville each have "
                "distinct Map Pack competitors and buyer communities."
            ),
            (
                "Companies headquartered in Austin often miss suburban search intent. TSBR "
                "builds dedicated north-metro visibility so you rank where growth is happening, "
                "not only in Austin city limits."
            ),
        ],
        "industries": [
            "Commercial construction",
            "HVAC and mechanical contractors",
            "Healthcare B2B",
            "Professional services",
            "Home builder trade partners (B2B)",
        ],
        "local_faq": [
            (
                "Should we create separate pages for Round Rock and Cedar Park?",
                "If you serve both, substantive location pages improve rankings versus a single "
                "generic Austin page."
            ),
            (
                "How does Williamson County search differ from Travis County?",
                "Suburban family and business growth drives more trade and services queries "
                "with explicit city names. Localization matters."
            ),
            (
                "Can TSBR manage our Austin and north-metro presence together?",
                "Yes. We coordinate one entity strategy with market-specific content layers."
            ),
        ],
        "search_behavior": (
            "Buyers search Round Rock, Cedar Park, and Georgetown by name rather than Austin "
            "alone. Commercial contractors and mechanical trades see strong mobile Map Pack "
            "traffic from new development zones along 79 and 183A."
        ),
    },
    "the-woodlands-katy-tx-seo-marketing-consultant.html": {
        "local_intro": [
            (
                "The Woodlands and Katy represent Houston affluent north and west growth "
                "corridors. Commercial contractors, professional services, and healthcare B2B "
                "firms compete for Map Pack visibility among discerning buyers."
            ),
            (
                "Suburban Houston search requires distinct strategy from inner-loop Houston. "
                "TSBR deploys citation targets, localized content, and GMB post calendars "
                "aligned to Woodlands and Katy buyer behavior."
            ),
        ],
        "industries": [
            "Commercial contracting",
            "Luxury commercial finishes",
            "Healthcare B2B and medical supply",
            "Landscape and exterior commercial",
            "Professional services",
        ],
        "local_faq": [
            (
                "Do Katy and The Woodlands need separate SEO efforts?",
                "Distinct content and citation emphasis for each suburb improves visibility "
                "versus a single generic Houston page."
            ),
            (
                "How competitive are Map Packs in The Woodlands?",
                "Highly competitive for contractors and professional services. Review depth "
                "and project photography are decisive."
            ),
            (
                "Can you integrate with our Houston HQ listing?",
                "Yes. We coordinate multi-suburb strategy without duplicate listing violations."
            ),
        ],
        "search_behavior": (
            "Woodlands and Katy buyers search with master-planned community context and "
            "freeway references: contractor Katy TX, commercial HVAC The Woodlands. "
            "Affluent B2B buyers compare multiple Map Pack listings before first contact."
        ),
    },
    "texas-statewide-seo-marketing-consultant.html": {
        "local_intro": [
            (
                "Many Texas B2B companies operate across multiple metros: DFW and Houston, "
                "Austin and San Antonio, or true statewide coverage including Corpus Christi, "
                "El Paso, Lubbock, and Tyler. Multi-market SEO requires coordination, not "
                "duplicated effort."
            ),
            (
                "TSBR manages statewide accounts from Arlington with market-specific playbooks "
                "for each region. We prevent NAP conflicts, listing duplication, and keyword "
                "cannibalization while scaling GMB Velocity Systems across your branch network."
            ),
        ],
        "industries": [
            "Multi-location industrial services",
            "Statewide contracting firms",
            "Regional distribution networks",
            "Franchise and dealer networks",
            "Professional services with Texas offices",
        ],
        "local_faq": [
            (
                "How do you prioritize markets in a statewide rollout?",
                "We start with highest-revenue metros and competitive gap analysis, then "
                "sequence branch optimization to compound authority without overwhelming your team."
            ),
            (
                "One agency for all Texas markets?",
                "Yes. Consistent entity strategy across markets prevents conflicting NAP and "
                "message drift that hurts AI and Maps rankings."
            ),
            (
                "Do you serve smaller Texas cities outside major metros?",
                "Yes. Secondary markets like Waco, Tyler, Beaumont, and Amarillo are included "
                "in statewide engagements with tailored citation and content plans."
            ),
        ],
        "search_behavior": (
            "Statewide buyers search with city plus service modifiers in each region. "
            "Corporate procurement may research HQ vendors but issue POs to local branches. "
            "Multi-location brands must rank locally in every city they serve, not only at "
            "headquarters."
        ),
    },
}


BLOG_ARTICLES = [
    {
        "slug": "gmb-velocity-system-texas.html",
        "title": "Proprietary GMB Velocity System for Texas B2B",
        "tag": "GMB",
        "desc": "How TSBR Velocity System delivers top 3-pack rankings and AI visibility for Texas B2B companies.",
        "read_time": "12 min",
        "published": "2026-01-08",
        "toc": [
            ("velocity-overview", "What the Velocity System is"),
            ("velocity-components", "Core components"),
            ("velocity-timeline", "90-day timeline"),
            ("velocity-texas", "Why it works in Texas"),
            ("velocity-mistakes", "Critical mistakes"),
            ("velocity-measurement", "Measuring success"),
            ("velocity-case", "DFW case pattern"),
            ("velocity-start", "Getting started"),
        ],
        "body_html": """
<h2 id="velocity-overview">What the GMB Velocity System is</h2>
<p>The GMB Velocity System is TSBR proprietary framework for moving Texas B2B Google Business Profiles from suppressed or invisible to top-three Map Pack dominance in sixty to ninety days. Unlike checklist optimization that fills fields once and hopes for movement, Velocity treats your profile as a living revenue asset with weekly signal deployment across photos, posts, reviews, Q and A, citations, and competitor response.</p>
<p>Mike Kaswatuka developed this system across Arlington, Dallas, Houston, Austin, and San Antonio industrial and contracting markets since 2012. Precision Machine Works in Irving moved from page nine to seventeen number-one Map Pack positions in seventy-four days using Velocity. Gulf Coast Commercial Construction in Houston achieved four point three times lead volume with combined Map Pack and AI citation dominance.</p>
<p>Velocity works because Google Maps ranking is not a single-factor game. Proximity, relevance, and prominence interact continuously. Texas commercial buyers add urgency: they search on mobile from job sites, compare three Map Pack listings in seconds, and call the business that looks most credible immediately. Velocity engineers that credibility at speed without violating Google guidelines.</p>
<p>Many agencies treat Google Business Profile as a setup task completed in an afternoon. That approach fails in DFW, Houston, and Austin metros where Map Pack competitors invest in ongoing content. Velocity is the operating system for profiles that must generate qualified B2B leads month after month.</p>

<h2 id="velocity-components">Core components of the Velocity System</h2>
<p>Five integrated components drive the system. Removing any one slows compounding and extends time to top-three positions.</p>
<h3>Profile reconstruction and category precision</h3>
<p>We audit primary and secondary categories against actual buyer searches in your Texas markets. Industrial equipment firms often choose generic categories that attract consumer clicks and repel commercial buyers. We align services, products, and attributes with terms like commercial CNC machining Irving, industrial pump repair DFW, and manufacturing support Grand Prairie.</p>
<p>Category misalignment is the silent killer of B2B Map Pack campaigns. Google matches queries to category semantics. If your competitors use precise commercial categories and you do not, you are filtered out before prominence even matters.</p>
<h3>Photo and video velocity</h3>
<p>Profiles with fewer than twenty photos rarely compete in Texas metros. Velocity deploys fifty to ninety geo-tagged images in the first thirty days: facility exteriors, production floors, fleet, certifications, team in PPE, and completed projects. Captions include city and service keywords naturally. Video walkthroughs increase engagement metrics Google measures and give AI models visual proof of operations.</p>
<p>Photo velocity is not a one-time upload. We add fresh project and team images weekly during launch phase to signal active management. Stale galleries tell buyers and algorithms the business may be inactive.</p>
<h3>Weekly Google Posts engine</h3>
<p>Posts are not optional decorations. They signal active management and match seasonal buyer intent. Hurricane season readiness posts for Houston contractors, year-end capital equipment posts for manufacturers, and Q1 procurement reminders for B2B services all align with how Texas buyers search through the calendar.</p>
<p>Each post uses tracked URLs, clear CTAs, and keyword themes mapped to your service catalog. We rotate offers, project spotlights, hiring announcements, and educational tips to avoid repetitive patterns that reduce engagement.</p>
<h3>Review acceleration with keyword context</h3>
<p>Reviews are prominence fuel. We implement post-project workflows that generate two to four new reviews per week from legitimate customers. We coach clients to mention project type, city, and service in authentic language. A review stating responsive commercial HVAC install in Katy carries more ranking and conversion weight than great service alone.</p>
<p>Review responses are part of Velocity. Mike Kaswatuka templates responses that reinforce services and service areas while staying natural. Ignoring reviews wastes a public SEO surface.</p>
<h3>Q and A seeding and competitor monitoring</h3>
<p>Pre-seeded Q and A answers buyer objections before they call competitors: licensing, insurance, service radius, emergency response, and lead times. We monitor Map Pack movement weekly and adjust post themes when competitors surge. Velocity is offensive and defensive.</p>

<div class="highlight-box">
<strong>Velocity benchmark:</strong> Texas B2B clients average first Map Pack movement in twenty-eight to sixty-seven days with full implementation. Dominant multi-keyword top-three clusters typically arrive by day ninety.
</div>

<h2 id="velocity-timeline">Ninety-day implementation timeline</h2>
<table>
<thead><tr><th>Phase</th><th>Days</th><th>Primary actions</th><th>Expected outcomes</th></tr></thead>
<tbody>
<tr><td>Audit</td><td>1-10</td><td>Duplicate resolution, NAP cleanup, category alignment, competitor teardown</td><td>Clean authoritative listing, baseline rankings</td></tr>
<tr><td>Foundation</td><td>11-25</td><td>Photo deployment, service build-out, citation push, website sync</td><td>Profile completeness score above ninety percent</td></tr>
<tr><td>Launch</td><td>26-45</td><td>Weekly posts, review workflows live, Q and A seeded, call tracking verified</td><td>First ranking movement, engagement lift</td></tr>
<tr><td>Accelerate</td><td>46-75</td><td>Suburban keyword expansion, AI schema reinforcement, competitor counter-moves</td><td>Top-three entries on priority keywords</td></tr>
<tr><td>Defend</td><td>76-90</td><td>Multi-location coordination, content refresh, prominence compounding</td><td>Stable Map Pack ownership, lead attribution clarity</td></tr>
</tbody>
</table>

<h2 id="velocity-texas">Why Velocity works specifically in Texas B2B markets</h2>
<p>Texas buyers search with geographic precision. A Dallas buyer rarely clicks a Fort Worth listing unless prominence signals overwhelm proximity. Multi-metro service firms need Velocity executed per service area with location pages and citations backing each zone.</p>
<p>B2B deal values justify aggressive investment. One commercial contract can exceed a year of marketing spend. Velocity targets quote-ready searches, not informational traffic that wastes estimator and inside sales time.</p>
<p>AI Overviews consume Google Business Profile entity data. Profiles with consistent categories, fresh posts, and review sentiment feed generative answers. Velocity clients increasingly appear when procurement staff ask AI for vendor recommendations in Houston, Austin, and DFW.</p>
<p>Texas economic diversity matters. Energy corridor buyers in Houston use different language than Austin tech procurement or San Antonio manufacturing plant managers. Velocity calendars reflect regional terminology and proof points.</p>

<h2 id="velocity-mistakes">Critical mistakes that kill Velocity results</h2>
<ul>
<li>Purchasing fake reviews or engagement spikes that trigger suspension</li>
<li>Pushing photo velocity while NAP remains inconsistent across citations</li>
<li>Using consumer-facing categories for commercial-only services</li>
<li>Stopping Google Posts after an initial ranking bump</li>
<li>Ignoring duplicate listings that split review authority across profiles</li>
<li>Using generic stock photography without facility, fleet, or project proof</li>
<li>Failing to implement call tracking so leads cannot be attributed</li>
<li>Setting unrealistic service areas that dilute relevance signals</li>
</ul>

<h2 id="velocity-measurement">How TSBR measures Velocity success</h2>
<p>Rankings alone are insufficient for B2B. Velocity reporting tracks Map Pack positions for agreed commercial keywords, review velocity and sentiment trends, Google Posts engagement, calls and form submissions with source attribution, and AI Overview citation appearances where applicable.</p>
<ol>
<li>Baseline audit score and ranking snapshot on day zero</li>
<li>Weekly internal ranking checks during launch phase</li>
<li>Monthly client reports with competitor movement deltas</li>
<li>Quarterly strategy review with Mike Kaswatuka for market expansion</li>
<li>CRM-aligned lead quality feedback from your sales team</li>
</ol>
<p>Texas B2B success means qualified pipeline and closed revenue, not vanity traffic. We deprioritize keywords that generate clicks without quote requests.</p>

<h2 id="velocity-case">Case pattern: industrial equipment in DFW</h2>
<p>Precision Machine Works arrived with strong offline reputation and weak digital signals. Competitors with inferior equipment owned the Map Pack because they invested in profile velocity earlier. Within seventy-four days of Velocity deployment they held seventeen number-one positions, generated ninety-one reviews, and increased commercial quote requests six hundred twenty percent.</p>
<p>The pattern repeats across verticals: foundation fix, content velocity, review systems, citation corroboration, AI-ready website sync. Velocity is repeatable because it respects how Google weights prominence over time.</p>

<h2 id="velocity-start">Getting started with Velocity</h2>
<p>Request a free Velocity readiness audit from TSBR in Arlington. We score your profile against Map Pack competitors in your Texas markets and deliver a written ninety-day action plan whether you hire us or not. If you are invisible despite superior service, Velocity is how overlooked companies become market cornerstones.</p>
<p>Call (682) 206-4178 or email hello@tsbrenterprises.com. We respond to audit requests within four business hours on weekdays.</p>
        """,
    },
    {
        "slug": "google-business-profile-ranking-texas.html",
        "published": "2026-01-22",
        "title": "How to Rank Your Google Business Profile in Texas",
        "tag": "Guide",
        "desc": "Complete playbook for Map Pack dominance across DFW, Houston, Austin, and San Antonio.",
        "read_time": "13 min",
        "toc": [
            ("gbp-ranking-intro", "Why GBP ranking matters"),
            ("gbp-complete-fields", "Complete every field"),
            ("gbp-photos", "Photo velocity"),
            ("gbp-reviews", "Review acceleration"),
            ("gbp-posts", "Weekly posts"),
            ("gbp-citations", "NAP consistency"),
            ("gbp-website", "Website alignment"),
            ("gbp-ai", "AI Overview prep"),
            ("gbp-competitive", "Competitive analysis"),
            ("gbp-next", "Next steps"),
        ],
        "body_html": """
<h2 id="gbp-ranking-intro">Why Google Business Profile ranking decides Texas B2B revenue</h2>
<p>When a facilities manager in Plano searches commercial roofing contractor near me, Google decides which three businesses appear in the Map Pack. Those three listings capture the majority of calls and direction requests. Everyone on page two of Maps might as well be invisible. For Texas B2B companies with high contract values, Map Pack ranking is not a marketing nice-to-have. It is the front door.</p>
<p>This guide is the complete playbook TSBR uses to rank Google Business Profiles across DFW, Houston, Austin, San Antonio, and statewide multi-location accounts. Mike Kaswatuka has executed these steps for industrial suppliers, contractors, engineers, and professional services firms since 2012.</p>
<p>Ranking factors cluster into relevance, distance, and prominence. You cannot change your proximity to every searcher, but you can maximize relevance and prominence through categories, services, content velocity, reviews, citations, and website alignment. Texas metros are competitive enough that partial optimization fails.</p>

<h2 id="gbp-complete-fields">Step 1: Complete every field with commercial intent</h2>
<p>Google rewards completeness. Fill business name exactly as registered, primary and secondary categories that match commercial searches, full service list with descriptions, products where applicable, attributes, opening hours including special hours, service areas, and a keyword-rich description written for humans first.</p>
<p>B2B firms often under-fill services. List every commercial service line separately: emergency repair, planned maintenance, installation, inspection, consulting. Each entry is a relevance hook for long-tail Map Pack queries.</p>
<p>Avoid keyword stuffing in the business name. Google suspends manipulated names. Put keywords in services, posts, and website content instead.</p>

<h2 id="gbp-photos">Step 2: Photo velocity and proof assets</h2>
<p>Upload fifty or more professional photos in the first thirty days. Include exterior, interior, team, equipment, fleet, certifications, and before-after project shots. Geo-tag and caption with city plus service naturally.</p>
<p>Texas buyers trust what they see. A machine shop without floor photos loses to a competitor with a polished gallery. Video tours increase engagement. Update photos monthly during active campaigns.</p>

<h2 id="gbp-reviews">Step 3: Review acceleration systems</h2>
<p>Reviews are among the strongest prominence signals. Aim for two to four new reviews per week with detailed context. Implement automated SMS or email requests after project milestones. Train field teams to ask at closeout.</p>
<p>Respond to every review within forty-eight hours. Thank positive reviewers and address concerns professionally on negative feedback. Responses reinforce keywords and show active management.</p>
<table>
<thead><tr><th>Review element</th><th>Why it matters in Texas B2B</th></tr></thead>
<tbody>
<tr><td>Keyword-rich detail</td><td>Matches commercial search semantics</td></tr>
<tr><td>City mention</td><td>Strengthens local relevance per metro</td></tr>
<tr><td>Project type</td><td>Converts searchers with similar needs</td></tr>
<tr><td>Recency</td><td>Signals active trustworthy operations</td></tr>
</tbody>
</table>

<h2 id="gbp-posts">Step 4: Weekly Google Posts</h2>
<p>Publish at least one Google Post per week. Rotate project spotlights, seasonal tips, hiring, certifications, and offers with tracked links. Posts reinforce freshness and give Google content to associate with your entity.</p>
<p>Align post themes with Texas seasonality: storm preparedness, summer HVAC load, year-end budget spend, spring construction ramp. Generic national post calendars underperform.</p>

<h2 id="gbp-citations">Step 5: Citation and NAP consistency</h2>
<p>Your name, address, and phone must match exactly across Google, Apple Maps, Bing, Yelp, BBB, industry directories, and chamber listings. Suite number variations, old addresses, and call tracking number swaps without proper configuration suppress rankings.</p>
<p>Build seventy or more consistent citations. Audit quarterly because data aggregators drift over time. NAP inconsistency is one of the most common reasons strong Texas businesses fail to rank.</p>

<h2 id="gbp-website">Step 6: Website alignment and local landing pages</h2>
<p>Your website must corroborate your GMB entity. Link from site to profile and profile to site. Build location pages for each Texas market served with unique proof points, not copy-paste doorway pages.</p>
<p>Embed maps, local phone numbers, and schema markup. Google cross-validates profile and site data. Conflicts reduce trust.</p>

<h2 id="gbp-ai">Step 7: Prepare for AI Overview visibility</h2>
<p>Generative search pulls from entities with corroborating signals. FAQ schema, case studies, founder expertise, and consistent citations help your profile influence AI answers. GMB optimization in 2026 includes AI readiness, not only Map Pack clicks.</p>

<h2 id="gbp-mistakes">Common Texas GMB ranking mistakes</h2>
<ul>
<li>Duplicate listings splitting reviews</li>
<li>Service area so wide relevance collapses</li>
<li>Consumer categories on commercial businesses</li>
<li>No call tracking so performance is invisible</li>
<li>Stock photos instead of real operations</li>
<li>Ignoring Q and A while competitors seed answers</li>
</ul>

<h2 id="gbp-timeline">Realistic ranking timeline</h2>
<p>Expect first movement in thirty to sixty days for competitive metros with full execution. Top-three dominance on priority keywords often arrives between sixty and ninety days. Heavily suppressed or suspended profiles may require additional cleanup time before velocity begins.</p>

<div class="highlight-box">
<strong>TSBR client benchmark:</strong> Average first Map Pack movement twenty-eight to sixty-seven days. Precision Machine Works achieved seventeen number-one rankings in seventy-four days.
</div>

<h2 id="gbp-competitive">Competitive analysis framework for Texas Map Packs</h2>
<p>Before changing your profile, document who ranks today and why. Export the top fifteen commercial keywords your sales team cares about. Search each from a device geolocated in your target city. Screenshot Map Pack results weekly. Record competitor review counts, photo totals, post frequency, primary categories, and obvious service gaps.</p>
<p>In DFW industrial corridors, the number-one listing often has triple the reviews and double the photos of position four. In Houston contracting, AI Overview citations overlap with Map Pack leaders, meaning entity strength off-profile accelerates Maps wins. Competitive analysis prevents wasted effort on low-impact tweaks.</p>
<p>TSBR delivers competitor teardowns in every free audit. You see exactly how far behind you are on each signal and which gaps close fastest for your vertical.</p>

<h2 id="gbp-multi">Multi-location ranking without duplicate violations</h2>
<p>Texas B2B firms with multiple branches face unique challenges. Each location needs a legitimate address or clear service-area rules per Google guidelines. Duplicate listings created by well-meaning staff must be merged. Shared call centers need consistent primary numbers on core citations.</p>
<p>Roll out optimization location by location starting with highest-revenue markets. Attempting fifty cities simultaneously dilutes execution. Sequence Irving before expanding to Plano, or Houston before Katy, based on pipeline priority.</p>

<h2 id="gbp-tracking">Tracking calls and proving ROI to leadership</h2>
<p>Implement dynamic number insertion or dedicated tracking lines on website and GMB where policy allows. Tag landing page URLs with UTM parameters in posts. Align CRM lead source fields with Maps, organic, and AI Overview so finance sees local SEO as revenue infrastructure, not marketing fluff.</p>
<p>Texas owners approve continued investment when quote requests tie to Google. Without attribution, even strong ranking gains get cut in budget reviews.</p>

<h2 id="gbp-seasonal">Seasonal optimization calendar for Texas</h2>
<ul>
<li>Q1: budget-cycle capital equipment and facility upgrade posts</li>
<li>Q2: pre-summer HVAC and mechanical readiness in Houston and DFW</li>
<li>Q3: hurricane and storm response visibility on Gulf Coast profiles</li>
<li>Q4: year-end project capacity and maintenance contract pushes</li>
</ul>
<p>Seasonal posts match buyer urgency and boost engagement metrics during peak decision windows.</p>

<h2 id="gbp-suspension">Recovery from suspension or suppression</h2>
<p>Suspended profiles require policy review, not panic reinstatement requests. Identify address verification issues, keyword-stuffed names, or guideline violations on service areas. Merge duplicates before appealing. Rebuild trust with conservative posting and authentic review velocity after reinstatement.</p>
<p>Suppressed listings may still appear to owners while hidden from public. Audit from incognito logged-out sessions in target cities to see true public status.</p>

<h2 id="gbp-checklist">Pre-launch GMB ranking checklist</h2>
<ol>
<li>Single authoritative listing confirmed</li>
<li>Categories validated against top ten buyer keywords</li>
<li>Fifty plus photos uploaded with captions</li>
<li>All services entered with descriptions</li>
<li>Review request workflow documented</li>
<li>Four weeks of posts scheduled</li>
<li>Seventy citations audited for NAP match</li>
<li>Website location pages live and linked</li>
<li>Call tracking tested end to end</li>
<li>Q and A seeded for top five buyer objections</li>
</ol>

<h2 id="gbp-next">Next steps</h2>
<p>Run a competitive GMB audit against the top three Map Pack listings in your Texas market. Score completeness, reviews, photos, posts, and citations. Gap size determines timeline. TSBR offers this audit free with a written ninety-day plan. Contact Mike Kaswatuka in Arlington to begin.</p>
        """,
    },
    {
        "slug": "optimizing-for-ai-overviews-texas-businesses.html",
        "title": "Optimizing for AI Overviews: Texas B2B Guide",
        "tag": "AI",
        "desc": "Practical steps to get cited when Texas buyers ask AI for local vendor recommendations.",
        "read_time": "12 min",
        "published": "2026-02-05",
        "toc": [
            ("aio-intro", "AI Overviews and B2B discovery"),
            ("aio-entity", "Build entity authority"),
            ("aio-structure", "Structured content"),
            ("aio-depth", "Topical depth"),
            ("aio-eeat", "E-E-A-T signals"),
            ("aio-gmb", "GMB as AI input"),
            ("aio-monitor", "Monitor and iterate"),
            ("aio-audit", "Free audit"),
        ],
        "body_html": """
<h2 id="aio-intro">AI Overviews changed how Texas B2B buyers discover vendors</h2>
<p>Google AI Overviews and other generative search interfaces answer vendor questions before users click traditional results. A procurement manager might ask Which industrial suppliers serve San Antonio manufacturing plants? and receive a synthesized answer citing three businesses by name. If you are not cited, you are not on the shortlist.</p>
<p>TSBR helps Texas B2B companies optimize for AI Overviews through entity authority, structured content, schema markup, citation corroboration, and E-E-A-T signals. This guide explains practical steps Mike Kaswatuka deploys for clients in Houston, Austin, DFW, and statewide markets.</p>
<p>AI optimization is not separate from local SEO. It layers on top of Google Business Profile excellence, citation consistency, and authoritative website content. Weak traditional signals rarely appear in generative answers.</p>

<h2 id="aio-entity">Build a clear, consistent entity</h2>
<p>AI models trust businesses they can identify unambiguously. Your legal name, address, phone, website, categories, and descriptions must match across GMB, website footer, LinkedIn, industry directories, and press mentions. Entity confusion causes models to omit or misrepresent your brand.</p>
<p>Create a founder and company narrative that highlights Texas experience, certifications, client outcomes, and service geography. Generative systems favor sources with demonstrable expertise.</p>

<h2 id="aio-structure">Structured content AI can parse</h2>
<p>Use clear heading hierarchies, direct answer paragraphs at the top of sections, FAQ blocks, bullet lists, and tables. Implement FAQ schema, Service schema, and LocalBusiness schema where appropriate.</p>
<p>Answer-first formatting matters. Lead with a concise response to the buyer question, then expand with detail. AI Overviews extract concise passages; burying answers reduces citation probability.</p>

<h2 id="aio-depth">Topical depth for Texas niches</h2>
<p>Publish in-depth content about services, industries, and cities you serve. A civil engineering firm should own content on Austin transportation permitting, Williamson County site development, and Texas DOT compliance topics relevant to buyers.</p>
<p>Thin generic pages fail. Depth includes case studies, process explanations, timelines, pricing factors, and comparison guidance that demonstrates real experience.</p>

<h2 id="aio-eeat">E-E-A-T signals for B2B trust</h2>
<p>Experience, expertise, authoritativeness, and trustworthiness determine whether AI cites you over a aggregator or national directory.</p>
<ul>
<li>Named founder bio with credentials and Texas tenure</li>
<li>Client case studies with measurable outcomes</li>
<li>Industry certifications and association memberships</li>
<li>Review corpus with specific project detail</li>
<li>Consistent NAP across authoritative citations</li>
</ul>

<h2 id="aio-gmb">Google Business Profile as AI input</h2>
<p>Your profile feeds Google's knowledge graph. Complete services, active posts, review sentiment, and Q and A content influence how AI represents your business. Profiles neglected for months rarely become cited sources.</p>

<h2 id="aio-monitor">Monitor and iterate</h2>
<p>Track queries where AI Overviews appear in your vertical. Note which competitors are cited and analyze their content structure, schema, and authority signals. Refresh content quarterly as models and query patterns evolve.</p>
<table>
<thead><tr><th>Signal type</th><th>AI impact</th><th>TSBR action</th></tr></thead>
<tbody>
<tr><td>Entity consistency</td><td>High</td><td>NAP audit, deduplication</td></tr>
<tr><td>FAQ schema</td><td>High</td><td>Buyer question mapping</td></tr>
<tr><td>Reviews</td><td>Medium-high</td><td>Velocity review systems</td></tr>
<tr><td>Local content depth</td><td>High</td><td>City and service silos</td></tr>
<tr><td>Backlinks</td><td>Medium</td><td>Industry and local links</td></tr>
</tbody>
</table>

<h2 id="aio-results">Texas client results</h2>
<p>Gulf Coast Commercial Construction achieved top-three AI Overview citations alongside four point three times lead growth. Lone Star Civil Engineering expanded AI visibility across Austin metro engineering queries. Results typically begin forty-five to seventy-five days after entity foundation work.</p>

<h2 id="aio-mistakes">Mistakes to avoid</h2>
<ol>
<li>Publishing AI-generated fluff without expert review</li>
<li>Contradictory service descriptions across web and GMB</li>
<li>Ignoring structured data implementation</li>
<li>No Texas-local proof on national-template pages</li>
<li>Expecting instant citations without citation corroboration</li>
</ol>

<div class="highlight-box">
<strong>Key takeaway:</strong> AI Overview optimization is entity engineering. Texas B2B companies with strong Maps presence, consistent citations, and deep local content become the sources generative search trusts.
</div>

<h2 id="aio-content-types">Content types that earn AI citations</h2>
<p>Not all pages are equal for generative extraction. Comparison guides, process explainers, regulatory summaries, pricing factor articles, and city-specific service FAQs outperform generic about pages. Publish content that answers questions procurement staff actually type into AI interfaces.</p>
<p>Include named experts. Articles attributed to Mike Kaswatuka or client engineering leads carry more weight than anonymous AI-generated blog spam. Google quality systems penalize low-effort mass content.</p>

<h2 id="aio-local-proof">Local proof modules for Texas pages</h2>
<p>Each page should reference specific Texas geography: counties, highways, industrial districts, and regional project types. Mention local codes, climate stressors, and supply chain realities. AI models use geographic specificity as a trust signal for local queries.</p>
<p>Embed client logos, project photos, and dated case metrics. Freshness matters when models choose between two similarly titled contractor pages.</p>

<h2 id="aio-technical">Technical implementation checklist</h2>
<ol>
<li>Validate schema with Google Rich Results Test</li>
<li>Ensure mobile page speed under three seconds on key landers</li>
<li>Fix canonical tags on duplicate parameter URLs</li>
<li>Publish XML sitemap with location and service URLs</li>
<li>Link sameAs social profiles in Organization schema</li>
<li>Remove conflicting old location pages from index</li>
</ol>

<h2 id="aio-competitive">Competitive AI citation analysis</h2>
<p>Monthly, query your top twenty buyer questions in Google and note AI Overview citations. Archive screenshots. When competitors appear and you do not, diff their page structure, word count, schema types, and backlink sources. Reverse-engineer patterns ethically by improving your entity signals, not copying text.</p>

<h2 id="aio-faq">FAQ engineering for B2B buyers</h2>
<p>Build FAQ sections from sales call transcripts. Questions about bonding capacity, EMR safety ratings, Texas licensing, lead times, and emergency response windows belong on site and in schema. These mirror how AI models formulate answers to complex vendor queries.</p>

<h2 id="aio-roadmap">Six-month AI optimization roadmap</h2>
<table>
<thead><tr><th>Month</th><th>Focus</th></tr></thead>
<tbody>
<tr><td>1</td><td>Entity audit, NAP, schema baseline</td></tr>
<tr><td>2</td><td>FAQ and service page rewrites</td></tr>
<tr><td>3</td><td>Location depth expansion</td></tr>
<tr><td>4</td><td>Citation corroboration push</td></tr>
<tr><td>5</td><td>Case study and review alignment</td></tr>
<tr><td>6</td><td>AI citation measurement and refresh</td></tr>
</tbody>
</table>

<h2 id="aio-voice">Brand voice and corroboration across the web</h2>
<p>AI models compare how your business is described on your website, Google profile, LinkedIn, press releases, and industry directories. Descriptions that conflict reduce confidence scores. Standardize elevator pitch paragraphs and service definitions, then propagate intentionally to each platform with appropriate formatting.</p>
<p>Seek third-party mentions: chamber features, supplier awards, project announcements, and partner case studies. External corroboration is prominence for generative systems. Texas regional publications and trade associations carry weight for local entity trust.</p>

<h2 id="aio-houston-austin">Metro-specific AI examples</h2>
<p>Houston energy corridor procurement teams ask AI about contractor safety records and hurricane response capacity. Austin tech facilities teams ask about LEED experience and fast response SLAs. DFW industrial buyers ask about fleet size and CNC tolerances. Tailor FAQ and case content to these distinct question patterns rather than one statewide FAQ blob.</p>

<h2 id="aio-longform">Long-form authority pieces</h2>
<p>Publish annual Texas market outlook articles for your vertical with dated statistics and named author credentials. Long-form pieces attract links and serve as citation sources for nuanced AI answers that short pages cannot support.</p>

<h2 id="aio-chatgpt">Beyond Google: ChatGPT and Perplexity visibility</h2>
<p>Texas procurement professionals use ChatGPT, Perplexity, and Copilot for vendor research. These systems rely on training data and live retrieval from authoritative web sources. Strong open-web presence, Wikipedia-notable achievements you legitimately earn, and consistent directory listings increase retrieval odds. Publish factual, citable statistics about your Texas operations that models can reference without hallucinating.</p>
<p>Maintain a press page with dated milestones: expansions, certifications, major project awards. Each milestone is a future citation anchor. Avoid exaggerated claims that models cannot corroborate elsewhere.</p>

<h2 id="aio-summary">Summary</h2>
<p>AI Overview optimization for Texas B2B is entity engineering across GMB, website, citations, and proof-rich content. Start with NAP consistency, add schema and FAQ depth, then measure citations monthly. TSBR clients see measurable AI visibility within forty-five to seventy-five days when foundations are executed completely.</p>

<h2 id="aio-audit">Free AI visibility audit</h2>
<p>TSBR includes AI Overview assessment in every free local search audit. We map citation gaps, schema opportunities, and content upgrades prioritized for your Texas markets. Request yours from Arlington headquarters today.</p>
        """,
    },
    {
        "slug": "b2b-local-seo-strategies-texas.html",
        "title": "B2B Local SEO Strategies for Texas",
        "tag": "B2B",
        "desc": "How industrial, contracting, and professional firms win high-value Texas buyers through search.",
        "read_time": "12 min",
        "published": "2026-02-19",
        "toc": [
            ("b2b-intro", "B2B vs B2C local SEO"),
            ("b2b-keywords", "Commercial keywords"),
            ("b2b-multi", "Multi-location strategy"),
            ("b2b-quality", "Lead quality focus"),
            ("b2b-integrate", "GMB and website integration"),
            ("b2b-metrics", "Metrics that matter"),
            ("b2b-start", "Get started"),
        ],
        "body_html": """
<h2 id="b2b-intro">B2B local SEO is not B2C local SEO with a different logo</h2>
<p>Texas industrial, contracting, and professional services firms lose leads when agencies apply consumer playbooks. Restaurant tactics do not rank machine shops in Irving or commercial contractors in Houston. B2B buyers use different keywords, longer consideration cycles, and higher scrutiny before first contact.</p>
<p>This guide outlines TSBR strategies for winning high-value Texas buyers through local search, Google Business Profile dominance, and AI-ready content architecture.</p>

<h2 id="b2b-keywords">Target commercial keyword intent</h2>
<p>Map keywords to buying stages. Prioritize terms with quote intent: commercial HVAC contractor Katy, industrial pump supplier San Antonio, civil engineering firm Round Rock. Deprioritize purely informational queries that attract students and DIY researchers.</p>
<p>Use sales team interviews to capture language from RFQs and discovery calls. That language becomes service descriptions, GMB posts, and page titles.</p>

<h2 id="b2b-multi">Multi-location Texas strategy</h2>
<p>Companies serving DFW and Houston need market-specific pages, citations, and GMB service areas. One generic Texas page cannot rank everywhere. Build substantive location content with local projects, phone numbers, and team presence.</p>
<p>Prevent cannibalization by assigning keyword clusters per branch and using proper primary listing hierarchy for multi-location brands.</p>

<h2 id="b2b-quality">Lead quality over traffic volume</h2>
<p>Ten thousand monthly sessions mean nothing if only twelve are quote requests. Measure calls, forms, RFQs, and CRM-opportunity creation. Optimize profiles and pages to filter consumer intent with clear commercial language and B2B proof.</p>

<h2 id="b2b-integrate">Integrate GMB and website storytelling</h2>
<p>Your profile and site must tell the same story: services, cities, certifications, and project proof. Cross-link services to location pages. Showcase case studies that mirror review themes on Google.</p>

<h2 id="b2b-citations">Citations and NAP for B2B entities</h2>
<p>Industry directories matter for B2B: Thomasnet, industry associations, BBB, regional chambers. Consistent NAP across seventy plus sources corroborates your entity for Maps and AI.</p>

<h2 id="b2b-content">Content silos that close deals</h2>
<p>Build silos for services, industries, locations, and resources. Internal linking distributes authority. Answer buyer objections: timelines, bonding, insurance, fleet size, emergency response, geographic limits.</p>
<table>
<thead><tr><th>B2B vertical</th><th>High-intent Texas keyword pattern</th></tr></thead>
<tbody>
<tr><td>Industrial equipment</td><td>commercial [equipment] repair [city]</td></tr>
<tr><td>Contracting</td><td>commercial [trade] contractor [metro]</td></tr>
<tr><td>Engineering</td><td>[discipline] engineering firm [city]</td></tr>
<tr><td>Distribution</td><td>industrial supplier near [city]</td></tr>
</tbody>
</table>

<h2 id="b2b-ai">Prepare for AI-mediated shortlists</h2>
<p>Procurement teams increasingly use generative tools. Entity strength and FAQ-rich content ensure you appear in AI-generated vendor lists alongside Map Pack visibility.</p>

<h2 id="b2b-metrics">Metrics that matter</h2>
<ul>
<li>Map Pack share of voice for commercial keywords</li>
<li>Qualified leads per month by source</li>
<li>Review velocity and sentiment</li>
<li>Location page conversion rate</li>
<li>Pipeline attributed to organic local search</li>
</ul>

<h2 id="b2b-cases">Texas proof points</h2>
<p>Precision Machine Works increased quote requests six hundred twenty percent. Alamo Industrial Supply achieved three point two times RFQs. Patterns repeat when B2B intent, not consumer vanity metrics, drive strategy.</p>

<div class="highlight-box">
<strong>Founder insight:</strong> Mike Kaswatuka works directly with Texas B2B clients to align search strategy with sales reality. If your CRM says leads are weak, we fix targeting before chasing more traffic.
</div>

<h2 id="b2b-sales">Align SEO with your sales process</h2>
<p>Interview estimators and inside sales reps quarterly. Capture phrases from won and lost deals. Lost deals due to discoverability problems indicate keyword gaps. Won deals from Google reveal terms to double down on in GMB services and location pages.</p>
<p>Configure CRM required fields for lead source and first-touch URL. Texas B2B pipelines move slowly; multi-touch attribution still starts with how buyers found you initially.</p>

<h2 id="b2b-vertical">Vertical-specific tactics</h2>
<p>Industrial equipment firms need equipment photos and spec-sheet downloads. Contractors need project galleries and bonding proof. Engineering firms need credentials, PE licenses, and municipal experience lists. Distributors need inventory and fulfillment FAQs. Customize proof modules per vertical instead of generic trust badges.</p>

<h2 id="b2b-fort-worth-dallas">DFW versus Houston versus Austin nuances</h2>
<p>DFW buyers split industrial west versus corporate north. Houston buyers weight storm readiness and energy corridor experience. Austin buyers scrutinize digital polish and technical depth. One statewide keyword list fails. Build metro-specific clusters and review themes.</p>

<h2 id="b2b-reporting">Reporting cadence for leadership</h2>
<ul>
<li>Weekly ranking snapshot during launch quarter</li>
<li>Monthly qualified lead report by source</li>
<li>Quarterly pipeline attribution review with finance</li>
<li>Annual competitive share-of-voice benchmark</li>
</ul>

<h2 id="b2b-roadmap">Twelve-month B2B local SEO roadmap</h2>
<ol>
<li>Months 1-3: GMB Velocity and citation foundation</li>
<li>Months 4-6: Location and service content expansion</li>
<li>Months 7-9: AI schema and FAQ engineering</li>
<li>Months 10-12: Multi-market defense and new city rollout</li>
</ol>

<h2 id="b2b-contract">Contract and project-based keyword clusters</h2>
<p>Group keywords by contract type: TI buildouts, plant shutdowns, municipal infrastructure, OEM maintenance. Each cluster gets a landing path from GMB service to website case study to contact CTA. Buyers searching shutdown maintenance Texas should land on proof-heavy pages, not a generic home page.</p>

<h2 id="b2b-reviews">Review strategy for long sales cycles</h2>
<p>B2B reviews often arrive months after project completion. Build CRM triggers at substantial completion, not invoice only. Ask project managers to request reviews when client satisfaction peaks. Accumulate steady velocity instead of sporadic bursts that look manipulated.</p>

<h2 id="b2b-tech">Technical SEO foundations for industrial sites</h2>
<p>Many Texas B2B sites run legacy CMS platforms with slow mobile performance. Fix Core Web Vitals on service pages before scaling content. Ensure HTTPS, clean canonicals, and structured breadcrumbs. Technical debt blocks rankings even with perfect GMB.</p>

<h2 id="b2b-partners">Partner and supplier ecosystem links</h2>
<p>Earn links from manufacturers you represent, general contractors you subcontract for, and industry associations. Local relevance plus industry authority strengthens both Maps and organic B2B rankings.</p>

<h2 id="b2b-inhouse">In-house versus agency execution</h2>
<p>Some Texas B2B firms hire internal marketing coordinators who lack local SEO depth. TSBR partners with internal teams: we supply strategy, audits, and specialist execution while your coordinator handles industry relationships and project photos. Hybrid models reduce cost and improve authenticity of content.</p>
<p>Founder access to Mike Kaswatuka prevents strategy drift that happens when agencies hand off to juniors. Your market is too competitive for inexperienced account management.</p>

<h2 id="b2b-defend">Defending Map Pack positions year two</h2>
<p>Year one wins attract competitor response. Year two requires review maintenance, post consistency, citation monitoring, and expansion into adjacent keywords. Budget for defense, not only initial conquest. Clients who stop at month six lose positions to hungrier competitors.</p>

<h2 id="b2b-budget">Budgeting B2B local SEO in Texas metros</h2>
<p>Competitive metros require sustained investment across GMB management, citations, content, and technical fixes. Underfunding one layer creates bottlenecks. A San Antonio supplier may move faster with smaller monthly spend than a Houston contractor facing fifty established Map Pack competitors. Benchmark against gap size from your audit, not national averages.</p>
<p>Finance teams should compare cost per qualified lead from local search against bid networks and trade shows. TSBR clients frequently report lower acquisition cost once Map Pack dominance stabilizes in month four through six.</p>

<h2 id="b2b-onboarding">Client onboarding data we request</h2>
<p>License numbers, insurance certificates, service area list by city, top twenty revenue services, active project photos, CRM export of lead sources, and access to GMB and analytics. Complete onboarding accelerates Velocity launch within two weeks of contract signature.</p>

<h2 id="b2b-summary">Closing perspective</h2>
<p>B2B local SEO in Texas rewards specialization. Generic agencies chase traffic. TSBR chases qualified commercial visibility in Maps, organic, and AI surfaces. The playbook is repeatable: audit, fix NAP, launch Velocity, expand content, measure pipeline. Execute with discipline and Texas market nuance.</p>

<h2 id="b2b-contact">Work with Mike Kaswatuka</h2>
<p>Founder-led strategy is the TSBR difference. Call (682) 206-4178 or email hello@tsbrenterprises.com for a B2B local SEO audit scoped to your Texas metros, industries, and revenue goals.</p>

<h2 id="b2b-start">Implement B2B local SEO with TSBR</h2>
<p>Request a free audit covering GMB, citations, competitor Map Packs, and AI visibility. Receive a ninety-day B2B action plan tailored to your Texas markets.</p>
        """,
    },
    {
        "slug": "citation-building-nap-consistency-texas.html",
        "title": "NAP Consistency and Citation Building for Texas",
        "tag": "Technical",
        "desc": "Why consistent name, address, and phone data remains a top local ranking factor for Texas B2B.",
        "read_time": "11 min",
        "published": "2026-03-04",
        "toc": [
            ("nap-intro", "NAP and rankings"),
            ("nap-what", "Multi-location NAP"),
            ("nap-priority", "Priority directories"),
            ("nap-build", "Building citations"),
            ("nap-mistakes", "Common mistakes"),
            ("nap-ai", "NAP and AI trust"),
            ("nap-audit", "Free audit"),
        ],
        "body_html": """
<h2 id="nap-intro">NAP consistency remains a cornerstone of Texas local rankings</h2>
<p>Name, Address, and Phone data tell search engines and AI models which business entity to trust. When your GMB listing says Suite 200 but Yelp shows Suite B, prominence suffers. Texas B2B companies with strong operations but messy citations routinely lose Map Pack positions to cleaner competitors.</p>
<p>TSBR treats citation building and NAP consistency as foundational engineering, not a legacy checkbox. This technical guide explains how we fix drift, build seventy plus authoritative listings, and monitor ongoing accuracy for clients statewide.</p>

<h2 id="nap-what">What NAP means for multi-location Texas firms</h2>
<p>NAP is your canonical business identity string. For multi-branch contractors, each location needs its own consistent NAP everywhere it appears. Headquarters NAP must not leak into branch listings or vice versa.</p>
<p>Phone strategy matters. Call tracking numbers work when implemented with proper primary number consistency on core citations. Random tracking swaps on major directories confuse aggregators.</p>

<h2 id="nap-priority">Priority directories for Texas B2B</h2>
<ol>
<li>Google Business Profile</li>
<li>Apple Business Connect</li>
<li>Bing Places</li>
<li>Yelp for Business</li>
<li>Better Business Bureau</li>
<li>Facebook business page</li>
<li>LinkedIn company page</li>
<li>Industry-specific directories</li>
<li>Regional chambers and economic development sites</li>
<li>Data aggregators: Foursquare, Data Axle, Localeze</li>
</ol>

<h2 id="nap-build">Citation building process</h2>
<p>We start with an audit of existing citations, classify duplicates and errors, establish a single canonical NAP, then build or correct listings in priority order. Aggregator corrections cascade to downstream sites over four to twelve weeks.</p>
<p>Manual submission beats pure automation for high-value B2B directories where category selection and description quality matter.</p>

<h2 id="nap-mistakes">Common NAP mistakes in Texas</h2>
<ul>
<li>Street versus St versus full street name inconsistency</li>
<li>Old locations still live on legacy directories</li>
<li>Multiple phone numbers without hierarchy</li>
<li>DBA versus legal name mismatch unlinked</li>
<li>Geo pages using different addresses than GMB</li>
<li>Franchise location pages sharing one phone incorrectly</li>
</ul>

<h2 id="nap-ai">NAP and AI Overview trust</h2>
<p>Generative models cross-check business facts across sources. Widespread inconsistency reduces likelihood of citation in AI answers. Clean NAP is AI entity hygiene.</p>

<table>
<thead><tr><th>Issue</th><th>Ranking impact</th><th>Fix timeline</th></tr></thead>
<tbody>
<tr><td>Duplicate GMB</td><td>Severe</td><td>1-3 weeks</td></tr>
<tr><td>Aggregator error</td><td>High</td><td>4-12 weeks cascade</td></tr>
<tr><td>Minor suite typo</td><td>Medium</td><td>1-4 weeks</td></tr>
<tr><td>Old address remnant</td><td>High</td><td>2-8 weeks</td></tr>
</tbody>
</table>

<h2 id="nap-monitor">Ongoing monitoring</h2>
<p>Citations drift when data aggregators merge incorrect third-party data. Quarterly audits catch problems before rankings drop. TSBR includes monitoring in ongoing management engagements.</p>

<h2 id="nap-case">Why citations blocked a San Antonio supplier</h2>
<p>Alamo Industrial Supply struggled despite inventory strength. Three conflicting addresses across directories suppressed their primary listing. After NAP remediation and seventy-five citation builds, they reached eight number-one Map Pack rankings and three point two times quote requests in ninety days.</p>

<div class="highlight-box">
<strong>Rule:</strong> Never launch photo and review velocity on top of dirty NAP. Fix identity first, then compound prominence.
</div>

<h2 id="nap-aggregators">How data aggregators affect Texas listings</h2>
<p>Aggregators distribute your NAP to dozens of downstream sites. Fixing Foursquare or Data Axle often corrects multiple errant listings weeks later. Patience is required. Launching review velocity before aggregator corrections complete can compound confusion.</p>
<p>We submit canonical data through authorized feeds where available and manually correct high-priority industry directories simultaneous to aggregator updates.</p>

<h2 id="nap-industry">Industry directory priorities by vertical</h2>
<p>Manufacturing suppliers target Thomasnet and regional industrial guides. Contractors prioritize Blue Book, Dodge, and construction associations. Engineering firms list with ACEC chapters and municipal prequalification databases where public. Match directory strategy to where your buyers verify credentials.</p>

<h2 id="nap-multilocation">Multi-location citation governance</h2>
<p>Create a master spreadsheet: location ID, legal name, display name, address, suite, phone, GMB URL, primary category. No branch marketing employee submits listings without template approval. Governance prevents ninety percent of future NAP drift.</p>

<h2 id="nap-tools">Audit tools and manual verification</h2>
<p>Automated tools surface candidates but humans verify in Texas-specific contexts. Call tracking numbers, virtual offices, and co-working addresses trigger spam filters if misconfigured. We validate from incognito search sessions in target cities, not only desktop SEO tools.</p>

<h2 id="nap-timeline">Citation project timeline expectations</h2>
<ol>
<li>Week 1-2: audit and canonical NAP decision</li>
<li>Week 3-6: priority directory corrections</li>
<li>Week 7-12: aggregator cascade and long-tail builds</li>
<li>Ongoing: quarterly reverification</li>
</ol>

<h2 id="nap-format">Formatting rules that prevent silent errors</h2>
<p>Choose one format and document it: 518 Brynmawr Ct versus 518 Brynmawr Court. (682) 206-4178 versus 682-206-4178. Legal name versus DBA display rules. Train every employee who touches listings. Business cards and truck wraps must match canonical NAP to avoid staff accidentally creating new inconsistent listings.</p>

<h2 id="nap-franchise">Franchise and dealer network citations</h2>
<p>Dealer networks need corporate plus local NAP rules. Corporate site lists authorized dealers with consistent URL patterns. Each dealer maintains local GMB with unique phone when required. Corporate marketing must not mass-produce identical city pages with swapped city names.</p>

<h2 id="nap-reviews">Reviews and citations interaction</h2>
<p>Review sites like Yelp and BBB create listings automatically. Claim and align them early or they generate alternate addresses from user suggestions. Monitor Google Q and A for address misinformation submitted by public.</p>

<h2 id="nap-service-area">Service-area businesses without storefronts</h2>
<p>Many Texas B2B firms visit customer sites without public walk-in locations. Google allows service-area configuration with hidden addresses when guidelines are met. Citations still need a consistent physical address for mail and licensing, often home office or HQ. Misrepresenting virtual offices as retail locations risks suspension.</p>
<p>Document service polygons honestly. Over-wide service areas dilute relevance in Maps ranking math.</p>

<h2 id="nap-case-dfw">DFW duplicate listing case pattern</h2>
<p>A common DFW pattern: mergers leave two listings with slightly different suite numbers splitting forty reviews across both. Neither listing ranks. Merge per Google procedure, forward phones, update citations in batch, then restart review velocity on the surviving profile. Rankings often jump within thirty days post-merge when other signals are strong.</p>

<h2 id="nap-checklist">Citation quality checklist</h2>
<ol>
<li>Exact canonical business name</li>
<li>Standardized address format</li>
<li>Primary phone matches GMB</li>
<li>Correct primary category on industry sites</li>
<li>Unique description per directory where allowed</li>
<li>Link to correct location URL</li>
<li>Logo and photos on major platforms</li>
</ol>

<h2 id="nap-summary">Why citations still matter in 2026</h2>
<p>Algorithms evolve but entity corroboration remains essential. Google and AI systems cross-check facts. Citations are facts distributed across the web. Texas B2B companies that treat NAP as permanent infrastructure outperform competitors who chase trends while their listings fracture. Fix identity, then compound prominence.</p>
<p>TSBR citation building is included in local SEO and GMB engagements because we refuse to build on cracked foundations.</p>

<h2 id="nap-houston">Houston sprawl and citation complexity</h2>
<p>Houston multi-location contractors often accumulate listings from old yard addresses, project trailers, and acquired companies. Consolidation projects take eight to twelve weeks but unlock Map Pack potential across Katy, Sugar Land, and inner loop simultaneously when executed with proper redirect and citation sequencing.</p>

<h2 id="nap-austin">Austin tech corridor listing hygiene</h2>
<p>Austin B2B firms rebrand frequently. Old startup names linger on Crunchbase, Yelp, and Apple Maps. Rebrand playbooks must include citation updates within fourteen days of public announcement or Google confuses entities and AI cites outdated names. TSBR manages rebrand citation sprints for Central Texas clients.</p>
<p>Document every change in a public change log on your website press page so humans and parsers recognize continuity of operations despite name or suite updates.</p>

<h2 id="nap-final">Final note on patience</h2>
<p>Citation corrections are not instantaneous. Plan ninety days for full propagation. Rankings may jump in week four or week ten depending on aggregator cycles. Consistency during the wait period matters more than frantic new submissions. Stay the course and measure monthly, not daily, until citations fully propagate.</p>

<h2 id="nap-audit">Free citation and NAP audit</h2>
<p>TSBR scans fifty plus sources in our standard free audit and prioritizes fixes. Contact hello@tsbrenterprises.com or call (682) 206-4178 from Arlington, Texas headquarters.</p>
        """,
    },
    {
        "slug": "ai-first-content-architecture-texas.html",
        "title": "AI-First Content Architecture for Texas Businesses",
        "tag": "AI",
        "desc": "Structure website content so Google and AI models understand and recommend your Texas B2B business.",
        "read_time": "11 min",
        "published": "2026-03-18",
        "toc": [
            ("aifa-intro", "AI-first architecture"),
            ("aifa-clusters", "Topic clusters"),
            ("aifa-answer", "Answer-first structure"),
            ("aifa-schema", "Schema stack"),
            ("aifa-gmb", "GMB sync"),
            ("aifa-audit", "Architecture audit"),
        ],
        "body_html": """
<h2 id="aifa-intro">AI-first content architecture prepares Texas businesses for every search surface</h2>
<p>Buyers no longer follow a linear path from Google query to blue link click. They encounter Map Pack results, AI Overviews, People Also Ask boxes, and generative assistants sometimes in one session. Your content architecture must serve all parsers: classic crawlers, local algorithms, and large language models.</p>
<p>TSBR builds AI-first content systems for Texas B2B clients: topic clusters, answer-first formatting, schema layers, and local proof woven into every silo. Mike Kaswatuka applies this architecture so companies become citable authorities, not thin brochure sites.</p>

<h2 id="aifa-clusters">Topic clusters and silos</h2>
<p>Organize content into four silos: services, locations, industries, and resources. Each service page links to relevant Texas city pages and industry use cases. Hub pages distribute authority to spokes.</p>
<p>Example: commercial HVAC service hub links to Katy location page, Houston energy corridor case study, and FAQ on emergency response SLAs.</p>

<h2 id="aifa-answer">Answer-first page structure</h2>
<p>Every major page opens with a direct answer to the primary buyer question in two to three sentences. Follow with depth: process, proof, comparisons, timelines, and CTAs. AI Overviews extract the opening answer when confidence is high.</p>

<h2 id="aifa-local">Local context on every page</h2>
<p>Texas specificity is non-negotiable. Mention cities, counties, regional terminology, climate factors, and local regulations. Generic national copy fails local algorithms and AI trust checks.</p>

<h2 id="aifa-schema">Schema markup stack</h2>
<ul>
<li>LocalBusiness on contact and location pages</li>
<li>Service on commercial service pages</li>
<li>FAQ on question-heavy pages</li>
<li>Article on blog resources</li>
<li>Organization sitewide with sameAs social profiles</li>
</ul>

<h2 id="aifa-internal">Internal linking rules</h2>
<p>Link location pages to services actually offered in that metro. Link case studies to matching service and city pages. Use descriptive anchor text with natural city and service terms. Avoid orphan pages with no inbound internal links.</p>

<h2 id="aifa-eeat">E-E-A-T content modules</h2>
<p>Include founder insight blocks, client metrics, certification lists, and dated update stamps on regulatory content. Show experience Texas buyers expect before issuing large POs.</p>

<table>
<thead><tr><th>Page type</th><th>Required modules</th></tr></thead>
<tbody>
<tr><td>Service</td><td>Answer intro, process, proof, FAQ, CTA</td></tr>
<tr><td>Location</td><td>Local intro, areas served, local proof, map</td></tr>
<tr><td>Case study</td><td>Challenge, solution, metrics, quote</td></tr>
<tr><td>Blog resource</td><td>TOC, tables, highlight boxes, internal links</td></tr>
</tbody>
</table>

<h2 id="aifa-gmb">Sync with Google Business Profile</h2>
<p>Website claims must match GMB services and cities. Post themes on Google should correspond to fresh site content. Split messaging confuses entity resolution.</p>

<h2 id="aifa-maintain">Maintenance cadence</h2>
<p>Review top pages quarterly. Update statistics, refresh project photos, add new FAQs from sales calls, and expand schema when Google adds supported types. Stale architecture decays like stale GMB profiles.</p>

<h2 id="aifa-results">Outcomes for Texas clients</h2>
<p>Clients combining AI-first architecture with GMB Velocity see faster Map Pack movement and earlier AI citations. Gulf Coast Commercial Construction and Lone Star Civil Engineering used this paired approach for multipliers in leads and RFP invitations.</p>

<div class="highlight-box">
<strong>Architecture principle:</strong> One entity, one story, many locally specific pages — all structured for humans and machines.
</div>

<h2 id="aifa-templates">Page templates that scale across Texas markets</h2>
<p>Build reusable templates with mandatory modules: hero answer block, proof strip, service details, FAQ, CTA, and internal links. Customize city paragraphs and project examples per location. Templates accelerate rollout to new metros without thin duplicate content penalties.</p>

<h2 id="aifa-briefs">Content briefs from buyer questions</h2>
<p>Each brief starts with a buyer question, primary keyword, city modifiers, required proof points, schema type, and internal link targets. Writers and AI assistants follow briefs under human expert review. Brief-driven production keeps architecture coherent at scale.</p>

<h2 id="aifa-performance">Measuring architecture performance</h2>
<p>Track indexation rate of new URLs, internal link click paths in analytics, rankings per silo, and assisted conversions from blog resources to contact pages. Architecture succeeds when authority flows to money pages, not when blog traffic spikes alone.</p>

<h2 id="aifa-migration">Migrating legacy sites without losing equity</h2>
<p>Texas B2B sites often carry years of messy URLs. Map redirects carefully, consolidate thin pages into authoritative hubs, and update sitemaps. Launch citation and GMB alignment only after canonical structure stabilizes to avoid conflicting signals during migration.</p>

<h2 id="aifa-team">Roles for ongoing architecture maintenance</h2>
<ul>
<li>Strategist: silo map and keyword ownership</li>
<li>Technical SEO: schema, speed, indexation</li>
<li>Content lead: briefs and E-E-A-T review</li>
<li>Sales liaison: quarterly question intake</li>
</ul>

<h2 id="aifa-video">Video and media in content architecture</h2>
<p>Embed facility tours and project time-lapse videos on service and location pages. Transcribe videos with captions for accessibility and crawler parsing. Host on YouTube with optimized titles including Texas city and service terms, then schema-link from site.</p>

<h2 id="aifa-conversion">Conversion paths without hurting architecture</h2>
<p>Every silo terminates in clear CTAs: audit request, quote form, or phone call. Sticky headers on mobile for commercial buyers searching from job sites. Architecture serves revenue, not only rankings.</p>

<h2 id="aifa-examples">Example silo map for Texas contractor</h2>
<p>Hub: commercial contracting Texas. Spokes: Dallas TI, Houston energy corridor buildouts, Austin tenant improvements, Fort Worth industrial renovation. Each spoke links to three case studies and one FAQ cluster. Internal links flow upward to hub and sideways to related trades.</p>

<h2 id="aifa-governance">Content governance documentation</h2>
<p>Maintain a living content map spreadsheet: URL, primary keyword, silo, schema type, last updated, owner, and internal link count. Quarterly audits flag orphan pages, cannibalization, and stale statistics. Governance prevents architecture decay when sales launches new service lines or cities.</p>
<p>Version major page rewrites in change logs so AI systems and returning buyers see transparent update history on regulated or technical topics.</p>

<h2 id="aifa-workflow">Production workflow for Texas B2B teams</h2>
<p>Month one: architecture map and template approval. Month two: priority service and HQ city pages. Month three: secondary Texas metros. Month four: blog resources supporting each silo. Field teams upload project photos to shared folders weekly so content stays fresh without bottlenecking on marketing.</p>
<p>Legal reviews regulated claims before publish on engineering, medical B2B, and environmental pages. Compliance and SEO align when workflow is documented.</p>

<h2 id="aifa-future">Future-proofing architecture for search evolution</h2>
<p>New SERP features will emerge, but answer-first structured content with strong entities persists as the safest long-term bet. Invest in architecture that serves buyers and machines simultaneously. Texas B2B firms that own their narrative in search own more of their market margin.</p>
<p>Pair architecture with GMB Velocity and citation discipline for full-stack local dominance. TSBR implements all three layers for clients statewide from Arlington headquarters.</p>

<h2 id="aifa-precision">Precision Machine Works content lesson</h2>
<p>Irving industrial clients rank faster when service pages mention tolerances, materials, industries served, and North Texas logistics advantages. Specificity beats generic manufacturing copy. Architecture should force specificity modules into every template so writers cannot publish thin pages by accident.</p>

<h2 id="aifa-schema-deep">Schema deployment sequence</h2>
<p>Deploy Organization schema site-wide first, then LocalBusiness on location pages, Service on commercial offer pages, and FAQ on support content. Validate each template before bulk publish. Broken schema wastes dev time and erodes trust signals. TSBR coordinates with your web developer or implements via CMS templates directly.</p>
<p>Revalidate after major CMS upgrades. Texas B2B sites on WordPress, Webflow, and custom stacks all require post-update schema checks.</p>

<h2 id="aifa-final">Start with architecture, not blog spam</h2>
<p>Random blog posts without silo planning create orphan URLs. Architecture first, volume second. Texas B2B sites win with fewer stronger pages tied to revenue services and cities. Every URL should have a defined job in the buyer journey and a parent silo that passes authority downstream to quote pages.</p>

<h2 id="aifa-audit">Content architecture audit</h2>
<p>TSBR evaluates your sitemap, internal links, schema, and local depth in our free audit today at no obligation. Receive prioritized restructure recommendations for your Texas B2B site. Based in Arlington, serving statewide multi-metro accounts across DFW, Houston, Austin, San Antonio, and beyond.</p>
        """,
    },
]


AI_NEWS_ARTICLES = [
    {
        "title": "Google Expands AI Overviews for Commercial Local Queries in Texas Markets",
        "date": "June 12, 2026",
        "summary": "Generative summaries now appear more frequently for B2B service searches in DFW, Houston, and Austin, increasing the importance of entity-consistent GMB and website signals.",
        "body_html": """
<p>Google has expanded AI Overview coverage for commercial and industrial local queries across major Texas metros. TSBR monitoring shows increased generative answers for searches such as commercial contractor Houston, industrial supplier DFW, and civil engineering firm Austin.</p>
<p>For B2B companies, this shift means Map Pack visibility alone is no longer sufficient. Businesses cited in AI Overviews share traits: consistent NAP across seventy plus directories, robust FAQ content, active Google Business Profiles with weekly posts, and corroborating case studies on their websites.</p>
<p>Mike Kaswatuka advises Texas clients to audit entity signals immediately. Companies that delay AI optimization risk losing shortlist visibility to competitors with cleaner structured data.</p>
<p>TSBR is updating client content calendars to include answer-first FAQ blocks on priority service pages and expanding schema deployment across Texas location silos.</p>
""",
    },
    {
        "title": "Map Pack Algorithm Update Hits Houston Industrial Corridors",
        "date": "May 28, 2026",
        "summary": "Recent ranking volatility along the Ship Channel and Katy Freeway industrial zones correlates with review recency and photo freshness signals.",
        "body_html": """
<p>Houston industrial and contracting clients experienced Map Pack volatility in late May. TSBR analysis correlates movement with review recency and photo freshness more than citation volume changes.</p>
<p>Profiles without new reviews in sixty days lost positions to competitors publishing weekly Google Posts and project photos. Gulf Coast Commercial Construction clients following the GMB Velocity System maintained top-three positions through the update.</p>
<p>Recommendation for Houston B2B firms: accelerate authentic review requests after project milestones and upload geo-tagged facility images monthly. Stale profiles are vulnerable regardless of historical prominence.</p>
""",
    },
    {
        "title": "Apple Business Connect Gains Traction Among Texas Procurement Teams",
        "date": "May 14, 2026",
        "summary": "B2B buyers on Apple devices increasingly discover vendors through Apple Maps, making Business Connect optimization a priority alongside Google.",
        "body_html": """
<p>Apple Maps usage among Texas procurement and facilities teams continues rising, especially in Austin and North DFW corporate corridors. Apple Business Connect listings that mismatch Google NAP create entity confusion.</p>
<p>TSBR now includes Apple Business Connect verification in standard citation onboarding. Key fields: exact name, address, phone, hours, categories, and deep links to location pages.</p>
<p>Multi-location manufacturers should align each branch listing with canonical spreadsheet data before Q3 expansion campaigns.</p>
""",
    },
    {
        "title": "New Google Business Profile Insights Metrics Help B2B Attribution",
        "date": "April 30, 2026",
        "summary": "Updated GMB insights expose more call and direction request data, helping Texas companies tie Maps visibility to pipeline.",
        "body_html": """
<p>Google Business Profile insights now provide granular call, message, and direction request reporting by device and query theme. Texas B2B clients can better attribute commercial leads to Maps when combined with call tracking.</p>
<p>TSBR integrates insights exports into monthly client dashboards alongside CRM lead source data. Discrepancies often reveal missing UTM tags on profile website links or untracked mobile clicks.</p>
<p>Finance teams should treat improved attribution as justification for ongoing Velocity management, not only initial optimization projects.</p>
""",
    },
    {
        "title": "DFW Multi-Location Brands Face Duplicate Listing Crackdown",
        "date": "April 16, 2026",
        "summary": "Google aggressive duplicate suppression in Dallas-Fort Worth requires merger and citation cleanup for franchises and acquired branches.",
        "body_html": """
<p>Google intensified duplicate listing enforcement across DFW in April. Common triggers: acquired companies retaining old GMB listings, slight suite number variations, and call tracking numbers submitted as primary on citations.</p>
<p>TSBR merged fourteen duplicate sets for industrial clients in Irving and Grand Prairie without suspension when following documented merge procedures. Attempting to delete competitors or create fake listings remains high-risk.</p>
<p>Action item: run incognito Map searches for each brand variation and merge duplicates before launching review velocity campaigns.</p>
""",
    },
    {
        "title": "TSBR Publishes 2026 Texas B2B Local Search Benchmark Report",
        "date": "March 22, 2026",
        "summary": "Internal aggregate data shows average 4.3x qualified lead growth and seventy-four day median time to multi-keyword Map Pack dominance.",
        "body_html": """
<p>The Stone Builders Rejected released internal 2026 benchmarks from Texas B2B engagements. Median time to first top-three Map Pack cluster: seventy-four days. Average qualified lead increase: four point three times within ninety days of full implementation.</p>
<p>Fastest verticals: industrial equipment, commercial contracting, and manufacturing supply. Most competitive keywords: Houston general contractors and Dallas IT managed services.</p>
<p>AI Overview citations appeared for sixty-two percent of clients actively maintaining FAQ schema and citation consistency. Report reinforces TSBR focus on GMB Velocity plus entity engineering as paired systems.</p>
<p>Request the executive summary through hello@tsbrenterprises.com.</p>
""",
    },
]


ABOUT_TIMELINE = [
    ("2012", "Mike Kaswatuka begins specializing in local search for Arlington and DFW B2B companies."),
    ("2014", "The Stone Builders Rejected brand formalized with focus on overlooked industrial and trade firms."),
    ("2016", "Expanded service footprint to Houston and Austin metros with multi-location citation systems."),
    ("2018", "Launched systematic GMB Velocity frameworks after Map Pack competition intensified statewide."),
    ("2020", "Added remote statewide delivery for Texas B2B clients during accelerated digital shift."),
    ("2022", "Introduced structured content and schema programs as AI-generated search previews emerged."),
    ("2024", "Integrated AI Overview monitoring and entity engineering into core client engagements."),
    ("2025", "Surpassed two hundred Texas B2B client engagements across four major metros."),
    ("2026", "Headquarters at 518 Brynmawr Ct, Arlington; full-stack local, GMB, AI, and lead systems statewide."),
]


ABOUT_VALUES = [
    {
        "title": "Biblical cornerstone ethos",
        "description": (
            "Our name from Psalm 118:22 reflects the mission: elevate overlooked businesses "
            "into market cornerstones through honest, excellent work."
        ),
    },
    {
        "title": "Texas market obsession",
        "description": (
            "We study DFW, Houston, Austin, and San Antonio search behavior continuously. "
            "Strategies are built for Texas buyers, not generic national templates."
        ),
    },
    {
        "title": "Measurable B2B outcomes",
        "description": (
            "Map Pack rankings, qualified leads, review velocity, and AI citations must tie "
            "to pipeline. Vanity metrics do not drive our decisions."
        ),
    },
    {
        "title": "Founder accountability",
        "description": (
            "Clients work directly with Mike Kaswatuka for strategy and quality control. "
            "We accept fewer accounts to maintain execution standards."
        ),
    },
]
