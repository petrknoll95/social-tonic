# Data and reproducible model

**Research date: 17 October 2026.** EUR amounts are manufacturer/brand planning receipts, not consumer market value or profit. No currency conversion of national consumer prices is performed. All scenario inputs are explicit hypotheses; none is measured demand for the proposed drink.

## Files

- [Population context](population-context.csv): Eurostat `demo_pjan`, both sexes, 1 January 2025. Adults = total minus ages under 1 through 17 and unknown age. Unknown-age counts are zero. 2025 is the common age-specific reference, not an assertion of October 2026 population. Dataset updated 25 September 2026. The country-specific API URL is saved in every row.
- [Spending context](spending-context.csv): Eurostat `prc_ppp_ind_1`, 2025, A01 actual individual consumption volume per capita and A010102 non-alcoholic beverage price levels, EU27=100. Latest retrieved dataset update 9 July 2026; 2025 estimates remain preliminary. AIC includes publicly provided consumption; beverage prices include other delivery forms. Neither is an RTD benchmark or willingness-to-pay measure.
- [Inputs](model-inputs.json): complete scenario and score parameters.
- [Country scorecard](country-scorecard.csv): operating factors, 45 possible weighted points, also rescaled to 100 for readability.
- [Category–country scorecard](category-country-scorecard.csv): 30 alternatives, including qualified reach and first/repeat buyers.
- [Demand scenarios](demand-scenarios.csv): 90 alternatives (5 countries × 6 benefits × 3 scenarios), not additive.
- [Demand sensitivity](sensitivity.csv), [contribution sensitivity](contribution-sensitivity.csv), [weight sensitivity](weight-sensitivity.csv), [score sensitivity](score-sensitivity.csv), [country cost sensitivity](country-economics-sensitivity.csv).
- [Recalculation script](recalculate.py): run `python3 data/recalculate.py` from this topic directory; standard library only, no network or paid dependencies. Rewrites derived CSVs, not evidence files. Assertions check arithmetic and cohort constraints.

## Reach construction and definitions

Every country's `reach` tuple is `[planned venues, unique eligible adults per venue over the horizon, unique eligible digital adults, cross-channel duplicate adults]`. Venue counts, exposures and deduplication are assumptions with **zero contracted venues/audience demonstrated by this research**. Venue contacts are expected unique adults after within/across-venue deduplication, not visits or footfall. Digital counts are intended unique adults exposed to a priced offer, not impressions, followers, clicks or signups. Adults are 18+ and screened for the proposed product's suitability; no child audience is included. Qualification then requires a relevant recent occasion, not a stated intention to buy.

`U = venues × adults_per_venue + digital_adults − cross_channel_duplicates`

`R = U × occasion_qualification`

`B = R × paid_trial_rate`

`P = B × repeat_buyer_rate`

`Units = B × first_purchase_units + P × repeat_orders × units_per_repeat_order`

`Net revenue = Units × net_price_per_unit`

`B` includes every first paid buyer once. `P` is a subset, not additional customers. Repeat orders exclude the first purchase. Frequency is the **mean number of repeat orders actually occurring before month 12 per repeater**, already discounted for staggered recruitment and attrition. It is not a full 12-month lifetime assigned to a customer acquired in month 11. Sales to a retailer are not counted again when the final consumer buys. Model assumes all paid units are consumed by their purchaser; gifts/sharing can break that identity and must be measured.

## Assumption rationale and limits

