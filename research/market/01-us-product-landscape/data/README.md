# Dataset guide

All product records have a research date of **2026-10-17** and US geographic scope. CSV files are UTF-8 with headers. Missing information is written as `unknown` or an explanatory string; it is not zero. Some fields therefore deliberately contain text rather than a number.

## Files

- [product-landscape.csv](product-landscape.csv): normalized master, 31 records, one row per exact product/variant or explicitly named retail assortment. This is the preferred file for comparison.
- [focus-energy.csv](focus-energy.csv), [relax-sleep-cbd.csv](relax-sleep-cbd.csv), [secondary-categories.csv](secondary-categories.csv): original workstream detail, with accepted review corrections applied. Different schemas preserve workstream-specific evidence. They are not additional products to add to the master count.

## Master fields

| Field(s) | Meaning |
|---|---|
| `product_id` | Stable FE, RS or SEC ID; do not count a crossover twice. |
| `research_date`, `market` | Observation cut-off and geographic scope. |
| `brand`, `exact_sku` | Exact flavor/formula/size or named assortment; brand-level figures are not assumed to belong to this SKU. |
| `primary_category`, `secondary_category` | Positioning taxonomy, not established effects. |
| `cohort` | `recent event`, `contextual comparator`, `announced / preorder`, or `discontinued predecessor`. |
| `recent_event_type`, `original_launch`, `event_2025_2026` | Original chronology separated from the reason for recent relevance. Unknown flavor dates are not filled from brand dates. |
| `commercial_status` | Documentary sale/listing evidence and stock/fulfillment caveats. Listed/orderable is not observed paid sales. |
| `format`, `volume_ml`, `serving_basis` | Finished can/bottle only. Nominal ml where verified; otherwise approximate US fl oz conversions. The original oz size takes priority over artificial conversion precision. Historical VYBES volume is unknown. |
| `caffeine_mg_per_container` | Milligrams per complete can/bottle when disclosed. Text retains uncertainty. No listed caffeine ingredient is not an analytical zero. |
| `stimulant_approach` | Distinguishes caffeine-containing, caffeine-free and paraxanthine. Caffeine-free does not establish absence of all stimulation. |
| `cannabinoid_status`, `cbd_mg_per_container`, `thc_status` | Brand/label declarations and verification limits. No cannabinoid ingredient listed is not a batch assay. Less-than-0.3% THC does not establish zero THC per can or EU compliance. |
| `ingredients_disclosed_doses` | Ingredient identity and disclosed amounts, including unknowns. Proprietary-blend totals are not individual doses. Gatorade label serving amounts are explicitly separate from scaled whole-bottle estimates. |
| `price_usd_per_container`, `price_basis` | US dollars per complete can/bottle; pack division, retailer, promotion and stock caveats. No FX conversion, weighted average or Czech price prediction. Unknown prices remain unknown. |
| `claimed_experience`, `claimed_onset_duration`, `target_occasion` | Brand claims/usage instructions. A before-bed usage time is not measured onset. |
| `distribution`, `commercial_evidence` | Channel evidence plus scope/attribution. Funding, enterprise value, planned doors, retail authorization, shipments and sell-through remain distinct. |
| `confidence`, `gaps` | Support for documentary facts, with unresolved issues; never a numerical efficacy rating. |
| `source_ids` | Semicolon-separated keys into [sources.csv](../sources.csv). |
| `product_url` | Exact product or retail page where recoverable; otherwise a dated launch/historical reference. Does not certify current fulfillment. |

## Price and unit handling

Workstream prices may be rounded to cents; the secondary dataset retains exact pack division to four decimals. Display tables round to two decimals. Hiyo $44.99/12 is $3.75 rounded, despite a $3.74 page widget; Blue Bear $47.99/12 rounds to $4.00. UPDATE $21.98/12 rounds to $1.83. Mixed-pack pricing is explicitly marked and is not an exact standalone-flavor price. Unreproduced CSE promotional pricing was removed in review.

Gatorade's 28 oz bottle contains 28/12 label servings: displayed whole-bottle figures are approximate arithmetic, not an assay. Do not treat retailer nutrient snippets for smaller servings as the full bottle. Ingredient extracts with equal mass need not have equal potency.
