import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

new_dropdown_content = """<div class="dropdown-menu">
                            <div class="dropdown-header">Golden Triangle</div>
                            <a class="dropdown-item" href="4-days-golden-triangle-tour.html">4 Days Golden Triangle</a>
                            <a class="dropdown-item" href="5-days-golden-triangle-tour.html">5 Days Golden Triangle</a>
                            <a class="dropdown-item" href="8-days-golden-triangle-tour.html">8 Days Golden Triangle</a>
                            <a class="dropdown-item" href="8-days-golden-triangle-varanasi-tour.html">8 Days Golden Triangle & Varanasi</a>
                            
                            <div class="dropdown-header">Delhi & Agra</div>
                            <a class="dropdown-item" href="delhi-sightseeing.html">Delhi Sightseeing Tour</a>
                            <a class="dropdown-item" href="delhi-food-tour.html">Delhi Food & Spice Tour</a>
                            <a class="dropdown-item" href="delhi-spiritual-tour.html">Delhi Spiritual & Temple Tour</a>
                            <a class="dropdown-item" href="delhi-bicycle-tour.html">New Delhi Bicycle Tour</a>
                            <a class="dropdown-item" href="delhi-tuk-tuk-tour.html">Delhi Tuk Tuk Tour</a>
                            <a class="dropdown-item" href="delhi-museum-tour.html">Delhi Museum Tour</a>
                            <a class="dropdown-item" href="agra-day-tour.html">Same Day Agra Tour</a>
                            <a class="dropdown-item" href="delhi-agra-2-day-tour.html">2-Day Taj Mahal & Delhi</a>
                            
                            <div class="dropdown-header">Rajasthan</div>
                            <a class="dropdown-item" href="imperial-rajasthan.html">Imperial Rajasthan Tour</a>
                            <a class="dropdown-item" href="rajasthan-heritage-tour.html">Rajasthan Heritage Tour</a>
                            <a class="dropdown-item" href="marvellous-marwar-tour.html">Marvellous Marwar Tour</a>
                            <a class="dropdown-item" href="rajasthan-desert-adventure.html">Rajasthan Desert Adventure</a>
                            <a class="dropdown-item" href="tiger-tour-jaipur.html">Tiger Tour With Jaipur</a>
                            
                            <div class="dropdown-header">Himalayas</div>
                            <a class="dropdown-item" href="himachal-exotic-tour.html">Himachal Exotic Tour</a>
                            <a class="dropdown-item" href="himalayan-sanctuary.html">Himalayan Sanctuary</a>
                        </div>"""

# Find <div class="dropdown-menu"> and replace everything until its closing </div>
# In the original, there are NO nested divs inside dropdown-menu.
# However, my previous script ALREADY modified 6 files, which now HAVE <div class="dropdown-header"> inside!
# So for those 6 files, <div class="dropdown-menu">.*?</div> would stop at the first </div> of dropdown-header!
# To handle both, we can just look for the wrapper:
# <div class="nav-dropdown"> ... <div class="dropdown-menu"> ... </div>\s*</div>\s*(?:<a href="contact|...)

pattern1 = re.compile(r'(<a [^>]*class="nav-link dropdown-toggle"[^>]*>.*?</a>\s*)<div class="dropdown-menu">.*?</div>(\s*</div>)', re.DOTALL)

updated_count = 0
for filename in os.listdir(repo_path):
    if filename.endswith(".html"):
        filepath = os.path.join(repo_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We will use the nav-link dropdown-toggle as the anchor
        # Match from dropdown-toggle to the end of dropdown-menu
        
        def repl(match):
            return match.group(1) + new_dropdown_content + match.group(2)
            
        new_content = pattern1.sub(repl, content)
        
        # For files that use the active state or different class order:
        pattern2 = re.compile(r'(<a [^>]*dropdown-toggle[^>]*>.*?</a>\s*)<div class="dropdown-menu">.*?</div>(\s*</div>)', re.DOTALL)
        if new_content == content:
             new_content = pattern2.sub(repl, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1
            print(f"Updated {filename}")
        else:
            print(f"Skipped/Failed {filename}")

print(f"Updated {updated_count} files in total.")
