# Review, validation and publication record

Created 17 October 2026, Europe/Prague (UTC+02:00). This records desk-research checks, not product clearance or completed consumer/shelf-life tests.

## Scope and evidence checks

- 47 broad-screen entries, including the caffeine reference, 16 deep routes and separate rejected/unresolved options. More than 30 distinct routes remain after excluding grouped nutrient entries and caffeine-bearing source variants.
- 16 dossiers with seven sections each: identity; perception/commercial usage; human studies; expected experience; safety; EU/Czech status; formulation.
- 48 structured study records, including reference-only entries REF-ALCOHOL and REF-DECAF, contextual populations and one explicitly labelled preprint. Records are not 48 independent demonstrations of efficacy. Multi-ingredient studies are retained once in the CSV and referenced by all relevant ingredient IDs.
- 195 dated source records. The same primary paper may appear under multiple workstream IDs; these are provenance entries, not independent corroboration.
- 105 promise/candidate rows cover all 47 screen entries plus an ingredient-free sensory/ritual route. The detailed experience map has 18 promise/modifier rows.
- Current primary/official sources were preferred; abstract-only extractions, unavailable funding information, supplier statements and anecdotal observations remain labelled. Exact-study findings do not clear a different generic extract.
- No supplier contacted, material purchased, prototype tasted, participant recruited or dosing experiment conducted. No price, effective serving, safe maximum, clinical effect or legal permission invented.

## Independent review and lead resolutions

The independent reviewer checked decisive sources and then read the completed report and all 16 dossiers. Its findings and limitations are preserved in [review-findings.md](workstreams/review-findings.md).

| Review issue | Lead resolution |
|---|---|
| Decaffeinated-shot paper calls itself caffeine-free despite Table 1 showing 6 mg caffeine | Described as low-caffeine/decaffeinated throughout integrated outputs. Null conclusion remains specific to that blend. |
| Paraxanthine selected contrasts versus null overall analyses | Expanded EN-ST05 null outcomes to all four task families; report retains uncertainty and no equivalence inference. |
| Nonsignificant caffeine comparison and p=.059 error in runners paper | Retained proper null interpretation; no superiority/equivalence or continuous-duration claim. |
| Theanine physiology versus subjective stress; positive pooled attention but no fatigue benefit | Both positive attention evidence and subjective nulls retained. Full subscription meta-analysis methods explicitly not inspected. |
| Dodd combination no longer significant versus placebo | Reworded: absence of the combination's significant placebo contrast is not proof of antagonism against caffeine. |
| Theobromine “six trials” could imply six independent replications | Reworded as one six-condition crossover study in 24 participants. |
| Saffron sublingual route and synthetic safranal outcome | Kept distinct from swallowed whole-extract soda; primary mood null and secondary social-rating result retained. |
| Lion's-mane hydroethanolic drink versus aqueous-process legal decision | No equivalence assumed; acute global nulls and proprietary/preprint preparation differences retained. |
| Direct interpersonal tryptophan evidence | Included both selected-population findings and contradiction; no acute-confidence promise. |
| Magnesium exposure scope | Explicitly includes supplements, water, or addition to foods/beverages under the relevant SCF salts/MgO scope; not a per-can recommendation. |
| Preparation-specific theanine/mushroom decisions; creatine claim refusal | Reverified and preserved, without converting unresolved material status into a blanket ban. |

The reviewer found no remaining material inference problem after those specified corrections. This was an adversarial targeted review, not a second systematic review, raw-data reanalysis, exhaustive national-law survey or finished-product clearance.

## Publication workflow

The source checkout contains concurrent work outside this run. Publication uses an isolated managed worktree and a `codex/` branch, containing only this timestamped run and its `ideas/README.md` index entry. Prior runs and unrelated work are preserved. The repository had no applicable `AGENTS.md`; the existing main branch and remote were inspected before publication.

Automated structural checks cover CSV shape, unique record IDs, resolvable source/study/ingredient references, required files, dossier coverage and relative Markdown links. Git whitespace validation is also run. Remote branch publication and pull-request state are verified after pushing; the resulting commit/PR links are returned in the chat. This record does not claim a merged main-branch result.

## Completed structural validation

Passed: all required files; consistent CSV row widths and unique IDs; resolved source and ingredient references (including explicit reference-only studies); all relative Markdown links; 16 complete A–G dossiers; 47 screen entries, 105 claim mappings, 48 study records and 195 source records. Git whitespace validation passed before commit. These checks establish document integrity, not efficacy or regulatory clearance.
