# Signal data guide

[signals.csv](signals.csv) contains **44 developments or dated competitive observations**, researched on **17 October 2026**. It is a purposive intelligence sample, not an exhaustive market census or a count of independent successful products.

- **Dates:** `event_date` states what happened or was planned; `publication_date` records coverage; `original_product_launch_date` prevents relabeling older products; `observed_date` is this review's access date. Text qualifiers are intentional where a precise day is unknown. A recent observation is not a recent launch.
- **Format:** `verified_can_bottle_format` identifies the qualifying liquid. Mixed-format financial evidence is explicitly bounded; excluded company products do not enter the liquid universe.
- **Sources:** original and corroborating IDs resolve to [sources.csv](../sources.csv), with direct URLs in the tracker. A corroborating link may verify a label or chronology rather than independently verify sales. An inaccessible original can be retained for metadata only, with an accessible account separately linked.
- **Evidence:** `evidence_type` and `confidence` concern the stated fact, not product efficacy. `limitations` preserves ambiguity, forecast status, incomplete access and broader revenue scope.
- **Interpretation:** `commercial_significance` and `eu_relevance` are analyst judgments unless a measured disclosure is explicitly identified. They are not market-size estimates, formula approvals or guarantees of demand.
- **Deduplication:** `shared_event_group` groups coordinated announcements. `independent_company_group` prevents multiple Hiyo events, for example, becoming independent-company trend observations. One company can contribute several legitimately distinct developments.
- **Prices:** snapshots and announced SRPs are not transaction averages, historical trends or Czech price validation. Unknown values are stated rather than filled by inference.
- **Recency:** refers to publication unless otherwise specified. Older measured sales disclosed recently remain dated to their actual reporting period.

Source aliases preserve IDs used in the report after URL deduplication. Repeated URLs, syndication and related publications do not create additional independent evidence. The report supplies the higher-level distinction between an isolated announcement, a recurring cross-company pattern and commercial validation.
