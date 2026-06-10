import re

with open('5-days-golden-triangle-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta and Title
html = re.sub(r'<title>.*?</title>', '<title>5 Days Golden Triangle Tour | Grand Holidays</title>', html)
html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="5 Days Golden Triangle tour covering Delhi, Jaipur, and Agra in a private Swift Dzire.">', html)
html = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://grandholidaytours.com/5-days-golden-triangle-tour.html">', html)

# JS import
html = html.replace('<script src="golden-triangle.js?v=4"></script>', '<script src="5-days-golden-triangle-tour.js"></script>')
html = html.replace('<script src="golden-triangle.js"></script>', '<script src="5-days-golden-triangle-tour.js"></script>')

# Mode Switcher removal
mode_switcher_regex = r'<div class="mode-switcher-container glass-card">.*?</div>\s*(<div class="tour-layout-grid">)'
html = re.sub(mode_switcher_regex, r'\1', html, flags=re.DOTALL)

# Update map header
html = html.replace('The Golden Triangle Route', '5 Days Golden Triangle Route')

# Update Map paths
html = re.sub(r'<path id="route-path" d=".*?"', '<path id="route-path" d="M340,148 L190,318 L438,318"', html)

# Add "TOUR ENDS" to Agra, update "TOUR STARTS & ENDS" to "TOUR STARTS"
html = html.replace('TOUR STARTS & ENDS', 'TOUR STARTS')

# Update Days on Map
# Delhi
html = re.sub(r'<rect x="360" y="111" width="40" height="14" rx="4" fill="#1a1208"/>\s*<text x="380" y="121"[^>]*>Day 8</text>', '', html) # remove day 8
html = re.sub(r'(<text x="300" y="121"[^>]*>)Day 1(</text>)', r'\1Day 1 & 2\2', html)

# Jaipur
html = re.sub(r'(<text x="190" y="290"[^>]*>)Day 5(</text>)', r'\1Day 3 & 4\2', html)

# Agra
html = re.sub(r'(<text x="438" y="290"[^>]*>)Day 3(</text>)', r'\1Day 4 & 5\2', html)

# Add TOUR ENDS to Agra
agra_end_badge = """
                            <rect x="368" y="280" width="140" height="20" rx="10" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="438" y="293" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR ENDS</text>
"""
html = html.replace('<rect x="418" y="280"', agra_end_badge + '<rect x="418" y="303"')
html = re.sub(r'<text x="438" y="290"', '<text x="438" y="313"', html) # shift day tag down

with open('5-days-golden-triangle-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
