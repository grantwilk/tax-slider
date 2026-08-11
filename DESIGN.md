# Tax Slider — use cases, requirements, and design

Draft for review. Written after the research wave, before any UI code.

## 1. What the site is

You enter your income and your age. The site shows every federal 2026 rule you
are inside, every rule you are outside, and how far you are from each edge.

It is not a tax calculator. It does not tell you what you owe. A calculator
gives you one number and hides the structure. This shows the structure: the
bands, the cliffs, and the phase-outs your income sits among.

## 2. Who it is for

A W-2 employee at a large technology company. They hold RSUs, possibly ISOs and
ESPP shares. They have a 401(k), maybe an HSA, and a taxable brokerage account.
They are financially literate. They do not work in finance, and they do not know
what a phase-out range is until they see one.

They are somewhere between their twenties and retirement, so age changes the
answer as much as income does.

## 3. Use cases

| # | The question | What the site must show |
|---|---|---|
| U1 | "What bracket am I in?" | The marginal band, and that it is marginal, not a flat rate |
| U2 | "Can I contribute to a Roth IRA?" | Yes, no, or partially, with the phase-out range drawn |
| U3 | "What happens if I get a raise?" | Every edge above the current income, in order, with the distance to each |
| U4 | "My RSUs vest this year. What changes?" | The thresholds that move when a large one-time amount lands |
| U5 | "Should I exercise ISOs?" | Where AMT starts to bite, given this income |
| U6 | "What am I leaving on the table?" | Everything available at this income that has a contribution limit |
| U7 | "What do I lose by earning more?" | Every phase-out and cliff above the current income |
| U8 | "What changes when I turn 50? 60? 65?" | The age axis, with windows that open and one that closes |
| U9 | "Is my income mix costing me?" | The same total, split differently, changes NIIT and the capital gains stack |
| U10 | "Where is the nearest cliff?" | Cliffs called out separately from phase-outs, because the loss is total |

## 4. Requirements

### Correctness

- R1. Every figure is tax year 2026 and federal only.
- R2. Every entry cites a primary source, reachable from the detail panel.
- R3. Every threshold is verified against a worked example computed by hand.
- R4. Where a rule cannot be derived from the entered income, the site says so
  rather than guessing. The mandatory Roth catch-up is the known case: it keys
  off last year's wages from one employer.
- R5. Rounding is modelled where it is visible. Tips and overtime phase out in
  $1,000 steps, car loan interest rounds the other way, and the senior deduction
  is continuous. These differ near an edge and must not be smoothed.

### Behavior

- R6. Inputs persist between visits.
- R7. A first-run dialog asks for the minimum: filing status, age, income.
- R8. Everything recomputes as the income changes, with no page reload.
- R9. Light and dark, following the system and overridable.
- R10. Phone and desktop layouts, no horizontal page overflow on a phone.

### Language

- R11. All prose in Simplified Technical English. Descriptive sentences 25 words
  or fewer, procedural 20 or fewer.
- R12. One term per concept for the whole page. "Phase-out" never becomes
  "reduction" or "taper" elsewhere.
- R13. No advice. The site states what is true at an income, not what to do.
- R14. A disclaimer sits at the foot of the page, in dim text, below the notes.
  It must say three things: the page is not tax or financial advice, the figures
  can contain errors, and a qualified professional should be consulted before
  acting. It must not use a banner, a modal, or a colored alert box, because it
  is a standing condition and not a warning about one action.

Draft wording, in Simplified Technical English:

> This page is for illustration. It is not tax advice and it is not financial
> advice. The figures come from public IRS, SSA, and CMS documents for tax year
> 2026, and they can contain errors. Tax rules change, and your situation can
> have facts that this page does not model. Speak to a qualified tax
> professional before you act on anything here.

## 5. The central design problem, and the answer

Different rules key off different measures of income:

