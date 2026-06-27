"""
cleanup_mobile_toggles.py
Removes duplicate mobile menu toggle bindings from individual JS files,
since global-ux.js already handles them perfectly.
"""

import os
import re

SITE_DIR = r"c:\xampp\htdocs\Grand"
SKIP = {'global-ux.js'}

def read_file(path):
    for enc in ('utf-8', 'utf-8-sig', 'latin-1', 'cp1252', 'utf-16'):
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read(), enc
        except (UnicodeDecodeError, ValueError):
            continue
    return None, None

def main():
    js_files = [f for f in os.listdir(SITE_DIR) if f.endswith('.js') and f not in SKIP]
    
    # We want to match the whole Mobile Navigation Toggle block and the Dropdown toggle block
    
    count = 0
    for fname in js_files:
        fpath = os.path.join(SITE_DIR, fname)
        
        content, enc = read_file(fpath)
        if content is None:
            print(f"Failed to read {fname}")
            continue
            
        new_content = content
        
        # Remove Mobile Navigation Toggle
        # We can just remove lines containing menuToggle inside these files since global-ux.js uses $()
        
        # Actually, a safer way:
        # Find from "// Mobile Navigation Toggle" until right before the next "//" or end of DOMContentLoaded
        # Because we know the exact structure, let's just use a regex to match the known block
        block_regex = r"[ \t]*// Mobile Navigation Toggle[\s\S]*?(?=[ \t]*//[ \t]*[A-Z]|$)"
        
        # We also want to remove "Dropdown toggle for mobile viewports"
        block_regex2 = r"[ \t]*// Dropdown toggle for mobile viewports[\s\S]*?(?=[ \t]*//[ \t]*[A-Z]|$)"
        
        # And "Mobile Dropdown Menu Toggle" (some files use this)
        block_regex3 = r"[ \t]*// Mobile Dropdown Menu Toggle[\s\S]*?(?=[ \t]*//[ \t]*[A-Z]|$)"

        new_content = re.sub(block_regex, '', new_content)
        new_content = re.sub(block_regex2, '', new_content)
        new_content = re.sub(block_regex3, '', new_content)
        
        # Alternatively, we can just remove all lines containing `menuToggle` or `dropdownToggle` 
        # But block removal is cleaner. Let's see if there are still any left
        
        if new_content != content:
            with open(fpath, 'w', encoding=enc) as f:
                f.write(new_content)
            print(f"Patched {fname}")
            count += 1
            
    print(f"Done. Patched {count} files.")

if __name__ == '__main__':
    main()
