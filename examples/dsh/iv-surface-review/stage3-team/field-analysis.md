# Field Analysis Report

**Manuscript:** Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches
**Source file:** `examples/dsh/iv-surface-review/stage5/paper-final.md`
**Phase:** 0 — field analysis and reviewer configuration
**Dispatch scope:** general finance / quantitative-finance review venue
**Target-binding status:** `criteria_binding_unavailable` — no author-confirmed #683 `ReviewTargetContext` or Target Criteria Brief was supplied with the dispatch; nothing in this report binds a venue, track, or article type.

## Paper Basic Information

- **Title**: Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches
- **Abstract length**: 207 words (English abstract); the paper is bilingual and also carries a Chinese-language abstract.
- **Full text length**: 6,804 body words as declared by the author (excluding abstract, declarations, references, and appendices); about 11,000 words in the Markdown file including tables and appendices.
- **Number of references**: 40 (30 peer-reviewed articles or conference papers and 10 preprints; 39 with a resolving DOI, one HAL record without a DOI).
- **Article type**: structured literature review (declared; APA 7.0; JEL G13, C45, C63).
- **Language**: English, with a Chinese abstract.
- **Declared target (manuscript front matter)**: "General academic journal / arXiv-style preprint (no specific venue)". This is a manuscript-level declaration, not author-confirmed `ReviewTargetContext` metadata, and it is not treated as a binding target here.

## Field Analysis

| Dimension | Analysis Result |
|-----------|----------------|
| Primary Discipline | Quantitative finance — derivatives pricing and volatility modelling. The object of study is the implied volatility surface; the organizing problem is enforcement of static and dynamic no-arbitrage in surface construction. The declared JEL codes G13 (contingent pricing), C45 (neural networks), and C63 (computational techniques) match this reading. |
| Secondary Disciplines | (1) Statistics and econometrics — nonparametric smoothing, Gaussian processes and kriging, model evaluation and benchmarking; (2) machine learning — neural networks, generative models (VAE/GAN, flows), operator learning, calibration surrogates; (3) mathematical finance and stochastic analysis — no-arbitrage theory, martingale consistency, SVI/SSVI/eSSVI parameterizations. |
| Research Paradigm | Literature review / evidence synthesis — a structured narrative review with an interpretive-conceptual component (four-family enforcement taxonomy, seven-dimension evaluation matrix, testable propositions). No empirical estimation and no meta-analysis. |
| Methodology Type | Structured (narrative) literature review: 24 OpenAlex full-text queries, a frozen 40-source corpus, metadata/abstract-level content coding, source-verification levels VI/VII, narrative thematic synthesis, and a cross-paper tension inventory. Scoping-review-style; explicitly not PRISMA-compliant; no full-text screening. |
| Target Journal Tier | `criteria_binding_unavailable` — no author-confirmed #683 target metadata was supplied. Field-general observation only: this is a corpus-scoped interpretive review with no new empirics, self-positioned for a general finance/quantitative-finance review venue and explicitly not a top-three empirical journal (§1.5). That profile is consistent with a field/general finance journal, a review track, or an arXiv-style preprint. No quartile, track, or venue-alignment claim is bound. |
| Paper Maturity | Pre-submission. Complete IMRaD-style structure plus a bilingual abstract, five appendices (A–E), an APA 7.0 reference list with DOIs, full declarations (data availability, ethics, CRediT, conflict of interest, funding, AI use), a revision log v1.2 → v4.0, and polished English. Basis: structural completeness, citation formatting, and language polish. |

## Recommended Target Journals (Top 3)

**Advisory only, under `criteria_binding_unavailable`.** The field analyst is not a target resolver: these are field-general candidates, not a venue-alignment determination, and they do not configure any reviewer card. Each rationale is grounded in the paper's own reference list or declared readership, not in journal-metric memory. An author-confirmed #683 target supersedes this list entirely.

1. **Quantitative Finance** — the corpus's centre of gravity: 6 of the 40 sources appear there (Fengler, 2009; Gatheral & Jacquier, 2014; Horvath et al., 2021; Mingone, 2022; Zhang et al., 2022; Andrès et al., 2026), so its readership already knows the static-arbitrage literature on which the review's strongest finding rests.
2. **Journal of Computational Finance** — closest article-type precedent in the corpus: Ruf and Wang's (2020) literature review of neural option pricing and hedging is placed there by the paper's own corpus; the venue's computational-construction and calibration remit matches the 45% neural/generative share, and its readership overlaps the quant-developer/model-validation audience the paper names.
3. **Journal of Financial Data Science** — practitioner-facing data-science venue that published Avellaneda et al. (2020); it matches the paper's stated primary reader (model-risk/model-validation analyst or benchmark designer) and the applied material in §5.3 and Table 7 better than a purely mathematical outlet would.

Alternative field-general outlet: **Applied Mathematical Finance** (4 of the 40 corpus sources), if the author reframes the contribution toward arbitrage theory rather than review and evaluation practice.

## Reviewer Configuration Cards

