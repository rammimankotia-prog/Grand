"""
add_client_validation.py  v2
Adds client-side validation for Name, Email, Mobile and Preferred Date
to all tour booking form JS handlers.
"""

import os
import re

SITE_DIR = r"c:\xampp\htdocs\Grand"

SKIP = {'global-ux.js', 'generate-sitemap.js', 'setup-hooks.js', 'script.js',
        'index.js', 'car-booking.js', 'contact.js', 'update_headers_footers.py',
        'add_client_validation.py'}

VALIDATION_SNIPPET = """\
            // ── Required-field validation ────────────────────────────
            if (!name || !email || !mobile || !date) {
                var missing = [];
                if (!name)   missing.push('Full Name');
                if (!email)  missing.push('Email Address');
                if (!mobile) missing.push('Mobile Number');
                if (!date)   missing.push('Preferred Date');
                alert('Please fill in the required fields:\\n\\u2022 ' + missing.join('\\n\\u2022 '));
                if (submitBtn) { submitBtn.innerText = origText; submitBtn.disabled = false; }
                return;
            }
            // ────────────────────────────────────────────────────────
"""

def read_file(path):
    for enc in ('utf-8', 'utf-8-sig', 'latin-1', 'cp1252'):
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read(), enc
        except (UnicodeDecodeError, ValueError):
            continue
    return None, None

def write_file(path, content, enc):
    with open(path, 'w', encoding=enc) as f:
        f.write(content)

def patch(content):
    if 'Required-field validation' in content:
        return content, 'already patched'

    # 1. Capture original button text before disabling
    # Insert `var origText = ...` before the disable block
    content = re.sub(
        r"(const submitBtn = bookingForm\.querySelector\(['\"]\.btn-sidebar-submit['\"]\);)",
        r"\1\n            var origText = submitBtn ? submitBtn.innerText : 'Submit';",
        content,
        count=1
    )

    # 2. Find where all 4 field vars are read and insert validation before fetch(
    # Strategy: find `const date = ` line then find the next `fetch(` and insert before it
    # We'll use a two-step approach

    # Find position of `const date =` assignment
    date_match = re.search(r'const date\s*=\s*[^\n]+\n', content)
    if not date_match:
        return content, 'date var not found'

    # Find the next `fetch(` after that position
    fetch_match = re.search(r'[ \t]*fetch\(', content[date_match.end():])
    if not fetch_match:
        return content, 'fetch not found after date'

    insert_pos = date_match.end() + fetch_match.start()

    # Get the indentation of the fetch line
    fetch_line = content[insert_pos:]
    indent = re.match(r'([ \t]*)', fetch_line).group(1)

    # Build the validation block with matching indentation
    validation = VALIDATION_SNIPPET

    new_content = content[:insert_pos] + validation + content[insert_pos:]
    return new_content, 'updated'


def main():
    js_files = sorted([
        f for f in os.listdir(SITE_DIR)
        if f.endswith('.js') and f not in SKIP
    ])
    print(f"\nProcessing {len(js_files)} JS files...\n")

    for fname in js_files:
        fpath = os.path.join(SITE_DIR, fname)
        content, enc = read_file(fpath)
        if content is None:
            print(f"  !! {fname}  [cannot read]")
            continue

        new_content, reason = patch(content)
        if new_content != content:
            write_file(fpath, new_content, enc)
            print(f"  OK {fname}  [{reason}]")
        else:
            print(f"  -- {fname}  [{reason}]")

    print("\nDone.")

if __name__ == '__main__':
    main()
