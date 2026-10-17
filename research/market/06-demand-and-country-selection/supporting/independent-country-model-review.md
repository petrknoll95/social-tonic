# Independent country and demand-model review

Review date: **17 October 2026**. Reviewer: Austria/Germany/Netherlands research agent, separate from the lead who built the model. This is an independent challenge of integration and calculations, not an external audit; the reviewer also supplied one regional evidence memo.

Reviewed: [model inputs](../data/model-inputs.json), [calculation script](../data/recalculate.py), all 90 [demand scenarios](../data/demand-scenarios.csv), 30 [category/country scores](../data/category-country-scorecard.csv), [data definitions](../data/README.md), [validation protocol](validation-tests.md), and the completed [integrated report](../report.md). Final narrative review completed on the research date; no material unresolved country/model finding.

## Arithmetic and scope checks

- Independent read-only calculations, without running the lead's regeneration function, matched every scenario's unique pool, qualified reach, first buyers, repeat buyers, units and revenue, and every category/country total score.
- Czech base independently recomputes to 14,000 unique adults, 8,400 qualified, 672 first paid buyers, 235.2 expected repeat buyers, 9,811.2 units and **€10,792.32 net revenue**. Fractions are expected values, not claims that part of a person bought a drink.
- Score weights total 100. Country-only results are scaled separately from their 45-point contribution; they must not be mistaken for the full category/country score.
- Scenarios are alternatives and category audiences overlap. The data README explicitly prohibits summing them, separates repeat from first buyers and provides an overlap illustration.
- No observed population/coffee/energy category is mechanically converted into new-product sales. All reach, conversion, price, retention and cost assumptions are labelled hypotheses. This is appropriate for early validation but does not constitute a statistical market-size estimate.
- Regional evidence preserves the canned/bottled-only product rule. Habit surveys covering fresh coffee are marked contextual. No whole-brand powder/concentrate revenue validates an RTD line.

## Challenges raised and their disposition

| Issue | Initial concern | Disposition in reviewed definitions |
|---|---|---|
| Repeated visitors across venues | Summing venue-level unique people can still double-count the same person across sites. | Data README explicitly defines venue reach as already deduplicated within/across venues. This remains an unmeasured assumption to replace with actual unique exposure data. |
| Staggered buyer acquisition | Six repeat orders could accidentally assign a full year to buyers recruited late. | Defined as average realised repeat orders before month12, already allowing for staggered recruitment/attrition. Actual cohorts must validate it. |
| Net revenue versus shelf price | VAT, deposits, wholesale margin, levies and costs could be mixed. | README excludes VAT/deposits/channel deductions from receipts; levies/nonrefundable fees enter costs; contribution excludes acquisition/fixed cost. Dutch excise needs actual formula classification. |
| Focus versus conventional energy | The 73 versus71 Czech result looks precise despite uncertain switching reasons. | A one-point reduction in focus's assumed switching score costs four points and reverses the lead. Treat the two-point gap as an unresolved comparison, not proof that focus wins. |
| Germany versus Austria | Broad economic size could be described as reachable demand. | Country-only German advantage is just one of45 possible points under assumptions. Reach plans differ and have no demonstrated access. Pair regional German and Austrian price/access tests; buyer access can reorder them. |
| Calm/sleep legality scores | Category labels could suggest an inherently unlawful beverage. | Low scores should describe effect-led ingredients/claims and evidence complexity. A flavour/ritual-only CBD-free drink may be simpler but must be tested separately; no exact formula is cleared. |
| Pilot repeat confidence | 35 of100 repurchasers might be called a proven annual35% repeat rate. | Protocol gives approximately26–45% Wilson95% interval and distinguishes the short pilot gate from annual repeat/order assumptions. |

## Evidence-date and geographic safeguards

The Dutch coffee figure is age16+ and the Austrian coffee survey age14–75, so neither is adult18+ prevalence. A Trimbos PDF uploaded in2025 contains adult2022 data; the newer2026 report uses a2024 adult panel. The German cognitive-motive paper and university release disagree on62.4% versus64.2%; neither numerical estimate enters the model. German AF beer production is not consumption; Austrian domestic sales and Dutch survey motives use different denominators. These cannot form a directly comparable country prevalence league table.

German retail-concentration sources differ by date/access path and scope. They support concentrated buying power, not a precise probability of a startup listing. National availability of a functional SKU is not efficacy, legal clearance, awareness or repeat.

## Review conclusion and residual uncertainty

The completed report preserves the age and date caveats, gives macro purchasing power limited meaning, states the weak two-point benefit lead, and makes the German/Austrian expansion order reversible. Its country table and model narrative are consistent with the source workstreams. No unsupported new-product awareness or repeat number is presented as fact. The German 85% concentration figure remains explicitly attached to the November2025 report, while the supporting evidence records a newer secondarily accessed estimate; this is acceptable as dated context, not a current precision ranking.

Two minor wording corrections were sent to the lead: label Monopolkommission as a commission/report rather than the competition authority, and describe a regional German test as a recommendation rather than an obligatory consequence of concentration. Clarify that **venue adult counts**, not venue counts themselves, have assumed cross-venue deduplication. These do not change the arithmetic or recommendation.

The reviewed model is arithmetically consistent and suitable as a **test-planning model** when its uncertainty labels remain prominent. The strongest decision is to learn locally before funding a foreign rollout; the exact benefit and expansion ranking are conditional. The work does not establish consumer demand for an unmade product, supplier cost, retailer access or sufficient margin. Paid, deduplicated cohorts and landed-cost quotes are necessary to replace the key assumptions.
