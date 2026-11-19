# Stage 3 — Devil's Advocate Review

**Recommendation:** Major Revision

## Strongest counter-argument

The paper's central claim—that “arbitrage-free” is a family of guarantees—is almost tautological once one lists construction, penalty, projection, and generation. The taxonomy may be a useful description, but it does not explain why methods succeed or fail, and the paper's evidence is a 40-source convenience sample read at abstract level. A skeptical reader may ask: what would I do differently after reading this that I would not do after reading Homescu (2011) and Ruf and Wang (2020)? The answer must be concrete: the static/dynamic separation, the guarantee checklist, and the decision guide. The paper needs to make that answer explicit and falsifiable.

## Major issues

**DA1. The “so what” is under-argued.** The paper says the contribution is a map, but it does not show a decision that the map changes. Add a short “what changes for the reader” paragraph with two concrete choices (e.g., a desk choosing between SVI and a generative model; a benchmark designer choosing dimensions) and a table of testable propositions. Without this, the paper reads as a survey with a new vocabulary.

**DA2. The taxonomy is post hoc and may not be falsifiable.** The four families were imposed after reading the corpus; hybrid cases are resolved by a “primary mechanism” rule. State what would count as evidence against the taxonomy (e.g., a method that carries a guarantee through a mechanism not in the four families, or a case where the primary-mechanism rule misclassifies a method's failure mode). Add a “what would change this map” paragraph.

**DA3. The convenience sample and the negative claim.** The 40/351 selection is not a systematic screen; the 311 are not coded; the “no shared benchmark” finding is a negative claim from a single database. The paper qualifies it, but the qualification is buried. Put the scope condition in the abstract and the first finding, not only in §5.4.

## Minor issues

- The “frontier” label is rhetorical; tie it to the dynamic table.
- The 2026/2027 sources are very recent; check online-first status.
- The abstract is 216 words and dense; consider trimming the method detail.
- The paper says “no ranking” several times; keep one.

## Stress tests

| Test | Result |
|---|---|
| Remove the strongest source (Gatheral & Jacquier, 2014) | The parametric claim loses its canonical anchor but the taxonomy survives; confidence reduced. |
| Flip the RQ to “when do constraints fail?” | The corpus would over-represent successes; the paper's negative-result gap becomes central. |
| Apply to a different market (Asia/Europe) | Not established; the paper's SPX/US concentration is a real limit. |
| “So what?” | Yes for the guarantee checklist and decision guide; no for a method ranking or a causal theory. |

## What would make it acceptable

A “what changes for the reader” paragraph, a falsifiability statement, a testable-proposition table, and the scope condition in the abstract. These are revisions, not new data.
