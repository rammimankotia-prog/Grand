import re

with open('8-hours-sightseeing-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Generate new SVG content for Delhi Map
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
                        
                        <!-- Map background aesthetic -->
                        <path d="M100,50 C200,30 400,30 500,50 C600,70 630,200 600,300 C570,400 450,450 350,450 C250,450 100,400 70,300 C40,200 50,70 100,50 Z" fill="#e0d3bd" opacity="0.45"/>
                        
                        <!-- Grid Lines -->
                        <line x1="340" y1="20" x2="340" y2="460" stroke="#c5b89a" stroke-width="0.6" stroke-dasharray="5,8" opacity="0.3"/>
                        <line x1="20" y1="240" x2="660" y2="240" stroke="#c5b89a" stroke-width="0.6" stroke-dasharray="5,8" opacity="0.3"/>
                        
                        <!-- Route Line Paths Connecting Sights -->
                        <!-- Route: Old Delhi (200, 140) -> New Delhi (480, 140) -> South Delhi (480, 340) -> Drop-off (200, 340) -->
                        <path id="route-path" d="M200,140 Q340,80 480,140 Q540,240 480,340 Q340,400 200,340 Q140,240 200,140" fill="transparent" stroke="#a67c31" stroke-width="3" stroke-dasharray="12,8" stroke-linecap="round" opacity="0.9">
                            <animate attributeName="stroke-dashoffset" from="0" to="-200" dur="5s" repeatCount="indefinite"/>
                        </path>

                        <!-- Moving Taxi Sedan along route -->
                        <g>
                            <animateMotion dur="12s" repeatCount="indefinite" rotate="auto">
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
                                <!-- Headlights (Front, facing right) -->
                                <rect x="18.5" y="0.8" width="1.2" height="1.2" rx="0.3" fill="#fef08a" stroke="#ca8a04" stroke-width="0.4"/>
                                <rect x="18.5" y="8" width="1.2" height="1.2" rx="0.3" fill="#fef08a" stroke="#ca8a04" stroke-width="0.4"/>
                                <!-- Taillights (Rear, facing left) -->
                                <rect x="-0.3" y="0.8" width="0.8" height="1.2" rx="0.3" fill="#ef4444"/>
                                <rect x="-0.3" y="8" width="0.8" height="1.2" rx="0.3" fill="#ef4444"/>
                                <!-- Windshield (Front, facing right) -->
                                <path d="M12,1.5 L15,3 L15,7 L12,8.5 Z" fill="#e0f2fe" stroke="#0369a1" stroke-width="0.5"/>
                                <!-- Rear Window (Back, facing left) -->
                                <path d="M5,1.8 L3.5,3 L3.5,7 L5,8.2 Z" fill="#e0f2fe" stroke="#0369a1" stroke-width="0.5"/>
                                <!-- Side windows -->
                                <rect x="5.5" y="0.8" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <rect x="8.8" y="0.8" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <rect x="5.5" y="8.4" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <rect x="8.8" y="8.4" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <!-- Bumpers -->
                                <rect x="-0.8" y="2" width="0.8" height="6" fill="#1e293b" rx="0.3"/>
                                <rect x="20" y="2" width="0.8" height="6" fill="#1e293b" rx="0.3"/>
                                <!-- Taxi Light on Roof -->
                                <rect x="7.5" y="3.5" width="5" height="3" rx="0.6" fill="#fff" stroke="#b45309" stroke-width="0.8"/>
                                <text x="10" y="5.7" font-family="Outfit, sans-serif" font-size="2.2" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="0.1">TAXI</text>
                            </g>
                        </g>

                        <!-- Distances / Durations -->
                        <g transform="translate(340,90)"><rect x="-35" y="-12" width="70" height="24" rx="12" fill="#1a1208" opacity="0.88"/><text x="0" y="3" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~25 min drive</text></g>
                        <g transform="translate(530,240)"><rect x="-35" y="-12" width="70" height="24" rx="12" fill="#1a1208" opacity="0.88"/><text x="0" y="3" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~35 min drive</text></g>
                        <g transform="translate(340,390)"><rect x="-35" y="-12" width="70" height="24" rx="12" fill="#1a1208" opacity="0.88"/><text x="0" y="3" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~40 min drive</text></g>
                        <g transform="translate(150,240)"><rect x="-35" y="-12" width="70" height="24" rx="12" fill="#1a1208" opacity="0.88"/><text x="0" y="3" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~30 min drive</text></g>

                        <!-- Node 1: Old Delhi -->
                        <g>
                            <circle cx="200" cy="140" r="25" fill="rgba(166,124,49,0.1)">
                                <animate attributeName="r" values="25;35;25" dur="3s" repeatCount="indefinite"/>
                                <animate attributeName="opacity" values="1;0;1" dur="3s" repeatCount="indefinite"/>
                            </circle>
                            <circle cx="200" cy="140" r="16" fill="#f0c060" filter="url(#pinShadow)"/>
                            <circle cx="200" cy="140" r="13" fill="#a67c31"/>
                            <text x="200" y="145" text-anchor="middle" font-family="Cinzel, serif" font-size="14" font-weight="700" fill="#fff">O</text>
                            
                            <rect x="140" y="165" width="120" height="28" rx="14" fill="#fff" stroke="#c59b3f" stroke-width="2" filter="url(#labelShadow)"/>
                            <text x="200" y="183" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#a67c31" letter-spacing="1.5">OLD DELHI</text>
                            
                            <rect x="160" y="110" width="80" height="18" rx="9" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="200" y="122" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR STARTS</text>
                        </g>

                        <!-- Node 2: New Delhi -->
                        <g>
                            <circle cx="480" cy="140" r="16" fill="#f0c060" filter="url(#pinShadow)"/>
                            <circle cx="480" cy="140" r="13" fill="#6B5F54"/>
                            <text x="480" y="145" text-anchor="middle" font-family="Cinzel, serif" font-size="14" font-weight="700" fill="#fff">N</text>
                            
                            <rect x="420" y="165" width="120" height="28" rx="14" fill="#fff" stroke="#c59b3f" stroke-width="2" filter="url(#labelShadow)"/>
                            <text x="480" y="183" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6B5F54" letter-spacing="1.5">NEW DELHI</text>
                        </g>

                        <!-- Node 3: South Delhi -->
                        <g>
                            <circle cx="480" cy="340" r="16" fill="#f0c060" filter="url(#pinShadow)"/>
                            <circle cx="480" cy="340" r="13" fill="#6B5F54"/>
                            <text x="480" y="345" text-anchor="middle" font-family="Cinzel, serif" font-size="14" font-weight="700" fill="#fff">S</text>
                            
                            <rect x="420" y="365" width="120" height="28" rx="14" fill="#fff" stroke="#c59b3f" stroke-width="2" filter="url(#labelShadow)"/>
                            <text x="480" y="383" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6B5F54" letter-spacing="1.5">SOUTH DELHI</text>
                        </g>

                        <!-- Node 4: Drop-off -->
                        <g>
                            <circle cx="200" cy="340" r="16" fill="#f0c060" filter="url(#pinShadow)"/>
                            <circle cx="200" cy="340" r="13" fill="#a67c31"/>
                            <text x="200" y="345" text-anchor="middle" font-family="Cinzel, serif" font-size="14" font-weight="700" fill="#fff">D</text>
                            
                            <rect x="140" y="365" width="120" height="28" rx="14" fill="#fff" stroke="#c59b3f" stroke-width="2" filter="url(#labelShadow)"/>
                            <text x="200" y="383" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#a67c31" letter-spacing="1.5">DROP-OFF</text>

                            <rect x="160" y="395" width="80" height="18" rx="9" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="200" y="407" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR ENDS</text>
                        </g>

                        <!-- Compass & Details -->
                        <g transform="translate(580,60)">
                            <circle cx="0" cy="0" r="22" fill="#fff" stroke="#e5d0a3" stroke-width="1"/>
                            <polygon points="-4,0 0,-14 4,0" fill="#a67c31"/>
                            <polygon points="-4,0 0,14 4,0" fill="#e5d0a3"/>
                            <text x="0" y="-16" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" font-weight="700" fill="#a67c31">N</text>
                            <text x="0" y="22" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#b0a592">S</text>
                            <text x="18" y="2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#b0a592">E</text>
                            <text x="-18" y="2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#b0a592">W</text>
                        </g>
                        
                        <text x="340" y="445" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="600" letter-spacing="3" fill="#b0a592">NEW DELHI LOCAL SIGHTSEEING</text>
                    </svg>"""

html = re.sub(r'<svg viewBox="0 0 680 480".*?</svg>', new_svg, html, flags=re.DOTALL)

with open('8-hours-sightseeing-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
