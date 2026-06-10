import re

with open('5-days-golden-triangle-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the route path
html = html.replace('d="M340,148 L190,318 L438,318"', 'd="M340,148 L190,318 L438,318 L340,148"')

# 2. Remove TOUR ENDS from Agra and update its Day to Day 4
agra_old = """<rect x="368" y="280" width="140" height="20" rx="10" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="438" y="293" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR ENDS</text>
<rect x="418" y="303" width="40" height="14" rx="4" fill="#1a1208"/>
                            <text x="438" y="313" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">Day 4 & 5</text>"""

agra_new = """<rect x="418" y="280" width="40" height="14" rx="4" fill="#1a1208"/>
                            <text x="438" y="290" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">Day 4</text>"""

html = html.replace(agra_old, agra_new)

# 3. Add TOUR ENDS (IGI AIRPORT) and Day 5 to Delhi
delhi_block_target = """<text x="340" y="124" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11.5" font-weight="800" fill="#6b4c12" letter-spacing="2">DELHI</text>
                        </g>"""

delhi_ends = """<text x="340" y="124" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11.5" font-weight="800" fill="#6b4c12" letter-spacing="2">DELHI</text>
                            
                            <rect x="250" y="170" width="180" height="20" rx="10" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="340" y="183" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR ENDS (IGI AIRPORT)</text>

                            <rect x="320" y="193" width="40" height="14" rx="4" fill="#1a1208"/>
                            <text x="340" y="203" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">Day 5</text>
                        </g>"""

html = html.replace(delhi_block_target, delhi_ends)

with open('5-days-golden-triangle-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
