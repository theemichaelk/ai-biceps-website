/**
 * Visual + structural audit of TSBR site via Playwright.
 * Usage: npm run visual-audit -- --base http://localhost:8080
 */
import { chromium } from 'playwright';
import { mkdir, writeFile } from 'fs/promises';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const base = process.argv.includes('--base')
  ? process.argv[process.argv.indexOf('--base') + 1]
  : 'http://localhost:8080';

const PAGES = [
  { path: '/', name: 'home' },
  { path: '/about.html', name: 'about' },
  { path: '/services.html', name: 'services' },
  { path: '/contact.html', name: 'contact' },
  { path: '/testimonials.html', name: 'testimonials' },
  { path: '/case-studies.html', name: 'case-studies' },
  { path: '/locations.html', name: 'locations' },
  { path: '/blog.html', name: 'blog' },
  { path: '/ai-news.html', name: 'ai-news' },
  { path: '/resources.html', name: 'resources' },
  { path: '/gmb-optimization.html', name: 'gmb' },
  { path: '/ai-search-optimization.html', name: 'ai-search' },
  { path: '/local-seo-texas.html', name: 'local-seo' },
  { path: '/arlington-tx-seo-marketing-consultant.html', name: 'location-arlington' },
  { path: '/blog/gmb-velocity-system-texas.html', name: 'blog-post-gmb' },
  { path: '/privacy.html', name: 'privacy' },
  { path: '/404.html', name: '404' },
];

const reportDir = join(__dirname, 'visual-report');
const issues = [];
const passes = [];

async function checkPage(page, { path, name }) {
  const url = `${base}${path}`;
  const res = await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  const status = res?.status() ?? 0;

  if (status >= 400) {
    issues.push(`${name}: HTTP ${status}`);
    return;
  }

  // Scroll full page so lazy-loaded images fetch before we check them
  await page.evaluate(async () => {
    await new Promise((resolve) => {
      let y = 0;
      const step = () => {
        y += window.innerHeight;
        window.scrollTo(0, y);
        if (y < document.body.scrollHeight) requestAnimationFrame(step);
        else { window.scrollTo(0, 0); resolve(); }
      };
      step();
    });
  });
  await page.waitForTimeout(800);

  const checks = await page.evaluate(() => {
    const imgs = [...document.querySelectorAll('img')];
    const broken = imgs.filter((img) => img.complete && img.naturalWidth === 0);
    return {
      title: document.title,
      h1: document.querySelector('h1')?.textContent?.trim() || '',
      hasMain: !!document.getElementById('main'),
      hasNav: !!document.querySelector('.nav-desktop'),
      hasFooter: !!document.querySelector('.site-footer'),
      hasFavicon: !!document.querySelector('link[rel="icon"]'),
      formCount: document.querySelectorAll('form').length,
      brokenImages: broken.length,
      brokenSrc: broken.map((img) => img.getAttribute('src')).slice(0, 5),
      overflowX: document.documentElement.scrollWidth > window.innerWidth + 2,
    };
  });

  if (!checks.hasMain) issues.push(`${name}: missing #main`);
  if (!checks.hasNav) issues.push(`${name}: missing nav`);
  if (!checks.hasFooter) issues.push(`${name}: missing footer`);
  if (!checks.hasFavicon) issues.push(`${name}: missing favicon`);
  if (checks.brokenImages > 0) {
    const srcs = checks.brokenSrc?.length ? ` (${checks.brokenSrc.join(', ')})` : '';
    issues.push(`${name}: ${checks.brokenImages} broken image(s)${srcs}`);
  }
  if (checks.overflowX) issues.push(`${name}: horizontal overflow`);

  if (path.startsWith('/blog/')) {
    const crumbs = await page.evaluate(() => {
      const links = [...document.querySelectorAll('.breadcrumb a')].map((a) => a.getAttribute('href'));
      return { links, homeOk: links.some((h) => h && !h.includes('../..')) };
    });
    if (!crumbs.homeOk) issues.push(`${name}: breadcrumb uses invalid ../../ paths`);
    const homeStatus = await page.evaluate(async (href) => {
      const res = await fetch(new URL(href, window.location.href));
      return res.status;
    }, crumbs.links[0] || '../index.html');
    if (homeStatus >= 400) issues.push(`${name}: breadcrumb Home link HTTP ${homeStatus}`);
  }

  await page.screenshot({ path: join(reportDir, `${name}.png`), fullPage: false });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: join(reportDir, `${name}-mobile.png`), fullPage: false });
  await page.setViewportSize({ width: 1280, height: 800 });

  passes.push({ name, url, status, ...checks });
}

async function main() {
  await mkdir(reportDir, { recursive: true });
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const page = await context.newPage();

  console.log(`\nVisual audit — ${base}\n`);

  for (const p of PAGES) {
    process.stdout.write(`  ${p.name}... `);
    try {
      await checkPage(page, p);
      console.log('ok');
    } catch (err) {
      issues.push(`${p.name}: ${err.message}`);
      console.log('FAIL');
    }
  }

  // Mobile nav toggle
  try {
    await page.goto(`${base}/`, { waitUntil: 'networkidle' });
    await page.setViewportSize({ width: 390, height: 844 });
    const toggle = page.locator('#nav-toggle');
    if (await toggle.count()) {
      await toggle.click();
      const open = await page.locator('#nav-mobile.is-open').count();
      if (!open) issues.push('home-mobile: nav toggle did not open menu');
      else passes.push({ name: 'home-mobile-nav', url: base, status: 200, h1: 'nav toggle works' });
    }
  } catch (err) {
    issues.push(`home-mobile-nav: ${err.message}`);
  }

  await browser.close();

  const report = {
    auditedAt: new Date().toISOString(),
    base,
    passes,
    issues,
    screenshots: join(reportDir),
  };
  await writeFile(join(reportDir, 'report.json'), JSON.stringify(report, null, 2));

  console.log(`\nScreenshots: ${reportDir}`);
  console.log(`Pages checked: ${passes.length}`);
  if (issues.length) {
    console.log(`\nIssues (${issues.length}):`);
    issues.forEach((i) => console.log(`  ✗ ${i}`));
    process.exitCode = 1;
  } else {
    console.log('\nNo issues found.');
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});