## Journal-Fit Review Report

**Manuscript:** Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches
**Source file:** `examples/dsh/iv-surface-review/stage5/paper-final.md`
**Review date:** 2026-11-19
**Review round:** Round 1 (independent seat card; not a re-review)
**Declared article type:** structured literature review (APA 7.0; JEL G13, C45, C63)
**Target binding:** `criteria_binding_unavailable` — no author-confirmed ReviewTargetContext or Target Criteria Brief was supplied with this dispatch; this card is field-general and makes no venue-alignment claim.

### Reviewer Identity

Associate Editor of a general quantitative-finance journal with a reviews-and-surveys remit; derivatives-pricing research background; 15 years of editorial experience across mathematical and computational finance, including commissioned surveys and unsolicited review submissions. I routinely decide whether a literature synthesis clears a field journal's originality bar, and I read every manuscript first as an editor deciding what to do with it, then as a reader asking whether it earns its space.

Scope disclosure: I do not adjudicate no-arbitrage mathematics, literature completeness, or systematic-review methodology. Those are the remits of the peer-review seats and are used here only as cross-checks. My confidence is in the contribution, readership, and structural judgement.

### Review Focus

Whether the four-family enforcement taxonomy is a genuine advance over Homescu (2011) and Ruf and Wang (2020) rather than a relabeling of known distinctions; whether the seven-dimension evaluation matrix changes how a reader classifies or evaluates methods; and whether the manuscript's framing, scoping, and article-type presentation are pitched at a general finance readership and proportionate to what a purposive, abstract-level corpus can support. The review applies the manuscript's declared type — a structured literature review — as its yardstick and does not require a PRISMA-compliant screen or new empirical benchmarks.

### Overall Recommendation

**Major Revision** — substantial revision and re-review required. The core contribution survives and no new data are needed, but two decision-bearing issues are unresolved: the originality delta against the closest prior survey is asserted rather than demonstrated (W1), and the article-type/venue positioning is not reconciled with the corpus and apparatus the manuscript actually carries (W2). The remaining findings are repairable within a revision.

### Confidence Score

**4** — Mostly within my area of expertise; high confidence.

Standard legend: 1 = outside my area; 2 = adjacent area, limited confidence; 3 = competent in the area; 4 = mostly within my area, high confidence; 5 = directly within my area, very high confidence.

Confidence is an uncertainty/scope disclosure only; it never changes consensus counts, severity, decision bearing, or arbitration.

### Calibration Status

`NOT_CALIBRATED`

This seat has not been calibrated against a gold-standard review set for this venue family; no calibration weighting or historical agreement adjustment is applied. The judgements below are criterion-bound editorial judgements, not calibrated predictions.

### Criterion-Bound Judgements

Target-binding disclosure: `criteria_binding_unavailable`. No author-confirmed target metadata was supplied, so no row assesses alignment to a named journal, track, or article-type quota.

| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| Originality: advance over the closest prior reviews (Homescu, 2011; Ruf and Wang, 2020) | Reviewer Configuration Card #1, Review Focus 1; quality rubric Dimension 1 | PARTLY_MEETS | text: §1.5 "replaces a method-family list with an enforcement taxonomy"; §2.1 "makes the constraint taxonomy explicit" | The manuscript states three respects in which it differs from Homescu but never maps its four families onto Homescu's constraint taxonomy, so the headline novelty cannot be verified from the paper | I cannot read Homescu's full taxonomy within this remit; the delta may be defensible once shown | Yes — W1; unresolved originality blocks acceptance |
| Significance and impact for the stated readership | Card #1, Review Focus 1–2; rubric Dimension 7 | PARTLY_MEETS | table: Table 2 — "Guarantee" and "Main failure mode" columns; text: §5.2 "These propositions are not tested in the corpus; they are a research agenda, not findings" | The paper supplies a reporting standard, a shared vocabulary, and testable propositions, but demonstrates no use of the framework beyond proposing it | Venue-dependent; with no bound target this cannot be sharpened further | Yes — supports a revise decision rather than rejection |
| Venue alignment to a named journal or track | criteria_binding_unavailable | NOT_ASSESSED | — | No author-confirmed target; the manuscript declares "General academic journal / arXiv-style preprint (no specific venue)" | No venue-specific criteria exist in this dispatch | No — replaced by the two rows below |
| Readership fit and framing (general finance reader vs IV specialist) | Card #1, Review Focus 2 | MEETS | text: §1.5 "The primary reader is a model-risk/model-validation analyst or a benchmark designer"; §1.2 "The result is that cross-paper claims of superiority are difficult to justify" | The which-guarantee hook is legible to a general reader, the primary reader is named, and §5.1 and Table 7 translate the framework without specialist machinery | Parameter detail in §2.1 and protocol detail in §3 still assume a quant reader | Yes — positive; argues against rejection on accessibility grounds |
| Article-type coherence and proportionality (review vs research in disguise; scoping language) | Card #1, Review Focus 3 | PARTLY_MEETS | text: §3.1 "It is not a PRISMA-compliant systematic review"; §3.7 "The corpus is a purposive, reproducible-but-not-exhaustive sample" | The manuscript disclaims systematic-review status in wording while carrying systematic-review-style reporting apparatus and original prescriptions; the two frames are never reconciled | No bound venue to set the bar | Yes — W2 |
| Argument coherence (Title → Abstract → Introduction → Conclusion) | Rubric Dimension 4 | PARTLY_MEETS | table: Table 5 — status column shows four "Resolved in synthesis" rows against §4.7's "five were resolved"; text: §5.2 "It generates four testable propositions" against Table 6 rows P1–P6 | The argument chain is traceable, but the paper's self-referential counts and the abstract's gap list diverge from what §5.5 and Table 8 deliver | None material once corrected | Yes — W4, repairable within a revision |
| Writing quality | Rubric Dimension 5 | MEETS | text: §2.6 "The four families describe the primary mechanism that carries the guarantee; a method may combine stages" | Prose is precise, plain, and operational; definitions are stated in use rather than assumed | Copyedit-level issues only | No — positive |
| Evidence sufficiency for the central taxonomy claim | Rubric Dimension 3 (contribution level only) | PARTLY_MEETS | table: Appendix D — enforcement-family column, including eight records labelled "None/soft" outside the four families; Table 2 reports no family counts | The source-level mapping exists in an appendix but is never aggregated in the main text, and the residual no-guarantee category is left undefined | Review-methodology sufficiency is outside this seat's remit | No — W3 |

Note: Do not total, weight, average, or mechanically map these judgements to the recommendation. The recommendation rests on the decision-bearing rows identified above — in particular the unresolved originality and article-type criteria.

### Summary Assessment

This manuscript is a structured, corpus-scoped literature review of arbitrage-free implied volatility surface construction across parametric, nonparametric, neural, and generative methods. From a corpus of 40 sources retrieved through 24 OpenAlex queries, it classifies methods by where the no-arbitrage constraint enters the construction pipeline — construction, penalty, projection/repair, or generation plus filtering — proposes a seven-dimension evaluation matrix, and argues that "arbitrage-free" names a family of guarantees rather than a single property. As an editor, I find it unusually clear, well organized, and candid about the limits of its evidence; the taxonomy and the static/dynamic distinction give a general finance reader a genuinely useful frame, and the reporting standard in §5.3 is the kind of contribution a review venue can publish. Its central weakness is that the headline originality claim is asserted rather than demonstrated against Homescu (2011), which the manuscript itself credits with "the constraint taxonomy", and that the review frame is never reconciled with the purposive, abstract-level corpus or with any named venue. The bookkeeping slips — the abstract's six-gap list, §4.7's counts, the proposition count — are repairable within a revision. Because the core contribution survives but its originality and positioning need substantive work, Major Revision is the appropriate disposition.

### Strengths

**S1. A clear, answerable research question and a thesis that survives the whole paper.**
Evidence Anchor: text: §1.3 "How do parametric, nonparametric, and neural methods for constructing equity-index implied volatility surfaces enforce static and dynamic no-arbitrage constraints"

The question is specific, comparative, and answerable within the declared corpus; the paper returns to it explicitly in §6, so the reader can check that the answer is the one promised.

**S2. Unusually candid evidence disclosure for a review of this genre.**
Evidence Anchor: text: §3.7 "The screening counts are a rationale, not a full audit"

Rather than dressing a purposive corpus as an exhaustive screen, the manuscript states the limitation in the methods, the findings, and the discussion. For an editor, this is the responsible form of the hedging that W5 argues is overdone — the transparency itself is a strength and should be preserved.

