# Evidence, data and publication checks

**Checked: 17 October 2026, Europe/Prague.** This records the scope and results of the local publication review. The final remote commit and verification are reported with the published deliverable; no remote upload is inferred from this document alone.

## Evidence and independent review

Three parallel, separately owned research streams were integrated by the lead. The secondary researcher reviewed the focus/calm streams and lead synthesis; the focus researcher independently reviewed secondary categories. Their [cross-stream review](independent-review.md) and [secondary review](independent-secondary-review.md) retain source-access limits and the lead's dispositions. These are targeted documentary reviews, not audits of private panel records or financial statements.

Decision-changing source checks included the SEC-hosted Nielsen energy table and exact filing date, Circana's first-year methodology and trade dollar reporting, PepsiCo's Poppi retail estimate and earnout note, OLIPOP's achieved-versus-forecast source chain, KDP's Electrolit period, Oikos bottle sizes and combined-line boundary, Recess/VYBES ranking universes, TRIP's audited gross/net/tax bridge, and current EFSA/Czech official evidence. Source dates and geographic limits remain attached to the claims.

Final corrections incorporated:

- Goodrays is **medium confidence**, with search-index-only access, failed direct page access and inferred UK geography stated. The underlying NIQ extract was unavailable.
- Unwell's August date is unresolved in internally inconsistent reporting; cessation after Halloween remains prospective at the cutoff.
- The exact SEC filing date is 2 December 2025. Oikos Pro Drinks + Shots is a combined qualifying liquid-line result, not whole-brand or yogurt-cup revenue.
- Numeric lower bounds and approximate counts retain their qualifiers in the datasets: more than 35m Bloom cans, more than 7.5m Neutonic cans, more than 50% unallocated reorders, and nearly 1,000 announced Walmart stores.
- Forecasts, cumulative claims, weak proxies and mixed-format accounts remain explicitly marked or segregated. No cases-to-cans, revenue-to-retail, annualization or assumed FX calculation is introduced.

## Mechanical checks

- Parsed every topic CSV with consistent row widths and nonempty required metadata; unique source IDs and metric IDs.
- **115 source records / 113 unique URLs**. FE04/SC29 and FE03/SC30 are intentional aliases for shared Circana evidence chains across workstreams, not independent corroborations.
- **71 raw metric records** partition exactly into **49 commercial observations** and **22 excluded/context records**, with no lost or duplicated IDs. The commercial file includes clearly labeled unknowns, forecasts, proxies and negative cases; 49 is not the number of proven successes.
- Resolved all metric source IDs and checked that consolidated direct URLs match the source register. Access dates are 17 October 2026; undated or imprecisely dated pages are labeled rather than assigned invented dates.
- Checked relative Markdown links across this topic and the research index, including the published topics 01, 04, 05 and 26. No local absolute paths, conflict markers, unfinished placeholders or credentials are included in the deliverables.
- Normalized CSV line endings and ran Git whitespace checks. Reviewed changed paths: only topic 02 and its additive research-index row belong to this change.
- Arithmetic checked: £66,936,709 gross minus £15,987,236 rebates equals £50,949,473 net; −£1,109,669 pre-tax result plus £1,243,150 tax credit equals £133,481 net profit; $278m minus $266m equals the $12m Poppi earnout valuation. These reconcile stated accounts, not beverage-line earnings.

## Repository preservation and publication procedure

The existing owner/remote was verified as **petrknoll95/social-tonic**. The original checkout's uncommitted/concurrent work was left untouched. This topic used an attached isolated worktree, initially based on 8d09cac. The remote refresh found competitor/customer research and CSV normalization through **ee4aa98**; those commits and index entries were preserved by rebasing and resolving the index additively.

Publish the reviewed commit through a normal non-forced push to the same repository. If protection requires review, use a dedicated branch and pull request. Verify the remote commit/tree and compare every changed file's object hash with the prepared commit, including the research index; return the exact GitHub report, data, sources and commit or PR links. No repository visibility change is part of this work.

No transient logs, downloaded source archives, source articles, credentials, or raw private financial/panel data are committed. No outreach, purchases, completed interviews, supplier quotations, or product/clinical tests occurred. Proposed validation protocols remain proposed work.
