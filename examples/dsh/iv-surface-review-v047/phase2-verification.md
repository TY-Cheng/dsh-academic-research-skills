# Phase 2 - Source Verification Report

**Scope.** 41 sources selected in Phase 2 (INVESTIGATION) of the ARS v3.24.4 validation run, verified at metadata and abstract level on 2026-11-23. No full texts were read; no author contact, no retraction-database sweep beyond OpenAlex flags, no live predatory-journal list check.

## Overall assessment

**Conditional pass.** The corpus is bibliographically sound (41/41 DOI lookups resolved, 0 retracted records) and sufficient for a Phase 3 synthesis that is explicit about evidence status and comparability. It is not a field census, and the following conditions must travel with any downstream use: (i) three metadata-only records (P4, P7, R4) may be cited only at title/metadata level and are graded `assumption`; (ii) 11 preprints (26.8%) are flagged and must be labelled as such in every synthesis claim; (iii) no source is described as 'arbitrage-free' when its evidence status is `numerical test`; (iv) violation-rate, fit and hedging numbers are not comparable across studies; (v) dynamic arbitrage is essentially unverified in this corpus - only C2 reviews the conditions and no construction method proves dynamic no-arbitrage.

## Method

- **Existence and identity.** Each selected DOI was looked up through the OpenAlex `/works/doi:` endpoint (41/41 HTTP 200). Title-search fallback was available but not needed. DOI strings were cross-checked against Crossref for the 4 records whose abstracts were recovered there. No DOI was invented or repaired by hand.
- **Abstract retrieval.** OpenAlex inverted-index reconstruction first, then Crossref (JATS tag stripping) and Semantic Scholar for records still missing or partial. Final coverage: 34 full, 4 partial, 3 metadata-only, 0 title-level.
- **Quality grading.** Two axes are kept separate, following `references/source_quality_hierarchy.md`: the evidence-hierarchy level (I-VII) and a six-criterion A-F rubric. Because the corpus is methods/simulation literature, the conventional level is VI (single study); VII is reserved for the one narrative review (C2). The matrix below grades Peer review, Method and Currency at metadata level, with COI `n/a` (no statement retrieved - not a finding of none). Overall is the median of those three grades, with integrity floors: a numerical test cannot be graded A; a claim-only or abstract-unavailable source, a preprint, a practitioner outlet or a metadata-only record cannot be graded above C; a partial abstract cannot be graded above B. Author-credibility checks were limited to whether author names are attached to the OpenAlex record; no affiliation verification was performed.
- **Cross-source checks.** Five claim clusters were read across sources: SVI/SSVI condition family (S1, P1, P2, P3, C2, P7); SABR asymptotics (S3 vs C4); penalty violation rates (N3, N4, N5, N6, G5, G6); repair violation floors (R5, R7); architectural guarantees (G1, G7, G8, G6). That covers 19 of 41 sources at least once. No claim was independently replicated; cross-checks establish consistency with the literature's own statements, not truth.
- **Not checked.** Full-text methods and proofs; conflict-of-interest and funding statements; author affiliations; journal indexing (Scopus/DOAJ/COPE); predatory-journal lists; retraction databases beyond OpenAlex `is_retracted`; citation counts (deliberately excluded).

## Source quality matrix

Level = evidence-hierarchy level (VI single study, VII review). Peer = A peer-reviewed journal/conference, C SSRN/arXiv preprint, D practitioner magazine. Method = A formal result reported in abstract, B numerical test reported, C claim-only or abstract unavailable. Currency = A 2024-2026 or seminal, B 2021-2023, C 2016-2020, D pre-2016 non-seminal. COI = n/a (no statement retrieved). Overall applies the caps described above.

