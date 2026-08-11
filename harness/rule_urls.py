#!/usr/bin/env python3
"""Print every URL the site cites, one per line, for verify-sources.js.

The site cites what gen_rules.py cites, so read that rather than the research
corpus. The corpus is wider and includes documents that never reach a reader.
"""
import pathlib
import re

text = (pathlib.Path(__file__).resolve().parent / 'gen_rules.py').read_text()
for url in sorted(set(re.findall(r"https://[^'\"]+", text))):
    print(url)