| Measure | Drives |
|---|---|
| Taxable income | Ordinary brackets, capital gains breakpoints, QBI |
| AGI | Medical floor, charitable ceilings |
| MAGI | Roth IRA, NIIT, IRMAA, the new OBBBA deductions, ACA credits |
| FICA wages | Additional Medicare Tax, Social Security wage base |
| Prior-year wages, one employer | Mandatory Roth catch-up |
| Alternative minimum taxable income | AMT exemption phase-out |

Putting all of those on one axis naively would be wrong, because $200,000 of
taxable income and $200,000 of MAGI are not the same point in a person's life.

**The answer, and the reason the site is called a slider.** You enter an income
*mix*, not a single number. The axis is your **total income**. The proportions
of the mix are held constant as the axis moves. Every threshold is then solved
backwards into total-income space: for a rule that triggers at MAGI of
$150,000, the site finds the total income at which *this* person's MAGI reaches
$150,000, and draws the edge there.

One vertical line marks where you are. Sliding it answers "what changes if I
earn more", which is the actual question.

This works because every measure rises monotonically with total income once the
mix is fixed, so each edge can be found by binary search over the engine. It
also captures the mix effects correctly and for free: a person with $300,000 of
wages and a person with $150,000 of wages plus $150,000 of long-term gains get
different NIIT edges, because the engine is evaluating their real mix.

## 5a. What the audit changed

The completeness audit checked the corpus against the primary documents. Three
of its findings change the build rather than only the content.

**Ask for gross pay, never for Box 1.** Pre-tax payroll items are already out of
W-2 Box 1: the 401(k) deferral, an HSA funded through payroll, the FSA, the
health premium, transit, and tuition help. If the site takes Box 1 as "wages"
and then subtracts the 401(k) again, it double-counts and every downstream edge
is wrong. So the wage input asks for **total pay before pre-tax deductions**,
and the label must say so, because a person looking at a W-2 will reach for
Box 1 by default. This also makes the slider mean the right thing: sliding it
models a raise on gross pay.

**Three phase-out edges move with the input.** For the tips, overtime, and car
loan deductions, the worksheet subtracts the reduction from the *actual* amount,
not from the cap. Someone with $8,000 of tips loses the deduction at $230,000 of
MAGI, not at the $400,000 that applies to someone with the full $25,000. Those
bars therefore cannot have fixed edges in the data. The engine computes the
right edge per render. The senior deduction is the exception and is fixed.

**The Social Security wage base is per employer, not per person.** Change jobs
mid-year and both employers withhold up to the full $184,500 base, which can
over-withhold by $11,439. It comes back as a credit, but only if you know to
claim it. Drawing the wage base as one hard ceiling would be wrong, so it gets a
note and a second-employer case rather than a single line.

The audit also named content the corpus had missed that this audience will hit:
the Form 1099-B basis problem on RSU and ESPP shares, where the broker reports a
basis near zero and the unwary pay tax twice; wash sales triggered by a routine
quarterly vest or dividend reinvestment while harvesting losses on employer
stock; the fact that capital gains bands run on taxable income while the 3.8%
surtax runs on MAGI, giving real top rates of 23.8% and 40.8%; the Section 121
home sale exclusion; and the three separate Roth five-year clocks. All are
folded into the rule set.

One negative finding is worth stating because it is easy to get wrong in the
other direction. **None of the four new deduction amounts index for 2026.** The
statute writes no inflation clause for them while the same Act writes one
explicitly for SALT, QSBS, and the estate exclusion; Revenue Procedure 2025-32
omits all four; and all four expire after 2028. They are frozen.

## 6. Inputs

Kept small by default, deep when opened.

**Always visible**
- Filing status: single, married filing jointly, married filing separately,
  head of household
