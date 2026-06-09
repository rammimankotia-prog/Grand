/**
 * setup-hooks.js
 * ─────────────────────────────────────────────────────────────────────────────
 * Run once after cloning the repo on a new machine to install the pre-commit
 * hook that auto-regenerates sitemap.xml before every git commit.
 *
 * Usage:  node setup-hooks.js
 * ─────────────────────────────────────────────────────────────────────────────
 */

const fs   = require('fs');
const path = require('path');

const hookDir  = path.join(__dirname, '.git', 'hooks');
const hookFile = path.join(hookDir, 'pre-commit');

const hookContent = `#!/bin/sh
# Auto-regenerates sitemap.xml before every git commit.
echo "🗺  Updating sitemap.xml..."
node generate-sitemap.js
git add sitemap.xml
echo "✅ sitemap.xml staged and ready."
`;

if (!fs.existsSync(hookDir)) {
    console.error('❌ .git/hooks directory not found. Make sure you are in the project root.');
    process.exit(1);
}

fs.writeFileSync(hookFile, hookContent, { encoding: 'utf8', mode: 0o755 });
console.log('✅ pre-commit hook installed at .git/hooks/pre-commit');
console.log('   The sitemap will now auto-update on every git commit.');
