# zapier-demo.verand.ai

A **fictional** financial-planning firm ("Harbor & Vale") that exists only to give Verand's Zapier
integration, and Zapier's reviewers, real data to work with. Every page carries
`<meta name="robots" content="noindex, nofollow">` and a visible demo banner. Nothing here is
advice; the firm and its people don't exist.

It's onboarded in Verand on the dedicated `zapier-test@verand.ai` account, with scheduled work off.

## Build

`python3 build.py` regenerates `docs/` (served by GitHub Pages from `main:/docs`). Edit the data at
the top of `build.py`, never the generated HTML.

## Findings planted on purpose

| Finding | Where | Feeds |
|---|---|---|
| Six related articles that never link to each other | `/insights/*` | New Opportunity (internal links) |
| No meta description | two articles | New Site Issue |
| Broken internal link | `/services/` | New Site Issue |
| Duplicate title | `/about/`, `/contact/` | New Site Issue |
| No H1 | `/contact/` | New Site Issue |
| Image without alt text | `/insights/retirement-income-buckets/` | New Site Issue |
| noindex on every page | everywhere | New Site Issue (deliberate) |

## Making a trigger fire on demand (live Zap runs)

Zapier only fires on items it hasn't seen since the Zap was turned on, and Verand's triggers key on
the finding, not the row, so a re-crawl of an unchanged site fires nothing. To produce a new item:

- **New Site Issue:** remove the `meta` of another article in `build.py`, rebuild, push, then run a
  crawl for the site in Verand (Scheduled Tasks, Deep full-site crawl, Run now).
- **New Opportunity:** add a seventh article on a related topic (unlinked), rebuild, push, re-crawl.
- **New Article Draft:** generate a draft from a brief in Verand (uses one article of the allowance).

Put the finding back afterwards so the site stays a stable baseline.
