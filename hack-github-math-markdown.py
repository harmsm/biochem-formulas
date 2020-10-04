#!/usr/bin/env python
__description__ = \
"""
Hack that takes markdown with $$ LaTeX display formulas and renders as images
via mathjax.  Brilliantly unorthodox solution described here:
https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b
"""

import sys

try:
    input_file = sys.argv[1]
except IndexError:
    err = "\n\nUsage: ./hack-github-math-markdown.py markdown_file_with_math\n\n"
    raise ValueError(err)

out = []
with open(input_file,"r") as f:
    for line in f:
        if line.startswith("$$"):
            x = line.strip().strip("$$").strip()
            url = f"https://render.githubusercontent.com/render/math?math={x}"
            out.append(f"<img src=\"{url}\">\n")
        else:
            out.append(line)

print("".join(out))