### Reviewer Configuration Card #1

**Role**: EIC
**Display role**: Journal-Fit Reviewer
**Serialized source ID**: EIC
**Identity Description**: Associate Editor of a general quantitative-finance journal with a reviews-and-surveys remit, with a derivatives-pricing research background and 15 years of editorial experience across mathematical and computational finance; has handled both commissioned surveys and unsolicited review submissions and routinely decides whether a literature synthesis clears a field journal's originality bar.
**Review Focus**:
  1. Originality and significance: whether the enforcement taxonomy (§2.6) is a genuine advance over Homescu (2011) and Ruf and Wang (2020) or a relabeling of known distinctions, and whether the seven-dimension matrix (Table 4) changes how a reader classifies or evaluates methods.
  2. Readership fit and framing: whether the paper is pitched at general finance readers through the "which guarantee?" hook or only at implied-volatility specialists; whether the balance between SVI/SSVI parameter detail (§2.1) and synthesis is right for the venue, and whether a non-specialist reaches the contribution.
  3. Article-type coherence and proportionality: whether the pervasive scoping language ("corpus-scoped", "no ranking", "not PRISMA", the six limitations of §5.4, and §5.5's "what this review can and cannot support") builds credibility or pre-empts the contribution, and whether this is a review article or a research article in disguise.
**Will particularly care about**: Whether the paper passes the "so what?" test for a general finance readership — a map, a matrix, and a research agenda are a contribution only if they change how readers classify or evaluate construction methods; disclaimers must not stand in for the contribution.
**Possible blind spots**: May not verify the technical accuracy of the no-arbitrage claims, the completeness of the literature, or the soundness of the review methodology; R2 and R1 compensate.

### Reviewer Configuration Card #2

**Role**: Peer Reviewer 1
**Display role**: Peer Reviewer 1 — Methodology
**Serialized source ID**: R1
**Identity Description**: Professor of evidence synthesis and information science specializing in systematic-review methodology — search-strategy reproducibility, screening and selection bias, and evidence-appraisal grading; methods editor for a review journal, with auditing experience on PRISMA-style and scoping-review protocols in finance and economics.
**Review Focus**:
  1. Search and selection reproducibility: whether the 24 OpenAlex queries, the deduplication, and the 351 → 40 flow (§3.2–3.3, Appendix C, Appendix E) are documented well enough to re-run, and whether a single primary database — with Semantic Scholar returning HTTP 429 for 10 of 10 requests — supports the corpus claims.
  2. Screening and evidence bias: whether abstract-only assessment (0 full texts), 10 of 40 preprints, four partial abstracts, and one title-level record (§3.4) are adequately disclosed; whether the VI/VII evidence grading bounds the findings, and whether static-arbitrage query vocabulary biases the corpus (§3.2, §4.4).
  3. Synthesis validity: whether the "three-source convergence / silence under two" rule (§3.5), the seven cross-paper tension assessments (Table 5), and the narrative synthesis (no meta-analysis) are defensible, and whether the interpretive taxonomy and matrix are consistently presented as proposals rather than findings.
**Will particularly care about**: Whether the corpus and the evidence claims are reproducible and whether the review's confidence tracks its abstract-level evidence — the central methodological risk is a structured narrative review using systematic-review rhetoric while disclaiming systematic-review procedure.
**Possible blind spots**: May assess review procedure in isolation from whether the synthesis is substantively right for the field, and may under-weight the technical accuracy of the taxonomy; R2 and the synthesizer compensate.

### Reviewer Configuration Card #3

**Role**: Peer Reviewer 2
**Display role**: Peer Reviewer 2 — Domain
**Serialized source ID**: R2
**Identity Description**: Senior professor of mathematical finance specializing in implied-volatility-surface construction and arbitrage-free parameterizations (SVI/SSVI/eSSVI and constrained smoothing), with publications in Quantitative Finance and the SIAM Journal on Financial Mathematics; teaches calibration and model validation and referees for the main derivatives and financial-mathematics journals.
**Review Focus**:
  1. Literature completeness and attribution accuracy: whether the canonical static- and dynamic-arbitrage strands are represented and correctly characterized, whether missing seminal work (for example, dynamic-arbitrage and no-arbitrage-density streams, and benchmark studies beyond SPX) would alter the map, and whether the attributions in §2 and the reference list are accurate.
  2. Taxonomy and classification validity: whether "where the constraint enters the pipeline" survives hybrid cases (penalty-plus-projection training, gated networks validated only in simulation, repair steps that are projections), and whether the source-level mapping in Appendix D and the method-family mix in Table 1 are consistent with the prose in §2.1–2.2.
  3. Contribution to the field: whether the static/dynamic distinction is framed with technical precision, whether "no shared benchmark identified in the retrieved abstracts" (§4.5) is correctly scoped, and whether the six gaps (§5.5) are the field's real gaps rather than artifacts of the corpus.
**Will particularly care about**: Whether "arbitrage-free" is used with technical precision throughout and whether claims about method families — SVI flexibility, hard architectural constraints, and the static-versus-dynamic sufficiency relation — are faithful to the mathematics; a domain reader will notice a mischaracterized no-arbitrage condition immediately.
**Possible blind spots**: May concentrate on missing citations and technical nuance while under-weighting the review's methodological and editorial quality (R1 and EIC compensate), and may not assess operational usefulness (R3).

### Reviewer Configuration Card #4

**Role**: Peer Reviewer 3
**Display role**: Peer Reviewer 3 — Cross-disciplinary/Practical
**Serialized source ID**: R3
**Identity Description**: Head of quantitative model validation and model risk at a systemically important bank, formerly a supervisory reviewer of derivatives pricing models; specializes in independent benchmarking, ongoing monitoring, and the evidentiary standard for "arbitrage-free" claims in pricing and risk systems; has worked with benchmark and data vendors on surface construction for sparse and stressed markets.
**Review Focus**:
  1. Operationalizability of the evaluation matrix: whether a validation team could implement the seven dimensions (Table 4) with actual tolerances — which dimensions (dynamic consistency, interpretability, wing behaviour) lack an accepted measurement protocol, and what a "minimum reporting standard" needs beyond a list of dimensions.
  2. Guarantee-to-evidence mapping: whether the four enforcement families imply specific validation evidence (construction: admissible-region documentation and calibration diagnostics; penalty: post-training violation audits; projection/repair: repair-rule sensitivity and observation-fidelity tests; generation plus filtering: independent static and dynamic tests), and where the paper's evidence map falls short of that standard.
  3. Practical and regulatory claims: whether the statement that a missing shared benchmark "may warrant supervisory attention" (§5.3) is supportable; whether the SPX/US-equity-index concentration, sparse wings, and stressed periods are treated adequately for a practitioner readership; and whether Table 7 could be misread as a validated selection rule despite its caveats.
**Will particularly care about**: Whether a practitioner can act on the paper — the taxonomy is useful only if it changes validation test design and reporting; because the paper concedes that no evaluation dimension has a shared metric, it should name the first concrete step toward one rather than only proposing the matrix.
**Possible blind spots**: May over-weight operational feasibility and under-value the interpretive/theoretical contribution, and may not audit the review's search methodology or the literature's technical accuracy; R1 and R2 compensate.

**Panel note.** These four cards are the complete configuration set. The fifth execution seat is the fixed Devil's Advocate, which receives no configuration card and is not dynamically configured.

## Review Strategy Recommendations

- **Apply the declared article type as the yardstick.** The paper is a structured narrative review with interpretive contributions (taxonomy, matrix, propositions), not a systematic review or an empirical benchmark study. Reviewers should judge faithfulness, reproducibility, and usefulness within that type; demanding a full PRISMA screen or new empirical benchmarks would be a request for a different paper. This follows the role prompt's literature-review edge case for R1's configuration (search strategy, inclusion/exclusion, bias assessment), with domain technical accuracy carried by R2.
- **Verify the hedging; do not reward it.** The manuscript pre-discloses its limitations (§5.4), declines PRISMA status (§3.1), repeatedly disclaims ranking, and itself reports a prior Devil's Advocate checkpoint that returned REVISE with five Major issues. Reviewers should check that the disclosures are accurate and sufficient, and the synthesizer should test whether the hedges actually resolve the disclosed issues rather than counting their re-discovery as new findings.
- **Separate in-corpus defects from corpus-expansion requests.** Because the corpus is frozen and abstract-level, most "missing literature" findings are legitimate but out of scope. The synthesizer should distinguish (a) accuracy and completeness defects within the 40-source corpus, which are actionable, from (b) corpus-expansion or full-text requests, which are author-owned scope decisions.
- **Expect complementary angles, with one real tension.** R1 tests the review method, R2 the literature and taxonomy, R3 the operational use, and the Journal-Fit Reviewer the contribution and readership; these are complementary rather than duplicative. The tension to manage is between R1's likely push for systematic-review rigor and the paper's declared (and defensible) structured-review scope: if that tension is not adjudicated first, the panel may manufacture severity for a scope the paper never claimed.
- **Schedule cross-section consistency checks.** The paper's density — six gap statements, eight tables, five appendices, and abstract ⇄ §4 ⇄ §5.5 cross-references — makes consistency a concrete review task; check targets include the abstract's six-gap list against the §5.5 agenda and Table 8, Table 1 against Appendix D classifications, Table 2 against Appendix D enforcement families, and §4.7's resolved/unresolved/not-applicable counts against Table 5's statuses. These are verification targets, not presumptions of error.
- **Carry the binding disclosure through the panel.** No author-confirmed #683 target was supplied, so the Journal-Fit Reviewer card is field-general by construction; every seat should disclose `criteria_binding_unavailable` and make no venue-alignment claim. If the orchestrating layer holds an author-confirmed target, it should replace this field-general configuration, and the four cards should be re-shown for author confirmation before any Phase 1 seat is dispatched.