| ID | Venue | Level | Peer | Method | Currency | COI | Overall |
|---|---|---|---|---|---|---|---|
| P1 | SIAM J. Financ. Math. | VI | A | A | C | n/a | A |
| P2 | SIAM J. Financ. Math. | VI | A | A | B | n/a | A |
| P3 | Quant. Finance | VI | A | A | B | n/a | A |
| P4 | Decis. Econ. Finance | VI | A | C | C | n/a | C |
| P5 | SIAM J. Financ. Math. | VI | A | A | A | n/a | A |
| P6 | J. Derivatives | VI | A | A | A | n/a | A |
| P7 | SSRN | VI | C | C | C | n/a | C |
| P8 | arXiv | VI | C | A | A | n/a | C |
| N1 | EJOR | VI | A | B | C | n/a | B |
| N2 | ICLR | VI | A | B | A | n/a | B |
| N3 | SSRN | VI | C | B | C | n/a | C |
| N4 | IEEE SSCI | VI | A | B | B | n/a | B |
| N5 | arXiv | VI | C | B | B | n/a | C |
| N6 | arXiv | VI | C | B | B | n/a | C |
| R1 | Appl. Math. Finance | VI | A | B | C | n/a | B |
| R2 | SSRN | VI | C | A | C | n/a | C |
| R3 | Stat. Risk Model. | VI | A | A | C | n/a | A |
| R4 | EJOR | VI | A | C | A | n/a | C |
| R5 | IEEE CIFEr | VI | A | B | A | n/a | B |
| R6 | arXiv | VI | C | A | A | n/a | C |
| R7 | arXiv | VI | C | B | A | n/a | C |
| R8 | SSRN | VI | C | C | B | n/a | C |
| R9 | JRFM | VI | A | B | C | n/a | B |
| G1 | SIAM J. Financ. Math. | VI | A | A | B | n/a | A |
| G2 | Appl. Math. Finance | VI | A | B | A | n/a | B |
| G3 | Appl. Math. Finance | VI | A | C | B | n/a | C |
| G4 | ACM ICAIF | VI | A | B | A | n/a | B |
| G5 | ACM ICAIF | VI | A | B | A | n/a | B |
| G6 | SSRN | VI | C | A | A | n/a | C |
| G7 | Appl. Math. Finance | VI | A | A | B | n/a | A |
| G8 | AAAI | VI | A | A | C | n/a | A |
| C1 | Appl. Math. Optim. | VI | A | A | A | n/a | A |
| C2 | SSRN | VII | C | C | D | n/a | C |
| C3 | Quant. Finance | VI | A | A | A | n/a | A |
| C4 | Front. Math. Finance | VI | A | A | B | n/a | B |
| C5 | Rev. Deriv. Res. | VI | A | B | A | n/a | B |
| S1 | Quant. Finance | VI | A | A | A | n/a | B |
| S2 | Quant. Finance | VI | A | B | A | n/a | B |
| S3 | Wilmott | VI | D | B | A | n/a | C |
| S4 | J. Comput. Finance | VI | A | C | A | n/a | C |
| S5 | J. Financial Econometrics | VI | A | C | A | n/a | C |

Distribution of overall grades: A 11; B 13; C 17. Evidence-hierarchy levels: VI 40; VII 1. No source was graded F; the integrity floors described in Method were applied.

## Flagged sources

**Preprints (11; 26.8%).** P7 Klassen (2016), P8 Barski & Wiśniewolski (2026), N3 Ackerer et al. (2019), N5 Na et al. (2023), N6 Hoshisashi et al. (2023), R2 De March & Henry-Labordère (2019), R6 Buehler et al. (2026), R7 Alvarez (2025), R8 Zetocha (2023), G6 Anagha (2026), C2 Niu (2015)

**Partial abstracts (4).** R2 (partial, 307 chars), G3 (partial, 448 chars), C4 (partial, 323 chars), S1 (partial, 405 chars). Claims are limited to the retrieved fragment; R2's fragment is a publisher-deposited snippet, G3's is truncated mid-argument, C4's and S1's are short but state their result explicitly.

**Metadata-only (3).** P4, P7, R4. No abstract in OpenAlex, Crossref or Semantic Scholar. P7 is a preprint whose title asserts necessary and sufficient conditions; the claim is recorded as `assumption` and must never be cited as a proof. R4 (EJOR 2026) and P4 are peer-reviewed but unverifiable at abstract level.

