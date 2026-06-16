#!/usr/bin/env python3
"""
Inject mobile.css, theme.css, and global-ux.js into all HTML pages
that don't already have them.
"""
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

GRAND_DIR = r'C:\Users\raman\.gemini\antigravity\scratch\Grand'

CSS_INJECT = '''    <link rel="stylesheet" href="mobile.css">
    <link rel="stylesheet" href="theme.css">'''

JS_INJECT = '    <script src="global-ux.js"></script>'

SKIP_FILES = {
    'googled60501e34605346d.html',
}

def needs_css(html):
    return 'mobile.css' not in html

def needs_js(html):
    return 'global-ux.js' not in html

updated = []
skipped = []

for fname in sorted(os.listdir(GRAND_DIR)):
    if not fname.endswith('.html'):
        continue
    if fname in SKIP_FILES:
        skipped.append(fname)
        continue

    fpath = os.path.join(GRAND_DIR, fname)
    try:
        html = open(fpath, encoding='utf-8').read()
    except Exception as e:
        print(f'  ERROR reading {fname}: {e}')
        continue

    changed = False

    # Inject CSS before </head>
    if needs_css(html):
        if '</head>' in html:
            html = html.replace('</head>', CSS_INJECT + '\n</head>', 1)
            changed = True
        else:
            print(f'  WARN: no </head> in {fname}')

    # Inject JS before </body>
    if needs_js(html):
        if '</body>' in html:
            html = html.replace('</body>', JS_INJECT + '\n</body>', 1)
            changed = True
        else:
            print(f'  WARN: no </body> in {fname}')

    if changed:
        open(fpath, 'w', encoding='utf-8').write(html)
        updated.append(fname)
        print(f'  ✓ Updated: {fname}')
    else:
        skipped.append(fname)
        print(f'  – Skipped (already injected): {fname}')

print(f'\nDone! Updated {len(updated)} files, skipped {len(skipped)} files.')
