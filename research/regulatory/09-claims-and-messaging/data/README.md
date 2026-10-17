# Claims and eligibility data

**17 October 2026 · EU/Czech provisional research.** No dataset is a formulation instruction, safety clearance or proof of efficacy.

- [Claims matrix](claims-matrix.csv): 44 contextual wording assessments, with classification, legal/source basis, conditions, risk, alternatives and a separate efficacy limitation. [Readable matrix](../claims-matrix.md).
- [Nutrient thresholds](nutrient-thresholds.csv): eight nutrients; NRVs and the source/high calculations for beverage concentration and genuine single-portion packages. Units are explicit; magnesium is elemental.
- [Caffeine examples](caffeine-concentration-examples.csv): eight hypothetical combinations; exact threshold comparison is computed before displayed rounding. The coffee/tea exception and other rules still require review.
- [Nutrition and serving examples](nutrition-and-serving-examples.csv): sugar limits, fibre energy basis, carbohydrate recovery and the narrowly applicable CBD supplement calculation.
- [Calculation method](recalculate.py): regenerates the three numerical CSVs using decimal arithmetic. The qualitative claims matrix is manually researched and reviewed; the script does not decide legal eligibility.

## Assumptions and interpretation

Nutrient source route: NRV ×0.075 per100 ml; total at that concentration = value ×volume/100. Genuine one-portion package route: NRV ×0.15. High claims require twice source. A large or resealable container is not automatically one portion because a label says so; final pack/consumption pattern needs review. These values are unrounded arithmetic, not label declarations or production targets. Account for shelf-life loss, variation, tolerances, permitted forms and safety separately. Legal/source details: CN08 and CN16 in [sources](../sources.csv).

Caffeine concentration = mg/pack ÷ml/pack ×1,000. The Annex III threshold is **more than150 mg/L**, not at least150. Concentration exactly on a legal boundary is not recommended manufacturing practice. A lower per-can dose can still exceed it. Source: CN08.

Low/sugars-free limits are per100 ml liquids. Fibre nutrition claims may use an energy basis; using the mass basis needs actual density, not an automatic100 g=100 ml assumption. Recovery4 g/kg is carbohydrate from **all sources** in the specified exercise/time window. The CBD arithmetic is included to prevent misuse of a supplement figure as an RTD dose. Sources: LM02/LM04, CS13/CS14 and CS04.

The numerical examples were recomputed by an independent agent. Final checks also verified CSV structure, unique matrix IDs, source resolution and internal links. The source ledger intentionally retains separate workstream IDs for some identical URLs so citations remain auditable; those are not independent corroborating sources.
