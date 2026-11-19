# Stage 3 — Reviewer 1 (Methodology)

**Recommendation:** Major Revision

## Summary

The paper is a structured review of 40 sources. The method is transparent about its limits, but the screening flow is not auditable enough for the paper's reproducibility claims, and the evidence level does not support some of the comparative language.

## Strengths

- The search strategy, corpus counts, and abstract coverage are reported.
- The paper distinguishes peer-reviewed sources from preprints.
- The limitations section is unusually candid.
- The cross-paper tension table is a good device.

## Major issues

**M1. The 24 queries and the 351 → 40 screen are not fully auditable.** Appendix A describes the strategy, but the exact queries are only in `openalex_search.py`; the 311 non-advanced records are not listed or coded. Add a query log (24 rows: query, date, hit count) and a source-level inclusion table or a record-level excluded list. If a full excluded list is impractical, say so and give the category-level counts; do not call the flow PRISMA-compliant.

**M2. Evidence level and comparative claims.** Ten of 40 sources are preprints, and the paper reads abstracts, not full texts. Claims such as “neural surrogates reduce calibration time” and “violations can reappear under distribution shift” are plausible but not tested here. Mark them as reported claims, not findings, and add an evidence-level column to the corpus mapping (Appendix D).

**M3. The negative “no shared benchmark” finding needs a search-validation check.** A negative claim is only as good as the search. Add a short “search validation” paragraph: a Crossref title search for the 40 included titles, a check that the query set covers “dynamic arbitrage” and “calendar arbitrage,” and a statement that the absence is “in the retrieved abstracts,” not globally.

## Minor issues

- The 40/351 count is a rationale, not a PRISMA flow; label it consistently.
- The search date (2026-11-19) should appear in the abstract or method, not only in the appendix.
- The paper says “no full text” in several places; one statement plus a table note is enough.
- The 2027 issue year of Yao et al. (2026) should be explained (online-first vs issue year).

## What would make it acceptable

A query log, a 40-source evidence mapping, and a search-validation paragraph. These are documentation additions; no new search is required.
