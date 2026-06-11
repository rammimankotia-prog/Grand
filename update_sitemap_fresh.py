import os

def generate_sitemap():
    base_url = "https://grandholidaytours.com/"
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    exclude_files = ['googled60501e34605346d.html']
    
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset\n'
    sitemap_content += '    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    sitemap_content += '    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'
    sitemap_content += '    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\n'
    sitemap_content += '        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n\n'
    
    for file in files:
        if file in exclude_files:
            continue
            
        priority = "0.9"
        if file == "index.html":
            priority = "1.0"
        elif file in ["privacy.html", "terms.html"]:
            priority = "0.4"
            
        sitemap_content += '    <url>\n'
        sitemap_content += f'        <loc>{base_url}{file}</loc>\n'
        sitemap_content += '        <lastmod>2026-06-11</lastmod>\n'
        sitemap_content += '        <changefreq>monthly</changefreq>\n'
        sitemap_content += f'        <priority>{priority}</priority>\n'
        sitemap_content += '    </url>\n'
        
    sitemap_content += '</urlset>\n'
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
        
if __name__ == "__main__":
    generate_sitemap()
