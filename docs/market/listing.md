# DSH Plugin Market — listing draft (not published)

Draft for a future DSH plugin-market submission. The 0.3.0 package remains the official sibling-recognition baseline; 0.4.4 is the native release. Do not publish until the live 0.4.4 validation in a new desktop session passes.

## Identity

- **Name:** `dsh-academic-research-skills`
- **Version:** 0.4.4
- **Tagline:** Full ARS academic-research pipeline for DeepSeek Harness — 5 skills, 16 `/ars-*` commands, a native review Team, and 5 native tools.
- **Repository:** https://github.com/TY-Cheng/dsh-academic-research-skills
- **Issues:** https://github.com/TY-Cheng/dsh-academic-research-skills/issues
- **Maintainer:** TY-Cheng
- **License:** CC-BY-NC-4.0 (upstream ARS content; no commercial relicensing)

## What it provides

- 5 vendored ARS skills: `deep-research`, `academic-paper`, `academic-paper-reviewer`, `academic-pipeline`, `sr-screener`.
- 16 `/ars-*` commands generated from the upstream command sources.
- Full upstream core: `scripts/`, `shared/`, `agents/`, `MODE_REGISTRY.md`, `THIRD_PARTY.md`, `requirements*.txt` — 1,006 files pinned to ARS `v3.24.2` (`6d93886`).
- Native 0.4.4 layer: `ars-team` and `ars-pipeline-team` skills, selectable `ars-team` agent preset, and `ars_search`, `ars_lookup`, `ars_integrity`, `ars_pipeline_status`, `ars_manifest`.
- E2E evidence: a complete academic-pipeline run in `examples/dsh/iv-surface-review/` (6,804-word paper, 40 refs, 8 tables, appendices, PDF/DOCX/TeX).

## Install

```bash
dsh plugin --profile <profile> add github:TY-Cheng/dsh-academic-research-skills#v0.4.4
```

Official-recognition baseline (no native layer):

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

- DSH 0.2.x; tested on the desktop profile with CLI 0.2.2-rc.5.
- The native tools/preset require the Host `tools` and `agentPresets` services; the skills work without them.
- Model-portability note: the e2e used a DeepSeek `deepseek-flash` session, not Claude. See `docs/sibling-submission/model-portability.md`.

## Market copy

Short description:

> A DSH port of the Academic Research Skills pipeline: research, write, review, revise, and finalize with 5 skills, 16 commands, a five-seat native review Team, and integrity/search tools.

Keywords: academic research, literature review, paper writing, peer review, citations, arXiv, OpenAlex, DeepSeek Harness, DSH.

## Not yet done

- Live 0.4.4 validation in a new desktop session (`docs/native-validation.md`).
- Official sibling recognition: upstream issue #1126 is open with no reply; 0.3.0 remains the baseline.
- Marketplace listing submission and promotion are intentionally deferred.
