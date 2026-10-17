# Reading the evidence registers

All final registers use UTF-8 CSV, one header row, decimal points and explicit currency/unit fields. `unknown` means not established, never zero. Observation cut-off is 17 October 2026; commercial event dates and measurement periods may be older or unresolved.

- **products.csv:** 39 SKU/history records, not 39 currently available sodas. Flavours are separate rows; multipacks are price options rather than new liquids. `scope_class` distinguishes primary sparkling drinks, adjacent formats and historical/excluded context. `current_status` preserves channel-specific detail; `status_normalized` is a conservative summary. A current offer does not verify delivery or physical inventory.
- **commercial-evidence.csv:** 34 observations, classified by evidence provenance. Publication by a journalist does not independently validate an embedded company assertion. One observation may cite several documents without becoming several independent corroborations. Unknown financials do not mean zero sales.
- **eu-availability.csv:** 39 country/channel/price observations, including non-EU UK/Swiss comparisons, substitutes and unresolved leads. It is not a count of products or stocked stores. Domestic retail, cross-border direct shipping and announced distribution remain distinct.
- **studies.csv:** 25 extractions covering original laboratory/human work, historical finished-product analysis, supplier/brand evidence and technical development. A study row is not necessarily an independent trial; multiple model conditions can come from one paper. No current finished-can shelf-life test was performed here.
- **economics-scenarios.csv:** three explicit illustrative price/headroom calculations. These are assumptions, not quotes, forecasts or validated margins.

## Dose, price and nutrition conventions

`serving_ml` is the reported serving/container volume, with rounding conflicts in `uncertainties`. `disclosed_amount_g` is the source's stated mass on `amount_basis`: compound, creatine equivalent or branded preparation. `creatine_equivalent_g` is populated only when a source expressly establishes it; a conditional supplier-composition calculation is not inserted as a verified label quantity.

`price_per_serving = price / pack_units`. `price_per_declared_g = price_per_serving / disclosed_amount_g`, using the explicit denominator. Thus a CreaBev price per declared preparation gram is **not** a price per active creatine gram. The separate equivalent-price field is unknown where the declared active basis is unresolved. Availability rows can use a different but explicitly named denominator; Humble+'s product row uses 3.4 g monohydrate, while its availability comparison uses the label's 3 g creatine equivalent.

Prices use original currencies. Deposit and delivery treatment is in the shipping fields; no FX comparison is implied. Current discounts, regular prices, introductory subscriptions and subsequent subscriptions are distinguished. Nutrition is per reported serving; declarations and contradictions are retained without presenting them as independent analysis. Unknown caffeine is not silently converted to zero.

## Traceability and limits

`source_ids` joins to [the source register](../sources.csv). P, E, T and L identify discovery workstreams, not evidence grades. Source entries retain access method, date, provenance, supported claims and limitations. `same_url_as_source_id` flags repeated URLs across workstreams; different URLs can still repeat one underlying announcement. The [methods](../supporting/methods-and-evidence-audit.md) and [independent challenge](../supporting/independent-evidence-audit.md) document source-chain and interpretation checks.

The `*-workstream.csv` files preserve agent inputs; final registers reconcile their schemas and add the lead's integration. No values imply completed purchases, customer validation, recipe validation or laboratory work.
