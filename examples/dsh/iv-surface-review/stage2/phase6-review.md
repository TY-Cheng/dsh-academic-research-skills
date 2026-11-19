# Phase 6 — Internal Peer Review

**Manuscript:** *Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches*  
**Version reviewed:** v1.1  
**Reviewer:** internal academic-paper Phase 6 panel (single reviewer, five dimensions)  
**Date:** 2026-11-19

## Dimension scores

| Dimension | Score | Note |
|---|---:|---|
| Originality | 3.5/5 | The guarantee taxonomy and static/dynamic separation are useful; the paper is a review, not a new theory. |
| Methodological rigor | 3.0/5 | Single database/date, 40/351 selection, abstract-level evidence, 10 preprints; disclosed but not repaired. |
| Evidence sufficiency | 3.0/5 | 40 sources, 30 peer-reviewed; enough for a map, not for ranking or causal claims. |
| Argument coherence | 4.0/5 | The central argument is clear; v1.1 had duplicated passages in §5–§6. |
| Writing quality | 3.5/5 | Clear but long; some repetition; tables 5–6 were unnumbered. |

**Overall:** 3.4/5 — **Major Revision** in one loop, then accept for Stage 2.5.

## Issues

### Major

**M1. Duplicated passages in the Discussion/Conclusion.** §5.3 repeated the practitioner/benchmark/regulator sentences; §5.4 repeated the limitations; §5.5 repeated the six gaps; §6 repeated the conclusion. This inflated the body and weakened the argument.  
**Fix applied in v1.2:** removed the repeated tails; kept one statement of each claim; body 6,396 → 6,315 words. The body remains within 6,000–8,000.

**M2. Tables 5 and 6 were unnumbered.** The decision guide and research agenda were presented as bare tables.  
**Fix applied in v1.2:** added `Table 5` and `Table 6` captions; the paper now has six numbered tables.

**M3. Screening reproducibility is asserted but not fully auditable.** The paper reports 351 → 40 and 311 not advanced, but the 311 are not individually coded and the 24 queries are only in the search script.  
**Fix applied in v1.2:** §3.7 and Appendix C state the rationale and the limits. The external review may still ask for a query log and a source-level mapping; those are carried to Stage 3/4 as an expected revision, not hidden.

**M4. Dynamic no-arbitrage evidence is thin.** Only a handful of sources engage dynamic consistency, and the “frontier” claim is corpus-scoped.  
**Fix applied in v1.2:** §4.4 explicitly says the label is about this corpus; the claim is “static necessary but not sufficient.” A dynamic-evidence table is carried to Stage 4 if the external reviewers ask.

**M5. The target venue is vague.** “General academic journal / arXiv-style” is not a venue decision; the contribution framing may not fit a top finance journal without a sharper “so what.”  
**Fix applied in v1.2:** §1.5 states the modest contribution and the review’s positioning. Venue selection remains a Stage 5 formatting/positioning decision; the paper does not claim a specific journal fit.

**M6. Abstract-level evidence and 10 preprints.** The paper cannot support full-text method claims, and the neural evidence is preprint-heavy.  
**Fix applied in v1.2:** §5.4 and the abstract disclose the evidence boundary; the 10 preprints are labeled; no full-text claim is made. This is a scope limitation, not a fixable defect.

### Minor

- m1. The title is long; acceptable for a review, but the running head should be shorter.
- m2. JEL codes are absent; add at Stage 5 if the venue requires them.
- m3. The Chinese abstract is a deliberate zh-CN deviation from the skill's zh-TW default; disclose in the Stage 5 process record.
- m4. The “seven dimensions” are sometimes called a “matrix”; standardize the term in Stage 4 copy-edit.
- m5. The decision guide is a proposal; keep the “proposed, not validated” wording in every reuse.

## Verdict

**Major Revision (one loop), revision applied.** v1.2 resolves M1–M2 and bounds M3–M6. The paper is ready for Stage 2.5 integrity with the following residual risks carried forward: single-database/abstract-level evidence, 40/351 selection, 10 preprints, no full-text/COI/plagiarism audit, and a corpus-scoped “no shared benchmark” claim. These are disclosed, not converted into a PASS claim.
