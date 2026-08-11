# G — Audit of the 2026 federal tax research corpus

Audit date: August 11, 2026. Scope: files A, B, C, C2, D, E, and F in this directory.

**Method.** I read all seven files. I then compared every high-stakes dollar figure against the
primary documents in this directory. The documents are `rp-25-32.txt`, `n-25-67.txt`,
`rp-25-19.txt`, `rp-25-25.txt`, `s1a.txt`, `sec1202.txt`, and `obbba.htm`. I did not rewrite
any file.

**Headline.** The dollar figures are clean. I checked more than 50 figures against the primary
documents and found one wrong number. The real risk is elsewhere. Three formulas are wrong or
incomplete, several phase-out endpoints are stated as fixed when they are not, and 44 rules that
this audience will meet are absent from all seven files.

**Counts.**

| Category | Count |
|---|---|
| Gaps — BLOCKING | 7 |
| Gaps — IMPORTANT | 19 |
| Gaps — NICE TO HAVE | 18 |
| Conflicts between files | 9 |
| Errors and defects | 12 confirmed, 2 unverified |

---

# 1. GAPS

A gap is a 2026 federal rule, threshold, limit, or phase-out that this audience meets and that no
file documents.

## 1.1 Payroll and the Form W-2

### G1. Excess Social Security tax after a mid-year change of employer — BLOCKING

File A calls the $184,500 OASDI wage base "a hard ceiling." The ceiling is per employer, not per
person. A person who changes employer in 2026 restarts at zero with the new employer. Both
employers withhold 6.2% up to $184,500 each. The employee recovers the excess as a refundable
credit under § 31(b), on Schedule 3 of Form 1040.

The maximum single-employer withholding is $11,439.00. A person with two employers can therefore
have up to $11,439.00 of excess OASDI withheld. No file states this. A site that models a job
change without this rule overstates the tax bill by up to five figures.

Two related points are also absent. First, the employer cannot refund its own 6.2% share, and the
employee cannot claim it. Second, Medicare has no wage base, so no parallel credit exists for the
1.45% or the 0.9% Additional Medicare Tax.

### G2. Which amounts are already out of Box 1 of the Form W-2 — BLOCKING

No file states which pre-tax items the employer already removed from wages before the Form W-2 is
issued. A calculator that subtracts them a second time is wrong by the full amount.

Already excluded from Box 1:

- Pre-tax 401(k) and 403(b) elective deferrals
- HSA contributions made through payroll under a § 125 cafeteria plan
- Health FSA and dependent care FSA salary reductions
- Employee-paid health, dental, and vision premiums under a § 125 plan
- § 132(f) transit and parking amounts
- § 127 educational assistance up to $5,250

Separate deductions that a user must enter:

- Traditional IRA contributions
- HSA contributions made directly to the trustee, outside payroll (Form 8889, line 2)
- One half of self-employment tax

File B says the HSA limit covers employer and employee amounts together. That is correct, but it
is a limit rule, not a deduction rule. The two are different and no file separates them.

### G3. Supplemental wage withholding — the other method, and the fix — IMPORTANT

File D covers the 22% flat rate and the 37% rate above $1,000,000. It omits two things.

First, the flat rate is optional. An employer can instead use the aggregate method and withhold on
the combined regular and supplemental payment at Form W-4 rates. Many large employers do this for
bonuses. The withheld amount then differs from 22%.

Second, an employee cannot elect a different flat rate, but an employee can raise total
withholding. The routes are extra withholding on Step 4(c) of Form W-4, or an estimated tax
payment. File D names the 22% shortfall but names no remedy.

### G4. Employer educational assistance, § 127 — IMPORTANT

The 2026 exclusion is $5,250 per employee per year. OBBBA § 70412 made permanent the rule that
lets the exclusion cover employer payments of principal or interest on a qualified education loan.
Rev. Proc. 2025-32 § 2.09 states that the $5,250 amount first indexes for years after 2026, so the
2026 figure is $5,250. Large technology employers commonly offer both tuition reimbursement and
student loan repayment. No file documents this.

### G5. Nonqualified deferred compensation and § 409A — IMPORTANT

Senior employees at large technology companies commonly hold a nonqualified deferred compensation
plan. Section 409A sets the election rules. A deferral election for 2027 compensation must
generally be made by December 31, 2026. For performance-based compensation over a period of at
least 12 months, the deadline is 6 months before the end of the period. A first-year participant
has 30 days from eligibility.

A failure makes all deferred amounts taxable at once. The employee then owes a 20% additional tax
plus premium interest under § 409A(a)(1)(B). No file mentions § 409A.

### G6. Commuter benefits, § 132(f) — NICE TO HAVE

For 2026 the monthly exclusion is $340 for transit passes and commuter highway vehicles, and $340
for qualified parking (Rev. Proc. 2025-32 § 4.16). OBBBA § 70112 permanently repealed the
qualified bicycle commuting reimbursement.

### G7. Group-term life insurance imputed income, § 79 — NICE TO HAVE

Employer-paid group-term life coverage above $50,000 creates imputed income. The amount comes from
the Table I rates in Reg. § 1.79-3(d)(2), not from the premium the employer paid. It appears in
Box 1 and Box 12 code C of the Form W-2.

