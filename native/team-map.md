# Native Team Mapping — 0.4.4

Status: the review panel and the 10-stage pipeline Team mapping are implemented; the remaining ARS role prompts stay inline. This document is the stage/panel map for the 0.4.4 native layer; `native/role-map.md` is the full 46-prompt inventory.

## 1. Agent preset

`lib/startup.js` registers a selectable preset when the `agentPresets` service is present:

```json
{
  "id": "ars-team",
  "plugins": [
    { "id": "ars-skills", "name": "dsh-academic-research-skills/startup" }
  ]
}
```

The preset composes the ARS plugin; it does not duplicate the vendored content. `cordis.patch.yml` injects `[skills, tools, agentPresets]`, and the tools/preset are optional at runtime — the offline verifier has no such services, so it registers only the 22 skills.

## 2. Team board

The `ars-team` skill uses the live Lead Session task board:

| Task | Role | Depends on | Output |
|---|---|---|---|
| `task-1` | Field analyst | — | `field-analysis.md` |
| `task-2` | Journal-Fit seat | `task-1` | `review-journal-fit.md` |
| `task-3` | R1 methodology | `task-1` | `review-r1-methodology.md` |
| `task-4` | R2 domain | `task-1` | `review-r2-domain.md` |
| `task-5` | R3 perspective | `task-1` | `review-r3-perspective.md` |
| `task-6` | Devil's Advocate | `task-1` | `review-da.md` |
| `task-7` | Editorial synthesizer | `task-2..task-6` | `editorial-decision.md`, `revision-roadmap.md` |

Rules: claim before complete; no seat reads another seat's output; the field analysis is canonical for the seats; the editorial writes the decision and roadmap; a documented lead fallback applies if the editorial subagent stalls.

## 3. Role prompts

The seats use these vendored reviewer prompts:

- `skills/academic-paper-reviewer/agents/eic_agent.md` — Journal-Fit seat (with the field analysis reviewer configuration card)
- `skills/academic-paper-reviewer/agents/methodology_reviewer_agent.md`
- `skills/academic-paper-reviewer/agents/domain_reviewer_agent.md`
- `skills/academic-paper-reviewer/agents/perspective_reviewer_agent.md`
- `skills/academic-paper-reviewer/agents/devils_advocate_reviewer_agent.md`
- `skills/academic-paper-reviewer/agents/editorial_synthesizer_agent.md`
- `skills/academic-paper-reviewer/agents/field_analyst_agent.md` — pre-panel field analysis

There is no separate `journal_fit_reviewer_agent.md` in the vendored set. The `ars-team` skill supplies the field-analyst and orchestration instructions. The panel is a role-separated prompt workflow, not five independent error processes. Full inventory: [`native/role-map.md`](role-map.md).

## 4. Native tools

| Tool | Purpose | Boundary |
|---|---|---|
| `ars_search` | OpenAlex full-text search; returns DOI/title/year/venue/authors/citations | OpenAlex only; 1 req/s anonymous; no Crossref fallback |
| `ars_lookup` | DOI lookup via OpenAlex or Crossref | Single DOI; title check; no batch |
| `ars_integrity` | Runs vendored `scripts/check_pipeline_integrity.py --json` on a workspace | Uses package `.venv` or `python3`; no shell |
| `ars_pipeline_status` | Lists pipeline stage/paper/review directories and Markdown files | Read-only inventory; no content review |
| `ars_manifest` | Returns the pinned upstream repository/commit, vendored counts, and the not-vendored boundary | Reads `manifest.json`; no upstream fetch |

## 5. Full pipeline Team

See the [`ars-pipeline-team` task graph](skills/ars-pipeline-team/SKILL.md#task-graph)
for stage dependencies and the checkpoints that hold downstream tasks.

The pipeline skill delegates Stage 3 to `ars-team`; it does not duplicate the five-seat procedure. It maps stages, not all 39 upstream role prompts.

## 6. What is mapped, what is not

Mapped natively: the 7-role review panel (field + 5 seats + editorial), the 10-stage pipeline task graph, the Team board, the `ars-team` preset, and the 5 tools.

Not mapped as separate Team roles: the 39 inline prompts (35 skill + 4 root). The 35 skill prompts are `deep-research` 14, `academic-paper` 12, `academic-pipeline` 5, `sr-screener` 4; the 4 root prompts are aliases. The 7 review prompts are the panel; the 39 inline prompts execute inside their stage skills. Mapping all 46 one-to-one would add 39 inline agents and is deliberately deferred — it would multiply cost without a validated benefit. Full inventory: `native/role-map.md`.

## 7. Evidence

- 0.4.0 panel: `examples/dsh/iv-surface-review/stage3-team/` — field 2,336 words; Journal-Fit 4,575; R1 5,737; R2 4,883; R3 3,772; DA 4,385; editorial 1,386 + roadmap 1,044; all five seats Major Revision; six majors + ten minor; no Critical.
- 0.4.2 fake-context smoke: 23 skills + 5 tools + `ars-team` preset; `ars_manifest` returned upstream `6d93886`, 199 skills, 803 core-directory files, 4 core root files, 1,006 vendored total, 16 commands; `ars_pipeline_status` listed stage2/stage3/stage3-prime/stage3-team/stage4/stage4-prime/stage4.5/stage5.
- Live new-session selection is pending; see `docs/native-validation.md`.