**Other flags.** S3 is published in *Wilmott*, an editorially reviewed practitioner magazine, not a peer-reviewed journal; it is graded D on Peer review and C overall. R9 is in JRFM (MDPI, open access, APC model) - not predatory on the evidence available, but different from the society/Elsevier journals. N2 is an ICLR 2025 paper whose DOI is the arXiv version (10.48550/arxiv.2406.11520); it is graded as peer-reviewed on the venue but the DOI resolves to the preprint. N5 and N6 are arXiv-DOI records whose OpenAlex primary location points at RePEc; the venue is recorded as arXiv because the DOI prefix is arXiv and the abstract is the arXiv abstract. R7's OpenAlex author string is irregular ('Alvarez, Robert Jenkinson'); the citation uses the initialed form and is flagged. C5 is included with a scope flag: its panel is single stocks, not an equity index.

## Predatory-journal screening result

No predatory red flag was identified in the venue set at structural level: 23 journal articles in established finance, mathematics, operations-research and econometrics journals, 6 peer-reviewed conference papers (ICLR, AAAI, IEEE SSCI, IEEE CIFEr, ACM ICAIF), 11 preprints on SSRN/arXiv (which are not journals), and 1 practitioner magazine. Two caveats: (a) no live check against Beall's list, DOAJ or COPE membership was performed - the assessment is structural only; (b) JRFM is an APC-based open-access journal and publication there is noted, not penalised. This result is 'no red flags found under a limited check', not 'verified non-predatory'.

## COI disclosures

No conflict-of-interest or funding statement was retrieved for any of the 41 records, because abstracts and metadata do not carry them. `n/a` in the matrix means 'not retrieved', never 'none declared'. Several sources are authored by current or former industry practitioners (notably S3 and R9); affiliations were not verified, so no COI conclusion is drawn.

## Cross-source consistency checks

- **SVI conditions.** S1 gives sufficient conditions for static-arbitrage-free SVI; P2 completes the butterfly characterisation; P1 generalises the family; C2's review is consistent. P7 claims necessity and sufficiency at title level only and cannot be used as confirmation.
- **SABR asymptotics.** S3 reports that the explicit SABR implied-volatility formula can produce arbitrage at low strikes, while C4 proves the SABR formula is asymptotically arbitrage-free. The two are compatible only in the asymptotic regime C4 states; the finite-strike tension is a real constraint on how SABR-based surfaces may be used and is carried into Phase 3.
- **Violation-rate claims.** G6 (synthetic, tolerance 1e-4), G5 (90.8% pass rate), R5 (about 5.4% butterfly floor on SPX) and R7 (<1%) are mutually consistent as evidence that residual violations persist, but their magnitudes are not comparable and were not pooled.
- **Architectural guarantees.** G1, G7, G8 and G6 all place the guarantee in the network structure; their abstracts agree that the guarantee is static, not dynamic.

## Verification limitations

- Abstract-level verification only; method quality beyond what abstracts state is `not assessed`.
- No full-text, appendix or replication-material inspection; no check that proofs are correct.
- No COI, funding or affiliation retrieval; no author-credibility assessment beyond name-to-record attachment.
- Single-reviewer screening and grading; no dual review or calibration; PRISMA-style, not PRISMA-compliant.
- One discovery query failed with a transient 429 and was not re-run successfully; the pool is not exhaustive.
- Abstract augmentation depended on Crossref and Semantic Scholar availability; arXiv API was rate-limited and unusable during the run.
- Citation counts were deliberately not used or reported.

## Recommendation

**Proceed to Phase 3 (synthesis) under the conditional pass above.** Keep the four-family structure, label every claim with its evidence status, keep the three metadata-only records at title level, and do not let the recency of the 2023-2026 half of the corpus silently crowd out the parametric baselines. If a Phase 2 revision is possible, the highest-value additions are: full-text retrieval for P4/P7/R4, a second screener for a reliability check, and one discovery pass with a fixed-rate OpenAlex key to close the failed SVI query.
