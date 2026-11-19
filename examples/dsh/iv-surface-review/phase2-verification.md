# Phase 2 — Source Verification

**Corpus:** 40 sources. **Date:** 2026-11-19 (Asia/Singapore). **Mode:** `deep-research` full, Phase 2 source-verification pass.

## 1. Overall Assessment

- **References verified:** 40/40 records resolve to an OpenAlex work; 39/40 have a DOI; 1 (Cousin & Gueye, 2021) is a HAL record with no DOI.
- **Peer review:** 30/40 (75.0%) peer-reviewed; 10/40 (25.0%) preprints (SSRN, arXiv, HAL).
- **Fabrication/retraction:** 0 fabricated references found; OpenAlex `is_retracted` is false for all 40. This is not an independent retraction-database check.
- **Predatory journals:** 0 alerts. SSRN, arXiv, and HAL are preprint servers, not journals; the 10 preprints are flagged as not peer-reviewed.
- **Abstract coverage:** 35 full abstracts, 4 partial publisher/web snippets, 1 unavailable (Horvath et al., 2021).
- **Evidence levels:** 0 Level I–IV studies; 38 Level VI single studies; 2 Level VII narrative reviews/surveys. This is a methods literature, not a clinical evidence base; the levels describe design, not quality.
- **Verdict:** **conditional pass with flags.** The corpus meets the bibliography's size, peer-review, and currency thresholds. Preprints and the one abstract-unavailable record must be handled with the flags below.

## 2. Verification Method

1. **OpenAlex DOI resolution (all 40):** each record was retrieved through the OpenAlex DOI endpoint (or, for the HAL record, a title search). This confirms the record exists and matches the title/year metadata; it does not confirm the paper's claims.
2. **Crossref cross-check (10 records with missing/partial abstracts):** 9 requests succeeded (4 abstracts recovered; 5 empty), 1 returned HTTP 429. Crossref abstracts are publisher-deposited and may be absent.
3. **Semantic Scholar (10 records):** all 10 requests returned HTTP 429 (unauthenticated rate limit). No S2 title/DOI score or abstract was available.
4. **arXiv/SSRN/publisher spot checks:** arXiv abstract for Ruf & Wang (2020); publisher/web snippets for Cao et al. (2020), Neufeld & Sester (2024), Zhuang & Wu (2026), and Yao et al. (2026).
5. **No full-text appraisal, no independent author/COI audit, no Web of Science/Scopus, no Cabells/predatory-journal database.**

## 3. Source Quality Matrix

