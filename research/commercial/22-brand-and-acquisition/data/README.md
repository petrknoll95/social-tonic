# Data and planning models

Date: 17 October 2026. No rows are customer results. [Acquisition economics](acquisition-economics.csv) contains entirely illustrative CZK assumptions; [test register](acquisition-tests.csv) is a compact execution index for the [full protocol](../supporting/acquisition-test-protocol.md). Source-workstream CSVs feed the canonical [source register](../sources.csv); they are provenance files, not independent corroboration.

## Unit economics before a CAC target

The example is a **six-can DTC order**, not a recommended pack, retail price, supplier quote or tax treatment. Net receipts of CZK240 already exclude applicable tax and are a model input, not derived from the CZK39/49/59 consumer price questions. Replace inputs using actual consumer pricing, applicable tax and delivery terms before interpreting viability.

First-order contribution before acquisition:

`240 − (6 × 18) − 12 outer pack − 18 pick/pack − 35 net delivery − 7 payment − 10 promotion/refund reserve = CZK50`.

Illustrative repeat-order contribution is CZK60, assuming the CZK10 first-order reserve disappears. That optimistic difference must be replaced if repeat discounts/refunds persist. Fixed overhead, founder wages, tax on profit, formulation and stock financing are not in order contribution and must be funded separately.

For a 60-day horizon with one additional order per repeater: `expected contribution = 50 + repeat fraction × 60`. At assumed 20%, 35% and 50% repeat, contributions are CZK62, CZK71 and CZK80. Keeping a **chosen 30% buffer** gives illustrative acquisition ceilings **CZK43.40, CZK49.70 and CZK56.00**. These are scenario constraints, not observed CAC, expected retention, an industry benchmark or a forecast. Do not use the middle 35% because another report used a similar gate; it is only a sensitivity input.

Before paid repeat exists, use at most first-order contribution after the same chosen buffer: `50 × 0.7 = CZK35` per new customer in this example. Even that ceiling is unusable if real costs make contribution negative. A negative contribution cannot be fixed by assuming greater volume.

Sensitivity: increasing landed can cost by CZK5 lowers each six-can order contribution by CZK30. At 35% repeat the illustrative ceiling drops from CZK49.70 to `(20 + .35 × 30) × .7 = CZK21.35`. A CZK20 larger net delivery cost reduces it to `(30 + .35 × 40) × .7 = CZK30.80`. This supports testing local delivery/retail access before scaling shipping-heavy DTC.

Sampling/creator budgets are learning caps and may be economically unattractive at small scale. For example, CZK12,000 / 60 new buyers is **CZK200 attributed acquisition cost**, exceeding all example ceilings. That is a failed scale case, even if it yielded useful feedback. Report one-time research spending separately and the fully loaded total; recurring staffing, sample, creator and transport expenses cannot be relabelled research to erase bad unit economics. Incremental acquisition remains unknown without a defensible comparison.

Retail/office economics require a separate net wholesale receipt, trade margin/fees, delivery frequency, waste and account-service model. Do not apply a DTC customer ceiling to a B2B account or compare a paid employer case order with an individual single-can purchase. A creator audience's size and a waitlist's size are not revenue inputs.
