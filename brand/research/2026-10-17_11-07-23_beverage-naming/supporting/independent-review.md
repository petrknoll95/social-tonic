# Independent methodology and evidence review

**Reviewer:** language/legal workstream agent, reviewing the lead and empirical agents' work. This is an independent internal review of other agents' reasoning, not independent consumer research or an external legal opinion. No source authored by this reviewer is treated as independently validated by this review.

**First-pass snapshot:** 17 October 2026, approximately 11:12:48 Europe/Prague (UTC+02:00). The report and beverage workstream were not yet present. Later passes and resolutions must be recorded below; this first pass is not sign-off on unseen files.

## Reviewed versions

Paths are relative to this research folder. SHA-256 identifies the file snapshot; subsequent edits may intentionally change it.

| File | Snapshot SHA-256 |
|---|---|
| `supporting/coding-framework.md` | `30a7674bca1638f4de3d4fef387575a3d1e4f3494bce7db4aecbeee4f26c7ac3` |
| `supporting/naming-brief.md` | `1f70adfab4f8f327fa9d2f948221f7c3ed58d81da237de316e9b7a0c49a72fc5` |
| `supporting/evaluation-and-testing.md` | `55763506ce4cd8d7dbf74ac6bc0673cfe692346f96737ce77e12210f9819d212` |
| `supporting/workstreams/lead.json` | `24a4abf95b50ca3088c6a2f1b4dc89a957be4ab794f5383027f637bf84d8b4d1` |
| `supporting/workstreams/empirical.json` | `142db2e802ed31b0103a7a220a2c4a303f28572b0ac2ef06504e6808af398178` |

Coverage: 24 coded brands, 37 commercial evidence rows and 63 source records available in the two JSON files. The reviewer inspected coding, origin confidence, metric scope, channel language, proposed tests, and sample design. A structural check found no character-count mismatch, whitespace word-count mismatch, duplicate source ID within either file, or missing brand-to-source reference in these files. Source references and numeric statements were spot-checked rather than every URL being reread.

## Actionable first-pass findings

| ID | Priority | Finding and required action | First-pass status |
|---|---|---|---|
| R01 | Required before pattern interpretation | The framework names statuses but lacks operational definitions. State that established can rest on documented longevity/scale and does not establish profit or retention. Describe emerging traction and current unknown explicitly. Keep historical and current outcomes separate. Do not call all established rows a matched successful cohort. | Sent to lead; final report/methods pending. |
| R02 | Required origin-label correction | Liquid Death has `origin_evidence=documented`, but its `name_origin` describes a founder entertainment/positioning account rather than the act of choosing the name. A documented positioning intention is not automatically a documented name origin. Downgrade the origin flag or add a specific origin source/wording. | Sent to lead. |
| R03 | Required provenance consistency | Dollar Shave Club CONE10 labels the $152m revenue as `independent_reporting` while its claim/limitations explicitly say the reporter repeated a company release. Consistently label the underlying metric company-reported, or explain that the provenance field denotes publication venue and preserve an explicit company-origin flag. Do not count it as independently measured revenue. | Lead action requested. |
| R04 | Recommended testing improvement | Audio first exposure uses “Yesterday I tried [name]”, while visual first exposure has only the name. This primes a product-use frame and can contaminate cross-arm category comparisons. Use isolated name audio first or the same neutral context in both arms; reserve realistic recommendation sentences for a separate ecological task. | Sent to lead. |
| R05 | Required source-access qualification if retained | Reopening `https://www.pepsi.com/faq` redirected this reviewer to `https://www.pepsi.de/`, which contains product listings but no Pep Kola origin account. Earlier successful retrieval may differ by location/time. Preserve the lead's exact retrieved passage or add a redirect caveat and fall back to the separately documented 1898 Pepsi-Cola rename. Do not pretend this independent check confirmed the etymology. | Sent to lead; access discrepancy, not demonstrated factual contradiction. |
| R06 | Required count labels | `founder_personal` includes a personal-name form with unknown origin (Casper), and secondary coding includes fictional characters (Warby Parker) and a goddess (Nike). Any summary must call this the combined personal-name/founder category and distinguish actual founder names. Similarly, `original_language` sometimes describes the form used in the market rather than documented etymology. Explain this before counting languages/origins. | Final report/methods pending. |
| R07 | Required scope language | Some planned alcohol-alternative brands also sell bottles intended for mixing. Their architecture can be relevant, but report explicit RTD versus mixer/aperitif scope instead of implying every sampled offer is a directly comparable ready-to-drink can. Keep non-beverage and beverage counts separate. | Beverage records not yet available. |
| R08 | Required reporting caveat | `descriptor` combines verbatim offer labels with analyst category/architecture summaries in some consumer rows. Mark which is which and do not count this as measured descriptor effectiveness. `descriptor_independence` is analyst expectation for an unfamiliar observer, not observed recognition among consumers already familiar with Apple or Nike. | Existing coding notes are good; carry into methods/report. |

