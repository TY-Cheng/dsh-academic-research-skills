# ARS Role Map — 0.4.3

This is the full inventory of the ARS role prompts shipped in the vendored core and the native layer. It corrects the 0.4.2 “39/32” shorthand.

**Counts:** 42 skill-agent prompts (deep-research 14, academic-paper 12, academic-paper-reviewer 7, academic-pipeline 5, sr-screener 4) + 4 root prompts = 46 files. **7** run as the review panel through `ars-team`; **39** execute inline inside their stage skill (35 skill + 4 root). The 0.4.2 “32 non-review” line was a miscount; this file is canonical.

## Review panel (7 real subagents)

| Prompt | Seat | Pipeline stage |
|---|---|---|
| `eic_agent.md` | Journal-Fit seat (with field analysis reviewer card) | Stage 3 |
| `methodology_reviewer_agent.md` | R1 methodology | Stage 3 |
| `domain_reviewer_agent.md` | R2 domain | Stage 3 |
| `perspective_reviewer_agent.md` | R3 perspective | Stage 3 |
| `devils_advocate_reviewer_agent.md` | Devil’s Advocate | Stage 3 |
| `editorial_synthesizer_agent.md` | Editorial decision + roadmap | Stage 3 |
| `field_analyst_agent.md` | Field Analyst / pre-panel | Stage 3 |

Note: the vendored `academic-paper-reviewer/agents/` directory has no separate `journal_fit_reviewer_agent.md`; the Journal-Fit seat uses `eic_agent.md` plus the field analysis’s reviewer configuration card. The 0.4.0 panel used a synthesized prompt for that seat.

## Inline role prompts (39 = 35 skill + 4 root)

| Skill | Prompt | Stage |
|---|---|---|
| deep-research | `bibliography_agent.md` | Stage 1: research |
| deep-research | `devils_advocate_agent.md` | Stage 1: research |
| deep-research | `editor_in_chief_agent.md` | Stage 1: research |
| deep-research | `ethics_review_agent.md` | Stage 1: research |
| deep-research | `meta_analysis_agent.md` | Stage 1: research |
| deep-research | `monitoring_agent.md` | Stage 1: research |
| deep-research | `report_compiler_agent.md` | Stage 1: research |
| deep-research | `research_architect_agent.md` | Stage 1: research |
| deep-research | `research_question_agent.md` | Stage 1: research |
| deep-research | `risk_of_bias_agent.md` | Stage 1: research |
| deep-research | `socratic_mentor_agent.md` | Stage 1: research |
| deep-research | `source_verification_agent.md` | Stage 1: research |
| deep-research | `synthesis_agent.md` | Stage 1: research |
| deep-research | `timeline_extraction_agent.md` | Stage 1: research |
| academic-paper | `abstract_bilingual_agent.md` | Stage 2: write |
| academic-paper | `argument_builder_agent.md` | Stage 2: write |
| academic-paper | `citation_compliance_agent.md` | Stage 2: write |
| academic-paper | `draft_writer_agent.md` | Stage 2: write |
| academic-paper | `formatter_agent.md` | Stage 2: write |
| academic-paper | `intake_agent.md` | Stage 2: write |
| academic-paper | `literature_strategist_agent.md` | Stage 2: write |
| academic-paper | `peer_reviewer_agent.md` | Stage 2: write |
| academic-paper | `revision_coach_agent.md` | Stage 2: write |
| academic-paper | `socratic_mentor_agent.md` | Stage 2: write |
| academic-paper | `structure_architect_agent.md` | Stage 2: write |
| academic-paper | `visualization_agent.md` | Stage 2: write |
| academic-pipeline | `claim_ref_alignment_audit_agent.md` | Stages 2-5: orchestration/integrity |
| academic-pipeline | `collaboration_depth_agent.md` | Stages 2-5: orchestration/integrity |
| academic-pipeline | `integrity_verification_agent.md` | Stages 2-5: orchestration/integrity |
| academic-pipeline | `pipeline_orchestrator_agent.md` | Stages 2-5: orchestration/integrity |
| academic-pipeline | `state_tracker_agent.md` | Stages 2-5: orchestration/integrity |
| sr-screener | `protocol_architect_agent.md` | Outside the 10-stage pipeline (screening) |
| sr-screener | `qc_auditor_agent.md` | Outside the 10-stage pipeline (screening) |
| sr-screener | `reporter_agent.md` | Outside the 10-stage pipeline (screening) |
| sr-screener | `screening_reviewer_agent.md` | Outside the 10-stage pipeline (screening) |
| root | `agents/report_compiler_agent.md` | cross-stage alias |
| root | `agents/research_architect_agent.md` | cross-stage alias |
| root | `agents/screening_reviewer_agent.md` | cross-stage alias |
| root | `agents/synthesis_agent.md` | cross-stage alias |

## Boundary

- The 7 review prompts are the only roles the native `ars-team` panel runs as real `subagent`s.
- The 39 inline prompts are executed by the stage skill that owns them; they are not separate Team tasks, and mapping each one to a task would be a different orchestration design.
- The 4 root prompts are root-level aliases of skill prompts (report compiler, research architect, screening reviewer, synthesis); they stay inline.
- The 10-stage `ars-pipeline-team` Team graph is the stage mapping; this file is the role-level map beneath it.
