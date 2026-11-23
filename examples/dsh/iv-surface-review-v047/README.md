# Examples / DSH — `academic-pipeline` E2E on ARS v3.24.4 (run `iv-surface-review-v047`)

This directory is a second, complete 10-stage `academic-pipeline` run on the DSH port
(`dsh-academic-research-skills` 0.4.7, vendored ARS v3.24.4, fork commit `19f11de`).
It exists as acceptance evidence for the v3.24.4 vendoring sync: the same topic and
research question as `../iv-surface-review/`, run again from a fresh discovery pass
on the newly vendored content, with the new v3.24.4 gates actually exercised.

## Provenance

- **ARS**: v3.24.4, tag commit `23807f987024f2e038d12fd9e4e5d2a7cc228674`; plugin
  0.4.7, sync commit `19f11de`.
- **Run**: 2026-11-23 by the DSH academic-pipeline orchestrator, driven entirely
  through subagents; no hand editing of the vendored skills or scripts. Python
  checks used the fork's `.venv`; PDF used xelatex (Pandoc is absent).
- **Operator preauthorization**: all MANDATORY checkpoints through Stage 5 were
  preauthorized as "continue"; the two substantive human turns are the sync
  request and the e2e request. Every such checkpoint is recorded in `run-log.md`.

## What this run exercised that the previous one could not

1. **Stage 2.5 and 4.5 are real gates**: both refused the first pass
   (`FAIL`), and both passed only after fixes and a fresh second round.
2. **The revision path from review to final**: 5-seat review → 9 required
   revisions → revision → minor-revision re-review → corrections → certified
   final draft. Also one recorded deviation: the contract-governed re-review
   needs sidecar artifacts that this run does not produce, so the re-review ran
   in the documented legacy single-pass mode (`[LEGACY-NO-CONTRACT]`) instead of
   pretending a contract pass.
3. **The reliability recheck**: a blind second coder re-coded 16 rows; the
   measured agreement (κ = 0.47 on evidence status) was below threshold, and
   the manuscript was rewritten to report the observed strength rather than the
   strong version of its classification claims.
4. **New v3.24.4 checks**: `check_phase_conformance.py`, `check_panel_synthesis.py`,
   `review_panel_provenance.py`, `check_author_letter.py`, `revision_roadmap/1.1`.
5. **Advisory boundaries**: #660 could not run without a phrase snapshot; #672's
   hermetic comparator has no preregistration to compare against. Both are
   recorded as advisories, not silently skipped.

## Deliverables

- `stage5/paper-final.md`, `paper-final.tex`, `paper-final.pdf` (54 pages).
- `stage6/paper_creation_process.md` — process record with collaboration
  evaluation and AI self-reflection, including the collaboration-depth advisory.
- `stage4.5-integrity.md` + `stage4.5-integrity-round2.md` — the final integrity
  evidence (round 1 FAIL, round 2 PASS WITH NOTES).

## Limits, stated plainly

- **Not a real submission.** Single coder + one blind recheck on a designed sample;
  abstract-level coding; no independent retraction sweep; no venue, no FORMATIVE
  receipt, `criteria_binding_unavailable`; no PRISMA conformity claimed.
- **DOCX not produced**: no Pandoc in this environment; instructions are in
  `stage5/README.md`.
- **Front matter reads "v2.0"**: the Phase 4 label is kept to preserve the certified
  bytes; the real version trail is `v1.3 → v2.0 → v3.0 → v3.1`.
- **This is not an upstream endorsement.** The run is platform evidence for the DSH
  port; it says nothing about the quality of ARS as a product.

## Related

- Earlier run on ARS v3.24.2 / plugin 0.3.0: `../iv-surface-review/` (same topic,
  35-page PDF; its README states that run's limits).
- Vendoring policy: `../../SYNC_POLICY.md`.
