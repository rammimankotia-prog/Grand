"""
update_headers_footers.py
Standardizes the header (nav + mega-menu) and footer across every HTML page
on the Grand Holidays website.
"""

import os
import re

SITE_DIR = r"c:\xampp\htdocs\Grand"

# ─────────────────────────────────────────────────────────────────────────────
# CANONICAL HEADER  (non-home pages: "scrolled" class, link-based Enquire Now)
# ─────────────────────────────────────────────────────────────────────────────
HEADER_NON_HOME = """\
<header class="main-header scrolled">
<div class="nav-container">
<a href="index.html" class="logo">
<span class="logo-accent">THE</span>
<span class="logo-main">GRAND HOLIDAYS</span>
<span class="logo-sub">( Unit of Godwin Hotels Delhi )</span>
</a>
<nav class="nav-menu" id="navMenu">
<a href="index.html" class="nav-link">Home</a>
<a href="about.html" class="nav-link">About Us</a>
<div class="nav-dropdown">
<a href="#" class="nav-link dropdown-toggle">Our Tours <span class="arrow">&#9660;</span></a>
<div class="dropdown-menu mega-menu">
<div class="mega-menu-inner">
<div class="mega-col">
<div class="mega-col-header"><span class="mega-col-icon">&#9670;</span> Golden Triangle</div>
<a class="dropdown-item" href="4-days-golden-triangle-tour.html">
<span class="item-icon">&#127963;&#65039;</span>
<span class="item-text"><span class="item-name">4 Days Golden Triangle</span><span class="item-sub">Delhi &middot; Agra &middot; Jaipur</span></span>
</a>
<a class="dropdown-item" href="5-days-golden-triangle-tour.html">
<span class="item-icon">&#128332;</span>
<span class="item-text"><span class="item-name">5 Days Golden Triangle</span><span class="item-sub">Delhi &middot; Agra &middot; Jaipur</span></span>
</a>
<a class="dropdown-item" href="8-days-golden-triangle-tour.html">
<span class="item-icon">&#11088;</span>
<span class="item-text"><span class="item-name">8 Days Golden Triangle</span><span class="item-sub">Delhi &middot; Agra &middot; Jaipur</span></span>
</a>
<a class="dropdown-item" href="8-days-golden-triangle-varanasi-tour.html">
<span class="item-icon">&#128725;</span>
<span class="item-text"><span class="item-name">8 Days with Varanasi</span><span class="item-sub">Golden Triangle + Varanasi</span></span>
</a>
</div>
<div class="mega-col-divider"></div>
<div class="mega-col">
<div class="mega-col-header"><span class="mega-col-icon">&#9670;</span> Delhi &amp; Agra</div>
<a class="dropdown-item" href="delhi-sightseeing.html">
<span class="item-icon">&#127983;&#65039;</span>
<span class="item-text"><span class="item-name">Delhi Sightseeing</span><span class="item-sub">Red Fort &middot; Qutub &middot; India Gate</span></span>
</a>
<a class="dropdown-item" href="italian-food-tour-new-delhi.html">
<span class="item-icon">&#127837;</span>
<span class="item-text"><span class="item-name">Italian Food Tour Delhi</span><span class="item-sub">Trattoria &middot; Delish Mama</span></span>
</a>
<a class="dropdown-item" href="delhi-food-tour.html">
<span class="item-icon">&#127835;</span>
<span class="item-text"><span class="item-name">Delhi Food &amp; Spice Tour</span><span class="item-sub">Chandni Chowk &middot; Street Food</span></span>
</a>
<a class="dropdown-item" href="delhi-spiritual-tour.html">
<span class="item-icon">&#128591;</span>
<span class="item-text"><span class="item-name">Delhi Spiritual Tour</span><span class="item-sub">Temples &middot; Gurudwaras &middot; Shrines</span></span>
</a>
<a class="dropdown-item" href="delhi-bicycle-tour.html">
<span class="item-icon">&#128692;</span>
<span class="item-text"><span class="item-name">Delhi Bicycle Tour</span><span class="item-sub">Old Delhi &middot; Heritage Lanes</span></span>
</a>
<a class="dropdown-item" href="delhi-tuk-tuk-tour.html">
<span class="item-icon">&#128698;</span>
<span class="item-text"><span class="item-name">Delhi Tuk Tuk Tour</span><span class="item-sub">Iconic Delhi Experience</span></span>
</a>
<a class="dropdown-item" href="delhi-museum-tour.html">
<span class="item-icon">&#127912;</span>
<span class="item-text"><span class="item-name">Delhi Museum Tour</span><span class="item-sub">National Museum &middot; Crafts</span></span>
</a>
<a class="dropdown-item" href="taj-mahal-sunrise-tour.html">
<span class="item-icon">&#127749;</span>
<span class="item-text"><span class="item-name">Taj Mahal Sunrise Tour</span><span class="item-sub">Express Entry &middot; Skip the Line</span></span>
</a>
<a class="dropdown-item" href="agra-day-tour.html">
<span class="item-icon">&#128717;</span>
<span class="item-text"><span class="item-name">Same Day Agra Tour</span><span class="item-sub">Taj Mahal &middot; Agra Fort</span></span>
</a>
<a class="dropdown-item" href="delhi-agra-2-day-tour.html">
<span class="item-icon">&#127749;</span>
<span class="item-text"><span class="item-name">2-Day Taj Mahal &amp; Delhi</span><span class="item-sub">Overnight &middot; Sunrise Taj Mahal</span></span>
</a>
</div>
<div class="mega-col-divider"></div>
<div class="mega-col">
<div class="mega-col-header"><span class="mega-col-icon">&#9670;</span> Rajasthan</div>
<a class="dropdown-item" href="imperial-rajasthan.html">
<span class="item-icon">&#128081;</span>
<span class="item-text"><span class="item-name">Imperial Rajasthan</span><span class="item-sub">Jaipur &middot; Jodhpur &middot; Udaipur</span></span>
</a>
<a class="dropdown-item" href="rajasthan-heritage-tour.html">
<span class="item-icon">&#127984;&#65039;</span>
<span class="item-text"><span class="item-name">Rajasthan Heritage Tour</span><span class="item-sub">Forts &middot; Palaces &middot; Stepwells</span></span>
</a>
<a class="dropdown-item" href="marvellous-marwar-tour.html">
<span class="item-icon">&#127748;</span>
<span class="item-text"><span class="item-name">Marvellous Marwar Tour</span><span class="item-sub">Jodhpur &middot; Jaisalmer &middot; Bikaner</span></span>
</a>
<a class="dropdown-item" href="rajasthan-desert-adventure.html">
<span class="item-icon">&#128042;</span>
<span class="item-text"><span class="item-name">Desert Adventure</span><span class="item-sub">Camel Safari &middot; Desert Camps</span></span>
</a>
<a class="dropdown-item" href="tiger-tour-jaipur.html">
<span class="item-icon">&#128047;</span>
<span class="item-text"><span class="item-name">Tiger Tour With Jaipur</span><span class="item-sub">Ranthambore Safari &middot; Jaipur</span></span>
</a>
<a class="dropdown-item" href="ranthambore-tiger-safari.html">
<span class="item-icon">&#127807;</span>
<span class="item-text"><span class="item-name">Ranthambore Tiger Safari</span><span class="item-sub">3 Days &middot; Delhi to Ranthambore</span></span>
</a>
<div class="mega-col-header" style="margin-top:1rem;"><span class="mega-col-icon">&#9670;</span> Himalayas &amp; Spiritual</div>
<a class="dropdown-item" href="himachal-exotic-tour.html">
<span class="item-icon">&#127956;&#65039;</span>
<span class="item-text"><span class="item-name">Himachal Exotic Tour</span><span class="item-sub">Shimla &middot; Manali &middot; Spiti</span></span>
</a>
<a class="dropdown-item" href="himalayan-sanctuary.html">
<span class="item-icon">&#127807;</span>
<span class="item-text"><span class="item-name">Himalayan Sanctuary</span><span class="item-sub">Rishikesh &middot; Haridwar &middot; Yoga</span></span>
</a>
<a class="dropdown-item" href="haridwar-rishikesh-tour.html">
<span class="item-icon">&#128567;</span>
<span class="item-text"><span class="item-name">Haridwar &amp; Rishikesh</span><span class="item-sub">Ganga Aarti &middot; Yoga &middot; Adventure</span></span>
</a>
</div>
</div>
</div>
</div>
<a href="contact.html" class="nav-link">Contact Us</a>
</nav>
<div class="nav-actions">
<div class="header-contact-info">
<a href="tel:+918860081995" class="header-contact-link">&#128222; +91 8860081995</a>
</div>
<button class="mobile-nav-toggle" id="menuToggle" aria-label="Toggle navigation">
<span class="bar"></span>
<span class="bar"></span>
<span class="bar"></span>
</button>
</div>
</div>
</header>"""

