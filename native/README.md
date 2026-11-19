# Native DSH layer (0.4.0, unreleased)

This directory holds the DSH-native additions that sit on top of the vendored
ARS content. Nothing here changes `skills/`, `scripts/`, `shared/`, `agents/`,
or `MODE_REGISTRY.md`; those remain byte-identical to upstream.

- `skills/ars-team/SKILL.md` — maps the five-seat
  `academic-paper-reviewer` panel (field analyst + methodology/domain/
  perspective reviewers + devil's advocate + editorial synthesizer) to real DSH
  `subagent` calls, instead of running the role prompts inline in one window.
- `ars_search` / `ars_lookup` — native read-only tools registered by
  `lib/startup.js` when the DSH `tools` service is mounted. They query OpenAlex
  and Crossref; they do not shell out to Python.

The native layer is additive: the 1,006 vendored files and the 0.3.0
official-recognition baseline are unchanged. `npm run verify` expects 22 skill
registrations (5 vendored + `ars-team` + 16 command wrappers); the native tools
are skipped in the offline verifier, which has no `tools` service.
