#!/usr/bin/env python3
"""Stage 5 formatter (fallback): Markdown -> LaTeX -> PDF.

Pandoc is not installed in this environment. ARS v3.24.4 says DOCX is produced
via Pandoc when available, otherwise the user gets instructions; this runner
therefore produces the PDF through LaTeX (ctex + xelatex, so the Chinese
abstract compiles) and leaves DOCX to the instructions in README.md. It is a
deterministic, structure-preserving conversion for e2e evidence, not a journal
typesetter. Run with the fork venv.
"""
from __future__ import annotations
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MD = ROOT / "paper-final.md"
TEX = ROOT / "paper-final.tex"
PDF = ROOT / "paper-final.pdf"

# ---------- shared parsing ----------
def strip_comments(s: str) -> str:
    return re.sub(r"<!--.*?-->", "", s, flags=re.S)

def blocks(md: str):
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            yield ("table", rows)
            continue
        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:].strip())
                i += 1
            yield ("list", items)
            continue
        if line.startswith("#"):
            m = re.match(r"^(#{1,4})\s+(.*)$", line)
            if m:
                yield ("h", len(m.group(1)), m.group(2).strip())
                i += 1
                continue
        if line.strip() == "---":
            yield ("rule",)
            i += 1
            continue
        para = [line.strip()]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if not nxt.strip() or nxt.startswith(("|", "- ", "#")) or nxt.strip() == "---":
                break
            para.append(nxt.strip())
            i += 1
        yield ("p", " ".join(para))

# ---------- LaTeX ----------
UNI = {
    "→": r"$\rightarrow$", "×": r"$\times$", "≥": r"$\geq$", "≤": r"$\leq$",
    "≈": r"$\approx$", "±": r"$\pm$", "§": r"\S ", "′": r"$'$",
}
def esc(s: str) -> str:
    s = s.replace("\\", "@@BS@@")
    for a, b in [("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"),
                 ("_", r"\_"), ("{", r"\{"), ("}", r"\}")]:
        s = s.replace(a, b)
    s = s.replace("~", r"\textasciitilde{}").replace("^", r"\textasciicircum{}")
    s = s.replace("@@BS@@", r"\textbackslash{}")
    return s

def inline(s: str) -> str:
    for i, (a, b) in enumerate(UNI.items()):
        s = s.replace(a, f"@@U{i}@@")
    s = esc(s)
    for i, (a, b) in enumerate(UNI.items()):
        s = s.replace(f"@@U{i}@@", b)
    s = re.sub(r"`([^`]+)`", r"\\texttt{\1}", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\\textit{\1}", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\\href{\2}{\1}", s)
    return s

WIDTHS = {
    2: ["0.30", "0.62"], 3: ["0.08", "0.45", "0.40"],
    4: ["0.06", "0.35", "0.18", "0.34"], 5: ["0.05", "0.28", "0.28", "0.18", "0.16"],
    6: ["0.04", "0.18", "0.18", "0.18", "0.18", "0.16"],
    7: ["0.04", "0.16", "0.12", "0.16", "0.10", "0.12", "0.10"],
}
def tex_table(rows: list[str]) -> str:
    cells = []
    for r in rows:
        r = r.strip().strip("|")
        cells.append([c.strip() for c in r.split("|")])
    if len(cells) < 2:
        return ""
    header = cells[0]
    data = [r for r in cells[2:]]  # skip separator
    n = len(header)
    if header and header[0].strip().strip("*").strip() == "ID" and n >= 10:
        # registry/evidence matrix: keep the wide source column and give the
        # trailing classification columns room, inside a 2.5pt tabcolsep
        base = [0.035, 0.145, 0.05, 0.075, 0.045, 0.075, 0.045, 0.035,
                0.035, 0.055, 0.06, 0.09, 0.07]
        if n == len(base):
            w = [f"{x:.4f}" for x in base]
        else:
            rest = (0.88 - 0.035) / (n - 1)
            w = ["0.035"] + [f"{rest:.4f}"] * (n - 1)
    elif n in WIDTHS:
        w = WIDTHS[n]
    else:
        # wide tables: keep the sum inside the text block instead of letting
        # n fixed columns overflow the page
        first = 0.18
        rest = (0.88 - first) / (n - 1)
        w = [f"{first:.4f}"] + [f"{rest:.4f}"] * (n - 1)
    spec = "".join(f"p{{{x}\\textwidth}}" for x in w)
    small = "\\scriptsize" if n >= 6 else ("\\small" if n == 5 else "")
    sep = "\\setlength{\\tabcolsep}{2.5pt}" if n >= 8 else ""
    out = [f"\\begingroup{small}{sep}", f"\\begin{{longtable}}{{@{{}}{spec}@{{}}}}", "\\toprule"]
    head_cells = [c.strip().strip("*").strip() for c in header]
    out.append(" & ".join(f"\\textbf{{{inline(c)}}}" for c in head_cells) + r" \\")
    out.append("\\midrule")
    out.append("\\endfirsthead")
    out.append("\\toprule")
    out.append(" & ".join(f"\\textbf{{{inline(c)}}}" for c in head_cells) + r" \\")
    out.append("\\midrule")
    out.append("\\endhead")
    for r in data:
        r = (r + [""] * n)[:n]
        out.append(" & ".join(inline(c) for c in r) + r" \\")
    out += ["\\bottomrule", "\\end{longtable}", "\\endgroup", ""]
    return "\n".join(out)

