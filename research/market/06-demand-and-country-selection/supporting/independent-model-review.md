# Independent adversarial review: model and validation plan

**Review date: 17 October 2026. Status:** initial review of model/input/derived files and validation protocol; lead report was still being drafted and was not available. This reviewer authored the separate Czechia/Poland evidence workstream but did not author or change the model, weights, scenarios or validation plan. Only this review file was written. Findings below are the pre-resolution record; subsequent lead resolutions should be recorded separately rather than represented as having existed during this review.

Reviewed [inputs](../data/model-inputs.json), [calculation script](../data/recalculate.py), all derived score/scenario/sensitivity tables, [data explanation](../data/README.md), population/spending CSVs, [methods](research-plan-and-method.md) and [validation protocol](validation-tests.md). Independent standard-library calculations read the JSON and compared every row of the 90-scenario CSV. No recalculation script was run because that script overwrites derived outputs; independent calculations were read-only.

## Outcome

**Arithmetic passes; decision confidence is materially weaker than the precision of the scorecard.** The artifacts provide visible assumptions, bottom-up adult reach, first/repeat purchaser separation, non-additive category alternatives and transparent net-revenue arithmetic. They are a planning model, not measured market size or a statistically calibrated forecast. A Czech-first learning recommendation is defensible as a founder preference if the report makes the fragility and economic gaps prominent.

Severity: **P1** means fix before using the study to justify paid country entry or production; **P2** means correct or explicitly qualify before publication. No P0 arithmetic or consumer-double-counting error was found.

## Findings and suggested corrections

### P1 — The paid-trial test lacks an explicit exposure denominator

Gate 5 aims for 100 first buyers, which can establish a repeat cohort. It does not explicitly require recording all unique, eligible adults shown an in-stock, priced offer, including people who decline. The model's 8% trial rate is conditional on exactly that denominator. Acquiring 100 buyers without knowing whether 500 or 10,000 relevant adults were exposed cannot replace trial, reach or acquisition-cost assumptions.

**Correction:** record unique qualified adult exposures, channel, displayed price, stock availability, purchase/no purchase, first-purchase date and acquisition spend; deduplicate across locations/digital. Keep free tasters and employer-paid drinkers separate. Use this denominator for paid trial, and first buyers for repeat. Report both with time windows. Do not imply that an 8–12-week repeat study validates six repeat orders within a full launch year; the existing caution on that point should remain.

### P2 — The first benefit recommendation flips with a single plausible score revision

Default Czech focus scores 73 and ordinary energy 71. Reducing focus's **switch reason** from 3 to 2 subtracts four points, making energy win 71 to 69. Raising energy's switch score from 1 to 2 makes it win 75 to 73. No measured switching evidence establishes the two-point difference. Weight scenarios already show energy wins when current demand evidence receives greater weight, but a weight scenario does not expose uncertainty in the scores themselves.

**Correction:** publish these one-score reversals and a short criterion rubric with a rationale/source/assumption for each decision-changing score. Recommend a *first concept to test*, conditional on switching and repeat, rather than a settled winning category. Established energy demand may be stronger while a distinct workday occasion is a better learning hypothesis; those are different claims.

### P2 — Country preference depends on unverified founder and channel access

Czech country points exceed Germany by eight (36 versus 28). Founder access alone adds nine points relative to Germany; channel access adds another two. Czech residence supports easier local operation, but neither actual audience nor venue contacts were supplied. The README correctly states zero contracted reach; scores of founder access 5/5 and channel access 4/5 nevertheless risk implying secured access or double-counting locality. Country score is not a statistically measured attractiveness index.

**Correction:** distinguish language/iteration convenience from actual commercial access in the score rationale. Add a sensitivity for Czech founder score 5→3 and channel score 4→3: country points fall eight to 28, tying Germany. Make Gate 1 a condition of the Czech-first recommendation. The founder-learning interpretation should appear next to the ranking, not only in methods.

### P2 — Focus and energy revenue equality is built into assumptions

In every country/scenario, focus qualification × price factor = 0.60×1.00, while general energy = 0.75×0.80 = 0.60. All other conversion, repeat and basket assumptions are identical. Thus equal projected net revenue is a mathematical identity. It is not a corroborating result that the categories have equal commercial potential. Similarly, sleep/social price premiums are assumptions unsupported by local paid demand.

**Correction:** flag the identity directly when discussing the category comparison. Do not optimize against these exact revenue rankings. Either retain as explicitly neutral planning controls or add a category-specific parameter stress range; eventual selection requires measured switching, repeat, channel mix and realizable price.

### P2 — Comparative channel economics are absent, while some cost inputs are unused

Country `variable_cost_eur` fields are not consumed by the script. The contribution output is solely a Czech grid with separately hard-coded costs. This is disclosed in the README, but a reader could assume the country cost parameters drive a comparable contribution forecast. German/Austrian/Dutch net-price advantages and Polish revenue disadvantage are assumed; the model has no shelf-price-to-brand-receipt bridge or country-specific channel mix. Single-can trial and repeat multipacks also share one net receipt, although current Czech Vilgain asking prices differ between singles and packs.

**Correction:** mark unused inputs or remove them. Explicitly state comparative contribution is unknown and must not be inferred from revenue. Provide a template for retail VAT/deposit, retailer/distributor deductions, promotions and DTC fees, plus landed cost, before choosing expansion. Include Poland's pending tax increase as a separate sensitivity, not current law. This need not become a fabricated supplier quote.

### P2 — Annual repeat and the very wide high case need prominent interpretation

