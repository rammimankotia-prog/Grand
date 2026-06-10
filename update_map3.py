import re

with open('5-days-golden-triangle-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace path
html = html.replace('d="M340,148 L190,318 L438,318 L270,170"', 'd="M340,148 L190,318 L438,318 L230,180"')

# Replace IGI Airport block
old_igi_g = """
                        <g>
                            <circle cx="270" cy="170" r="25" fill="rgba(166,124,49,0.1)">
                                <animate attributeName="r" values="12;22;12" dur="2.8s" repeatCount="indefinite"/>
                                <animate attributeName="opacity" values="0.5;0;0.5" dur="2.8s" repeatCount="indefinite"/>
                            </circle>
                            <circle cx="270" cy="170" r="10" fill="#a67c31" stroke="#fff" stroke-width="2.5" filter="url(#pinShadow)"/>
                            <text x="270" y="174" text-anchor="middle" font-family="Playfair Display,serif" font-size="10" font-weight="700" fill="#fff">✈</text>
                            
                            <rect x="225" y="138" width="90" height="24" rx="12" fill="#fff" stroke="#a67c31" stroke-width="2" filter="url(#labelShadow)"/>
                            <text x="270" y="154" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#6b4c12" letter-spacing="1">IGI AIRPORT</text>
                            
                            <rect x="220" y="185" width="100" height="18" rx="9" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="270" y="197" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR ENDS</text>

                            <rect x="250" y="206" width="40" height="14" rx="4" fill="#1a1208"/>
                            <text x="270" y="216" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">Day 5</text>
                        </g>"""

new_igi_g = """
                        <g>
                            <circle cx="230" cy="180" r="25" fill="rgba(166,124,49,0.1)">
                                <animate attributeName="r" values="12;22;12" dur="2.8s" repeatCount="indefinite"/>
                                <animate attributeName="opacity" values="0.5;0;0.5" dur="2.8s" repeatCount="indefinite"/>
                            </circle>
                            <circle cx="230" cy="180" r="10" fill="#a67c31" stroke="#fff" stroke-width="2.5" filter="url(#pinShadow)"/>
                            <text x="230" y="184" text-anchor="middle" font-family="Playfair Display,serif" font-size="10" font-weight="700" fill="#fff">✈</text>
                            
                            <rect x="185" y="148" width="90" height="24" rx="12" fill="#fff" stroke="#a67c31" stroke-width="2" filter="url(#labelShadow)"/>
                            <text x="230" y="164" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#6b4c12" letter-spacing="1">IGI AIRPORT</text>
                            
                            <rect x="180" y="195" width="100" height="18" rx="9" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="230" y="207" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR ENDS</text>

                            <rect x="210" y="216" width="40" height="14" rx="4" fill="#1a1208"/>
                            <text x="230" y="226" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">Day 5</text>
                        </g>"""

html = html.replace(old_igi_g, new_igi_g)

with open('5-days-golden-triangle-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
