# Stage 3′ — Re-Review (Verification)

**Input:** `stage4/paper-v2.md`; `stage4/response-to-reviewers.md`; `stage3/revision-roadmap.md`  
**Mode:** verification re-review — does the revision address each Stage 3 major issue?  
**Verdict: Minor Revision** (no new major issue; two copy-edit fixes)

## Verification against the roadmap

| # | Issue | Status | Evidence |
|---|---|---|---|
| R1 | Audience/venue | Addressed | §1.5 names the model-risk/model-validation analyst and the review-venue type; abstract remains corpus-scoped. |
| R2 | Review type | Addressed | §3.1 boxed statement: structured narrative, not systematic, not PRISMA, not registered. |
| R3 | Query log | Addressed | Appendix E has 24 rows with query, OpenAlex matches, retrieval count, date. |
| R4 | 40-source mapping | Addressed | Appendix D has 40 rows: source, method family, enforcement family, static/dynamic test, evidence level. |
| R5 | Dynamic table | Addressed | Table 7 lists five dynamic candidates and what each reports; “frontier” is tied to the table. |
| R6 | Testable propositions | Addressed | Table 8 has six propositions with support and falsification conditions; §5.2 adds “what would change this map.” |
| R7 | Proposal status | Addressed | Table 5 and §5.3 label the guide proposed, not validated; use case and warning added. |
| R8 | Scope/excluded streams | Addressed | §3.6 names rough vol, stochastic-vol calibration, American options beyond one source, crypto/FX, RL. |
| R9 | Minor | Partial | JEL/running head added; Appendix B year note claimed in the response but not found in `paper-v2.md`; table numbers are out of order. |

## Remaining issues

### Minor 1 — Table numbering is not sequential

The new tables were inserted in argument order: the sequence in the document is Table 1, Table 2, **Table 7**, Table 3, Table 4, **Table 8**, Table 5, Table 6. The text references are consistent with the labels, but a reader cannot follow the numbering. Required: renumber all tables in order of appearance and update every in-text reference and table note. No content change.

### Minor 2 — Online-first year note is missing from Appendix B

The response says Appendix B notes that online-first articles are cited by online-first year and that the print issue year may be later (#26, #29). The current Appendix B has the rubric note but not the year convention. Required: add one sentence to the Appendix B note. No content change.

### Non-blocking observations

- The paper repeats the no-ranking rule in §1.5, §5.1, §5.3, and §6. This is defensible; one instance may be trimmed at copy-edit, but it is not required.
- Appendix D’s mapping is interpretive; the note says so. The evidence levels now match the 30/10 count.
- The response is accurate on R1–R8. It overstates R9’s year note and does not mention the table-order issue; both are copy-edit fixes, not substantive.

## Recommendation

Accept the response as substantively complete. Apply the two copy-edit fixes in a Stage 4′ revision (`paper-v3.md`) and proceed to Stage 4.5 final integrity. No new search, no new corpus, no new review loop required for the minors.

**Residual limits (unchanged):** abstract-level evidence for most sources; 10 preprints; #14 title-level; no full text; S2 429 at search time; no plagiarism scan; no full COI audit. These are disclosed in the paper and the integrity reports, not resolved.
