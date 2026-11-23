# Phase 2 screening summary (PRISMA-style, not PRISMA-compliant)

Run directory: `examples/dsh/iv-surface-review-v047/`. Discovery date: 2026-11-23.
Screening level: title for the full pool, abstract for the included set only.
Reviewer model: a single research agent (no dual screening, no kappa).

## Flow

```
Records identified through OpenAlex API (31 queries x 25 records/query; one query returned none after retry)
  pool after cross-query deduplication ......... 430
  excluded at title screening .................. 389
  included ..................................... 41
     abstracts read for confirmation ............ 41
     replaced during abstract-level reading ..... 2 (documented in the screening log)
```

Two records were replaced after abstract-level reading, because the title
matched the topic but the abstract did not fit the research question:

- N2 (old): Liu, Oosterlee & Bohte (2019), *Pricing options and computing
  implied volatilities using neural networks* (Risks) - no arbitrage-enforcement
  claim; replaced by Wiedemann, Jacquier & Gonon (2025). Reason code in the log:
  `RELEVANT_NOT_SELECTED` with the replacement note.
- C4 (old): Wang, Zhao & Bao (2018), *Arbitrage-free conditions for implied
  volatility surface by Delta* - FX-market empirics, outside the equity-index
  scope; replaced by Fukasawa (2022). Reason code: `OUT_OF_SCOPE_ASSET`.

The log stores the post-replacement state; both removed records remain visible
with their overrides rather than being silently reclassified by the generic
title rules.

## Reason codes and counts

| Reason code | n | Meaning |
|---|---|---|
| DUPLICATE_VERSION | 31 | Duplicate/alternate version (same DOI or near-identical title) of another pool record. |
| PRE_2015_BACKGROUND | 86 | Published before 2015; outside the 2015-2026 window. Retained as background knowledge only (older seminal works enter the corpus only through the explicitly flagged baseline set). |
| PUBLICATION_TYPE | 32 | Dissertation, book, software/replication package, review, paratext or other grey-literature type not eligible as a peer-reviewed/preprint research source. |
| NON_ENGLISH | 0 | Not written in English. |
| OUT_OF_SCOPE_ASSET | 34 | Underlying is not an equity index (FX, rates, commodities, energy, crypto, single-name equity, or a non-financial domain). |
| OFF_TOPIC | 141 | Title is not about implied-volatility/option-price surface construction or its arbitrage constraints. |
| FORECASTING_OR_TRADING | 21 | Surface forecasting, hedging or trading application rather than a construction/enforcement method. |
| MODEL_CALIBRATION_PRICING | 4 | Stochastic-volatility model calibration, asymptotics or option pricing without surface-construction enforcement. |
| RELEVANT_NOT_SELECTED | 40 | Topically relevant at title level but not selected: corpus cap (35-45), family balance, recency/version precedence, or already represented by a stronger record in the same family. |

The 40 `RELEVANT_NOT_SELECTED`
records are a real cap-and-balance bucket, not noise: they are topically
relevant titles that lost to corpus-size limits (35-45), family balance or
version precedence. They are disclosed as a selection-bias guard in the
bibliography and are the first place to look if the corpus is expanded.

## Screening limitations

- Title-level decisions use keyword rules; they are reproducible but not
  semantic, so some off-topic titles may sit in `OFF_TOPIC` for the wrong
  sub-reason.
- No dual screening, no adjudication, no inter-rater reliability; this is
  PRISMA-*style* reporting only.
- One discovery query failed even after retry (`SVI stochastic volatility
  inspired`, transient OpenAlex 429), so the pool is not exhaustive.
- OpenAlex language tags were unreliable (two English papers are tagged `it`), so language was checked at title/abstract level; the one Korean record was already outside the 2015-2026 window. No translation screening.