The Czech focus base is 672 first buyers, 235.2 expected repeaters and 9,811.2 cans. **86.3% of units come from repeat orders.** The high scenario reaches 40,000 adults, 2,880 first buyers, 1,440 repeaters and 123,840 cans, compared with 326.4 cans in low. Net revenue ranges €277.44–€160,992, a roughly 580-fold ratio. This is produced by jointly raising reach, conversion, repeat, frequency, basket and net price; it is not an empirical forecast interval.

The model defines frequency as already adjusted for staggered acquisition, but no acquisition-month cohort schedule verifies that adjustment. The definition makes the arithmetic coherent; the assumed adjustment remains untested.

**Correction:** retain the explicit stress-scenario label next to the headline range and state that most base revenue depends on unobserved repeat. Call high an operational stretch requiring more channel work/working capital, not plausible upside at the same budget. Add acquisition-month/time-at-risk data in the pilot and a monthly cohort model before a production commitment. Fractional buyers/cans are expectations, not actual purchasable units; round user-facing tables sensibly.

### P2 — The cheapest concept test risks too many sparse cells

Gate 2 proposes 60–100 adults, three concepts and three prices. A full 3×3 design yields approximately 7–11 people per cell. It can reveal confusion and qualitative objections, but cannot reliably rank conversion differences, identify price elasticity or support nine-cell optimization. The protocol correctly calls small cells directional; the implied breadth still needs narrowing.

**Correction:** hold price fixed for the first concept comparison, use the same ready-to-drink can size, and test finalist price separately. If retaining nine cells, explicitly treat it as qualitative screening and prohibit selecting a winning conversion percentage from it. None of these responses should be substituted for paid trial in the model.

## Checks that passed

- Independently recomputed all 90 outputs with no discrepancies for union reach, qualified adults, first buyers, repeaters, units or revenue.
- Czech base: 12×500+10,000−2,000 = 14,000 unique adults; ×0.60 = 8,400 qualified; ×0.08 = 672 first buyers; ×0.35 = 235.2 expected repeaters; 672×2+235.2×6×6 = 9,811.2 cans; ×€1.10 = €10,792.32.
- Category qualification fractions sum above one but rows are explicitly mutually alternative launch plans. Repeaters are correctly subsets of first buyers. No portfolio sum is presented; overlap example correctly caps the union at the shared pool. Country rows likewise cannot be added automatically.
- Net receipts exclude VAT/deposits and downstream margins. Variable levies/packaging fees are explicitly allocated to costs, preventing an obvious double deduction. These definitions are sound even though no actual commercial terms validate the inputs.
- Czech contribution at €1.10 net and €0.85 variable cost is €2,452.80, or €3.65 per acquired first buyer, before acquisition/fixed costs/founder time. The 60,000-can break-even illustration for €15,000 fixed costs is correct. Calling base revenue a viable business would contradict the model's own economics.
- 35/100 repeaters gives an approximately 26–45% Wilson interval, consistent with the validation note.
- Population CSV adult totals equal total minus under-18 and unknown-age counts; this arithmetic check did not independently re-fetch or audit the full Eurostat age extraction. The data explanation appropriately avoids using population or AIC as direct functional-drink demand.

## Overall instruction to integration

The assignment is substantially fulfilled at the *transparent hypothetical demand-planning* level, not at verified accessible-customer or paid-market-size level. Keep that distinction visible. Fix the pilot denominator, show score fragility, avoid treating constructed revenue ties as findings, and keep expansion conditional on actual contribution and access. An unresolved assumption is acceptable in exploratory research; a precise ranking must not conceal it.

## Resolution recheck — 17 October 2026

The same reviewer subsequently read the revised validation protocol, [score rationale](score-rationale.md), [score sensitivity](../data/score-sensitivity.csv), country-cost output and code, channel-receipt worksheet, and the relevant integrated-report passages. This was a targeted read-only recheck of the findings above; only this appended review record was written.

- **Paid-trial denominator — resolved.** The protocol and report now explicitly require all unique qualified adult exposures to a priced, in-stock offer, including nonbuyers, together with stock, price, qualification, channel, acquisition spend and deduplication. First buyers remain the separate repeat denominator.
- **Benefit and country score fragility — resolved through disclosure and sensitivity.** One-score reversals and the Czech/German tie under weaker Czech access are present. Criterion rationales distinguish local iteration from secured access and identify the default as a learning preference. Score sensitivity still contains ordinal ranks for ties; the equal numeric scores and report interpretation, rather than arbitrary tied row order, govern the conclusion.
- **Constructed focus/energy revenue tie — resolved.** The integrated report and data explanation now explicitly state that the equal result is built into the qualification/price assumptions and does not establish equal commercial potential.
- **Country-cost inputs and receipt bridge — resolved for research scope.** Country cost assumptions now feed five contribution rows. Independent calculations reproduced all five contribution totals and per-first-buyer values. The receipt worksheet separates VAT/deposits, downstream margins, channel/basket mix and landed variable costs. Actual comparative economics appropriately remain unknown; these placeholders do not establish the expansion winner.
- **Repeat/horizon and high-case interpretation — resolved through qualification.** The report foregrounds the 86.3% dependence on unobserved repeat, rounds expected buyers/cans, describes high as a demanding joint stretch, and explicitly permits zero-sale/blocked-launch outcomes. A monthly cohort schedule is required before inventory commitments. No empirical probability is assigned to the scenarios.
- **Sparse concept/price cells — resolved.** The protocol now holds price and can size fixed for the initial concept comparison and tests finalist prices sequentially.

No material unaddressed model-review blocker remains for publishing this as an exploratory, assumption-led country-entry study. This recheck does **not** validate actual demand, consumer efficacy, supplier costs, distribution access or launch legality. The report's conditional recommendation and instruction against premature national rollout/large production are consistent with the evidence limits.