**S3. The four-family taxonomy gives each enforcement mechanism a distinct guarantee and a distinct failure mode.**
Evidence Anchor: table: Table 2 — "Guarantee" and "Main failure mode" columns; each family row pairs a guarantee type with its characteristic failure

The contribution of Table 2 is not the list of four families but the pairing: construction admits a parametric region but restricts shape; a penalty does not guarantee anything at inference; projection repairs statically and not dynamically; generation plus filtering is only as good as its filter. That pairing is the paper's most durable conceptual asset and the clearest reason to publish it.

**S4. The reporting recommendation is concrete enough to be used.**
Evidence Anchor: text: §5.3 "reporting the guarantee family, the static and dynamic test results, and the evaluation dimensions"

A review that gives a model-validation team a one-line reporting standard has done something an editor can defend; this is the paper's most practical sentence and should be foregrounded in the abstract and conclusion.

**S5. The static/dynamic distinction is handled with more care than the literature usually shows.**
Evidence Anchor: text: §2.4 "static no-arbitrage is necessary but not sufficient"

The paper correctly separates the two layers and uses the separation to explain why cross-paper comparisons of "arbitrage-free" claims fail. That explanatory move is genuinely useful and is independent of the taxonomy-coverage issue in W3.

**S6. The corpus documentation makes the review auditable.**
Evidence Anchor: table: Appendix E — 24-query log with OpenAlex match counts; Appendix B — 40-record corpus index

Appendix E records the queries and match counts, Appendix B lists all 40 records with metadata, and Appendix D maps every record to the taxonomy. A reader can re-run the search at the level claimed and see exactly which source grounds which sentence — rare in reviews of this literature and a real credit to the manuscript.

### Weaknesses

**W1. The originality delta against the closest prior survey is asserted, not demonstrated.**

- **Problem:** §1.5 and §2.1 credit Homescu (2011) with "the constraint taxonomy", and §1.5 claims the review "replaces a method-family list with an enforcement taxonomy", but the paper never lays out Homescu's taxonomy and compares it with its four families. The same weakness appears, more mildly, with Ruf and Wang (2020): the paper adopts their "no common benchmark" finding as confirmation rather than as a prior result to extend. A reader therefore cannot tell whether the enforcement axis is new, a relabeling of the static/dynamic constraint split, or a refinement of a taxonomy already present in the survey.
- **Evidence Anchor:** text: §1.5 "replaces a method-family list with an enforcement taxonomy"; §2.1 "makes the constraint taxonomy explicit"
- **Why it matters:** This is the manuscript's headline contribution claim. If an editor cannot verify the delta against the one survey the paper names as its closest antecedent, the paper cannot clear an originality bar; if the delta is small, the paper should reposition around the matrix and the post-2020 generative corpus rather than around the taxonomy.
- **Suggestion:** Add a two-column mapping of Homescu's categories to the four enforcement families (including the "None/soft" residual), and state in one sentence what is new: the organizing axis itself, the coverage of generative/operator methods, or the corpus-scoped evidence map. If the honest answer is "the axis applied to a post-2020 generative corpus", say that and drop the broader "replaces" language.
- **Severity:** Major
- **Confidence:** 4 — core competence: originality assessment of review articles from 15 years of editorial handling of surveys and syntheses.

**W2. The article type is not settled, and the review apparatus is disproportionate to the declared contribution.**

- **Problem:** The manuscript is declared a literature review and explicitly disclaims systematic-review status, yet roughly 1,100 words of §3 plus Appendices A, C, and E describe a screening protocol, a 351 → 40 flow, and a 24-query log with OpenAlex match counts. Meanwhile the manuscript names no target venue, so neither the systematic-review bar nor a conceptual-essay bar can be applied, and the declared primary reader is a model-risk/model-validation analyst while the declared venue is a general academic finance venue — a practitioner-facing product in academic packaging. The result is that a review-track editor must first decide what kind of article this is before deciding whether it works, and the paper spends scarce space on protocol detail that neither plausible bar requires.
- **Evidence Anchor:** text: §3.1 "It is not a PRISMA-compliant systematic review"; §3.7 "The corpus is a purposive, reproducible-but-not-exhaustive sample"
- **Why it matters:** Article type governs the review criteria, expected length, methods standard, and readership; leaving it unresolved is a fit problem, not a copyedit. It also signals an unresolved submission strategy: the apparatus is written for a systematic-review audience the paper declines to address.
- **Suggestion:** Choose the venue first and let it set the type. For a reviews-and-surveys remit at a general quant-finance journal, compress Appendices A, C, and E into one "search note" and let §2's framework lead. For a systematic-review outlet, the corpus and screening would have to be rebuilt — a different paper. For an arXiv-style preprint, keep the apparatus but remove the systematic-review vocabulary and the front-matter pipeline labels.
- **Severity:** Major
- **Confidence:** 3 — editorial judgement on review-track fit; confidence is moderated because no venue is bound, so the finding is conditional on the only plausible field-general profiles.

