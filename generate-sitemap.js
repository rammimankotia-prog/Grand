/**
 * generate-sitemap.js
 * ─────────────────────────────────────────────────────────────────────────────
 * Auto-generates sitemap.xml by scanning all .html files in the project root.
 * Run manually:  node generate-sitemap.js
 * Or automatically via the git pre-commit hook (see .git/hooks/pre-commit).
 * ─────────────────────────────────────────────────────────────────────────────
 */

const fs   = require('fs');
const path = require('path');

// ── CONFIGURATION ─────────────────────────────────────────────────────────────
const BASE_URL   = 'https://grandholidaytours.com';
const OUTPUT     = path.join(__dirname, 'sitemap.xml');
const DIR        = __dirname;

// Pages excluded from the sitemap (add any you want hidden from search engines)
const EXCLUDED   = new Set(['googled60501e34605346d.html']);

// Priority & change-frequency rules – matched by filename keyword
const RULES = [
    { match: 'index',               priority: '1.0', changefreq: 'weekly'  },
    { match: 'about',               priority: '0.8', changefreq: 'monthly' },
    { match: 'contact',             priority: '0.8', changefreq: 'monthly' },
    { match: 'golden-triangle',     priority: '0.9', changefreq: 'monthly' },
    { match: 'delhi-sightseeing',   priority: '0.9', changefreq: 'monthly' },
    { match: 'delhi-food-tour',     priority: '0.9', changefreq: 'monthly' },
    { match: 'delhi-spiritual-tour',priority: '0.9', changefreq: 'monthly' },
    { match: 'delhi-bicycle-tour',  priority: '0.9', changefreq: 'monthly' },
    { match: 'agra-day-tour',       priority: '0.9', changefreq: 'monthly' },
    { match: 'himalayan-sanctuary', priority: '0.9', changefreq: 'monthly' },
    { match: 'imperial-rajasthan',  priority: '0.9', changefreq: 'monthly' },
    { match: 'privacy',             priority: '0.4', changefreq: 'yearly'  },
    { match: 'terms',               priority: '0.4', changefreq: 'yearly'  },
];

// Default rule for any page not matched above
const DEFAULT_RULE = { priority: '0.7', changefreq: 'monthly' };
// ─────────────────────────────────────────────────────────────────────────────

function getRule(filename) {
    const name = filename.toLowerCase();
    for (const rule of RULES) {
        if (name.includes(rule.match)) return rule;
    }
    return DEFAULT_RULE;
}

function getLastmod() {
    // Use today's date in YYYY-MM-DD format
    return new Date().toISOString().split('T')[0];
}

function buildSitemap() {
    // Scan root directory for all .html files
    const files = fs.readdirSync(DIR).filter(f => {
        return f.endsWith('.html') && !EXCLUDED.has(f);
    }).sort();

    const today = getLastmod();

    const urls = files.map(file => {
        const rule = getRule(file);
        const loc  = `${BASE_URL}/${file}`;
        return `
    <url>
        <loc>${loc}</loc>
        <lastmod>${today}</lastmod>
        <changefreq>${rule.changefreq}</changefreq>
        <priority>${rule.priority}</priority>
    </url>`;
    }).join('');

    const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
${urls}
</urlset>
`;

    fs.writeFileSync(OUTPUT, xml, 'utf8');
    console.log(`✅ sitemap.xml updated — ${files.length} pages indexed.`);
    files.forEach(f => console.log(`   → ${BASE_URL}/${f}`));
}

buildSitemap();
