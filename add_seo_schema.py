import os
import glob
import re
import json

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

local_business_schema = {
  "@context": "https://schema.org",
  "@type": "TravelAgency",
  "name": "Grand Holidays",
  "image": "https://www.grandholidaytours.com/assets/logo.png",
  "@id": "",
  "url": "https://www.grandholidaytours.com",
  "telephone": "+91 8860081995",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Plot No. 8502/41, Ground Floor, Arakashan Rd, behind Sheela Cinema Street, Ram Nagar, Paharganj",
    "addressLocality": "New Delhi",
    "addressRegion": "Delhi",
    "postalCode": "110055",
    "addressCountry": "IN"
  }
}

keywords_mapping = {
    r'\bTaj Mahal\b': 'agra-day-tour.html',
    r'\bGolden Triangle\b': '8-days-golden-triangle-tour.html',
    r'\bTiger Safari\b': 'tiger-tour-jaipur.html',
    r'\bRanthambore\b': 'tiger-tour-jaipur.html',
    r'\bDelhi Sightseeing\b': 'delhi-sightseeing.html'
}

def inject_internal_links(content):
    # This is a bit tricky, we only want to replace inside <p> tags, not inside existing <a> tags or attributes
    # A simple approach for this specific site is to use regex cautiously.
    # To avoid breaking HTML, we'll use a simpler replacement that tries to only match plain text outside tags, 
    # but since regex for that is complex, we will just do it carefully.
    
    # We will split the document by <p> and </p>, process the text inside, and put it back.
    parts = re.split(r'(?i)(<p.*?>|</p>)', content)
    
    inside_p = False
    for i, part in enumerate(parts):
        if re.match(r'(?i)<p.*?>', part):
            inside_p = True
        elif re.match(r'(?i)</p>', part):
            inside_p = False
        elif inside_p:
            # We are inside a paragraph, replace keywords if not already in an <a> tag
            # If the part already contains <a>, we skip it to be safe, or just do a simple replace 
            # if we are sure it won't break things.
            if '<a ' not in part:
                for kw_regex, url in keywords_mapping.items():
                    # Only replace the FIRST occurrence in a block to avoid spamming links
                    part = re.sub(f'({kw_regex})', rf'<a href="{url}" class="seo-internal-link">\1</a>', part, count=1)
                parts[i] = part
    return "".join(parts)


for filepath in glob.glob(os.path.join(repo_path, '*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    is_tour_page = filename.endswith('-tour.html') or filename == 'delhi-sightseeing.html'

    # Extract Title
    title_match = re.search(r'<title>(.*?)</title>', content)
    page_title = title_match.group(1).split('|')[0].strip() if title_match else "Tour"

    schema_list = [local_business_schema]

    # Add Breadcrumbs and Schema for Tour Pages
    if is_tour_page:
        breadcrumb_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [{
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://www.grandholidaytours.com/"
            },{
                "@type": "ListItem",
                "position": 2,
                "name": "Tours",
                "item": "https://www.grandholidaytours.com/all-tours.html"
            },{
                "@type": "ListItem",
                "position": 3,
                "name": page_title
            }]
        }
        
        tourist_schema = {
            "@context": "https://schema.org",
            "@type": "TouristTrip",
            "name": page_title,
            "provider": {
                "@type": "TravelAgency",
                "name": "Grand Holidays"
            }
        }

        schema_list.append(breadcrumb_schema)
        schema_list.append(tourist_schema)

        # Inject UI Breadcrumb
        breadcrumb_html = f'''
        <nav aria-label="breadcrumb" class="tour-breadcrumbs" style="margin-bottom: 1rem;">
            <ol style="list-style: none; padding: 0; margin: 0; display: flex; gap: 0.5rem; font-size: 0.85rem; opacity: 0.8;">
                <li><a href="index.html" style="color: inherit; text-decoration: none;">Home</a></li>
                <li><span style="opacity: 0.5;">/</span></li>
                <li><a href="all-tours.html" style="color: inherit; text-decoration: none;">Tours</a></li>
                <li><span style="opacity: 0.5;">/</span></li>
                <li aria-current="page" style="font-weight: 500;">{page_title}</li>
            </ol>
        </nav>
        '''
        
        if 'tour-breadcrumbs' not in content and '<div class="tour-layout-grid">' in content:
            content = content.replace('<div class="tour-layout-grid">', breadcrumb_html + '\n<div class="tour-layout-grid">')


    # Inject Schema into <head>
    schema_json = json.dumps(schema_list, indent=2)
    schema_script = f'\n<!-- JSON-LD Schema -->\n<script type="application/ld+json">\n{schema_json}\n</script>\n'
    
    # Check if schema already exists to prevent duplication
    if '<!-- JSON-LD Schema -->' not in content:
        content = content.replace('</head>', schema_script + '</head>')

    # Inject Internal Links
    content = inject_internal_links(content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Schema, Breadcrumbs, and Internal Links added successfully.")
