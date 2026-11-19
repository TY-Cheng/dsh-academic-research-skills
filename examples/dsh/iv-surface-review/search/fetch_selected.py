#!/usr/bin/env python3
"""Fetch metadata + abstracts for the 40-source Phase 2 corpus.

The selection is recorded here (not inferred at runtime) so the corpus is
reproducible. OpenAlex is used for metadata and abstracts; the DOI endpoint
is tried first, with an exact-title search only for the one HAL record that
has no DOI.
"""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://api.openalex.org/works"
FIELDS = ",".join(
    [
        "id",
        "doi",
        "title",
        "publication_year",
        "authorships",
        "primary_location",
        "cited_by_count",
        "type",
        "is_retracted",
        "abstract_inverted_index",
    ]
)

# (doi or "", exact title, inclusion bucket)
SELECTED = [
    ("10.1080/14697688.2013.819986", "Arbitrage-free SVI volatility surfaces", "parametric"),
    ("10.1137/120900320", "Generalized Arbitrage-Free SVI Volatility Surfaces", "parametric"),
    ("10.1080/14697680802595585", "Arbitrage-free smoothing of the implied volatility surface", "parametric"),
    ("10.48550/arxiv.1107.1834", "Implied Volatility Surface: Construction Methodologies and Characteristics", "parametric"),
    ("10.2139/ssrn.3402942", "Deep Smoothing of the Implied Volatility Surface", "neural"),
    ("10.48550/arxiv.1810.03399", "Deep calibration of rough stochastic volatility models", "neural"),
    ("10.1609/aaai.v31i1.10505", "Gated Neural Networks for Option Pricing: Rationality by Design", "constraints"),
    ("10.21314/jcf.2020.390", "Neural Networks for Option Pricing and Hedging: A Literature Review", "constraints"),
    ("10.1016/j.ejor.2020.12.003", "Option valuation under no-arbitrage constraints with neural networks", "constraints"),
    ("10.1080/1350486x.2020.1846573", "Detecting and Repairing Arbitrage in Traded Option Prices", "constraints"),
    ("10.3390/risks7010016", "Pricing Options and Computing Implied Volatilities using Neural Networks", "constraints"),
    ("10.3905/jfds.2020.1.032", "PCA for Implied Volatility Surfaces", "nonparametric"),
    ("10.1137/21m1443546", "Arbitrage-Free Implied Volatility Surface Generation with Variational Autoencoders", "neural"),
    ("10.1080/14697688.2020.1817974", "Deep Learning Volatility", "neural"),
    ("10.1080/14697688.2022.2135454", "A two-step framework for arbitrage-free prediction of the implied volatility surface", "neural"),
    ("10.1080/1350486x.2025.2471317", "VolGAN: A Generative Model for Arbitrage-Free Implied Volatility Surfaces", "neural"),
    ("10.1080/1350486x.2023.2277960", "Simulation of Arbitrage-Free Implied Volatility Surfaces", "neural"),
    ("10.1080/1350486x.2023.2257217", "Arbitrage-Free Neural-SDE Market Models", "neural"),
    ("10.1002/fut.22302", "Multistep forecast of the implied volatility surface using deep learning", "neural"),
    ("10.1145/3447548.3467115", "Incorporating Prior Financial Domain Knowledge into Neural Networks for Implied Volatility Surface Prediction", "neural"),
    ("10.1142/s2705109925500051", "On Deep Calibration of (rough) Stochastic Volatility Models", "neural"),
    ("10.1145/3768292.3771252", "Arbitrage-Free Implied Volatility Surface Smoothing via Generative Adversarial Networks", "neural"),
    ("10.1145/3858063.3858741", "Latent Flow Matching for Arbitrage-Aware Implied Volatility Surface Generation", "neural"),
    ("10.48550/arxiv.2509.01743", "Controllable Generation of Implied Volatility Surfaces with Variational Autoencoders", "neural"),
    ("10.1145/3677052.3698601", "Whack-a-mole Online Learning: Physics-Informed Neural Network for Intraday Implied Volatility Surface", "neural"),
    ("10.1007/s00245-024-10184-9", "Neural Networks Can Detect Model-Free Static Arbitrage Strategies", "constraints"),
    ("10.1109/cifer67845.2026.11692406", "Observation-Anchored Arbitrage Repair for Sparse Implied Volatility Surface Completion", "constraints"),
    ("10.1016/j.jocs.2026.102818", "SABR-informed multitask Gaussian process: A synthetic-to-real framework for implied volatility surface construction", "nonparametric"),
    ("10.1016/j.ejor.2026.07.049", "Joint arbitrage-free smoothing of American call and put options surfaces", "nonparametric"),
    ("10.1080/14697688.2026.2637739", "The implied volatility surface (also) is path-dependent", "dynamics"),
    ("10.1137/24m1713107", "Volatility Parametrizations with Random Coefficients: Analytic Flexibility for Implied Volatility Surfaces", "parametric"),
    ("10.1137/20m1351060", "No Arbitrage SVI", "parametric"),
    ("10.1080/14697688.2022.2117076", "No arbitrage global parametrization for the eSSVI volatility surface", "parametric"),
    ("10.3390/math11092108", "The Application of Symbolic Regression on Identifying Implied Volatility Surface", "nonparametric"),
    ("10.48550/arxiv.2406.11520", "Operator Deep Smoothing for Implied Volatility", "neural"),
    ("10.2139/ssrn.4803161", "Gaussian Processes for Implied Volatility Estimation", "nonparametric"),
    ("10.48550/arxiv.2310.16703", "No-Arbitrage Deep Calibration for Volatility Smile and Skewness", "neural"),
    ("10.2139/ssrn.4623940", "Volatility Transformers: an optimal transport-inspired approach to arbitrage-free shaping of implied volatility surfaces", "neural"),
    ("", "Kriging for implied volatility surface", "nonparametric"),
    ("10.2139/ssrn.7577418", "Trainable Hard Constraints: Architectural Enforcement of Arbitrage-Free Implied Volatility Surfaces via Automatic Differentiation", "constraints"),
]


