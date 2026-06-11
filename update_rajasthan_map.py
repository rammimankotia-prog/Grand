import re

with open('rajasthan-heritage-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the feature blocks
html = html.replace('Pick-Up &amp; Stay', 'STAY')
html = html.replace('Hotel Grand Godwin', 'Premium hotel')
html = html.replace('Breakfast Location', 'BREAKFAST')
html = html.replace('Indian Grill Restaurant', 'Daily Breakfast')

# 2. Replace the entire gt-map-section
new_map_section = """    <!-- RAJASTHAN MAP SECTION -->
    <section class="gt-map-section">
        <div class="container">
            <div class="gt-map-header">
                <span class="eyebrow">Route Overview</span>
                <h2 class="gt-map-title">Rajasthan Heritage Route</h2>
                <p class="gt-map-subtitle">A heritage loop traversing through the Pink City, the Blue City, the Golden Sands of Thar, and the romantic Lake Palace.</p>
            </div>
            <div class="gt-map-wrapper">
                <div class="gt-map-canvas">
                    <svg viewBox="0 0 680 480" xmlns="http://www.w3.org/2000/svg" class="gt-svg">
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
                        <path id="route-path" d="M480,160 Q400,190 320,220 Q240,200 160,180 Q240,200 320,220 Q380,290 440,360" fill="none" stroke="#a67c31" stroke-width="3" stroke-dasharray="10,8" stroke-linecap="round" opacity="0.9">
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
                                <!-- Side windows (Split for Sedan) -->
                                <!-- Top side windows -->
                                <rect x="5.5" y="0.8" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <rect x="8.8" y="0.8" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <!-- Bottom side windows -->
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

                        <!-- Jaipur (480, 160) -->
                        <g>
                            <circle cx="480" cy="160" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="480" y="140" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">JAIPUR</text>
                        </g>

                        <!-- Jodhpur (320, 220) -->
                        <g>
                            <circle cx="320" cy="220" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="320" y="200" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">JODHPUR</text>
                        </g>

                        <!-- Jaisalmer (160, 180) -->
                        <g>
                            <circle cx="160" cy="180" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="160" y="160" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">JAISALMER</text>
                        </g>

                        <!-- Udaipur (440, 360) -->
                        <g>
                            <circle cx="440" cy="360" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="440" y="385" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">UDAIPUR</text>
                        </g>

                    </svg>
                </div>
                <div class="gt-city-cards">
                    <div class="gt-city-card">
                        <div class="city-card-num">01</div>
                        <div class="city-card-icon">&#127963;</div>
                        <h3 class="city-card-name">Jaipur</h3>
                        <p class="city-card-desc">The Pink City &mdash; Rajasthan's royal capital. Amber Fort, Hawa Mahal and palace hotels define this heritage jewel.</p>
                        <div class="city-card-tags"><span>Amber Fort</span><span>Hawa Mahal</span><span>City Palace</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">02</div>
                        <div class="city-card-icon">&#127984;</div>
                        <h3 class="city-card-name">Jodhpur</h3>
                        <p class="city-card-desc">The Blue City &mdash; guarded by the majestic Mehrangarh Fort. A mesmerizing sea of blue houses in the Thar.</p>
                        <div class="city-card-tags"><span>Mehrangarh Fort</span><span>Jaswant Thada</span><span>Mandore</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">03</div>
                        <div class="city-card-icon">&#127964;</div>
                        <h3 class="city-card-name">Jaisalmer</h3>
                        <p class="city-card-desc">The Golden City &mdash; rising from the desert sands. Famous for its living fort and intricate havelis.</p>
                        <div class="city-card-tags"><span>Jaisalmer Fort</span><span>Patwon ki Haveli</span><span>Sand Dunes</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">04</div>
                        <div class="city-card-icon">&#127961;</div>
                        <h3 class="city-card-name">Udaipur</h3>
                        <p class="city-card-desc">The Lake City &mdash; the most romantic city in India. Grand palaces overlooking the tranquil Lake Pichola.</p>
                        <div class="city-card-tags"><span>City Palace</span><span>Lake Pichola</span><span>Jagdish Temple</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

old_map_pattern = r'<!-- GT MAP SECTION -->\s*<section class="gt-map-section">.*?</section>'
html = re.sub(old_map_pattern, new_map_section, html, flags=re.DOTALL)

with open('rajasthan-heritage-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
