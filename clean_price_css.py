import os
import re

SITE_DIR = r"c:\xampp\htdocs\Grand"

css_files = [f for f in os.listdir(SITE_DIR) if f.endswith('.css')]

# Regex to match the .price-summary-box block
# It usually looks like:
# .price-summary-box { ... }
# .summary-label { ... }
# .summary-value { ... }

# We'll use a regex that matches each of these classes and their blocks.
# A block is class name, any spaces, '{', anything until '}'
def remove_class(content, class_name):
    pattern = r"^[ \t]*" + re.escape(class_name) + r"[ \t]*\{[^}]*\}[ \t]*\n?"
    return re.sub(pattern, "", content, flags=re.MULTILINE)

count = 0
for fname in css_files:
    if fname == "index.css": continue # we will append here manually
    fpath = os.path.join(SITE_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    orig = content
    content = remove_class(content, ".price-summary-box")
    content = remove_class(content, ".summary-label")
    content = remove_class(content, ".summary-value")
    
    if orig != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {fname}")
        count += 1
        
print(f"Cleaned {count} CSS files.")
