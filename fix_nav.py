import re

with open('delhi-travel-guide.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the Delhi Guide nav item from the header nav
html = html.replace(
    '                    <li><a href="delhi-travel-guide.html" class="nav-link" style="color: var(--gold);">Delhi Guide</a></li>\n',
    ''
)

with open('delhi-travel-guide.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
