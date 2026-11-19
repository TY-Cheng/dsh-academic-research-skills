# Stage 4.5 — Final Integrity Verification

**Manuscript:** `stage4-prime/paper-v3.md` (final pre-format version)  
**Date:** 2026-11-19 (Asia/Singapore)  
**Reviewer:** integrity verification (fresh pass, not a re-check of Stage 2.5)  
**Verdict: PASS — bounded coverage** (no blocking issue; seven advisories disclosed)

## Gate summary

| Phase | Check | Result |
|---|---|---|
| A | Reference integrity | 40/40 metadata resolved; 39 DOI + 1 HAL; 0 fabricated; 0 retracted; 20/40 abstract-level spot-check |
| B | Citation context | 40/40 references cited; 0 orphans; 0 dangling `src-` IDs; 40 unique IDs |
| C | Data and ethics | No original data; no human subjects; declarations present |
| D | Originality | No plagiarism scan available; synthesis is original; overlap with Stage 1 report disclosed |
| E | Claim verification | 10-claim sample checked at the paper’s stated evidence level; 0 unsupported; 2 overclaim candidates scoped |
| F | AI failure modes | 0 critical; 0 major; 2 minor copy/coverage advisories |

The gate passes because no blocking defect was found. The coverage is bounded: this is an abstract-level review of a frozen 40-source corpus, not a full-text systematic review.

## A. Reference integrity

- **40/40 references** have a resolvable record: 39 DOI, one HAL record (#39, no DOI). OpenAlex DOI lookup succeeded for all 40 in the original corpus build; Crossref metadata was retrieved for a subset; S2 was rate-limited (HTTP 429) at search time.
- **0 fabricated references.** Every reference corresponds to a record in `search/selected_sources.json`; no reference was added during revision.
- **0 retracted** according to the OpenAlex `is_retracted` flags at retrieval; no independent Retraction Watch check was possible.
- **30 peer-reviewed / 10 preprints**: preprints are #4, #5, #6, #24, #35, #36, #37, #38, #39, #40. Appendix B and Appendix D now use this count; the earlier 31/9 figure was corrected before Stage 4.
- **Abstract coverage**: 35 full, 4 partial (#9, #26, #28, #29), 1 title-level (#14). No full-text verification was performed for any source.
- **Spot-check**: 20/40 reference metadata (author, year, title, venue, DOI) matched the record; no mismatch found. The remaining 20 were checked at the record level only.

## B. Citation context

- 40 unique `src-01..src-40` markers in the manuscript; all 40 references are cited at least once; no orphan reference and no dangling marker.
- The in-text claims were spot-checked against the cited source’s abstract/metadata. The following claims are scoped as required:
  - “No shared benchmark was identified in the retrieved abstracts” — corpus-scoped, not a claim that none exists.
  - “Dynamic no-arbitrage is the frontier” — tied to Table 7 and the thin evidence, not a claim of consensus.
  - “Parametric methods are well-characterized, not solved” — retains the fit-limitation caveat.
  - No method ranking, no regulatory determination, no causal claim about enforcement families.
- #14 (Horvath et al., 2021) is cited for the calibration-map idea only; it is not used for a speed claim. The paper notes the title-level limitation in Appendix B and §4.4.

## C. Data and ethics

- No original empirical data; no human subjects; no consent or IRB requirement. The corpus is frozen in `search/selected_sources.json`; the query log is Appendix E; the screening rationale is Appendix C.
- Declarations present: Data Availability, Ethics Declaration, CRediT, COI, Funding, AI-use statement, Limitations.
- COI/funding: no funding; no declared COI; a full COI audit was not possible from metadata. The AI-use statement says AI assisted with corpus construction, synthesis, and editing, and that findings were checked at the metadata/abstract level — not that a full-text or plagiarism audit was performed.

## D. Originality

- No plagiarism or similarity scan was available in this environment; the paper does not claim one. The synthesis, taxonomy, decision guide, and propositions are original to this review; the Stage 1 report is the authors’ own prior draft and is disclosed as the evidence base.
- The literature review does not reproduce long passages from sources; quotations are absent or short and attributed.

## E. Claim verification (sample)

| Claim | Evidence level | Result |
|---|---|---|
| SVI/SSVI/eSSVI admit explicit static-arbitrage conditions | Theoretical/peer-reviewed | Supported |
| Neural methods use soft/hard/projection/generation mechanisms | Abstract-level, 30 peer + 10 preprints | Supported at abstract level |
| No shared benchmark identified in retrieved abstracts | Corpus-scoped | Supported as scoped |
| Dynamic evidence is thin (five candidates) | Table 7 | Supported |
| 30 peer-reviewed / 10 preprints | Appendix B/D | Supported |
| 40 sources, 7/6/18/8/1 buckets | Appendix B | Supported |
| Evaluation dimensions are fragmented | Table 4 | Supported at abstract level |
| No method ranking is warranted | Argument | Supported |
| The guide is proposed, not validated | Table 7/§5.3 | Supported |
| Regulatory use is not established | §5.3/§5.4 | Supported |

Two overclaim candidates were found and already scoped: “no shared benchmark” (corpus-scoped) and “frontier” (tied to Table 7). No unsupported factual claim was found in the sample.

## F. AI failure-mode checklist

| Mode | Finding |
|---|---|
| Fabricated evidence | 0 |
| Citation distortion | 0 in sample; #14 scoped |
| Scope overreach | 0 blocking; two claims scoped |
| Numeric inconsistency | 0: 40 sources; 30/10; 39 DOI + 1 HAL; 6,804 body; 216 abstract; 8 tables; 40 Appendix D; 24 Appendix E |
| Hidden contradiction | 0 blocking; CP-004 indirect is disclosed |
| Plagiarism | Not assessed (no scanner); disclosed |
| Methodology fabrication | 0; the review-type box says not systematic/not PRISMA |

## Advisories (non-blocking)

1. **Abstract-level evidence** for most sources; no full-text verification. Claims are labelled accordingly.
2. **10 preprints** (25%); peer-reviewed share is 75%, above the 60% threshold, but the neural/generative evidence is preprint-heavy.
3. **#14 title-level**; not used for a speed claim.
4. **S2 unavailable** (HTTP 429) at search time; reference existence relies on OpenAlex/Crossref, not S2.
5. **No plagiarism/similarity scan**; no full COI audit.
6. **No dual screening**; 311 non-advanced records were not individually coded (Appendix C).
7. **No independent replication** of the query set; the corpus is frozen and the query log is provided.

## Final gate decision

**PASS — bounded coverage.** The manuscript may proceed to Stage 5 finalization with the advisories above. The final paper must retain the corpus-scoped language, the review-type box, the proposed-status labels, and the AI-use qualifier.
