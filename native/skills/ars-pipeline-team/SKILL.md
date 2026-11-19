---
name: ars-pipeline-team
description: Run the full ARS academic-pipeline as a DSH Team-board workflow — stage tasks, subagent stage runners, mandatory integrity/review gates, and the Stage 3 ars-team panel. Use when a workspace should advance from research through finalize with auditable stage state, not just a one-off paper draft.
---

# ARS Pipeline Team

This skill maps the 10-stage ARS pipeline onto the live Lead Session Team board. It does not replace the vendored stage skills; it gives them a durable task graph and a single lead orchestrator.

## Preconditions

- The ARS package is installed and `academic-pipeline` plus the stage skills are registered.
- A pipeline workspace exists (for example `examples/dsh/iv-surface-review/`).
- The user has authorized the run through at least Stage 5. If the user has not authorized intermediate checkpoints, stop at every user-facing gate and ask.
- `team_task_*` tools are available. If they are not, fall back to a written checklist and say so; do not pretend tasks exist.

## Task graph

Create these tasks before starting; later tasks are blocked by earlier ones. Claim a task before working on it and complete it only after its outputs exist.

| Task | Stage | Depends on | Output |
|---|---|---|---|
| `p1-research` | 1 research | — | Phase 6 research report |
| `p2-write` | 2 write | `p1-research` | Paper draft through Stage 2 Phase 6 |
| `p2.5-integrity` | 2.5 pre-review integrity | `p2-write` | Integrity report, PASS/FAIL |
| `p3-review` | 3 peer review | `p2.5-integrity` PASS | Five seat reports + editorial decision |
| `p4-revise` | 4 revision | `p3-review` | Revised paper + response to reviewers |
| `p3p-re-review` | 3′ verification | `p4-revise` | Verification review |
| `p4p-re-revise` | 4′ re-revision | `p3p-re-review` Major | Final revision |
| `p4.5-integrity` | 4.5 final integrity | `p3p-re-review` / `p4p-re-revise` | Fresh integrity report |
| `p5-finalize` | 5 finalize | `p4.5-integrity` PASS | MD + requested DOCX/PDF/TeX |
| `p6-process` | 6 process record (optional) | `p5-finalize` | Process summary |

## Stage procedure

1. **Stage 1 — research.** Run the `deep-research` full workflow; use the stage's own phase gates. The output is a Phase 6 report in the workspace. Do not start Stage 2 until the research checkpoint is accepted or the user pre-authorized it.
2. **Stage 2 — write.** Run `academic-paper` full through Phase 6; reuse the Stage 1 corpus; do not re-run the literature search. Produce the draft and the Stage 2 audit artifacts.
3. **Stage 2.5 — integrity.** Run `ars_integrity` on the workspace and the `integrity_verification_agent` protocol. A FAIL blocks Stage 3; fix and re-run, maximum three attempts.
4. **Stage 3 — review.** Use `ars-team` for the field analyst, five seats, and editorial. The `ars-team` skill owns the seven-task sub-board; this pipeline task is complete only when its editorial decision and roadmap exist.
5. **Stage 4 / 3′ / 4′.** Apply the revision roadmap; write a response to reviewers; re-review; if the verdict is Major, run the final re-revision; do not return to review after 4′.
6. **Stage 4.5 — final integrity.** Run a fresh check from the current files, not only the known issues. PASS requires zero blocking findings; disclose bounded checks (no full text, no plagiarism scan, no COI audit) rather than faking a pass.
7. **Stage 5 — finalize.** Run the `academic-paper` formatter. Decide the citation style at entry; produce Markdown and, on request, DOCX/PDF/TeX. PDF must be LaTeX; never HTML-to-PDF. The final checkpoint is FULL.
8. **Stage 6 — optional.** Only if asked; the default run stops after Stage 5.

## Tools

- `ars_pipeline_status` — inspect stage directories and files before/after a stage.
- `ars_integrity` — run the vendored integrity checker with JSON findings.
- `ars_manifest` — read the pinned upstream commit and vendored counts.
- `ars_search` / `ars_lookup` — literature search/lookup during Stage 1 or a scoped revision.
- `ars-team` — the Stage 3 review panel; do not duplicate its five-seat procedure here.

## Boundaries

- This maps **stages**, not all 39 upstream role prompts one-to-one. The seven review roles are native Team roles; the other stage roles run inline through their vendored skills. Do not claim a full 39-agent Team.
- The Team board is the source of truth for stage status; do not mark a task complete without its output files.
- The panel is role-separated prompts, not five independent error processes.
- No method ranking, no PRISMA claim, and no regulatory conclusion is implied by a completed pipeline.
