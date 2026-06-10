import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the existing .logo-accent { color: var(--primary); }
# with a more specific override.
old_accent = ".logo-accent {\n  color: var(--primary);\n}"
new_accent = """.logo-accent {
  color: var(--primary);
}

.nav-logo .logo-accent {
  font-size: inherit;
  letter-spacing: normal;
  text-transform: uppercase;
  font-family: inherit;
  font-weight: inherit;
}
"""

css = css.replace(old_accent, new_accent)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
