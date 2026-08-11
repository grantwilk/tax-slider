#!/usr/bin/env python3
"""Put the checked rule set into the page. Run from anywhere.

index.html is built, not hand-edited. Edit page.html for markup and style, and
gen_rules.py for the figures.
"""

import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

rules = subprocess.run([sys.executable, str(HERE / 'gen_rules.py')],
                       capture_output=True, text=True)
sys.stderr.write(rules.stderr)
if rules.returncode:
    sys.exit(rules.returncode)

page = (HERE / 'page.html').read_text()
if '/*__RULES__*/' not in page:
    sys.exit('page.html has no /*__RULES__*/ marker')

out = page.replace('/*__RULES__*/', rules.stdout.rstrip())
(ROOT / 'index.html').write_text(out)
print('index.html: %d lines' % out.count('\n'))
