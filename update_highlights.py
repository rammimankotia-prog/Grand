import os

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
html_file = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.html')
css_file = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.css')
js_file = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.js')

# 1. Update HTML
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

highlights_html = '''
              <div class="detail-block glass-card highlights-split-block">
                  <div class="highlights-split-grid">
                      <div class="highlights-split-title">
                          <h3>Highlights</h3>
                      </div>
                      <div class="highlights-split-list">
                          <ul id="tour-highlights-list-split">
                              <!-- Injected by JS -->
                          </ul>
                      </div>
                  </div>
              </div>
'''

# Insert right before the Itinerary block
if 'highlights-split-block' not in html_content:
    html_content = html_content.replace('<!-- Day by Day Itinerary -->', highlights_html + '\n              <!-- Day by Day Itinerary -->')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

# 2. Update CSS
css_content = '''
/* Highlights Split Block */
.highlights-split-block {
    padding: 2rem !important;
}
.highlights-split-grid {
    display: flex;
    gap: 2rem;
}
.highlights-split-title {
    flex: 0 0 160px;
}
.highlights-split-title h3 {
    font-family: 'Outfit', sans-serif;
    color: #1a3550;
    font-size: 1.6rem;
    margin: 0;
    font-weight: 700;
}
.highlights-split-list ul {
    list-style: none;
    padding: 0;
    margin: 0;
}
.highlights-split-list li {
    position: relative;
    padding-left: 28px;
    margin-bottom: 0.9rem;
    color: #334155;
    font-size: 1.05rem;
    line-height: 1.5;
}
.highlights-split-list li svg {
    position: absolute;
    left: 0;
    top: 3px;
    width: 18px;
    height: 18px;
    color: #10b981; /* Green checkmark to make it visible */
}

@media (max-width: 768px) {
    .highlights-split-grid {
        flex-direction: column;
        gap: 1rem;
    }
    .highlights-split-title {
        flex: auto;
    }
}
'''

with open(css_file, 'a', encoding='utf-8') as f:
    f.write(css_content)

# 3. Update JS
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Remove highlights from the top highlight box
target_to_remove = """                <div style="margin-top: 15px; border-top: 1px dashed rgba(255,255,255,0.3); padding-top: 15px;">
                    <h4 style="color: #fff; font-size: 1.1rem; margin-bottom: 10px;">Highlights</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; color: rgba(255,255,255,0.95); font-size: 0.95rem;">
                        ${modeData.highlightsList.map(h => `<li style="margin-bottom: 6px; display: flex; align-items: flex-start;"><svg style="min-width: 16px; margin-right: 8px; margin-top: 4px;" fill="none" stroke="currentColor" viewBox="0 0 24 24" width="16" height="16"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>${h}</li>`).join('')}
                    </ul>
                </div>"""

js_content = js_content.replace(target_to_remove, '')

# Add JS logic to inject into the new split block
injection_logic = '''
        // Render split highlights
        const highlightsSplitBox = document.getElementById('tour-highlights-list-split');
        if (highlightsSplitBox && modeData.highlightsList) {
            highlightsSplitBox.innerHTML = modeData.highlightsList.map(h => `
                <li>
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                    ${h}
                </li>
            `).join('');
        }
'''

if 'highlightsSplitBox' not in js_content:
    js_content = js_content.replace('// Render timeline', injection_logic + '\n        // Render timeline')

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print('Updated Highlights block.')