### G8. 401(k) employer match true-up — NICE TO HAVE

A per-paycheck match formula can underpay an employee who reaches the $24,500 deferral limit early
in the year. A true-up corrects it after year end. This is plan design, not federal tax law. A
site must label it as such and must not present it as a federal rule.

### G9. Employer adoption assistance exclusion, § 137 — NICE TO HAVE

The 2026 exclusion is $17,670, with the same MAGI phase-out as the credit ($265,080 to $305,080).
Rev. Proc. 2025-32 § 4.18 gives it. File C covers the § 23 credit but not the § 137 exclusion.

## 1.2 Equity compensation

### G10. Form 1099-B cost basis for RSU and ESPP shares — BLOCKING

File D makes this point for nonstatutory options only. It applies with more force to RSUs and to
ESPP shares, which this audience holds.

Under Reg. § 1.6045-1(d)(6)(iii), a broker cannot include the compensation component in the basis
it reports for a share acquired under an equity plan on or after January 1, 2014. For an RSU the
employee usually pays nothing, so the broker reports a basis at or near zero. The true basis is the
vest-date value already taxed as wages. For an ESPP share the broker reports the discounted
purchase price, not the price plus the ordinary income part.

A person who uses the Form 1099-B figure pays tax twice on the same dollars. The correction goes on
Form 8949 with code B and a basis adjustment in column (g). No file states this for RSUs or ESPP.

### G11. Wash sale caused by a vest, an ESPP purchase, or a reinvested dividend — BLOCKING

File D states the wash sale rule correctly in the abstract. It never connects the rule to the
events that this audience cannot control.

The 61-day window runs 30 days before and 30 days after a loss sale. An RSU vest inside that window
is an acquisition of substantially identical stock. So is an ESPP purchase date. So is a dividend
reinvestment. Each one disallows part or all of the loss.

A technology employee with a quarterly vest schedule has an acquisition roughly every 90 days. Any
tax-loss harvest on employer stock therefore needs a date check. A site that offers loss harvesting
without this rule produces deductions that do not exist.

### G12. Phantom income from a vest before a price fall — IMPORTANT

The wage income equals the vest-date value. That amount is fixed. A later price fall does not
reduce it. The fall creates a capital loss instead, and § 1211(b) caps the ordinary-income use of
that loss at $3,000 per year ($1,500 MFS).

A person whose shares vest at $100 and fall to $20 during a trading blackout owes tax on $100 per
share. The $80 loss offsets capital gains without limit, then reaches ordinary income at $3,000 per
year. The remainder carries forward. Files A, D, and the loss cap all exist separately. The
interaction is nowhere.

### G13. Lot identification on a sale — IMPORTANT

A person who holds several lots of the same stock chooses which lot to sell. Under
Reg. § 1.1012-1(c) the identification must reach the broker at or before settlement, and the broker
must confirm it in writing within a reasonable time. Without an identification the broker default
applies, which is first-in, first-out for stock.

This choice drives both the gain amount and the holding period. No file documents it.

### G14. Equity compensation is never qualified business income — IMPORTANT

Section 199A(d)(1)(B) excludes the trade or business of performing services as an employee.
Section 199A(c)(4)(A) excludes reasonable compensation. RSU income, NSO spread, ESPP ordinary
income, and salary are therefore never QBI. File C documents the QBI thresholds but never states
this exclusion. A reader with a side business will ask.

### G15. ESPP § 423(c) income and FICA — NICE TO HAVE

File D states that no income tax withholding applies to the § 423(c) compensation amount. It does
not state that the amount is also outside Social Security and Medicare tax, under § 3121(a)(22).
The same exclusion covers an ISO disqualifying disposition.

### G16. Dual basis on ISO shares at sale — NICE TO HAVE

An ISO exercise creates two different bases. The regular tax basis is the exercise price. The AMT
basis is the exercise price plus the § 56(b)(3) adjustment. At sale the taxpayer computes two gains
and reports the difference on Form 6251 line 2k. File D mentions the AMT capital loss carryforward
but never sets out the dual-basis computation.

### G17. Net unrealized appreciation on employer stock in a 401(k) — NICE TO HAVE

Section 402(e)(4) lets a person take a lump-sum distribution of employer stock in kind. The person
pays ordinary tax on the plan's cost basis only. The appreciation becomes long-term capital gain at
sale. This matters to a long-tenured employee whose 401(k) holds company stock.

## 1.3 Investment income

### G18. The net investment income tax and the capital gains brackets use different bases — BLOCKING

File A and file D each describe the two rules correctly on their own. Neither states how they
interact, and the interaction decides the answer.

- The 0%, 15%, and 20% capital gains bands are measured against **taxable income**. Taxable income
  is after the standard deduction or itemized deductions.
- The 3.8% NIIT threshold is measured against **MAGI**, which is close to AGI. MAGI is before those
  deductions, and it includes wages.

A single filer can therefore sit in the 15% capital gains band and still owe the 3.8% tax. The
combined top rates that no file states:

