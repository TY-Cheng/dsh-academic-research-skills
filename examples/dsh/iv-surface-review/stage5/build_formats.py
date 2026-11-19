#!/usr/bin/env python3
"""Stage 5 fallback formatter: Markdown -> LaTeX/PDF + DOCX.

Pandoc is not installed in this environment; this is a deterministic,
structure-preserving fallback for the e2e evidence. It is not a journal
typesetter. The LaTeX output uses ctex + xelatex so the Chinese abstract
compiles. Run with the bundled Python (python-docx present).
"""
from __future__ import annotations
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MD = ROOT / "paper-final.md"
TEX = ROOT / "paper-final.tex"
PDF = ROOT / "paper-final.pdf"
DOCX = ROOT / "paper-final.docx"

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
    w = WIDTHS.get(n, ["0.14"] * n)
    spec = "".join(f"p{{{x}\\textwidth}}" for x in w)
    small = "\\scriptsize" if n >= 6 else ("\\small" if n == 5 else "")
    out = [f"\\begingroup{small}", f"\\begin{{longtable}}{{@{{}}{spec}@{{}}}}", "\\toprule"]
    out.append(" & ".join(f"\\textbf{{{inline(c)}}}" for c in header) + r" \\")
    out.append("\\midrule")
    out.append("\\endfirsthead")
    out.append("\\toprule")
    out.append(" & ".join(f"\\textbf{{{inline(c)}}}" for c in header) + r" \\")
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

# ---------- DOCX ----------
def add_runs(par, text: str):
    # split **bold** and *italic*; strip backticks
    text = text.replace("`", "")
    tokens = re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", text)
    for tok in tokens:
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**") and len(tok) > 4:
            r = par.add_run(tok[2:-2]); r.bold = True
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            r = par.add_run(tok[1:-1]); r.italic = True
        else:
            par.add_run(tok)

def build_docx(md: str) -> None:
    from docx import Document
    from docx.shared import Pt, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    doc = Document()
    sec = doc.sections[0]
    sec.left_margin = sec.right_margin = Inches(1)
    sec.top_margin = sec.bottom_margin = Inches(1)
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(11)
    first_h1 = True
    first_rule = True
    for b in blocks(md):
        kind = b[0]
        if kind == "h":
            level, text = b[1], b[2]
            if level == 1 and first_h1:
                first_h1 = False
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(text); r.bold = True; r.font.size = Pt(18)
            else:
                doc.add_heading(text, level=max(1, level - 1))
        elif kind == "p":
            p = doc.add_paragraph()
            add_runs(p, b[1])
        elif kind == "table":
            rows = []
            for r in b[1]:
                r = r.strip().strip("|")
                rows.append([c.strip() for c in r.split("|")])
            if len(rows) < 2:
                continue
            header = rows[0]
            data = rows[2:]
            table = doc.add_table(rows=1, cols=len(header))
            table.style = "Table Grid"
            for i, h in enumerate(header):
                cell = table.rows[0].cells[i]
                cell.text = ""
                p = cell.paragraphs[0]
                add_runs(p, h)
                for run in p.runs:
                    run.bold = True
            for r in data:
                cells = table.add_row().cells
                for i, c in enumerate(r[:len(header)]):
                    cells[i].text = ""
                    add_runs(cells[i].paragraphs[0], c)
        elif kind == "list":
            for it in b[1]:
                p = doc.add_paragraph(style="List Bullet")
                add_runs(p, it)
        elif kind == "rule":
            if first_rule:
                first_rule = False
                doc.add_page_break()
            else:
                doc.add_paragraph("—" * 12)
    doc.save(DOCX)

def main() -> int:
    md = strip_comments(MD.read_text())
    TEX.write_text(build_tex(md))
    print("wrote", TEX.name)
    ok, err = compile_pdf()
    print("pdf", "ok" if ok else "FAILED")
    if not ok:
        print(err[:3000])
    try:
        build_docx(md)
        print("wrote", DOCX.name)
    except Exception as e:
        print("docx skipped:", repr(e))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
