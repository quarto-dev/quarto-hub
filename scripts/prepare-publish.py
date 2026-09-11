#!/usr/bin/env python3
"""Prepare Quarto Hub sources for a public quarto-cli build.

Run in CI on a checkout (not on the working tree you sync with Hub). It:

1. Removes `format: q2-preview` from YAML frontmatter. Hub's editor needs it,
   but in a website build it overrides `format: html` and breaks rendering.
2. Removes Hub review comments, stored inline as `[>> comment text]`, which
   quarto-cli would render as visible text.

Usage: python3 scripts/prepare-publish.py [project-dir]
"""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
FRONTMATTER_LINE = re.compile(r"^format:\s*q2-preview\s*\n", re.M)
HUB_COMMENT = re.compile(r"\[>>[^\]]*\]")

changed = 0
for path in root.rglob("*.qmd"):
    if any(part.startswith((".", "_site")) for part in path.relative_to(root).parts):
        continue
    text = path.read_text(encoding="utf-8")
    new = FRONTMATTER_LINE.sub("", text)
    new = HUB_COMMENT.sub("", new)
    if new != text:
        path.write_text(new, encoding="utf-8")
        changed += 1
        print(f"cleaned {path.relative_to(root)}")

print(f"{changed} file(s) cleaned")