| Income type | Top federal rate with NIIT |
|---|---|
| Long-term capital gain and qualified dividends | 20% + 3.8% = 23.8% |
| Short-term capital gain, interest, non-qualified dividends | 37% + 3.8% = 40.8% |

One more point is missing. Inside the NIIT phase-in band the marginal cost of an extra dollar of
gain is higher than 3.8%, because the dollar raises MAGI and raises net investment income at the
same time.

### G19. Gain on the sale of a main home, § 121 — BLOCKING

The exclusion is $250,000 for a single filer and $500,000 on a joint return. Both figures are fixed
in statute and neither indexes. The taxpayer must have owned and used the home as a main home for
at least 2 of the 5 years before the sale. The full exclusion is available once every 2 years. A
partial exclusion applies for a move caused by work, health, or an unforeseen circumstance.

File D mentions the excluded gain only as an item outside net investment income. No file gives the
figures or the tests. A site that shows a large taxable gain on a home sale is wrong by up to
$500,000 of income.

### G20. Capital gain distributions from funds — IMPORTANT

A mutual fund or ETF reports capital gain distributions in Box 2a of Form 1099-DIV. These are
long-term for the shareholder whatever the holding period of the fund shares. They are unavoidable.
An investor receives them without selling anything. This is a common surprise in a taxable
brokerage account and no file covers it.

### G21. The marriage penalty map — IMPORTANT

File A notes that the MFS 37% band starts at exactly half the joint figure. No file states where
the joint figure is **not** twice the single figure. For a dual-income technology couple this
decides the result.

| Item | Single | MFJ | MFJ is twice Single? |
|---|---|---|---|
| 10% through 32% band edges | $12,400 to $256,225 | $24,800 to $512,450 | Yes |
| 37% band start | $640,600 | $768,700 | **No** (twice would be $1,281,200) |
| 15% capital gains ceiling | $545,500 | $613,700 | **No** (twice would be $1,091,000) |
| NIIT threshold | $200,000 | $250,000 | **No** (twice would be $400,000) |
| Additional Medicare Tax | $200,000 | $250,000 | **No** |
| AMT exemption | $90,100 | $140,200 | **No** (twice would be $180,200) |
| SALT phase-down start | $505,000 | $505,000 | **No** — identical, not doubled |
| Roth IRA phase-out start | $153,000 | $242,000 | **No** |
| Standard deduction | $16,100 | $32,200 | Yes |
| AMT phase-out start | $500,000 | $1,000,000 | Yes |

The NIIT and Additional Medicare Tax rows bite at income levels that two technology salaries reach
easily. The SALT row is the largest single penalty in the table.

### G22. Foreign tax paid through a fund — NICE TO HAVE

Box 7 of Form 1099-DIV reports foreign tax paid by an international fund. A taxpayer can claim the
credit without Form 1116 when the total is $300 or less ($600 on a joint return) and all the income
is passive. Above that figure Form 1116 is required.

### G23. Digital assets — NICE TO HAVE

The wash sale rule in § 1091 covers "stock or securities." Digital assets are property, not
securities, so the rule does not reach them. Broker reporting on Form 1099-DA began for 2025
transactions, and basis reporting is phased in.

### G24. Bond premium, market discount, and original issue discount — NICE TO HAVE

Boxes 10 through 13 of Form 1099-INT and Form 1099-OID carry adjustments that change taxable
interest. The § 6045 covered-security rules split reporting by acquisition date. This is relevant
to a brokerage account that holds individual bonds.

## 1.4 Retirement

### G25. The Roth five-year rules — BLOCKING

File B promotes both the backdoor Roth and the mega-backdoor Roth. It never states the five-year
rules. There are three separate clocks.

1. **Roth IRA qualified distribution clock, § 408A(d)(2).** Earnings come out tax-free only after
   5 tax years from the first contribution to any Roth IRA, and after age 59½, death, disability,
   or a first home purchase. The clock starts on January 1 of the year of the first contribution.
   It is one clock per person, not one per account.
2. **Conversion recapture clock, § 408A(d)(3)(F).** A converted amount withdrawn within 5 years,
   before age 59½, carries the 10% additional tax even though the amount is not taxable income.
   Each conversion has its own clock. A backdoor Roth is a conversion, so a user who follows file B
   starts a new clock every year.
3. **Designated Roth 401(k) clock, § 402A(d)(2).** This clock is separate from the Roth IRA clock
   and does not move to a new employer. A rollover to a Roth IRA picks up the Roth IRA clock
   instead.

A site that tells a user "Roth withdrawals are tax free" without these three rules is wrong.

### G26. Excess elective deferral after a mid-year job change — IMPORTANT

File B states that the $24,500 limit applies per person across all employers. It stops there. A
person with two employers in 2026 can exceed the limit, because neither plan sees the other.

The correction has a hard calendar. The participant must notify a plan by March 1, 2027. The plan
must distribute the excess and its earnings by April 15, 2027. If the deadline passes, the excess
is taxed in 2026 and taxed again when it finally comes out of the plan. Neither plan is required to
find the problem.

### G27. Roth 401(k), pre-tax 401(k), and after-tax 401(k) — IMPORTANT

Three buckets exist inside one plan and no file separates them.

