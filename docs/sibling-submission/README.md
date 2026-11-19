# DSH sibling-distribution submission package

**Status:** design issue open — [#1126](https://github.com/Imbad0202/academic-research-skills/issues/1126);
official sibling recognition has **not** been requested or granted.

This package collects the material the upstream ARS maintainer asks for in
`CONTRIBUTING.md` § *Platform ports* → *Sibling distribution*. It is the
submission scaffold, not a claim of endorsement.

| Item | Value |
| --- | --- |
| Sibling repository | https://github.com/TY-Cheng/dsh-academic-research-skills |
| Plugin version | `dsh-academic-research-skills` 0.3.0 |
| Upstream | https://github.com/Imbad0202/academic-research-skills |
| Upstream pin | `6d9388674de1ad0437ad95db3d52f92b92204d84` (`v3.24.2-3-g6d93886`), tag `v3.24.2` |
| License | CC-BY-NC-4.0, attribution retained |
| Named maintainer | TY-Cheng ([@TY-Cheng](https://github.com/TY-Cheng)) |
| E2E evidence | [`examples/dsh/iv-surface-review/`](../../examples/dsh/iv-surface-review/README.md) |
| Design issue | [#1126](https://github.com/Imbad0202/academic-research-skills/issues/1126) |

## Submission checklist

| Upstream requirement | Evidence in this repo | Status |
| --- | --- | --- |
| Sibling shape: separate repo, upstream pinned in `manifest.json` | [`manifest.json`](../../manifest.json) (`upstream.commit`, `tag`, `version`, per-file SHA-256) | done |
| Written update / sync policy | [`SYNC_POLICY.md`](../../SYNC_POLICY.md) (6-week cadence, drift check, release rules) | done |
| Vendored content unmodified; only outer adapter platform-specific | 1,006 vendored files: 199 skills, 644 `scripts/`, 155 `shared/`, 4 `agents/`, 4 root files; `npm run verify`; CI `verify-vendor` | done |
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

## What this package does **not** claim

- Official sibling-distribution status; the design issue is open, and recognition
  is the next step.
- A supported Simplified-Chinese (`zh-CN`) locale pack. The e2e paper used an
  English body and a Chinese abstract for the operator's convenience; ARS's
  default pair is English + Traditional Chinese (`zh-TW`). No locale-pack
  ownership or two-owner arrangement is claimed.
- Independent execution of the five review seats. The e2e ran the role prompts
  inline in one DSH session; role separation is not a claim of independent
  error processes. DSH subagent/Team mapping is planned as native enhancement.
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
