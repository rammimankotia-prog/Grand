with open('delhi-travel-guide.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_header = """    <header class="site-header" id="siteHeader">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-accent">THE</span>
                <span class="logo-main">GRAND HOLIDAYS</span>
                <span class="logo-sub">LUXURY TOUR CO.</span>
            </a>
            <nav class="nav-menu">
                <a href="index.html" class="nav-link">Home</a>
                <a href="about.html" class="nav-link">About Us</a>
                <div class="nav-dropdown">
                    <a href="all-tours.html" class="nav-link dropdown-toggle">Our Tours <span class="arrow">▼</span></a>
                    <div class="dropdown-menu">
                        <a href="golden-triangle.html" class="dropdown-item">Golden Triangle Tour</a>
                        <a href="imperial-rajasthan.html" class="dropdown-item">Imperial Rajasthan Tour</a>
                        <a href="himalayan-sanctuary.html" class="dropdown-item">Himalayan Sanctuary</a>
                        <a href="marwar-tour.html" class="dropdown-item">Marwar Heritage Tour</a>
                        <a href="rajasthan-heritage-tour.html" class="dropdown-item">Rajasthan Heritage Tour</a>
                        <a href="rajasthan-desert-adventure.html" class="dropdown-item">Rajasthan Desert Adventure</a>
                        <a href="himachal-exotic-tour.html" class="dropdown-item">Himachal Exotic Tour</a>
                        <a href="tiger-tour-jaipur.html" class="dropdown-item">Tiger Tour With Jaipur</a>
                        <a href="all-tours.html" class="dropdown-item" style="font-weight:700;">View All Tours →</a>
                    </div>
                </div>
                <a href="train-booking.html" class="nav-link">Train Booking</a>
                <a href="car-booking.html" class="nav-link">Car Hire</a>
                <a href="contact.html" class="nav-link">Contact Us</a>
            </nav>
            <div class="nav-actions">
                <div class="header-contact-info">
                    <a href="tel:+918860081995" class="header-contact-link">📞 +91 8860081995</a>
                </div>
                <a href="contact.html" class="btn btn-outline btn-nav">Plan My Trip</a>
            </div>
        </div>
    </header>"""

new_header = """    <!-- Top Glow Accent -->
    <div class="top-glow"></div>

    <!-- Floating Navigation Bar -->
    <header class="main-header scrolled">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-accent">THE</span>
                <span class="logo-main">GRAND HOLIDAYS</span>
                <span class="logo-sub">LUXURY TOUR CO.</span>
            </a>
            
            <nav class="nav-menu">
                <a href="index.html" class="nav-link">Home</a>
                <a href="about.html" class="nav-link">About Us</a>
                <div class="nav-dropdown">
                    <a href="#" class="nav-link dropdown-toggle">Our Tours <span class="arrow">▼</span></a>
                    <div class="dropdown-menu">
                        <a href="golden-triangle.html" class="dropdown-item">Golden Triangle Tour</a>
                        <a href="delhi-sightseeing.html" class="dropdown-item">Delhi Sightseeing Tour</a>
                        <a href="delhi-food-tour.html" class="dropdown-item">Delhi Food & Spice Tour</a>
                        <a href="delhi-spiritual-tour.html" class="dropdown-item">Delhi Spiritual & Temple Tour</a>
                        <a href="delhi-bicycle-tour.html" class="dropdown-item">New Delhi Bicycle Tour</a>
                        <a href="agra-day-tour.html" class="dropdown-item">Same Day Agra Tour</a>
                        <a href="himalayan-sanctuary.html" class="dropdown-item">Himalayan Sanctuary</a>
                        <a href="imperial-rajasthan.html" class="dropdown-item">Imperial Rajasthan Tour</a>
                        <a href="himachal-exotic-tour.html" class="dropdown-item">Himachal Exotic Tour</a>
                        <a href="tiger-tour-jaipur.html" class="dropdown-item">Tiger Tour With Jaipur</a>
                        <a href="all-tours.html" class="dropdown-item" style="font-weight:700;">View All Tours →</a>
                    </div>
                </div>
                <a href="contact.html" class="nav-link">Contact Us</a>
            </nav>
            
            <div class="nav-actions">
                <div class="header-contact-info">
                    <a href="tel:+918860081995" class="header-contact-link">📞 +91 8860081995</a>
                </div>
                <a href="contact.html" class="btn btn-outline btn-nav">Plan My Trip</a>
            </div>
        </div>
    </header>"""

if old_header in html:
    html = html.replace(old_header, new_header)
    print("Header replaced successfully")
else:
    print("Header not found as expected - checking...")
    # Try a simpler replace finding the site-header tag
    import re
    html = re.sub(r'<header class="site-header".*?</header>', new_header, html, count=1, flags=re.DOTALL)
    print("Used regex replace")

with open('delhi-travel-guide.html', 'w', encoding='utf-8') as f:
    f.write(html)