| Bucket | Counts against | 2026 limit |
|---|---|---|
| Pre-tax elective deferral | § 402(g) | $24,500 combined |
| Designated Roth elective deferral | § 402(g) | $24,500 combined |
| Voluntary after-tax (non-Roth) | § 415(c) only | Room up to $72,000 total |

The key fact is that pre-tax and Roth deferrals share one $24,500 limit. A site that offers
separate inputs for each, without one shared cap, lets a user contribute $49,000.

File B describes after-tax contributions only inside the mega-backdoor Roth block. It never
contrasts them with Roth deferrals.

### G28. Contribution deadlines — IMPORTANT

- 401(k) elective deferrals for 2026 must come out of 2026 pay. The deadline is December 31, 2026.
- Traditional and Roth IRA contributions for 2026 can be made through April 15, 2027.
- HSA contributions for 2026 can be made through April 15, 2027.
- An extension of time to file does not extend either April 15, 2027 deadline.

No file gives any of these dates.

### G29. Rollover mechanics at a job change — IMPORTANT

Two rules matter and no file states either.

First, a plan must withhold 20% from an eligible rollover distribution that it pays to the
participant. A direct trustee-to-trustee transfer avoids the withholding. A person who takes the
check must replace the withheld 20% from other money within 60 days, or that part becomes a taxable
distribution.

Second, § 408(d)(3)(B) allows one IRA-to-IRA 60-day rollover in any 12-month period, counted across
all of a person's IRAs. Trustee-to-trustee transfers and conversions do not count against it.

### G30. No recharacterization of a Roth conversion — NICE TO HAVE

A Roth conversion made in 2026 cannot be undone. Section 408A(d)(6)(B)(iii) removed
recharacterization of conversions for 2018 and later years. Recharacterization of a regular
contribution between a traditional IRA and a Roth IRA is still allowed.

## 1.5 Deductions and credits

### G31. Miscellaneous itemized deductions stay repealed — IMPORTANT

OBBBA § 70110 made the repeal permanent. For 2026 a W-2 employee cannot deduct investment advisory
fees, unreimbursed employee business expenses, tax preparation fees, or a home office. No file says
this. A financially literate reader will look for these lines.

### G32. Carryforward of contributions blocked by the new 0.5% floor — IMPORTANT

File C documents the floor. It does not document the carryforward rule that OBBBA § 70425(a)(2)
added at § 170(d)(1)(C). An amount disallowed by the floor carries forward only from a year in
which the taxpayer also exceeded the AGI percentage limit. In a normal year the disallowed amount
is simply lost. That result is the opposite of what a reader will assume.

### G33. The overall cap on the QBI deduction — IMPORTANT

Section 199A(a) limits the deduction to the lesser of the combined QBI amount, or 20% of taxable
income reduced by net capital gain. File C gives the 20% rate and the thresholds. It omits the
taxable-income cap. A user with large long-term gains gets a much smaller QBI deduction than the
20%-of-QBI figure suggests.

### G34. Gifts of appreciated stock — NICE TO HAVE

A gift of long-term appreciated stock to a public charity produces a deduction at fair market
value, and the donor recognizes no capital gain. The ceiling is 30% of the contribution base, with
a 5-year carryforward. File C gives the 30% figure but not the no-gain rule, which is the reason
the strategy exists.

### G35. Excess business loss limit — NICE TO HAVE

For 2026 the § 461(l)(3) amount is $256,000, or $512,000 on a joint return
(Rev. Proc. 2025-32 § 4.31). It applies to a reader with a side business.

## 1.6 Filing and procedure

### G36. Filing status and the cost of filing separately — IMPORTANT

Marital status on December 31, 2026 sets the filing status for the whole year. No file states this.
No file lists what married filing separately costs, and the list is long.

- The Roth IRA phase-out range collapses to $0 through $10,000.
- The traditional IRA deduction phase-out range collapses to $0 through $10,000.
- The student loan interest deduction is unavailable.
- The American Opportunity Credit and Lifetime Learning Credit are unavailable.
- The child and dependent care credit is generally unavailable.
- The senior deduction, the tips deduction, and the overtime deduction are unavailable.
- The capital loss limit halves to $1,500.
- The NIIT and Additional Medicare Tax thresholds halve to $125,000.

### G37. Nonresident and dual-status filers — IMPORTANT

A large technology employer holds many visa holders. No file covers them. The missing items are the
substantial presence test in § 7701(b)(3), the 31-day and 183-day counts with the 1/3 and 1/6
weighting, the first-year and dual-status elections, the FICA exemption for an F-1 or J-1
nonresident student under § 3121(b)(19), and the rule that a nonresident alien cannot take the
standard deduction.

### G38. Filing and payment deadlines — IMPORTANT

The 2026 return is due April 15, 2027. Form 4868 gives an automatic extension to October 15, 2027.
The extension moves the filing date only. Tax remains due April 15, 2027, and interest and the
failure-to-pay penalty run from that date. No file states any of this.

### G39. Interest and penalties on a late payment — NICE TO HAVE