def build_tex(md: str) -> str:
    out = [
        r"\documentclass[11pt]{article}",
        r"\usepackage[UTF8]{ctex}",
        r"\usepackage[margin=1in]{geometry}",
        r"\usepackage{booktabs,longtable,array}",
        r"\setlength{\emergencystretch}{3em}",
        r"\usepackage{hyperref}",
        r"",
        r"\usepackage{microtype}",
        r"\setlength{\parindent}{0pt}",
        r"\setlength{\parskip}{6pt}",
        r"\renewcommand{\arraystretch}{1.12}",
        r"\begin{document}",
        "",
    ]
    first_h1 = True
    first_rule = True
    for b in blocks(md):
        kind = b[0]
        if kind == "h":
            level, text = b[1], b[2]
            if level == 1:
                if first_h1:
                    first_h1 = False
                    out.append(r"\begin{center}")
                    out.append(r"{\LARGE\bfseries " + inline(text) + r"}\\[1.2em]")
                    out.append(r"\end{center}")
                else:
                    out.append(r"\section*{" + inline(text) + "}")
            elif level == 2:
                out.append(r"\subsection*{" + inline(text) + "}")
            elif level == 3:
                out.append(r"\subsubsection*{" + inline(text) + "}")
            else:
                out.append(r"\paragraph{" + inline(text) + "}")
        elif kind == "p":
            out.append(inline(b[1]) + "\n")
        elif kind == "table":
            out.append(tex_table(b[1]))
        elif kind == "list":
            out.append(r"\begin{list}{}{\leftmargin=1.6em \itemindent=-1.6em \itemsep=0.25em}")
            for it in b[1]:
                out.append(r"\item " + inline(it))
            out.append(r"\end{list}")
        elif kind == "rule":
            if first_rule:
                first_rule = False
                out.append(r"\newpage")
            else:
                out.append(r"\par\medskip\hrule\medskip")
    out += [r"\end{document}", ""]
    return "\n".join(out)

def compile_pdf() -> tuple[bool, str]:
    for _ in range(2):
        p = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", TEX.name],
                           cwd=ROOT, text=True, capture_output=True)
        if p.returncode != 0:
            return False, (p.stdout or "")[-3000:] + "\n" + (p.stderr or "")[-1000:]
    return PDF.exists(), ""

def main() -> int:
    md = strip_comments(MD.read_text())
    # Greek kappa is absent from the text font; map it to math mode in the
    # LaTeX source only (the Markdown deliverable keeps the plain character).
    tex = build_tex(md).replace("κ", "$\\kappa$")
    TEX.write_text(tex)
    print("wrote", TEX.name)
    ok, err = compile_pdf()
    print("pdf", "ok" if ok else "FAILED")
    if not ok:
        print(err[:3000])
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
