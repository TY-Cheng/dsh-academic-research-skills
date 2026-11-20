---
name: ars-pipeline-team
description: Run the full ARS academic-pipeline as a DSH Team-board workflow — stage tasks, subagent stage runners, mandatory integrity/review gates, and the Stage 3 ars-team panel. Use when a workspace should advance from research through finalize with auditable stage state, not just a one-off paper draft.
---

# ARS Pipeline Team

This skill maps the 10-stage ARS pipeline onto the live Lead Session Team board. It does not replace the vendored stage skills; it gives them a durable task graph and a single lead orchestrator.

## Preconditions

- The ARS package is installed and `academic-pipeline` plus the stage skills are registered.
- A pipeline workspace exists (for example `examples/dsh/iv-surface-review/`).
- The user has authorized the run through at least Stage 5. That sets the run's scope; it does not waive any checkpoint.
- `team_task_*` tools are available. If they are not, fall back to a written checklist and say so; do not pretend tasks exist.

## Checkpoints

Follow the vendored `academic-pipeline` checkpoint and routing rules. At each MANDATORY checkpoint, the Lead Session presents the result, asks for the decision, and waits for a fresh, explicit user reply at that checkpoint, even if the user asked upfront to run straight through. Record the reply before releasing the next task. Keep the checkpoint-bearing task open while waiting; an artifact, a review verdict, or prior authorization is not clearance. Apply the same stops when using the fallback checklist.

At Stage 2.5 or 4.5, on FAIL, fix and re-verify for at most three rounds. If still FAIL, list the unresolved items and stop for the user's decision under the vendored Integrity Check FAIL Loop (`skills/academic-pipeline/references/pipeline_state_machine.md`, relative to `DSH_ARS_ROOT`). Record the decision and its rationale as required by the upstream protocol. If the decision permits proceeding with unresolved items, disclose that the draft is partially unverified and retain the FAIL verdict; otherwise keep the next stage blocked until resolved. Items the Stage 5 formatter would refuse must be handled or removed, not waived.

## Task graph

Create these tasks before starting. Claim a task only when its route and prerequisites are satisfied; complete it only after its outputs exist and any checkpoint it carries is resolved. Keep tasks on untaken routes out of the active dependencies.

| Task | Stage | Depends on | Output |
|---|---|---|---|
| `p1-research` | 1 research | — | Phase 6 research report |
| `p2-write` | 2 write | `p1-research` | Paper draft through Stage 2 Phase 6 |
| `p2.5-integrity` | 2.5 pre-review integrity | `p2-write` | Integrity report, PASS/FAIL |
| `p3-review` | 3 peer review | `p2.5-integrity` resolved and user confirms | Five seat reports + editorial decision |
| `p4-revise` | 4 revision | `p3-review`; user confirms the revision route | Revised paper + response to reviewers |
| `p3p-re-review` | 3′ verification | `p4-revise` | Verification review |
| `p4p-re-revise` | 4′ re-revision | `p3p-re-review` Major; user confirms the re-revision route | Final revision |
| `p4.5-integrity` | 4.5 final integrity | Confirmed route from `p3-review`, `p3p-re-review`, or `p4p-re-revise` | Fresh integrity report |
| `p5-finalize` | 5 finalize | `p4.5-integrity` resolved; user confirms proceeding and chooses citation style | MD + requested DOCX/PDF/TeX |
| `p6-process` | 6 process record (optional) | `p5-finalize` | Process summary |

## Stage procedure

1. **Stage 1 — research.** Run the `deep-research` full workflow; use the stage's own phase gates. The output is a Phase 6 report in the workspace. Resolve the research checkpoint under the vendored rules before starting Stage 2.
2. **Stage 2 — write.** Run `academic-paper` full through Phase 6; reuse the Stage 1 corpus; do not re-run the literature search. Produce the draft and the Stage 2 audit artifacts.
3. **Stage 2.5 — integrity.** Run `ars_integrity` on the workspace and the `integrity_verification_agent` protocol. On FAIL, use the loop above. Present the PASS or recorded FAIL resolution and wait for the user's confirmation before dispatching Stage 3.
4. **Stage 3 — review.** Use `ars-team` for the field analyst, five seats, and editorial. When the editorial decision and roadmap exist, present the decision and wait for the user to confirm the next action. Follow the vendored route for that decision; do not dispatch revision or final integrity while waiting.
5. **Stage 4 / 3′ / 4′.** On the revision route, apply the roadmap and write a response to reviewers. After re-review, present the Stage 3′ decision and wait for the user to confirm the next action before dispatching 4′ or 4.5. Route under the vendored rules; do not return to review after 4′.
6. **Stage 4.5 — final integrity.** Run a fresh check from the current files. PASS requires zero issues, including final-output pre-check issues; notes and advisories are not issues. Disclose bounded check coverage. On FAIL, use the loop above. After PASS or a recorded resolution permitting continuation, present the result at the single Stage 5 entry checkpoint. Wait for the user to explicitly confirm proceeding **and** choose the citation style; record both before releasing Stage 5.
7. **Stage 5 — finalize.** Dispatch the `academic-paper` formatter only after the entry checkpoint. Use the citation style recorded there; produce Markdown and, on request, DOCX/PDF/TeX. PDF must be LaTeX; never HTML-to-PDF. The separate completion checkpoint is FULL.
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
