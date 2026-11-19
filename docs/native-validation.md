# Native 0.4.4 — live validation

The 0.4.3 native layer passed the live check in a new desktop session: `ars-team` and `ars-pipeline-team` were listed as skills, `ars-team` was selectable as a preset, and `ars_search`, `ars_lookup`, `ars_integrity`, `ars_pipeline_status`, and `ars_manifest` were present. The smoke test also found one usability bug: `ars_pipeline_status` and `ars_integrity` resolved relative paths against the plugin root, not the calling Session's working directory. 0.4.4 fixes that by resolving relative paths through the Host `workingDirectory` service.

## Verified offline

- Profile dependency: `github:TY-Cheng/dsh-academic-research-skills#v0.4.4`; installed package version 0.4.4.
- `node tooling/verify-vendor.mjs` in the installed package: 199 skills, 644 scripts, 155 shared, 4 agents, 4 root files, 16 commands, **23 registrations OK**.
- The verifier's fake context warns `ctx.tools unavailable` and `ctx.agentPresets unavailable` — expected, because it only exercises the skill registrar. The real Host services are what the live session must show.
- The 0.4.4 relative-path harness: a fake `workingDirectory.ensure` returns the package checkout; `ars_pipeline_status` with `examples/dsh/iv-surface-review` returns the absolute workspace and the eight stage directories; `ars_integrity` with the same relative path checks the absolute workdir and returns 0 findings.
- 0.4.0 panel evidence exists under `examples/dsh/iv-surface-review/stage3-team/`; 0.4.4 adds the pipeline Team skill, the preset, the 5 tools, and the path fix.

## Clean install from the pinned commit (0.4.4)

Tested on macOS with DSH `0.2.2-rc.5` and pnpm `11.28.5`. With a new `DSH_HOME`, a fresh `web` profile, and an empty pnpm store, the following install completed successfully:

```bash
dsh plugin --profile web add 'git+https://github.com/TY-Cheng/dsh-academic-research-skills.git#2e4da620d697dec68ab74ef86dc94a0bb559924a'
```

- The lockfile resolved to the GitHub source archive for that exact commit, and the installed package reported version `0.4.4`. Its `package.json`, `lib/startup.js`, and `cordis.patch.yml` matched the pinned source byte-for-byte.
- `dsh --profile web --dump-config` included the `ars-skills` patch entry. Running `tooling/verify-vendor.mjs` from the installed package passed its file checks and reported **23 registrations OK**.

This verifies installation and profile configuration composition. The registrar check is offline; it does not exercise a live Host's native tools or agent preset. The existing desktop profile was unchanged.

## Live desktop result (0.4.4)

On 2026-11-19, a new DSH desktop session (`DSH-044 desktop smoke pipeline status check`) in Default Workspace called both native tools with the literal relative path `fork/examples/dsh/iv-surface-review`. The tool-call log confirms that both resolved it against the session's working directory, not the plugin installation directory. Both returned `/Users/tycheng/Documents/deepseek-harness/default-workspace/fork/examples/dsh/iv-surface-review` without error:

- `ars_pipeline_status`: `workspace` matched the expected path and `stages` contained eight directories.
- `ars_integrity`: `workdir` matched the expected path; `phase_dirs` was `{}` and `findings` was `[]`. Zero findings do not establish phase-level integrity coverage because the checker detected no phase directories.

This run verifies relative-path resolution for these two tools. It does not revalidate the full tool catalog or the agent preset on 0.4.4.

## New-session checklist for 0.4.4

1. Open a **new desktop session** after the profile is on `#v0.4.4`; the running session does not hot-reload a new plugin version.
2. Confirm `ars-team` and `ars-pipeline-team` in the skill list.
3. Confirm `ars_search`, `ars_lookup`, `ars_integrity`, `ars_pipeline_status`, `ars_manifest` in the tool list.
4. Confirm `ars-team` in the preset/agent selector.
5. Run the smoke:
   - `ars_pipeline_status` with `fork/examples/dsh/iv-surface-review` relative to Default Workspace — expect the absolute workspace and stage dirs.
   - `ars_integrity` with the same relative path — expect the same absolute `workdir`; report `phase_dirs` alongside `findings` so an empty result is not mistaken for coverage.
   - `ars_search` / `ars_lookup` / `ars_manifest` — expect records, metadata, and the pinned upstream.

## If something is missing

Collect the session's plugin list and the Host console lines containing `dsh-academic-research-skills`; the package logs one line when tools/preset are skipped. Do not reinstall blindly — the profile dependency is already the GitHub tag.

## Known limits

- The current authoring session was started against an older catalog; `skill("ars-team")` returned `unknown or no longer available`, and the tool list had no native tools until the new session. This is expected and is why the manual panel was used for the 0.4.0 evidence.
- `dsh --profile desktop --help` fails with `profile "desktop" is managed exclusively by the Electron application`; the desktop profile cannot be exercised headlessly.
- The preset is selectable only where `agentPresets` is present; the offline verifier skips it by design.
