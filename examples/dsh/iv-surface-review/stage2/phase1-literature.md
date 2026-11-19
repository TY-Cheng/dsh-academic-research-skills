# Phase 1 — Literature and Evidence Handoff

## Decision

Phase 1 reuses the Stage 1 `deep-research` corpus. No new search is run.

- 40 frozen sources: 30 peer-reviewed articles or conference papers; 10 preprints.
- 28 sources (70%) from 2021–2026; 12 (30%) older, including seminal 2009–2014 work.
- Method mix: neural/generative 18; constraints/evaluation 8; parametric 7; nonparametric 6; dynamics 1.
- Abstract coverage: 35 full, 4 partial, 1 title-level only (Horvath et al., 2021).
- 40/40 resolved through OpenAlex; 39 DOI; 1 HAL record without DOI; 0 flagged retracted; 0 fabricated.
- Search: 24 OpenAlex full-text queries; 351 unique records; 40 retained after title/abstract screening; 311 not individually coded; no full text read.

## Why no new search

The Stage 1 search already covers the paper's question and the paper is a review, not a new empirical study. Re-running the search would create a second, inconsistent corpus. The reproducibility limits are disclosed in §3.7, §5.4, Appendix A, and Appendix C.

## Evidence boundary

The corpus is abstract-level. It supports claims about reported mechanisms, reported evaluation dimensions, and the absence of a shared benchmark in the retrieved abstracts. It does not support full-text method audit, effect-size synthesis, or claims about implementation quality. The 10 preprints are labeled in the corpus and are weaker evidence than the peer-reviewed records.

## Handoff paths

- `../phase6-final.md` — Stage 1 final report.
- `../phase2-bibliography.md` — annotated bibliography and search strategy.
- `../phase2-verification.md` — source verification matrix.
- `../phase3-synthesis.md` — synthesis and cross-paper tensions.
- `../search/selected_sources.json` — frozen 40-record corpus.
- `../search/openalex_search.py`, `../search/fetch_selected.py` — search and selection scripts.
