# Phase 4a — Writer Paper-Blind Pre-Commitment

**Run:** `iv-surface-review-v047` · **Stage 2, Phase 4a** · **Agent role:** draft_writer (paper-blind call) · **Contract:** `academic_paper/writer_full/v1` (schema 13.1, baseline v3.6.6) · **Date:** 2026-11-23

**User content seen at this call (and nothing else):** the `writer_full` contract JSON; paper metadata — `title`: "Four Loci of Enforcement: Static and Dynamic No-Arbitrage in Equity-Index Implied-Volatility Surfaces, 2015–2026"; `field`: Finance / quantitative finance — derivatives, implied volatility; `word_count`: 7,400.

**Not seen at this call:** Paper Configuration Record, Paper Outline, Argument Blueprint, Annotated Bibliography, evidence map, or any draft text. The criteria below are paraphrased from the contract and the metadata only; no drafting artefact informed them.

## Acceptance Criteria Paraphrase

### D1: section_completeness

Mandatory. Every section in the Structure Architect's approved outline must be written before handoff to citation compliance, with no `[MATERIAL GAP]` placeholder left unresolved. In practice: I will enumerate the outline's sections and subsection headings before writing, write each one to its declared purpose, and re-check the enumeration against the finished body. A heading that exists but carries no prose, or prose that ends in a placeholder, counts as a block-level failure. Where the outline allocates tables or figures to a section, the section must actually carry them and refer to them in its text.

### D2: citation_density

Mandatory. Every factual claim must carry at least one citation to an assigned source; hedging language alone does not satisfy the dimension. Uncited factual claims must either gain a source, be omitted, or be marked `[MATERIAL GAP]`. I will treat any sentence that asserts what a study did, found, or reported as requiring a citation, and any sentence that states a number as requiring a citation unless the number is the review's own coded count — and coded counts will be attributed explicitly to this review's coding so they are not mistaken for source claims. Under the #548 exception, an absence or novelty claim cannot cite a source for an absence: it satisfies this dimension through documented-search provenance in the bounded form plus a citation to the named nearest prior work where adjacent work exists, or an explicit absence-of-adjacent-work statement otherwise. My bound will name the database, the date range, and the last search date actually used, and it will name the nearest prior work rather than asserting field-wide novelty.

### D3: argument_blueprint_fidelity

Mandatory. Each section must follow the claim–evidence–reasoning chains delivered by the Argument Blueprint, not a chain invented at drafting time: topic sentences match the chain's claim, the evidence cited for a claim is the set of sources the blueprint assigned to it, and the explanation links back to the declared section purpose. The Argument Blueprint, not this contract, is the source of the chains. I will read each chain's claim, evidence list, counter-argument, and strength rating before writing the corresponding section, and I will keep counter-arguments visible where the blueprint rates counter-argument risk as rising, rather than writing a one-sided account. If a chain's evidence cannot support its claim as stated, the honest move is to narrow the claim to what the assigned evidence licenses, not to import an unassigned source or a stronger assertion.

### D4: total_word_count

High priority. The finished body must stay within ±10 percent of the 7,400-word target declared in the Paper Configuration Record — that is, between 6,660 and 8,140 words — and must never exceed the record's hard ceiling. I will therefore measure the body by the canonical whitespace-split algorithm after stripping audit markers, exclude the title, abstract, keywords, tables, figure captions, references, declarations, and appendices exactly as the configuration states, and report the measured total with the measurement method named so it can be reproduced. If the first pass overshoots, I trim prose rather than deleting cited evidence; if it undershoots, I develop the declared sections rather than adding new claims.

### D5: per_section_word_count

High priority. Each section must stay within ±15 percent of the per-section allocation declared in the Paper Configuration Record. This constrains where length may go: a section that is comfortable but over its allocation is still a failure, and a short section cannot borrow a neighbour's budget. I will record the allocation per section before drafting, write to those budgets, and check each section's count individually rather than only the total, because a compensating error between two sections satisfies D4 while failing D5. Headings, tables, and references are excluded from every section count by the same convention as D4.

### D6: paragraph_structure

Normal priority. Each body paragraph must serve its section's purpose with a clear point, adequate cited support, explanation, and linkage, judged by clarity and evidential support rather than a TEEL percentage or a length preset; author and venue requirements take priority over any structural template, and transitions must be present between sections. I will give each paragraph one claim, the evidence that licenses it, and the reasoning that connects them, and I will not pad, split, or stretch paragraphs to meet a count. Every section boundary will carry an explicit transition sentence so the argument's movement is visible without a heading performing the work.

### D7: register_consistency

Normal priority. Academic register must hold throughout, with no colloquial mixing and with discipline-appropriate phrasing per the Paper Configuration Record: third-person formal prose, active voice where it does not misattribute agency, and hedging proportioned to the evidence rather than applied uniformly. In this field the register is also a precision requirement — a "test" is not a "proof", "reported" is not "established", and a phrase used loosely by practitioners must be defined before the paper relies on it. I will keep terminology fixed once defined, define every abbreviation at first use, and avoid evaluative vocabulary that would imply a ranking where none is licensed.

[PRE-COMMITMENT-ACKNOWLEDGED]