The underpayment interest rate comes from § 6621 and changes each quarter. The failure-to-pay
penalty is 0.5% per month, capped at 25%. The failure-to-file penalty is 5% per month, capped at
25%. Rev. Proc. 2025-32 § 4.52 sets the minimum late-filing addition at the lesser of $535 or the
full tax, for a return filed more than 60 days late.

### G40. Foreign account reporting — NICE TO HAVE

FinCEN Form 114 (FBAR) is required when the aggregate value of foreign financial accounts exceeds
$10,000 at any time in the year. Form 8938 under § 6038D uses separate thresholds, starting at
$50,000 on the last day of the year, or $75,000 at any time, for a single filer in the United
States.

### G41. Form 1099-K threshold — NICE TO HAVE

OBBBA § 70432 restored the third-party network reporting threshold to more than $20,000 and more
than 200 transactions. This is separate from the § 6041 threshold of $2,000 in
Rev. Proc. 2025-32 § 2.15.

## 1.7 Scope

### G42. No state conformity warning — IMPORTANT

The corpus is federal by design, and every file says so. No file warns that several documented
items have no state analogue. This audience concentrates in California, Washington, New York, and
Massachusetts. Three examples:

- California does not allow a deduction for HSA contributions, and it taxes HSA earnings.
- California does not conform to the § 1202 QSBS exclusion.
- California runs its own AMT and taxes the ISO spread under it, with different figures.

A site that shows a federal-only result to a California reader understates the total tax by a large
margin. The site needs a stated boundary, not a state module.

### G43. Which health premiums an HSA can pay — NICE TO HAVE

Section 223(d)(2)(C) allows HSA payment of COBRA premiums, health coverage premiums while
receiving unemployment compensation, and Medicare premiums other than Medigap. Ordinary health
insurance premiums are not qualified expenses. This matters at a layoff and at age 65.

### G44. The FSA grace period — NICE TO HAVE

File B states that a plan can offer a carryover or a grace period, but not both. It does not give
the grace period length, which is 2 months and 15 days after the end of the plan year.

---

# 2. CONFLICTS

## C1. The senior deduction phase-out endpoint for a couple where both spouses are 65 or over

| File | Value stated |
|---|---|
| A | $250,000, with confidence marked "medium" |
| C | $250,000 |
| C2 | $250,000, resolved |
| **E** | **$350,000 for a $12,000 base**, and "phases out over a $200,000 band from $150,000" |

**Correct value: $250,000. File E is wrong.**

Two independent documents in this directory settle it.

First, `s1a.txt`. Line 35 computes one figure: $6,000 minus 6% of MAGI above the threshold. Lines
36a and 36b each enter **the amount from line 35**. The same reduced figure is entered twice. The
reduction therefore applies to the per-person $6,000, not to the couple's combined $12,000.

Second, the statute. OBBBA § 70103 adds § 151(d)(5)(C). Clause (i) allows "$6,000 for each
qualified individual." Clause (iii)(I) reduces "the $6,000 amount in clause (i)" by 6% of MAGI over
the threshold. The reduced amount is the per-individual amount. It reaches zero at
$150,000 + $6,000 ÷ 0.06 = $250,000, whether one spouse or both spouses qualify.

**Verification of the C2 reasoning, as requested.** C2 is correct on every point. It is correct
that the worksheet decides it, correct that lines 36a and 36b enter the same figure, correct that
$350,000 comes from reducing the combined $12,000 instead of the per-person $6,000, and correct
that this is the wrong order of operations. The statute confirms the worksheet, so the conclusion
rests on two independent sources rather than one. File A can raise its confidence from medium to
high. File E needs the correction.

## C2. Whether Form 1040-ES for 2026 exists

File A cites "Form 1040-ES (2026)" twice, as a source for the senior deduction and for the
self-employment tax worksheet. File D states: "IRS has not published a Form 1040-ES for 2026 that
this research could locate."

**File D is wrong.** The research date is August 11, 2026. The IRS publishes Form 1040-ES for a
year in January of that year, because the first installment is due April 15. The form has existed
for about seven months.

## C3. Section number for cafeteria plans in Rev. Proc. 2025-32

File B cites "section 3.15, Cafeteria Plans." File F cites "§4.15."

**File F is correct.** `rp-25-32.txt` places cafeteria plans at § 4.15. Section 3 of that document
covers 2025 items that OBBBA modified, and it has only two paragraphs.

## C4. Section number for the aged and blind standard deduction

File E cites "Rev. Proc. 2025-32 §2.14(3)." File A cites "§ 4.14(3)."

**File A is correct.** `rp-25-32.txt` § 4.14(3) gives the $1,650 and $2,050 amounts. Section 2.14
of that document is about the estate tax exclusion amount.

## C5. Statutory authority for indexing the AMT exemption

File A cites § 55(d)(4)(B). File D cites § 55(d)(3).

**File A is correct.** Section 55(d)(3) is the rule that increases AMTI for a married person filing
separately. Section 55(d)(4)(B) carries the inflation adjustment, and `rp-25-32.txt` § 2.07 quotes
it by that number.

## C6. Statutory authority for indexing the AMT 28% breakpoint

File A cites § 55(d)(4)(B). File D cites § 55(b)(1).

