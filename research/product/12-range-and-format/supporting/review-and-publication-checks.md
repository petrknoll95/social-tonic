# Review resolutions and publication checks

**17 October 2026.** This record distinguishes research quality checks from product validation. No formula, claim, consumer test or supplier has been approved by this exercise.

## Independent reviews actually performed

- [Model and brief review](independent-model-and-brief-review.md): the operations agent independently audited lead-authored calculations, brief and validation protocol. All 258 original outputs recomputed with Decimal matched rounding. A configurable-window defect was identified and corrected; isolated 13- and 26-week reruns verified the fix. The reviewer did not count its own operations memo as an independent review.
- [Evidence review](independent-evidence-review.md): the safety agent audited the lead's synthesis, dose/claim treatment, format compliance and citations, excluding its own safety memo from the independent-review claim.
- [Portfolio review](independent-portfolio-review.md): the benchmark agent audited the lead's attribution, exact-product use and provisional brief, excluding its own source memo from the independence claim.

The lead also inspected all three workstream outputs and checked the key scientific/legal sources, local price pages, source IDs, local links and final arithmetic. These reviews are editorial/evidence checks, not external certification.

## Corrections and disagreements resolved

| Finding | Resolution |
|---|---|
| Inventory model hardcoded 26 weeks in one formula despite configurable input | All inventory calculations now use the configured window; output includes the window and generic end-of-window column names. Independently checked at 13/26 weeks. |
| Brief did not explicitly connect its caffeine range to 250 ml warning concentration | Added 40–60 mg/250 ml =160–240 mg/l and the covered-beverage warning implication; no final dose or label approved. |
| Single-can price test could be read without volume | Specified 250 ml in the brief; report explicitly compares premium against observed 330 ml controls. |
| Repeated tasting arms could accumulate untracked exposure | Protocol now records sample volumes and total actives, including background intake, under a qualified suitability/safety procedure. |
| Two report URLs were not the verified source URLs | Replaced SLY and Gatorade links with exact PB17/PB22 URLs and checked master-register membership. |
| VYBES current bottle closure/resealability was not verified | Removed report inference and set dataset field to unknown. Generic bottle/closure comparisons remain design options. |
| Neutonic old/new ingredient disclosures could be misread as proven reformulation | Report now states disclosures differ and reconciliation is unknown; no new formula is assigned to Orange Sunrise. |
| Hiyo case volume might be interpreted as US-only sales | Added geographic split unknown, alongside unknown case size and reporting window; no can/revenue conversion. |
| Halfday range event might become an exact-SKU launch date | Explicitly distinguishes 2026 slim-can range launch from unknown exact Tropical date. |
| Earlier Daytrip flyer could not be refetched | Recorded 404 limitation; current unavailable CBD offer is historical/source-reconciliation context, not a current sold-product benchmark or traction observation. |
| Madison public pilot/bottle minimums conflict across pages | Retained discrepancy and dated 4,000±10% pilot example, without claiming project-specific availability. |
| Illustrative fixed costs could be mistaken for a full launch budget | Report/model guide identify incomplete allowances and inventory-only cash separately; development, testing and other launch costs remain unknown. |
| Newer CBD and ingredient decisions qualify earlier research | Exact 2026 source/material/use distinctions retained; supplement opinions are not RTD authorization and botanical claims need separate review. |

## Reproducibility and file integrity

Pre-publication checks cover: required files; relative Markdown links within the repository; CSV header/row consistency;69 unique source IDs and dated access/geography fields; source-ID references in benchmark/packaging datasets; all report external URLs present in the master source register; JSON parsing; deterministic model regeneration; whitespace/diff checks; no source-document copies, credentials or transient logs introduced. The model includes 180 inventory,24 trade and 54 DTC scenarios. The source count is records, not unique domains or proof of 69 independent studies.

The lead normalised CSV line endings only inside this new topic. Some external sites limit automated access and one older flyer no longer resolves; such limitations are disclosed rather than disguised as full-text verification. Not every URL was subjected to an automated HTTP-status sweep; direct browsing and reviewer spot checks support the cited claims.

## Repository and publication procedure

The supplied remote establishes `petrknoll95/social-tonic`. Initial concurrent work was preserved via a managed isolated worktree. Before final review, current main `d6124de` was integrated, including topic 06. Only `research/product/12-range-and-format/` and the topic 12 row in `research/README.md` are included in this research commit. Further remote updates are integrated before pushing; no force push, repository duplication or visibility change is used.

Remote commit/file verification is performed after push and reported with exact GitHub links in the completion message. This file records the checks and method without claiming that a yet-unpushed commit is already remote. If direct main push is blocked by protection, the fallback is a dedicated branch and pull request, not bypassing protection.
