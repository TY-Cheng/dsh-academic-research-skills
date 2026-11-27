# DSH sibling-distribution submission package

**Status:** design issue open — [#1126](https://github.com/Imbad0202/academic-research-skills/issues/1126);
official sibling recognition has **not** been requested or granted.

This package collects the material the upstream ARS maintainer asks for in
`CONTRIBUTING.md` § *Platform ports* → *Sibling distribution*. It is the
submission scaffold, not a claim of endorsement.

| Item | Value |
| --- | --- |
| Sibling repository | https://github.com/TY-Cheng/dsh-academic-research-skills |
| Plugin version | `dsh-academic-research-skills` 0.3.0 (official baseline); 0.4.4 native layer is additive, not part of the baseline |
| Upstream | https://github.com/Imbad0202/academic-research-skills |
| Upstream pin | `74453f859a4625954e5d2a7dd30c5d716842d060` (`v3.24.5`), tag `v3.24.5` |
| License | CC-BY-NC-4.0, attribution retained |
| Named maintainer | TY-Cheng ([@TY-Cheng](https://github.com/TY-Cheng)) |
| E2E evidence | [`examples/dsh/iv-surface-review/`](../../examples/dsh/iv-surface-review/README.md) |
| Design issue | [#1126](https://github.com/Imbad0202/academic-research-skills/issues/1126) |

## Submission checklist

| Upstream requirement | Evidence in this repo | Status |
| --- | --- | --- |
| Sibling shape: separate repo, upstream pinned in `manifest.json` | [`manifest.json`](../../manifest.json) (`upstream.commit`, `tag`, `version`, per-file SHA-256) | done |
| Written update / sync policy | [`SYNC_POLICY.md`](../../SYNC_POLICY.md) (6-week cadence, drift check, release rules) | done |
| Vendored content unmodified; only outer adapter platform-specific | 1,018 vendored files: 200 skills, 655 `scripts/`, 155 `shared/`, 4 `agents/`, 4 root files; `npm run verify`; CI `verify-vendor` | done |
| Named maintainer in repo README | [`README.md`](../../README.md) attribution block; [`maintainer.md`](maintainer.md); [`NOTICE.md`](../../NOTICE.md) | done |
| Full `academic-pipeline` run under `examples/` | [`examples/dsh/iv-surface-review/README.md`](../../examples/dsh/iv-surface-review/README.md); final paper and all stage reports | done |
| Claims–evidence alignment | [`claims-evidence.md`](claims-evidence.md) | done |
| Model-portability note | [`model-portability.md`](model-portability.md) | done |
| Design issue opened before requesting recognition | [#1126](https://github.com/Imbad0202/academic-research-skills/issues/1126); body retained in [`design-issue.md`](design-issue.md) | done |

## E2E at a glance

- **Topic:** arbitrage-free implied volatility surface construction — a
  40-source structured literature review.
- **Pipeline:** Stage 1 deep research → Stage 2 academic paper → 2.5 integrity →
  Stage 3 five-seat review → Stage 4 revision → Stage 3′ re-review → Stage 4′
  copy-edit → Stage 4.5 final integrity → Stage 5 finalize. Stage 6 was not run,
  per the operator's instruction to stop at Stage 5.
- **Verdicts:** Stage 2 internal Major Revision → v1.2; Stage 2.5 PASS
  (bounded); Stage 3 Major Revision (six major issues); Stage 3′ Minor Revision
  (two copy-edits); Stage 4.5 PASS (bounded); Stage 5 final formats.
- **Final paper:** 6,804-word body, 40 references, 8 numbered tables, five
  appendices, English body + Chinese abstract, APA 7.0.
- **Formats:** Markdown, DOCX, LaTeX, PDF. Pandoc is not installed in the e2e
  environment; `stage5/build_formats.py` is a deterministic fallback
  (`ctex` + `xelatex` for the 35-page PDF; `python-docx` for DOCX). They are
  working conversions, not journal typesetting.

## Native layer (0.4.4, additive)

The 0.4.4 release adds, outside the vendored ARS core:

- `native/skills/ars-team` — the five-seat panel run as real `subagent`s on the
  DSH Team board (field analyst → five seats → editorial).
- `native/skills/ars-pipeline-team` — the 10-stage pipeline mapped onto a
  Team-board stage task graph.
- `ars_search` / `ars_lookup` / `ars_integrity` / `ars_pipeline_status` /
  `ars_manifest` — native tools (OpenAlex search; DOI lookup via
  OpenAlex/Crossref; pipeline integrity checker; stage-artifact inventory;
  pinned upstream/content counts), registered only when `tools` is available.
- `ars-team` preset — registered when `agentPresets` is mounted; a new session
  can select it to compose the team skill with the Team board.

Validation: the final Stage 5 paper was reviewed by five seat subagents plus the
field analyst and editorial synthesizer; outputs are in
`examples/dsh/iv-surface-review/stage3-team/`; verdict **Major Revision**, six
required majors and ten minor fixes. The official e2e remains the 0.3.0 inline
run; the native panel is additive evidence, not a replacement. Role separation
is a process control, not proof of independent error processes.

## What this package does **not** claim

- Official sibling-distribution status; the design issue is open, and recognition
  is the next step.
- A supported Simplified-Chinese (`zh-CN`) locale pack. The e2e paper used an
  English body and a Chinese abstract for the operator's convenience; ARS's
  default pair is English + Traditional Chinese (`zh-TW`). No locale-pack
  ownership or two-owner arrangement is claimed.
- Independent execution of the five review seats **in the official e2e**. That
  run used inline role prompts; role separation is not a claim of independent
  error processes. The additive 0.4.4 native layer was separately exercised with
  five `subagent`s + a Team board; it does not retrofit the official 0.3.0 e2e.
- Full-text, plagiarism, or complete COI verification. The review is
  abstract-level: 10/40 sources are preprints, 1 is title-level, 4 are partial;
  no full text was available; S2 returned HTTP 429 at search time.
- PRISMA or PRISMA-ScR compliance. The flow is PRISMA-style; 311 non-advanced
  records were not individually coded.
- Model parity with the Claude baseline. This was one DeepSeek Harness run, not
  a head-to-head benchmark; see [`model-portability.md`](model-portability.md).

## Binary-format decision

The e2e bundle includes the 35-page PDF and DOCX because they are the artifacts
the run actually produced. The design issue asks whether the upstream maintainer
prefers only Markdown + review reports for the recognition request; if so, the
binaries can be omitted from the link rather than regenerated.

## Files here

| File | Purpose |
| --- | --- |
| [`claims-evidence.md`](claims-evidence.md) | Claim → evidence → coverage table for the README and e2e claims |
| [`model-portability.md`](model-portability.md) | Tested platform/model, divergences, and non-claims |
| [`maintainer.md`](maintainer.md) | Named-maintainer statement and sync/triage commitments |
| [`design-issue.md`](design-issue.md) | Body of the upstream design issue, posted as [#1126](https://github.com/Imbad0202/academic-research-skills/issues/1126) |