**W3. Enforcement-family coverage is never quantified, and the residual category is undefined.**

- **Problem:** Table 1 (method families) and Table 2 (enforcement families) are not parallel: Table 1 reports counts, Table 2 does not. Appendix D is the only place where every source receives an enforcement label, and 11 of the 40 records fall outside the four families (8 "None/soft", 2 survey entries such as "Survey (no construction)", 1 "Evaluation/detection"), with "None/soft" never defined in the main text and never named in Table 2. The paper's own sentence about "eight constraints/evaluation sources" therefore cannot be reconstructed from the main text.
- **Evidence Anchor:** table: Appendix D — enforcement-family column: eight records "None/soft", two survey entries, one "Evaluation/detection", none of which appears as a category in Table 2
- **Why it matters:** The claim that enforcement mechanism is the better organizing variable is only as strong as its coverage. Leaving roughly a quarter of the corpus in an undefined residual invites the reading that the taxonomy is fitted to a convenient subset, and it weakens the otherwise strong Table 2 argument.
- **Suggestion:** Add an enforcement-family count column to Table 2 (or a compact accompanying table), define "None/soft" in §2.6, and state coverage explicitly — for example, "29 of 40 sources carry a guarantee mechanism; 8 report no enforcement; 3 are surveys or detection studies".
- **Severity:** Minor
- **Confidence:** 4 — verified by recounting the Appendix D rows directly.

**W4. Self-referential counts and deliverable lists diverge across sections.**

- **Problem:** §4.7 reports seven pairs with five resolved, one unresolved, and one not applicable, but Table 5 records four resolved (CP-001, CP-002, CP-003, CP-005), one unresolved (CP-004), and two not applicable (CP-006, CP-007). §5.2 promises "four testable propositions" while Table 6 lists six (P1–P6). The abstract's six gaps include cross-market evidence, which §5.5 and Table 8 replace with head-to-head enforcement under distribution shift. And §1.5's three contributions (taxonomy; static/dynamic separation; seven-dimension matrix) differ from §6's three (taxonomy; matrix; corpus-scoped evidence map).
- **Evidence Anchor:** text: §4.7 "Five were resolved as conditional differences or method-class differences; one was flagged unresolved; one was not applicable"
- **Why it matters:** These are the paper's own bookkeeping claims about its deliverables, and when they disagree with its tables the synthesis looks less controlled than the prose claims; the abstract also promises a gap that the agenda does not deliver. Each slip is individually trivial, but together they cost the paper the appearance of care on which a review's authority depends.
- **Suggestion:** Regenerate the abstract's gap list from Table 8, correct §4.7 to the Table 5 counts, write "four propositions plus two evaluation propositions" (or list all six), and align §6's contribution list with §1.5.
- **Severity:** Minor
- **Confidence:** 4 — verified directly against Table 5, Table 6, Table 8, and §6.

**W5. Over-hedging pre-empts the contribution.**

- **Problem:** The contribution is announced as "deliberately modest"; the abstract's final sentence is a disclaimer; §5.3 and Table 7 repeat the same non-ranking caveat twice in adjacent lines; §5.4 reports six limitations and the manuscript's own adversarial review; and §5.5 closes on what the paper cannot support. Hedging is accurate here, but its density means a skimming editor meets several qualifications before reaching the contribution's content, and the paper's final impression is defensive.
- **Evidence Anchor:** text: §1.5 "The contribution is deliberately modest"; §5.5 "It cannot support a method ranking, a claim that no benchmark exists anywhere"
- **Why it matters:** Scoping language is doing two jobs — protecting the reader from over-inference and protecting the paper from attack — and the second job shows. A review article should end on the usable claim, not on its retraction; the candour itself (S2) should be preserved, while its repetition is trimmed.
- **Suggestion:** Keep one clear scope paragraph and move the repeated disclaimers into §5.4 and the Declarations; end the abstract and §6 with the actionable message ("report the guarantee, not just the fit") without a trailing caveat.
- **Severity:** Minor
- **Confidence:** 5 — direct editorial experience reading review submissions; the rhetorical pattern is verifiable from the manuscript alone.

