import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
html_file = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.html')

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_faqs = """<div class="faq-grid" id="faq-grid-gt">
  <div class="faq-item">
  <button aria-expanded="false" class="faq-question">
  <span class="faq-q-text">Which cities are covered in this tour?</span>
  <span class="faq-icon"><svg viewbox="0 0 14 14"><line x1="7" x2="7" y1="1" y2="13"></line><line x1="1" x2="13" y1="7" y2="7"></line></svg></span>
  </button>
  <div class="faq-answer"><div class="faq-answer-inner"><p>This comprehensive tour covers four iconic destinations: Delhi (the historic capital), Agra (home of the Taj Mahal), Jaipur (the royal Pink City), and Varanasi (the spiritual heart of India). It beautifully blends the classic Golden Triangle with a deeply spiritual extension.</p></div></div>
  </div>
  <div class="faq-item">
  <button aria-expanded="false" class="faq-question">
  <span class="faq-q-text">How do we travel between the different cities?</span>
  <span class="faq-icon"><svg viewbox="0 0 14 14"><line x1="7" x2="7" y1="1" y2="13"></line><line x1="1" x2="13" y1="7" y2="7"></line></svg></span>
  </button>
  <div class="faq-answer"><div class="faq-answer-inner"><p>For the Golden Triangle leg (Delhi, Agra, and Jaipur), you will travel in a private, chauffeur-driven premium A/C vehicle. For the onward journey to Varanasi, the tour includes a comfortable domestic flight from Jaipur to Varanasi, followed by a return flight from Varanasi to Delhi on your final day.</p></div></div>
  </div>
  <div class="faq-item">
  <button aria-expanded="false" class="faq-question">
  <span class="faq-q-text">What experiences are included in Varanasi?</span>
  <span class="faq-icon"><svg viewbox="0 0 14 14"><line x1="7" x2="7" y1="1" y2="13"></line><line x1="1" x2="13" y1="7" y2="7"></line></svg></span>
  </button>
  <div class="faq-answer"><div class="faq-answer-inner"><p>In Varanasi, you will witness the mesmerizing evening Ganga Aarti ceremony on the riverbanks. The following morning, you will experience a serene sunrise boat ride on the holy River Ganges, walk through the ancient labyrinthine alleys, and visit the historic site of Sarnath where Lord Buddha gave his first sermon.</p></div></div>
  </div>
  <div class="faq-item">
  <button aria-expanded="false" class="faq-question">
  <span class="faq-q-text">Can we get private sunrise access to the Taj Mahal?</span>
  <span class="faq-icon"><svg viewbox="0 0 14 14"><line x1="7" x2="7" y1="1" y2="13"></line><line x1="1" x2="13" y1="7" y2="7"></line></svg></span>
  </button>
  <div class="faq-answer"><div class="faq-answer-inner"><p>Yes — all our packages include a private early-morning visit to the <a href="agra-day-tour.html" class="seo-internal-link">Taj Mahal</a> before general tourist crowds arrive. Your personal historian guide provides exclusive context while you experience the monument in near-total tranquillity.</p></div></div>
  </div>
  <div class="faq-item">
  <button aria-expanded="false" class="faq-question">
  <span class="faq-q-text">Is this itinerary suitable for families and seniors?</span>
  <span class="faq-icon"><svg viewbox="0 0 14 14"><line x1="7" x2="7" y1="1" y2="13"></line><line x1="1" x2="13" y1="7" y2="7"></line></svg></span>
  </button>
  <div class="faq-answer"><div class="faq-answer-inner"><p>Absolutely. We pace the itinerary comfortably with premium vehicles and domestic flights to minimize fatigue. The boat rides in Varanasi are very safe, and our guides ensure that walking tours are adjusted to your comfort level.</p></div></div>
  </div>
  <div class="faq-item">
  <button aria-expanded="false" class="faq-question">
  <span class="faq-q-text">What is the best time of year to take this tour?</span>
  <span class="faq-icon"><svg viewbox="0 0 14 14"><line x1="7" x2="7" y1="1" y2="13"></line><line x1="1" x2="13" y1="7" y2="7"></line></svg></span>
  </button>
  <div class="faq-answer"><div class="faq-answer-inner"><p>The ideal window is October through March, when North India experiences pleasant weather (15—25°C), clear blue skies, and vibrant cultural festivals. This is especially important for Varanasi, where cool mornings make the sunrise boat rides incredibly peaceful.</p></div></div>
  </div>"""

# Find the start and end of the faq-grid
start_marker = '<div class="faq-grid" id="faq-grid-gt">'
end_marker = '</div>\n  </div>\n  </section>'

start_idx = content.find(start_marker)
if start_idx != -1:
    # Find the closing tag of the faq-grid. It's the div right before the section closes.
    # Actually, let's just use regex to replace from <div class="faq-grid" id="faq-grid-gt"> up to the next </section>
    
    # We want to replace the whole faq-grid content
    pattern = re.compile(r'<div class="faq-grid" id="faq-grid-gt">.*?(?=\s*</div>\s*</section>)', re.DOTALL)
    
    if pattern.search(content):
        content = pattern.sub(new_faqs, content)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated FAQs!")
    else:
        print("Could not find the end of the FAQ section.")
else:
    print("Could not find faq-grid start marker.")
