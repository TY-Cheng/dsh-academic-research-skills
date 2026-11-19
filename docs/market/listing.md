# DSH Plugin Market — listing draft (not published)

Draft for community Plugin Market submission. The 0.3.0 package is the proposed baseline for separate upstream sibling recognition; 0.4.4 is the current native release. The 0.4.3 live desktop session passed (2 skills, preset, 5 tools); a fresh 0.4.4 session confirmed the fix for the relative-path bug found there.

## Identity

- **Name:** `dsh-academic-research-skills`
- **Version:** 0.4.4
- **Tagline:** Full ARS academic-research pipeline for DeepSeek Harness — 5 skills, 16 `/ars-*` commands, a native review Team, and 5 native tools.
- **Repository:** https://github.com/TY-Cheng/dsh-academic-research-skills
- **Market install source:** Git, repository root, commit `2e4da620d697dec68ab74ef86dc94a0bb559924a`
- **Release:** https://github.com/TY-Cheng/dsh-academic-research-skills/releases/tag/v0.4.4
- **Issues:** https://github.com/TY-Cheng/dsh-academic-research-skills/issues
- **Maintainer:** TY-Cheng
- **License:** CC-BY-NC-4.0 (upstream ARS content; no commercial relicensing)

## What it provides

- 5 vendored ARS skills: `deep-research`, `academic-paper`, `academic-paper-reviewer`, `academic-pipeline`, `sr-screener`.
- 16 `/ars-*` commands generated from the upstream command sources.
- Full upstream core: `scripts/`, `shared/`, `agents/`, `MODE_REGISTRY.md`, `THIRD_PARTY.md`, `requirements*.txt` — 1,006 files pinned to ARS `v3.24.2` (`6d93886`).
- Native 0.4.4 layer: `ars-team` and `ars-pipeline-team` skills, selectable `ars-team` agent preset, and `ars_search`, `ars_lookup`, `ars_integrity`, `ars_pipeline_status`, `ars_manifest`.
- 0.4.4 fix: workspace-scoped tools resolve relative paths against the calling Session's current directory via the Host `workingDirectory` service.
- E2E evidence: a complete academic-pipeline run in `examples/dsh/iv-surface-review/` (6,804-word paper, 40 refs, 8 tables, appendices, PDF/DOCX/TeX).

## Install

```bash
dsh plugin --profile <profile> add github:TY-Cheng/dsh-academic-research-skills#v0.4.4
```

Proposed upstream sibling-recognition baseline (no native layer):

```bash
dsh plugin --profile <profile> add github:TY-Cheng/dsh-academic-research-skills#v0.3.0
```

Python tools are optional; for `ars_integrity` and the vendored checker scripts, create a virtualenv and install:

```bash
cd <plugin-root>
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Requirements / compatibility

- Tested on macOS with DSH `0.2.2-rc.5`: isolated `web` profile for installation and a separate desktop session for the two-tool relative-path smoke. Other DSH versions and platforms were not verified in these runs.
- The native tools/preset require the Host `tools` and `agentPresets` services; the skills work without them.
- Model-portability note: the e2e used a DeepSeek `deepseek-flash` session, not Claude. See `docs/sibling-submission/model-portability.md`.

## Market copy

Short description:

> A DSH port of the Academic Research Skills pipeline: research, write, review, revise, and finalize with 5 skills, 16 commands, a five-seat native review Team, and integrity/search tools.

Keywords: academic research, literature review, paper writing, peer review, citations, arXiv, OpenAlex, DeepSeek Harness, DSH.

## Installation and desktop validation

The pinned v0.4.4 commit installed successfully into a fresh `web` profile with an empty pnpm store. The lockfile resolved the exact SHA, `--dump-config` included the plugin patch, and the offline registrar verified 23 registrations. This did not exercise the native tools or agent preset in the isolated profile. See the [clean installation result](../native-validation.md#clean-install-from-the-pinned-commit-044).

The 0.4.4 relative-path smoke passed: `ars_pipeline_status` and `ars_integrity` both resolved the input against the calling session's working directory. `ars_pipeline_status` returned eight stage directories. `ars_integrity` reported zero findings with empty `phase_dirs`, so this run does not establish integrity coverage. See the [live desktop result](../native-validation.md#live-desktop-result-044).

## Not yet done

- Official sibling recognition: upstream issue #1126 is open with no reply; 0.3.0 remains the baseline.
- Marketplace submission and promotion: this listing is ready; submission/promo is a user decision.
