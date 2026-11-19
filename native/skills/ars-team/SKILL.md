---
name: ars-team
description: Orchestrate the ARS five-seat academic paper review as role-separated DSH subagents (field analyst, methodology/domain/perspective reviewers, devil's advocate, editorial synthesis) on the DSH Team board. Use when a native subagent-backed review is requested.
---

# ARS Team — subagent-backed five-seat review on the DSH Team board

This is the native DSH orchestration layer for the vendored `academic-paper-reviewer` panel. It does not rewrite the ARS role prompts: it passes each vendored role file to a real `subagent`, records the work on the DSH Team board, collects the reports, and lets the editorial synthesizer make the decision.

## When to use

Use this skill when the user asks for the ARS five-seat panel in a DSH-native run, or when the review must have role-separated workers instead of inline role prompts. Do not use it for a quick single-reviewer read; use `academic-paper-reviewer` directly for that.

## Inputs

- `paper`: path to the manuscript Markdown (required).
- `review_type`: `full`, `methodology`, or `quick` (default `full`).
- `output_dir`: defaults to `stage3-team/` next to the paper.
- `venue`: optional target venue or venue type.

If no author-confirmed target or `ReviewTargetContext` exists, every seat must report `criteria_binding_unavailable` and make no venue-alignment claim. Do not invent a target to make the field analysis look complete.

## Role files (vendored — do not paraphrase)

Read these from `$DSH_ARS_ROOT/skills/academic-paper-reviewer/agents/`:

- `field_analyst_agent.md`
- `methodology_reviewer_agent.md`
- `domain_reviewer_agent.md`
- `perspective_reviewer_agent.md`
- `devils_advocate_reviewer_agent.md`
- `editorial_synthesizer_agent.md`

Pass each child the absolute path to its role file; the child reads it. Do not paste a summary of the role in place of the file.

## Team board

Create the board with `team_task_create` before spawning children:

- `task-1` — field analysis (no blockers).
- `task-2` — journal-fit; `task-3` — R1 methodology; `task-4` — R2 domain; `task-5` — R3 perspective; `task-6` — Devil's Advocate. All blocked by `task-1`.
- `task-7` — editorial decision; blocked by `task-2` through `task-6`.

A task must be `in_progress` before it can be completed. The owner must **claim** a task first (`team_task_update` action `claim`), then **complete** it (`action complete`). A direct `complete` on a `pending` task fails with `only an in-progress task can complete`. If a child writes the file but cannot claim/complete, the lead claims and completes the task after verifying the file.

Each task's `write_scopes` is the exact output path. Children must not read another seat's report.

## Procedure

1. Read the paper and `$DSH_ARS_ROOT/skills/academic-paper-reviewer/SKILL.md`. Create `output_dir` and write `review-plan.md` with the paper path, review type, venue, role paths, the five-seat rubric, and the Team board ids.
2. Create the seven Team tasks as above, with `blocked_by` and `write_scopes`.
3. **Field analyst.** Claim `task-1` (or let the field child claim it), spawn one `subagent` with the field-analyst role file, the paper path, and the output path `field-analysis.md`. Wait for it before the panel. Verify the file, then complete `task-1`.
4. **Five seats in parallel.** In one message, spawn five `subagent` calls, one per seat. Each prompt contains: its Team task id, the seat's role-file path, the paper path, the field-analysis path, the review type/venue, and its output path. Use these names and outputs:
   - `ars-journal-fit` → `task-2` → `review-journal-fit.md`
   - `ars-r1-methodology` → `task-3` → `review-r1-methodology.md`
   - `ars-r2-domain` → `task-4` → `review-r2-domain.md`
   - `ars-r3-perspective` → `task-5` → `review-r3-perspective.md`
   - `ars-da` → `task-6` → `review-da.md`
   Each child must claim its task, write the file, then complete it. Each must not read another seat's report. Each must return a recommendation (`Accept`, `Minor Revision`, `Major Revision`, or `Reject`) plus major and minor issues. Target 1,500–3,000 words per seat; longer reports are allowed only when the issues require it.
5. **Editorial synthesis.** Claim `task-7`, then spawn one `subagent` with `editorial_synthesizer_agent.md`, the five report paths, the field analysis, and the output paths `editorial-decision.md` and `revision-roadmap.md`. Tell it not to rewrite a seat verdict and to target 1,500–2,500 words total. If the editorial child has not produced both files after a bounded effort (roughly ten minutes or one retry), the lead synthesizes them from the five reports and the field analysis, marks the fallback in `review-plan.md`, and completes `task-7`. This is a documented fallback, not a silent replacement.
6. **Parent verification.** If a child returned its report as text instead of writing the file, write the returned text to the output path. Verify all eight files exist and the task board is complete. Do not rewrite the verdicts. Report the editorial decision and the paths.

## Guardrails

- Role separation is a process control, not proof of independent error processes. Say so when presenting the result.
- This panel is not a substitute for the pipeline's mandatory integrity pass.
- No fabricated sources. If a seat cannot verify a citation, it must mark it as unverified rather than guess.
- If a child fails or times out, record the failure in `review-plan.md`; do not silently replace the seat or synthesize a missing seat report. The editorial fallback above is explicitly recorded and is allowed only for the editorial synthesis.
- The five reports and the editorial decision are the artifact; the parent's summary is not a new verdict.
- The 0.4.0 implementation uses the Team board plus `subagent` calls. A full `agentPresets`/`agentTeams` preset composition (selectable in a new DSH session) is a later enhancement, not a requirement for this skill to work.
