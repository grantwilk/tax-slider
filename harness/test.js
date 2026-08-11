// Check the page in a real browser: the arithmetic, the layout, and the wiring.
//
// The expected values below were worked by hand from the 2026 tables in
// ../research before the engine existed. They are not read back off the engine,
// which is the whole point. Where a figure needed arithmetic, the arithmetic is
// written into the comment so a reader can re-do it without trusting the code.
//
//   node test.js [--headed] [--shots]

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const PAGE = 'file://' + path.resolve(__dirname, '..', 'index.html');
const HEADED = process.argv.includes('--headed');
const SHOTS = process.argv.includes('--shots');
const SHOTDIR = path.resolve(__dirname, 'screenshots');

let pass = 0, fail = 0;
const failures = [];

function ok(name, cond, got, want) {
  if (cond) { pass++; return; }
  fail++;
  failures.push(`${name}\n      got:  ${got}\n      want: ${want}`);
}
function eq(name, got, want) { ok(name, got === want, got, want); }
function near(name, got, want, tol) {
  ok(name, Math.abs(got - want) <= tol, got, `${want} (+/- ${tol})`);
}

// Drive the page by setting state directly, then ask the engine one question.
// Going through the state object rather than the DOM keeps these tests about
// the arithmetic instead of about which input has which id.
async function ask(page, state, fn) {
  return page.evaluate(([st, body]) => {
    const t = window.__ts;
    Object.assign(t.S, JSON.parse(JSON.stringify(st.top || {})));
    if (st.mix) Object.assign(t.S.mix, st.mix);
    if (st.adj) Object.assign(t.S.adj, st.adj);
    if (st.oth) Object.assign(t.S.oth, st.oth);
    return new Function('t', body)(t);
  }, [state, '\n' + fn + '\n']);
}

const wages = n => ({ mix: { wage: n, bonus: 0, rsu: 0, int: 0, qdiv: 0, ltg: 0, stg: 0, exempt: 0 } });
const zeroAdj = { adj: { k401: 0, hsa: 0, iso: 0 } };
const zeroOth = { oth: { tips: 0, ot: 0, car: 0, ss: 0, hdhp: false, own: false } };
function base(over) {
  return Object.assign({ top: { status: 'single', age: 35, children: 0, income: 120000 } },
                       wages(120000), zeroAdj, zeroOth, over);
}

