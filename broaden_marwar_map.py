import re

with open('marvellous-marwar-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_svg = """                    <svg viewBox="0 0 680 480" xmlns="http://www.w3.org/2000/svg" class="gt-svg">
                        <defs>
                            <filter id="pinShadow"><feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="rgba(0,0,0,0.28)"/></filter>
                            <filter id="labelShadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="rgba(0,0,0,0.1)"/></filter>
                            <radialGradient id="bgG" cx="50%" cy="50%" r="60%">
                                <stop offset="0%" stop-color="#fdf8f1"/>
                                <stop offset="100%" stop-color="#ede4d5"/>
                            </radialGradient>
                        </defs>
                        <rect x="0" y="0" width="680" height="480" rx="20" fill="url(#bgG)"/>
                        
                        <!-- Route Line Paths Connecting Sights -->
                        <path id="route-path" d="M500,350 L340,100 L120,280 L500,350" fill="none" stroke="#a67c31" stroke-width="3" stroke-dasharray="10,8" stroke-linecap="round" opacity="0.9">
                             <animate attributeName="stroke-dashoffset" from="0" to="-200" dur="5s" repeatCount="indefinite"/>
                        </path>

                        <!-- Moving Taxi Sedan along route -->
                        <g>
                            <animateMotion dur="16s" repeatCount="indefinite" rotate="auto">
                                <mpath href="#route-path"/>
                            </animateMotion>
                            <g transform="translate(-10, -5)">
                                <!-- Wheels -->
                                <rect x="3" y="-1.2" width="4" height="1.2" fill="#111" rx="0.5"/>
                                <rect x="13" y="-1.2" width="4" height="1.2" fill="#111" rx="0.5"/>
                                <rect x="3" y="10" width="4" height="1.2" fill="#111" rx="0.5"/>
                                <rect x="13" y="10" width="4" height="1.2" fill="#111" rx="0.5"/>
                                <!-- Car body -->
                                <rect x="0" y="0" width="20" height="10" rx="3" fill="#f59e0b" stroke="#78350f" stroke-width="1.2"/>
                                <!-- Front Grill -->
                                <rect x="19.5" y="3.5" width="0.7" height="3" fill="#1e293b" rx="0.2"/>
                                <!-- Headlights -->
                                <rect x="18.5" y="0.8" width="1.2" height="1.2" rx="0.3" fill="#fef08a" stroke="#ca8a04" stroke-width="0.4"/>
                                <rect x="18.5" y="8" width="1.2" height="1.2" rx="0.3" fill="#fef08a" stroke="#ca8a04" stroke-width="0.4"/>
                                <!-- Taillights -->
                                <rect x="-0.3" y="0.8" width="0.8" height="1.2" rx="0.3" fill="#ef4444"/>
                                <rect x="-0.3" y="8" width="0.8" height="1.2" rx="0.3" fill="#ef4444"/>
                                <!-- Windshield -->
                                <path d="M12,1.5 L15,3 L15,7 L12,8.5 Z" fill="#e0f2fe" stroke="#0369a1" stroke-width="0.5"/>
                                <!-- Rear Window -->
                                <path d="M5,1.8 L3.5,3 L3.5,7 L5,8.2 Z" fill="#e0f2fe" stroke="#0369a1" stroke-width="0.5"/>
                                <!-- Side windows -->
                                <rect x="5.5" y="0.8" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <rect x="8.8" y="0.8" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <rect x="5.5" y="8.4" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <rect x="8.8" y="8.4" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <!-- Bumpers -->
                                <rect x="-0.8" y="2" width="0.8" height="6" fill="#1e293b" rx="0.3"/>
                                <rect x="20" y="2" width="0.8" height="6" fill="#1e293b" rx="0.3"/>
                                <!-- Taxi Light -->
                                <rect x="7.5" y="3.5" width="5" height="3" rx="0.6" fill="#fff" stroke="#b45309" stroke-width="0.8"/>
                                <text x="10" y="5.7" font-family="Outfit, sans-serif" font-size="2.2" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="0.1">TAXI</text>
                            </g>
                        </g>

                        <!-- Distance Badges -->
                        <!-- Jodhpur to Bikaner -->
                        <g transform="translate(420,225)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">250 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~4.5 hrs drive</text>
                        </g>

                        <!-- Bikaner to Jaisalmer -->
                        <g transform="translate(230,190)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">330 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~5 hrs drive</text>
                        </g>

                        <!-- Jaisalmer to Jodhpur -->
                        <g transform="translate(310,315)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">285 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~4.5 hrs drive</text>
                        </g>

                        <!-- TOUR STARTS / ENDS -->
                        <g transform="translate(500, 350)">
                            <rect x="-70" y="-60" width="140" height="20" rx="10" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="0" y="-47" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR STARTS / ENDS</text>
                            
                            <rect x="-40" y="-37" width="80" height="14" rx="4" fill="#1a1208"/>
                            <text x="0" y="-27" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">Day 1 &amp; Day 5</text>
                        </g>

                        <!-- Jodhpur (500, 350) -->
                        <g>
                            <circle cx="500" cy="350" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="500" y="375" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">JODHPUR</text>
                        </g>

                        <!-- Bikaner (340, 100) -->
                        <g>
                            <circle cx="340" cy="100" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="340" y="80" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">BIKANER</text>
                        </g>

                        <!-- Jaisalmer (120, 280) -->
                        <g>
                            <circle cx="120" cy="280" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="120" y="260" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">JAISALMER</text>
                        </g>

                    </svg>"""

old_svg_pattern = r'<svg viewBox="0 0 680 480".*?</svg>'
html = re.sub(old_svg_pattern, new_svg, html, flags=re.DOTALL)

with open('marvellous-marwar-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
