"""Render out/report.md to out/report.pdf via markdown-it-py + headless Chrome."""
import re
import shutil
import subprocess
from pathlib import Path

from markdown_it import MarkdownIt

CSS = """
@page { size: A4 landscape; margin: 12mm; }
body { font-family: "DejaVu Sans", "Noto Sans", "Liberation Sans", Arial, sans-serif; font-size: 10pt; line-height: 1.35; color: #111; }
h1 { font-size: 20pt; } h2 { font-size: 15pt; margin-top: 1.2em; border-bottom: 1px solid #999; }
h3 { font-size: 12pt; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; table-layout: auto; margin: 0.6em 0; }
th, td { border: 1px solid #888; padding: 2px 5px; vertical-align: top; overflow-wrap: anywhere; word-break: break-word; }
th { background: #eee; overflow-wrap: normal; word-break: normal; hyphens: none; }
th, td:nth-child(-n+1) { white-space: nowrap; }
tr { page-break-inside: avoid; }
details { margin: 0.3em 0; } summary { font-weight: bold; }
blockquote { margin: 0.3em 0 0.3em 1em; padding-left: 0.8em; border-left: 3px solid #bbb; color: #333; }
code { font-size: 9pt; }
"""


def run(cfg=None, out_dir="out"):
    out = Path(out_dir).resolve()
    md = (out / "report.md").read_text(encoding="utf-8")
    html = MarkdownIt("commonmark", {"html": True}).enable("table").render(md)
    html = re.sub(r"<details(?![^>]*\bopen\b)", "<details open", html)
    page = (f'<!doctype html><html lang="pl"><head><meta charset="utf-8">'
            f'<title>AI concerns PL</title><style>{CSS}</style></head><body>{html}</body></html>')
    html_path, pdf_path = out / "report.html", out / "report.pdf"
    html_path.write_text(page, encoding="utf-8")
    chrome = shutil.which("google-chrome") or "/usr/bin/google-chrome"
    subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path}", html_path.as_uri()],
                   check=True, capture_output=True, timeout=180)
    print(f"[pdf] wrote {pdf_path} ({pdf_path.stat().st_size // 1024} KB)")
    return pdf_path
