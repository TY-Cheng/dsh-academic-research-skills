# dsh-academic-research-skills

[English](#english) · [中文](#中文)

DeepSeek Harness（DSH）插件：把 Claude Code 的
[Academic Research Skills (ARS)](https://github.com/Imbad0202/academic-research-skills)
（v3.24.2，CC-BY-NC-4.0）移植为 DSH 技能，并随包携带完整 ARS 核心工具层
（`scripts/`、`shared/`、根 `agents/` 与 `MODE_REGISTRY.md`）。

安装后自动获得：

- **5 个模型可调用技能**：`deep-research`（13-agent 调研团队，8 种模式）、
  `academic-paper`（12-agent 论文写作，11 种模式）、`academic-paper-reviewer`
  （5 席位同行评审面板）、`academic-pipeline`（10 阶段全流水线编排）、
  `sr-screener`（协议驱动的系统综述记录筛选，8 种模式）
- **1 个原生 DSH 团队技能**（0.4.0 原生层）：`ars-team`，
  用真实 `subagent` 跑五席位评审，而不是把角色提示内联在一个窗口里
- **2 个原生工具**（0.4.0）：`ars_search`（OpenAlex 检索）与 `ars_lookup`
  （DOI 元数据，OpenAlex/Crossref）；仅在 `tools` 服务挂载时注册，否则自动跳过
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
> 本仓库是 nullptr-DZF 原始 DSH 移植的维护分支，由 TY-Cheng 维护；
> 上游仍是 Imbad0202 的 ARS。

## 安装

要求：DeepSeek Harness（`dsh`）0.2.x（本次 e2e 在 0.2.2-rc.5 上验证），
pnpm 可用。完整确定性工具链另需 Python 3.9+；建议在插件目录建 `.venv`：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
# 可选：PDF 内容分类器
.venv/bin/python -m pip install -r requirements-pdf-content-classifier.txt
```

```bash
# 方式一：GitHub 仓库（当前 v0.4.0；官方收录基线仍是 v0.3.0）
dsh plugin --profile web add github:TY-Cheng/dsh-academic-research-skills#v0.4.0

# 官方收录基线（不含 0.4.0 原生层）
dsh plugin --profile web add github:TY-Cheng/dsh-academic-research-skills#v0.3.0

# 方式二：本地路径（开发调试）
dsh plugin --profile web add <本仓库绝对路径>

# 把 web 换成实际 profile（本次 e2e 用 desktop）；重启对应 profile 后生效
```

安装后 `dsh.profile.bundles` 会追加 `dsh-academic-research-skills`，启动时
`lib/startup.js` 把 22 个技能（5 个 vendored + 1 个 `ars-team` + 16 个命令）
注册进 `ctx.skills`；`manifest.json` 记录上游 pin，`SYNC_POLICY.md` 说明
vendored 边界。

## 使用

| 用法 | 操作 |
| --- | --- |
| 模型自动路由 | 直接说“做学术研究 / 文献综述 / 帮我审稿 / 写论文”等（技能描述带触发词） |
| 技能注入 | 输入 `/deep-research`、`/academic-pipeline` 等技能名 |
| 斜杠命令 | 输入 `/ars-full`（全流程）、`/ars-reviewer`（审稿）、`/ars-plan`（规划）等 |

## 与上游的差异

- **hooks 不移植**：上游 `hooks/hooks.json`（写保护 guard、SessionStart 播报）
  是 Claude Code 专属；DSH 无 hook 系统，写保护由 DSH 自身文件沙箱承担。
- **完整核心已 vendor**：`skills/`、`scripts/`、`shared/`、根 `agents/`、
  `MODE_REGISTRY.md` 与上游对应文件逐字节一致；`commands/` 是生成的 DSH
  适配层。Python 依赖见上。
- **路径解析**：注册时会在每个技能正文前加入 ARS package root 提示，
  `DSH_ARS_ROOT` 指向插件包根目录；`sr-screener` 自己的 `scripts/` 仍相对
  技能目录解析。这样 `python3 scripts/...` 不会误落到用户论文项目目录。
- **原生层（0.4.0）**：`native/skills/ars-team` 把五席位评审
  映射为真实 `subagent`；`lib/startup.js` 在 `tools` 服务可用时注册
  `ars_search` / `ars_lookup`。vendored 内容不变，0.3.0 官方基线不受影响。
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
npm run verify                                  # 离线哈希校验 + 22 个注册断言
```

---

<a name="english"></a>

# English

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin
port of Claude Code's
[Academic Research Skills (ARS)](https://github.com/Imbad0202/academic-research-skills)
(v3.24.2, CC-BY-NC-4.0). The package also carries the full ARS core:
`scripts/`, `shared/`, root `agents/`, and `MODE_REGISTRY.md`.

Provides, out of the box:

- **5 model-invocable skills**: `deep-research`, `academic-paper`,
  `academic-paper-reviewer`, `academic-pipeline`, `sr-screener`
- **1 native team skill** (0.4.0 native layer): `ars-team`, which runs
  the five-seat panel as real `subagent`s instead of inline role prompts
- **2 native tools** (0.4.0): `ars_search` (OpenAlex search) and `ars_lookup`
  (DOI metadata via OpenAlex/Crossref); registered only when the `tools`
  service is mounted, skipped otherwise
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
> This is the maintained fork of nullptr-DZF's original DSH port,
> maintained by TY-Cheng; upstream remains Imbad0202's ARS.

## Install

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
# current release (0.4.0 native layer; official-recognition baseline is v0.3.0)
dsh plugin --profile web add github:TY-Cheng/dsh-academic-research-skills#v0.4.0
# official-recognition baseline (no 0.4.0 native layer)
dsh plugin --profile web add github:TY-Cheng/dsh-academic-research-skills#v0.3.0
# or from a local checkout:
dsh plugin --profile web add /path/to/this/repo
# replace web with your profile (this e2e used desktop); restart it
```

The bundle patch mounts `lib/startup.js`, which registers the 22 skills
(5 vendored + `ars-team` + 16 commands) into `ctx.skills` at boot.

## Differences from upstream

- **Hooks are not ported**: upstream `hooks/` are Claude Code specific; DSH has
  no hook system (write protection is DSH's file sandbox).
- **Full core is vendored**: `skills/`, `scripts/`, `shared/`, root `agents/`,
  and `MODE_REGISTRY.md` are byte-identical to upstream; `commands/` is the
  generated DSH adapter layer. Python dependencies are listed above.
- **Path resolution**: every registered skill body is prefixed with an ARS
  package-root note; `DSH_ARS_ROOT` points at the plugin package root.
  `sr-screener`'s own `scripts/` still resolve relative to its skill directory,
  so `python3 scripts/...` does not fall through to the paper project.
- **Native layer (0.4.0)**: `native/skills/ars-team` maps the
  five-seat review to real `subagent`s; `lib/startup.js` registers
  `ars_search`/`ars_lookup` when the `tools` service is mounted. Vendored
  content is unchanged; the 0.3.0 official baseline is unaffected.
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
npm run verify                                      # hashes + 22 registration assertions
```