# ─────────────────────────────────────────────────────────────────────────────
# CANONICAL HEADER  (HOME PAGE: index.html — modal button, id="mainHeader")
# ─────────────────────────────────────────────────────────────────────────────
HEADER_HOME = """\
<header class="main-header" id="mainHeader">
<div class="nav-container">
<a class="logo" href="index.html" id="logoLink">
<span class="logo-accent">THE</span>
<span class="logo-main">GRAND HOLIDAYS</span>
<span class="logo-sub">( Unit of Godwin Hotels Delhi )</span>
</a>
<nav class="nav-menu" id="navMenu">
<a class="nav-link active" href="index.html">Home</a>
<a class="nav-link" href="about.html">About Us</a>
<div class="nav-dropdown">
<a class="nav-link dropdown-toggle" href="#">Our Tours <span class="arrow">&#9660;</span></a>
<div class="dropdown-menu mega-menu">
<div class="mega-menu-inner">
<div class="mega-col">
<div class="mega-col-header"><span class="mega-col-icon">&#9670;</span> Golden Triangle</div>
<a class="dropdown-item" href="4-days-golden-triangle-tour.html">
<span class="item-icon">&#127963;&#65039;</span>
<span class="item-text"><span class="item-name">4 Days Golden Triangle</span><span class="item-sub">Delhi &middot; Agra &middot; Jaipur</span></span>
</a>
<a class="dropdown-item" href="5-days-golden-triangle-tour.html">
<span class="item-icon">&#128332;</span>
<span class="item-text"><span class="item-name">5 Days Golden Triangle</span><span class="item-sub">Delhi &middot; Agra &middot; Jaipur</span></span>
</a>
<a class="dropdown-item" href="8-days-golden-triangle-tour.html">
<span class="item-icon">&#11088;</span>
<span class="item-text"><span class="item-name">8 Days Golden Triangle</span><span class="item-sub">Delhi &middot; Agra &middot; Jaipur</span></span>
</a>
<a class="dropdown-item" href="8-days-golden-triangle-varanasi-tour.html">
<span class="item-icon">&#128725;</span>
<span class="item-text"><span class="item-name">8 Days with Varanasi</span><span class="item-sub">Golden Triangle + Varanasi</span></span>
</a>
</div>
<div class="mega-col-divider"></div>
<div class="mega-col">
<div class="mega-col-header"><span class="mega-col-icon">&#9670;</span> Delhi &amp; Agra</div>
<a class="dropdown-item" href="delhi-sightseeing.html">
<span class="item-icon">&#127983;&#65039;</span>
<span class="item-text"><span class="item-name">Delhi Sightseeing</span><span class="item-sub">Red Fort &middot; Qutub &middot; India Gate</span></span>
</a>
<a class="dropdown-item" href="italian-food-tour-new-delhi.html">
<span class="item-icon">&#127837;</span>
<span class="item-text"><span class="item-name">Italian Food Tour Delhi</span><span class="item-sub">Trattoria &middot; Delish Mama</span></span>
</a>
<a class="dropdown-item" href="delhi-food-tour.html">
<span class="item-icon">&#127835;</span>
<span class="item-text"><span class="item-name">Delhi Food &amp; Spice Tour</span><span class="item-sub">Chandni Chowk &middot; Street Food</span></span>
</a>
<a class="dropdown-item" href="delhi-spiritual-tour.html">
<span class="item-icon">&#128591;</span>
<span class="item-text"><span class="item-name">Delhi Spiritual Tour</span><span class="item-sub">Temples &middot; Gurudwaras &middot; Shrines</span></span>
</a>
<a class="dropdown-item" href="delhi-bicycle-tour.html">
<span class="item-icon">&#128692;</span>
<span class="item-text"><span class="item-name">Delhi Bicycle Tour</span><span class="item-sub">Old Delhi &middot; Heritage Lanes</span></span>
</a>
<a class="dropdown-item" href="delhi-tuk-tuk-tour.html">
<span class="item-icon">&#128698;</span>
<span class="item-text"><span class="item-name">Delhi Tuk Tuk Tour</span><span class="item-sub">Iconic Delhi Experience</span></span>
</a>
<a class="dropdown-item" href="delhi-museum-tour.html">
<span class="item-icon">&#127912;</span>
<span class="item-text"><span class="item-name">Delhi Museum Tour</span><span class="item-sub">National Museum &middot; Crafts</span></span>
</a>
<a class="dropdown-item" href="taj-mahal-sunrise-tour.html">
<span class="item-icon">&#127749;</span>
<span class="item-text"><span class="item-name">Taj Mahal Sunrise Tour</span><span class="item-sub">Express Entry &middot; Skip the Line</span></span>
</a>
<a class="dropdown-item" href="agra-day-tour.html">
<span class="item-icon">&#128717;</span>
<span class="item-text"><span class="item-name">Same Day Agra Tour</span><span class="item-sub">Taj Mahal &middot; Agra Fort</span></span>
</a>
<a class="dropdown-item" href="delhi-agra-2-day-tour.html">
<span class="item-icon">&#127749;</span>
<span class="item-text"><span class="item-name">2-Day Taj Mahal &amp; Delhi</span><span class="item-sub">Overnight &middot; Sunrise Taj Mahal</span></span>
</a>
</div>
<div class="mega-col-divider"></div>
<div class="mega-col">
<div class="mega-col-header"><span class="mega-col-icon">&#9670;</span> Rajasthan</div>
<a class="dropdown-item" href="imperial-rajasthan.html">
<span class="item-icon">&#128081;</span>
<span class="item-text"><span class="item-name">Imperial Rajasthan</span><span class="item-sub">Jaipur &middot; Jodhpur &middot; Udaipur</span></span>
</a>
<a class="dropdown-item" href="rajasthan-heritage-tour.html">
<span class="item-icon">&#127984;&#65039;</span>
<span class="item-text"><span class="item-name">Rajasthan Heritage Tour</span><span class="item-sub">Forts &middot; Palaces &middot; Stepwells</span></span>
</a>
<a class="dropdown-item" href="marvellous-marwar-tour.html">
<span class="item-icon">&#127748;</span>
<span class="item-text"><span class="item-name">Marvellous Marwar Tour</span><span class="item-sub">Jodhpur &middot; Jaisalmer &middot; Bikaner</span></span>
</a>
<a class="dropdown-item" href="rajasthan-desert-adventure.html">
<span class="item-icon">&#128042;</span>
<span class="item-text"><span class="item-name">Desert Adventure</span><span class="item-sub">Camel Safari &middot; Desert Camps</span></span>
</a>
<a class="dropdown-item" href="tiger-tour-jaipur.html">
<span class="item-icon">&#128047;</span>
<span class="item-text"><span class="item-name">Tiger Tour With Jaipur</span><span class="item-sub">Ranthambore Safari &middot; Jaipur</span></span>
</a>
<a class="dropdown-item" href="ranthambore-tiger-safari.html">
<span class="item-icon">&#127807;</span>
<span class="item-text"><span class="item-name">Ranthambore Tiger Safari</span><span class="item-sub">3 Days &middot; Delhi to Ranthambore</span></span>
</a>
<div class="mega-col-header" style="margin-top:1rem;"><span class="mega-col-icon">&#9670;</span> Himalayas &amp; Spiritual</div>
<a class="dropdown-item" href="himachal-exotic-tour.html">
<span class="item-icon">&#127956;&#65039;</span>
<span class="item-text"><span class="item-name">Himachal Exotic Tour</span><span class="item-sub">Shimla &middot; Manali &middot; Spiti</span></span>
</a>
<a class="dropdown-item" href="himalayan-sanctuary.html">
<span class="item-icon">&#127807;</span>
<span class="item-text"><span class="item-name">Himalayan Sanctuary</span><span class="item-sub">Rishikesh &middot; Haridwar &middot; Yoga</span></span>
</a>
<a class="dropdown-item" href="haridwar-rishikesh-tour.html">
<span class="item-icon">&#128567;</span>
<span class="item-text"><span class="item-name">Haridwar &amp; Rishikesh</span><span class="item-sub">Ganga Aarti &middot; Yoga &middot; Adventure</span></span>
</a>
</div>
</div>
</div>
</div>
<a class="nav-link" href="contact.html">Contact</a>
</nav>
<div class="nav-actions">
<div class="header-contact-info">
<a class="header-contact-link" href="tel:+918860081995">&#128222; +91 8860081995</a>
</div>
<button aria-label="Toggle navigation" class="mobile-nav-toggle" id="menuToggle">
<span class="bar"></span>
<span class="bar"></span>
<span class="bar"></span>
</button>
</div>
</div>
</header>"""