## Independent source spot checks

- **Red Bull:** official FAQ confirms 13.969 billion worldwide cans in 2025. This supports the recorded company-reported unit indicator, not recognition, loyalty or a name effect. [LEAD004](https://www.redbull.com/ca-en/energydrink/questions/how-many-cans-does-red-bull-sell-world-wide).
- **Monster:** the official 26 February 2026 release expressly puts Monster, Reign and Bang in the $1.99bn Q4 2025 Monster Energy Drinks segment. The dataset's multi-brand limitation is correct and must stay next to any quoted number. It is not Monster-only sales. [LEAD006](https://investors.monsterbevcorp.com/news-releases/news-release-details/monster-beverage-reports-2025-fourth-quarter-and-full-year).
- **Warby Parker:** the SEC exhibit confirms FY2025 $871.9m revenue, 323 year-end stores, and $1.6m full-year net income. The company culture page confirms the Kerouac-character combination, so it must not be recast as founders' surnames. [CON011](https://www.sec.gov/Archives/edgar/data/1504776/000150477626000003/warbyparkerincearningsrele.htm), [CON012](https://www.warbyparker.com/culture).
- **Liquid Death UK:** the trade report confirms the announced 2025 withdrawal, a company manufacturing explanation and £2m UK NIQ sales for the year ended 7 September 2024. Its additional suggestions that aggressive branding or national humour caused the result are commentator/competitor opinion, not demonstrated causes. The dataset appropriately does not adopt those explanations. Do not generalise a UK withdrawal to EU rejection or current global closure. [LEAD011](https://www.foodmanufacture.co.uk/Article/2025/02/10/liquid-death-exiting-uk-less-than-2-years-since-debut/).
- **innocent:** the current owner page itself says full Coca-Cola ownership in 2013. The dataset accurately attributes this company account. Acquisition is not proof of current profit or retention. [LEAD016](https://www.innocentdrinks.co.uk/our-owner).
- **2026 name-length paper:** the VUB abstract confirms 98 participants, 36 fictional brands in cars/refrigerators/smartphones, repeated measures, forced-choice recognition and divergent length/attitude findings. The dataset correctly does not treat 3,528 measurements as 3,528 independent people or the same study's policy brief as a replication. This is a reason to reject a universal short-name rule, not adopt a universal long-name rule. [EMP008](https://researchportal.vub.be/en/publications/rightsizing-brand-names-the-effects-of-brand-name-length-on-brand/).

## Strengths to preserve in integration

The selected sample is explicitly purposive and includes counterexamples. No causal superiority of a style can be estimated without a market denominator, comparable failures, and control for exposure, category, distribution, price, product and capital. Adding a few failed brands reduces rhetorical cherry-picking but does not remove selection/survivorship bias. Report counts only as counts within the coded set.

The available records separate sales, retail scans, longevity, availability, acquisition and loss. ZICO is correctly active/scale-unknown despite historical phase-out; Casper is not called currently insolvent from a 2021 loss. Oatly company revenue includes non-beverage products; NIKE Brand revenue includes Jordan; Amazon includes AWS. These units must not silently become individual consumer-product sales. An established brand can also have revenue decline, losses or country withdrawal.

Most origin fields properly retain unknown status rather than filling gaps with folklore. Literal meaning, observed resemblance and retrospective corporate narrative remain different kinds of evidence. The report should retain this restraint even when a familiar origin anecdote would make prose more entertaining.

The test protocol is unusually careful about separate audio/visual routes, delayed unaided recall before recognition, matching packaging, false-positive recognition, no-choice responses, unknown status and raw denominators. Its 8–12 exploratory interviews are explicitly diagnostic. Its illustrative n≈96 ±10 percentage-point calculation is correctly identified as a proportion-precision illustration, not power analysis or representativeness. These numbers should not become automatic pass/fail rules.

## Still to review

Final report and all final CSVs; beverage workstream records and source chains; count denominators and status definitions; source-ID consistency across combined files; explicit source access downgrades; the lead's resolution of R01–R08. This review does not certify legal availability, actual consumer reactions, sales attribution, or every figure in every source.


## Second pass: integrated reasoning and beverage records

**Snapshot:** 2026-10-17T11:16:26+02:00 Europe/Prague (UTC+02:00). Reviewed the integrated report draft, methods, revised protocol and all 48 brand records across lead/consumer/beverage workstreams. The report still contained count/source-link placeholders at this snapshot, so final rendered counts and CSV equivalence remain a separate completion check. The language/legal sources were included in identifier validation only; this reviewer does not independently certify their own research.

| File | Snapshot SHA-256 |
|---|---|
| `report.md` | `fc6c4932b729fcdf71aacd722963897a8731f54bb9abdc802fc53c4bdbb352a8` |
| `supporting/methods-and-limitations.md` | `1297b682b15a9c9fc5a256743be8f2d80e5a9e6a344c74a46bb0d96539e35540` |
| `supporting/evaluation-and-testing.md` | `2122602cfa9953074c09fdd6bb842540563f02cb18a295c06c001be92a7de2af` |
| `supporting/workstreams/lead.json` | `4f8fcd686747f3145c02e7de70c05d5d940a835ad954eedae6c76717e4a45bbf` |
| `supporting/workstreams/empirical.json` | `cf9b63d718f21f308cbff4a8f2efc81d9744acf0c024db0899c2f95e86bdb623` |
| `supporting/workstreams/empirical.md` | `3cae3b6514887c19e57286d8ce9a727acd4c234eff52e1b8556bc747cff9c527` |
| `supporting/workstreams/beverage.json` | `f01fe4abe242276f47fafe9e179eabff92a48c1ca50a8c63b9c99ae7b004f751` |
| `supporting/workstreams/beverage.md` | `57f356e924792b7cd5c31b801e2a55d4a5b592a862e70c33179b16b48daaacaa` |

### Resolution and additional findings

- **R01 resolved:** report section 2 and methods define each qualitative status, distinguish underlying events and explicitly reject success-cohort inference. These definitions improve interpretation without turning non-comparable figures into a common success threshold.
- **R02 resolved:** Liquid Death origin is now unverified; documented founder positioning remains separate from actual coinage.
- **R03 resolved:** CONE10 now records `company_report`; the journalistic source and limitations retain the original chain.
- **R04 resolved:** isolated-name audio uses the visual arm's neutral context. The realistic recommendation sentence is a later, separate task.
- **R05 resolved:** the deeper Pepsi etymology is removed, and the geography-dependent retrieval issue is stated in methods. The independently sourced 1898 rename is retained.
- **R06 resolved in methods:** personal-name coding and apparent source language are explicitly not founder counts or verified language-origin data.
- **R07 resolved:** report scope, methods and beverage rows distinguish direct RTD cans, ready-to-pour alternatives and mixing bottles. Pentire and Botivo now have explicit RTD-can sources; Seedlip core bottles remain adjacent architecture comparators. PRAGER'S revenue remains an alcoholic/nonalcoholic portfolio figure, and Vilgain remains a broad nutrition masterbrand with an RTD product rather than a pure beverage company.
- **R08 resolved in methods:** descriptor strings are an observed/analytical mixture and category independence is desk coding for an unfamiliar observer, not measured recognition or a verbatim pack-copy corpus.
- **R09, minor source scope, sent to lead:** section 6 places Coca-Cola Zero/Zero Sugar alongside documented renames, whereas LEAD024 supports current Zero Sugar/Diet Coke architecture rather than a dated Zero-to-Zero-Sugar transition. Reframe as current descriptive architecture or add direct rename evidence; do not imply this source establishes a measured improvement.
- **R10, count sensitivity, sent to lead:** Ghia's invented primary code is explicitly provisional. It is an opaque token to the sampled market, not verified coinage. A count of invented-type names must disclose this or give a sensitivity count excluding it. Other overlapping primary/secondary classifications must remain analyst categories.

### Additional primary-source spot checks

Reopening the [OLIPOP official explanation](https://drinkolipop.com/blogs/digest/why-is-olipop-called-olipop) confirms the stated oligosaccharide/pop construction (BEV025); reopening [hiyo's story](https://drinkhiyo.com/pages/our-story) confirms its acronym account (BEV031). This validates source attribution, not independent historical corroboration, buyer understanding or product efficacy.

[PepsiCo management remarks](https://investor.pepsico.com/docs/pepsico-5v9wci20/media/Files/investors/q4-2025-prepared-management-remarks.pdf), page 5, explicitly call the nearly USD745m poppi figure **estimated 2025 retail sales**, not manufacturer revenue (BEV028). The [TÖST Form C-AR](https://www.sec.gov/Archives/edgar/data/1733215/000185177324000008/tostcar.pdf), second PDF page, reports 2023 revenue USD6,763,816.23 versus USD3,206,994.66 in 2022, with 2023 net loss USD432,228.91 (BEV042). Filing status does not mean SEC endorsement, and revenue growth coexists with loss. The beverage records preserve these distinctions.

### Count and structural cross-check

Combined JSON contains **48 brand records, 69 commercial/status observations and 144 sources**. All brand IDs, evidence IDs and source IDs are unique across workstreams. Every commercial row points to an existing brand/source, and every brand source reference resolves. Character counts match Unicode code-point length; word counts match whitespace tokenisation. These checks validate internal structure, not every external claim.

| Dimension | All 48 | Beverage subset, n=36 |
|---|---|---|
| Status | 24 established; 7 emerging traction; 15 active/scale unknown; 2 discontinued | 15 established; 7 emerging traction; 12 active/scale unknown; 2 discontinued |
| Descriptor-independence coding | 34 opaque; 12 partial; 2 clear | 25 opaque; 10 partial; 1 clear |
| Origin evidence | 12 documented; 28 unverified; 8 interpretation only | 8 documented; 24 unverified; 4 interpretation only |

The additional 24-brand beverage memo also reproduces its own data correctly: 19/24 one-token names, 15/24 opaque, 8/24 partially informative and 1/24 clear; 5 established, 7 emerging, 11 unknown-scale and 1 discontinued. The report should not silently substitute these 24-brand workstream denominators for the 36-brand beverage total.

No newly observed evidence issue overturns the report's conclusions. The principal remaining risks are unequal evidence ages, opaque-token classification, format/portfolio mixing and survivorship bias; these are stated limits, not solvable by arithmetic. Final-file checks are still required before completion.


## Final data/count pass

**Snapshot:** 2026-10-17T11:16:50+02:00 Europe/Prague (UTC+02:00). This pass covers the completed count section and merged CSVs, not later edits after these hashes.

| File | Snapshot SHA-256 |
|---|---|
| `report.md` | `a16250c237de847d8ea62a762cde4985689c235ed052ceb9ece318f435aa8123` |
| `data/brand-name-analysis.csv` | `147e5b55bc91f30555ad0f789d4ba277a9ef3d724bc2ee198cb87462da1115bc` |
| `data/commercial-evidence.csv` | `009be4ab897e156a7ce77e4e1ef880c39455f5de21f42b02cc35bacdb5957108` |
| `sources.csv` | `be66440182d6d84c5ddf13d531ba547027651cffd953878cf456da3ecfc948ad` |

All three CSVs parse with their intended headers and are exact string-value equivalents of the four workstream JSON arrays: **48 brands, 69 evidence rows, 144 sources**. The report's status, primary-code, word-form, character-range, syllable, descriptor and region counts match recalculation from the CSV. Specifically, word counts are 38 one-token, 9 two-token and 1 three-token; lengths range 4–17 characters; 43 rows have a coded syllable count, including 18 two-syllable readings. The primary-name-type totals sum to 48 and the beverage subgroup totals to 36. No prevalence or significance inference is attached to these numbers.

The report now removes both completion placeholders and gives explicit denominators, qualitative coding caveats and Ghia's sensitivity calculation (12/47 overall and 10/35 beverages after exclusion). **R10 resolved.** The Coca-Cola sentence now illustrates current Original Taste/Zero Sugar descriptors rather than claiming a source-documented historical rename. **R09 resolved.** All 79 source reference labels used in the report have matching Markdown link definitions. The complete 144-row register retains the sources needed for data/workstream claims beyond the report narrative.

No unresolved material methodology or evidence-scope issue was found in this reviewed snapshot. This conclusion is limited to internal consistency, stated methods and the enumerated source spot checks. It is not exhaustive source re-verification, independent financial audit, legal clearance, native-language validation or evidence that naming caused commercial outcomes. The lead remains responsible for final local-link checks, diff review, staging and commit.
