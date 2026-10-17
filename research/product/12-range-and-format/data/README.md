# Datasets and reproducible models

**17 October 2026. All model values are explicit scenarios, not supplier quotes, measured demand, approved doses or a launch budget.** Currency is CZK; costs and contribution are ex VAT unless stated. The model assumes a VAT-registered business able to recover relevant input VAT; founder registration and actual tax treatment remain to be checked.

## Files

- [RTD benchmarks](rtd-benchmarks.csv): exact US can/bottle examples, with dates, scope and unknowns; maintained separately from customer hypotheses.
- [Packaging options](packaging-options.csv): material/portion/process choices and evidence limits.
- [Inputs](model-inputs.json) and [recalculation script](recalculate.py): Python standard library; run `python3 research/product/12-range-and-format/data/recalculate.py` from the repository root.
- [Inventory sensitivity](inventory-sensitivity.csv): 180 scenarios, four range structures × five run sizes × three costs × three demand rates.
- [Trade economics](trade-economics-sensitivity.csv): 24 scenarios, four retail prices × three costs × two routes.
- [DTC pack economics](dtc-pack-sensitivity.csv): 54 scenarios, three unit prices × three packs × three costs × one-off/subscription.

## Input provenance and limits

The run-size scenarios of 1,500 / 3,000 / 4,000 / 6,000 / 30,000 bracket published European examples discussed in [operations](../supporting/packaging-and-operations.md). They do **not** imply the same manufacturer, recipe, packaging or process is available at every size. In particular, a standard-recipe minimum does not establish a custom-formula minimum. The 6,000 base is a stress-test point, not a production instruction.

All cost figures are analyst sensitivity assumptions: manufactured filled/decorated can 16/22/30, incremental formula allowance 20,000, SKU setup allowance 10,000, retail margin 35%, distributor margin 15%, trade logistics/allowance 2 per can, DTC payment 2.5% of goods revenue including VAT, pick/pack 30 per order, brand-paid delivery 90 per order, damage/refund reserve 2% of ex-VAT sales. None is a quote or market average. Fixed allowances are especially incomplete: the published Hardtank recipe-development price alone can exceed them; no currency conversion is used to imply equivalence. Freight to warehouse, extended storage, full development/stability/regulatory work, insurance, working-capital timing, salaries, marketing, financing and applicable packaging/deposit administration are not fully priced. This is a comparison subtotal, never total cash required to launch.

Model VAT is 21%, consistent with the Czech GFŘ guidance for ordinary non-exempt beverages; verify the final product, registration and current law before pricing. [Official guidance, effective 1 January 2024](https://www.financnisprava.cz/assets/cs/prilohy/d-seznam-dani/Informace_GFR_ke_zmenam_sazeb_DPH_od_1_1_2024.pdf), accessed 17 October 2026. Other launch markets require different tax/packaging inputs.

Demand of 100/300/600 total cans per week is **unobserved**, held constant across architectures to isolate fragmentation. Two-SKU shares of 70/30 and six-SKU shares of 35/15/20/10/12/8 are invented planning scenarios explicitly labeled as such, not predicted flavor preferences. In real life extra choice might grow or cannibalize demand. The saleable window of 26 weeks is an assumption about useful selling time **after** manufacturing/logistics and channel residual-life requirements; it is not a measured shelf life. Unsold stock after that window is exposure, not an asserted write-off.

## Equations

- Initial cans = run per finished SKU × SKU count. Inventory cash = initial cans × manufactured cost.
- Fixed allowance = formula count × formula allowance + SKU count × SKU allowance. Model cash subtotal = inventory cash + fixed allowance.
- Slowest-SKU clearance weeks = run per SKU / (total weekly demand × smallest SKU share).
- Required total weekly demand within a window = run per SKU / (window weeks × smallest SKU share).
- Unsold at window end = sum over SKUs of max(0, run − total weekly demand × SKU share × window).
- Trade brand net sales = retail price / (1 + VAT) × (1 − retailer margin), multiplied by (1 − distributor margin) only on the distributor route. Margins are sequential percentages of each buyer's selling value, not markups and not added together.
- Trade contribution = brand net sales − manufactured cost − trade variable cost.
- DTC contribution = goods revenue ex VAT − manufactured units cost − payment fee on gross goods sales − reserve on net sales − pick/pack − brand-paid delivery. Subscription reduces the gross goods price by 10% before these calculations.

A negative CAC-headroom value is a loss before any acquisition spend, not a permissible negative advertising budget. Positive headroom is an arithmetic break-even ceiling, not a sensible acquisition target. Contribution excludes fixed costs; no lifetime value is inferred from subscriptions. The same 90-CZK delivery assumption across packs isolates pack-size effects; actual weight bands and packaging damage must replace it. Buyer-paid delivery reduces the brand's net delivery burden but may reduce conversion.

Architecture B (one caffeine-free evening formula) has the same SKU-count structure as A; its actual costs, demand and formula allowances may differ. It does not inherit A's economics without new inputs. These datasets contain no efficacy or demand measurements.
