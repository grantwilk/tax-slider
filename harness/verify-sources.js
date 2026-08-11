// Check that every cited URL resolves and lands where it claims to.
//
// Government sites are the bulk of this corpus and most answer a plain request
// fine. A few (congress.gov, some publishers) refuse anything that is not a
// real browser, so those fall back to Chromium rather than being reported dead.
//
//   node verify-sources.js <file-of-urls> [--concurrency 6]

const fs = require('fs');
const { chromium } = require('playwright');

const listPath = process.argv[2];
if (!listPath) {
  console.error('usage: node verify-sources.js <file-of-urls>');
  process.exit(2);
}
const flagIdx = process.argv.indexOf('--concurrency');
const CONCURRENCY = flagIdx > -1 ? Number(process.argv[flagIdx + 1]) : 6;

const urls = fs.readFileSync(listPath, 'utf8')
  .split('\n').map(s => s.trim()).filter(s => s.startsWith('http'));

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
         + '(KHTML, like Gecko) Chrome/125.0 Safari/537.36';

function titleOf(html) {
  const m = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  if (!m) return '';
  return m[1].replace(/\s+/g, ' ').trim().slice(0, 95);
}

async function viaFetch(url) {
  const ctl = new AbortController();
  const timer = setTimeout(() => ctl.abort(), 25000);
  try {
    const res = await fetch(url, {
      redirect: 'follow',
      signal: ctl.signal,
      headers: { 'User-Agent': UA, 'Accept': '*/*' },
    });
    const type = res.headers.get('content-type') || '';
    let title = '';
    if (type.includes('pdf')) {
      title = '[PDF]';
    } else {
      const body = await res.text();
      title = titleOf(body);
    }
    return { status: res.status, finalUrl: res.url, title, via: 'http' };
  } finally {
    clearTimeout(timer);
  }
}

async function viaBrowser(browser, url) {
  const ctx = await browser.newContext({ userAgent: UA });
  const page = await ctx.newPage();
  try {
    const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 35000 });
    const title = (await page.title() || '').replace(/\s+/g, ' ').trim().slice(0, 95);
    return { status: res ? res.status() : 0, finalUrl: page.url(), title, via: 'browser' };
  } finally {
    await ctx.close();
  }
}

(async () => {
  const browser = await chromium.launch();
  const results = [];
  let cursor = 0;

  async function worker() {
    while (cursor < urls.length) {
      const url = urls[cursor++];
      let r;
      try {
        r = await viaFetch(url);
        // A bot-block or a server error is worth a second try with a real browser.
        if (r.status === 403 || r.status === 429 || r.status >= 500) {
          r = await viaBrowser(browser, url);
        }
      } catch (e) {
        try {
          r = await viaBrowser(browser, url);
        } catch (e2) {
          r = { status: 0, finalUrl: url, title: String(e2.message).slice(0, 70), via: 'failed' };
        }
      }
      results.push({ url, ...r });
    }
  }

  await Promise.all(Array.from({ length: CONCURRENCY }, worker));

  results.sort((a, b) => urls.indexOf(a.url) - urls.indexOf(b.url));
  const bad = [];
  for (const r of results) {
    const ok = r.status >= 200 && r.status < 400;
    if (!ok) bad.push(r);
    console.log(`${ok ? 'ok  ' : 'BAD '} ${String(r.status).padEnd(3)} ${r.via.padEnd(7)} ${r.url}`);
    if (r.title) console.log(`              "${r.title}"`);
    if (r.finalUrl !== r.url) console.log(`           -> ${r.finalUrl}`);
  }

  console.log(`\n${results.length} checked, ${bad.length} need a look`);
  if (bad.length) {
    console.log('\nNEEDS A LOOK:');
    for (const r of bad) console.log(`  ${r.status}  ${r.url}  ${r.title}`);
  }
  await browser.close();
  process.exit(bad.length ? 1 : 0);
})();
