#!/usr/bin/env python3
"""Generates the demo site into ./docs from the data below. Run: python3 build.py

A FICTIONAL firm used to test Verand's Zapier integration (and give Zapier's reviewers real data).
Every page carries <meta name="robots" content="noindex, nofollow"> and a visible demo banner.

Planted on purpose, so Verand's crawl has findings to report (README lists them):
  - the six articles never link to each other (internal-linking opportunities);
  - two articles have no meta description;
  - /services/ links to a page that doesn't exist (broken internal link);
  - /about/ and /contact/ share a title (duplicate title);
  - /contact/ has no H1;
  - the chart image on /insights/retirement-income-buckets/ has no alt text.
"""
import os, html, shutil

BASE = "https://zapier-demo.verand.ai"
FIRM = "Harbor &amp; Vale"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")  # GitHub Pages serves main:/docs

DISCLAIMER = ("Demo content for testing Verand's software. Harbor &amp; Vale is a fictional firm; "
              "nothing here is financial, tax or legal advice.")

ARTICLES = [
    {
        "slug": "roth-conversion-basics",
        "title": "Roth Conversions: How They Work",
        "meta": None,  # REVIEW RUN 2 (Zapier T004, 2026-11-17): restore "What a Roth conversion is, how it's taxed, and the questions to answer before you convert."
        "body": [
            "A Roth conversion moves money from a traditional IRA or 401(k) into a Roth IRA. The amount you convert counts as ordinary income in the year you convert it, so you pay the tax now in exchange for tax-free qualified withdrawals later.",
            "The decision usually turns on one comparison: your tax rate today against the rate you expect when you'd otherwise withdraw the money. If you expect a higher rate later, converting now can come out ahead. If you expect a lower one, it often doesn't.",
            "There's no income limit on conversions, which is why they're the standard route into a Roth for people who earn too much to contribute directly. You also don't have to convert everything at once. Many people convert a slice each year to control how much income they recognize.",
            "Pay attention to timing. Each conversion starts its own five-year clock for penalty-free access to the converted principal if you're under 59 and a half. And a large conversion can raise other costs tied to income, such as Medicare premiums for people on Medicare.",
            "Before converting, map out where the tax money will come from. Paying it from outside the account keeps more money growing tax-free inside the Roth.",
        ],
    },
    {
        "slug": "roth-conversion-tax-brackets",
        "title": "Filling a Tax Bracket With a Roth Conversion",
        "meta": None,  # planted: no meta description
        "body": [
            "One common way to size a Roth conversion is to fill the rest of your current tax bracket and stop there. You estimate your taxable income for the year, find where the top of your bracket sits, and convert just enough to reach it.",
            "The appeal is control. Every dollar converted inside the bracket is taxed at the same marginal rate, and nothing spills into the next one. Doing this over several years spreads the tax across lower-income years instead of paying it all at once.",
            "The low-income years between retirement and the start of required distributions are often the best window. Wages have stopped, Social Security may not have started, and taxable income can be unusually low.",
            "Estimates matter here. Capital gains, dividends and a late-year bonus can all move your taxable income, so many people wait until late in the year, when the numbers are clearer, before deciding how much to convert.",
            "Keep in mind that a conversion can't be undone once it's done. Size it with a margin for income you haven't counted yet.",
        ],
    },
    {
        "slug": "required-minimum-distributions",
        "title": "Required Minimum Distributions, Explained",
        "meta": "When required minimum distributions start, how they're calculated, and what happens if you miss one.",
        "body": [
            "Required minimum distributions, or RMDs, are the amounts you must withdraw each year from most tax-deferred retirement accounts once you reach the starting age set by law. The government lets the money grow tax-deferred for decades; RMDs are how it eventually gets taxed.",
            "The calculation is simple in outline. Take the account balance at the end of the previous year and divide it by a life-expectancy factor from the IRS tables. The result is the minimum you have to take out this year. You can always take more.",
            "Roth IRAs don't have RMDs for the original owner, which is one reason people convert before RMDs begin. Inherited accounts follow their own rules, and those rules changed in recent years, so check the current ones for any account you've inherited.",
            "Missing an RMD is expensive. The penalty is a percentage of the amount you should have withdrawn, though it's reduced if you correct the shortfall promptly.",
            "Because RMDs add taxable income every year, planning for them usually starts well before the first one is due.",
        ],
    },
    {
        "slug": "rmd-qualified-charitable-distributions",
        "title": "Using Charitable Distributions to Meet an RMD",
        "meta": "How a qualified charitable distribution from an IRA can count toward your RMD without adding to taxable income.",
        "body": [
            "A qualified charitable distribution, or QCD, sends money directly from your IRA to a qualifying charity. If you're old enough to make one, it counts toward your required minimum distribution for the year, and it isn't added to your taxable income.",
            "That second part is the point. Taking an RMD and then donating it puts the full amount into your income first, even if you deduct the gift afterward. Many retirees take the standard deduction, so the gift never gets deducted at all. A QCD keeps the money out of income from the start.",
            "The money has to go straight from the IRA custodian to the charity. A check made out to you and then donated doesn't qualify. Donor-advised funds and private foundations aren't eligible recipients.",
            "There's an annual limit per person, adjusted for inflation, so check the current figure before planning a large gift.",
            "Keep the charity's acknowledgment letter. Your custodian's year-end form won't show that the distribution was a QCD, so you'll report it on your return.",
        ],
    },
    {
        "slug": "emergency-fund-sizing",
        "title": "How Big Should an Emergency Fund Be?",
        "meta": None,  # planted: no meta description
        "body": [
            "The usual guideline is three to six months of essential expenses, held somewhere you can reach quickly without risking a loss. It's a starting point, not a rule.",
            "Lean toward the higher end if your income is irregular, if one income supports the household, or if your industry takes a long time to hire. Lean toward the lower end if you have stable income, several earners and other assets you could draw on.",
            "Count essentials, not your full budget. Housing, food, insurance, transport and minimum debt payments are what the fund has to cover. The things you'd cut in a hard month don't need a cushion.",
            "Retirees face a different version of the same question. Instead of covering lost wages, the cash reserve lets you avoid selling investments after a market drop to pay the bills.",
            "Whatever size you choose, write down what counts as an emergency before you need the money. It's easier to protect the fund when the rules were set in a calm moment.",
        ],
    },
    {
        "slug": "retirement-income-buckets",
        "title": "The Bucket Approach to Retirement Income",
        "meta": "How splitting retirement savings into time-based buckets can make withdrawals easier to manage.",
        "image": True,  # planted: chart image with no alt text
        "body": [
            "The bucket approach splits retirement savings by when you'll need the money. A near-term bucket holds cash for the next year or two of spending. A middle bucket holds steadier investments for the following several years. A long-term bucket holds growth investments you won't touch for a decade or more.",
            "The structure is mostly about behavior. When markets fall, you spend from the near-term bucket and leave the long-term one alone, which makes it easier to avoid selling growth investments at a low point.",
            "Refilling the buckets is where the work is. Some people top up the near-term bucket on a schedule. Others refill it only after good years, letting it run down after bad ones.",
            "The approach doesn't change your overall investment mix by itself. It's a way of organizing the same portfolio so withdrawals feel deliberate rather than reactive.",
            "Your required distributions and any Roth conversions interact with the buckets, so it helps to plan all three together.",
        ],
    },
    {
        # REVIEW RUN 2 (Zapier T004, 2026-11-17): a seventh related article, unlinked, so the crawl
        # raises a new internal-links opportunity. Delete this entry afterwards.
        "slug": "roth-conversion-five-year-rules",
        "title": "The Five-Year Rules for Roth Conversions",
        "meta": "How the two Roth five-year clocks work, and how they apply to converted money and to earnings.",
        "body": [
            "Roth accounts have two separate five-year rules, and they're easy to mix up. One decides when earnings can come out tax-free. The other decides when converted money can come out without the early-withdrawal penalty.",
            "The first clock starts with your first contribution to any Roth IRA. Once five years have passed and you're 59 and a half or older, withdrawals of earnings are tax-free. That clock runs once, for all your Roth IRAs together.",
            "The second clock applies to each Roth conversion on its own. Every conversion starts a new five-year period for penalty-free access to the converted principal if you're under 59 and a half. Several conversions mean several clocks.",
            "After 59 and a half, the conversion clocks stop mattering for the penalty, but the first clock still governs whether earnings are tax-free.",
            "Because each conversion has its own clock, people who convert in slices over several years often keep a simple record of each year's amount and date.",
        ],
    },
]

