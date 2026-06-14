import os
import shutil

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
source_html = os.path.join(repo_path, '8-days-golden-triangle-tour.html')
target_html = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.html')

source_js = os.path.join(repo_path, '8-days-golden-triangle-tour.js')
target_js = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.js')

source_css = os.path.join(repo_path, '8-days-golden-triangle-tour.css')
target_css = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.css')

# 1. Duplicate CSS
shutil.copy2(source_css, target_css)

# 2. Duplicate JS and modify completely
js_content = """document.addEventListener('DOMContentLoaded', () => {
    // Tour Options Database
    const tourModes = {
        flight: {
            duration: "8 Days / 7 Nights",
            cities: "Delhi - Agra - Jaipur - Varanasi",
            price: "Enquire for Price",
            shortDesc: "Experience the majestic Golden Triangle combined with the spiritual heart of India. This luxury itinerary includes private chauffeured drives and short domestic flights, allowing you to absorb India's beauty and profound spirituality at your own pace.",
            highlight: "✈️ Includes domestic flights (Jaipur - Varanasi, Varanasi - Delhi), dedicated private car for city tours, and an unforgettable sunrise boat ride on the sacred Ganges.",
            itinerary: [
                { day: 1, title: "Arrival & Welcome to Delhi", desc: "Touch down in the vibrant capital, Delhi. You will be warmly greeted at the airport and chauffeured to your luxury hotel. Take the evening to rest, relax, and prepare for the incredible journey ahead." },
                { day: 2, title: "Delhi Sightseeing: Historic Marvels", desc: "Dive into the heart of India's capital. Explore magnificent landmarks including ancient mosques, bustling heritage markets, towering historical forts, and the iconic India Gate and Qutub Minar." },
                { day: 3, title: "Delhi to Agra: The Mughal Capital", desc: "Enjoy a comfortable private drive to the historical city of Agra. After checking into your hotel, spend the afternoon exploring the massive, red-sandstone Agra Fort, a testament to the grandeur of the Mughal Empire." },
                { day: 4, title: "Sunrise at Taj Mahal & Drive to Jaipur", desc: "Witness the ethereal beauty of the Taj Mahal bathed in the soft glow of sunrise. Afterwards, embark on a scenic drive to the 'Pink City' of Jaipur, pausing en route to explore the fascinating abandoned ghost city of Fatehpur Sikri." },
                { day: 5, title: "Explore Jaipur: The Pink City", desc: "Spend the day immersed in royal Rajasthani heritage. Ascend the majestic Amber Fort, wander through the opulent City Palace, and marvel at the intricate facade of the famous Hawa Mahal (Palace of Winds)." },
                { day: 6, title: "Flight to Varanasi & Spiritual Evening", desc: "Board a short domestic flight from Jaipur to Varanasi, the spiritual capital of India. In the evening, head to the sacred riverbanks to witness the mesmerizing Ganga Aarti—a beautiful, deeply spiritual ceremony of light and chanting." },
                { day: 7, title: "Varanasi: Sunrise Boat Ride & Sarnath", desc: "Experience profound tranquility during a sunrise boat ride on the holy River Ganges. Later, walk through the ancient, labyrinthine alleys of the old city and visit Sarnath, the deeply historic site where Lord Buddha delivered his first sermon." },
                { day: 8, title: "Fly back to Delhi & Departure", desc: "Conclude your incredible spiritual and historical journey with a flight from Varanasi back to Delhi, where you will seamlessly connect to your onward flight or final destination." }
            ],
            inclusions: [
                "Pickup and drop-off at hotels and airports in Delhi",
                "7 nights accommodation in a 3, 4, or 5-star hotel (as per preference)",
                "Breakfast at Hotel",
                "Round Trip Flight Ticket (Jaipur - Varanasi | Varanasi - Delhi)",
                "All Sightseeing by private Air Conditioned Car",
                "Professional Local tour guide in each city destination",
                "Morning boat ride on the holy river Ganges in Varanasi",
                "Battery Rickshaw ride at Taj Mahal",
                "Daily Water Bottle",
                "Hotel/airport pick-up and drop-off"
            ],
            exclusions: [
                "Entrance Tickets of all Monuments",
                "Lunches and dinners",
                "Tips (optional)"
            ],
            highlightsList: [
                "Discover the major sites such as Taj Mahal and River Ganges",
                "Explore Indian culture including Jaipur and Varanasi",
                "See the amazing views of Ganga Aarti Ceremony at Varanasi",
                "On the way to Jaipur, pause in Fatehpur Sikri.",
                "Savor the bright flavors of Indian food"
            ]
        }
    };

    let currentMode = 'flight'; // Default to flight mode
    
    // Elements to update
    const displayDuration = document.getElementById('display-duration');
    const displayCities = document.getElementById('display-cities');
    const displayPrice = document.getElementById('display-price');
    const summaryPriceDisplay = document.getElementById('summary-price-display');
    const shortDesc = document.getElementById('tour-short-desc');
    const modeHighlightBox = document.getElementById('mode-highlight-box');
    const timelineBox = document.getElementById('itinerary-timeline-box');
    const inclusionsBox = document.getElementById('inclusions-list');
    const exclusionsBox = document.getElementById('exclusions-list');
    
    function renderTourData(mode) {
        const modeData = tourModes[mode];
        if (!modeData) return;

        displayDuration.innerText = modeData.duration;
        displayCities.innerText = modeData.cities;
        displayPrice.innerText = `From ${modeData.price}`;
        summaryPriceDisplay.innerText = `${modeData.price}`;
        shortDesc.innerText = modeData.shortDesc;
        
        // Render highlight block
        modeHighlightBox.innerHTML = `
            <div class="highlight-card">
                <p>${modeData.highlight}</p>
                <div style="margin-top: 15px; border-top: 1px dashed rgba(255,255,255,0.3); padding-top: 15px;">
                    <h4 style="color: #fff; font-size: 1.1rem; margin-bottom: 10px;">Highlights</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; color: rgba(255,255,255,0.95); font-size: 0.95rem;">
                        ${modeData.highlightsList.map(h => `<li style="margin-bottom: 6px; display: flex; align-items: flex-start;"><svg style="min-width: 16px; margin-right: 8px; margin-top: 4px;" fill="none" stroke="currentColor" viewBox="0 0 24 24" width="16" height="16"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>${h}</li>`).join('')}
                    </ul>
                </div>
            </div>
        `;

        // Render timeline
        timelineBox.innerHTML = modeData.itinerary.map(item => `
            <div class="timeline-item">
                <div class="timeline-marker"></div>
                <div class="timeline-content">
                    <h3 class="day-title">Day ${item.day}: ${item.title}</h3>
                    <p class="day-desc">${item.desc}</p>
                </div>
            </div>
        `).join('');

        // Render inclusions
        inclusionsBox.innerHTML = modeData.inclusions.map(inc => `
            <li>
                <svg class="inc-icon check" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                ${inc}
            </li>
        `).join('');

        // Render exclusions
        exclusionsBox.innerHTML = modeData.exclusions.map(exc => `
            <li>
                <svg class="inc-icon cross" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                ${exc}
            </li>
        `).join('');
    }

    renderTourData(currentMode);

    // Make mode switcher hidden since we only have one mode for this tour
    const modeTabs = document.querySelector('.mode-tabs');
    if (modeTabs) {
        modeTabs.style.display = 'none';
    }

    // FAQ Accordion Logic
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        question.addEventListener('click', () => {
            const answer = item.querySelector('.faq-answer');
            const isOpen = question.classList.contains('open');
            
            faqItems.forEach(i => {
                i.querySelector('.faq-question').classList.remove('open');
                i.querySelector('.faq-answer').classList.remove('open');
            });

            if (!isOpen) {
                question.classList.add('open');
                answer.classList.add('open');
            }
        });
    });
});
"""

