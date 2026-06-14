import os
import glob
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

for filepath in glob.glob(os.path.join(repo_path, '*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to find the related-carousel section and strip out the seo-internal-link <a> tags inside it.
    if '<div class="related-carousel">' in content:
        parts = content.split('<div class="related-carousel">')
        before = parts[0]
        
        # We need to split the second part by the end of the section so we don't mess up 
        # other valid SEO links outside the carousel.
        # The carousel ends roughly at the end of the section.
        subparts = parts[1].split('</section>')
        carousel_content = subparts[0]
        after = '</section>' + '</section>'.join(subparts[1:])

        # Remove the nested <a> tags but keep their inner text
        fixed_carousel = re.sub(r'<a href="[^"]*" class="seo-internal-link">(.*?)</a>', r'\1', carousel_content)
        
        new_content = before + '<div class="related-carousel">' + fixed_carousel + after

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print('Fixed nested anchor tags in carousels.')
