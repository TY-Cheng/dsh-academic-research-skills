# Response to Reviewers — Stage 4

**Manuscript:** *Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches*  
**Decision addressed:** Major Revision (Stage 3 editorial, 2026-11-19)  
**Revised manuscript:** `stage4/paper-v2.md` (body 6,804 words; 40 references)  
**Rule:** no new search, no new corpus, no method ranking.

## Summary of changes

The revision adds the six elements the panel asked for: an explicit reader/venue statement (§1.5), a review-type box (§3.1), a 24-query reproducibility log (Appendix E), a 40-row source-level taxonomy mapping (Appendix D), a dynamic-evidence table (Table 7), and a propositions/falsifier table (Table 8). It also adds the scope paragraph (§3.6), the decision-guide use case and warning (§5.3, Table 5), JEL codes and a running head, and it corrects the evidence levels in Appendix B to the 30 peer-reviewed / 10 preprint count used throughout the paper. No source was added or removed; the corpus remains frozen at 40.

## Point-by-point

### Editorial and Journal-Fit

**J1 — Audience and venue.** The primary reader is now named in §1.5: a model-risk/model-validation analyst or benchmark designer, reading a general finance/quant-finance review venue. The paper no longer implies a top-three empirical-journal contribution.

**J2 — “Proposed” status of the decision guide.** Table 5 and §5.3 now state that the guide is a proposed aid, not a validated selection rule or a ranking. The table note repeats the warning.

**J3 — Abstract contribution.** The abstract keeps the corpus-scoped framing (“this review links…”) and §1.5 states the contribution as a taxonomy plus an evaluation frame, not a new empirical result. No new claims were added.

### R1 — Methodology

**M1 — Reproducibility of the 40/351 selection.** Appendix E lists all 24 OpenAlex queries with total matches, retrieval count, and date; Appendix C states that the 311 non-advanced records were not individually coded. §3.7 now points to both appendices and calls the flow a screening rationale, not a record-level audit. Re-running the search is possible from `search/openalex_search.py`; the included corpus is frozen in `selected_sources.json`.

**M2 — Evidence/taxonomy mapping.** Appendix D maps all 40 sources to method family, enforcement family, static test, dynamic test, and evidence level. The mapping is explicitly interpretive and classifies hybrids by the mechanism that carries the guarantee. Appendix B’s evidence levels were corrected: the 10 preprints are 4, 5, 6, 24, 35, 36, 37, 38, 39, and 40; the remaining 30 are VI.

**M3 — Validation of the search.** The revision does not add a second database or dual screening. It states the limitation, adds the query log, and narrows the claims to the retrieved corpus. No PRISMA or systematic-review claim is made.

### R2 — Domain

**D1 — Appendix D and the taxonomy.** Appendix D is the requested source-level table; Table 2’s note states the primary-mechanism rule for hybrids. The four families are presented as an organizing device, not as mutually exclusive natural kinds.

**D2 — Dynamic evidence.** Table 7 lists the five dynamic-consistency candidates in the corpus and states what each actually reports. The “frontier” label is tied to that table and to the thinness of the evidence, not to a claim that the literature has converged.

**D3 — Scope.** §3.6 names the excluded streams (rough volatility, stochastic-volatility calibration, American options beyond one source, crypto/FX, reinforcement learning) and states that the 40-source corpus is the boundary of the claims.

### R3 — Perspective

**P1 — Review type.** §3.1 now has a boxed statement: structured narrative review, frozen corpus, not systematic, not PRISMA-compliant, not registered.

**P2 — Proposal status.** The seven-dimension matrix and the decision guide are labelled proposed; §5.3 and Table 5 say they are not validated instruments.

**P3 — So-what and use case.** §5.3 adds a concrete desk use case (SVI construction vs neural generator, guarantee vs flexibility) and a warning that the guide does not validate either choice. Table 8 turns the map into six testable propositions.

### Devil’s Advocate

**DA1 — Falsifiability.** Table 8 gives support and falsification conditions for six propositions; §5.2 adds “what would change this map” (a fifth mechanism, a static-to-dynamic implication result, or a full-text reclassification of a substantial share of the corpus).

**DA2 — Selection and aggregate claims.** The revision keeps the 351 → 40 count transparent, states that the 311 were not individually coded, and confines claims to the 40 included sources. It does not claim the corpus is exhaustive.

**DA3 — No ranking.** The paper repeats the no-ranking rule in §1.5, §5.1, §5.3, and §6. The repetition is deliberate; the final copy-edit can trim one instance without changing the claim.

### Minor comments

- **JEL/running head:** added (`G13, C45, C63`; “Which Guarantee?”).
- **Online-first years:** Appendix B now notes that online-first articles are cited by online-first year; the print issue year may be later (#26, #29).
- **zh-CN abstract:** retained; the English abstract remains the primary abstract.
- **Repeated “no ranking”:** kept in the argument; one instance may be trimmed at copy-edit.
- **Table numbering:** the new tables were inserted in argument order; numbering will be normalized sequentially at the Stage 4′ copy-edit.

## Verification

- Body 6,804 words (within 6,000–8,000).
- 40 references; 40 cited; 0 orphans (Stage 2.5 and Stage 4 checks).
- Appendix D 40 rows; Appendix E 24 rows.
- No new search results; no new citations.
- Residual limits unchanged: abstract-level evidence for most sources, 10 preprints, one title-level source (#14), no full-text screening, S2 unavailable (429), no plagiarism scan, no full COI audit.