### Detailed Comments

#### Journal Fit

The manuscript declares no specific venue, so fit cannot be scored against binding criteria; `criteria_binding_unavailable` applies and I make no venue-alignment claim. At the field-general level it fits a reviews-and-surveys remit at a general quantitative-finance journal or an arXiv-style preprint; it does not fit a top empirical finance outlet, which the paper itself acknowledges. The advisory candidates for this field — Quantitative Finance, Journal of Computational Finance, and Journal of Financial Data Science, with Applied Mathematical Finance as an alternative — are context, not a determination. Two fit-relevant tensions remain. First, the paper names a practitioner as its primary reader while declaring a general academic venue; a general academic reader will expect the synthesis argument to carry more weight than the practitioner guide, whereas the paper's most confident pages are the practitioner-facing ones. Second, the corpus is heavily SPX/US-index; defensible for a scoped review, but it should be stated in the framing rather than left implicit, because the abstract itself promises cross-market evidence (W4). Length compliance cannot be assessed without a venue; at 6,804 declared body words the manuscript is plausible for a review essay and short for a full survey at several finance journals.

#### Originality

The paper claims four contributions: an enforcement taxonomy, the static/dynamic separation, a seven-dimension evaluation matrix, and six testable propositions. The matrix and the propositions are the more defensible innovations: Table 4 gives an operational evaluation vocabulary, and Table 6 states propositions that are independent enough to test. The static/dynamic separation is not itself novel — it is established in the dynamic no-arbitrage literature — but elevating it to an organizing axis and using it to explain why cross-paper comparisons fail is a genuine synthesis move. The taxonomy is the risk: Homescu (2011) is the paper's own closest antecedent and is credited with "the constraint taxonomy", yet no mapping is shown, so the boldest originality claim is the least evidenced (W1). The "no common benchmark" finding reproduces Ruf and Wang (2020); the paper properly hedges it in §4.5, but should label it as corroboration rather than as a finding of this review.

#### Significance

For a general finance readership the impact is agenda-setting rather than result-delivering: a shared vocabulary ("which guarantee"), a reporting standard, and six testable gaps. That is real value for a review venue and comparable to what the better surveys in this area achieve. It is not a result that changes practice on its own — Table 7 is a proposal, not a validated instrument, and the propositions are untested by design — and the paper is careful to say so. The remaining significance question is adoption: a model-risk team could use Table 4 immediately, which argues for framing at least part of the paper toward that readership rather than toward a general academic audience that will want more theoretical payoff. If the author can show the matrix in use on two or three surfaces, the significance case strengthens considerably even within a conceptual review.

#### Structural Coherence

The chain is traceable: ambiguity in §1.2, question in §1.3, framework in §2.6, findings in §4, implications in §5, answer in §6. The table progression (1 method families, 2 enforcement families, 3 dynamic evidence, 4 evaluation dimensions, 5 tensions, 6 propositions, 7 decision guide, 8 agenda) is well designed and reads as a deliberate funnel. The problems are local: the abstract's gap list, §4.7's counts, the proposition count, and the §1.5/§6 contribution lists (W4); the unheaded "Scope and excluded streams" paragraph interrupting the flow between §3.6 and §3.7; and the weight given to search protocol before the framework appears (W2). Nothing structural is broken; the ordering is sound and the argument is easy to find.

#### Title & Abstract

The title is accurate and descriptive at 15 words, and it signals both the review type and the three method families. Two reservations: "Neural" under-represents the generative and operator content (the neural/generative bucket includes VAEs, GANs, flows, neural SDEs, and an operator model), and the paper's own running head, "Which Guarantee?", is a stronger editorial hook than the descriptive title — consider making it the subtitle. The abstract is 207 words and well structured, reporting corpus size, date range, and query count, which is good practice. Three issues: the six-gap list does not match §5.5 and Table 8 (W4); the benchmark-gap sentence lists five dimensions while Table 4 defines seven, omitting fit and dynamic consistency, the latter being the paper's best distinction; and the final sentence is a disclaimer (W5). Align the list and close on the which-guarantee claim.