# ─────────────────────────────────────────────────────────────────────────────
# CANONICAL FOOTER  (same for all pages)
# ─────────────────────────────────────────────────────────────────────────────
FOOTER_CANONICAL = """\
<footer class="luxury-footer">
<div class="container">
<div class="footer-top">
<div class="footer-brand">
<a class="logo" href="index.html">
<span class="logo-accent">THE</span>
<span class="logo-main">GRAND HOLIDAYS</span>
<span class="logo-sub">( Unit of Godwin Hotels Delhi )</span>
</a>
<p class="footer-desc">A bespoke luxury travel operator creating timeless, deeply personal journeys across the Indian subcontinent since 2011.</p>
<p class="footer-desc" style="margin-top: 1.2rem; opacity: 0.8; font-size: 0.8rem; line-height: 1.5;">
<strong>Grand Holidays Office</strong><br/>
Plot No. 8502/41, Ground Floor, Arakashan Rd,<br/>
behind Sheela Cinema Street, Ram Nagar,<br/>
Paharganj, New Delhi, Delhi 110055
</p>
</div>
<div class="footer-links-col">
<h4>Explore</h4>
<a href="all-tours.html">All Tours</a>
<a href="train-booking.html">Book Train Tickets</a>
<a href="car-booking.html">Book Private Car</a>
<a href="about.html">About Us</a>
<a href="contact.html">Contact</a>
<a href="delhi-travel-guide.html">Delhi Travel Guide</a>
</div>
<div class="footer-links-col">
<h4>Our Tours</h4>
<a href="4-days-golden-triangle-tour.html">Golden Triangle 4 Days</a>
<a href="delhi-sightseeing.html">Delhi Sightseeing</a>
<a href="agra-day-tour.html">Same Day Agra Tour</a>
<a href="imperial-rajasthan.html">Imperial Rajasthan</a>
<a href="ranthambore-tiger-safari.html">Ranthambore Safari</a>
<a href="haridwar-rishikesh-tour.html">Haridwar &amp; Rishikesh</a>
</div>
<div class="footer-links-col">
<h4>Newsletter</h4>
<p>Subscribe for curated itineraries and rare travel discoveries.</p>
<form class="footer-newsletter" id="newsletterForm">
<input class="newsletter-input" id="newsletterEmail" placeholder="Your email address" required="" type="email"/>
<button class="btn-newsletter-submit" type="submit">&#8594;</button>
</form>
<span class="newsletter-success" id="newsletterSuccess">Subscribed successfully. &#10003;</span>
</div>
</div>
<div class="footer-bottom">
<p>&#169; 2026 Grand Holidays ( Unit of Godwin Hotels Delhi ). All rights reserved.<br/>
<span style="opacity: 0.8; font-size: 0.9em;">Unit of <a href="https://godwinhotels.com/" rel="noopener noreferrer" style="color: inherit; text-decoration: underline; text-underline-offset: 3px;" target="_blank">Godwin Hotels Delhi</a></span></p>
<div class="footer-legal">
<a href="privacy.html">Privacy Policy</a>
<span class="bullet">&#8226;</span>
<a href="terms.html">Terms of Service</a>
</div>
</div>
</div>
</footer>"""

