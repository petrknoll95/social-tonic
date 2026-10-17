# Competitor data dictionary

Observation date: **2026-10-17**. The [consolidated CSV](competitor-matrix.csv) contains 52 country/SKU observations; the three workstream CSVs retain country-specific evidence. The [rendered matrix](../competitor-matrix.md) and [report](../report.md) interpret them. Source IDs resolve in [sources.csv](../sources.csv).

## Fields and interpretation

| Field(s) | Meaning |
|---|---|
| `record_id` | Stable research identifier. Different countries/variants are distinct observations, not necessarily unique brands. Missing numbers reflect excluded candidates, not missing records. |
| `country`, `eu_status`, `observation_date` | Market being examined, EU/non-EU status and access snapshot. Country is not manufacturing origin. A German-targeted cross-border offer remains classified as cross-border. |
| `brand`, `exact_sku`, `format`, `volume_ml` | Exact qualifying finished can/bottle; volume is one container. Historical sizes and sister products are not merged. |
| `benefit_segment`, `occasion`, `formulation_type` | Intended proposition/use and reported composition. These are not verified effects or cleared claims. |
| `caffeine_mg_per_container`, `cbd_mg_per_container` | Label/retailer amounts or explicit calculation, with conflicts retained. Text qualifiers are intentional. Unknown means uncollected or unresolved, not zero. “None declared” and “not listed” mean no declared ingredient in the reviewed evidence, not an assay. Ordinary unknown CBD cells do not imply CBD inclusion. |
| `price_local`, `currency`, `pack_units` | Observed total asking price for the stated pack and its local currency. Shipping excluded. Hospitality, promotion and unavailable offers remain labeled. |
| `price_per_container`, `price_basis` | Net beverage price per entire can/bottle, with deposit deductions only where explicitly included. The basis identifies regular/promotion, subscription exclusion, unit-rate derivation or unavailable catalogue evidence. Larger bottles are not equal portions to small cans. |
| `included_pack_deposit_local` | Explicit refundable deposit subtracted from the displayed pack price. Zero means no deduction documented, not proof no deposit exists. |
| `container_deposit_local` | Separate deposit per container where collected in the Czech dataset. Unknown elsewhere does not mean zero; consult `price_basis`. This is not a comprehensive national deposit-system map. |
| `availability_state`, `channel_type`, `distribution_evidence` | Exact observed route and stock state. Distinguishes mainstream/specialist, DTC, hospitality, cross-border and announcement/watchlist evidence. No checkout or national store census performed. |
| `local_scale_evidence` | Country/line/SKU-specific evidence or explicitly limited company/category proxies. Missing sales remain unknown. |
| `business_maturity` | Qualitative operating-history classification: established, emerging or unknown, with parent/new-line distinctions. Does not rate product success. |
| `brand_recognition_evidence` | Measured local recognition is unknown in all sampled rows. Longevity and retailer presence are visibility proxies only. |
| `evidence_quality`, `observation_confidence` | Original detailed assessment and normalized high/medium/low observation label. Neither scores efficacy, legal compliance or sales. |
| `source_ids`, `uncertainty`, `alcohol_abv` | Source cross-reference, limitations and ABV where collected. Unknown ABV is unresolved; the matrix does not imply every non-alcoholic beverage is 0.00%. |

## Price calculations

`price_per_container = (price_local − included_pack_deposit_local) ÷ pack_units`

Three explicit deposit deductions: DE03 €3 per 12-pack, DE07 €0.08 per bottle and PL05 PLN1 per bottle. Other separately stated deposits are additional cash at checkout. Examples: DE03 `(19.99−3)/12 = 1.4158`; DE07 `3.40−0.08 = 3.32`; PL05 `4.99−1 = 3.99`; CANS Balance `1049/24 = 43.7083`. Display prices use two decimals with half-up rounding; CSV precision follows the observed/calculated workstream values. No currency conversion or country price average is calculated.

Club-Mate CZ-C10 and Powerade CZ-C11 use sold-out catalogue unit rates, not executable in-stock prices. Czech Starbucks uses the latest 59.90 offer rather than the 70.90 reference. Austrian Gösser's 0.64 promotion is limited to 16–17 October 2026; it is not a durable regular-price anchor. Recheck before commercial decisions.

## Evidence normalization and scope

High means exact product/offer well supported, including a clearly unavailable offer. Medium flags material formula/version, stock, retrieval or price inconsistency. Low covers weak route confirmation such as cross-border-only, old announcement or indexed-menu evidence. Central workstream `B` direct listings map to high observation confidence; `C` maps to low. AT01 and Western rows with material formulation/availability qualifications are reduced to medium. Original wording remains available for audit.

All 52 rows pass the finished can/bottle format filter. Four UK/Swiss rows are references outside the EU total. Five rows declare CBD; one additional Swiss hemp-themed row has no quantified CBD and is not treated as a verified CBD drink. Listed ingredients and retailer claims are not legal clearance. The [regulatory memo](../supporting/regulatory-and-evidence-update.md) assesses CBD separately.

No national distribution, awareness, market-share or saturation estimate can be derived from row counts. Products missing from the sample, including a verified local dedicated sleep drink, remain coverage gaps. A source register is an evidence map, not an independent-source vote count; retailer/manufacturer claims may share their origin even at different URLs.