| # | Source | Level | Venue | Author | Method | Currency | COI | Overall | Basis |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Gatheral & Jacquier (2014) | VI | Peer-reviewed | Pass* | Pass* | Warn (seminal) | n/a | Verified | OpenAlex DOI; abstract |
| 2 | Guo et al. (2016) | VI | Peer-reviewed | Pass* | Pass* | Warn (older) | n/a | Verified | OpenAlex DOI; abstract |
| 3 | Fengler (2009) | VI | Peer-reviewed | Pass* | Pass* | Warn (seminal) | n/a | Verified | OpenAlex DOI; abstract |
| 4 | Homescu (2011) | VII | Preprint | Pass* | Warn (narrative/preprint) | Warn (seminal) | n/a | Plausible (preprint) | OpenAlex DOI; abstract |
| 5 | Ackerer et al. (2019) | VI | Preprint | Pass* | Warn (preprint) | Warn (older) | n/a | Plausible (preprint) | OpenAlex DOI; abstract |
| 6 | Bayer & Stemper (2018) | VI | Preprint | Pass* | Warn (preprint) | Warn (older) | n/a | Plausible (preprint) | OpenAlex DOI; abstract |
| 7 | Yang et al. (2017) | VI | Peer-reviewed | Pass* | Pass* | Warn (older) | n/a | Verified | OpenAlex DOI; abstract |
| 8 | Ruf & Wang (2020) | VII | Peer-reviewed | Pass* | Warn (narrative) | Warn (older) | n/a | Verified | OpenAlex DOI; arXiv abstract |
| 9 | Cao et al. (2020) | VI | Peer-reviewed | Pass* | Pass* | Warn (older) | n/a | Verified | OpenAlex DOI; web snippet |
| 10 | Cohen et al. (2020) | VI | Peer-reviewed | Pass* | Pass* | Warn (older) | n/a | Verified | OpenAlex DOI; abstract |
| 11 | Liu et al. (2019) | VI | Peer-reviewed | Pass* | Pass* | Warn (older) | n/a | Verified | OpenAlex DOI; abstract |
| 12 | Avellaneda et al. (2020) | VI | Peer-reviewed | Pass* | Pass* | Warn (older) | n/a | Verified | OpenAlex DOI; abstract |
| 13 | Ning et al. (2023) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 14 | Horvath et al. (2021) | VI | Peer-reviewed | Pass* | Unassessed | Pass | n/a | Verified (metadata only) | OpenAlex DOI; abstract missing |
| 15 | Zhang et al. (2022) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 16 | Vuletić & Cont (2025) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 17 | Cont & Vuletić (2023) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 18 | Cohen et al. (2023) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 19 | Medvedev & Wang (2021) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 20 | Zheng et al. (2021) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 21 | Bayer et al. (2025) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 22 | Ginart Belmonte & Cole (2025) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 23 | Bajalica et al. (2026) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 24 | Wang et al. (2025) | VI | Preprint | Pass* | Warn (preprint) | Pass | n/a | Plausible (preprint) | OpenAlex DOI; abstract |
| 25 | Hoshisashi et al. (2024) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 26 | Neufeld & Sester (2024) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; zbMATH summary |
| 27 | Xiong & Liu (2026) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 28 | Zhuang & Wu (2026) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; publisher snippet |
| 29 | Yao et al. (2026) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; IDEAS abstract |
| 30 | Andrès et al. (2026) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 31 | Zaugg et al. (2025) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 32 | Martini & Mingone (2022) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 33 | Mingone (2022) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 34 | Luo & Yu (2023) | VI | Peer-reviewed | Pass* | Pass* | Pass | n/a | Verified | OpenAlex DOI; abstract |
| 35 | Wiedemann et al. (2024) | VI | Preprint | Pass* | Warn (preprint) | Pass | n/a | Plausible (preprint) | OpenAlex DOI; abstract |
| 36 | Appana et al. (2024) | VI | Preprint | Pass* | Warn (preprint) | Pass | n/a | Plausible (preprint) | OpenAlex DOI; abstract |
| 37 | Hoshisashi et al. (2023) | VI | Preprint | Pass* | Warn (preprint) | Pass | n/a | Plausible (preprint) | OpenAlex DOI; abstract |
| 38 | Zetocha (2023) | VI | Preprint | Pass* | Warn (preprint) | Pass | n/a | Plausible (preprint) | OpenAlex DOI; abstract |
| 39 | Cousin & Gueye (2021) | VI | Preprint | Pass* | Warn (preprint) | Pass | n/a | Plausible (no DOI) | OpenAlex title; HAL |
| 40 | Anagha (2026) | VI | Preprint | Pass* | Warn (preprint) | Pass | n/a | Plausible (preprint) | OpenAlex DOI; abstract |

`Pass*` = metadata-level check only; author identity, affiliation, and COI were not independently audited. `n/a` = no COI statement was available in the retrieved metadata; this is not a finding of no conflict.

## 4. Flagged Sources

### 4.1 Preprints (not peer-reviewed)

| # | Source | Server | Handling |
|---|---|---|---|
| 4 | Homescu (2011) | arXiv | Use only as recent-method evidence; do not use as sole support for a central claim. |
| 5 | Ackerer et al. (2019) | SSRN | Use only as recent-method evidence; do not use as sole support for a central claim. |
| 6 | Bayer & Stemper (2018) | arXiv | Use only as recent-method evidence; do not use as sole support for a central claim. |
| 24 | Wang et al. (2025) | arXiv | Use only as recent-method evidence; do not use as sole support for a central claim. |
| 35 | Wiedemann et al. (2024) | arXiv | Use only as recent-method evidence; do not use as sole support for a central claim. |
| 36 | Appana et al. (2024) | SSRN | Use only as recent-method evidence; do not use as sole support for a central claim. |
| 37 | Hoshisashi et al. (2023) | arXiv | Use only as recent-method evidence; do not use as sole support for a central claim. |
| 38 | Zetocha (2023) | SSRN | Use only as recent-method evidence; do not use as sole support for a central claim. |
| 39 | Cousin & Gueye (2021) | HAL | Use only as recent-method evidence; do not use as sole support for a central claim. |
| 40 | Anagha (2026) | SSRN | Use only as recent-method evidence; do not use as sole support for a central claim. |

