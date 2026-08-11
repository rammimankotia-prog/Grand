import re

with open('8-hours-sightseeing-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update City Cards
new_city_cards = """<div class="gt-city-cards">
                    <div class="gt-city-card">
                        <div class="city-card-num">01</div>
                        <div class="city-card-icon">&#127983;</div>
                        <h3 class="city-card-name">Old Delhi</h3>
                        <p class="city-card-desc">The historic heart of the capital &mdash; navigate the bustling lanes of Chandni Chowk and witness Mughal architectural marvels.</p>
                        <div class="city-card-tags"><span>Red Fort</span><span>Jama Masjid</span><span>Chandni Chowk</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">02</div>
                        <div class="city-card-icon">&#127963;&#65039;</div>
                        <h3 class="city-card-name">New Delhi</h3>
                        <p class="city-card-desc">The imperial center &mdash; drive past the grand colonial-era monuments and pay homage to India's soldiers at the iconic arch.</p>
                        <div class="city-card-tags"><span>India Gate</span><span>Parliament House</span><span>President's Estate</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">03</div>
                        <div class="city-card-icon">&#127984;</div>
                        <h3 class="city-card-name">South Delhi</h3>
                        <p class="city-card-desc">Where ancient meets modern &mdash; explore UNESCO World Heritage sites and stunning modern temples of peace.</p>
                        <div class="city-card-tags"><span>Qutub Minar</span><span>Lotus Temple</span><span>Hauz Khas</span></div>
                    </div>
                </div>"""

html = re.sub(r'<div class="gt-city-cards">.*?</div>\s*</div>\s*</div>\s*</section>', new_city_cards + '\n            </div>\n        </div>\n    </section>', html, flags=re.DOTALL)


# 2. Update FAQ Section
new_faq_section = """<!-- FAQ Section -->
    <section class="faq-section" id="faq">
        <div class="container">
            <div class="faq-header">
                <span class="eyebrow">Common Questions</span>
                <h2>Frequently Asked Questions</h2>
                <p>Everything you need to know about the Delhi Sightseeing Tour by Tempo Traveller.</p>
            </div>
            <div class="faq-grid" id="faq-grid-gt">
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">What places will we visit during the 8-hour Delhi sightseeing tour?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>You will explore major landmarks including the Red Fort, Jama Masjid, India Gate, Parliament House, Lotus Temple, and Qutub Minar. Our itinerary is flexible, allowing you to spend more time at your favorite spots.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">Is the Tempo Traveller air-conditioned and comfortable?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>Yes, all our Tempo Travellers are fully air-conditioned, spacious, well-maintained, and equipped with comfortable push-back seats. It's the perfect vehicle for families and groups of up to 16 people traveling together.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">Are monument entry tickets and meals included in the package?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>No, the package exclusively covers the Tempo Traveller rental, a professional English-speaking driver, fuel, and local toll charges. Monument entry fees, camera charges, and meals are excluded so you can customize your experience.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">Can we customise the itinerary or extend the time limit?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>Absolutely! The standard package covers 8 hours and 80 kilometres within Delhi. If you wish to extend the time, travel further, or visit specific spots like Akshardham Temple, it can be seamlessly arranged subject to nominal extra charges per kilometre/hour.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">Where will we be picked up and dropped off?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>We offer convenient, door-to-door service. You can specify any pick-up and drop-off location within Delhi NCR limits, whether it's your hotel, residence, or the airport.</p></div></div>
                </div>
            </div>
        </div>
    </section>"""

html = re.sub(r'<!-- FAQ Section -->.*?<section class="faq-section".*?</section>', new_faq_section, html, flags=re.DOTALL)

with open('8-hours-sightseeing-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
