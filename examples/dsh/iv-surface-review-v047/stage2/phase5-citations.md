# Phase 5a — Citation Compliance Report

**Target:** `paper-draft.md` (v1.1), body sections 1–7, Tables 1–6, Figures 1–2, Declarations, References, Appendices A–C.
**Style:** APA 7.0. **Corpus:** the 41 frozen Stage 1 sources; no reference was added, removed, renumbered, or rewritten.
**Checker note:** this fork has no standalone APA orphan/reference auditor under `scripts/`; the three-layer emission lint (`scripts/check_v3_7_3_three_layer_citation.py`) and the procedural cross-check specified in `agents/citation_compliance_agent.md` §1 (In-Text ↔ Reference List Cross-Check) were run, the latter scripted over the manuscript. Results are below.

## Summary

| Item | Result |
|---|---|
| Sources in corpus | 41 |
| Distinct corpus IDs cited in text | 41 |
| Reference entries | 41 |
| Uncited reference entries (orphans) | 0 |
| In-text citations with no reference entry | 0 |
| Unknown / out-of-corpus slugs | 0 |
| Preprint entries | 11, each marked `[preprint]` once at first in-text mention; `[Preprint]` tag retained in all 11 entries |
| Self-citation ratio | 0 / 41 (no entry authored by TY-Cheng) |
| DOIs present and resolvable in form | 41 / 41 (`https://doi.org/…` trailing each entry) |
| Reference list alphabetical order | verified, 41 / 41 |
| Three-layer emission lint | PASSED, exit 0 |
| Multi-source parenthetical ordering | 8 groups reordered alphabetically (APA 7 §8.12); 5 already compliant |
| Auto-corrections applied | 9 (8 orderings, 1 apostrophe normalisation) |
| Items flagged for review (not auto-corrected) | 4 |

## Corrections Made

1. **Multi-source parenthetical ordering (APA 7 §8.12), 8 groups reordered.** Works inside one parenthetical are ordered alphabetically by first author surname. Reordered groups, with the pre-correction order shown: §2.1 `Gatheral → Martini → Anagha` became `Anagha → Gatheral → Martini`; §2.1 `Xiong → Bajalica` became `Bajalica → Xiong`; §2.3 `Cohen → Andrès` became `Andrès → Cohen`; §5.1 `Sidogi → Na → Xiong` became `Na → Sidogi → Xiong`; §5.1 `Ning → Anagha → Cohen → Yang` became `Anagha → Cohen → Ning → Yang`; §6.1 `Sidogi → Na` became `Na → Sidogi`; §6.2 `Bajalica → Anagha` became `Anagha → Bajalica`; §6.2 `Hagan → Fukasawa` became `Fukasawa → Hagan`. Segment text, ref markers, and anchor markers were moved as units, so every `<!--ref:-->` stayed adjacent to its `<!--anchor:-->` (lint re-run PASSED). The five remaining multi-source groups were already alphabetical and were left untouched.
2. **Apostrophe normalisation, 3 occurrences.** In-text `Le Floc'h` (U+0027) normalised to `Le Floc’h` (U+2019) to match the reference entry and the corpus record. No other name form differed between text and list.

No citation was added, deleted, renumbered, or re-attributed; no sentence was rewritten for content; no non-APA convention was altered.

## Items Flagged for Review

1. **Four reference entries carry a bracketed printed-issue-year note after the DOI** (Cohen et al., 2021; Fengler et al., 2006; Gatheral & Jacquier, 2013; Vuletić & Cont, 2024). APA 7 ends a reference with the DOI, so the trailing bracket is a provenance marker rather than an APA element. It was left in place because the notes record a verified online-versus-print year difference and deleting them would lose auditable information; a venue that enforces strict APA might ask for the note to move into a table note. Author decision, not an auto-correction.
2. **Three metadata-only rows are cited at title level** (P4, P7, R4). The citations are APA-correct, but the evidence behind them is unverified; §4.1 marks them as claims rather than evidence, and Appendix C records the metadata-only status.
3. **No page locators accompany any citation.** Page anchors would be fabricated at abstract level, so every anchor is `section:`-kind. The three-layer lint accepts this; a reviewer who requires page-level anchors for quotations will find none because the manuscript quotes no source verbatim.
4. **`[preprint]` appears in-text once per preprint rather than at every citation.** APA does not govern in-text preprint labelling; the convention is stated here so a reader does not read a later unmarked citation as a peer-reviewed claim. Each of the 11 entries also carries `[Preprint]` in the reference list, and Appendix B carries a peer-reviewed column for every row.

## Cross-Check Detail

**In-text → reference list.** Every visible citation was paired with its `<!--ref:ID-->` slug and compared against the corpus record's author string and year: 112 slug occurrences, 41 distinct IDs, 0 mismatches. Parenthetical and narrative forms both resolve: 2 narrative two-author forms use "and" (`Gatheral and Jacquier (2013)`, `Martini and Mingone (2022)`), parenthetical forms use `&`, three-or-more-author sources use `et al.` at first citation, and no two-author source is cited with `et al.` (13 two-author sources checked).

**Reference list → in-text.** All 41 entries are cited at least once. Recency is uneven by design: P2, N4, N5, R5, and G6 are cited in five or more sections (Appendix B lists the exact section map per row), while the metadata-only rows appear only where their claim is discussed.

**Format integrity.** All 41 entries have author–year–title–venue structure, 32 use the `, & ` last-author connector (the remaining 9 have a single author or are formatted as such in the Stage 1 list), italic markers are balanced in every entry, and every entry ends with a resolvable DOI. Journal names are italicised, volume numbers are italicised with the issue in parentheses, and the four entries without an issue number follow the continuous-volume form.

**Style consistency.** No Chicago, MLA, or numeric citation forms appear; no `[1]`-style markers; no "ibid."; no bare URLs without DOI. In-text citations of corporate or anonymous sources do not occur in this corpus, so no organisational-author variants were needed.

**Items not verifiable here.** DOI resolution was checked as URL form only — the underlying records were resolved during Stage 1 (41/41, none retracted). No reference's page range, volume, or issue was re-checked against a publisher record in this phase; those fields were frozen from Stage 1 and are certified there, not here.