- Age (plus spouse's age when filing jointly)
- Total income

Filing status is not a minor setting. It moves almost every threshold in the
corpus, and married filing separately is punishing in ways people do not expect:
the Net Investment Income Tax starts at $125,000 instead of $250,000, the
capital loss offset halves to $1,500, and the Roth IRA phase-out runs from $0 to
$10,000, which shuts out nearly everybody. The site must show those, because
they are exactly the kind of thing a person only learns after choosing.

**Income mix (collapsed, defaults to all wages)**
- Wages and salary
- Bonus and other supplemental pay
- RSU vesting
- Interest
- Qualified dividends
- Ordinary dividends
- Long-term capital gains
- Short-term capital gains
- Tax-exempt municipal interest

**Adjustments you control (collapsed)**
- Traditional 401(k) deferral
- HSA contribution

These matter because they lower AGI, which can move you back under an edge.
Showing that is one of the more useful things the site can do.

**Situation toggles (collapsed)**
- I buy my own health coverage → unlocks the ACA premium tax credit and its cliff
- I have a high-deductible health plan → unlocks HSA rows
- My employer's plan offers Roth → affects the catch-up rules
- Household size → needed for the poverty-level calculation

## 7. Layout

A direct descendant of Paws and Effect, because the shape of the problem is the
same: many bands over one axis, with a marker showing where you are.

```
  masthead: Tax Slider          [filing status] [age] [income]  [theme]
  ---------------------------------------------------------------
  AT YOUR INCOME                                    $210,000
    columns, one per section, listing what applies right now
    NEXT EDGES: $4,200 -> Roth IRA phase-out starts   $12,000 -> 24% bracket
  ---------------------------------------------------------------
  [section filters]                     legend
  ---------------------------------------------------------------
  ruler:  $0      $100k      $200k      $300k      $400k ...
  |                            | <- your income
  RATES
    10% bracket        ####
    12% bracket            ########
    ...
  ACCOUNTS
    Roth IRA, full      ##############
    Roth IRA, partial                 ~~~~
    ...
  ---------------------------------------------------------------
  detail panel: title, plain-English explanation, the numbers, the source
  ---------------------------------------------------------------
  footer note
```

The chart scrolls sideways on desktop and stacks on a phone, exactly as the
other site does. The axis runs from $0 to $1.5M, which covers the last edge
(the AMT exemption reaching zero at $1,280,400 joint).

## 8. Bar shapes

| Shape | Meaning | Example |
|---|---|---|
| Solid band | Applies between two incomes | The 22% bracket |
| Gradient | Phases out across this range | Roth IRA eligibility |
| Hard edge | A cliff. Everything is lost at one dollar | ACA subsidy at 400% of poverty |
| Faded right | Applies above here, with no upper end | Net Investment Income Tax |
| Step pattern | Phases out in discrete steps | Tips and overtime deductions |
| Diamond | A single point | Social Security wage base |

The cliff shape must be visually distinct from the gradient. A person needs to
see at a glance which edges cost a little and which cost everything.

## 9. Engine

Pure functions, no framework, inline in one HTML file.

```
  inputs -> mix
         -> measures(totalIncome, mix, adjustments, situation)
              { agi, magi, taxableIncome, ficaWages, amti, ... }
         -> for each rule: evaluate(measures) -> { applies, amount, distanceToEdge }
         -> for each rule threshold: solve back to total income by bisection
         -> render bars, marker, "at your income" panel
```

Each rule is one data object, the way each timeline entry was on the other site:
an id, a section, a title, the measure it keys off, its thresholds by filing
status, its shape, its plain-English text, and its sources.

## 10. Verification plan

- V1. Hand-worked test cases at chosen incomes, checked against the engine.
- V2. Property tests: every phase-out reaches zero exactly at its stated end;
  no rule is non-monotonic; bisection converges for every threshold.
- V3. Browser suite: input persistence, first-run dialog, theme, filters,
  phone overflow, keyboard access, contrast.
- V4. Source check: every cited URL resolves. Already passing at 124 of 124.
- V5. Blind review panel on the finished page.

## 11. Known limits, to be stated on the page

- Federal only. No state or local tax.
- One tax year, 2026.
- It models thresholds, not liability. It does not tell you what you owe.
- The mandatory Roth catch-up test uses last year's wages from one employer,
  which the site cannot infer.
- IRMAA uses income from two years earlier, so today's income is a forecast.
