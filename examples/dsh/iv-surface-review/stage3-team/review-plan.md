# Stage 3-team — real 5-subagent panel (0.4.0 validation)

**Date:** 2026-11-19
**Paper:** `../stage5/paper-final.md`
**Plugin:** 0.4.0 installed in the desktop profile. The current session still runs the 0.3.0 catalog, so `ars-team` is not in this session's skill list. This run follows the installed `ars-team` procedure manually with real `subagent` calls.

## Panel

| Stage | Agent | Role prompt | Output |
|---|---|---|---|
| 0 | Field analyst | `skills/academic-paper-reviewer/agents/field_analyst_agent.md` | `field-analysis.md` |
| 1 | Journal-fit reviewer | `.../journal_fit_reviewer_agent.md` | `review-journal-fit.md` |
| 2 | R1 methodology | `.../methodology_reviewer_agent.md` | `review-r1-methodology.md` |
| 3 | R2 domain | `.../domain_reviewer_agent.md` | `review-r2-domain.md` |
| 4 | R3 perspective | `.../perspective_reviewer_agent.md` | `review-r3-perspective.md` |
| 5 | Devil's Advocate | `.../devils_advocate_reviewer_agent.md` | `review-da.md` |
| 6 | Editorial synthesizer | `.../editorial_synthesizer_agent.md` | `editorial-decision.md`, `revision-roadmap.md` |

## Isolation

- The field analyst sees only the paper and its own role prompt.
- Each seat sees the paper, the field analysis, and its own role prompt. No seat reads another seat's report.
- The editorial synthesizer sees the paper, the field analysis, and all five seat reports. It does not see the parent's prior reviews.
- The parent writes returned text to files; it does not rewrite a seat's verdict.

## Team board

- `task-1` — field analysis (no blockers).
- `task-2` … `task-6` — journal-fit, R1, R2, R3, DA (all blocked by `task-1`).
- `task-7` — editorial decision (blocked by `task-2` … `task-6`).

Each seat claims its task, writes its file, and completes the task. The parent does not mark a seat complete until the file exists and the report is non-empty.

## Decision rule

The editorial synthesizer owns the decision. If it returns Major Revision, the stage does not pass to Stage 4 until the roadmap is recorded. If it returns Minor Revision or Accept, record the required fixes and proceed.
