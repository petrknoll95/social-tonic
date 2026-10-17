# Independent review of the product brief and scenario models

**17 October 2026. Reviewer: packaging/operations sub-agent, independently examining lead-authored material.** This review covers [product brief](../product-brief.md), [model inputs](../data/model-inputs.json), [recalculation script](../data/recalculate.py), the three output scenario CSVs, [data guide](../data/README.md), and [validation/RFQ protocol](validation-and-rfq-protocol.md). The reviewer did not author those documents and did not edit them. The reviewer's own packaging memo was not independently reviewed in this pass. The integrated report was outside this review's initial scope.

**Final disposition: pass for publication as explicitly provisional research and sensitivity models.** The initial parameterization defect was corrected and independently retested at both 26 and 13 weeks. The consumer-format filter passes, and no approved dose/claim or validated customer demand is implied. This is not manufacturing, legal or safety approval.

## Findings and requested corrections

| Priority | Finding | Evidence and consequence | Requested action / initial status |
|---|---|---|---|
| Material reproducibility issue — corrected | Saleable window was configurable in the input and used for unsold stock, but required total demand was divided by a hardcoded 26; several headers also hardcoded 26 | With 6,000 units, 30% share and a changed 13-week window, the correct threshold is 1,538.46 total cans/week, while the initial script still reported 769.23. Original 26-week outputs were correct | Corrected: configured window now used throughout; CSV includes window and generic headers. Independent isolated 13/26-week tests pass |
| Presentation clarification | CZK20,000/formula and CZK10,000/SKU are arbitrary comparison allowances | Data guide already labels them incomplete and explicitly notes Hardtank's advertised €3,000 recipe-development price can exceed them. Their purpose is scenario comparison, not adequate launch funding. A second flavour may also require separate recipe work | Retain a prominent inventory-only comparison; do not headline the CZK162,000 one-SKU subtotal as a launch budget. Actual full development/quality/regulatory costs remain unknown |
| Standalone brief clarification | A comparatively low total caffeine amount can still trigger the covered-beverage warning in a small pack | 40–60 mg in 250 ml calculates to 160–240 mg/L, above 150 mg/L. The linked safety memo correctly explains the warning and narrow coffee/tea naming exception; the brief leaves this to linked review | Add the concentration implication to the caffeine row so a reader cannot infer that 40–60 mg avoids warning requirements; final wording/classification remains [R,S] |
| Price-basis clarification | Price anchors should remain tied to the proposed 250 ml can | CZK49/250 ml = CZK196/L. The same CZK49 for 330 ml = CZK148.48/L; the smaller pack is 32% higher per litre despite identical checkout price | Keep price-per-can and pack volume together; disclose the 250 ml basis in model interpretation. The brief already acknowledges premium positioning versus observed 330 ml controls |
| Validation protocol improvement | Sequential tasting experiments could expose a participant to more than one serving if portions are not specified | The protocol requires safe/lawful samples but does not initially state total sample volumes or summed caffeine/active exposure across all tasting arms | Record small tasting volumes, maximum total active intake across samples, and participant eligibility in a qualified protocol before testing; do not have each participant consume multiple full cans simply to complete experimental cells |

These findings were sent to the lead for correction/integration and the resulting changes were reread. The correction history above records why the changes were made; this review does not confer product safety or legal approval.

## Independent calculation checks

All **258** existing scenarios were independently recomputed with decimal arithmetic using the input values, without executing the lead's model generator: **180 inventory + 24 trade + 54 DTC** rows. Selected computed fields matched the published CSVs within a rounding tolerance of 0.000051. This tests arithmetic and implementation, not the truth of assumptions.

At 6,000 cans per finished SKU, CZK22 manufacturing cost and 300 total cans/week:

| Structure | Inventory cash only | Initial illustrative fixed allowance | Slowest SKU clearance | Unsold after 26 weeks | Manufacturing value of unsold stock |
|---|---:|---:|---:|---:|---:|
| One formula, one flavour | CZK132,000 | CZK30,000 | 20.00 weeks | 0 | CZK0 |
| One formula, two flavours, 70/30 demand | CZK264,000 | CZK40,000 | 66.67 weeks | 4,200 | CZK92,400 |
| Two formulas, two occasions, 70/30 demand | CZK264,000 | CZK60,000 | 66.67 weeks | 4,200 | CZK92,400 |
| Three formulas, six SKUs, stated shares | CZK792,000 | CZK120,000 | 250.00 weeks | 28,200 | CZK620,400 |

The model appropriately holds total demand constant to isolate fragmentation. It does not establish that a broader range will maintain, increase or cannibalize real demand. Unserved demand after a SKU stocks out is not reassigned; clearance assumes its original demand rate continues. Unsold stock at the chosen useful selling-window endpoint is exposure, not an established expiry/write-off. Reorders, batch age, payment timing, receivables and full working capital are not modeled.

For CZK49 retail including 21% model VAT, CZK22 manufacturing cost, 35% retailer margin, 15% distributor margin and CZK2 trade variable cost:

