with open('delhi-travel-guide.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_header = """    <!-- ══ HEADER (same as other pages) ══ -->
    <header class="main-header" id="mainHeader">
        <div class="header-inner container">
            <a href="index.html" class="logo" id="site-logo">
                <span class="logo-accent">THE</span>
                <span class="logo-main">GRAND HOLIDAYS</span>
                <span class="logo-sub">LUXURY TOUR CO.</span>
            </a>
            <nav class="main-nav" id="mainNav">
                <ul class="nav-list">
                    <li><a href="index.html" class="nav-link">Home</a></li>
                    <li class="nav-item-dropdown">
                        <a href="all-tours.html" class="nav-link">Tours <span class="nav-caret">▾</span></a>
                        <div class="dropdown-menu">
                            <a href="golden-triangle.html" class="dropdown-item">Golden Triangle Tour</a>
                            <a href="imperial-rajasthan.html" class="dropdown-item">Imperial Rajasthan Tour</a>
                            <a href="himalayan-sanctuary.html" class="dropdown-item">Himalayan Sanctuary</a>
                            <a href="marwar-tour.html" class="dropdown-item">Marwar Heritage Tour</a>
                            <a href="rajasthan-heritage.html" class="dropdown-item">Rajasthan Heritage</a>
                            <a href="rajasthan-desert-adventure.html" class="dropdown-item">Rajasthan Desert Adventure</a>
                            <a href="himachal-exotic-tour.html" class="dropdown-item">Himachal Exotic Tour</a>
                            <a href="tiger-tour-jaipur.html" class="dropdown-item">Tiger Tour With Jaipur</a>
                            <a href="all-tours.html" class="dropdown-item" style="font-weight:700; color:var(--gold);">View All Tours →</a>
                        </div>
                    </li>
                    <li><a href="train-booking.html" class="nav-link">Train Booking</a></li>
                    <li><a href="car-booking.html" class="nav-link">Car Hire</a></li>
                    <li><a href="contact.html" class="nav-link">Contact</a></li>
                </ul>
            </nav>
            <button class="btn btn-primary btn-nav" id="openModalBtn">Plan My Trip</button>
            <button class="hamburger" id="hamburgerBtn" aria-label="Open menu">
                <span></span><span></span><span></span>
            </button>
        </div>
    </header>"""

new_header = """    <header class="site-header" id="siteHeader">
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

html = html.replace(old_header, new_header)

with open('delhi-travel-guide.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Header replaced")
