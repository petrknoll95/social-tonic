# Naming screen and decision notes

**Checked:** 17 October 2026 · Europe/Prague

**Scope:** limited public-web discovery, plus registry RDAP requests for six domains. Results were reviewed through the search tool's returned text/excerpts. No systematic trademark-register search, social-handle audit, native-speaker review or legal opinion was performed.

This screen helped remove conspicuous collisions from a creative exploration. It cannot establish global originality or permission to use a name. Ordinary phrases can be used by many organisations, and an apparently novel coinage can still resemble an existing mark. Search engines also relax queries and omit results; a sparse result set is not evidence of absence.

## Final 20: query coverage and observations

Queries below preserve the wording used. Some were submitted in multi-query batches or combined with OR; the observations concern the returned results, not an exhaustive search of each string. The search interface did not expose a controllable country, language or personalisation setting, so this is not a Czech-localised search audit. Exact, phonetic, translated and accent-free trademark searches remain pending for all 20.

| Candidate | Query used | Observation and next check |
|---|---|---|
| Mezidoba | `"Mezidoba" nápoj značka` | A lexical/synonym result surfaced. No clear exact-name beverage brand was identified in the returned set. Check *Mezidobí* and similar occasion names. |
| Půlkrok | `"Po práci slunce" OR "Půlkrok"` | Ordinary-text uses surfaced; this was a broad, combined draft query. A dedicated commercial and accent-free search is still needed. |
| Druhá scéna | `"Druhá scéna" nápoj` | Theatre/literary and incidental scene descriptions dominated the returned material. Check venues, events and shortened *Scéna*. |
| Přisedni | `"Přisedni" nápoj značka` | Invitation/project wording and incidental text surfaced. No exact beverage brand was identified, but the .cz registration check below found an existing record. |
| Místo navíc | `"Místo navíc" nápoj` | Mostly incidental/general-language results. Dedicated hospitality, service-brand and accent-free searches remain necessary. |
| Spoluno | `"Spoluno"`; `"Spoluno" drink`; also `"Jiskrol" OR "Spoluno" OR "Vlnora"` | No clear exact-name commercial hit was identified in returned results. Check *Spolu*, *Spoluna* and phonetic neighbours. |
| Vlnora | `"Vlnora" drink brand`; `"Vlnora"`; combined query above | No clear beverage hit was identified. The exact .com nevertheless has a registration record: sparse web results did not mean an unregistered domain. |
| Jiskrol | `"Jiskrol"`; combined query above | No clear exact-name brand was identified. Medicinal/alcohol-like associations are an editorial concern to test, not an observed consumer finding. |
| Copper Picnic | `"Copper Picnic" brand` | Copper-coloured picnic products and cocktail equipment surfaced. An exact beverage brand was not identified. Search the individual words and related hospitality marks. |
| Oblá vlna | `"Oblá vlna" nápoj OR značka` | The phrase appears on a [corrugated sheet-metal product](https://www.burger-obchod.cz/produkty-obla-vlna-0-55-800-2000-mm-zn-detail-2672), plus incidental technical uses. This is existing descriptive language, not an unused phrase. |
| Klevuna | `"Klevuna" OR "Orvilo"`; `"Klevuna"`; `"Klevuna" drink` | No clear exact-name commercial hit was identified in the returned material. The *klevety* association in the concept is a proposed Czech reading to test. |
| Tavunelo | `"Tavunelo"`; `"Tavunelo" drink` | No clear exact-name commercial hit was identified. Check syllable loss, doubled-letter forms and related longer marks. |
| Doveli | `"Doveli" OR "Nuvrilo"`; `"Doveli"` | A [Croatian dictionary entry](https://www.crodict.com/de/englisch-kroatisch/Doveli) identifies an inflected form. Retained with the explicit condition that this is not a word with no existing linguistic use; native interpretation remains unknown. |
| Velvet Tram | `"Velvet Tram"` | Historical tram/velvet descriptions and unrelated results surfaced. No clear exact-name beverage identity was identified. Check transport, venue and tourism brands as well as beverages. |
| Malý rozruch | `"Malý rozruch" nápoj` | Incidental text and *Rozruch*-related material surfaced. Check the likely shortened brand as well as the complete phrase. |
| Dobrý zmatek | `"Dobrý zmatek" nápoj` | Mostly incidental uses of the component words; no exact beverage identity was identified. Search noise and the potentially negative meaning remain unresolved. |
| Tekutá tečka | `"Tekutá tečka"` | [Apetit's “Sladká tekutá tečka”](https://www.apetitonline.cz/tipy-triky/sladka-tekuta-tecka) is an existing drink-related editorial phrase. Retained as an ordinary-language concept, with a digestif/dessert association and a distinctiveness concern. |
| Dílna doušků | `"Dílna doušků"` | No clear exact-name commercial hit was identified. Tasting/workshop services, the accent-free string and shortened forms still need checking. |
| Várkot | `"Várkot" OR "Varkot" drink`; `"Várkot"` | No clear exact beverage hit was identified. Broader *Varkot*, *Varkoč* and neighbouring-language checks remain outstanding. |
| Rukopis chuti | `"Rukopis chuti"` | General culinary authorship language surfaced. [Odkolek's Rukopis pekaře](https://odkolek.cz/predstavujeme-novou-radu-rukopis-pekare-kvaskove-chleby-spojujici-tradici-s-modernimi-trendy/) is an adjacent food example, not an exact match. Retained as a deliberately more descriptive craft challenger. |

“No clear hit identified” is an observation about this limited returned material. It is not a pass on the source report's trademark, language or operational-identity gates.

## Three-name domain check

Direct HTTPS requests were made to Verisign's .com RDAP endpoint and CZ.NIC's .cz RDAP endpoint on 17 October 2026. Successful 200 responses were additionally inspected for the `domain` object type and matching domain name. The first Python requests failed local certificate verification; a subsequent curl request succeeded with normal TLS verification enabled. Only the successful requests support the table.

| Proposed name | Domain | Observed registry response | Interpretation |
|---|---|---|---|
| Spoluno | [spoluno.com](https://rdap.verisign.com/com/v1/domain/spoluno.com) | HTTP 404 | No record returned by this endpoint at check time. Registrar confirmation is still required; not a guarantee of availability. |
| Spoluno | [spoluno.cz](https://rdap.nic.cz/domain/spoluno.cz) | HTTP 404 | No record returned at check time; same limitation. |
| Vlnora | [vlnora.com](https://rdap.verisign.com/com/v1/domain/vlnora.com) | HTTP 200; domain object `VLNORA.COM` | An existing registration record was returned. Ownership, sale status and brand use were not investigated. |
| Vlnora | [vlnora.cz](https://rdap.nic.cz/domain/vlnora.cz) | HTTP 404 | No record returned at check time; same limitation. |
| Přisedni | [prisedni.com](https://rdap.verisign.com/com/v1/domain/prisedni.com) | HTTP 404 | No record returned for the accent-free form at check time; same limitation. |
| Přisedni | [prisedni.cz](https://rdap.nic.cz/domain/prisedni.cz) | HTTP 200; domain object `prisedni.cz` | An existing registration record was returned. Ownership, sale status and brand use were not investigated. |

No domains were purchased or reserved. Domain records say nothing by themselves about trademark rights. No domain availability conclusion is made for the other 17 candidates, and no exact social handle was checked.

## Drafts removed before the final set

These are rejected working drafts, **not additional recommendations**. Removing a name here is a creative triage decision; it does not assert that its use for a beverage would necessarily infringe a right.

| Draft | Why it was removed | Observed source or editorial reason |
|---|---|---|
| Mezivo | Exact hospitality-software use, plus a Czech lexical association inconsistent with the intended drink | [Mezivo's own QR-menu page](https://mezivo.com/en/solutions/qr-menu); [Czech Linguistic Atlas entry](https://cja.ujc.cas.cz/e-cja/heslo/3/174) includes *mezivo* among dialect forms for colostrum. |
| Tykano | Existing company name and additional language complexity outweighed the intended informal-social cue | [Australian ABN record](https://abr.business.gov.au/ABN/View?id=17075364251) identifies TYKANO PTY LTD, with cancelled ABN status. This is not proof of current trademark rights. |
| Podvečer | Exact word already used on a nearby-market wine product | [Producer's Trnkové “Podvečer” listing](https://ovocinarhrehor.sk/produkt/trnkove-podvecer/). |
| Oblouk | Existing local hospitality identity closely tied to beer | [Oblouk's own site](https://obloukova171.cz/). |
| Velumo | Multiple existing uses; little reason to carry that search burden into a new identity | [Velumo app](https://www.velumoapp.com/?from=AppAgg.com). |
| Tavilo | Established exact furniture identity serving hospitality settings | [Tavilo's own company page](https://tavilousa.com/pages/who-we-are). |
| Odrivo | Exact corporate-name history surfaced | [Luxembourg official publication](https://memorialc.public.lu/memorial/2016/C/Pdf/c2008087.pdf) includes ODRIVO Sàrl. Current activity and rights were not established. |
| Brivana | Existing regional Portuguese word, undermining the intended blank-slate story | [Priberam](https://www.dicionario.priberam.org/brivana) records a regional Brazilian word for a female horse. This is a naming-fit decision, not a claim the meaning is inherently offensive. |
| Orvilo | Exact commercial uses surfaced on a dedicated follow-up after an initially sparse combined search | [Orvilo contact page](https://tryorvilo.com/pages/contact); [Orvilo app signup](https://orvilo.app/accounts/signup/). |
| Orelvo | Exact commercial and medical-research name uses | [Orelvo retail site](https://orelvo.co/); [clinical-trial protocol](https://cdn.clinicaltrials.gov/large-docs/99/NCT03021499/Prot_002.pdf). No medical inference is needed for the naming decision. |
| Nuvrilo | Exact commercial identity and a less appealing consonant cluster | [Nuvrilo store's own About page](https://nuvrilo.shop/about-us). |
| Brumeli | Personal-name and dialect uses made it less useful than remaining candidates | [French National Library publisher record](https://nouveautes-editeurs.bnf.fr/accueil?id_declaration=10000001306125&titre_livre=Sans_toi_sous_la_lune); [Oberaargau dialect study](https://www.e-periodica.ch/cntmng?pid=oag-001%3A2002%3A45%3A%3A307). |
| Paper Orchard | A reported exact phrase in an existing art mark; it also risked an unnecessarily specific fruit story | [Third-party mark record](https://furm.com/trademarks/the-paper-orchard-97684234). Status was not independently checked in an official register; treated only as a discovery flag. |
| Pátý roh | Existing Czech company name surfaced | [Company-record aggregator](https://www.mesec.cz/rejstrik-firem/firma-paty-roh-s-r-o-28472055). Current official status was not verified; enough of a flag to prefer another creative route. |
| Nová várka | Too close to ordinary promotional language about a new batch | [A brewer's ordinary “Nová várka” announcement](https://www.pivofracek.cz/blog/nova-varka-nerve-spa-v-prodeji); editorial distinctiveness decision. |
| Po práci slunce | Too narrowly tied to after-work timing; reads more like a line of copy than a brand | Creative rejection, not a legal conclusion. |
| Orchard Static | Fruit and electronic associations compete, while search results mix unrelated technical and music contexts | Creative rejection following a public-web query; no claim of a conflicting beverage brand. |

## Remaining decision work

The final shortlist needs separate Czech audio and visual testing, native-language checks in the actual expansion markets, and qualified review of exact and similar marks against the actual product. The source report's [evaluation protocol](../../brand/research/2026-10-17_11-07-23_beverage-naming/supporting/evaluation-and-testing.md) supplies the structure. None of those future checks has been simulated or counted as completed here.
