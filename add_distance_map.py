import re

with open('rajasthan-heritage-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Badges to add into the SVG
badges_svg = """
                        <!-- Distance Badges -->
                        <!-- Jaipur to Jodhpur -->
                        <g transform="translate(400,175)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">350 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~6 hrs drive</text>
                        </g>

                        <!-- Jodhpur to Jaisalmer -->
                        <g transform="translate(240,185)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">300 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~5 hrs drive</text>
                        </g>

                        <!-- Jodhpur to Udaipur -->
                        <g transform="translate(380,290)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">265 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~5 hrs drive</text>
                        </g>
"""

# Insert the badges right before the first city <g> element in the SVG
insert_target = "                        <!-- Jaipur (480, 160) -->"
html = html.replace(insert_target, badges_svg + "\n" + insert_target)

with open('rajasthan-heritage-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
