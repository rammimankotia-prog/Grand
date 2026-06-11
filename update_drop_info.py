import re

with open('rajasthan-desert-adventure.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_starts_ends = """                        <!-- TOUR STARTS / ENDS -->
                        <g transform="translate(500, 350)">
                            <rect x="-70" y="-60" width="140" height="20" rx="10" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="0" y="-47" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR STARTS / ENDS</text>
                            
                            <rect x="-40" y="-37" width="80" height="14" rx="4" fill="#1a1208"/>
                            <text x="0" y="-27" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">Day 1 &amp; Day 5</text>
                        </g>"""

new_starts_ends = """                        <!-- TOUR STARTS / ENDS -->
                        <g transform="translate(500, 350)">
                            <rect x="-70" y="-60" width="140" height="20" rx="10" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="0" y="-47" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR STARTS / ENDS</text>
                            
                            <rect x="-40" y="-37" width="80" height="14" rx="4" fill="#1a1208"/>
                            <text x="0" y="-27" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">Day 1 &amp; Day 5</text>

                            <rect x="-65" y="-19" width="130" height="14" rx="4" fill="#1a1208" opacity="0.85"/>
                            <text x="0" y="-9" text-anchor="middle" font-family="Outfit,sans-serif" font-size="6.5" font-weight="700" fill="rgba(255,220,120,0.9)">Drop at Jodhpur Railway Station</text>
                        </g>"""

html = html.replace(old_starts_ends, new_starts_ends)

with open('rajasthan-desert-adventure.html', 'w', encoding='utf-8') as f:
    f.write(html)
