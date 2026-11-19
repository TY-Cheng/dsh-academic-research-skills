# Phase 5 — Editorial Review

**Manuscript:** Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches  
**Reviewer role:** Editor-in-Chief (Q1 journal standard)  
**Date:** 2026-11-19  
**Input:** `phase4-report.md` (Phase 4 draft)

## Editorial Review

### Overall Assessment

**Verdict:** Minor Revision  
**Weighted Score:** 3.05 / 5.0

The manuscript is a useful, clearly written structured review with a genuine organizing contribution: the four-family enforcement taxonomy and the seven-dimension evaluation matrix. Its main weakness is not prose but evidence discipline at the edges: one citation is used beyond its verified abstract, the taxonomy's categories overlap without a primary-mechanism rule, and the selection of 40 records from 351 is not reproducible from the manuscript. These are fixable in one revision loop without new data.

### Dimension Scores

| Dimension | Weight | Score | Notes |
|-----------|--------|-------|-------|
| Originality & Contribution | 20% | 3.0 / 5 | The taxonomy and evaluation matrix are useful synthesizing contributions, but the review does not test them or offer a new empirical result. |
| Methodological Rigor | 25% | 2.5 / 5 | The search is transparent and the script is supplied, but screening is single-pass, the 311 non-advanced records are not logged, and no full text was read. Appropriate for a structured review, below the bar for a systematic review. |
| Evidence Sufficiency | 25% | 2.5 / 5 | 40 sources, 30 peer-reviewed, 10 preprints; abstract-level evidence; one title-level record used inconsistently. The claims are mostly hedged, but some recommendations outrun the evidence. |
| Argument Coherence | 15% | 4.0 / 5 | The RQ → taxonomy → findings → discussion chain is clear; the static/dynamic distinction is sustained; the “no ranking” stance is consistent. |
| Writing Quality | 15% | 4.0 / 5 | Clear, well-structured, APA-style; some long paragraphs; tables are effective. Minor line editing needed. |

**Weighted calculation:** (3.0×0.20) + (2.5×0.25) + (2.5×0.25) + (4.0×0.15) + (4.0×0.15) = 0.60 + 0.625 + 0.625 + 0.60 + 0.60 = 3.05.

### Strengths

1. **A real organizing contribution.** The four-family enforcement taxonomy (construction, penalty, projection/repair, generation+filter) gives the reader a way to compare papers that use the same phrase for different guarantees. The seven-dimension evaluation matrix in Table 3 is the most practically useful part of the manuscript.
2. **Honest limitations.** §5.4 does not hide the 40/351 selection, the 10 preprints, the abstract-level evidence, or the Semantic Scholar 429s. The limitations are substantive rather than performative.
3. **Consistent anti-ranking discipline.** The manuscript repeatedly refuses to declare a winning method and explains why the evidence cannot support one. This is the right stance for the corpus.
4. **Citation coverage and structure.** All 40 sources are cited, the reference list is complete, and the appendix corpus index makes the evidence base auditable.

### Required Revisions

#### Critical

- None. No flaw invalidates the core argument.

#### Major

- [ ] **M1 — Horvath et al. (2021) is used beyond its verified evidence.** §2.3 and §4.3 cite Horvath et al. for reduced calibration time, while §4.4 correctly says the record is title-level only. Remove Horvath from the calibration-speed parentheticals, or explicitly label the citation as title-level and non-substantive. The current wording creates an internal contradiction that a hostile reviewer will find.
- [ ] **M2 — The four enforcement families are not mutually exclusive.** §2.6 and Table 2 present construction, penalty, projection/repair, and generation+filter as if each method belongs to one family. A two-step method is penalty + projection; a generative model with a repair step is generation + projection. Add a primary-mechanism rule (“classify by the mechanism that carries the guarantee”) and name hybrid cases. Otherwise the taxonomy is descriptively useful but analytically ambiguous.
- [ ] **M3 — The 40/351 selection is not reproducible from the manuscript.** §3.3 and Appendix A report the counts but not the excluded-record log or the screening rules that produced the 40. Add a screening-rationale table (counts by exclusion reason, even if reconstructed), state that the 311 records were not individually coded, and add a reproducibility note. Do not present the flow as PRISMA-compliant; the manuscript already says it is not, but the method section should make the gap explicit.

#### Minor

- [ ] **m1 — The regulatory sentence in §5.3 overreaches.** “For regulators, the absence of a shared benchmark is a supervisory gap” is a policy conclusion the corpus cannot support. Soften to “may warrant supervisory attention” and add “this review does not evaluate regulatory practice.”
- [ ] **m2 — CP-004 in Table 4 is an indirect pairing.** Cohen et al. (2020) is a repair study, not a direct test of generated surfaces. Label the pair “indirect tension” and explain that the conflict is between generative claims and the absence of independent validation, not a direct contradiction between the two papers.
- [ ] **m3 — “Three broad families” and the four-family taxonomy need an explicit axis sentence.** §1.1 introduces three method families; §2.6 introduces four enforcement families. Add one sentence in §1.1 or §2.6: the three method families and the four enforcement families are different axes, and one method family can use more than one enforcement mechanism.
- [ ] **m4 — Line editing and date consistency.** Tighten the long §4.3 paragraph; check 2026/2027 venue dates against the bibliography; ensure all table captions use the same style.

### Suggestions (Optional)

- Add a short worked example applying the taxonomy to one paper (e.g., Zhang et al., 2022 as penalty + projection) in §2.6. It would make the primary-mechanism rule concrete.
- Add a “What this review can and cannot support” paragraph before §6. It would pre-empt the strongest counter-argument and make the contribution boundary explicit.
- Consider a small figure mapping method families to enforcement families; the text currently carries the whole taxonomy.

### Line-Level Feedback

| Section | Issue | Recommendation |
|---------|-------|----------------|
| Abstract | “No shared benchmark … was identified in the retrieved abstracts” is correctly qualified; keep it, but ensure the conclusion and Table 4 use the same qualifier. | Keep “in the retrieved abstracts”; do not let later sections drop it. |
| §1.1 | “Three broad families dominate construction” versus four enforcement families in §2.6. | Add the axis sentence (m3). |
| §2.3 / §4.3 | Horvath et al. (2021) cited for calibration speed while §4.4 calls it title-level. | Remove from speed claim or label title-level (M1). |
| §2.6 / Table 2 | The four families read as mutually exclusive. | Add primary-mechanism rule and hybrid examples (M2). |
| §3.3 / Appendix A | 40/351 with no excluded-record log or screening rules. | Add screening-rationale table and reproducibility note (M3). |
| §4.7 / Table 4 | CP-004 pairs a generative study with a repair study as a direct tension. | Relabel as indirect tension (m2). |
| §5.3 | “Supervisory gap” is a regulatory conclusion. | Soften and scope (m1). |
| References | 40 entries, complete; check 2026/2027 dates. | Date-consistency pass (m4). |

### Summary

This is a solid structured review with a clear contribution and unusually honest limitations. The revision is minor in scope but not cosmetic: the Horvath citation must be made consistent, the taxonomy needs a primary-mechanism rule, and the screening flow needs a reproducibility note. If those three are addressed, the manuscript would be a credible map of the evidence—not a ranking of methods, which it rightly refuses to provide. I would not accept it as a systematic review, and the manuscript should continue to say so.

---

**Phase 5 note:** This editorial review is one of three parallel Phase 5 inputs. The ethics review and Devil's Advocate checkpoint 3 are separate artifacts; their findings should be combined in Phase 6.
