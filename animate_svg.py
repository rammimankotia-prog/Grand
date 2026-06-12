from bs4 import BeautifulSoup

file_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo/delhi-museum-tour.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

svg = soup.find('svg', class_='gt-svg')
if svg:
    new_svg_str = '''
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
    </defs>
    
    <rect fill="url(#bgG)" height="100%" rx="16" width="100%"/>
    
    <!-- Compass -->
    <g transform="translate(40,40) scale(0.8)">
        <circle cx="0" cy="0" fill="none" r="16" stroke="#b0a090" stroke-width="1"/>
        <path d="M0 -22 L4 -6 L22 0 L4 6 L0 22 L-4 6 L-22 0 L-4 -6 Z" fill="#d4c4b4"/>
        <path d="M0 -22 L4 -6 L0 0 L-4 -6 Z" fill="#A67C31"/>
        <text fill="#a67c31" font-family="Outfit,sans-serif" font-size="10" font-weight="800" text-anchor="middle" x="0" y="-27">N</text>
    </g>

    <!-- Map Title -->
    <text fill="#b0a090" font-family="Outfit,sans-serif" font-size="14" font-weight="600" letter-spacing="3" text-anchor="middle" x="340" y="60">DELHI MUSEUM CIRCUIT</text>

    <!-- Circuit Path (Closed loop from Godwin Deluxe) -->
    <path id="route-path" d="M 160 140 Q 180 240 260 320 T 420 360 T 560 220 Q 400 80 160 140" fill="none" stroke="url(#lineGrad)" stroke-dasharray="8 6" stroke-linecap="round" stroke-width="3">
        <animate attributeName="stroke-dashoffset" dur="4s" from="0" repeatCount="indefinite" to="-140"></animate>
    </path>
    
    <!-- Moving Taxi Sedan along route -->
    <g>
        <animateMotion dur="12s" repeatCount="indefinite" rotate="auto">
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
            <!-- Headlights (Front, facing right) -->
            <rect fill="#fef08a" height="1.5" width="1.5" x="19" y="1.5"></rect>
            <rect fill="#fef08a" height="1.5" width="1.5" x="19" y="7"></rect>
            <!-- Tail lights -->
            <rect fill="#ef4444" height="1.5" width="1" x="0" y="1.5"></rect>
            <rect fill="#ef4444" height="1.5" width="1" x="0" y="7"></rect>
            <!-- Windshields -->
            <path d="M12 1.5 L15 2.5 L15 7.5 L12 8.5 Z" fill="#38bdf8"></path>
            <path d="M6 1.5 L3 2.5 L3 7.5 L6 8.5 Z" fill="#38bdf8"></path>
            <rect fill="#38bdf8" height="7" width="4" x="7.5" y="1.5"></rect>
            <!-- TAXI text on roof -->
            <rect fill="#fff" height="3" rx="0.5" width="8" x="6" y="3.5"></rect>
            <text fill="#000" font-family="Outfit, sans-serif" font-size="2.2" font-weight="900" letter-spacing="0.1" text-anchor="middle" x="10" y="5.7">TAXI</text>
        </g>
    </g>

    <!-- Distance Markers -->
    <!-- Godwin to National -->
    <g transform="translate(180, 230)">
        <rect fill="#fff" rx="8" width="50" height="18" x="-25" y="-9" stroke="#d4c4b4" stroke-width="1"/>
        <text fill="#6b4c12" font-family="Outfit,sans-serif" font-size="9" font-weight="700" text-anchor="middle" x="0" y="3">5 KM</text>
    </g>
    <!-- National to Rail -->
    <g transform="translate(340, 365)">
        <rect fill="#fff" rx="8" width="50" height="18" x="-25" y="-9" stroke="#d4c4b4" stroke-width="1"/>
        <text fill="#6b4c12" font-family="Outfit,sans-serif" font-size="9" font-weight="700" text-anchor="middle" x="0" y="3">6 KM</text>
    </g>
    <!-- Rail to Dolls -->
    <g transform="translate(490, 305)">
        <rect fill="#fff" rx="8" width="50" height="18" x="-25" y="-9" stroke="#d4c4b4" stroke-width="1"/>
        <text fill="#6b4c12" font-family="Outfit,sans-serif" font-size="9" font-weight="700" text-anchor="middle" x="0" y="3">9 KM</text>
    </g>
    <!-- Dolls to Godwin -->
    <g transform="translate(360, 150)">
        <rect fill="#fff" rx="8" width="50" height="18" x="-25" y="-9" stroke="#d4c4b4" stroke-width="1"/>
        <text fill="#6b4c12" font-family="Outfit,sans-serif" font-size="9" font-weight="700" text-anchor="middle" x="0" y="3">4 KM</text>
    </g>

    <!-- Point 0: Godwin Deluxe -->
    <g transform="translate(160, 140)">
        <circle cx="0" cy="0" r="10" fill="#fff" stroke="#4a90e2" stroke-width="3" filter="url(#pinShadow)"/>
        <circle cx="0" cy="0" r="4" fill="#4a90e2"/>
        <rect fill="#fff" filter="url(#labelShadow)" height="40" rx="4" width="160" x="-80" y="-55"/>
        <text fill="#1a1208" font-family="Outfit,sans-serif" font-size="9" font-weight="800" letter-spacing="1" text-anchor="middle" x="0" y="-35">TOUR STARTS &amp; ENDS</text>
        <text fill="#4a90e2" font-family="Outfit,sans-serif" font-size="11" font-weight="800" letter-spacing="1" text-anchor="middle" x="0" y="-20">GODWIN DELUXE</text>
    </g>

    <!-- Point 1: National Museum -->
    <g transform="translate(260, 320)">
        <circle cx="0" cy="0" r="8" fill="#fff" stroke="#A67C31" stroke-width="4" filter="url(#pinShadow)"/>
        <circle cx="0" cy="0" r="3" fill="#A67C31"/>
        <rect fill="#fff" filter="url(#labelShadow)" height="26" rx="4" width="140" x="-70" y="15"/>
        <text fill="#1a1208" font-family="Cinzel,serif" font-size="12" font-weight="700" text-anchor="middle" x="0" y="32">National Museum</text>
    </g>

    <!-- Point 2: Rail Museum -->
    <g transform="translate(420, 360)">
        <circle cx="0" cy="0" r="8" fill="#fff" stroke="#A67C31" stroke-width="4" filter="url(#pinShadow)"/>
        <circle cx="0" cy="0" r="3" fill="#A67C31"/>
        <rect fill="#fff" filter="url(#labelShadow)" height="26" rx="4" width="160" x="-80" y="15"/>
        <text fill="#1a1208" font-family="Cinzel,serif" font-size="12" font-weight="700" text-anchor="middle" x="0" y="32">National Rail Museum</text>
    </g>

    <!-- Point 3: Dolls Museum -->
    <g transform="translate(560, 220)">
        <circle cx="0" cy="0" r="8" fill="#fff" stroke="#A67C31" stroke-width="4" filter="url(#pinShadow)"/>
        <circle cx="0" cy="0" r="3" fill="#A67C31"/>
        <rect fill="#fff" filter="url(#labelShadow)" height="26" rx="4" width="130" x="-65" y="-35"/>
        <text fill="#1a1208" font-family="Cinzel,serif" font-size="12" font-weight="700" text-anchor="middle" x="0" y="-18">Dolls Museum</text>
    </g>
    
    </svg>
    '''
    
    new_svg = BeautifulSoup(new_svg_str, 'html.parser').svg
    svg.replace_with(new_svg)
    
    with open(file_path, 'w', encoding='utf-8') as fw:
        fw.write(str(soup))
    print('SVG Replaced with Animated Loop!')
