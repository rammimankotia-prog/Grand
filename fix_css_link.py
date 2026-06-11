with open('delhi-travel-guide.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add golden-triangle.css after index.css for the shared header/nav styles
html = html.replace(
    '<link rel="stylesheet" href="index.css?v=14">',
    '<link rel="stylesheet" href="index.css?v=14">\n    <link rel="stylesheet" href="golden-triangle.css?v=5">'
)

# Also add the JS for the hamburger / scroll behaviour used in other tour pages
old_script_tag = '    <script>\n        // Header scroll behaviour\n        const header = document.getElementById(\'mainHeader\');'

new_script_tag = '''    <script>
        // Header scroll (matching other pages)
        const siteHeader = document.getElementById('siteHeader');
        const hamburger = document.querySelector('.hamburger-btn') || document.querySelector('[class*=hamburger]');
        const navMenu = document.querySelector('.nav-menu');

        window.addEventListener('scroll', () => {
            if (siteHeader) siteHeader.classList.toggle('scrolled', window.scrollY > 60);
        });

        if (hamburger && navMenu) {
            hamburger.addEventListener('click', () => navMenu.classList.toggle('active'));
        }
        // Header scroll behaviour legacy
        const header = document.getElementById('mainHeader') || document.getElementById('siteHeader');'''

html = html.replace(old_script_tag, new_script_tag)

with open('delhi-travel-guide.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
