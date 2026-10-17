# Methods, boundaries and review record

**Created 2026-10-17T11:07:23+02:00 · Europe/Prague · UTC+02:00.** Research and access cut-off: 17 October 2026. The machine-readable creation record is [creation.json](creation.json). No final name was generated.

## Repository review and preservation

The lead inspected the local repository and git status before editing. No applicable AGENTS.md was found in the repository or checked ancestors. Read the root README and research/ideas indexes; brand/ was empty. Reviewed relevant findings in research topics 01 US landscape, 02 commercial traction, 04 EU/Czech competition, 05 customers/occasions, 09 claims, 12 range/format and 22 brand/acquisition, plus the existing new-drink-opportunities report. Read the concurrent claim-led-ingredient report as context only; it is not an independently validated source and its evolving recommendations were not adopted as settled positioning.

At start there was a modified research/market/.DS_Store, untracked research/market/02-commercial-traction/.DS_Store, and concurrent claim-led-ingredient and creatine-RTD research directories. These were preserved. Only this timestamped folder and brand/research/README.md are intended for this assignment's commit. Concurrent changes outside that scope must remain unstaged by this work. No existing brand assets were edited.

## Design before analysis

The [shared framework](coding-framework.md) fixed 48 planned names before counts: 12 non-beverage consumer brands and 36 beverage brands. The discovery leads in the brief were retained along with global soda/energy incumbents, EU/Czech brands, adjacent alcohol alternatives, different naming mechanisms and adverse commercial histories. This is a purposive coverage design, not random sampling, a matched case-control design or a market-share-weighted list.

Inclusion required a verifiable consumer-facing identity and documented product/category context, plus a commercial/status source or explicit unknown-scale classification. Historical discontinued names qualified because they challenge deterministic success stories. No brands were selected for a preferred vowel, length or final naming territory. Non-beverage names are mechanism comparators; they are not evidence that beverage buyers behave identically. No post hoc statistical significance tests are appropriate.

The beverage sample intentionally permits adjacent architecture comparisons beyond the project's finished can/bottle RTD scope. Oatly includes cartons/foods. Seedlip and Three Spirit have mixing/serving bottles; other aperitif brands may also have RTD cans. Each portfolio must be read by product form, not declared entirely RTD or entirely concentrate. No powder revenue is assigned to a ready-to-drink line. Corporate and portfolio financials are labelled as such.

## Operational outcome labels

- **established:** specific documented material scale or durable multi-year presence. The evidence may be historical; this is not a claim of 2026 profit, growth, retention or market leadership. Longstanding offers/history are weaker than audited current sales, and the event rows retain that distinction.
- **emerging_traction:** a documented sales/growth/distribution event sufficient to go beyond mere existence, without assuming mature scale or profitability. Announced/company-reported listings are identified and not equated with retailer sell-through.
- **active_scale_unknown:** current offer/listing confirmed, but this review does not establish adequate comparable sales/retention. It does not mean the business is small or failing.
- **discontinued/renamed/struggling:** a specifically sourced event/time/geography. A historical adverse event does not automatically determine today's status. ZICO and Casper illustrate this distinction.

These are qualitative evidence-summary codes, not a quantitative success threshold. “Established” is not a clean group for success/failure odds. Funding, valuation, social followers, media attention and attractive design are not sufficient to move a brand into a sales-traction classification. Commercial-evidence rows are authoritative when a compact brand status obscures mixed outcomes.

## Coding rules and ambiguity

Each brand row records name/level, category, market and region, apparent name language, dominant/secondary name type, semantic territory, counts, pronunciation/spelling considerations, associations, promise anchor, tone, descriptor, hypothetical category independence, origin evidence, status, channels, architecture and source IDs.

**Primary name type** is one dominant analyst classification, not a mutually exclusive natural law. Secondary tags preserve overlaps. A compound may also be provocative; an ingredient root may be opaque to consumers. `founder_personal` combines personal-name form and founder names; never report its total as a count of actual founder surnames. Warby Parker's characters and Casper's personal-name form do not establish founder provenance. Place-based coding does not imply a protected geographical indication.

**Original language** is explicit where documented, otherwise it describes the market-facing lexical form or is unknown. It is not a verified coinage language for every brand. No source proves that an English-looking invented word was invented in English merely by being sold in the US. Do not count these cells as verified language-origin statistics.

**Counts:** whitespace-delimited word tokens; hyphenated Coca-Cola/Club-Mate/fritz-kola are one token. Characters are Unicode code points including spaces, hyphens, apostrophes and diacritics, excluding trademark symbols not included in the stored name. Capitalisation follows documented brand text where practical; stylised logos can differ. Syllables are indicative for the reading described in the row, not language-invariant. Ambiguous entries remain blank. Counts do not measure processing effort or memorability.

