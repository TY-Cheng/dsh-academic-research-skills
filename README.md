# dsh-academic-research-skills

[English](#english) · [中文](#中文)

<a name="english"></a>

# English

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin
port of Claude Code's
[Academic Research Skills (ARS)](https://github.com/Imbad0202/academic-research-skills)
(v3.24.4, CC-BY-NC-4.0). The package also carries the full ARS core:
`scripts/`, `shared/`, root `agents/`, and `MODE_REGISTRY.md`.

Provides, out of the box:

- **5 model-invocable skills**: `deep-research`, `academic-paper`,
  `academic-paper-reviewer`, `academic-pipeline`, `sr-screener`
- **2 native team skills** (0.4.4 native layer): `ars-team`, which runs the
  five-seat panel as real `subagent`s, and `ars-pipeline-team`, which maps the
  10 pipeline stages onto a Team-board stage task graph
- **5 native tools** (0.4.4): `ars_search` (OpenAlex search), `ars_lookup`
  (DOI metadata via OpenAlex/Crossref), `ars_integrity` (runs the vendored
  `check_pipeline_integrity.py`), `ars_pipeline_status` (stage-artifact
  inventory), and `ars_manifest` (pinned upstream/content counts); registered
  only when the `tools` service is mounted, skipped otherwise
- **Optional ARS Team agent preset** (0.4.4): registered when `agentPresets` is
  mounted; a new session can select the `ars-team` preset, which composes the
  `ars-team` skill with the Team board
- **Full ARS core**: root `scripts/` (Python checkers, ledger, citation gate,
  adapters), `shared/` (schemas/contracts), root `agents/`, and
  `MODE_REGISTRY.md`, byte-identical to upstream
- **16 user-invocable commands**: `/ars-full`, `/ars-plan`, `/ars-reviewer`,
  `/ars-lit-review`, `/ars-abstract`, `/ars-revision`, `/ars-outline`,
  `/ars-citation-check`, `/ars-disclosure`, `/ars-format-convert`,
  `/ars-rebuttal-audit`, `/ars-revision-coach`, `/ars-cache-invalidate`,
  `/ars-mark-read`, `/ars-unmark-read`, `/ars-3w`

> **Attribution**: this is a DSH port of ARS; skill content and commands are
> derived from Cheng-I Wu's
> [academic-research-skills](https://github.com/Imbad0202/academic-research-skills).
> Everything in this repo (including the porting layer) is licensed
> **CC-BY-NC-4.0** — non-commercial use only. See [NOTICE.md](NOTICE.md) and
> [LICENSE](LICENSE).
>
> This community DSH port is maintained by TY-Cheng and builds on
> nullptr-DZF's original port. It is not an official ARS release;
> upstream remains Imbad0202's ARS.

## Install

The current version is `v0.4.7`. See the [release notes](docs/releases/v0.4.7.md).

Requires DeepSeek Harness 0.2.x (tested on 0.2.2-rc.5) and pnpm. The
deterministic tooling also needs Python 3.9+; a plugin-local `.venv` is
recommended:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
# optional PDF content classifier
.venv/bin/python -m pip install -r requirements-pdf-content-classifier.txt
```

```bash
# current release (v0.4.7)
dsh plugin --profile web add github:TY-Cheng/dsh-academic-research-skills#v0.4.7
# v0.3.0 used for the e2e submitted for upstream review (no 0.4.4 native layer)
dsh plugin --profile web add github:TY-Cheng/dsh-academic-research-skills#v0.3.0
# or from a local checkout:
dsh plugin --profile web add /path/to/this/repo
# replace web with your profile (this e2e used desktop); restart it
```

The bundle patch mounts `lib/startup.js`, which registers 23 entries
(5 vendored skills, 2 native skills, and 16 commands) into `ctx.skills` at boot.

## Differences from upstream

- **Hooks are not ported**: the upstream Claude Code per-role write-scope
  guard and SessionStart announcement are unavailable in this port. On macOS,
  DSH `0.2.2-rc.5`'s file-write and Bash backends under the tested
  `workspace-write` policy allowed writes inside the workspace and denied the
  tested writes to a sibling directory. This is host-level confinement,
  not the ARS per-role guard. See the
  [test and its limits](docs/sibling-submission/claims-evidence.md#g-dsh-sandbox-write-boundary-smoke-test).
- **Full core is vendored**: `skills/`, `scripts/`, `shared/`, root `agents/`,
  and `MODE_REGISTRY.md` are byte-identical to upstream; `commands/` is the
  generated DSH adapter layer. Python dependencies are listed above.
- **Path resolution**: every registered skill body is prefixed with an ARS
  package-root note; `DSH_ARS_ROOT` points at the plugin package root.
  `sr-screener`'s own `scripts/` still resolve relative to its skill directory,
  so `python3 scripts/...` does not fall through to the paper project.
- **Native layer (0.4.4)**: `native/skills/ars-team` maps the five-seat review
  to real `subagent`s; `native/skills/ars-pipeline-team` maps the 10 stages onto
  a Team-board stage task graph; `lib/startup.js` registers
  `ars_search`/`ars_lookup`/`ars_integrity`/`ars_pipeline_status`/`ars_manifest`
  when the `tools` service is mounted, and an optional `ars-team` preset when
  `agentPresets` is mounted. Vendored content is unchanged; the native
  validation is separate from the v0.3.0 e2e submitted for upstream review.
- **Subagents**: the 42 skill-agent prompt files (plus the 4 root `agents/`
  files) run inline by default; `ars-team` uses `subagent`s for the five seats.
  Role separation is a process control, not proof of independent error
  processes.
- **Command wrappers are DSH-adapted**: the wrappers are regenerated from the
  upstream `commands/ars-*.md` and stripped of Claude Code's `Skill` tool calls
  and `${CLAUDE_PLUGIN_ROOT}` paths, so they run as-is under DSH.

## Regenerating command wrappers

`commands/` is generated from upstream `commands/ars-*.md`:

```bash
node tooling/regenerate-commands.mjs <upstream-checkout-path>
```

Regeneration also strips Claude Code's `Skill` tool call and
`${CLAUDE_PLUGIN_ROOT}` paths.

For a routine sync and offline check:

```bash
node tooling/sync-upstream.mjs <upstream-checkout>   # copy core + regenerate commands + manifest
npm run verify                                      # hashes + 23 registration assertions
```

---

<a name="中文"></a>

# 中文

DeepSeek Harness（DSH）插件：把 Claude Code 的
[Academic Research Skills (ARS)](https://github.com/Imbad0202/academic-research-skills)
（v3.24.4，CC-BY-NC-4.0）移植为 DSH 技能，并随包携带完整 ARS 核心工具层
（`scripts/`、`shared/`、根 `agents/` 与 `MODE_REGISTRY.md`）。

安装后自动获得：

- **5 个模型可调用技能**：`deep-research`（13-agent 调研团队，8 种模式）、
  `academic-paper`（12-agent 论文写作，11 种模式）、`academic-paper-reviewer`
  （5 席位同行评审面板）、`academic-pipeline`（10 阶段全流水线编排）、
  `sr-screener`（协议驱动的系统综述记录筛选，8 种模式）
- **2 个原生 DSH 团队技能**（0.4.4 原生层）：`ars-team` 用真实 `subagent` 跑五席位评审；
  `ars-pipeline-team` 把 10 阶段流水线映射成 Team board 的 stage task graph
- **5 个原生工具**（0.4.4）：`ars_search`（OpenAlex 检索）、`ars_lookup`
  （DOI 元数据，OpenAlex/Crossref）、`ars_integrity`（调用 vendored
  `check_pipeline_integrity.py`）、`ars_pipeline_status`（流水线阶段产物盘点）与
  `ars_manifest`（pinned upstream/内容计数）；仅在 `tools` 服务挂载时注册，否则自动跳过
- **可选 ARS Team agent preset**（0.4.4）：在 `agentPresets` 服务可用时注册，
  新会话可选择 `ars-team` 预设，组合 `ars-team` 技能与 Team board
- **映射、验证与市场草稿**：[`native/team-map.md`](native/team-map.md)、
  [`docs/native-validation.md`](docs/native-validation.md)、
  [`docs/market/listing.md`](docs/market/listing.md)
- **完整 ARS 核心工具层**：根 `scripts/`（Python 检查器、ledger、citation gate、
  adapters）、`shared/`（schema/合同）、根 `agents/` 与 `MODE_REGISTRY.md`，
  与上游对应文件逐字节一致
- **16 个用户可调用命令**：`/ars-full`、`/ars-plan`、`/ars-reviewer`、
  `/ars-lit-review`、`/ars-abstract`、`/ars-revision`、`/ars-outline`、
  `/ars-citation-check`、`/ars-disclosure`、`/ars-format-convert`、
  `/ars-rebuttal-audit`、`/ars-revision-coach`、`/ars-cache-invalidate`、
  `/ars-mark-read`、`/ars-unmark-read`、`/ars-3w`

> **署名 / Attribution**：本项目为 ARS 的 DSH 移植，技能内容与命令衍生自
> Cheng-I Wu（[Imbad0202](https://github.com/Imbad0202)）的
> [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)，
> 全部内容（含移植层）遵循 **CC-BY-NC-4.0**（非商业用途），详见
> [NOTICE.md](NOTICE.md) 与 [LICENSE](LICENSE)。
>
> 本仓库是由 TY-Cheng 维护的社区 DSH 移植，源自 nullptr-DZF 的移植版本，
> 不是 ARS 官方发行版；上游仍是 Imbad0202 的 ARS。

## 安装

当前版本为 `v0.4.7`；详见[发布说明](docs/releases/v0.4.7.md)。

要求：DeepSeek Harness（`dsh`）0.2.x（本次 e2e 在 0.2.2-rc.5 上验证），
pnpm 可用。完整确定性工具链另需 Python 3.9+；建议在插件目录建 `.venv`：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
# 可选：PDF 内容分类器
.venv/bin/python -m pip install -r requirements-pdf-content-classifier.txt
```

```bash
# 方式一：GitHub 仓库（当前 v0.4.7）
dsh plugin --profile web add github:TY-Cheng/dsh-academic-research-skills#v0.4.7

# 提交上游审查的 e2e 使用 v0.3.0（不含 0.4.4 原生层）
dsh plugin --profile web add github:TY-Cheng/dsh-academic-research-skills#v0.3.0

# 方式二：本地路径（开发调试）
dsh plugin --profile web add <本仓库绝对路径>

# 把 web 换成实际 profile（本次 e2e 用 desktop）；重启对应 profile 后生效
```

安装后 `dsh.profile.bundles` 会追加 `dsh-academic-research-skills`，启动时
`lib/startup.js` 把 23 个入口（5 个 vendored 技能 + 2 个原生技能 + 16 个命令）
注册进 `ctx.skills`；`manifest.json` 记录上游 pin，`SYNC_POLICY.md` 说明
vendored 边界。

## 使用

| 用法 | 操作 |
| --- | --- |
| 模型自动路由 | 直接说“做学术研究 / 文献综述 / 帮我审稿 / 写论文”等（技能描述带触发词） |
| 技能注入 | 输入 `/deep-research`、`/academic-pipeline` 等技能名 |
| 斜杠命令 | 输入 `/ars-full`（全流程）、`/ars-reviewer`（审稿）、`/ars-plan`（规划）等 |

## 与上游的差异

- **hooks 不移植**：上游 Claude Code 的按角色写入 guard 与 SessionStart
  播报在此移植版中不可用。macOS 上，DSH `0.2.2-rc.5` 的文件写入与
  Bash 后端在实测的 `workspace-write` 策略下允许 workspace 内写入、
  拒绝向测试用的相邻目录写入。这是宿主写入边界，不等同于 ARS 的按角色
  guard。见[实测与适用范围](docs/sibling-submission/claims-evidence.md#g-dsh-sandbox-write-boundary-smoke-test)。
- **完整核心已 vendor**：`skills/`、`scripts/`、`shared/`、根 `agents/`、
  `MODE_REGISTRY.md` 与上游对应文件逐字节一致；`commands/` 是生成的 DSH
  适配层。Python 依赖见上。
- **路径解析**：注册时会在每个技能正文前加入 ARS package root 提示，
  `DSH_ARS_ROOT` 指向插件包根目录；`sr-screener` 自己的 `scripts/` 仍相对
  技能目录解析。这样 `python3 scripts/...` 不会误落到用户论文项目目录。
- **原生层（0.4.4）**：`native/skills/ars-team` 把五席位评审
  映射为真实 `subagent`；`native/skills/ars-pipeline-team` 把 10 阶段流水线
  映射为 Team board 的 stage task graph；`lib/startup.js` 在 `tools` 服务
  可用时注册 `ars_search`/`ars_lookup`/`ars_integrity`/`ars_pipeline_status`/
  `ars_manifest`，在 `agentPresets` 可用时注册可选 `ars-team` preset。
  vendored 内容不变；原生层验证与提交上游审查的 v0.3.0 e2e 分开。
- **子代理**：5 个 vendored 技能内共 42 个 agent 提示文件（另有 4 个根
  `agents/` 文件）默认内联运行；`ars-team` 用 `subagent` 分工跑五席位。
  角色分离是流程控制，不是独立误差过程的证明。
- **命令包装为 DSH 适配版**：由上游 `commands/ars-*.md` 再生成并去掉 Claude
  Code 专属的 `Skill` 工具调用与 `${CLAUDE_PLUGIN_ROOT}` 路径，产物可直接在
  DSH 中执行（见下节）。

## 重新生成命令包装

`commands/` 由上游 `commands/ars-*.md` 转换而来（加入
`disable-model-invocation: true` + `user-invocable: true`）：

```bash
node tooling/regenerate-commands.mjs <上游仓库路径>
```

再生成时会自动去掉 Claude Code 专属的 `Skill` 工具调用和
`${CLAUDE_PLUGIN_ROOT}` 路径。

日常同步与校验：

```bash
node tooling/sync-upstream.mjs <上游仓库路径>   # 复制核心 + 生成命令 + 写 manifest
npm run verify                                  # 离线哈希校验 + 23 个注册断言
```
