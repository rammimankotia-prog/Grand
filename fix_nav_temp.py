import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

nav = re.search(r'<nav class="nav-menu" id="navMenu">.*?</nav>', idx, re.DOTALL).group(0)

with open('8-hours-sightseeing-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<nav class="nav-menu" id="navMenu">.*?</nav>', nav, html, flags=re.DOTALL)

with open('8-hours-sightseeing-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
