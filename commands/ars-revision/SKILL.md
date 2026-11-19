---
name: ars-revision
description: "ARS academic-paper `revision` mode — revised draft + R&R responses"
disable-model-invocation: true
user-invocable: true
---

The user invoked `/ars-revision` (port of the Claude Code slash command). First call the `skill` tool with name `academic-paper` to load that skill (unless it is already loaded in this session), then execute the mode it specifies:

Trigger the `academic-paper` skill in `revision` mode. Produces a revised draft plus point-by-point response-to-reviewers. Fidelity spectrum, high oversight.

Mode reference: `MODE_REGISTRY.md` § academic-paper.
Skill entry: `academic-paper/SKILL.md`.

If the skill or a required file cannot be loaded, report the loading failure and stop; do not substitute this command summary for the mode instructions.

Note: this command was ported from the ARS Claude Code plugin (Imbad0202/academic-research-skills, CC-BY-NC-4.0). The ARS core (scripts/, shared/, agents/, MODE_REGISTRY.md) is vendored in this package; resolve those paths against the package root (DSH_ARS_ROOT), not the paper project working directory.