# ─────────────────────────────────────────────────────────────────────────────
# PAGES TO PROCESS
# ─────────────────────────────────────────────────────────────────────────────
SKIP_FILES = {"googled60501e34605346d.html"}

def get_html_files():
    files = []
    for f in os.listdir(SITE_DIR):
        if f.endswith(".html") and f not in SKIP_FILES:
            files.append(f)
    files.sort()
    return files

def replace_block(content, pattern, replacement):
    """Replace first match of pattern (DOTALL) with replacement."""
    new_content, count = re.subn(pattern, replacement, content, count=1, flags=re.DOTALL | re.IGNORECASE)
    return new_content, count

def process_file(filename):
    filepath = os.path.join(SITE_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    is_home = (filename == "index.html")

    # ── Replace HEADER ────────────────────────────────────────────────────────
    header_pattern = r'<header\b[^>]*>.*?</header>'
    header_replacement = HEADER_HOME if is_home else HEADER_NON_HOME
    content, h_count = replace_block(content, header_pattern, header_replacement)

    # ── Replace FOOTER ────────────────────────────────────────────────────────
    footer_pattern = r'<footer\b[^>]*class="luxury-footer"[^>]*>.*?</footer>'
    content, f_count = replace_block(content, footer_pattern, FOOTER_CANONICAL)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        status = []
        if h_count: status.append("header")
        if f_count: status.append("footer")
        print(f"  OK {filename}  [{', '.join(status)} updated]")
    else:
        print(f"  -- {filename}  [no changes]")

def main():
    files = get_html_files()
    print(f"\nProcessing {len(files)} HTML files in: {SITE_DIR}\n")
    for f in files:
        process_file(f)
    print("\nDone.")

if __name__ == "__main__":
    main()