(async () => {
  const browser = await chromium.launch({ headless: !HEADED });
  const page = await browser.newPage({ viewport: { width: 1280, height: 1000 } });

  const consoleErrors = [];
  page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text()); });
  page.on('pageerror', e => consoleErrors.push('pageerror: ' + e.message));

  await page.goto(PAGE);
  await page.waitForFunction(() => window.__ts !== undefined);

  // The first-run dialog should be up on a clean profile, and should go away.
  eq('first run dialog is open', await page.locator('#scrim').isVisible(), true);
  await page.locator('#mGo').click();
  eq('first run dialog closes', await page.locator('#scrim').isVisible(), false);

  // ------------------------------------------------------- the measures ---
  // Single, $120,000 of pay, nothing set aside.
  //   AGI     120,000
  //   std ded  16,100   (Rev. Proc. 2025-32)
  //   taxable 103,900
  let m = await ask(page, base(), 'return t.measure(120000)');
  eq('agi, no adjustments', m.agi, 120000);
  eq('taxable, single, no adjustments', m.taxable, 103900);
  eq('fica wages equal pay', m.wages, 120000);

  // A traditional 401(k) cuts income tax but not payroll tax. An HSA taken
  // from pay cuts both. That difference is the point of this case.
  //   AGI     120,000 - 24,500 - 4,400 = 91,100
  //   taxable  91,100 - 16,100          = 75,000
  //   FICA    120,000 - 4,400           = 115,600   (401k is still FICA pay)
  m = await ask(page, base({ adj: { k401: 24500, hsa: 4400, iso: 0 } }), 'return t.measure(120000)');
  eq('agi drops by both', m.agi, 91100);
  eq('taxable after both', m.taxable, 75000);
  eq('401k does not escape payroll tax', m.wages, 115600);

  // The ISO spread moves the AMT measure and nothing else.
  m = await ask(page, base({ adj: { k401: 0, hsa: 0, iso: 60000 } }), 'return t.measure(120000)');
  eq('iso spread lifts amti', m.amti, 180000);
  eq('iso spread leaves agi alone', m.agi, 120000);

  // Tax-exempt interest stays out of AGI and comes back for MAGI.
  m = await ask(page, base({ mix: { wage: 100000, bonus: 0, rsu: 0, int: 0, qdiv: 0, ltg: 0, stg: 0, exempt: 20000 } }),
                'return t.measure(120000)');
  near('tax-exempt interest is outside agi', m.agi, 100000, 1);
  near('tax-exempt interest is inside magi', m.magi, 120000, 1);

  // Age 66, married filing jointly, $200,000 of pay.
  //   std      32,200 basic + 1,650 for age
  //   senior    6,000 - 0.06 x (200,000 - 150,000) = 3,000
  //   total    36,850     taxable = 163,150
  m = await ask(page, base({ top: { status: 'mfj', age: 66, children: 0, income: 200000 } }).top
                  ? Object.assign(base(), { top: { status: 'mfj', age: 66, children: 0, income: 200000 } },
                                  wages(200000))
                  : null,
                'return t.measure(200000)');
  eq('deduction at 66, mfj, includes a part senior deduction', m.deduction, 36850);
  eq('taxable at 66, mfj', m.taxable, 163150);

  // ------------------------------------------------- placing the edges ---
  // The 22% band runs 50,400 to 105,700 of taxable income. With a 16,100
  // standard deduction that is 66,500 to 121,800 of total income.
  let p = await ask(page, base(), 'return t.place(t.RULES.find(r=>r.id==="bracket_22"))');
  near('22% band starts, in total income', p.lo, 66500, 1);
  near('22% band ends, in total income', p.hi, 121800, 1);

  // Put 24,500 into a 401(k) and the same band slides up by exactly that much.
  p = await ask(page, base({ adj: { k401: 24500, hsa: 0, iso: 0 } }),
                'return t.place(t.RULES.find(r=>r.id==="bracket_22"))');
  near('a 401k slides the band up by the deferral', p.lo, 91000, 1);

  // The Social Security wage base is 184,500 of FICA pay. An HSA from pay is
  // outside FICA pay, so the ceiling arrives 4,400 later in total income.
  p = await ask(page, base({ adj: { k401: 0, hsa: 4400, iso: 0 } }),
                'return t.place(t.RULES.find(r=>r.id==="ss_wage_base"))');
  near('wage base, pushed out by an HSA', p.hi, 188900, 1);

  // NIIT is a MAGI threshold, so a 401(k) moves it and an HSA moves it too.
  p = await ask(page, base({ adj: { k401: 24500, hsa: 4400, iso: 0 } }),
                'return t.place(t.RULES.find(r=>r.id==="niit"))');
  near('niit threshold, after adjustments', p.lo, 228900, 1);   // 200,000 + 28,900

  // ---------------------------------------------- the moving right edges ---
  // The worked example in the corpus: $8,000 of tips ends at $230,000 of MAGI.
  let e = await ask(page, base({ oth: { tips: 8000, ot: 0, car: 0, ss: 0, hdhp: false, own: false } }),
                    'return t.movingEnd(t.RULES.find(r=>r.id==="tips_deduction"), 150000)');
  eq('tips end where the corpus says', e, 230000);

  // The full $25,000 of tips needs 250 steps of $100, so 400,000.
  e = await ask(page, base({ oth: { tips: 40000, ot: 0, car: 0, ss: 0, hdhp: false, own: false } }),
                'return t.movingEnd(t.RULES.find(r=>r.id==="tips_deduction"), 150000)');
  eq('tips cap at 25,000 and end at 400,000', e, 400000);

  // Car loan interest rounds the excess UP, so $6,000 of interest is gone once
  // the excess passes $29,000, not $30,000. Check the step either side.
  e = await ask(page, base({ oth: { tips: 0, ot: 0, car: 6000, ss: 0, hdhp: false, own: false } }),
                'return t.movingEnd(t.RULES.find(r=>r.id==="car_loan_deduction"), 100000)');
  eq('car loan rounds up, so it dies a step early', e, 129000);

  // Two children is $4,400 of credit. At $50 per $1,000 rounded up, the last
  // $50 goes at an excess of $87,001, so the edge sits at $287,000.
  e = await ask(page, base({ top: { status: 'single', age: 35, children: 2, income: 120000 } }),
                'return t.movingEnd(t.RULES.find(r=>r.id==="ctc_phaseout"), 200000)');
  eq('child credit edge for two children', e, 287000);

  // ------------------------------------------------------- the ACA cliff ---
  // 400% of the 2025 poverty guideline, which is what 2026 cover uses.
  eq('aca cliff, one person', await ask(page, base(), 'return t.acaCliff()'), 62600);
  eq('aca cliff, a couple',
     await ask(page, base({ top: { status: 'mfj', age: 35, children: 0, income: 120000 } }), 'return t.acaCliff()'),
     84600);                                                    // 4 x 21,150
  eq('aca cliff, a couple with two children',
     await ask(page, base({ top: { status: 'mfj', age: 35, children: 2, income: 120000 } }), 'return t.acaCliff()'),
     128600);                                                   // 4 x 32,150

  // ------------------------------------------------------ the age limits ---
  const lim = (age, id) => ask(page, base({ top: { status: 'single', age: age, children: 0, income: 120000 } }),
                               `return t.limitFor(t.LIMITS.find(l=>l.id==="${id}")).total`);
  eq('deferral at 40', await lim(40, 'deferral'), 24500);
  eq('deferral at 50 adds the catch-up', await lim(50, 'deferral'), 32500);
  eq('deferral at 59 is still the catch-up', await lim(59, 'deferral'), 32500);
  eq('deferral at 60 uses the super catch-up', await lim(60, 'deferral'), 35750);
  eq('deferral at 63 is the last super year', await lim(63, 'deferral'), 35750);
  eq('deferral at 64 drops back', await lim(64, 'deferral'), 32500);
  eq('ira at 49', await lim(49, 'ira'), 7500);
  eq('ira at 50', await lim(50, 'ira'), 8600);
  eq('hsa self at 54', await lim(54, 'hsa_self'), 4400);
  eq('hsa self at 55', await lim(55, 'hsa_self'), 5400);
  eq('hsa family at 55', await lim(55, 'hsa_family'), 9750);

  // A figure that follows filing status rather than age.
  const std = s => ask(page, base({ top: { status: s, age: 40, children: 0, income: 120000 } }),
                       'return t.limitFor(t.LIMITS.find(l=>l.id==="stdded")).total');
  eq('standard deduction, single', await std('single'), 16100);
  eq('standard deduction, joint', await std('mfj'), 32200);
  eq('standard deduction, head of household', await std('hoh'), 24150);
  eq('standard deduction, separate', await std('mfs'), 16100);

  // The charity-from-an-IRA figure must not appear before the age that unlocks it.
  const shows = (age, id) => page.evaluate(([a, i]) => {
    const t = window.__ts; t.S.age = a; t.render();
    return !!document.querySelector('.lim[data-limit="' + i + '"]');
  }, [age, id]);
  eq('no IRA charity figure at 60', await shows(60, 'qcd'), false);
  eq('IRA charity figure at 72', await shows(72, 'qcd'), true);
  eq('no extra deduction at 64', await shows(64, 'aged'), false);
  eq('extra deduction at 65', await shows(65, 'aged'), true);

  // ------------------------------------------------- who a rule reaches ---
  const applies = (over, id) => ask(page, base(over), `return t.applies(t.RULES.find(r=>r.id==="${id}"))`);
  eq('no senior deduction at 40', await applies({}, 'senior_deduction'), false);
  eq('senior deduction at 65', await applies({ top: { status: 'single', age: 65, children: 0, income: 120000 } }, 'senior_deduction'), true);
  eq('no senior deduction filing separately at 65',
     await applies({ top: { status: 'mfs', age: 65, children: 0, income: 120000 } }, 'senior_deduction'), false);
  eq('no tips bar without tips', await applies({}, 'tips_deduction'), false);
  eq('tips bar with tips', await applies({ oth: { tips: 5000, ot: 0, car: 0, ss: 0, hdhp: false, own: false } }, 'tips_deduction'), true);
  eq('no child credit bar without children', await applies({}, 'ctc_phaseout'), false);
  eq('no medicare surcharge at 35', await applies({}, 'irmaa_1'), false);
  eq('medicare surcharge shows at 63', await applies({ top: { status: 'single', age: 63, children: 0, income: 120000 } }, 'irmaa_1'), true);
  eq('no student loan bar filing separately',
     await applies({ top: { status: 'mfs', age: 35, children: 0, income: 120000 } }, 'student_loan_interest'), false);
  eq('no aca cliff on employer cover', await applies({}, 'aca_cliff'), false);
  // The earnings test only bites between 62 and full retirement age.
  const drawing = { oth: { tips: 0, ot: 0, car: 0, ss: 24000, hdhp: false, own: false } };
  eq('no earnings test at 60',
     await applies(Object.assign({ top: { status: 'single', age: 60, children: 0, income: 120000 } }, drawing),
                   'ss_earnings_test'), false);
  eq('earnings test at 64',
     await applies(Object.assign({ top: { status: 'single', age: 64, children: 0, income: 120000 } }, drawing),
                   'ss_earnings_test'), true);
  eq('no earnings test at 68',
     await applies(Object.assign({ top: { status: 'single', age: 68, children: 0, income: 120000 } }, drawing),
                   'ss_earnings_test'), false);

  // Every rule that survives its filters must land somewhere on the axis,
  // for every filing status. A rule that cannot be placed is a broken rule.
  const unplaceable = await page.evaluate(() => {
    const t = window.__ts, bad = [];
    for (const st of ['single', 'mfj', 'mfs', 'hoh']) {
      t.S.status = st; t.S.age = 66; t.S.children = 2;
      t.S.oth = { tips: 9000, ot: 9000, car: 3000, ss: 30000, hdhp: true, own: true };
      t.S.mix = { wage: 90000, bonus: 20000, rsu: 40000, int: 2000, qdiv: 3000,
                  ltg: 10000, stg: 1000, exempt: 4000 };
      for (const r of t.RULES) {
        if (!t.applies(r)) continue;
        const p = t.place(r);
        if (!p) { bad.push(st + '/' + r.id + ': no placement'); continue; }
        if (p.hi !== null && p.hi < p.lo) bad.push(st + '/' + r.id + ': end below start');
        if (!isFinite(p.lo)) bad.push(st + '/' + r.id + ': start is not a number');
      }
    }
    return bad;
  });
  eq('every applicable rule can be placed', unplaceable.join(' | '), '');

  // Each measure must rise with total income, or the bisection is meaningless.
  const nonMonotonic = await page.evaluate(() => {
    const t = window.__ts, bad = [];
    t.S.status = 'single'; t.S.age = 66; t.S.adj = { k401: 24500, hsa: 4400, iso: 20000 };
    t.S.mix = { wage: 100000, bonus: 20000, rsu: 30000, int: 2000, qdiv: 3000, ltg: 10000, stg: 1000, exempt: 5000 };
    const names = ['agi', 'magi', 'taxable', 'wages', 'amti', 'supplemental', 'provisional'];
    let prev = t.measure(0);
    for (let v = 5000; v <= 2000000; v += 5000) {
      const cur = t.measure(v);
      for (const n of names) if (cur[n] < prev[n] - 0.01) bad.push(`${n} fell at ${v}`);
      prev = cur;
    }
    return bad.slice(0, 5);
  });
  eq('every measure rises with income', nonMonotonic.join(' | '), '');

  // ------------------------------------------------------------- the UI ---
  await page.evaluate(() => {
    const t = window.__ts;
    t.S.status = 'single'; t.S.age = 35; t.S.children = 0; t.S.income = 180000;
    t.S.axis = 250000; t.S.off = {}; t.S.picked = null;
    t.S.mix = { wage: 180000, bonus: 0, rsu: 0, int: 0, qdiv: 0, ltg: 0, stg: 0, exempt: 0 };
    t.S.adj = { k401: 0, hsa: 0, iso: 0 };
    t.S.oth = { tips: 0, ot: 0, car: 0, ss: 0, hdhp: false, own: false };
    t.render();
  });

  const rows = await page.locator('.row').count();
  ok('the chart draws rows', rows > 15, rows, 'more than 15');
  eq('the marker is drawn', await page.locator('.mark').count(), 1);
  eq('the marker reads the income', (await page.locator('.markcap').innerText()).trim(), '$180,000');

  // At $180,000 taxable is 163,900, which is inside the 24% band.
  const marginal = await page.locator('.stat').first().locator('.v').innerText();
  eq('summary shows the right marginal rate', marginal.trim(), '24%');

  // No bar may leave its lane, and none may run off the right of the plot.
  const overflow = await page.evaluate(() => {
    const bad = [];
    for (const bar of document.querySelectorAll('.bar')) {
      const b = bar.getBoundingClientRect(), p = bar.parentElement.getBoundingClientRect();
      if (b.right > p.right + 1.5) bad.push('runs past the right edge');
      if (b.left < p.left - 1.5) bad.push('starts left of the plot');
      if (b.width < 0.5) bad.push('has no width');
    }
    return bad.slice(0, 4);
  });
  eq('no bar escapes its lane', overflow.join(' | '), '');

  // Clicking a row must open that row in the detail panel.
  await page.locator('.row').filter({ hasText: 'Roth IRA phase-out' }).first().click();
  const dTitle = (await page.locator('#detail h3').innerText()).trim();
  eq('a row opens in the detail panel', dTitle, 'Roth IRA phase-out');
  const srcCount = await page.locator('#detail .srcs a').count();
  ok('the detail panel cites a source', srcCount >= 1, srcCount, 'at least 1');
  const href = await page.locator('#detail .srcs a').first().getAttribute('href');
  ok('the source is a real link', /^https:\/\//.test(href), href, 'an https url');

  // Clicking a figure in the panel must work the same way.
  await page.locator('.lim').filter({ hasText: '401(k) and 403(b)' }).first().click();
  ok('a limit opens in the detail panel',
     (await page.locator('#detail h3').innerText()).includes('401(k)'),
     await page.locator('#detail h3').innerText(), 'the 401(k) limit');

  // Section filters must actually remove rows.
  const before = await page.locator('.row').count();
  await page.locator('#filters button[data-sec="rates"]').click();
  const after = await page.locator('.row').count();
  ok('a filter removes its rows', after < before, `${after} of ${before}`, 'fewer rows');
  await page.locator('#filters button[data-sec="rates"]').click();
  eq('a filter puts them back', await page.locator('.row').count(), before);

  // Moving the slider must move the marker.
  await page.locator('#income').fill('90000');
  await page.locator('#income').dispatchEvent('input');
  eq('the slider moves the marker', (await page.locator('.markcap').innerText()).trim(), '$90,000');

  // -------------------------------------------------------- the themes ---
  const bgOf = () => page.evaluate(() => getComputedStyle(document.body).backgroundColor);
  await page.locator('[data-theme-set="dark"]').click();
  const darkBg = await bgOf();
  await page.locator('[data-theme-set="light"]').click();
  const lightBg = await bgOf();
  ok('light and dark differ', darkBg !== lightBg, `${lightBg} / ${darkBg}`, 'two colors');
  eq('the theme choice sticks', await page.evaluate(() => localStorage.getItem('ts.theme')), 'light');

  // Text must stay readable against the paper in both themes.
  for (const theme of ['light', 'dark']) {
    await page.locator(`[data-theme-set="${theme}"]`).click();
    const ratio = await page.evaluate(() => {
      const lum = c => {
        const [r, g, b] = c.match(/\d+/g).map(Number).map(v => {
          v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4);
        });
        return .2126 * r + .7152 * g + .0722 * b;
      };
      const a = lum(getComputedStyle(document.body).color);
      const b = lum(getComputedStyle(document.body).backgroundColor);
      return (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
    });
    ok(`${theme}: body text has contrast`, ratio >= 7, ratio.toFixed(1), 'at least 7:1');
  }
  await page.locator('[data-theme-set="light"]').click();

  // ---------------------------------------------------------- the phone ---
  if (SHOTS) fs.mkdirSync(SHOTDIR, { recursive: true });
  if (SHOTS) await page.screenshot({ path: path.join(SHOTDIR, 'desktop-light.png'), fullPage: true });
  await page.locator('[data-theme-set="dark"]').click();
  if (SHOTS) await page.screenshot({ path: path.join(SHOTDIR, 'desktop-dark.png'), fullPage: true });
  await page.locator('[data-theme-set="light"]').click();

  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(180);

  const scrolls = await page.evaluate(() =>
    document.documentElement.scrollWidth - document.documentElement.clientWidth);
  ok('the phone layout does not scroll sideways', scrolls <= 1, scrolls + 'px over', '0px over');

  // Short labels must actually be in use, and must not be clipped.
  const clippedLabels = await page.evaluate(() => {
    let n = 0;
    for (const el of document.querySelectorAll('.row .txt'))
      if (el.scrollWidth > el.clientWidth + 1) n++;
    return n;
  });
  eq('no row label is clipped on a phone', clippedLabels, 0);
  eq('the phone uses the short label',
     await page.locator('.row').filter({ hasText: 'SS wage base' }).count(), 1);

  const tinyLabels = await page.evaluate(() => {
    let n = 0;
    for (const el of document.querySelectorAll('.row .txt, .stat .v, .lim .lt'))
      if (parseFloat(getComputedStyle(el).fontSize) < 10.5) n++;
    return n;
  });
  eq('no text shrinks below 10.5px on a phone', tinyLabels, 0);

  const clipped = await page.evaluate(() => {
    const w = document.documentElement.clientWidth, bad = [];
    for (const el of document.querySelectorAll('.stat, .lim, .filters button, .sliderhead .big')) {
      const r = el.getBoundingClientRect();
      if (r.right > w + 1) bad.push(el.className);
    }
    return bad.slice(0, 3);
  });
  eq('nothing hangs off the right on a phone', clipped.join(' | '), '');
  if (SHOTS) await page.screenshot({ path: path.join(SHOTDIR, 'phone-light.png'), fullPage: true });

  // ------------------------------------------------------- persistence ---
  await page.setViewportSize({ width: 1280, height: 1000 });
  await page.evaluate(() => { window.__ts.S.income = 315000; window.__ts.S.axis = 500000; });
  await page.locator('#age').fill('58');
  await page.locator('#age').dispatchEvent('input');
  await page.reload();
  await page.waitForFunction(() => window.__ts !== undefined);
  eq('the dialog stays shut for a returning reader', await page.locator('#scrim').isVisible(), false);
  eq('the age survives a reload', await page.locator('#age').inputValue(), '58');
  eq('the catch-up follows the saved age',
     await page.evaluate(() => {
       const t = window.__ts;
       return t.limitFor(t.LIMITS.find(l => l.id === 'deferral')).total;
     }), 32500);

  eq('no console errors', consoleErrors.join(' | '), '');

  await browser.close();

  console.log(`\n${pass} passed, ${fail} failed`);
  if (fail) {
    console.log('\nFAILURES:');
    for (const f of failures) console.log('  - ' + f);
  }
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
