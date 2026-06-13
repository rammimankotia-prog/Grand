import os
from bs4 import BeautifulSoup

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
html_file = os.path.join(repo_path, '4-days-golden-triangle-tour.html')

with open(html_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

svg_map = soup.find('svg', class_='gt-svg')
if svg_map:
    new_svg = """
    <svg class="gt-svg" viewBox="0 0 680 480" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <filter id="pinShadow"><feDropShadow dx="0" dy="3" flood-color="rgba(0,0,0,0.28)" stdDeviation="5"/></filter>
            <filter id="labelShadow"><feDropShadow dx="0" dy="2" flood-color="rgba(0,0,0,0.1)" stdDeviation="3"/></filter>
            <radialGradient cx="50%" cy="50%" id="bgG" r="60%">
                <stop offset="0%" stop-color="#fdf8f1"/>
                <stop offset="100%" stop-color="#ede4d5"/>
            </radialGradient>
            <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#b0a090"/>
                <stop offset="50%" stop-color="#A67C31"/>
                <stop offset="100%" stop-color="#b0a090"/>
            </linearGradient>
            <!-- Start/End Marker Gradient -->
            <linearGradient id="startEndGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#4a90e2"/>
                <stop offset="100%" stop-color="#2a5298"/>
            </linearGradient>
        </defs>
        
        <rect fill="url(#bgG)" height="100%" rx="16" width="100%"/>
        
        <!-- Route Path -->
        <!-- Delhi(180, 140) -> Agra(480, 220) -> Jaipur(220, 360) -> Delhi(180,140) -->
        <path id="route-path" d="M 180 140 Q 330 140 480 220 Q 380 340 220 360 Q 140 250 180 140" fill="none" stroke="url(#lineGrad)" stroke-dasharray="8 6" stroke-linecap="round" stroke-width="3">
            <animate attributeName="stroke-dashoffset" dur="6s" from="0" repeatCount="indefinite" to="-200"></animate>
        </path>

        <!-- Distance Markers -->
        <!-- Delhi to Agra: 240 KM -->
        <g transform="translate(330, 160)">
            <rect fill="#fff" filter="url(#labelShadow)" height="20" rx="10" width="56" x="-28" y="-10"/>
            <text fill="#b0a090" font-family="Outfit, sans-serif" font-size="10" font-weight="700" text-anchor="middle" x="0" y="3">240 KM</text>
        </g>
        
        <!-- Agra to Jaipur: 240 KM -->
        <g transform="translate(360, 305)">
            <rect fill="#fff" filter="url(#labelShadow)" height="20" rx="10" width="56" x="-28" y="-10"/>
            <text fill="#b0a090" font-family="Outfit, sans-serif" font-size="10" font-weight="700" text-anchor="middle" x="0" y="3">240 KM</text>
        </g>

        <!-- Jaipur to Delhi: 280 KM -->
        <g transform="translate(145, 250)">
            <rect fill="#fff" filter="url(#labelShadow)" height="20" rx="10" width="56" x="-28" y="-10"/>
            <text fill="#b0a090" font-family="Outfit, sans-serif" font-size="10" font-weight="700" text-anchor="middle" x="0" y="3">280 KM</text>
        </g>

        <!-- Moving Taxi -->
        <g>
            <animateMotion dur="15s" repeatCount="indefinite" rotate="auto">
                <mpath href="#route-path"></mpath>
            </animateMotion>
            <g transform="translate(-10, -5)">
                <!-- Wheels -->
                <rect fill="#111" height="1.2" rx="0.5" width="4" x="3" y="-1.2"></rect>
                <rect fill="#111" height="1.2" rx="0.5" width="4" x="13" y="-1.2"></rect>
                <rect fill="#111" height="1.2" rx="0.5" width="4" x="3" y="10"></rect>
                <rect fill="#111" height="1.2" rx="0.5" width="4" x="13" y="10"></rect>
                <!-- Car body -->
                <rect fill="#f59e0b" height="10" rx="3" stroke="#78350f" stroke-width="1.2" width="20" x="0" y="0"></rect>
                <!-- Front Grill -->
                <rect fill="#1e293b" height="3" rx="0.2" width="0.7" x="19.5" y="3.5"></rect>
                <!-- TAXI text -->
                <rect fill="#fff" height="3" rx="0.5" width="8" x="6" y="3.5"></rect>
                <text fill="#000" font-family="Outfit, sans-serif" font-size="2.2" font-weight="900" letter-spacing="0.1" text-anchor="middle" x="10" y="5.7">TAXI</text>
            </g>
        </g>

        <!-- Points -->
        <!-- Delhi (Start/End) -->
        <g transform="translate(180, 140)">
            <circle cx="0" cy="0" r="12" fill="#fff" stroke="url(#startEndGrad)" stroke-width="3" filter="url(#pinShadow)"/>
            <circle cx="0" cy="0" r="5" fill="url(#startEndGrad)">
                <animate attributeName="r" values="5;7;5" dur="2s" repeatCount="indefinite"/>
            </circle>
            <!-- Start / End Label above the city label -->
            <rect fill="#1a1208" filter="url(#labelShadow)" height="20" rx="4" width="90" x="-45" y="-55"/>
            <text fill="#fff" font-family="Outfit,sans-serif" font-size="10" font-weight="600" letter-spacing="1" text-anchor="middle" x="0" y="-41">START / END</text>
            
            <rect fill="#fff" filter="url(#labelShadow)" height="26" rx="4" width="80" x="-40" y="-30"/>
            <text fill="#1a1208" font-family="Cinzel,serif" font-size="12" font-weight="700" text-anchor="middle" x="0" y="-13">New Delhi</text>
        </g>
        
        <!-- Agra -->
        <g transform="translate(480, 220)">
            <circle cx="0" cy="0" r="8" fill="#fff" stroke="#A67C31" stroke-width="4" filter="url(#pinShadow)"/>
            <circle cx="0" cy="0" r="3" fill="#A67C31"/>
            <rect fill="#fff" filter="url(#labelShadow)" height="26" rx="4" width="60" x="-30" y="-35"/>
            <text fill="#1a1208" font-family="Cinzel,serif" font-size="12" font-weight="700" text-anchor="middle" x="0" y="-18">Agra</text>
        </g>

        <!-- Jaipur -->
        <g transform="translate(220, 360)">
            <circle cx="0" cy="0" r="8" fill="#fff" stroke="#A67C31" stroke-width="4" filter="url(#pinShadow)"/>
            <circle cx="0" cy="0" r="3" fill="#A67C31"/>
            <rect fill="#fff" filter="url(#labelShadow)" height="26" rx="4" width="70" x="-35" y="15"/>
            <text fill="#1a1208" font-family="Cinzel,serif" font-size="12" font-weight="700" text-anchor="middle" x="0" y="32">Jaipur</text>
        </g>
    </svg>
    """
    svg_map.replace_with(BeautifulSoup(new_svg, 'html.parser').svg)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))