def reconstitute(index: dict | None) -> str:
    if not index:
        return ""
    positions: dict[int, str] = {}
    for word, places in index.items():
        for place in places:
            positions[place] = word
    return " ".join(positions[i] for i in sorted(positions))


def get(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=30) as response:
        return json.load(response)


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    records = []
    for doi, title, bucket in SELECTED:
        query_title = title
        if doi:
            url = f"{BASE}/doi:{urllib.parse.quote(doi, safe='')}?select={FIELDS}"
        else:
            url = (
                f"{BASE}?search={urllib.parse.quote(title)}&per-page=3"
                f"&select={FIELDS}"
            )
        try:
            payload = get(url)
            work = payload if doi else (payload.get("results") or [{}])[0]
        except Exception as exc:  # noqa: BLE001
            records.append(
                {
                    "doi": doi,
                    "title": query_title,
                    "bucket": bucket,
                    "error": str(exc),
                    "abstract": "",
                }
            )
            print(f"[error] {query_title}: {exc}")
            time.sleep(1.1)
            continue

        authors = [
            (a.get("author") or {}).get("display_name", "")
            for a in (work.get("authorships") or [])
        ]
        source = (work.get("primary_location") or {}).get("source") or {}
        records.append(
            {
                "doi": (work.get("doi") or doi).replace("https://doi.org/", ""),
                "title": work.get("title") or query_title,
                "year": work.get("publication_year"),
                "venue": source.get("display_name") or "",
                "authors": [a for a in authors if a],
                "cited_by_count": work.get("cited_by_count") or 0,
                "type": work.get("type") or "",
                "is_retracted": bool(work.get("is_retracted")),
                "openalex_id": work.get("id"),
                "bucket": bucket,
                "abstract": reconstitute(work.get("abstract_inverted_index")),
            }
        )
        print(
            f"[ok] {(work.get('publication_year') or '?')} "
            f"{work.get('title') or query_title} | abstract={len(records[-1]['abstract'])}"
        )
        time.sleep(1.1)

    (out_dir / "selected_sources.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    lines = [
        "# Selected Phase 2 corpus (40 sources)",
        "",
        "| # | Bucket | Year | Venue | DOI | Title | Abstract chars |",
        "|---:|---|---:|---|---|---|---:|",
    ]
    for index, record in enumerate(records, start=1):
        title = (record.get("title") or "").replace("|", "\\|")
        venue = (record.get("venue") or "").replace("|", "\\|")
        lines.append(
            f"| {index} | {record['bucket']} | {record.get('year') or ''} | "
            f"{venue} | `{record.get('doi') or ''}` | {title} | "
            f"{len(record.get('abstract') or '')} |"
        )
    (out_dir / "selected_sources.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print(f"selected={len(records)}")


if __name__ == "__main__":
    main()
