# OBBBA deduction phase-out rates, from the IRS worksheet

Leg C found the caps and the phase-out starts but not the rates. The rates are
on the face of the form, so they came from there rather than from a summary.

Source: [Draft Schedule 1-A (Form 1040), created 2025-11-04](https://www.irs.gov/pub/irs-dft/f1040s1a--dft.pdf),
saved locally as `f1040s1a--dft.pdf`, text in `s1a.txt`.

CAVEAT: this is the **2025** form. The arithmetic carries to 2026, but every
dollar figure below must be re-checked against Rev. Proc. 2025-32 before it goes
in the site, because some of these index and some do not. Flagged for the audit.

## MAGI used by all four (Part I)

MAGI = AGI, plus excluded Puerto Rico income, plus the Form 2555 foreign earned
income and housing exclusions, plus the Form 4563 exclusion. For a typical
domestic filer, MAGI equals AGI.

## The four computations

| Deduction | Cap | Phase-out starts (MAGI) | Rate | Rounding |
|---|---|---|---|---|
| Qualified tips | $25,000 | $150k single / $300k MFJ | $100 per $1,000 = **10%** | down to whole $1,000 |
| Qualified overtime | $12,500 single / $25,000 MFJ | $150k / $300k | $100 per $1,000 = **10%** | down to whole $1,000 |
| Car loan interest | $10,000 | $100k / $200k | $200 per $1,000 = **20%** | **up** to whole $1,000 |
| Senior deduction | $6,000 per person | $75k / $150k | **6%** of the excess | none, continuous |

### CORRECTION: there is no fixed end point for the first three

An earlier version of this note listed a single "fully gone at" figure for each
row. That is wrong for the first three, and the audit caught it.

The worksheet subtracts the reduction from the **actual** deduction, not from
the cap. Line 7 is the smaller of your tips or $25,000, and line 13 subtracts
the reduction from line 7. So the deduction reaches zero as soon as the
reduction equals *your* amount, which depends on what you entered.

    tips deduction   = min(tips, 25000) - 100 * floor(max(0, MAGI - start) / 1000)
    overtime         = min(ot,   cap)   - 100 * floor(max(0, MAGI - start) / 1000)
    car loan         = min(int,  10000) - 200 * ceil (max(0, MAGI - start) / 1000)
    senior           = 6000 - 0.06 * max(0, MAGI - start)     [per qualifying person]

Worked example. With the full $25,000 of tips the deduction ends at $400,000 of
MAGI, which is where the old figure came from. With $8,000 of tips it ends at
$230,000, because only $8,000 of reduction is needed. The end point moves with
the input.

**Consequence for the site.** These three bars cannot have fixed edges baked
into the data. Their right-hand edge is a function of the amount the user
enters, so the engine has to compute it per render. The senior deduction is the
one exception: it is always $6,000 per person, so its end point really is fixed
at $175,000 single and $250,000 joint.

Three details worth carrying into the code:

1. The rounding directions are not the same. Tips and overtime round the excess
   **down** to a whole $1,000, which favors the taxpayer. Car loan interest
   rounds **up**, which does not. The senior deduction uses no rounding at all.
2. Because tips and overtime round down, the phase-out is a staircase, not a
   ramp. The deduction only drops at each full $1,000 of excess MAGI.
3. The senior deduction is per qualifying person, so a married couple where both
   are 65 or older gets two of them, but each is reduced by the same 6% figure.

## Resolved: where the senior deduction ends for a couple who are both 65

Two legs flagged this, and third-party calculators disagree. Some publish
$250,000 and some publish $350,000. The worksheet decides it.

Lines 36a and 36b each enter **the amount from line 35**, which is the *same*
single figure. So the reduction applies to the per-person $6,000, and it applies
once, not to the couple's combined $12,000.

    line 35 = $6,000 - 0.06 x (MAGI - $150,000)
    line 35 hits zero when MAGI = $150,000 + $6,000/0.06 = $250,000

**$250,000 is correct**, for one spouse aged 65 or for both. A couple where both
qualify gets two copies of the same reduced amount, so their maximum is $12,000
at or below $150,000 MAGI, and their deduction is zero at $250,000.

The $350,000 figure is what you get by reducing the combined $12,000 instead of
the per-person $6,000: $12,000/0.06 = $200,000 of excess. That is the wrong
order of operations, and the worksheet does not do it.

## Age rule for the senior deduction

The 2025 form asks whether the person was born before January 2, 1961, which is
the standard way of writing "65 or older at the end of the tax year". For 2026
this becomes born before January 2, 1962.