**Descriptor** stores observed category/family wording and, in some cases, a clearly identifiable analytical summary of the product offer. Semicolons separate examples, not a claim that one exact tagline appears everywhere. It is not a verbatim pack-copy corpus. `descriptor_independence` judges whether an unfamiliar reader could infer category from the word itself; it ignores fame and is not measured consumer recognition. `category_partial` supplies a clue, `category_opaque` needs learned association/support and `category_clear` strongly describes the offering. Tone, promise anchor, semantic territory and expansion risks are analyst interpretations.

**Origin:** documentary corporate/founder accounts establish what the source says, not perfect historical causation. Literal meanings and inferred resemblance do not become origin stories. Sources are attached at brand-row level; individual assertions remain bounded by supported_claims in the source ledger. Unverified origins are deliberately left unresolved. Liquid Death's documented entertainment positioning is not misclassified as a verified account of coinage. Pepsi's deeper etymology is omitted after inconsistent geography-dependent FAQ access; the separately sourced 1898 rename is retained.

## Evidence and source handling

The source register retains title, URL, publisher, publication date, access date, provenance type, access level, supported claims and limitations. Dates marked undated are snapshots, not guessed publication dates. Historical indicators keep their reporting period; 2023 retail sales do not become a 2026 run rate. The retrieved source's body/dateline takes precedence over misleading search-engine relative dates.

Peer-reviewed articles were checked through publisher pages, author/institution-hosted copies or clearly labelled accessible abstracts. A university summary of a paper is not independent replication. No pooled effect size was computed. Practitioner material is labelled and not used as independent causal proof.

Official product pages support existence, stated scope and packaging language, not efficacy, actual inventory in every market or quantified commercial scale. Underlying metric provenance matters: company numbers quoted by journalists remain company_report in commercial-evidence.csv. The source register separately identifies the publisher and source genre. Acquisitions, revenue, loss, units, retail sales, distribution, awareness and availability remain separate rows.

Some official pages and PDFs returned redirects, empty responses or blocked opens. Where specific content was available only in indexed excerpts, access_level says search_excerpt and the claim is narrow. No paid report or raw panel database was accessed. Accessible sources were browsed during this assignment; validation checks source-ID/URL consistency and claim scope, not perpetual availability of every URL.

## Delegation and independent review

The lead defined the schema, reviewed repository context, researched 12 beverage cases and channel/practitioner evidence, authored the synthesis/brief/protocol, merged datasets, validated and owns the local commit. Complementary sub-agents researched (1) empirical naming evidence plus 12 non-beverage comparators, (2) 24 beverage/social-tonic comparators with commercial checks, and (3) Czech/EU language and legal considerations. These agents used the same coding contract.

After completing their research, the language/legal agent independently reviewed other workstreams' methodology and evidence, including primary-source spot checks. The empirical agent separately reviewed the integrated synthesis and legal/language reasoning. A reviewer is independent of the author of the relevant section, not an external expert or consumer sample. Review coverage and unresolved limits appear in [independent-review.md](independent-review.md) and [independent-synthesis-review.md](independent-synthesis-review.md). The lead resolves issues in the final files; the first-pass snapshots remain historical records.

### Resolution log

| Review issue | Lead resolution |
|---|---|
| R01 ambiguous success/status | Added explicit definitions in report section 2 and these methods; prohibit success-cohort inference. |
| R02 Liquid Death name origin | Downgraded to unverified; retain founder positioning account separately. |
| R03 Dollar Shave Club revenue provenance | Changed underlying metric to company_report while retaining journalistic publisher/source context. |
| R04 unequal audio priming | Isolated name first in both routes; recommendation sentence reserved for a separate contextual task. |
| R05 Pepsi FAQ geography redirect | Documented access discrepancy; removed deeper etymology and retain 1898 rename. |
| R06 founder/personal and language categories | Explained category scope and prohibited founder-count or verified-language-origin overinterpretation. |
| R07 adjacent formats | Added direct-versus-adjacent scope in report/methods; preserve portfolio-specific product notes. |
| R08 descriptors and independence | Explicitly analytical, sometimes summarised descriptors; not consumer recognition data or a verbatim copy corpus. |

Further synthesis resolutions and validation results are recorded in [validation.md](validation.md).

## What remains unknown

The sample lacks a complete entrant/failure denominator, comparable advertising/distribution controls, uniform retail data, cohort retention and name-only sales experiments. It overrepresents visible English-language and digitally documented brands. Unknown-scale firms may be very successful, and historical closures may reflect ownership strategy rather than poor demand. Counterexamples do not remove survivorship bias.

No Czech or other native-speaker validation, trademark clearance, domain availability judgment, recruited testing, sensory research, efficacy testing or verified conversion analysis was performed. Five language contexts do not cover the EU. Category interpretation and emotional transfer remain hypotheses. The testing protocol is a future design, not results. Nothing was purchased, registered, filed, sent to companies or externally published.