### 4.2 Abstract unavailable or partial

| # | Source | Status | Handling |
|---|---|---|---|
| 14 | Horvath, Muguruza & Tomas (2021) | Abstract unavailable; arXiv 1909.11716 is a different paper (“Optimal Transport to a Variety”) | Title-level only; do not attribute findings. |
| 9 | Cao, Liu & Zhai (2020) | Partial web snippet | Paraphrase only what the snippet states; no method/finding beyond it. |
| 26 | Neufeld & Sester (2024) | zbMATH summary | Treat as abstract-level; verify claims against the published article if used centrally. |
| 28 | Zhuang & Wu (2026) | Publisher snippet | Abstract-level only. |
| 29 | Yao, Cui & Pan (2026) | IDEAS abstract | Abstract-level only; note the 2027 issue date. |

### 4.3 Other flags

- **#39 Cousin & Gueye (2021):** HAL record, no DOI; OpenAlex title match only. Overall: plausible, not DOI-verified.
- **#29 Yao, Cui & Pan:** DOI is 2026 online; the EJOR issue is 2027, so the citation year is the online year.
- **#4 Homescu (2011) and #37 Hoshisashi et al. (2023):** OpenAlex venue field says “RePEc” (an aggregator); the records are arXiv preprints. The bibliography corrects the venue to arXiv.
- **#40 Anagha (2026):** proof-of-concept preprint; not peer-reviewed; use with caution.
- **#14 Horvath et al.:** DOI resolves, but no abstract was retrieved; do not infer the paper's claims from its title.

## 5. Predatory Journal Alerts

None. The peer-reviewed venues are established journals/conferences (SIAM Journal on Financial Mathematics, Quantitative Finance, Applied Mathematical Finance, European Journal of Operational Research, Journal of Computational Finance, Journal of Financial Data Science, Journal of Futures Markets, Journal of FinTech, Risks, Mathematics, AAAI, KDD, ICAIF, IEEE CIFEr). SSRN/arXiv/HAL are preprint servers, not predatory journals; they are flagged for peer-review status, not venue legitimacy. No Cabells or similar database was consulted, so this is a metadata-level check, not a guarantee.

## 6. COI Disclosures

No author COI statements were available in the retrieved metadata. No funding/COI audit was performed. This is a **not assessed** item, not a clean bill of health.

## 7. Verification Limitations

- Semantic Scholar was rate-limited (HTTP 429) for all 10 attempts; the Tier-0 S2 title/DOI check could not be run. DOI resolution (Tier 1) was run for 39/40; #39 has no DOI.
- Crossref returned one 429 and five empty abstracts; publisher metadata is incomplete.
- No full text was read; method weaknesses are abstract-level and reader-inferred.
- No independent retraction check beyond OpenAlex `is_retracted`; no Cabells/predatory check; no author/COI audit.
- No double screening, no formal risk-of-bias tool, no meta-analysis; 10/40 are preprints.
- The corpus is SPX/US-equity-index heavy; cross-market generalization is not established.

## 8. Recommendation

**Proceed to Phase 3 with flags.** Use the 30 peer-reviewed sources as the core evidence base. Use the 10 preprints only for recent-method coverage and label them as preprints in the synthesis. Treat #14 as title-level only and #9/#26/#28/#29 as abstract-level. Do not rank methods on a single metric or claim a PRISMA-compliant systematic review. Disclose the S2/Crossref rate limits and the absence of full-text appraisal in the final report's limitations.

## 9. Verification Log (selected)

```text
OpenAlex DOI endpoint: 40/40 records resolved (39 DOI + 1 title/HAL)
Crossref: 10 requests -> 4 abstracts, 5 empty, 1 HTTP 429
Semantic Scholar: 10 requests -> 10 HTTP 429
arXiv: Ruf & Wang abstract fetched; Horvath et al. arXiv ID mismatch
Web/publisher: Cao et al., Neufeld & Sester, Zhuang & Wu, Yao et al. snippets
OpenAlex is_retracted: false for all 40
```