**File A is closer.** Section 55(b)(1) states the amount. Section 55(d)(4)(B) performs the
adjustment.

## C7. Rounding of the tips phase-out

File C says the tips deduction is "reduced by $100 for each $1,000 (or fraction) of MAGI above the
start." File C2 says the excess rounds **down** to a whole $1,000.

**File C2 is correct.** Two sources agree. Section 224(b)(2)(A) says "$100 for each $1,000" with no
"or fraction." Line 11 of Schedule 1-A says to decrease the result to the next lower whole number.
The words "(or portion thereof)" appear only in the car loan provision, § 163(h)(4)(C)(ii)(I),
which rounds up. File C is also internally inconsistent, because its overtime block omits the same
words.

## C8. Whether a capital loss carryforward survives the taxpayer

File A states that an unused carryforward ends at death and does not pass to the estate or to
heirs, at medium confidence. File D states that there is "no expiration date on the carryforward
for an individual" and says nothing about death.

**File A is right and file D is incomplete.** Both statements can be read together, but a site that
uses file D alone will carry the loss past death.

## C9. Confidence ratings on the same fact

Three files rate the same senior deduction endpoint differently. File A says medium. File C says
high. File C2 says resolved. File E asserts a different number at high confidence. Any site that
uses a confidence field to decide what to publish will get an unstable answer.

---

# 3. ERRORS

I spot-checked more than 50 dollar figures against the primary documents. The table below lists
what I checked and the result.

| Group | Figures checked | Source | Result |
|---|---|---|---|
| Ordinary brackets, all 4 statuses | 28 band edges and 28 cumulative amounts | `rp-25-32.txt` § 4.01 | All match |
| Standard deduction, aged/blind, dependent | $32,200 / $24,150 / $16,100; $1,650 / $2,050; $1,350 + $450 | § 4.14 | All match |
| Capital gains breakpoints | 10 figures | § 4.03 | All match |
| AMT exemption, phase-out, breakpoint | 14 figures | § 4.10 | All match |
| Kiddie tax | $1,350 / $2,700 / $13,500 / $9,750 | §§ 4.02, 4.11 | All match |
| QBI thresholds | $403,500 / $553,500 / $201,775 / $276,775 / $201,750 / $276,750 | § 4.26 | All match |
| Student loan interest | $85,000 / $100,000 / $175,000 / $205,000 | § 4.29 | All match |
| Child and adoption credits | $2,200 / $1,700 / $17,670 / $265,080 / $305,080 / $5,120 | §§ 4.04, 4.05 | All match |
| Cafeteria plan | $3,400 / $680 | § 4.15 | All match |
| Gift, estate, GST, FEIE | $19,000 / $194,000 / $15,000,000 / $132,900 | §§ 4.42, 2.14, 4.39 | All match |
| 401(k), IRA, plan limits | $24,500 / $8,000 / $11,250 / $72,000 / $360,000 / $160,000 / $235,000 / $7,500 / $1,100 | `n-25-67.txt` | All match |
| Roth and traditional IRA phase-outs | $153,000 / $168,000 / $242,000 / $252,000 / $81,000 / $91,000 / $129,000 / $149,000 | `n-25-67.txt` | All match |
| Saver's Credit boundaries | 9 figures | `n-25-67.txt` | All match |
| SIMPLE, SEP, QCD, domestic abuse | $17,000 / $18,100 / $4,000 / $3,850 / $5,250 / $800 / $111,000 / $55,000 / $10,500 | `n-25-67.txt` | All match |
| HSA and HDHP | $4,400 / $8,750 / $1,700 / $3,400 / $8,500 / $17,000 | `rp-25-19.txt` | All match |
| ACA applicable percentages | 12 figures plus 9.96% | `rp-25-25.txt` | All match |
| SALT | $40,400 / $20,200 / $505,000 / $252,500 / 30% / $10,000 / 2030 | `obbba.htm` § 70120 | All match |
| OBBBA new deductions | $25,000 / $12,500 / $10,000 / $6,000 and all MAGI starts | `obbba.htm` §§ 70103, 70201–70203 | All match |
| CDCC percentages | 50 / 35 / 20, $2,000, $15,000 / $75,000 / $150,000 | `obbba.htm` § 70405 | All match |
| QSBS | $15,000,000 / $10,000,000 / $5,000,000 / $75,000,000 / 50-75-100% | `sec1202.txt` | All match |
| NIIT, Additional Medicare, capital loss, safe harbor | $250,000 / $200,000 / $125,000 / $3,000 / $1,500 / $150,000 / $75,000 / $1,000 | Statute, unchanged since enactment | All match |
| Social Security and Medicare arithmetic | $184,500 × 6.2% = $11,439.00; all six IRMAA tiers | Internal arithmetic | All consistent |

**One wrong dollar figure. Eleven other defects.**

## E1. File E — $350,000 senior deduction endpoint

**Claimed:** "$350,000 for a $12,000 base." Also: "MFJ with two qualifiers phases out over a
$200,000 band from $150,000."

**Correct:** $250,000, for one qualifying spouse or two. The band is $100,000 wide, from $150,000
to $250,000.

