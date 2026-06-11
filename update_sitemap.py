import glob
import re
from datetime import datetime

html_files = glob.glob("*.html")
html_files = [f for f in html_files if not f.startswith("google")]

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

today = datetime.today().strftime('%Y-%m-%d')
new_urls = []

for file in html_files:
    if f"<loc>https://grandholidaytours.com/{file}</loc>" not in sitemap:
        priority = "0.9"
        if file in ["car-booking.html", "train-booking.html"]:
            priority = "0.9"
        elif file.endswith("-tour.html"):
            priority = "0.9"
            
        url_block = f"""    <url>
        <loc>https://grandholidaytours.com/{file}</loc>
        <lastmod>{today}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>{priority}</priority>
    </url>"""
        new_urls.append(url_block)

if new_urls:
    # Insert new URLs before the closing </urlset>
    closing_tag = "</urlset>"
    insertion = "\n" + "\n".join(new_urls) + "\n"
    sitemap = sitemap.replace(closing_tag, insertion + closing_tag)
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f"Added {len(new_urls)} new URLs to sitemap.xml")
else:
    print("No new URLs to add.")
