#!/bin/bash 
./hack-github-math-markdown.py formula.md > README.md
pandoc formula.md -s -o formula.pdf
git add formula.md formula.pdf README.md
git commit -m "updated formulas"
git push origin main
