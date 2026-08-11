# Tax Slider

A single page that shows where the 2026 federal tax edges fall for one person.
Move the slider and watch the brackets, the phase-outs, the cliffs, and the
contribution limits change.

Live at **<https://grantwilk.com/tax-slider/>**.

Federal only, tax year 2026 only. The page shows where the edges are. It does
not work out what you owe.

## What it is for

Most tax tools answer "what do I owe". This one answers a different question:
"what changes if my income moves". That question is hard to answer from a table,
because different rules read different measures of income. The tax brackets read
taxable income. The Roth IRA limit reads modified AGI. The Social Security tax
reads wages. The Medicare surcharge reads the income you had two years ago.

The page puts all of them on one axis so you can see them at the same time.

## How it works

You enter a mix of income: pay, bonus, vesting stock, interest, dividends,
gains. The slider scales that mix up and down and holds the proportions steady.
For every rule, the engine works out which measure of income it reads, then
solves backward to find where that threshold lands on the total-income axis. The
solve is a bisection, which works because every measure rises with total income.

A row only earns a bar if it has an edge on that axis. Contribution limits are
driven by your age, not your income, so they sit in a panel of their own rather
than pretending to have a position on a dollar scale.

## The shapes mean something

| Shape | Meaning |
|---|---|
| Solid block | A fixed band. The rate or rule applies inside it. |
| Fading right edge | A benefit that slides away as income rises. |
| Staircase | A benefit that drops in steps, not smoothly. |
| Hatched, hard left edge | A cliff. One dollar changes the answer. |

## Sources

Every figure traces to a primary document from the IRS, the SSA, or CMS. The
links are in the detail panel of each item, and the full research corpus is in
[`research/`](research/). Each URL in that corpus was checked to resolve and to
say what it is cited for.

## Building

`index.html` is generated. Do not edit it by hand.

```sh
python3 harness/build.py
```

- `harness/gen_rules.py` holds every figure, its shape, its explanation, and its
  source. It refuses to emit a rule set that fails its own checks.
- `harness/page.html` holds the markup, the styles, and the engine.
- `harness/build.py` puts the first into the second and writes `index.html`.

## Testing

```sh
cd harness
npm install          # first time only
node test.js         # add --shots to write screenshots, --headed to watch
```

The suite drives a real browser. It checks the arithmetic against values worked
by hand from the source documents, checks that every measure rises with income
so the bisection is valid, checks that every applicable rule can be placed for
every filing status, and checks the layout on a desktop and on a phone in both
themes.

`harness/verify-sources.js` re-checks that every cited URL still resolves.

## Not advice

This page is for illustration. It is not tax advice and it is not financial
advice. The figures come from public documents and they can contain errors. Tax
rules change, and your situation can have facts that this page does not model.
Speak to a qualified tax professional before you act on anything here.
