# Claims → evidence

This table covers the **load-bearing, verifiable claims** in the repository
README and in the e2e evidence bundle. It is deliberately narrower than every
sentence in those documents: qualitative statements about usefulness or fit are
not treated as measured claims.

**Snapshot:** plugin 0.3.0 official baseline; 0.4.2 native layer (additive); upstream pin
`6d9388674de1ad0437ad95db3d52f92b92204d84`; e2e commit `40b7e77`; CI run
`44530710616`; 2026-11-19.

## A. Upstream sibling-distribution requirements

| Requirement | Claim | Evidence | Coverage / caveat |
| --- | --- | --- | --- |
| Separate repo with a pinned upstream commit | The sibling pins ARS `v3.24.2` at `6d93886` | [`manifest.json`](../../manifest.json) `upstream.commit`, `tag`, `version`; [`SYNC_POLICY.md`](../../SYNC_POLICY.md) § Upstream pin | The pin is a commit hash, not a moving branch. |
| Written sync / update policy | The port follows a documented six-week sync cadence | [`SYNC_POLICY.md`](../../SYNC_POLICY.md) § Sync cadence, § Drift check, § Versioning | The policy is a commitment; it has not yet survived multiple upstream minors. |
| Vendored content unmodified | 1,006 upstream files are vendored byte-for-byte | `npm run verify` → 199 skills, 644 `scripts/`, 155 `shared/`, 4 `agents/`, 4 root files; per-file SHA-256 in `manifest.json`; CI `verify-vendor` | CI checks the committed manifest, not a live upstream checkout. A development `diff -qr` against the pinned upstream was empty. |
| Only the outer adapter is platform-specific | DSH-specific code is confined to the porting layer | `lib/startup.js`, `cordis.patch.yml`, `tooling/*.mjs`, generated `commands/`, docs/CI; no local edits under `skills/`, `scripts/`, `shared/`, `agents/` | `commands/` is generated from upstream command sources, not vendored; this is the adapter layer. |
| Named maintainer | TY-Cheng maintains the port and triages DSH issues | [`README.md`](../../README.md) attribution block; [`maintainer.md`](maintainer.md); [`NOTICE.md`](../../NOTICE.md); `manifest.json.maintainer` | One maintainer; no backup owner is claimed. |
| Full `academic-pipeline` e2e under `examples/` | The port ran the full pipeline on a real topic | [`examples/dsh/iv-surface-review/README.md`](../../examples/dsh/iv-surface-review/README.md); final paper and stage reports | One run; see the limits in § E. |
| Claims–evidence alignment | This table | This file | Covers the load-bearing claims, not every sentence. |
| Model-portability note | The e2e ran on DeepSeek Harness, not Claude | [`model-portability.md`](model-portability.md) | One model, one run; no Claude baseline. |
| Design issue before recognition | The design issue is the first upstream contact | [#1126](https://github.com/Imbad0202/academic-research-skills/issues/1126) | Open as #1126; recognition not yet requested. |

## B. Repository README claims

| Claim | Evidence | Coverage / caveat |
| --- | --- | --- |
| 5 model-invocable skills | `find skills -maxdepth 1 -mindepth 1 -type d` → 5; `npm run verify` registers 5 skills | Registration is proven; model routing quality is not benchmarked. |
| 16 user-invocable commands | `find commands -mindepth 2 -name SKILL.md` → 16; `npm run verify` → 16 commands; `lib/startup.js` registers them | The e2e exercised the **skills**, not every slash wrapper. Command registration is proven; per-command runtime behavior is not exhaustively exercised. |
| Full ARS core is carried | 1,006 vendored files: 199 + 644 + 155 + 4 + 4 | `commands/` is generated, and `docs/`, `evals/`, `examples/`, `hooks/`, `pi/`, `audits/` are not vendored. “Core” here means the five skills plus root `scripts/`, `shared/`, `agents/`, and four root files. |
| Vendored files are byte-identical | `manifest.json` per-file SHA-256; `npm run verify`; CI | CI is offline against the manifest; the live `diff -qr` was run in the development checkout at sync time. |
| 21 skills registered in 0.3.0; 23 in 0.4.2 | `npm run verify` → “registered 21 skills” (0.3.0); 0.4.2 registers 23 (21 + `ars-team` + `ars-pipeline-team`) | 0.3.0: 5 skills + 16 commands. 0.4.2 adds `ars-team` and `ars-pipeline-team`; the vendored count is unchanged. |
| The Python tool layer ships | 644 `scripts/` files; `requirements-*.txt`; `470` Python files parsed by the CI AST check | Installed and smoke-tested. The e2e workflow used the skills, custom search scripts, and the format builder; it did **not** run every core checker end-to-end. |
| `DSH_ARS_ROOT` path note prevents mis-resolution | `lib/startup.js`; e2e README § “What the e2e actually exercised”; Python calls used the profile-local `.venv` | Proves the note is injected; does not prove every possible relative path in every skill. `sr-screener`’s own `scripts/` is intentionally skill-local. |
| Hooks are not ported | README § Differences; upstream `hooks/` are Claude Code-specific; DSH has no hook system | A platform difference, not a feature claim. |
| 42 skill-agent prompt files + 4 root agent files run inline | `find skills -path '*/agents/*.md' -type f \| wc -l` → 42; `find agents -type f \| wc -l` → 4; e2e README | The e2e ran the role prompts inline in one session; it did **not** run them as independent DSH subagents. The README previously said “43”; corrected to 42 + 4. |
| 16 commands are generated, not hand-written | `commands/ars-*/SKILL.md`; `tooling/regenerate-commands.mjs`; CI checks 16 command files | Generator output is verified by hash; the slash commands were not all exercised in the e2e. |
| Install from `#v0.3.0` works on DSH | Tag `v0.3.0` at `96e4e4d`; e2e installed it on DSH desktop; `dsh --version` = `0.2.2-rc.5` | Tested on the desktop profile; the README examples use `web` as a placeholder and now say to substitute the actual profile. |
| Python 3.9+ and vendored dependencies | `requirements-dev.txt`; e2e `.venv` (Python 3.15.2) installed PyYAML 6.0.3, jsonschema 4.26.0, etc. | Tested on the e2e host; not a matrix across Python versions/OSes. |
| CC-BY-NC-4.0; attribution retained | [`LICENSE`](../../LICENSE); [`NOTICE.md`](../../NOTICE.md); upstream author/version | No relicensing or commercial-use claim. |
| Maintained by TY-Cheng | [`README.md`](../../README.md) attribution; [`maintainer.md`](maintainer.md); `manifest.json` | One maintainer. |

## C. E2E bundle claims

| Claim | Evidence | Coverage / caveat |
| --- | --- | --- |
| The full pipeline ran, Stage 1 → Stage 5 | E2E README § Pipeline verdicts; stage directories and reports | One run; the operator explicitly stopped after Stage 5; Stage 6 not run. |
| Stage 2 internal review → Major Revision → v1.2 | `stage2/phase6-review.md`; `stage2/paper-draft.md` v1.2 (6,315 words) | Internal review was an inline role; not an external editor. |
| Stage 2.5 integrity → PASS (bounded) | `stage2.5-integrity.md`; 5 advisories | Abstract-level checks; no full text/plagiarism/COI. |
| Stage 3 five-seat review → Major Revision | `stage3/` (field analysis, five seat reports, editorial decision, roadmap) | Role-separated prompts run inline; not independent subagents; not a claim of independent error processes. |
| Stage 4 revision → v2; Stage 3′ Minor; Stage 4′ v3; Stage 4.5 PASS; Stage 5 final | `stage4/`, `stage3-prime/`, `stage4-prime/`, `stage4.5-integrity.md`, `stage5/` | One review/revision cycle; no Stage 6. |
| 40-source corpus | `search/selected_sources.json`; `phase2-bibliography.md`; e2e README | 30 peer-reviewed / 10 preprints; 35 full abstracts, 4 partial, 1 title-level; 39 DOI + 1 HAL. |
| 24 OpenAlex queries → 351 unique → 40 included | `search/openalex_search.py`; `search/openalex_candidates.json`; e2e README | PRISMA-style, not PRISMA-compliant; 311 non-advanced records not individually coded. |
| 0 fabricated/retracted references | `phase2-verification.md`; 40/40 OpenAlex DOI resolution; 39 DOI; 0 retracted per OpenAlex | No full-text verification; one HAL record has no DOI; one source is title-level. |
| Final paper: 6,804 words, 40 refs, 8 tables, appendices A–E | `stage5/paper-final.md`; `stage5/README.md`; e2e README | Word count is body; references/appendices excluded. |
| No method ranking, no universal-benchmark claim, no regulatory determination | Paper abstract and §6; Stage 3/4 revisions | The paper is corpus-scoped and states this. |
| Chinese abstract | `stage5/paper-final.md` § 摘要 | Simplified Chinese (zh-CN); ARS’s default pair is English + zh-TW; this is not a supported locale pack. |
| PDF/DOCX/TeX/MD formats | `stage5/`; `build_formats.py` | Pandoc absent; PDF is a 35-page `ctex` + `xelatex` fallback; DOCX is structural; not journal typesetting. |
| E2E used DSH inline roles | E2E README § What the e2e exercised; `model-portability.md` | The official e2e used one DSH session with inline roles; the additive native panel is separate (F). |

## D. Claims narrowed or corrected for this package

- **“43 prompt roles”** → the vendored tree contains **42** skill-agent
  Markdown files plus **4** root agent files. The README was corrected. The e2e
  ran the prompts inline; it did not execute 42/46 independent agents.
- **“16 commands”** → 16 generated wrappers are registered; the e2e exercised
  the skills, not every `/ars-*` wrapper.
- **“Full ARS core”** → the five skills plus root `scripts/`, `shared/`,
  `agents/`, and four root files. Generated `commands/` are adapter output;
  `docs/`, `evals/`, `examples/`, `hooks/`, `pi/`, and `audits/` are not
  vendored.
- **“Python tool layer used”** → installed and smoke-tested; the e2e’s integrity
  reports are agent-produced, not the output of a full checker run.
- **“5-seat review” in the official e2e** → five role-separated prompts run
  inline, not independent subagents; role separation is not a claim of
  independent error processes. The additive 0.4.0 native panel is separate (F).
- **“No PRISMA”** → the flow is PRISMA-style, not PRISMA-compliant; 311 records
  were not individually coded.
- **“zh-CN abstract”** → an operator-language choice for the e2e, not a locale
  pack or a claim of zh-CN support.
- **“Official sibling”** → not claimed; the design issue is the first contact.

## E. Known limits

- Abstract-level evidence: 10/40 preprints, 1 title-level, 4 partial; no full
  text.
- No plagiarism scan, no complete COI/funding audit, no dual screening.
- Semantic Scholar returned HTTP 429 at search time; Crossref returned one 429;
  no S2 verification layer.
- Official e2e: one DeepSeek Harness inline run; no Claude baseline; no
  independent subagent panel. The 0.4.0 native panel separately used five
  subagents + a Team board; it is not a model benchmark and does not retrofit
  the official e2e.

- The 35-page PDF and DOCX are working conversions, not journal typesetting.
- The e2e is platform evidence for sibling recognition, not a model benchmark
  and not an endorsement by the ARS maintainer.

## F. Native layer (0.4.2, additive)

| Claim | Evidence | Coverage / caveat |
| --- | --- | --- |
| 0.4.2 adds native team skills | `native/skills/ars-team/SKILL.md`, `native/skills/ars-pipeline-team/SKILL.md`; `lib/startup.js` `SKILL_DIRS`; `npm run verify` → 23 registrations | 0.3.0 remains 21; the official baseline is unchanged. |
| The five-seat panel ran with real subagents | `examples/dsh/iv-surface-review/stage3-team/` (field analysis, five seat reports, editorial decision, roadmap); Team board tasks | One native-layer validation run; the official e2e used inline prompts. Role separation is not independent error processes. |
| The native panel reached Major Revision | `stage3-team/editorial-decision.md`; six required majors + ten minor fixes | The paper’s Stage 3 decision; not a claim that the native layer improves review quality. |
| Five native tools exist | `lib/startup.js` `ars_search`/`ars_lookup`/`ars_integrity`/`ars_pipeline_status`/`ars_manifest`; `cordis.patch.yml` inject `[skills, tools, agentPresets]` | Registered only when the `tools` service is present; the current session was still 0.3.0, so the tools were not visible there. No exhaustive tool test. |
| The ARS Team preset is registered | `lib/startup.js` `ARS_PRESET`; `cordis.patch.yml` inject `agentPresets`; fake-context harness | Preset selection requires a new desktop session; not exercised in the current 0.3.0 session. |
| The native Team mapping is documented | `native/team-map.md`; `ars-team` skill; 0.4.0 panel artifacts | Seven review roles (field, five seats, editorial) and the 10 pipeline stages are mapped; the other 32 non-review ARS prompts remain inline. This is not a one-to-one 39-agent mapping. |
| The 0.4.2 native layer is additive | `package.json` 0.4.2; `files` includes `native/`; vendored core unchanged; `npm run verify` 23 | Not part of the 0.3.0 official sibling baseline; the 0.3.0 package remains the pinned official evidence. |