with open(target_js, 'w', encoding='utf-8') as f:
    f.write(js_content)

# 3. Duplicate HTML and modify specific parts
with open(source_html, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace JS and CSS links
html_content = html_content.replace('8-days-golden-triangle-tour.css', '8-days-golden-triangle-varanasi-tour.css')
html_content = html_content.replace('8-days-golden-triangle-tour.js', '8-days-golden-triangle-varanasi-tour.js')

# Replace Title and Meta
html_content = html_content.replace('<title>8 Days Golden Triangle Tour | Grand Holidays</title>', '<title>8 Days Golden Triangle & Varanasi Tour | Grand Holidays</title>')
html_content = html_content.replace('Experience the majestic Golden Triangle in unparalleled luxury. A bespoke 6-day journey through Delhi, Agra (Taj Mahal), and Jaipur.', 'Experience the spiritual heart of India. A bespoke 8-day luxury journey through Delhi, Agra, Jaipur, and Varanasi, including domestic flights and private tours.')
html_content = html_content.replace('luxury golden triangle tour, Delhi Agra Jaipur tour, premium golden triangle package, Taj Mahal luxury tour', 'Golden Triangle with Varanasi luxury tour, Delhi Agra Jaipur Varanasi package, premium Varanasi Ganges tour, India spiritual tour package')
html_content = html_content.replace('https://grandholidaytours.com/8-days-golden-triangle-tour.html', 'https://grandholidaytours.com/8-days-golden-triangle-varanasi-tour.html')

# Replace Hero Title
html_content = html_content.replace('<h1 class="hero-title" id="tour-hero-title">8 Days Golden Triangle Tour</h1>', '<h1 class="hero-title" id="tour-hero-title" style="font-size: 3rem;">8 Days Golden Triangle & Varanasi Tour</h1>')

# Replace breadcrumb
html_content = html_content.replace('>8 Days Golden Triangle Tour</li>', '>8 Days Golden Triangle & Varanasi Tour</li>')

# Remove mode tabs since we only have one mode for this tour
html_content = html_content.replace('''<div class="mode-tabs">
                <button class="mode-btn active" data-mode="car">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg>
                    By Car
                </button>
            </div>''', '')

# Update FAQ
old_faq = """<div class="faq-grid">
                  <!-- FAQ 1 -->
                  <div class="faq-item">
                      <button class="faq-question">
                          Are monument entry tickets included in this 8-day itinerary?
                          <span class="faq-icon"><svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>
                      </button>
                      <div class="faq-answer">
                          <div class="faq-answer-inner">
                              <p>Yes, all monument entry fees, including VIP fast-track access to the <a href="agra-day-tour.html" class="seo-internal-link">Taj Mahal</a>, Amber Fort, and City Palace, are fully covered in the package. You will not need to wait in line.</p>
                          </div>
                      </div>
                  </div>
                  <!-- FAQ 2 -->
                  <div class="faq-item">
                      <button class="faq-question">
                          Is the early morning <a href="agra-day-tour.html" class="seo-internal-link">Taj Mahal</a> visit included?
                          <span class="faq-icon"><svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>
                      </button>
                      <div class="faq-answer">
                          <div class="faq-answer-inner">
                              <p>Yes — all our packages include a private early-morning visit to the <a href="agra-day-tour.html" class="seo-internal-link">Taj Mahal</a> before general tourist crowds arrive. Your personal historian guide provides exclusive context while you experience the monument in near-total tranquillity. VIP gate entry is pre-arranged so there is zero queuing.</p>
                          </div>
                      </div>
                  </div>
                  <!-- FAQ 3 -->
                  <div class="faq-item">
                      <button class="faq-question">
                          What type of vehicle is provided for the 'By Car' mode?
                          <span class="faq-icon"><svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>
                      </button>
                      <div class="faq-answer">
                          <div class="faq-answer-inner">
                              <p>We provide a premium, air-conditioned Toyota Innova Crysta for standard luxury bookings. For ultra-luxury requests, we offer Mercedes-Benz or BMW SUVs. All vehicles come with a dedicated, professional chauffeur, mobile Wi-Fi, and complimentary bottled water and refreshments.</p>
                          </div>
                      </div>
                  </div>
                  <!-- FAQ 4 -->
                  <div class="faq-item">
                      <button class="faq-question">
                          Can the itinerary be customized?
                          <span class="faq-icon"><svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>
                      </button>
                      <div class="faq-answer">
                          <div class="faq-answer-inner">
                              <p>Absolutely. While this 8-day itinerary is our most highly recommended route, every Grand Holidays tour is 100% bespoke. We can add rest days, include specialized culinary tours, or adjust the duration to perfectly match your preferences.</p>
                          </div>
                      </div>
                  </div>
              </div>"""

new_faq = """<div class="faq-grid">
                  <div class="faq-item">
                      <button class="faq-question">
                          Are the domestic flights between Jaipur, Varanasi, and Delhi included?
                          <span class="faq-icon"><svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>
                      </button>
                      <div class="faq-answer">
                          <div class="faq-answer-inner">
                              <p>Yes, round-trip economy domestic flight tickets (Jaipur to Varanasi, and Varanasi to Delhi) are fully included in the package price. We handle all bookings to ensure seamless connections.</p>
                          </div>
                      </div>
                  </div>
                  <div class="faq-item">
                      <button class="faq-question">
                          What is the luggage allowance for the domestic flights?
                          <span class="faq-icon"><svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>
                      </button>
                      <div class="faq-answer">
                          <div class="faq-answer-inner">
                              <p>Standard domestic flights in India typically allow 15kg (33 lbs) of checked baggage and 7kg (15 lbs) of cabin baggage per person. If you require more allowance, please let our concierges know so we can pre-purchase extra weight for you.</p>
                          </div>
                      </div>
                  </div>
                  <div class="faq-item">
                      <button class="faq-question">
                          What is the dress code for the Ganga Aarti and temples in Varanasi?
                          <span class="faq-icon"><svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>
                      </button>
                      <div class="faq-answer">
                          <div class="faq-answer-inner">
                              <p>Varanasi is a deeply spiritual and conservative city. We highly recommend modest clothing. Both men and women should wear clothing that covers their shoulders and knees. Slip-on shoes are advised as you will need to remove footwear before entering temples.</p>
                          </div>
                      </div>
                  </div>
                  <div class="faq-item">
                      <button class="faq-question">
                          Are monument entry tickets included in this itinerary?
                          <span class="faq-icon"><svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>
                      </button>
                      <div class="faq-answer">
                          <div class="faq-answer-inner">
                              <p>No, as per the exclusions list, entrance tickets to the monuments are not included. Your private guide will assist you in purchasing these directly at the monuments, or we can arrange them for you as an optional add-on.</p>
                          </div>
                      </div>
                  </div>
              </div>"""

html_content = html_content.replace(old_faq, new_faq)

with open(target_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Created Varansi tour files.')
