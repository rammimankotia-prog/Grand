import re

with open('himachal-exotic-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_faq = """<div class="accordion">
                        <div class="accordion-item">
                            <button class="accordion-btn" aria-expanded="false">
                                What is the best time to take the Himachal Exotic Tour?
                                <span class="accordion-icon">+</span>
                            </button>
                            <div class="accordion-content">
                                <p>The best time to visit depends on what you wish to experience. For pleasant, cool weather to escape the heat, visit between <strong>March and June</strong>. If you want to experience the magic of snowfall in Kufri and Manali, <strong>November to February</strong> is the ideal time.</p>
                            </div>
                        </div>

                        <div class="accordion-item">
                            <button class="accordion-btn" aria-expanded="false">
                                Are adventure activities in Solang Valley included?
                                <span class="accordion-icon">+</span>
                            </button>
                            <div class="accordion-content">
                                <p>The package includes private AC transportation to Solang Valley. However, the direct fees for specific adventure activities like <strong>paragliding, zorbing, or skiing</strong> are excluded and can be paid directly on-site based on your interests.</p>
                            </div>
                        </div>

                        <div class="accordion-item">
                            <button class="accordion-btn" aria-expanded="false">
                                Is the drive safe in the mountainous terrain?
                                <span class="accordion-icon">+</span>
                            </button>
                            <div class="accordion-content">
                                <p>Absolutely. You will be traveling in a premium, fully-serviced AC car driven by highly experienced, professional drivers who are specifically trained for the Himalayan mountain routes.</p>
                            </div>
                        </div>

                        <div class="accordion-item">
                            <button class="accordion-btn" aria-expanded="false">
                                What is excluded from this tour package?
                                <span class="accordion-icon">+</span>
                            </button>
                            <div class="accordion-content">
                                <p>The package does not include air or train fare to/from Delhi, guide and monument entrance fees, camera/safari charges, or personal travel insurance. You will be responsible for your lunches, dinners, and any personal shopping.</p>
                            </div>
                        </div>
                    </div>"""

# Find the accordion div and replace it
faq_pattern = r'<div class="accordion">.*?</div>\s*</section>'
# Wait, replacing all the way to </section> is safe, just make sure to add it back
replacement = new_faq + '\n                </section>'

html = re.sub(faq_pattern, replacement, html, flags=re.DOTALL)

with open('himachal-exotic-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