| Input | Why the planning range is used | How to replace it |
|---|---|---|
| Venue count and unique reach | Small city-level manual route versus a larger operational stretch; Czech base highest because founder is local. No actual network supplied. | Named eligible outlet inventory, access decisions, measured deduplicated adult exposures and cost. |
| Focus qualification 60%; energy 75%; social 40%; sleep 20%; hydration 45%; gut 35% | Deliberately broad **hypotheses** about overlap within an already selected beverage-occasion audience. Not national prevalence or survey estimates. | Screen recent behaviour before displaying concepts. |
| Trial 4/8/12% | Conversion stress range for a relevant, exposed adult offered a priced product; inappropriate for raw ad impressions. | Actual paid choices with a no-purchase option. |
| Repeat 20/35/50% | Unknown probability of at least one additional paid purchase within the horizon. Not derived from US brands. | Mature, uniquely identified paid cohorts; separate 30/60/90-day outcomes. |
| Repeat orders 3/6/10; units 4/6/8 | Hypothetical single-unit/pack mix over the remaining horizon; channels are blended for initial simplicity. | Channel-specific consumer orders, not wholesale cases, and realised time at risk. |
| First units 1/2/3 | Low case approximates singles; base/high mixed single and multipack baskets. All servings are whole cans/bottles. | Actual basket size; do not assume a six-pack is six independent buyers. |
| Country net prices | Hypothetical realised brand receipts; higher AT/DE/NL cases reflect price context, not validated premium acceptance. | Separate DTC/wholesale contract terms, promotions, returns, taxes and fees. |
| Benefit price factors | Energy 0.8; focus/gut 1.0; social 1.1; sleep 1.15; hydration 0.85. Tests whether differing achievable price could matter. | Blind taste plus priced choice by exact can/bottle. |
| Same conversion/repeat/frequency across categories | A neutral comparison to isolate reach and price; **not** evidence of equal category behaviour. Different category repeat is unknown. | Separate category paid cohorts; do not borrow focus repeat for sleep. |

Different reach and price assumptions mean these are **founder-operable scenarios**, not equal-spend experiments. There is no supplied fixed budget and no cost-per-qualified-adult evidence. The high case needs more channel work and working capital than base. A later equal-budget country test should measure cost per paid first buyer and contribution per repeat buyer.

## Net price and contribution boundary

Net price excludes VAT, refundable deposits, consumer shipping charged separately, retailer/distributor margin and trade discounts/returns. Product levies and nonrefundable packaging fees belong in variable costs; avoid subtracting them twice. Model values are assumptions **after channel deductions**, not retailer shelf prices. DTC fulfilment, freight subsidy, production, can/label/carton, levies, packaging fees and expected wastage must be included in variable cost. Acquisition, founder time and fixed development/registration/compliance costs remain outside gross contribution.

The contribution grid uses Czech base volume and variable-cost hypotheses of €0.70/€0.85/€1.05 per can against net €0.85/€1.10/€1.35. These are **not supplier quotes**. €15,000 is an illustrative fixed-cost hurdle, not a prescribed budget. At €0.25 contribution per unit, 60,000 units cover that hurdle before acquisition/founder pay; base volume provides only €2,453 and €3.65 per acquired buyer. It would be misleading to call base revenue a viable business.

Low/base/high are joint stress scenarios, not percentiles or confidence intervals. Changing one variable while holding others fixed ignores elasticity, stock availability and correlated behaviour. The one-way sensitivity is useful for deciding what to measure, not predicting an independent response to each lever.

## Deduplication across benefits and countries

The six qualification fractions sum to 2.75; this intentionally permits adults to have several needs. **Never sum category reach, buyers or revenue.** For example Czech base focus reach 8,400 and social reach 5,600 have an unknown union between 8,400 and 14,000 (the common pool cap). A hypothetical 50% overlap of the smaller pool gives 11,200 unique adults; it is an illustration, not measured overlap. A multi-SKU launch requires a customer-level overlap table and allocation of a finite beverage budget/occasion count; this model authorizes no portfolio sum.

Countries are alternative launch plans too. A traveler or cross-border shopper must be assigned one acquisition market in an actual CRM. Population ceilings are not customer lists. Retain consented, pseudonymous customer IDs in future fieldwork; no customer personal data is stored here.

## Channel receipt worksheet before a commercial decision

Record each country/channel separately: displayed consumer price including VAT and deposit; subtract refundable deposit; divide by one plus the applicable VAT rate; apply retailer margin and any distributor margin on clearly specified bases; subtract promotion/returns allowances to obtain brand net receipt. For DTC, separate shipping charged from shipping cost, payment/marketplace fees and fulfilment; for B2B, use the signed net invoice terms rather than assumed shelf-price margins. Weight country receipts by **sold units** in each channel and singles/pack mix. Then subtract exact landed production, handling, levies, packaging fees and waste. No actual rates, channel splits, invoices or quotes exist yet.

The country cost table now consumes the country cost assumptions explicitly. All are placeholders, not estimates of achieved cost. Focus/energy revenue equality is constructed by offsetting reach qualification and price factors, so it must never be interpreted as an empirical tie. The base scenario is 86.3% repeat units; a monthly acquisition/cohort schedule must replace the aggregate horizon assumption before buying production inventory.