- Net retail value = **CZK40.4959**.
- Brand sales direct to retailer = **CZK26.3223**; contribution = **CZK2.3223/can**.
- Brand sales through distributor = **CZK22.3740**; contribution = **−CZK1.6260/can**.

The implementation correctly treats the distributor margin sequentially rather than adding 35% and 15% together. Positive contribution is before acquisition/fixed costs and is not operating profit.

For CZK43 per can, CZK22 manufacturing cost and the stated order assumptions:

| Pack | Goods payment incl. VAT, one-off | Contribution before acquisition/fixed, one-off | Contribution with 10% subscription discount |
|---|---:|---:|---:|
| 6 cans | CZK258 | −CZK49.4913 | −CZK69.7422 |
| 12 cans | CZK516 | CZK21.0174 | −CZK19.4844 |
| 24 cans | CZK1,032 | CZK162.0347 | CZK81.0312 |

These figures use the **same hypothetical CZK90 brand-paid delivery and CZK30 pick/pack per order**. The model explicitly warns that real delivery weight bands and damage can differ. Thus the apparent 24-pack advantage is conditional, not a recommendation to maximize box size. The maximum first-order CAC field is a break-even ceiling before fixed costs; negative values mean no acquisition-spend headroom.

## Brief, scope and source-fit checks

- **Format pass:** recommended consumer product is a finished 250 ml can, challenged only by another can size. Bottled options remain qualifying comparisons. No powder, pouch, dilution product or non-liquid format is introduced as a consumer launch recommendation.
- **Portfolio pass:** one formula/one flavour is the explicit minimum; a second flavour requires incremental demand and its own sell-through. Evening and CBD alternatives are separate gates, not a required daily system. Subscription is deferred and does not imply daily dosing.
- **Dose/claim pass with clarification:** 40–60 mg caffeine is marked concept/bench work only. No final dose, alertness wording, nootropic effect or CBD efficacy is approved. The safety memo states the concentration rule and rejects treating scientific rationale as claim authorization. Final food category, source, tolerances and foreseeable combined intake remain open.
- **Nutrition pass:** 2.5 g sugars/100 ml correctly becomes 6.25 g/250 ml and supplies 25 kcal from sugars alone. The brief explicitly notes that its maximum sugar and maximum calorie targets may conflict once other energy-bearing ingredients enter. Sweetness and legal nutrition claims are not conflated.
- **Shelf-life pass:** nine months is labeled an aspiration requiring validation; the 26-week useful selling period is explicitly separate. Supplier shelf-life claims are not transferred to this formula.
- **MOQ/source-fit pass with limitation:** the guide correctly says 1,500/3,000/4,000/6,000/30,000 are bracketed examples from different advertised offerings, not interchangeable production quotes. The 1,500 Madison homepage banner conflicts with the dated 4,000-can pilot article; it must remain a low scenario, not a promised custom MOQ.
- **Cost/source-fit pass with limitation:** manufactured cost, margins, delivery, demand and share distributions are explicitly invented sensitivities, not quotations or measured preferences. Hardtank's recipe fee is supplier advertising; no currency conversion is used to manufacture a project budget.
- **VAT source fit:** the reviewer opened the [Czech GFŘ guidance effective 1 January 2024](https://www.financnisprava.cz/assets/cs/prilohy/d-seznam-dani/Informace_GFR_ke_zmenam_sazeb_DPH_od_1_1_2024.pdf) on 17 October 2026. It supports the standard-rate framework and specified beverage exceptions, while calling itself interpretive guidance. The model's final-product/current-law review caveat is appropriate; this review does not establish a new tax ruling.
- **Validation pass with improvement:** interviews and 24–36-person tasting work are labeled qualitative/directional rather than efficacy or representative market studies. The paid-repeat denominator/censoring instructions are appropriate, and no customer interviews or tests are falsely represented as completed. Add the cumulative tasting exposure controls noted above.

## Final recheck

The corrected generator was copied with its inputs into isolated temporary directories; no lead-authored inputs or outputs were changed by the reviewer. At **26 weeks**, all 180 inventory rows independently matched the expected window calculations and the resulting inventory CSV matched the saved deliverable byte-for-byte. At **13 weeks**, all 180 rows independently matched decimal calculations for required demand, remaining stock and manufacturing value at risk. The new `saleable_window_weeks` field correctly records each setting. Temporary files were removed after the check. The original independent checks of the other 78 trade/DTC rows remain valid because their arithmetic was unchanged.

The final brief explicitly states the **160–240 mg/L** implication for its **250 ml / 40–60 mg** bench comparison and ties its price tests to **250 ml**. The validation protocol now requires participant-suitability controls, each sample volume and cumulative actives/background intake; it explicitly rejects an implication that multiple prototypes require multiple full cans. The report's economics section presents inventory cash separately and labels fixed allowances and total subtotals incomplete assumptions, with a linked exclusions guide. Actual costs and launch cash need remain unknown.

**No unresolved publication blocker was found within this review's scope.** Pass means arithmetic and provisional framing are suitable for research publication. Product efficacy, customer demand, supplier availability, actual price/cost economics, ingredient legality and commercial release remain subject to the explicit gates in the brief and supporting assessments.
