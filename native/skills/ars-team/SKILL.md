---
name: ars-team
description: Orchestrate the ARS five-seat academic paper review as role-separated DSH subagents (field analyst, methodology/domain/perspective reviewers, devil's advocate, editorial synthesis). Use when a native subagent-backed review is requested.
---

# ARS Team — subagent-backed five-seat review

This is the native DSH orchestration layer for the vendored `academic-paper-reviewer` panel. It does not rewrite the ARS role prompts: it passes each vendored role file to a real `subagent`, collects the reports, and lets the editorial synthesizer make the decision.

## When to use

Use this skill when the user asks for the ARS five-seat panel in a DSH-native run, or when the review must have role-separated workers instead of inline role prompts. Do not use it for a quick single-reviewer read; use `academic-paper-reviewer` directly for that.

## Inputs

- `paper`: path to the manuscript Markdown (required).
- `review_type`: `full`, `methodology`, or `quick` (default `full`).
- `output_dir`: defaults to `stage3-team/` next to the paper.
- `venue`: optional target venue or venue type.

## Role files (vendored — do not paraphrase)

Read these from `$DSH_ARS_ROOT/skills/academic-paper-reviewer/agents/`:

- `field_analyst_agent.md`
- `methodology_reviewer_agent.md`
- `domain_reviewer_agent.md`
- `perspective_reviewer_agent.md`
- `devils_advocate_reviewer_agent.md`
- `editorial_synthesizer_agent.md`

Pass each child the absolute path to its role file; the child reads it. Do not paste a summary of the role in place of the file.

## Procedure

1. Read the paper and `$DSH_ARS_ROOT/skills/academic-paper-reviewer/SKILL.md`. Create `output_dir` and write `review-plan.md` with the paper path, review type, venue, role paths, and the five-seat rubric.
2. **Field analyst.** Spawn one `subagent` with the field-analyst role file, the paper path, and the output path `field-analysis.md`. Wait for it before the panel; the panel needs the field context.
3. **Five seats in parallel.** In one message, spawn five `subagent` calls, one per seat. Each prompt contains: the seat's role-file path, the paper path, the field-analysis path, the review type/venue, and its output path. Use these names and outputs:
   - `ars-journal-fit` → `review-journal-fit.md`
   - `ars-r1-methodology` → `review-r1-methodology.md`
   - `ars-r2-domain` → `review-r2-domain.md`
   - `ars-r3-perspective` → `review-r3-perspective.md`
   - `ars-da` → `review-da.md`
   Each child must not read another seat's report. Each must return a recommendation (`Accept`, `Minor Revision`, `Major Revision`, or `Reject`) plus major and minor issues.
4. **Editorial synthesis.** Spawn one `subagent` with `editorial_synthesizer_agent.md`, the five report paths, and the output paths `editorial-decision.md` and `revision-roadmap.md`. It must preserve the five recommendations and must not invent a sixth seat.
5. **Parent verification.** If a child returned its report as text instead of writing the file, write the returned text to the output path. Verify all seven files exist. Do not rewrite the verdicts. Report the editorial decision and the paths.

## Guardrails

- Role separation is a process control, not proof of independent error processes. Say so when presenting the result.
- This panel is not a substitute for the pipeline's mandatory integrity pass.
- No fabricated sources. If a seat cannot verify a citation, it must mark it as unverified rather than guess.
- If a child fails or times out, record the failure in `review-plan.md`; do not silently replace the seat or synthesize a missing report.
- The five reports and the editorial decision are the artifact; the parent's summary is not a new verdict.