#### Conclusion

The conclusion answers the research question and does not over-infer; it restates the limits accurately. But its contribution list differs from §1.5's (W4), it adds no reader-facing "what to do next" beyond pointing at the agenda, and its final sentences are disclaimers, so the paper's last impression is defensive. A single closing sentence stating the actionable claim would fix the tone; this is a revision edit, not a structural problem.

### Questions for Authors

1. What exactly does the four-family enforcement taxonomy add over Homescu's (2011) constraint taxonomy? Could you provide a mapping table and state whether the new axis, the generative-method coverage, or the evidence map is the novel element?
2. Which venue and article type is the manuscript aimed at — a general journal's reviews-and-surveys track, a specialist review outlet, or an arXiv preprint — and how should the purposive, abstract-level corpus and the disclosure apparatus be read against that bar?
3. The abstract lists cross-market evidence as one of six gaps, but §5.5 and Table 8 replace it with head-to-head enforcement under distribution shift. Which is the manuscript's position, and why do the two lists differ?
4. Appendix D assigns 8 of 40 sources to "None/soft" and a further 3 to survey or evaluation categories outside the four families. What share of the corpus does each enforcement family cover, and how should the residual be classified for the taxonomy's coverage claim?

### Minor Issues

**Language and clarity**

- §3.3: "the currency distribution is at the 30% cap and does not trigger an advisory" — the 30% cap is an internal screening rule that the manuscript never defines; define it in §3.3 or remove the sentence.
- §3.1: "This is a structured literature review in `deep-research` full mode" — the tool-mode reference is meaningful to the pipeline, not to a journal reader; delete it or gloss it in one clause.
- §5.4: "A Devil's Advocate checkpoint returned REVISE with five Major issues" — reporting the manuscript's own adversarial review is a process artifact that will read oddly to an editor; move it to a disclosure note or remove it.
- §5.2: "It generates four testable propositions" — Table 6 lists six; write "four propositions from the taxonomy, plus two evaluation propositions" (see W4).
- Abstract: the benchmark-gap sentence lists five dimensions where Table 4 defines seven (fit and dynamic consistency are omitted); say "five of the seven" or list all seven.
- Front matter: remove the revision log (v1.2 → v4.0) and stage labels ("Stage 5", "Stage 4′") for submission; they belong in the project history, not the manuscript.

**Citation and reference format**

- APA 7 sentence case is applied inconsistently to article titles (for example, "Deep Smoothing of the Implied Volatility Surface" versus "Arbitrage-free SVI volatility surfaces"); normalize the reference list to sentence case for article titles.
- Cousin and Gueye (2021) is given an OpenAlex landing page (`https://openalex.org/W3184266889`) rather than the HAL record used elsewhere; cite the HAL handle.
- Confirm the publication status of the 2026 entries (Anagha; Xiong and Liu; Bajalica et al.), which are listed as forthcoming at the time of writing; give "in press" or the issue details rather than a bare year if the record is not final.

**Figures, tables, and layout**

- Table 3 versus Appendix D: Vuletić and Cont (2025) are marked "Static filter; dynamic validation limited" in Table 3 but "Y" in Appendix D's dynamic-test column; align the classification.
- Fengler (2009): §2.1 and §2.2 place him as constrained smoothing and present him under Nonparametric and Constrained Smoothing, but Table 1, Appendix B, and Appendix D classify him as parametric. Resolve before the method-family counts are treated as final (this may overlap the second seat's classification review).
- Table 1: the parametric "representative sources" include Fengler (2009), whose enforcement family is projection/repair; acceptable on the method-family axis, but it will confuse readers who meet him in §2.2 — add a footnote or move the example.
- Table 7: the non-ranking caveat appears in the caption and again in the text immediately before it; keep one.
- Appendix D: "None/soft" is used as a label alongside the four families without being defined as a residual category; rename the column or split it into "no enforcement" and "other" (see W3).
- Layout: the bold "Scope and excluded streams." paragraph sits between §3.6 and §3.7 with no heading; give it a heading or fold it into §3.7.
