import re

with open('delhi-sightseeing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove Distance Labels & Travel Times block
distance_block = re.compile(r'<!-- Distance Labels & Travel Times -->.*?<!-- SIGHT MARKERS -->', re.DOTALL)
content = distance_block.sub('<!-- SIGHT MARKERS -->', content)

# Remove specific time pill labels
# <rect x="310" y="43" width="60" height="18" rx="6" fill="#1a1208"/>
# <text x="340" y="56" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="700" fill="#f0c060">09:30 AM</text>
time_pills = re.compile(r'<rect[^>]+fill="#1a1208"/>\s*<text[^>]+fill="#f0c060">\d{2}:\d{2} [AP]M</text>', re.DOTALL)
content = time_pills.sub('', content)

# Remove the scale block (contains "10 km")
scale_block = re.compile(r'<g transform="translate\(52,444\)">.*?</g>', re.DOTALL)
content = scale_block.sub('', content)

with open('delhi-sightseeing.html', 'w', encoding='utf-8') as f:
    f.write(content)
