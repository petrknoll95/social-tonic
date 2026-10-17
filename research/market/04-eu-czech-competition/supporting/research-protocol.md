# Research protocol and delegation record

Research cut-off and access date: **17 October 2026**. This is an exploratory competitor map, not a retail census, sales forecast or legal clearance. No people were contacted, purchases made or consumer tests performed.

## Repository review and scope

The supplied checkout's remote resolves to `https://github.com/petrknoll95/social-tonic.git`; the owner was read from the remote, not guessed. Baseline: `fd1f121`, `main`, clean and synchronized with `origin/main`. The lead read the root README, research index, US report, EU/science memo, independent review, opportunity ranking and validation plan. No applicable `AGENTS.md` was found in the checkout or its ancestor directories. No equivalent EU/Czech competition folder existed: this topic uses the requested `research/market/04-eu-czech-competition/` without a mapping or duplicate repository.

The [US landscape](../../01-us-product-landscape/README.md) remains the benchmark source. It correctly separates promises, ingredient evidence and commercial outcomes, and distinguishes recent launches from flavor/retail events. Its largest gaps for this assignment are local distribution, Czech price competition, country-specific alternatives and bottled/canned coffee and tea. Newly discovered evidence and contradictions are recorded in this topic rather than silently overwriting the earlier work.

During research, concurrent commit `db4216a` revised topic 01 to research-only scope and removed its old opportunity ranking and validation plan. Those files were read at baseline but are not linked as current outputs. This topic's shortlist and next-step proposals respond to the present assignment independently. Unrelated work in topic 26 was also observed and preserved. The lead refreshed the repository and research index again before publishing. Topic26 was published as commit `8d09cac` during final integration; its README, briefing and methods were inspected. The lead used a linked publication checkout based on that commit to preserve its index entry and unrelated local work. No duplicate Git repository was created.

## Parallel work and ownership

| Workstream | Research questions | Assigned outputs | Independence |
|---|---|---|---|
| Czechia agent | Which exact drinks can a Czech buyer obtain, at what price, through which channel? Which direct focus/calm competitors already exist? | Czechia memo, source register and dataset | Separate from other countries and lead synthesis |
| Central EU agent | How do Germany, Austria and Poland differ in functional options, substitutes and verified routes to market? | Central EU memo, source register and dataset | Non-overlapping country remit |
| Western Europe agent | What do Netherlands/France reveal about functional, social and CBD offers? What must remain separate in UK/Switzerland? | Western Europe memo, source register and dataset | Non-overlapping country remit |
| Lead | Reuse US evidence; update EU/Czech regulatory and scientific gates; integrate country and occasion comparisons; validate files and publish | Shared report, matrix, consolidated sources, index, protocols and publication record | Owns all shared files and Git operations |
| Independent review | Reopen decision-changing sources; challenge geography, package eligibility, price arithmetic, channel/scale and proposed gaps | Review memo and resolutions | Researchers review another researcher's work; no self-review claimed |

Agents received the full project context, repository findings, strict format rule, shared schemas and explicit file ownership. The research ran concurrently; integration and publishing are sequential. Review scope and any residual limitations appear in the independent review.

## Sampling and exclusions

Countries are a **purposive shortlist**, not a ranking of market attractiveness. Czechia is the founder-access learning market; Germany, Austria and Poland are adjacent comparison markets; the Netherlands and France provide different domestic grocery, functional and adult-soft-drink contexts. UK and Switzerland are non-EU reference markets. Other EU countries, including Slovakia, remain unassessed; omission does not imply weak demand or poor launch suitability.

Qualifying consumer products are finished, ready-to-drink liquids in cans or bottles, including exact coffee/tea and bottled-shot SKUs. Alcohol-free beer, premium soda, kombucha and premixed alcohol-free mocktails qualify as substitutes. Non-alcoholic does not necessarily mean 0.00% ABV; verify the exact label and residual alcohol before any strict-zero proposition. Excluded formats: powder, sachet, pouch (including liquid), tablet, capsule, gummy, gel, drops and consumer concentrate requiring preparation. Raw manufacturing ingredients may use other forms. Brewed coffee/tea and supplement routines may inform interviews but are never product benchmark rows or attributed sales evidence.

Local competitors need not be recent launches. US benchmarks must retain their verified 2025–2026 relevance and exact liquid-line limitations from topic 01. No whole-brand supplement revenue is used to establish drink success. No THC-led/intoxicating product is a launch candidate.

## Evidence rules

Every dataset observation is dated. A page without a publication date is `unknown`; crawl/access date does not become publication date. A live page is not guaranteed fulfillment. `In stock`, `listed`, `unavailable` and conflicting controls are kept separate. Checkout and delivery were not tested. Search snippets are weaker than opened source pages and flagged when relied upon.

Channel classification describes the evidenced route: mainstream retailer listing, specialist retailer, hospitality, domestic DTC or cross-border offer. A chain website is not proof of nationwide physical shelf presence. A stockist list is a brand claim until independently corroborated. Hospitality presence requires identifiable outlets/menus or distribution evidence; a brand's suggested serving occasion is insufficient.

Use three separate evidence questions:

1. **Availability/formula/price:** retailer and label/brand pages can establish the observed offer, subject to variant and stock uncertainty.
2. **Commercial demand and scale:** prefer geography- and line-specific units/value/velocity with defined period and method. Store count, funding, reviews, company size and launches are proxies with different meanings. Missing public sales remain unknown, not zero.
3. **Effects:** marketing is not scientific evidence. Ingredient studies require exact dose, identity, population, duration and delivery assessment before transfer to a processed, stored mixed beverage.

Product evidence quality is `high`, `medium` or `low` for the supported observation, not a score of product quality or efficacy. Strong listing evidence can coexist with unknown scale. Business maturity is an analyst classification based on the evidenced operator/range: established, emerging, or unknown. An established parent's new SKU does not inherit established SKU sales. Brand recognition is unknown unless supported by relevant consumer measurement; retailer reach and company longevity are labeled proxies.

## Prices and calculations

One serving is defined consistently as **one entire can or bottle**, even when a label suggests smaller portions. `price_per_container = (displayed pack price − refundable deposit included in that price) / pack_units`; subtract a deposit only where the source explicitly includes it. Round to two decimals for comparisons while retaining basis. Separately charged deposits are additional cash at checkout. Multi-serve bottles are identified and not treated as equivalent consumption volumes. Prices remain in local currency; no exchange-rate or purchasing-power equivalence is assumed. Retain regular/promotion/subscription distinctions, deposit treatment where visible, and shipping exclusions. An unverified price is `unknown`, not estimated from another country or flavor. Compare like channel, volume and promotional status before interpreting a premium.

## Limits and next evidence

Search engines and public retail pages bias the sample toward visible, indexed products. Local distribution, recognition and sales are incompletely disclosed; store audits and buyer interviews are needed before claiming saturation or a distribution gap. Customer interviews must investigate the last real occasion and current substitute, not merely agreement with a wellness benefit. Exact proposed protocols and disconfirmation tests are in [validation protocol](validation-protocol.md).