STATIC_PAGES = [
    {
        "path": "",
        "title": "Harbor & Vale Financial Planning",
        "meta": "Fee-only financial planning for people approaching and living in retirement. A demo site for Verand.",
        "h1": "Planning for the years after work",
        "body": [
            "Harbor &amp; Vale is a fictional fee-only planning firm. This site exists so Verand's crawl, triggers and drafts have something real to work on.",
            "We write about the decisions that come up most in the decade around retirement: when to convert to a Roth, how to handle required distributions, how much cash to keep, and how to turn savings into income.",
        ],
        "links": [("/insights/", "Read our insights"), ("/services/", "See our services")],
    },
    {
        "path": "about/",
        "title": "Harbor & Vale",  # planted: duplicate of /contact/
        "meta": "About Harbor & Vale, a fictional fee-only financial planning firm used as a Verand demo.",
        "h1": "About us",
        "body": [
            "Harbor &amp; Vale is a fictional firm. Its planners and clients exist only on this demo site.",
            "Our fictional team works with people in their fifties, sixties and seventies, with a focus on tax-aware retirement income.",
        ],
    },
    {
        "path": "services/",
        "title": "Services | Harbor & Vale",
        "meta": "Retirement income planning, Roth conversion planning and tax-aware withdrawal strategies.",
        "h1": "Services",
        "body": [
            "Retirement income planning, Roth conversion planning, required distribution planning and charitable giving strategies.",
            "Every engagement starts with a review of your accounts, your expected income and your tax picture.",
        ],
        "links": [("/insights/estate-planning-checklist/", "Our estate planning checklist")],  # planted: broken link
    },
    {
        "path": "contact/",
        "title": "Harbor & Vale",  # planted: duplicate of /about/
        "meta": "Contact Harbor & Vale. This is a demo site, so there's no one to contact.",
        "h1": None,  # planted: no H1
        "body": ["This is a demo site for Verand, so there's no one to contact here."],
    },
]

