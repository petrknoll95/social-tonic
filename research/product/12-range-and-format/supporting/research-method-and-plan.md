# Research method, delegation and repository reconciliation

**Cut-off: 17 October 2026. Status: research integrated and independently reviewed; corrections recorded in review-and-publication-checks.md.**

## Scope and ownership

The supplied remote resolves to `https://github.com/petrknoll95/social-tonic.git`; the owner was not guessed. Root README, research index, relevant topics 01 (US landscape), 02 (commercial traction), 04 (EU/Czech competition), 05 (customer occasions), 26 (trends), and concurrently prepared local topic 06 (demand/country selection) were inspected. No applicable AGENTS.md was found in the repository or parent directory chain. No equivalent range-and-format folder existed; requested path `research/product/12-range-and-format/` is used unchanged. Paths refer to the repository root.

The initial checkout had a modified research index and untracked concurrent research. An isolated managed worktree based on fetched `origin/main` commit `70535ed` was created, on branch `codex/range-and-format-research`. Unrelated files in the original checkout were left intact. The lead owns the integrated report, source register, shared index and publication. Agents write only their assigned topic files. Remote state is refreshed before publication; no force push or visibility change is authorized or used.

## Questions and complementary workstreams

1. **Portfolio benchmarks agent:** exact US cans/bottles with a 2025–2026 event; flavors versus formulas, dayparts, sensory/portion/pack mechanics, commercial evidence and limits. Outputs: `portfolio-benchmarks.md`, `portfolio-sources.csv`, `../data/rtd-benchmarks.csv`.
2. **Packaging/operations agent:** cans versus glass/PET bottles, resealability, single/multi-serve, manufacturing capabilities and published minima, operational implications. Outputs: `packaging-and-operations.md`, `packaging-sources.csv`, optional packaging dataset.
3. **Safety/regulation agent:** EU/Czech ingredient/claim gates, daily combined exposure, science transfer and CBD alternatives. Outputs: `safety-and-regulatory-gates.md`, `safety-sources.csv`.
4. **Lead:** Czech price anchors, architecture choice, explicit assumptions, inventory/unit-economics sensitivity, provisional brief, validation plan, integration and publication.
5. **Independent review:** after first-round outputs, assign a separate review of the integrated recommendations, calculations, citations, format compliance and unresolved contradictions. Reviewer did not author the integrated report/model; findings and resolutions are retained.

These tasks were actually dispatched concurrently, not merely described as a plan. No people are contacted, purchases made, supplier quotes requested or tests represented as completed.

## Evidence rules

Only finished, ready-to-drink liquids in cans or bottles are eligible product benchmarks, including verified bottled shots and RTD coffee/tea. Exclude consumer powders, sachets, pouches (also liquid), tablets, capsules, gummies, gels, drops, dilution products and cartons. Raw manufacturing ingredients can differ in form. Non-RTD habits inform interviews only. Exact SKU identity and current package are checked; historical data are not silently mapped to a newer formulation. Whole-brand results with excluded formats are not evidence of the liquid line.

Keep five labels distinct: **verified source fact**, **attributed brand/supplier claim**, **estimate/model assumption**, **customer hypothesis**, **unknown**. A listing/rollout is availability, not sell-through. A source quoting a company remains a company-origin claim. US purchases do not prove Czech/EU demand; commercial success does not validate efficacy; an ingredient study does not establish the finished drink's effect. Science transfer checks dose, ingredient/extract identity, delivery matrix, processing/shelf life, population, comparator and endpoint. Direct URLs, publication dates (or undated), access date and geographic scope are recorded in CSV.

This is targeted desk research, not a systematic clinical review, a representative consumer study, an approved formula or a legal opinion. Full-year 2026 actuals cannot be assumed at this cut-off. Current product pages are snapshots, not launch dates. Search extracts are explicitly weaker where full text is unavailable.

## Prior findings reused and issues to reconcile

- Topic 01/26 establishes the broad RTD map; topic 02 supersedes ambiguous brand revenue with scoped energy/soda evidence. Hiyo case counts have unknown case size; projections remain projections. No can revenue is inferred from valuations or acquisition prices.
- Topic 05 supplies behavioural hypotheses, not validated demand. The work-break occasion and zero-caffeine preference must remain separate. Flavor preference, paid repeat and acceptable price are unknown.
- Local topic 06 is concurrent work, not a new dataset authored here. Its Czech research priority and 250–330 ml hypothesis are considered, not imposed. Its forecast and country scores are not imported as observed sales. Topic 06 subsequently appeared remotely at `5001efe` and was integrated into this worktree; cross-links now resolve.
- Earlier CBD notes emphasize February 2026 EFSA supplement-only conditions. Topic 02 adds a September 2026 opinion on one synthetic-CBD MCT-oil supplement. Recheck the newer source; neither is generic beverage authorization.
- US 12 fl oz is about 355 ml, not the same package as a European 330 ml can. Do not transfer dose concentration or can-line availability without checking.

## Publication integration

Before staging, the worktree fast-forwarded to fetched main `d6124de`, incorporating the concurrent topic 06 and research index. Existing unrelated tracked files, including user-added metadata, were not edited or staged as part of this research. The final commit is limited to topic 12 and its research-index entry. A final fetch/ancestry check and remote file comparison follow the pre-publication checks.
