# Commercial metric data

**Cut-off/access: 17 October 2026.** These are selected public observations, not a complete market panel. Repeated rows for a brand measure different things; never add them together.

## Files

- [commercial-metrics.csv](commercial-metrics.csv): consolidated eligible-line observations, distribution proxies, forecasts, unknowns and negative cases. The `status` column controls interpretation: the file is not a list of proven successes.
- [excluded-business-context.csv](excluded-business-context.csv): mixed formats, mixed cannabinoid/geographic segments, unallocated subscribers/reorders and unverified current formats. These cannot be used to infer the qualifying drink line's scale. Included for transparent attribution and contradiction review.
- [focus-energy-metrics.csv](focus-energy-metrics.csv), [calm-sleep-cbd-metrics.csv](calm-sleep-cbd-metrics.csv), [secondary-metrics.csv](secondary-metrics.csv): original workstream extractions. Read all scope/eligibility/status fields; these preserve rejected/context rows too.
- The authoritative combined source ledger is [sources.csv](../sources.csv). Stream source extracts preserve authorship and provenance.

## Fields and normalization

| Field | Meaning |
|---|---|
| metric_id | Stable unique ID; FEM, CSM or SCM prefixes identify workstream, not evidence rank |
| brand / line_or_sku | Brand and actual measurement scope; an exact flavor may only verify packaging |
| category / format | Consumer job/category and qualifying can/bottle, or explicit reason the context fails the filter |
| metric / amount / unit | Exact observation; `>`, `nearly`, intervals and unknown values are retained as text, not silently converted to point estimates |
| currency | ISO currency for financial amounts; `not applicable` for counts/rates/ranks; `unknown` where unresolved. Original extracts sometimes place units in this field; use the consolidated view for normalization. |
| period | Measurement interval; not necessarily publication date. Unspecified first-year, annual or cumulative windows remain explicit. |
| geography | Reported territory and channel; inference is labeled. UK is not EU; combined UK/Europe is not EU-only. |
| scope | Eligible line versus whole business, category, flavor and channel boundary |
| status | Achieved observation, cumulative claim, forecast, proxy, unknown, contextual exclusion or negative case |
| evidence_class / confidence | Underlying origin and confidence in exact observation. A filing-hosted panel table is panel evidence, not audited brand revenue. |
| source_ids / source_urls | Semicolon-delimited IDs and direct links; multiple sources may verify metric plus packaging, not independent measurements |
| limitations | Missing definitions, access restrictions, non-comparability and attribution risks |

`Unknown` means not established by this review, not zero. `Not applicable` means the concept does not apply. No FX conversion, annualization, retail-price-times-units revenue estimate, cases-to-cans conversion or revenue/store-count velocity estimate is used. Confidence is documentary, not clinical.

Metrics do not include every incidental number in supporting memos. The report prioritizes decision-useful observations, while source extracts also retain rejected leads. Evidence counts are record counts, not counts of independent sales audits. Publication/access dates, title, publisher, supported claims and limitations are in the source ledger; undated pages remain undated.

## Reading the ranking

Compare specialist productivity drinks with each other before comparing them with mass energy. Compare CBD-free calm separately from CBD; mixed TRIP cans cannot be assigned to either. Sleep products with a live exact-format offer remain unproven where line sales are unknown. Poppi retail dollars and OLIPOP company revenue cannot be ranked as equivalent measures. The same line can have older achieved sales and newer negative evidence, as Poppi illustrates.

There is no validated cross-brand store-velocity or paid-retention benchmark here. The [proposed protocol](../supporting/validation-and-diligence-protocol.md) specifies the missing denominators and measurement windows needed for later diligence.
