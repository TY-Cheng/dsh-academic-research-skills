# Model-portability note

The upstream `CONTRIBUTING.md` asks sibling distributions to document **which
providers/models were tested** and **where downstream-agent behavior diverged
from the Claude baseline** (ARS prompts are calibrated against Claude: Opus for
architecture/review, Sonnet for execution; never Haiku).

## Tested configuration

| Item | Value |
| --- | --- |
| Platform | DeepSeek Harness (DSH), desktop profile |
| DSH CLI | `0.2.2-rc.5` |
| Plugin | `dsh-academic-research-skills` 0.3.0 |
| Runtime model | DeepSeek Harness's configured model, reported as `deepseek-flash` |
| Claude / Anthropic API | **not used** |
| Python | 3.15.2 in the profile-local `.venv`; PyYAML 6.0.3, jsonschema 4.26.0, etc. |
| Run | one `academic-pipeline` e2e on 2026-11-19 (Asia/Singapore) |
| Evidence | [`examples/dsh/iv-surface-review/`](../../examples/dsh/iv-surface-review/README.md) |

The exact DSH session model identifier is the runtime's responsibility; the
agent reported `deepseek-flash` for this run. No Claude run was made, so
divergence from the Claude baseline was not tested.

## How the ARS roles ran

- The five skills' role prompts ran **inline in one DSH session**. The vendored
  tree contains 42 skill-agent Markdown files plus 4 root agent files.
- The Stage 3 “five-seat panel” was five role-separated prompts (Journal-Fit,
  R1, R2, R3, DA) plus editorial synthesis — not five independent model
  instances. Role separation is not a claim of independent error processes.
- The native DSH `subagent`/Team mapping is **not** part of v0.3.0. In this
  e2e, “5 seats” means five prompts, not five isolated agents. The later
  native-layer validation is [separate](../native-validation.md).
- The 16 generated `/ars-*` command wrappers were registered, but the e2e
  exercised the skills rather than every slash wrapper.
- The upstream Claude Code hooks, including the per-role write-scope guard,
  are not ported. The separate
  [DSH sandbox check](claims-evidence.md#g-dsh-sandbox-write-boundary-smoke-test)
  covers workspace confinement for specific backends and policy, not the ARS
  per-role guard or model behavior in this run.

## Observations from the DSH run

These observations describe **one DeepSeek Harness run**, not a controlled
comparison with Claude:

1. **Execution topology.** The Claude Code distribution can run role prompts as
  separate subagents; this run kept them inline. The “seats” and the writer
  and reviewer roles were not independently executed in this run.
2. **Evidence depth.** The run worked at metadata/abstract level: 10/40 sources
   are preprints, one is title-level, four are partial; full texts were not
   available. The paper and integrity reports disclose this rather than
   inferring beyond the abstracts.
3. **Search rate limits.** Semantic Scholar returned HTTP 429 for all attempted
   S2 lookups; Crossref returned one 429. The run used OpenAlex DOI resolution
   (40/40) and Crossref abstracts where available. No S2 verification tier was
   obtained.
4. **Language pair.** The e2e paper used an English body and a **Simplified
   Chinese (zh-CN)** abstract for the operator's convenience. ARS's default
   output pair is English + Traditional Chinese (zh-TW). This is not a claim of
   a supported zh-CN locale pack, and no two-owner locale-pack arrangement is
   claimed.
5. **Format conversion.** Pandoc is absent in the e2e environment. The final
   PDF is a 35-page `ctex` + `xelatex` fallback; the DOCX is a structural
   `python-docx` conversion. They are not journal typesetting and were not
   compared with the Claude Code/Pandoc pipeline.
6. **Command surface.** The plugin registers 16 command wrappers; the e2e used
   the skills. Slash-command runtime behavior is therefore not fully exercised
   by this evidence bundle.
7. **Review quality.** The Stage 2 internal review and Stage 3 panel produced
   Major Revision verdicts; Stage 3′ was Minor Revision. These are the model's
   judgments on this paper, not a calibrated measure of review quality against
   Claude.

## What is deterministic (not model-dependent)

- Vendored content: 1,017 files; per-file SHA-256 in `manifest.json`;
  `npm run verify`; CI `verify-vendor`.
- Registration: 5 skills + 16 commands = 21; 23 with the native team skills.
- Package contents: `npm pack --dry-run` includes the core, `manifest.json`,
  `SYNC_POLICY.md`, `lib/startup.js`, `cordis.patch.yml`; no `__pycache__`/`.pyc`.
- Python syntax: 470 files parse in CI.
- Upstream pin, sync policy, license, and maintainer statement.
- The DSH path note (`DSH_ARS_ROOT` / package root) and the generated command
  wrappers.

## What this note does **not** claim

- That DeepSeek Harness is equivalent to Claude Opus/Sonnet for ARS quality.
- That the e2e is a model benchmark, a reproduction of the Claude baseline, or
  an official endorsement.
- That the 35-page PDF/DOCX match the upstream's Pandoc/LaTeX formatting.
- That zh-CN is a supported ARS locale.
- That five inline prompts are equivalent to five independent subagents.

## What the upstream can reasonably conclude

The DSH port is **platform-viable**: the vendored ARS content registers and
runs; the full pipeline reached a disclosed, corpus-scoped paper; the integrity
and review gates were executed and their limits recorded. The run is **one
non-Claude data point**, not a portability proof. This bundle provides DSH
platform evidence only; it does not establish model parity.

See [`claims-evidence.md`](claims-evidence.md) for the claim-by-claim evidence
table and [`README.md`](README.md) for the submission checklist.