CSS = """
:root{--ink:#1d2433;--muted:#5a6475;--line:#e3e7ee;--accent:#1e5640;--bg:#ffffff;--band:#fff4d6}
*{box-sizing:border-box}body{margin:0;font:17px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg)}
.demo{background:var(--band);border-bottom:1px solid #f0d58a;padding:8px 16px;font-size:14px;text-align:center}
header,main,footer{max-width:760px;margin:0 auto;padding:16px}
header{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line)}
header a{color:var(--ink);text-decoration:none}nav a{margin-left:14px;font-size:15px}
.brand{font-weight:700}h1{font-size:30px;line-height:1.25;margin:24px 0 12px}a{color:var(--accent)}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:14px;margin-top:40px}
ul.list{padding-left:18px}img{max-width:100%;height:auto}
"""

def esc_attr(s):
    return html.escape(s, quote=True)

def page(path, title, meta, h1, body_html):
    meta_tag = f'<meta name="description" content="{esc_attr(meta)}">' if meta else ""
    h1_tag = f"<h1>{h1}</h1>" if h1 else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{html.escape(title)}</title>
{meta_tag}
<link rel="canonical" href="{BASE}/{path}">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<div class="demo">Demo site for testing <a href="https://verand.ai">Verand</a>. {FIRM} is a fictional firm.</div>
<header><a class="brand" href="/">{FIRM}</a><nav><a href="/about/">About</a><a href="/services/">Services</a><a href="/insights/">Insights</a><a href="/contact/">Contact</a></nav></header>
<main>
{h1_tag}
{body_html}
</main>
<footer><p>{DISCLAIMER}</p></footer>
</body>
</html>
"""

def write(path, content):
    full = os.path.join(OUT, path, "index.html") if not path.endswith(".html") else os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def paras(ps):
    return "\n".join(f"<p>{p}</p>" for p in ps)

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    urls = []
    for p in STATIC_PAGES:
        links = "".join(f'<p><a href="{href}">{text}</a></p>' for href, text in p.get("links", []))
        write(p["path"], page(p["path"], p["title"], p["meta"], p["h1"], paras(p["body"]) + links))
        urls.append(p["path"])
    # Insights index links to every article; the articles themselves never link to each other.
    items = "".join(f'<li><a href="/insights/{a["slug"]}/">{a["title"]}</a></li>' for a in ARTICLES)
    write("insights/", page("insights/", "Insights | Harbor & Vale", "Articles on Roth conversions, required distributions, emergency funds and retirement income.", "Insights", f'<ul class="list">{items}</ul>'))
    urls.append("insights/")
    for a in ARTICLES:
        path = f'insights/{a["slug"]}/'
        body = paras(a["body"])
        if a.get("image"):
            body = '<p><img src="/img/buckets.svg" width="640" height="260"></p>' + body  # planted: no alt
        write(path, page(path, f'{a["title"]} | Harbor & Vale', a["meta"], a["title"], body))
        urls.append(path)

    with open(os.path.join(OUT, "style.css"), "w") as f:
        f.write(CSS.strip() + "\n")
    os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
    with open(os.path.join(OUT, "img", "buckets.svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 260"><rect width="640" height="260" fill="#f6f8fb"/>'
                '<rect x="60" y="150" width="140" height="80" fill="#9cc7b2"/><rect x="250" y="100" width="140" height="130" fill="#5f9e80"/>'
                '<rect x="440" y="40" width="140" height="190" fill="#1e5640"/></svg>\n')
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        # Crawling stays allowed: a search engine has to fetch a page to see its noindex tag.
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            f.write(f"  <url><loc>{BASE}/{u}</loc></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write("zapier-demo.verand.ai\n")
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print(f"built {len(urls)} pages into {OUT}")

if __name__ == "__main__":
    main()
