# Shared coding and inclusion framework

Defined before pattern analysis on 17 October 2026. This is a purposive mechanism-and-status sample, not a market census or a matched outcome study. Target: 48 names, 12 non-beverage consumer brands and 36 beverage brands. Include established scale/longevity, emerging documented commercial traction, active offers of unknown scale, discontinued or renamed names. Keep UK separate from EU. Select category and naming diversity before counting; no selection based on a preferred name style. Exclude powder-only functional brands from beverage count. A legacy beverage masterbrand is eligible with its historical status explicitly stated. Company or portfolio revenue cannot be assigned to an individual SKU.

## Deliverable JSON contracts

Each workstream writes its own JSON object with arrays `brands`, `evidence`, `sources`. Lead merges into CSV; no agent edits shared files, index, or git.

Brand keys (all strings unless otherwise noted): `brand_id`, `brand_name`, `sample_group` (beverage/non_beverage), `name_level` (masterbrand/product_family/legacy_masterbrand), `category`, `principal_market`, `market_region` (US/EU/UK/global/other), `original_language`, `primary_name_type`, `secondary_name_types`, `semantic_territory`, `word_count` (integer), `character_count` (integer, Unicode code points including spaces and punctuation), `syllable_count` (integer or blank for ambiguous), `pronunciation_spelling`, `literal_meaning_associations`, `promise_anchor` (ingredient/benefit/occasion/identity/none/mixed), `tone`, `descriptor`, `descriptor_independence` (category_clear/category_partial/category_opaque; analyst judgment), `name_origin`, `origin_evidence` (documented/unverified/interpretation_only), `commercial_status` (established/emerging_traction/active_scale_unknown/discontinued/renamed/struggling), `channel_history`, `architecture_expansion`, `source_ids` (semicolon-separated), `coding_notes`.

Primary name types: descriptive, benefit_led, suggestive, arbitrary_real_word, invented, compound, founder_personal, place_based, emotional_occasion, provocative, ingredient_led, metaphor_cultural. Exactly one dominant analyst code; secondary codes retain ambiguity. Origin language can be unknown; a resemblance to a language is not evidence of origin. Store stylisation as rendered in official heading/text; explain if wordmark differs. Syllables use stated market-language reading; leave blank when unclear. Semantic/tone coding is interpretation, not consumer evidence.

Evidence keys: `evidence_id`, `brand_id`, `indicator_type` (revenue/retail_sales/units/growth/distribution/longevity/availability/acquisition/closure/rename/retention/awareness/other), `claim`, `value`, `unit`, `geography`, `period`, `publication_date`, `provenance` (company_report/filing/independent_reporting/retailer_observation/official_history), `source_id`, `source_url`, `limitations`. At least one row per brand. Funding/valuation is context only and cannot justify commercial success. Acquisition ≠ consumer retention. Current offer ≠ scale. Absence of data ≠ failure.

Source keys: `source_id`, `title`, `url`, `publisher`, `publication_date` (date/year/undated), `accessed_date` (2026-10-17), `source_type`, `access_level` (full_text/abstract/publisher_summary/search_excerpt/partial_page), `supported_claims`, `limitations`. Use prefixes EMP (empirical), CON (consumer), BEV (beverages), LEG (legal/language), LEAD (lead). Browse actual sources; precise metrics need text or explicit downgrade. No invented etymologies, current-state assumptions or causality. Unknown must stay unknown.

## Planned names

Non-beverage: Apple, Amazon, IKEA, Nike, Patagonia, Dove, Oatly is reserved for beverage; instead consumer list includes Warby Parker, Dollar Shave Club, Spanx, Casper, Glossier, Away (12 total).

Beverage delegated sample (24): OLIPOP, poppi, Culture Pop, Hiyo, Recess, Kin Euphorics, Ghia, De Soi, TRIP, Daytrip, DASH, TÖST, Seedlip, Three Spirit, Pentire, Botivo, Leilo, Taika, CANS, PRAGER'S, Vilgain, Club-Mate, fritz-kola, Ugly Drinks.

Beverage lead sample (12): Coca-Cola, Pepsi, Red Bull, Monster, CELSIUS, Liquid Death, Kofola, Birell, innocent, Oatly, Sierra Mist, ZICO.

No final brand names will be generated. Pattern counts are descriptive of this selected sample only. An independent reviewer will challenge source chains, status classification, survivorship bias, etymology and causal language before finalisation.
