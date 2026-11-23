# Run log — ARS v3.24.4 end-to-end validation (v0.4.7 content)

- Date: 2026-11-23 (Asia/Singapore)
- Repo: `/Volumes/ExternalSSD/projects/dsh-academic-research-skills/fork`, commit `19f11de` (sync to ARS `v3.24.4`, plugin `0.4.7`)
- Instruction source: vendored ARS v3.24.4 skill/agent files read directly from the fork. The installed desktop plugin (0.4.6) was NOT used; its loaded skill text is stale.
- Operator authorization: unattended e2e. The operator preauthorized the run through Stage 5 (same pattern as `examples/dsh/iv-surface-review`). Recorded checkpoint replies: "确认" / continue, including the §921 review-form note (continue current work; no separate review form; no PRISMA claim).
- Python: `fork/.venv/bin/python` (requirements-dev installed 2026-11-23).
- Toolchain note: xelatex/pdflatex present at `/Library/TeX/texbin/`; `pandoc` NOT installed → DOCX unavailable unless installed later; record as limitation.

| Stage | Status | Notes |
|---|---|---|
| S1 P1 SCOPING | done | RQ + FINER 4.0 + methodology + DA checkpoint PASS (3 major fixes into P2); review-form note recorded |
| S1 P2 INVESTIGATION | done | 41 sources (8/6/9/8/5/5), 29 peer-reviewed + 11 preprints + 1 practitioner; 34 full abstracts / 4 partial / 3 metadata-only; verification conditional pass |
| S1 P3 ANALYSIS | done | 41-row matrix, 7 themes, 8 tensions, 7 gaps, DA CP2 PASS (3 major fixes closed) |
| S1 P4 COMPOSITION | done | 5,247-word APA report; citation checker PASS |
| S1 P5 REVIEW | done | editorial MAJOR REVISION (7M/19m/27 line); ethics CONDITIONAL (7 conditions); DA REVISE (0C/7M/10m) |
| S1 P6 REVISION | done | phase6-final.md 5,596 words; 55 review items → 50 fixed / 4 partly / 1 pushed back |
| S2 WRITE | done | paper-draft.md v1.2 7,629 words; evaluator accept after 1 revision round |
| S2.5 INTEGRITY | done | PASS WITH NOTES, 2 rounds, 14 edits, v1.3 7,641 words |
| S3 REVIEW | done | five-seat panel, all conformant; decision **Major Revision** (F3 fired, no block/fatal/DA CRITICAL); package R1–R9 + S1–S11, provenance PASS, letter PASS, advisories #1001/#1002/#849 appended; claim check could not run (auditor prompt lives in non-vendored evals/) |
| S4 REVISE | done | `stage4/paper-draft-v2.md` v2.0, 7,862 body words; R1–R9 fully addressed, response letter + revision log; second-coder reliability recheck run (16 rows: family 12/16, evidence status 10/16 κ 0.47, audit 15/16, time 16/16, dynamic 16/16, comparability 10/16), 17 cell disagreements adjudicated, §3.4 figures filled and affected claims restated; deviations below |
| S3' RE-REVIEW | done | legacy single-pass verification review, `[LEGACY-NO-CONTRACT]`; verdict **Minor Revision** — R1–R3, R5–R9 fully addressed, R4 partially (39 of 40 exclusion reasons absent, disclosed); four minor editing defects N1–N4, no new major issue |
| S4' RE-REVISE | done | `stage4-prime/paper-draft-v3.md` v3.0, 7,761 body words: deduplicated §3.1, corrected D.10 tally to 29/12, fixed AI-disclosure sentence, aligned abstract proof/audit sentence; response letter + revision log reconciled; citation checker PASSED |
| S4.5 FINAL INTEGRITY | done | round 1 on v3.0 **FAIL** (2 MINOR) → corrections in v3.1 → round 2 **PASS WITH NOTES**, 0 issues, terminal PASS, sha256 `d05dd050…1009` |
| S5 FINALIZE | pending | MD + PDF (DOCX if pandoc) |
| S6 PROCESS SUMMARY | pending | |

## Stage 3 checkpoint (preauthorized)

- The editor decision (Major Revision) is a MANDATORY checkpoint. Operator preauthorization for the unattended run is recorded as: continue to Stage 4. No independent human approval was obtained for this e2e; the author-side decisions below are made by the run operator under that preauthorization.

## Stage 4 deviation — revision authority chain not exercised

- ARS v3.24.4's patch-authority chain (`revision-roadmap/1.1` + `claim-surface-manifest/1.0` + `author-adjudication/1.0` + patch `1.1` + `ars_apply_revision_patch.py` + `validate-bundle`) requires an anchored base draft and claim-intent artifacts produced by the 1.3 writer flow. This run emulated the v3.6.6 four-call writer/evaluator protocol (Phase 4/6), so no Claim Intent Manifest exists and no claim surfaces can be registered. The Stage 4 revision is therefore performed as a direct writer revision against the immutable package tables, with a response letter; it does NOT claim a 1.3 authorization PASS and is not presented as a Revision-Evidence Bundle round. The vendored patch scripts remain covered by their unit tests.

