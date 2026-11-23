# NOTICE — 署名 / Attribution

## 本仓库是什么 / What this is

`dsh-academic-research-skills` 是 DeepSeek Harness（DSH）插件形态的
**Academic Research Skills (ARS)** 移植版。ARS 原本是 Claude Code 插件
（research → write → review → revise → finalize 的契约审计学术流水线）。
本包将其 5 个 vendored 技能、1 个原生 `ars-team` 技能与 16 个斜杠命令
移植为 DSH 技能注册，并加入 2 个只读原生工具（`ars_search`、`ars_lookup`）。

This repository is a DeepSeek Harness (DSH) plugin port of
**Academic Research Skills (ARS)**, originally a Claude Code plugin providing a
contract-audited academic research pipeline
(research → write → review → revise → finalize).

## 上游项目 / Upstream

| 项 | 值 |
| --- | --- |
| 项目 / Project | Academic Research Skills |
| 作者 / Author | Cheng-I Wu |
| 作者主页 / Author URL | https://github.com/Imbad0202 |
| 上游仓库 / Upstream repo | https://github.com/Imbad0202/academic-research-skills |
| 上游版本 / Upstream version | 3.24.4 |
| 上游许可 / Upstream license | [CC-BY-NC-4.0](LICENSE) |

## 内容归属 / Content ownership

- 本包中的 5 个技能包（`skills/deep-research`、`skills/academic-paper`、
  `skills/academic-paper-reviewer`、`skills/academic-pipeline`、
  `skills/sr-screener`，含其 `SKILL.md`、`agents/`、`references/`、
  `templates/`、`examples/`、`scripts/`）、16 个命令定义（`commands/`），
  以及根 `scripts/`、`shared/`、`agents/`、`MODE_REGISTRY.md`、
  `THIRD_PARTY.md` 与 Python 依赖清单（`requirements-*.txt`）
  **全部衍生自上游项目**，继续以
  **CC-BY-NC-4.0** 授权。任何再分发须保留本署名并仅限非商业用途。
- 移植层（`lib/startup.js`、`cordis.patch.yml`、`tooling/`、注册时的
  ARS package root 路径提示、打包与文档）最初由
  `nullptr-DZF` 完成，现由 `TY-Cheng` 维护；为保持一致同样以
  **CC-BY-NC-4.0** 发布。
- 原生层（`native/skills/ars-team`、`ars_search`/`ars_lookup` 工具定义）
  由 `TY-Cheng` 编写，不衍生自上游内容；与移植层一样以
  **CC-BY-NC-4.0** 发布。

The 5 skill bundles, 16 command definitions, and the root `scripts/`,
`shared/`, `agents/`, `MODE_REGISTRY.md`, `THIRD_PARTY.md`, and
`requirements-*.txt` in this package are **derived from the upstream project**
and remain licensed under **CC-BY-NC-4.0**; any redistribution must retain this
attribution and stay non-commercial. The porting layer (registrar, bundle
patch, `tooling/`, the ARS package-root path note, packaging, docs) was
originally written by `nullptr-DZF` and is now maintained by `TY-Cheng`,
released under the same license for consistency. The native layer
(`native/skills/ars-team`, the `ars_search`/`ars_lookup` tool definitions) was
written by `TY-Cheng`, is not derived from upstream content, and is released
under the same license.

## 维护者 / Maintainer

- 维护者 / Maintainer: TY-Cheng — https://github.com/TY-Cheng
- 本仓库 / This repo: https://github.com/TY-Cheng/dsh-academic-research-skills
- 原始移植 / Original port: nullptr-DZF — https://github.com/nullptr-DZF/dsh-academic-research-skills
