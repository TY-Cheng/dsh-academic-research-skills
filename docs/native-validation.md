# Native 0.4.2 — live validation checklist

The package and profile are installed and offline-verified. The remaining check is a **new desktop session**: the current session was started against 0.3.0 and does not reload the 0.4.2 catalog.

## What is already verified

- Profile dependency: `github:TY-Cheng/dsh-academic-research-skills#v0.4.2`; installed package version 0.4.2.
- `node tooling/verify-vendor.mjs` in the installed package: 199 skills, 644 scripts, 155 shared, 4 agents, 4 root files, 16 commands, **23 registrations OK**.
- The verifier's fake context warns `ctx.tools unavailable` and `ctx.agentPresets unavailable` — expected, because it only exercises the skill registrar. The real Host services are what the live session must show.
- 0.4.0 panel evidence exists under `examples/dsh/iv-surface-review/stage3-team/`; 0.4.2 adds the pipeline Team skill, the preset, and the 5 tools.

## New-session checklist

1. Open a **new desktop session** (not this one). The profile is already `#v0.4.2`; no reinstall is needed.
2. In the skill list, confirm `ars-team` and `ars-pipeline-team` are present.
3. In the tool list, confirm `ars_search`, `ars_lookup`, `ars_integrity`, `ars_pipeline_status`, `ars_manifest`.
4. In the preset/agent selector, confirm `ars-team` is selectable.
5. Run a small smoke:
   - `ars_search` with a short IV-surface query; expect records.
   - `ars_lookup` with a known DOI; expect metadata.
   - `ars_pipeline_status` on `examples/dsh/iv-surface-review`; expect stage2/stage3/stage3-prime/stage3-team/stage4/stage4-prime/stage4.5/stage5.
   - `ars_manifest` with no arguments; expect upstream `6d93886` and 1,006 vendored files.
   - `ars_integrity` on an empty temp directory; expect 0 findings.

## If something is missing

Collect the session's plugin list and the Host console lines containing `dsh-academic-research-skills`; the package logs one line when tools/preset are skipped. Do not reinstall blindly — the profile dependency is already the GitHub tag.

## Known limits

- The current session still has the 0.3.0 catalog; `skill("ars-team")` returned `unknown or no longer available`, and the tool list had no native tools. This is expected and is why the manual panel was used.
- `dsh --profile desktop --help` fails with `profile "desktop" is managed exclusively by the Electron application`; the desktop profile cannot be exercised headlessly.
- The preset is selectable only where `agentPresets` is present; the offline verifier skips it by design.