## Stage 4 reliability recheck (second coder)

- Blind packet: `stage4/reliability/blind-handbook.md` (D.1–D.8 with first-coder tallies removed) + `stage4/second-coder-input.json` (16 records, abstracts only). The second coder was told to read nothing else; its return is `stage4/reliability/second-coder-form.json`.
- Agreement on 16 rows (threshold from handbook D.9: ≥0.85 and, for evidence status, κ ≥ 0.70): family 12/16, evidence status 10/16 (κ = 0.47), audit 15/16, time-axis 16/16, dynamic enforcement 16/16, comparability 10/16; overall 79/96 (82.3%).
- Outcome: time-axis, dynamic enforcement and audit clear the bar; family, evidence status and comparability do not. Per the published rule, the claims resting on the failing fields are restated at the observed stability in §3.3/§3.4/§4/§5.1 and the manuscript no longer presents those tallies as reproducible classifications. The 17 cell disagreements are adjudicated row by row in `stage4/reliability/adjudication.md`; the adjudication kept the ledger codes, so Appendix B and Table 3 are unchanged.
- This is a real finding of the run: the v3.24.4 second-coder protocol is executable end to end with vendored tooling and it caught that two of the manuscript's headline partitions (evidence status, comparability) are not reproducible at the paper's own threshold.

## Stage 3' deviation — archived re-review contract not replayable

- The v3.24.4 default is the #576 three-gate re-review; the legacy single pass requires `ARS_RE_REVIEW_LEGACY=1`. Both paths' checkers (`scripts/check_re_review_synthesis.py`, `scripts/legacy/check_re_review_synthesis_v1_0.py`) require a hash-bound input manifest plus a Schema 7 machine-form roadmap, the author-adjudication sidecar and a Revision-Evidence Bundle. This run has only the human-editable editorial package (markdown roadmap tables), no claim-intent artifacts and no bundle (the same #670 authority-chain gap recorded for Stage 4).
- Therefore Stage 3' runs as a disclosed legacy single pass: one verifier subagent checks each R1–R9 against the original draft, the v2 draft, and the response letter, producing `stage3-prime/re-review.md` prefixed `[LEGACY-NO-CONTRACT]`. The archived checker is not invoked and no contract PASS is claimed.

## Stage 4.5 — round 1 (FAIL) and corrections

- Fresh Mode 2 pass by an independent verifier subagent on `stage4-prime/paper-draft-v3.md`: `stage4.5-integrity.md` (199 lines), artifacts under `stage4.5-artifacts/` (claim registry 202 claims bound to the v3 raw sha256 `090a5992…`, coverage report `candidate_unregistered_count: 0` with `--validate-report` PASS, 112 evidence rows over 59 citation-bearing claims, Phase A–D checks, token-conservation pair v1.3→v3 and v2→v3).
- Verdict FAIL on 2 MINOR defects (any MINOR is an issue at Stage 4.5): F-MINOR-1 the prefactor in §2.1 read `C″(K)=K⁻¹e^{−2k}(c″−c′)` instead of the correct `K⁻¹e^{−k}(c″−c′)` (also in the response letter and revision log); F-MINOR-2 the Table A1 note called the de-duplicated union the "750-record retrieval set" while Table 1 reports 430 unique after de-duplication.
- Corrections applied to `stage4-prime/paper-draft-v3.1.md` (v3.0 bytes preserved for the round-1 record): both fixes, plus response letter and revision-log sync. Body stays 7,761 words; citations lint PASSED. `experiment-intake-declaration.json` persisted at the run root (`status: no_experiments_declared`), closing the Phase C4 condition (1) note.
- Round 2 re-verification is a fresh pass on the v3.1 bytes with a new registry binding (FAIL-loop round 1 of at most 3, per `skills/academic-pipeline/SKILL.md` § Stage 2.5 / 4.5 loop rule).

## Stage 5 — finalization record

- Entry gate: `stage5-entry.md` (MANDATORY checkpoint, recorded continue; APA 7.0 finalization; Markdown + PDF; DOCX instructions because Pandoc is absent). Advisories bound to the certified draft: `#660` `not_checked`/`SNAPSHOT_NOT_PROVIDED`; `#672` `ADVISORY_UNAVAILABLE:SOURCE_MANIFEST_INVALID` (no preregistration in a review; the preregistration handoff is `status: not_provided`).
- Final Markdown = certified draft v3.1 with hidden provenance comments stripped; LaTeX/PDF built by `stage5/build_formats.py` (xelatex, ctex). PDF 54 pages; zero undefined refs/citations, zero missing glyphs, 101 overfull hboxes ≤ 57 pt from long DOI strings. Citations lint PASSED on the final Markdown.
- Completion checkpoint (FULL) recorded in `stage5-completion.md`: deliverables confirmed, Stage 6 proceeds.
- Corrections made during Stage 5 were formatting-only (formatter table widths, Greek kappa mapped to math mode in LaTeX); the certified bytes were never edited.
