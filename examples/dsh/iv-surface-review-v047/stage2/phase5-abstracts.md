## Abstract

### English Abstract

Equity-index option markets quote hundreds of strikes and maturities daily, and the implied volatility surface that risk systems consume is economically coherent only if it excludes arbitrage on a single date and across dates. This review characterises, without ranking, how four families of construction methods enforce those constraints: parametric construction, which restricts the parameter domain; penalty-augmented objectives; projection-repair, which maps a fitted surface onto an admissible set; and generation-filtering, which screens candidate surfaces. The corpus is 41 sources — 36 published in 2015–2026 and 5 seminal precursors — of which 29 are peer-reviewed and 11 are preprints, coded on eight fields and read at abstract level; no systematic-review compliance or method ranking is claimed. Seventeen sources assert their guarantee at proof level, 16 report a numerical test, and 8 assert admissibility with neither. In all 41 rows the certified object is a single date's surface, and no source enforces or tests dynamic no-arbitrage, including none of the 31 construction rows. Proof-level and test-level evidence come from almost disjoint sets, and no source states data, metric and tolerance together, so no two rows are directly comparable. Read this way, the four families are not competing answers but four enforcement loci licensing four kinds of evidence, and the apparent disagreement between them is a division of evidential labour that leaves the dynamic condition visible as a void.

**Keywords:** implied volatility surfaces; no-arbitrage constraints; static arbitrage; dynamic arbitrage; model-free constraints; structured literature review

---

### Chinese Abstract

股指期权市场每一交易日都报出数百个行权价与到期日的组合，而风险系统实际消费的不是报价，是拟合后的隐含波动率曲面；该曲面只有在单日层面与跨日层面均不含套利时才具备经济一致性。本文对这四类构造方法如何承载上述约束作刻画性（而非排序性）梳理：参数化构造（以限制参数域实现）、惩罚增强型目标、投影修复（把拟合曲面映射到可行集），以及生成—筛选（对候选曲面进行检验）。语料为41篇文献，其中36篇发表于2015–2026年、5篇为有意纳入的早期奠基性研究，含29篇同行评审论文与11篇预印本；按八个字段编码、在摘要层面阅读，不主张系统性综述合规性，也不给出方法排序。17篇以证明层级主张其保证，16篇报告数值检验，另8篇既无证明也无检验却断言可行性。41篇所认证的对象全部是单一交易日的曲面；没有任何一篇强制或检验动态无套利，31篇构造类文献无一例外。证明层级与检验层级的证据来自几乎不相交的集合，且没有任何一篇同时给出数据、度量与容差，因此任意两篇之间都不能直接比较。据此解读，四类方法不是相互竞争的答案，而是四个执行位点，各自许可一类证据；表面上的分歧实为证据分工，动态条件则被显现为一处空缺。

**Keywords:** 隐含波动率曲面；无套利约束；静态套利；动态套利；模型无关约束；结构化文献综述

### Abstract Quality Report

| Metric | English | Chinese |
|---|---|---|
| Word count | 225 words (Standard regime 150–250) | 425 CJK characters (Standard regime 300–500) |
| Components covered | 5 / 5 — Background (surface admissibility), Purpose (characterise, not rank, four families), Method (41-source corpus, eight-field coding, abstract-level read), Findings (17 / 16 / 8 evidence split; 0 of 41 dynamic; no direct comparability), Implications (four loci, evidential division of labour, dynamic void) | 5 / 5 — same five components in the same order, with the same counts and the same hedges |
| Keywords | 6 — implied volatility surfaces; no-arbitrage constraints; static arbitrage; dynamic arbitrage; model-free constraints; structured literature review | 6 — 隐含波动率曲面；无套利约束；静态套利；动态套利；模型无关约束；结构化文献综述 |
| Independence check | Composed from the manuscript's own findings; contains no citation, no source name, and no table reference | Composed independently for Chinese rhetorical conventions (topic–comment opening, four-character parallelism in the closing clause), then aligned to the English structure; not a sentence-by-sentence translation — e.g. "generation-filtering" rendered as 生成—筛选 with the screening step named explicitly, and "certified object" as 所认证的对象 |
| Hedge consistency | Corpus-scoped absence only ("no source in the corpus"); no field-wide absence claim, so the #548 bounded-search qualifier of §6.2 is not restated | Same scope: 没有任何一篇 (no single paper), never 文献中没有 (nothing in the literature) |
| Acronyms / terms | No acronym used; "implied volatility surface" spelled out | No Latin acronym used; 隐含波动率曲面 spelled out at first mention |
| Language pair | L2 English — matches the requested pair | L1 Simplified Chinese — `zh-Hans` is not a registered token in `shared/output_language_pair.md` (registry carries only `zh-tw-en`); recorded as a visible registry mismatch (Phase 0 finding V1), not silently normalised to Traditional Chinese |

Two notes for the pipeline record. First, the abstracts describe the paper's own corpus-scoped findings; they make no claim about the literature at large, no venue-alignment claim, and no method ranking, consistent with `criteria_binding_unavailable`. Second, both abstracts name the four families in the same order as §2, so a reader who reads only the abstract can map each family to its section.
