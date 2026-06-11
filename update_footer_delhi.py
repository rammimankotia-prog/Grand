import re

# 1. Add Delhi Guide link to ALL existing pages' footers
import glob
import os

html_files = [f for f in glob.glob('*.html') if f != 'delhi-travel-guide.html']

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False

    # Add to Explore section in footer if not already there
    if 'delhi-travel-guide.html' not in html:
        # Add after contact.html link in footer
        html = html.replace(
            '<a href="contact.html">Contact</a>\n                </div>',
            '<a href="contact.html">Contact</a>\n                    <a href="delhi-travel-guide.html">Delhi Travel Guide</a>\n                </div>'
        )
        changed = True

    if changed:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated footer in: {fname}")

# 2. Update sitemap
with open('update_sitemap.py', 'r', encoding='utf-8') as f:
    sitemap_script = f.read()

# Run manually since script reads all HTML files
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

new_url = """
    <url>
        <loc>https://grandholidaytours.com/delhi-travel-guide.html</loc>
        <lastmod>2026-06-11</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>"""

if 'delhi-travel-guide.html' not in sitemap:
    sitemap = sitemap.replace('</urlset>', new_url + '\n</urlset>')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("Added delhi-travel-guide.html to sitemap.xml")