**Settled by:** `s1a.txt` lines 35, 36a, and 36b, and § 151(d)(5)(C)(iii)(I) in `obbba.htm`.

This is the only wrong dollar figure I found. See conflict C1.

## E2. File C — the § 68 limitation formula omits the add-back

**Claimed:** "reduction = (2/37) × lesser of (a) total itemized deductions or (b) taxable income
over the 37% threshold."

**Correct:** OBBBA § 70111 rewrites § 68(a). The second term is taxable income "determined without
regard to this section **and increased by such amount of itemized deductions**," to the extent it
exceeds the 37% bracket start.

**Effect:** File C measures against taxable income after the deductions. The statute measures
against taxable income with the deductions added back. The statute therefore reaches taxpayers whom
file C's version misses, and it produces a larger reduction for the rest. A taxpayer with $700,000
of taxable income and $150,000 of itemized deductions gets a reduction of zero under file C, and a
reduction of $2/37 × $81,300 = $4,394.59 under the statute.

**Settled by:** `obbba.htm` § 70111(a).

## E3. File C — wrong rounding direction on the tips phase-out

**Claimed:** "reduced by $100 for each $1,000 (or fraction) of MAGI above the start."

**Correct:** $100 for each full $1,000. The excess rounds down.

**Effect:** Up to $100 of deduction per taxpayer, in the wrong direction. It also inverts the shape
of the curve, which matters for a slider.

**Settled by:** § 224(b)(2)(A) in `obbba.htm`, and line 11 of `s1a.txt`. See conflict C7.

## E4. Files C and C2 — phase-out endpoints stated as fixed

**Claimed:** Tips are "fully phased out at $400,000 / $550,000." Overtime at "$275,000 / $550,000."
Car loan interest at "$150,000 / $250,000." Senior at "$175,000 / $250,000."

**Correct:** Those figures hold only when the taxpayer claims the maximum deduction. The worksheet
subtracts the reduction from the **capped actual amount**, not from the cap.

`s1a.txt` line 7 is the smaller of actual tips or $25,000. Line 13 is line 7 minus line 12. A
taxpayer with $8,000 of qualified tips reaches zero at $80 × 100, that is at $80,000 of excess
MAGI. That is MAGI of $230,000, not $400,000.

**Effect:** For any user below the cap, the site draws the phase-out ending far too late. The
senior deduction is the one exception, because the $6,000 is a flat amount and not a cap on an
actual expense. Its endpoint of $175,000 or $250,000 is genuinely fixed.

**Settled by:** `s1a.txt` lines 7, 13, 15, 21, 24, 30.

## E5. File D — Form 1040-ES for 2026 stated as unavailable

See conflict C2. The statement is wrong as of August 2026.

## E6. File B — Rev. Proc. 2025-32 cited as "section 3.15"

Correct section is 4.15. See conflict C3.

## E7. File E — Rev. Proc. 2025-32 cited as "§2.14(3)"

Correct section is 4.14(3). See conflict C4.

## E8. File D — AMT exemption indexing cited to § 55(d)(3)

Correct citation is § 55(d)(4)(B). See conflict C5.

## E9. File D — AMT 28% breakpoint indexing cited to § 55(b)(1)

The adjustment is in § 55(d)(4)(B). See conflict C6.

## E10. File C — the charitable floor measured against AGI

**Claimed:** "only charitable contributions exceeding 0.5% of AGI are deductible."

**Correct:** The new § 170(b)(1)(I) measures against the taxpayer's **contribution base**, which
§ 170(b)(1)(H) defines as AGI computed without any net operating loss carryback. For most of this
audience the two are equal. The wording is wrong.

**Settled by:** `obbba.htm` § 70425(a)(1).

## E11. File C — SALT sourced to secondary material, and an unnecessary open question

File C sources $40,400, $20,200, $505,000, $252,500, and the 30% rate to a NYC Comptroller report
and a TurboTax page. The enacted statute is in this directory and states every figure. File C also
marks the post-2029 reversion as medium confidence and flags "at least one local-government
analysis described indexing through 2033."

**The values are all correct.** Section 164(b)(7)(A)(iv) states plainly: for a tax year beginning
after calendar year 2029, the applicable limitation amount is $10,000. The open question can be
closed and the confidence raised.

## E12. File C — the open question about a phase-out above $400,000 for the care credit

File C asks whether "any separate ARPA-era high-income ($400,000) further phaseout" survives.

**It does not.** OBBBA § 70405(a) replaces § 21(a)(2) in full. The replacement text has exactly two
reduction stages and no third one. A site that implements a third stage above $400,000 will be
wrong.

**Settled by:** `obbba.htm` § 70405(a).

## Two items I could not verify from this directory

**U1. File B — the Saver's Match phase-out widths.** File B states thresholds of $20,500 single and
$41,000 joint, "with a reduced match phasing out $15,000 above that for single filers and $30,000
above for joint filers." The width figures do not match my reading of § 6433(b)(2), which appears to
use $10,000 and $20,000. No copy of § 6433 or of the cited Notice 2026-48 is in this directory.
This is a 2027 item and is out of scope for a 2026 site, but the figures need a second look before
publication.

