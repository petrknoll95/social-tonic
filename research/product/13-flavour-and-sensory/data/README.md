# Data and fieldwork templates

**17 October 2026. All response templates are empty; no participant observations or tasting results exist.** Source IDs refer to the topic [source register](../sources.csv). Product/material data are desk-research observations of documents, not laboratory measurements.

| File | Use and limits |
|---|---|
| [us-sensory-benchmarks.csv](us-sensory-benchmarks.csv) | Nine exact canned/bottled US records: eight recent-event references plus one older/contextual still tea. Version and exposure holds remain explicit. Sugar/caffeine are declared, not assayed. No whole-brand revenue used. USB09 is intentionally absent: unresolved Chameleon versions remain only in the investigation memo. |
| [ingredient-risk-register.csv](ingredient-risk-register.csv) | Thirteen exact-material/identity-gap rows; published evidence, supplier claims and unknown matrix effects distinguished. No formula or safe-use clearance. |
| [serving-sequences.csv](serving-sequences.csv) | Four position/carryover-balanced sequences for a proposed 48-person, four-product pilot. A–D are hidden recipe aliases, not participant-facing codes. Randomize sequence allocation and independently counterbalance the later diagnostic pass. |
| [sample-manifest-template.csv](sample-manifest-template.csv) | Unblinded operator inventory for exact lot, format, label, exposure, process and measured physical properties. Do not collect participant health details here. |
| [tasting-responses-template.csv](tasting-responses-template.csv) | One row per participant × product × pass. Pass A contains primary liking/desire/open comment; Pass B contains diagnostics. Leave fields not asked in that pass empty. |
| [preference-template.csv](preference-template.csv) | One row per participant × session/condition; supports tied preferences, neither/uncertain and separated blind versus revealed hypothetical choices. |
| [full-serving-template.csv](full-serving-template.csv) | One row per participant × product × serving day; captures noncompletion and actual second-serving experience. Same-day further servings are separately recorded only if permitted. |

## Recording conventions

- Blank = missing/not asked, never zero. Zero is valid for not-perceived intensity and no volume consumed. Use `unknown` for unresolved document facts; do not insert a guessed dose.
- Liking: integers 1–9. Intensities/desire/fit: 0–10. JAR: 1 much too low, 2 somewhat too low, 3 just right, 4 somewhat too high, 5 much too high. A higher JAR value is not better.
- Use ISO dates and local times with timezone; volumes ml, caffeine mg/container, temperature °C. For other actives, state identity, unit and elemental versus compound basis. Record assay/label source and rounding.
- Quote free text containing commas using standard CSV escaping. A semicolon separates multiple source IDs in evidence datasets. Free-text associations must not be interpreted as ingredient analyses.
- Keep respondent identity, contact and screening/health data outside GitHub in the organizer's restricted records. Templates use anonymous IDs only. Public publishing of fieldwork results requires a separate privacy review.

## Planning arithmetic, not observed consumption

A four-product pilot with two 30 ml pours per product offers **240 ml/person**. For 48 people, the analytical sample volume is **11.52 L overall**, **2.88 L/product**, before freshness losses, spare containers, staff checks or withdrawals. Do not order only this volume: controlled opening times and serving logistics can materially increase requirements. No prices or supplier quotations were obtained.

Repeating three products twice across separate days entails **six product days/person**. At 24–30 people, this is **144–180 whole packs offered**, not necessarily consumed. Recruit retention and assess burden before committing; a two-product repeat design can reduce burden, but the chosen comparison and decision rule must be changed before testing. All servings remain subject to ingredient/label limits.

Caffeine illustration: 120 mg / 355 ml × 30 ml = **10.14 mg** per pour (rounded). Sum every sample and other same-day exposure; never treat this illustration as a target dose. Equal-elemental magnesium arithmetic is documented in the technical memo. Proposed statistical thresholds and sample counts are assumptions, not industry guarantees or a power calculation.