**U2. File A — the § 55(d)(3) rule for married filing separately.** File A states that the AMTI
add-back for a separate return is 25% of the excess over the complete phase-out point. OBBBA raised
the general phase-out rate from 25% to 50%. Whether it also moved the § 55(d)(3) figure is not
resolvable from the documents here, because no copy of § 55 is in this directory. The item affects
only married filing separately under the AMT.

---

# 4. INDEXING CHECK — THE FOUR OBBBA DEDUCTIONS

**Answer: none of them index for 2026. Every 2026 figure equals the figure on the 2025
Schedule 1-A.** The C2 caveat can be closed.

## The 2026 figures

| Item | 2025 figure | Indexed for 2026? | **Correct 2026 figure** | Authority |
|---|---|---|---|---|
| Qualified tips cap | $25,000 | No | **$25,000** | § 224(b)(1) |
| Qualified overtime cap | $12,500 / $25,000 MFJ | No | **$12,500 / $25,000 MFJ** | § 225(b)(1) |
| Car loan interest cap | $10,000 | No | **$10,000** | § 163(h)(4)(C)(i) |
| Senior deduction | $6,000 per person | No | **$6,000 per person** | § 151(d)(5)(C)(i) |
| Tips MAGI start | $150,000 / $300,000 | No | **$150,000 / $300,000** | § 224(b)(2)(A) |
| Overtime MAGI start | $150,000 / $300,000 | No | **$150,000 / $300,000** | § 225(b)(2)(A) |
| Car loan MAGI start | $100,000 / $200,000 | No | **$100,000 / $200,000** | § 163(h)(4)(C)(ii)(I) |
| Senior MAGI start | $75,000 / $150,000 | No | **$75,000 / $150,000** | § 151(d)(5)(C)(iii)(I) |

The phase-out rates and rounding also carry over unchanged: $100 per full $1,000 for tips and
overtime, $200 per $1,000 or part of $1,000 for car loan interest, and a flat 6% for the senior
deduction.

## Why none of them index — three independent reasons

**Reason 1. No inflation clause exists in any of the four provisions.** I read all four in
`obbba.htm`. Sections 224 and 225 each run from subsection (a) to a termination subsection, and
neither contains a cost-of-living paragraph. Section 163(h)(4) runs from subparagraph (A) to
subparagraph (E), and contains none. Section 151(d)(5)(C) runs from clause (i) to clause (v), and
contains none.

The contrast inside the same public law is sharp. OBBBA writes an explicit indexing clause every
time it wants one:

| Provision in the same act | Indexing clause |
|---|---|
| § 164(b)(7)(A)(iii), SALT | "101 percent of the dollar amount in effect ... for the preceding calendar year" |
| § 1202(b)(5)(A), QSBS $15,000,000 | "In the case of any taxable year beginning after 2026 ... increased by ..." |
| § 1202(b)(4), QSBS $75,000,000 | Same form |
| § 530A(b)(2), Trump accounts $5,000 | Adjusted for a year after 2027 |
| § 199A(i), the $400 and $1,000 amounts | Adjusted for years after 2026 |
| § 127, the $5,250 exclusion | Adjusted for years after 2026 |
| § 2010(c)(3), the $15,000,000 exclusion | Adjusted for years after 2026 |

The four deductions in question have no such clause. Silence in a statute that is this explicit
elsewhere is decisive.

**Reason 2. Rev. Proc. 2025-32 does not list them.** That document is the complete set of 2026
inflation-adjusted items for the Code as in effect on October 9, 2025. Its header lists every Code
section it touches. Sections 151, 163, 224, and 225 do not appear in that list, and no paragraph in
its § 4 covers them. The IRS adjusted the OBBBA items that index, including the standard deduction,
the child tax credit, the adoption credit, § 179, § 199A, and the ABLE limit. It did not adjust
these four, because there is nothing to adjust.

**Reason 3. All four terminate after 2028.** Sections 224(h) and 225(g) bar any deduction for a tax
year beginning after December 31, 2028. Section 163(h)(4)(A) covers tax years beginning after
December 31, 2024 and before January 1, 2029. Section 151(d)(5)(C)(i) covers a tax year beginning
before January 1, 2029. A four-year provision has no need of an inflation adjustment, and Congress
gave it none.

## What still needs to change before these go on the site

The dollar figures carry over. Two other things do not.

1. **The age date moves.** The 2025 Schedule 1-A asks whether the person was born before
   January 2, 1961. For 2026 the date is January 2, 1962. C2 already says this and is correct.
2. **The Form W-2 reference in line 4a moves.** Line 4a of the 2025 form points to a Social
   Security wage figure of $176,100 in Box 5. For 2026 that figure is $184,500. The 2026 form will
   carry the new number. This only affects the tips computation.

One caution on the source. `s1a.txt` and `f1040s1a--dft.pdf` are a **draft** of the **2025** form,
created November 4, 2025. The arithmetic is reliable, and the statute confirms every step of it.
The site must not cite the draft form as a 2026 authority. Cite the statute instead, at
§§ 151(d)(5)(C), 163(h)(4), 224, and 225 of the Internal Revenue Code.
