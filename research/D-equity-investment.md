# US Federal Tax Rules — Equity Compensation and Investment Income

**Tax year:** 2026
**Reader profile:** W-2 employee of a technology company. Holds RSUs, ISOs, NSOs, ESPP shares, and a taxable brokerage account.
**Compiled:** August 11, 2026
**Primary rate and threshold source for 2026:** Revenue Procedure 2025-32, which states 2026 inflation-adjusted amounts for the Code as in effect on October 9, 2025.

**Note on the One Big Beautiful Bill Act (OBBBA).** OBBBA is Public Law 119-21, enacted July 4, 2025. It changed two things inside this scope: the alternative minimum tax (AMT) exemption phase-out (section 70107) and Section 1202 qualified small business stock (section 70431).

---

## 1. Restricted Stock Units (RSUs)

### RSU income recognition at vesting
- id: rsu_income_recognition
- kind: rule
- driven_by: vesting date and the share price on that date
- values: Ordinary compensation income equals the fair market value of the shares on the date the shares become substantially vested, minus any amount paid for the shares. For a typical RSU the employee pays nothing, so the full fair market value is income.
- shape: Not a phase-out. The clock is the vesting event. Property is substantially vested when it is transferable, or when it is no longer subject to a substantial risk of forfeiture, whichever happens first.
- indexed: no
- why_it_matters: The amount of ordinary income depends on the share price on the vesting date, not on the grant price or the sale price.
- source: [IRS Pub. 525, Restricted Property](https://www.irs.gov/publications/p525) and [26 U.S.C. § 83(a)](https://www.law.cornell.edu/uscode/text/26/83)
- confidence: high

### RSU reporting on Form W-2
- id: rsu_w2_reporting
- kind: rule
- driven_by: the vesting event
- values: The employer reports the vested value as wages in Box 1 of Form W-2. The amount is also subject to Social Security tax, Medicare tax, and federal income tax withholding.
- shape: Not applicable.
- indexed: no
- why_it_matters: RSU income arrives inside the same W-2 wage figure as salary, so it is not separately visible on the tax return.
- source: [IRS Pub. 525, Employee Compensation](https://www.irs.gov/publications/p525)
- confidence: high

### RSU basis and holding period after vesting
- id: rsu_basis_and_holding_period
- kind: holding_period
- driven_by: vesting date and sale date
- values: The cost basis of the shares equals the fair market value that was included in wages. The capital gain holding period starts on the day after the shares become substantially vested.
- shape: The clock starts the day after vesting. It runs to the sale date, and the sale date is counted.
- indexed: no
- why_it_matters: Gain or loss after vesting is capital gain or loss measured against the vest-date value, and it is separate from the wage income.
- source: [IRS Pub. 525, Restricted Property](https://www.irs.gov/publications/p525) and [IRS Topic no. 409](https://www.irs.gov/taxtopics/tc409)
- confidence: high

### Supplemental wage flat withholding rate
- id: supplemental_wage_flat_rate
- kind: rate
- driven_by: cumulative supplemental wages paid by the employer in the calendar year
- values: 22 percent flat, for supplemental wages up to and including $1,000,000 in the calendar year. This rate applies when the employer identifies the supplemental payment separately from regular wages and withheld income tax from regular wages in the current or immediately preceding calendar year. No other percentage is allowed under this method.
- shape: Flat rate on the first $1,000,000 of supplemental wages. Not a phase-out.
- indexed: no
- why_it_matters: RSU vesting is a supplemental wage payment, so most employers withhold federal income tax on it at 22 percent.
- source: [IRS Pub. 15 (Circular E) for 2026, section 7](https://www.irs.gov/publications/p15)
- confidence: high

### Supplemental wage mandatory higher rate
- id: supplemental_wage_mandatory_rate
- kind: rate
- driven_by: cumulative supplemental wages paid by the employer in the calendar year
- values: 37 percent on the part of supplemental wages that exceeds $1,000,000 in the calendar year. This rate is mandatory and applies without regard to the Form W-4 of the employee.
- shape: Applies only to the excess over $1,000,000. The first $1,000,000 remains at 22 percent.
- indexed: no
- why_it_matters: The 37 percent rate equals the top 2026 ordinary income rate, so withholding above the threshold matches the top marginal rate.
- source: [IRS Pub. 15 (Circular E) for 2026, section 7](https://www.irs.gov/publications/p15)
- confidence: high

### Supplemental wage $1,000,000 threshold
- id: supplemental_wage_million_threshold
- kind: threshold
- driven_by: cumulative supplemental wages from one employer in the calendar year
- values: $1,000,000. The same figure applies to every filing status. Payments from all businesses under common control are combined for this test.
- shape: A single hard step. Below or at the threshold the rate is 22 percent. Above it the excess is withheld at 37 percent.
- indexed: no
- why_it_matters: The threshold is per employee per employer per calendar year, and it counts all supplemental wages, not RSU income alone.
- source: [IRS Pub. 15 (Circular E) for 2026, section 7](https://www.irs.gov/publications/p15)
- confidence: high

### Cause of RSU under-withholding
- id: rsu_underwithholding_gap
- kind: rule
- driven_by: total taxable income and filing status
- values: The 22 percent flat rate is fixed. For 2026 a single filer reaches the 24 percent bracket at $105,700 of taxable income, the 32 percent bracket at $201,775, the 35 percent bracket at $256,225, and the 37 percent bracket at $640,600. A married couple filing jointly reaches 24 percent at $211,400, 32 percent at $403,550, 35 percent at $512,450, and 37 percent at $768,700.
- shape: The shortfall equals the marginal rate of the taxpayer minus 22 percent, applied to the RSU income, for taxpayers whose marginal rate is above 22 percent.
- indexed: yes — the ordinary income brackets are indexed. The 22 percent flat rate is not indexed.
- why_it_matters: When the marginal rate of the taxpayer is above 22 percent, withholding at 22 percent covers less than the tax due on the RSU income.
- source: [IRS Pub. 15 for 2026](https://www.irs.gov/publications/p15) for the rate, and [Rev. Proc. 2025-32, § 4.01](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) for the 2026 brackets
- confidence: high

---

## 2. Nonstatutory Stock Options (NSOs)

### NSO taxation at exercise
- id: nso_tax_at_exercise
- kind: rule
- driven_by: share price on the exercise date and the exercise price
- values: For an NSO without a readily determinable fair market value at grant, there is no tax at grant. At exercise the employee includes in income the fair market value of the stock received minus the amount paid. The amount is ordinary compensation income and is reported as wages.
- shape: Not a phase-out. The trigger is the exercise event.
- indexed: no
- why_it_matters: The spread at exercise is ordinary income even when the employee holds the shares and sells nothing.
- source: [IRS Topic no. 427](https://www.irs.gov/taxtopics/tc427) and [IRS Pub. 525, Nonstatutory Stock Options](https://www.irs.gov/publications/p525)
- confidence: high

### NSO taxation at sale
- id: nso_tax_at_sale
- kind: rule
- driven_by: sale price, exercise-date value, and holding period after exercise
- values: The basis of the shares equals the exercise price plus the spread already taxed as wages. The difference between the sale price and this basis is capital gain or capital loss. The holding period starts the day after exercise.
- shape: The capital gain clock starts the day after the exercise date.
- indexed: no
- why_it_matters: Form 1099-B for options granted on or after January 1, 2014 does not include the wage amount in the reported basis, so the basis reported by the broker is lower than the true basis.
- source: [IRS Pub. 525, Nonstatutory Stock Options](https://www.irs.gov/publications/p525)
- confidence: high

---

## 3. Incentive Stock Options (ISOs)

### ISO regular tax at exercise
- id: iso_no_regular_tax_at_exercise
- kind: rule
- driven_by: exercise event
- values: No regular income tax applies at grant or at exercise of an ISO. Section 421(a) applies if the holding period test and the employment test are met.
- shape: Not applicable.
- indexed: no
- why_it_matters: The absence of regular tax at exercise is separate from the AMT treatment of the same exercise.
- source: [26 U.S.C. § 422(a)](https://www.law.cornell.edu/uscode/text/26/422) and [IRS Topic no. 427](https://www.irs.gov/taxtopics/tc427)
- confidence: high

### ISO AMT adjustment at exercise
- id: iso_amt_adjustment
- kind: rule
- driven_by: share price on the exercise date, the exercise price, and the number of shares
- values: For AMT the taxpayer includes the excess of the fair market value of the stock over the amount paid for the stock. The measurement date is the date the rights in the stock become transferable or stop being subject to a substantial risk of forfeiture. The amount goes on Form 6251, line 2i, as a positive number. No adjustment is required if the taxpayer disposes of the stock in the same year as the exercise. The AMT basis of the stock increases by the adjustment.
- shape: Not a phase-out. The clock is the exercise date, or the later vesting date if the stock is unvested at exercise.
- indexed: no
- why_it_matters: The AMT adjustment is a positive item that increases alternative minimum taxable income in the exercise year even when no shares are sold and no cash is received.
- source: [Instructions for Form 6251, Line 2i](https://www.irs.gov/instructions/i6251) and [IRS Pub. 525, Alternative Minimum Tax](https://www.irs.gov/publications/p525)
- confidence: high — the published Form 6251 instructions are the 2025 revision. The line 2i mechanic is statutory and does not change for 2026. The 2026 dollar amounts come from Rev. Proc. 2025-32.

### ISO qualifying disposition holding periods
- id: iso_qualifying_disposition_periods
- kind: holding_period
- driven_by: grant date, exercise date, and sale date
- values: The taxpayer must make no disposition of the share within 2 years from the date the option was granted, and within 1 year after the share was transferred to the taxpayer. Both tests must be met. A separate test requires the taxpayer to be an employee of the granting corporation, or of a parent or subsidiary, from the grant date until the day 3 months before the exercise date. The 3-month period becomes 1 year if the employee is disabled.
- shape: Two clocks that run at the same time. Clock one starts on the grant date and runs 2 years. Clock two starts on the share transfer date at exercise and runs 1 year. The later of the two dates controls.
- indexed: no
- why_it_matters: If both periods are met, the full gain from the sale is long-term capital gain measured against the exercise price.
- source: [26 U.S.C. § 422(a)(1) and § 422(c)(6)](https://www.law.cornell.edu/uscode/text/26/422)
- confidence: high

### ISO disqualifying disposition
- id: iso_disqualifying_disposition
- kind: rule
- driven_by: sale date relative to the grant date and the exercise date
- values: A sale before either holding period is met is a disqualifying disposition. The spread at exercise becomes ordinary compensation income in the year of the sale, and the employer reports it as wages. If the disposition is a sale or exchange on which a loss would be recognized, the ordinary income is capped at the amount realized minus the adjusted basis of the share.
- shape: Not a phase-out. The trigger is a sale before the later of the two ISO holding period dates.
- indexed: no
- why_it_matters: A disqualifying disposition in the same calendar year as the exercise removes the AMT adjustment for that exercise.
- source: [26 U.S.C. § 422(c)(2)](https://www.law.cornell.edu/uscode/text/26/422) and [IRS Pub. 525, ISOs](https://www.irs.gov/publications/p525)
- confidence: high

### ISO $100,000 annual vesting limit
- id: iso_100k_vesting_limit
- kind: limit
- driven_by: the number of shares first exercisable in a calendar year and the share price on the grant date
- values: $100,000 per calendar year. The test uses the aggregate fair market value of the stock for which ISOs are exercisable for the first time during the calendar year. Fair market value is measured as of the grant date, not the vesting date. The limit counts all plans of the employer and its parent and subsidiary corporations. Options are counted in the order in which they were granted. Any excess is treated as a nonstatutory stock option.
- shape: A hard annual cap. The clock is the calendar year in which the option first becomes exercisable.
- indexed: no
- why_it_matters: A grant that vests more than $100,000 of grant-date value in one calendar year is split, and the excess portion follows NSO rules.
- source: [26 U.S.C. § 422(d)](https://www.law.cornell.edu/uscode/text/26/422)
- confidence: high

### ISO information return, Form 3921
- id: iso_form_3921
- kind: rule
- driven_by: an ISO exercise during the calendar year
- values: The corporation furnishes Form 3921 after an ISO exercise. Box 3 shows the exercise price per share, box 4 shows the fair market value per share on the exercise date, and box 5 shows the number of shares transferred.
- shape: Not applicable.
- indexed: no
- why_it_matters: Boxes 3, 4, and 5 of Form 3921 supply the figures needed to compute the Form 6251 line 2i adjustment.
- source: [IRS Topic no. 427](https://www.irs.gov/taxtopics/tc427) and [Instructions for Form 6251, Line 2i](https://www.irs.gov/instructions/i6251)
- confidence: high

---

## 4. Alternative Minimum Tax for 2026

### AMT exemption amount for 2026
- id: amt_exemption_2026
- kind: threshold
- driven_by: filing status
- values: Married filing jointly and surviving spouses $140,200. Unmarried individuals other than surviving spouses $90,100. Married filing separately $70,100. Estates and trusts $31,400.
- shape: A fixed subtraction from alternative minimum taxable income, before the phase-out is applied.
- indexed: yes — adjusted annually under § 55(d)(3).
- why_it_matters: The exemption reduces the alternative minimum taxable income that is subject to the 26 percent and 28 percent AMT rates.
- source: [Rev. Proc. 2025-32, § 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

### AMT exemption phase-out threshold for 2026
- id: amt_phaseout_threshold_2026
- kind: threshold
- driven_by: alternative minimum taxable income and filing status
- values: Married filing jointly and surviving spouses: phase-out starts at $1,000,000 and is complete at $1,280,400. Unmarried individuals other than surviving spouses: starts at $500,000 and is complete at $680,200. Married filing separately: starts at $500,000 and is complete at $640,200. Estates and trusts: starts at $104,800 and is complete at $167,600.
- shape: Start, end, and rate. Start is the figure above. Rate is 50 cents of exemption lost for each dollar of alternative minimum taxable income above the start. End is the start plus twice the exemption amount.
- indexed: no for 2026. Section 55(d)(4)(B) as amended states that the $1,000,000 amount is not adjusted for inflation for any taxable year beginning before January 1, 2027. Indexing restarts for years after 2026, using calendar year 2025 as the base.
- why_it_matters: Alternative minimum taxable income above the start reduces the exemption, and the exemption reaches zero at the end figure.
- source: [Rev. Proc. 2025-32, § 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) and [26 U.S.C. § 55(d)(4)](https://www.law.cornell.edu/uscode/text/26/55)
- confidence: high

### AMT exemption phase-out rate — OBBBA change
- id: amt_phaseout_rate_obbba
- kind: rate
- driven_by: alternative minimum taxable income above the phase-out start
- values: 50 percent for tax years beginning after December 31, 2025. The rate was 25 percent for 2025 and earlier years under TCJA. OBBBA § 70107(c) added § 55(d)(4)(A)(ii)(IV), which substitutes "50 percent" for "25 percent". OBBBA § 70107(d) makes the amendments apply to taxable years beginning after December 31, 2025.
- shape: For each dollar of alternative minimum taxable income above the phase-out start, the exemption falls by 50 cents.
- indexed: no — the rate is a fixed statutory percentage.
- why_it_matters: The doubled rate exhausts the exemption over half the income range that the 25 percent rate required.
- source: [26 U.S.C. § 55(d)(4)(A)(ii)(IV) and Effective Date of 2025 Amendment note](https://www.law.cornell.edu/uscode/text/26/55)
- confidence: high

### What OBBBA changed in the AMT for 2026, stated exactly
- id: amt_obbba_change_summary
- kind: rule
- driven_by: alternative minimum taxable income and filing status
- values: Two changes, both effective for tax years beginning after December 31, 2025. Change one: the phase-out start resets to the un-indexed statutory base. For married filing jointly it falls from $1,252,700 in 2025 to $1,000,000 in 2026. For unmarried individuals it falls from $626,350 in 2025 to $500,000 in 2026. Change two: the phase-out rate rises from 25 percent to 50 percent. The combined effect on the point of full exemption loss: married filing jointly moves from $1,800,700 in 2025 to $1,280,400 in 2026, and unmarried individuals move from $978,750 in 2025 to $680,200 in 2026.
- shape: Start moves down, and rate doubles. Both act in the same direction.
- indexed: The phase-out start is not indexed for 2026. It is indexed again for tax years after 2026, with 2025 as the base year. The exemption amount itself stays indexed.
- why_it_matters: An ISO exercise adds to alternative minimum taxable income, and in 2026 the exemption of the taxpayer starts to phase out at a lower income figure and disappears twice as fast as in 2025.
- source: [26 U.S.C. § 55(d)(4)](https://www.law.cornell.edu/uscode/text/26/55) and [Rev. Proc. 2025-32, § 2.07 and § 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf). 2025 comparison figures from [IR-2024-273](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2025).
- confidence: high — the 2026 phase-out end figures in Rev. Proc. 2025-32 reconcile exactly with a 50 percent rate. For example, $1,000,000 plus $140,200 divided by 0.50 equals $1,280,400.

### AMT tax rates and the 28 percent breakpoint for 2026
- id: amt_rates_2026
- kind: rate
- driven_by: taxable excess, which is alternative minimum taxable income minus the exemption
- values: 26 percent on the first tranche of taxable excess and 28 percent above it. For 2026 the 28 percent rate applies to taxable excess above $244,500 for all taxpayers other than married filing separately, and above $122,250 for married filing separately.
- shape: A two-step rate. The step point is the figure above.
- indexed: yes — adjusted annually under § 55(b)(1).
- why_it_matters: A large ISO exercise can push taxable excess past the step point and expose part of the AMT base to 28 percent instead of 26 percent.
- source: [Rev. Proc. 2025-32, § 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) and [26 U.S.C. § 55(b)(1)](https://www.law.cornell.edu/uscode/text/26/55)
- confidence: high

### AMT credit carryforward
- id: amt_credit_carryforward
- kind: rule
- driven_by: AMT paid in prior years and regular tax liability in the current year
- values: A minimum tax credit is allowed against regular tax. The credit for a year equals the adjusted net minimum tax imposed for all prior tax years beginning after 1986, minus the credit already allowed for those prior years. The credit for a year cannot exceed the regular tax liability reduced by certain other credits, minus the tentative minimum tax for that year. Unused amounts carry forward with no expiration date. The credit is claimed on Form 8801.
- shape: The clock is indefinite. The carryforward has no time limit. The annual use is limited by the gap between regular tax and tentative minimum tax.
- indexed: no
- why_it_matters: AMT paid because of the ISO exercise adjustment is a deferral preference, so it generates a credit that can offset regular tax in later years.
- source: [26 U.S.C. § 53](https://www.law.cornell.edu/uscode/text/26/53) and [Instructions for Form 6251](https://www.irs.gov/instructions/i6251)
- confidence: high

---

## 5. Employee Stock Purchase Plans (Section 423)

### Section 423 plan status
- id: espp_section_423_status
- kind: rule
- driven_by: the terms of the employer plan
- values: A Section 423 plan is a statutory stock option plan. The plan must be approved by the stockholders within 12 months before or after adoption. Options must go to all employees of a participating corporation, with limited exclusions for employees with less than 2 years of service, employees who work 20 hours or less per week, seasonal employees, and highly compensated employees. No employee who owns 5 percent or more of the combined voting power or value of the employer stock can receive an option. All participants must have the same rights and privileges.
- shape: Not applicable.
- indexed: no
- why_it_matters: Section 421(a) applies only if the plan meets every requirement in § 423(b).
- source: [26 U.S.C. § 423(b)](https://www.law.cornell.edu/uscode/text/26/423)
- confidence: high

### ESPP maximum discount
- id: espp_max_discount
- kind: limit
- driven_by: the plan option price formula
- values: The option price cannot be less than the lesser of 85 percent of the fair market value of the stock at grant, or 85 percent of the fair market value of the stock at exercise. The maximum discount is therefore 15 percent.
- shape: A floor on the option price, set at 85 percent of the reference price.
- indexed: no
- why_it_matters: The 15 percent figure is the maximum statutory discount, and a plan can set a smaller discount.
- source: [26 U.S.C. § 423(b)(6)](https://www.law.cornell.edu/uscode/text/26/423)
- confidence: high

### ESPP lookback
- id: espp_lookback
- kind: rule
- driven_by: the plan option price formula and the share prices at grant and at exercise
- values: Section 423(b)(6) permits the option price to be the lesser of a percentage of the grant-date value or the same percentage of the exercise-date value. This two-point formula is the lookback. A plan that uses the lookback with the maximum discount sets the price at 85 percent of the lower of the two prices. A plan that uses a lookback and prices off the exercise-date value can run for up to 5 years from the grant date. A plan whose price is not determinable in that manner can run for only 27 months from the grant date.
- shape: Two measurement points. Point one is the grant date, which is usually the start of the offering period. Point two is the exercise date, which is the purchase date.
- indexed: no
- why_it_matters: With a lookback, a share price rise during the offering period increases the discount measured at the purchase date.
- source: [26 U.S.C. § 423(b)(6) and § 423(b)(7)](https://www.law.cornell.edu/uscode/text/26/423)
- confidence: high

### ESPP $25,000 annual limit
- id: espp_25k_annual_limit
- kind: limit
- driven_by: the share price on the grant date and the calendar years in which the option is outstanding
- values: $25,000 of fair market value of stock per calendar year, measured at the time the option is granted. The limit applies across all Section 423 plans of the employer and its parent and subsidiary corporations. The right to purchase accrues when the option first becomes exercisable during the calendar year. An accrued but unused right under one option cannot be carried over to another option.
- shape: A hard annual cap keyed to the calendar year in which the option is outstanding. Value is measured at grant, not at purchase.
- indexed: no — the figure is fixed in the statute and is not inflation-adjusted.
- why_it_matters: Because the $25,000 is measured with grant-date value, the number of shares that the limit permits is fixed at grant even when the purchase price is lower.
- source: [26 U.S.C. § 423(b)(8)](https://www.law.cornell.edu/uscode/text/26/423)
- confidence: high

### ESPP qualifying disposition holding period
- id: espp_qualifying_disposition_period
- kind: holding_period
- driven_by: grant date, share transfer date, and sale date
- values: The taxpayer must make no disposition within 2 years after the grant date, and within 1 year after the share was transferred to the taxpayer. Both tests must be met. The employment test in § 423(a)(2) also applies.
- shape: Two clocks that run at the same time. Clock one starts on the grant date, which is usually the first day of the offering period, and runs 2 years. Clock two starts on the purchase date and runs 1 year. The later date controls.
- indexed: no
- why_it_matters: Because the 2-year clock starts at grant and not at purchase, it can be satisfied before or after the 1-year clock depending on the length of the offering period.
- source: [26 U.S.C. § 423(a)(1)](https://www.law.cornell.edu/uscode/text/26/423)
- confidence: high

### ESPP qualifying disposition tax treatment
- id: espp_qualifying_disposition_treatment
- kind: rule
- driven_by: grant-date price, option price, sale price, and holding period
- values: If the option price was less than 100 percent but not less than 85 percent of the grant-date fair market value, the taxpayer includes as compensation the lesser of two amounts. Amount one is the excess of the grant-date fair market value over the option price. Amount two is the excess of the fair market value at disposition over the amount paid for the share. Any remaining gain is capital gain. A loss on the sale is a capital loss and produces no ordinary income.
- shape: Not a phase-out. The ordinary income part is capped by the smaller of the two amounts above.
- indexed: no
- why_it_matters: In a qualifying disposition the ordinary income part is measured with the grant-date discount, so it does not grow when the share price rises after grant.
- source: [26 U.S.C. § 423(c)](https://www.law.cornell.edu/uscode/text/26/423) and [IRS Pub. 525, Option granted at a discount](https://www.irs.gov/publications/p525)
- confidence: high

### ESPP disqualifying disposition tax treatment
- id: espp_disqualifying_disposition_treatment
- kind: rule
- driven_by: exercise-date price, option price, and sale price
- values: If the holding period test is not met, the ordinary income equals the amount by which the fair market value of the stock at exercise exceeded the option price. This ordinary income is not limited by the gain on the sale. The basis of the stock increases by this ordinary income. The difference between the increased basis and the sale price is capital gain or capital loss.
- shape: Not a phase-out. The measurement point moves from the grant date to the exercise date.
- indexed: no
- why_it_matters: In a disqualifying disposition the ordinary income is measured at exercise and can exceed the total gain on the sale.
- source: [IRS Pub. 525, Holding period requirement not satisfied](https://www.irs.gov/publications/p525)
- confidence: high

### ESPP information return, Form 3922
- id: espp_form_3922
- kind: rule
- driven_by: first transfer or sale of ESPP shares acquired at a discount
- values: The corporation furnishes Form 3922 after the first transfer of legal title of a share acquired under a Section 423 plan where the option price was below the grant-date value. The form reports the grant date, the exercise date, the grant-date value, the exercise-date value, and the exercise price.
- shape: Not applicable.
- indexed: no
- why_it_matters: Form 3922 supplies the grant-date and exercise-date values needed to compute the ordinary income part of an ESPP sale.
- source: [IRS Topic no. 427](https://www.irs.gov/taxtopics/tc427) and [IRS Pub. 525](https://www.irs.gov/publications/p525)
- confidence: high

### ESPP withholding on the § 423(c) amount
- id: espp_no_withholding_on_423c
- kind: rule
- driven_by: a qualifying disposition of discounted ESPP shares
- values: No amount is required to be deducted and withheld under chapter 24 with respect to any amount treated as compensation under § 423(c).
- shape: Not applicable.
- indexed: no
- why_it_matters: The compensation income from a qualifying ESPP disposition is reported as wages but carries no income tax withholding.
- source: [26 U.S.C. § 423(c), final sentence](https://www.law.cornell.edu/uscode/text/26/423)
- confidence: high

---

## 6. Section 83(b) Election

### Section 83(b) election effect
- id: section_83b_effect
- kind: rule
- driven_by: transfer date of the restricted property and its value on that date
- values: The person who performs the services elects to include in gross income for the year of transfer the fair market value of the property at transfer, minus any amount paid. Value is determined without regard to any restriction other than a restriction that by its terms will never lapse. If the election is made, § 83(a) does not apply to the transfer, and later appreciation is not compensation when the property vests. If the property is later forfeited, no deduction is allowed for the forfeiture. The election cannot be revoked without the consent of the Secretary.
- shape: Moves the income measurement date from the vesting date back to the transfer date.
- indexed: no
- why_it_matters: The election fixes the compensation amount at the transfer-date value and starts the capital gain holding period at transfer.
- source: [26 U.S.C. § 83(b)](https://www.law.cornell.edu/uscode/text/26/83) and [IRS Pub. 525, Choosing to include in income for year of transfer](https://www.irs.gov/publications/p525)
- confidence: high

### Section 83(b) 30-day deadline
- id: section_83b_deadline
- kind: rule
- driven_by: the date the property is transferred
- values: The election must be made no later than 30 days after the date of the transfer. Form 15620 is the IRS form for a § 83(b) election. Form 15620 cannot be used for a § 83(i) election.
- shape: A fixed 30-day clock that starts on the transfer date. There is no extension provision in the statute.
- indexed: no
- why_it_matters: The 30-day period runs from the transfer of the property, not from the grant date or the vesting date.
- source: [26 U.S.C. § 83(b)(2)](https://www.law.cornell.edu/uscode/text/26/83) and [IRS Pub. 525](https://www.irs.gov/publications/p525)
- confidence: high

### Who a Section 83(b) election applies to
- id: section_83b_applicability
- kind: rule
- driven_by: the type of equity award held
- values: The election applies to a transfer of property in connection with the performance of services where the property is subject to a substantial risk of forfeiture. This covers restricted stock awards and early-exercised stock options, because in both cases shares are transferred. It does not apply to a restricted stock unit, because an RSU is an unfunded promise and no property is transferred at grant. The election also does not apply to a nonstatutory option without a readily determinable value.
- shape: Not applicable.
- indexed: no
- why_it_matters: An RSU holder cannot make a § 83(b) election, because no property transfer occurs at grant.
- source: [26 U.S.C. § 83(a) and § 83(b)](https://www.law.cornell.edu/uscode/text/26/83) and [IRS Pub. 525, Restricted Property and Option with readily determinable value](https://www.irs.gov/publications/p525)
- confidence: high — the statute and Pub. 525 state that § 83 applies to transferred property, and Pub. 525 states that the year-of-transfer choice does not apply to a nonstatutory option. Pub. 525 does not state the RSU conclusion in one sentence. The conclusion follows from the absence of a property transfer at RSU grant.

### Section 83(i) deferral election
- id: section_83i_election
- kind: rule
- driven_by: private company status, plan coverage, and employee status
- values: A qualified employee of a private corporation can elect to defer income tax for up to 5 years from the vesting date on qualified stock from broad-based option or RSU programs. The corporation must have a written plan that offers an RSU or option to at least 80 percent of its US employees. The election must be made no later than 30 days after the first date the rights of the employee become transferable or stop being subject to a substantial risk of forfeiture, whichever occurs first. A 1 percent owner, current or at any point in the prior 10 calendar years, is not a qualified employee. Withholding is at the highest marginal rate.
- shape: A fixed 30-day clock that starts on the vesting date, and a deferral of up to 5 years.
- indexed: no
- why_it_matters: The deferral ends early on the first date the stock becomes transferable, on the first date any employer stock becomes readily tradable on an established securities market, on the date the employee becomes an excluded employee, or on revocation.
- source: [26 U.S.C. § 83(i)](https://www.law.cornell.edu/uscode/text/26/83) and [IRS Pub. 525, Qualified Equity Grants](https://www.irs.gov/publications/p525)
- confidence: high

---

## 7. Capital Gains

### Long-term versus short-term holding period
- id: capital_gain_holding_period
- kind: holding_period
- driven_by: acquisition date and disposition date
- values: More than 1 year produces long-term treatment. One year or less produces short-term treatment. Count from the day after the day the asset was acquired, up to and including the day of disposition.
- shape: The clock starts the day after acquisition. The disposal day is counted. The boundary is "more than one year", so exactly one year is short-term.
- indexed: no
- why_it_matters: Short-term capital gain is taxed as ordinary income at graduated rates, and long-term capital gain uses the separate 0, 15, and 20 percent rate schedule.
- source: [IRS Topic no. 409](https://www.irs.gov/taxtopics/tc409)
- confidence: high

### Long-term capital gain 0 percent bracket for 2026
- id: ltcg_0_percent_2026
- kind: threshold
- driven_by: taxable income and filing status
- values: The 0 percent rate applies to adjusted net capital gain up to these maximum zero rate amounts of taxable income. Married filing jointly and surviving spouse $98,900. Married filing separately $49,450. Head of household $66,200. All other individuals, which includes single filers, $49,450. Estates and trusts $3,300.
- shape: The figure is the top of the 0 percent band, measured with total taxable income including the capital gain.
- indexed: yes — adjusted annually under § 1(j)(5)(B).
- why_it_matters: The band is measured against total taxable income, so ordinary income fills the band before capital gain does.
- source: [Rev. Proc. 2025-32, § 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

### Long-term capital gain 15 percent bracket for 2026
- id: ltcg_15_percent_2026
- kind: threshold
- driven_by: taxable income and filing status
- values: The 15 percent rate applies above the zero rate amount and up to these maximum 15 percent rate amounts of taxable income. Married filing jointly and surviving spouse $613,700. Married filing separately $306,850. Head of household $579,600. All other individuals $545,500. Estates and trusts $16,250.
- shape: A band that runs from the top of the 0 percent amount to the figure above.
- indexed: yes — adjusted annually under § 1(j)(5)(B).
- why_it_matters: The figure is the top of the 15 percent band, and gain above it is taxed at 20 percent.
- source: [Rev. Proc. 2025-32, § 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

### Long-term capital gain 20 percent rate for 2026
- id: ltcg_20_percent_2026
- kind: rate
- driven_by: taxable income and filing status
- values: 20 percent applies to adjusted net capital gain to the extent taxable income exceeds the maximum 15 percent rate amount for the filing status.
- shape: The top band. It starts at the figure in `ltcg_15_percent_2026` and has no upper limit.
- indexed: yes — the starting point is indexed.
- why_it_matters: The 20 percent rate is separate from the 3.8 percent net investment income tax, and both can apply to the same gain.
- source: [Rev. Proc. 2025-32, § 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) and [IRS Topic no. 409](https://www.irs.gov/taxtopics/tc409)
- confidence: high

### Short-term capital gain rate
- id: stcg_rate_2026
- kind: rate
- driven_by: taxable income and filing status
- values: Net short-term capital gain is taxed as ordinary income at the graduated 2026 rates of 10, 12, 22, 24, 32, 35, and 37 percent.
- shape: Uses the ordinary income brackets in Rev. Proc. 2025-32 § 4.01.
- indexed: yes — the ordinary brackets are indexed.
- why_it_matters: A sale one year or less after acquisition uses the ordinary rate schedule instead of the capital gain schedule.
- source: [IRS Topic no. 409](https://www.irs.gov/taxtopics/tc409) and [Rev. Proc. 2025-32, § 4.01](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

### Special maximum rates above 20 percent
- id: capital_gain_special_max_rates
- kind: rate
- driven_by: the type of asset sold
- values: The taxable part of gain from Section 1202 qualified small business stock has a maximum rate of 28 percent. Net capital gain from collectibles has a maximum rate of 28 percent. Unrecaptured Section 1250 gain has a maximum rate of 25 percent.
- shape: Rate ceilings that replace the 20 percent top rate for these asset classes.
- indexed: no
- why_it_matters: The part of Section 1202 gain that the exclusion does not cover is taxed at up to 28 percent, not 20 percent.
- source: [IRS Topic no. 409](https://www.irs.gov/taxtopics/tc409)
- confidence: high

---

## 8. Net Investment Income Tax

### Net investment income tax rate
- id: niit_rate
- kind: rate
- driven_by: net investment income and modified adjusted gross income
- values: 3.8 percent. The tax applies to the lesser of net investment income, or the excess of modified adjusted gross income over the threshold for the filing status.
- shape: A flat rate applied to the lesser of two amounts.
- indexed: no
- why_it_matters: The tax is computed on Form 8960 and is separate from the income tax on the same income.
- source: [IRS Topic no. 559](https://www.irs.gov/taxtopics/tc559)
- confidence: high

### Net investment income tax MAGI thresholds
- id: niit_magi_thresholds
- kind: threshold
- driven_by: modified adjusted gross income and filing status
- values: Married filing jointly or qualifying surviving spouse $250,000. Married filing separately $125,000. Single or head of household $200,000.
- shape: A single step, not a phase-out. Only the excess of modified adjusted gross income over the threshold is compared to net investment income.
- indexed: no — these figures are fixed in § 1411 and are not inflation-adjusted.
- why_it_matters: Because the thresholds are not indexed, the number of taxpayers above them rises with nominal income over time.
- source: [IRS Topic no. 559](https://www.irs.gov/taxtopics/tc559)
- confidence: high

### Definition of net investment income
- id: niit_income_definition
- kind: rule
- driven_by: the type and source of the income
- values: Net investment income includes interest, dividends, certain annuities, royalties, and rents unless derived in a trade or business to which the tax does not apply. It includes income from a trade or business that is a passive activity under § 469, and from trading in financial instruments or commodities under § 475(e)(2). It includes net gains from the disposition of property such as stocks, bonds, mutual funds, and real estate, to the extent taken into account in taxable income. It does not include wages, unemployment compensation, or income from an active business. It does not include tax-exempt state or municipal bond interest, or the excluded part of gain on the sale of a principal residence.
- shape: Not applicable.
- indexed: no
- why_it_matters: RSU, NSO, ISO, and ESPP compensation income is wages and is not net investment income, while the capital gain on the same shares after sale is net investment income.
- source: [IRS Topic no. 559](https://www.irs.gov/taxtopics/tc559)
- confidence: high

### Definition of MAGI for the net investment income tax
- id: niit_magi_definition
- kind: rule
- driven_by: adjusted gross income and any foreign earned income exclusion
- values: MAGI is adjusted gross income for regular income tax, increased by the foreign earned income exclusion and adjusted for certain deductions related to that exclusion. For a taxpayer with no excluded foreign earned income, MAGI equals adjusted gross income.
- shape: Not applicable.
- indexed: no
- why_it_matters: Wage income, including equity compensation reported on Form W-2, raises MAGI and can push a taxpayer over the threshold even though wages are not net investment income.
- source: [IRS Topic no. 559](https://www.irs.gov/taxtopics/tc559)
- confidence: high

---

## 9. Dividends

### Qualified dividend holding period, common stock
- id: qualified_dividend_holding_period
- kind: holding_period
- driven_by: purchase date, sale date, and the ex-dividend date
- values: The taxpayer must hold the stock for more than 60 days during the 121-day period that begins 60 days before the ex-dividend date. Count the day of disposal. Do not count the day of acquisition.
- shape: A 121-day window centered on the ex-dividend date. The window starts 60 days before the ex-dividend date and ends 60 days after it. The taxpayer must hold the shares for at least 61 days inside that window.
- indexed: no
- why_it_matters: A dividend reported in box 1b of Form 1099-DIV is not a qualified dividend for the recipient if the recipient fails this holding period test.
- source: [IRS Pub. 550, Qualified Dividends — Holding period](https://www.irs.gov/publications/p550)
- confidence: high

### Qualified dividend holding period, preferred stock
- id: qualified_dividend_holding_period_preferred
- kind: holding_period
- driven_by: purchase date, sale date, ex-dividend date, and the period the dividend covers
- values: If the preferred dividends are due to periods totaling more than 366 days, the taxpayer must hold the stock for more than 90 days during the 181-day period that begins 90 days before the ex-dividend date. If the periods total less than 367 days, the common stock rule applies.
- shape: A 181-day window centered on the ex-dividend date, with a 91-day minimum holding requirement.
- indexed: no
- why_it_matters: The longer test applies only to preferred dividends that cover periods totaling more than 366 days.
- source: [IRS Pub. 550, Exception for preferred stock](https://www.irs.gov/publications/p550)
- confidence: high

### Qualified dividend tax rate
- id: qualified_dividend_rate
- kind: rate
- driven_by: taxable income and filing status
- values: Qualified dividends are taxed at the long-term capital gain rates of 0, 15, or 20 percent, using the same 2026 breakpoints as `ltcg_0_percent_2026` and `ltcg_15_percent_2026`. Ordinary dividends that are not qualified are taxed at the graduated ordinary income rates.
- shape: Uses the capital gain rate schedule, not the ordinary rate schedule.
- indexed: yes — the breakpoints are indexed.
- why_it_matters: The difference between qualified and ordinary treatment is the difference between the capital gain rate schedule and the ordinary rate schedule on the same dollar of dividend.
- source: [IRS Pub. 550, Qualified Dividends](https://www.irs.gov/publications/p550) and [Rev. Proc. 2025-32, § 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

---

## 10. Capital Losses and the Wash Sale Rule

### Annual capital loss offset against ordinary income
- id: capital_loss_annual_offset
- kind: limit
- driven_by: net capital loss for the year and filing status
- values: $3,000 per year. $1,500 for married filing separately. The deductible amount is the lesser of that figure, or the total net loss on line 16 of Schedule D. The loss is claimed on line 7a of Form 1040.
- shape: A hard annual cap on the amount of net capital loss that can reduce ordinary income.
- indexed: no — the figure is fixed in § 1211(b) and is not inflation-adjusted.
- why_it_matters: Capital losses first offset capital gains without limit, and only the remaining net loss is subject to the annual cap.
- source: [IRS Topic no. 409](https://www.irs.gov/taxtopics/tc409)
- confidence: high

### Capital loss carryforward
- id: capital_loss_carryforward
- kind: rule
- driven_by: net capital loss above the annual cap
- values: A net capital loss above the annual limit carries forward to later years. The carryforward keeps its character as short-term or long-term. The amount is figured with the Capital Loss Carryover Worksheet in Pub. 550 or in the Schedule D instructions. There is no expiration date on the carryforward for an individual.
- shape: The clock is indefinite. The carryforward continues until the loss is used.
- indexed: no
- why_it_matters: A separate AMT capital loss carryforward can exist, because the AMT basis of ISO shares differs from the regular tax basis.
- source: [IRS Topic no. 409](https://www.irs.gov/taxtopics/tc409) and [Instructions for Form 6251, Line 2k](https://www.irs.gov/instructions/i6251)
- confidence: high

### Wash sale rule and its 30-day window
- id: wash_sale_rule
- kind: rule
- driven_by: sale date of the loss position and the dates of any acquisition of substantially identical stock or securities
- values: A loss on a sale of stock or securities is not deductible if, within the period that begins 30 days before the sale and ends 30 days after the sale, the taxpayer acquired substantially identical stock or securities, or entered into a contract or option to acquire them. The term "stock or securities" includes contracts or options to acquire or sell stock or securities. An exception applies to a dealer in stock or securities for losses sustained in the ordinary course of that business.
- shape: A 61-day window in total. It starts 30 days before the sale date, includes the sale date, and ends 30 days after the sale date.
- indexed: no
- why_it_matters: The window runs in both directions, so a purchase made before the loss sale can trigger the rule as well as a purchase made after it.
- source: [26 U.S.C. § 1091(a)](https://www.law.cornell.edu/uscode/text/26/1091)
- confidence: high

### Wash sale basis and holding period adjustment
- id: wash_sale_basis_adjustment
- kind: rule
- driven_by: the disallowed loss amount and the price of the replacement shares
- values: The basis of the replacement stock equals the basis of the stock sold, increased or decreased by the difference between the price at which the replacement property was acquired and the price at which the original stock was sold. The disallowed loss is therefore added to the basis of the replacement shares and is not permanently lost.
- shape: Not applicable.
- indexed: no
- why_it_matters: The wash sale rule defers the loss into the basis of the replacement position rather than eliminating it.
- source: [26 U.S.C. § 1091(d)](https://www.law.cornell.edu/uscode/text/26/1091)
- confidence: high

### Wash sale rule for short sales
- id: wash_sale_short_sales
- kind: rule
- driven_by: the closing date of a short sale
- values: Rules similar to § 1091(a) apply to a loss realized on the closing of a short sale if, within the period beginning 30 days before the closing and ending 30 days after it, substantially identical stock or securities were sold, or another short sale of substantially identical stock or securities was entered into.
- shape: The same 61-day window, measured from the closing date of the short sale.
- indexed: no
- why_it_matters: The rule extends to short positions and to securities futures contracts to sell.
- source: [26 U.S.C. § 1091(e)](https://www.law.cornell.edu/uscode/text/26/1091)
- confidence: high

---

## 11. Section 1202 Qualified Small Business Stock

**Key date.** Section 1202(a)(6)(A) defines the "applicable date" as the date of enactment of that paragraph. The Code notes state that this is the enactment date of Public Law 119-21, which is **July 4, 2025**.

### QSBS tiered exclusion for stock acquired after July 4, 2025
- id: qsbs_tiered_exclusion_new
- kind: rate
- driven_by: the acquisition date of the stock and the holding period
- values: For qualified small business stock acquired after July 4, 2025, the applicable percentage of gain excluded from gross income is: 50 percent at 3 years held, 75 percent at 4 years held, and 100 percent at 5 years or more held. Gain is eligible only if the stock is held for at least 3 years.
- shape: A three-step table keyed to the holding period. The clock starts on the acquisition date. There is no exclusion below 3 years.
- indexed: no — the percentages are fixed in the statute.
- why_it_matters: Under the tiered rule a partial exclusion becomes available at 3 years, where the earlier rule required more than 5 years for any exclusion.
- source: [26 U.S.C. § 1202(a)(1)(B) and § 1202(a)(5)](https://www.law.cornell.edu/uscode/text/26/1202)
- confidence: high

### QSBS exclusion for stock acquired on or before July 4, 2025
- id: qsbs_exclusion_old
- kind: rate
- driven_by: the acquisition date of the stock and the holding period
- values: The stock must be held for more than 5 years. For stock acquired after September 27, 2010 and on or before July 4, 2025, the exclusion is 100 percent. For stock acquired after February 17, 2009 and on or before September 27, 2010, the exclusion is 75 percent. For stock acquired before February 18, 2009, the base exclusion is 50 percent. There is no partial exclusion at 3 or 4 years for stock in this group.
- shape: A single cliff at more than 5 years. Below that point the exclusion is zero.
- indexed: no
- why_it_matters: Stock acquired on or before July 4, 2025 keeps the more-than-5-year rule, so the tiered table does not apply to it.
- source: [26 U.S.C. § 1202(a)(1)(A), § 1202(a)(3), and § 1202(a)(4)](https://www.law.cornell.edu/uscode/text/26/1202)
- confidence: high

### QSBS per-issuer dollar cap
- id: qsbs_per_issuer_cap
- kind: limit
- driven_by: the acquisition date of the stock and the amount of eligible gain from that issuer
- values: For stock acquired after July 4, 2025 the applicable dollar limit is $15,000,000, reduced by eligible gain from the same issuer taken into account in prior years and by certain current-year gain from older stock of the same issuer. For stock acquired on or before July 4, 2025 the limit stays at $10,000,000. For a married individual filing separately, the $10,000,000 figure becomes $5,000,000, and the $15,000,000 figure is halved. On a joint return the gain taken into account is allocated equally between the spouses for later years.
- shape: A per-issuer, per-taxpayer cap. The limit for a later year drops to zero once eligible gain from post-July 4, 2025 stock of that issuer exceeds the applicable dollar limit.
- indexed: The $15,000,000 figure is indexed for tax years beginning after 2026, with calendar year 2025 as the base and rounding to the nearest $10,000. The $10,000,000 figure is not indexed.
- why_it_matters: The per-issuer cap is the greater of the applicable dollar limit or 10 times the aggregate adjusted bases of the stock of that issuer disposed of during the year.
- source: [26 U.S.C. § 1202(b)(1), § 1202(b)(3), § 1202(b)(4), and § 1202(b)(5)](https://www.law.cornell.edu/uscode/text/26/1202)
- confidence: high — the statute as codified contains two paragraphs numbered (b)(4), which the Code notes flag as an error in the original. The inflation adjustment for the $15,000,000 figure appears in the paragraph added by OBBBA § 70431(c)(2).

### QSBS 10-times-basis alternative cap
- id: qsbs_10x_basis_cap
- kind: limit
- driven_by: the aggregate adjusted bases of the stock disposed of during the year
- values: The per-issuer limit is the greater of the applicable dollar limit, or 10 times the aggregate adjusted bases of qualified small business stock of that issuer disposed of by the taxpayer during the tax year. The adjusted basis is determined without regard to any addition to basis after the date the stock was originally issued.
- shape: An alternative ceiling. It applies when 10 times basis exceeds the dollar cap.
- indexed: no
- why_it_matters: For a taxpayer with a high basis in the stock, the 10-times-basis figure can exceed the dollar cap and become the controlling limit.
- source: [26 U.S.C. § 1202(b)(1)(B)](https://www.law.cornell.edu/uscode/text/26/1202)
- confidence: high

### QSBS gross asset limit of the issuing corporation
- id: qsbs_gross_asset_limit
- kind: limit
- driven_by: the aggregate gross assets of the issuing corporation at issuance
- values: $75,000,000 for stock issued after July 4, 2025. The limit was $50,000,000 for stock issued on or before that date. The test applies at all times after August 10, 1993 and before the issuance, and also immediately after the issuance taking into account amounts received in the issuance. Aggregate gross assets means cash plus the aggregate adjusted bases of other property held by the corporation. Members of the same parent-subsidiary controlled group are treated as one corporation.
- shape: A ceiling on the size of the issuing corporation, measured at and before the moment of issuance.
- indexed: The $75,000,000 figure is indexed for tax years beginning after 2026, with calendar year 2025 as the base and rounding to the nearest $10,000.
- why_it_matters: The test is applied to the corporation at the time of issuance, so later growth of the corporation does not disqualify stock that already met the test.
- source: [26 U.S.C. § 1202(d)(1) and the second § 1202(b)(4)](https://www.law.cornell.edu/uscode/text/26/1202)
- confidence: high

### QSBS effective dates under OBBBA
- id: qsbs_obbba_effective_dates
- kind: rule
- driven_by: the acquisition or issuance date of the stock, and the tax year
- values: Three different effective-date rules apply. The tiered exclusion, the applicable percentage table, and the applicable date definition in OBBBA § 70431(a) apply to taxable years beginning after July 4, 2025. The per-issuer dollar limit changes in OBBBA § 70431(b) apply to taxable years beginning after July 4, 2025. The $75,000,000 gross asset limit and the inflation adjustments in OBBBA § 70431(c) apply to stock issued after July 4, 2025.
- shape: Not applicable.
- indexed: no
- why_it_matters: The gross asset limit is keyed to the stock issuance date, while the exclusion and cap changes are keyed to the taxable year.
- source: [26 U.S.C. § 1202, Effective Date of 2025 Amendment notes, citing Pub. L. 119-21 §§ 70431(a)(6), (b)(4), and (c)(3)](https://www.law.cornell.edu/uscode/text/26/1202)
- confidence: high

### QSBS and the AMT preference item
- id: qsbs_amt_preference
- kind: rule
- driven_by: the acquisition date of the stock
- values: Section 57(a)(7) now applies only to stock acquired on or before September 27, 2010, the enactment date of the Creating Small Business Jobs Act of 2010. For that older stock the preference is 7 percent of the amount excluded under § 1202. For stock acquired after September 27, 2010 there is no AMT preference from the § 1202 exclusion. OBBBA § 70431(a)(4) made this change, and it takes effect as if it had been included in the 2010 Act.
- shape: Not applicable.
- indexed: no
- why_it_matters: Line 2h of Form 6251 applies only to gain excluded on qualified small business stock acquired before September 28, 2010.
- source: [26 U.S.C. § 57(a)(7) and the Effective Date of 2025 Amendment note](https://www.law.cornell.edu/uscode/text/26/57), and [Instructions for Form 6251, Line 2h](https://www.irs.gov/instructions/i6251)
- confidence: high

### Rate on the non-excluded part of QSBS gain
- id: qsbs_taxable_portion_rate
- kind: rate
- driven_by: the amount of § 1202 gain that the exclusion does not cover
- values: The taxable part of gain from the sale of Section 1202 qualified small business stock is taxed at a maximum rate of 28 percent.
- shape: A rate ceiling that replaces the 20 percent top long-term capital gain rate for this gain.
- indexed: no
- why_it_matters: With a 50 percent exclusion at 3 years, the remaining half of the gain is taxed at up to 28 percent and can also be subject to the 3.8 percent net investment income tax.
- source: [IRS Topic no. 409](https://www.irs.gov/taxtopics/tc409)
- confidence: high

---

## 12. Estimated Tax and Underpayment Penalties

### Estimated tax safe harbor, current year
- id: estimated_tax_safe_harbor_current_year
- kind: threshold
- driven_by: total tax for the current year
- values: 90 percent of the tax shown on the return for the tax year. If no return is filed, 90 percent of the tax for that year.
- shape: One of the two branches of the required annual payment. The required annual payment is the lesser of this branch and the prior-year branch.
- indexed: no
- why_it_matters: The required annual payment is the lesser of the two branches, so a taxpayer can use whichever produces the smaller number.
- source: [26 U.S.C. § 6654(d)(1)(B)(i)](https://www.law.cornell.edu/uscode/text/26/6654)
- confidence: high

### Estimated tax safe harbor, prior year
- id: estimated_tax_safe_harbor_prior_year
- kind: threshold
- driven_by: total tax shown on the prior year return
- values: 100 percent of the tax shown on the return of the individual for the preceding tax year. This branch does not apply if the preceding tax year was not a 12-month year, or if the individual filed no return for that year.
- shape: The second branch of the required annual payment.
- indexed: no
- why_it_matters: The prior-year branch uses a known number, so it does not depend on an estimate of current-year income.
- source: [26 U.S.C. § 6654(d)(1)(B)(ii)](https://www.law.cornell.edu/uscode/text/26/6654)
- confidence: high

### The 110 percent rule for higher AGI
- id: estimated_tax_110_percent_rule
- kind: threshold
- driven_by: adjusted gross income shown on the prior year return, and filing status
- values: If the adjusted gross income shown on the prior year return exceeds $150,000, the prior-year branch uses 110 percent instead of 100 percent. For a married individual who files a separate return for the current year, the trigger figure is $75,000.
- shape: A single step, not a phase-out. At or below the trigger the factor is 100 percent. Above it the factor is 110 percent for the whole prior-year tax.
- indexed: no — the $150,000 and $75,000 figures are fixed in § 6654(d)(1)(C) and are not inflation-adjusted.
- why_it_matters: The test uses prior-year adjusted gross income, so a large equity event in the prior year raises the safe harbor factor for the current year.
- source: [26 U.S.C. § 6654(d)(1)(C)](https://www.law.cornell.edu/uscode/text/26/6654)
- confidence: high

### Quarterly due dates for tax year 2026
- id: estimated_tax_due_dates_2026
- kind: rule
- driven_by: the calendar
- values: Four required installments, each 25 percent of the required annual payment. Statutory due dates are April 15, June 15, September 15, and January 15 of the following tax year. For tax year 2026 these fall on Wednesday April 15, 2026, Monday June 15, 2026, Tuesday September 15, 2026, and Friday January 15, 2027. All four are weekdays, so no weekend shift applies.
- shape: Four fixed dates. If a due date falls on a Saturday, Sunday, or legal holiday, the payment is on time if made on the next day that is not a Saturday, Sunday, or holiday.
- indexed: no
- why_it_matters: A taxpayer who files the return and pays in full on or before January 31 of the following year avoids the penalty on the fourth installment only.
- source: [26 U.S.C. § 6654(c)(2) and § 6654(h)](https://www.law.cornell.edu/uscode/text/26/6654), and [IRS Estimated taxes](https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes)
- confidence: high — statutory dates confirmed. Weekday check performed against the 2026 and 2027 calendars. IRS has not published a Form 1040-ES for 2026 that this research could locate.

### Small underpayment exception
- id: estimated_tax_de_minimis
- kind: threshold
- driven_by: tax shown on the return, reduced by withholding credits
- values: $1,000. No underpayment penalty applies if the tax shown on the return, reduced by the credit allowed under § 31 for amounts withheld, is less than $1,000.
- shape: A single step. Below the figure no penalty applies.
- indexed: no
- why_it_matters: The test subtracts withholding, so a taxpayer with large wage withholding can fall under the figure even with a large total tax.
- source: [26 U.S.C. § 6654(e)(1)](https://www.law.cornell.edu/uscode/text/26/6654) and [IRS Estimated taxes](https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes)
- confidence: high

### No liability in the prior year exception
- id: estimated_tax_no_prior_liability
- kind: rule
- driven_by: prior year tax liability, residency, and the length of the prior tax year
- values: No penalty applies if all three conditions are met. The taxpayer had no tax liability for the prior year. The taxpayer was a US citizen or resident alien for the whole year. The prior tax year covered a 12-month period.
- shape: Not applicable.
- indexed: no
- why_it_matters: The taxpayer had no liability for the prior year if total tax was zero or if the taxpayer was not required to file a return.
- source: [IRS Estimated taxes](https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes) and [26 U.S.C. § 6654(e)(2)](https://www.law.cornell.edu/uscode/text/26/6654)
- confidence: high

### Annualized income installment method
- id: estimated_tax_annualized_method
- kind: rule
- driven_by: the timing of income during the year
- values: If income is received unevenly, the taxpayer can compute each installment on an annualized basis. The applicable percentages are 22.5 for the first installment, 45 for the second, 67.5 for the third, and 90 for the fourth. Annualization uses taxable income, alternative minimum taxable income, and adjusted self-employment income for the months ending before the installment due date. Any reduction from this method is recaptured by increasing the next required installment. The computation is made on Form 2210.
- shape: Four cumulative percentages applied to annualized tax.
- indexed: no
- why_it_matters: The method matches required payments to the periods in which the income was actually received.
- source: [26 U.S.C. § 6654(d)(2)](https://www.law.cornell.edu/uscode/text/26/6654) and [IRS Estimated taxes](https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes)
- confidence: high

### Wage withholding treated as paid across installments
- id: withholding_ratable_treatment
- kind: rule
- driven_by: total federal income tax withheld from wages during the year
- values: Amounts withheld as tax under chapter 24 are treated as payments of estimated tax. An equal part of the total withheld is treated as paid on each installment due date, unless the taxpayer establishes the actual dates of withholding.
- shape: The default allocation spreads total withholding equally across the four installment dates, regardless of when it occurred.
- indexed: no
- why_it_matters: Because withholding is spread across all four dates by default, additional withholding late in the year can cover an earlier installment shortfall.
- source: [26 U.S.C. § 6654(g)](https://www.law.cornell.edu/uscode/text/26/6654)
- confidence: high

---

## 13. Interest Income

### Bank interest
- id: bank_interest_treatment
- kind: rule
- driven_by: the amount of interest credited during the year
- values: Interest on bank accounts, money market accounts, certificates of deposit, and deposited insurance dividends is taxable as ordinary income. It is reported in box 1 of Form 1099-INT and is taxed at the graduated ordinary income rates. Interest forfeited on an early withdrawal from a time deposit appears in box 2 of Form 1099-INT as a deductible amount.
- shape: Not applicable.
- indexed: no
- why_it_matters: Bank interest is net investment income for the 3.8 percent net investment income tax.
- source: [IRS Pub. 550, Taxable Interest — General](https://www.irs.gov/publications/p550) and [IRS Topic no. 559](https://www.irs.gov/taxtopics/tc559)
- confidence: high

### US Treasury interest
- id: treasury_interest_treatment
- kind: rule
- driven_by: the amount of Treasury interest received during the year
- values: Interest income from Treasury bills, notes, and bonds is subject to federal income tax. It is exempt from all state and local income taxes. The amount is reported in box 3 of Form 1099-INT. Interest on obligations issued by any agency or instrumentality of the United States is also taxable for federal purposes. For a Treasury bill, the difference between the discounted purchase price and the face value at maturity is interest income, and it is generally reported when the bill is paid at maturity.
- shape: Not applicable.
- indexed: no
- why_it_matters: Treasury interest is fully taxable at the federal level and is net investment income for the 3.8 percent net investment income tax.
- source: [IRS Pub. 550, U.S. Treasury Bills, Notes, and Bonds](https://www.irs.gov/publications/p550)
- confidence: high

### Municipal bond interest
- id: municipal_bond_interest_treatment
- kind: rule
- driven_by: the issuer of the bond and the use of the bond proceeds
- values: Interest on an obligation issued by a state, the District of Columbia, a US territory, or any of their political subdivisions is generally excluded from gross income. Original issue discount on a tax-exempt state or local bond is treated as tax-exempt interest. Exceptions exist. Interest on an arbitrage bond is taxable. Interest on a private activity bond that is not a qualified bond is taxable. Interest on most state or local home mortgage bonds issued after April 24, 1979 is taxable unless the bond is a qualified mortgage bond or a qualified veterans' mortgage bond.
- shape: Not applicable.
- indexed: no
- why_it_matters: Tax-exempt municipal interest is excluded from gross income, so it does not enter adjusted gross income.
- source: [IRS Pub. 550, State or Local Government Obligations and Tax-Exempt Interest](https://www.irs.gov/publications/p550), and [26 U.S.C. § 103](https://www.law.cornell.edu/uscode/text/26/103)
- confidence: high

### Effect of municipal bond interest on other thresholds
- id: municipal_interest_threshold_effects
- kind: rule
- driven_by: the amount of tax-exempt interest received
- values: Tax-exempt interest is not net investment income and does not enter modified adjusted gross income for the net investment income tax, because it is not in adjusted gross income. A taxpayer who must file a return is still required to report the total tax-exempt interest on line 2a of Form 1040. This is an information reporting requirement and does not convert the interest to taxable interest. The total comes from box 8 of Form 1099-INT, box 11 of Form 1099-OID, and box 12 of Form 1099-DIV. Separately, box 9 of Form 1099-INT and box 13 of Form 1099-DIV report the part of that tax-exempt interest that is subject to AMT. Those box 9 and box 13 amounts are already included in the box 8 and box 12 totals and must not be added again.
- shape: Not applicable.
- indexed: no
- why_it_matters: Interest on a specified private activity bond is a tax preference item for AMT even though it is excluded from regular gross income.
- source: [IRS Pub. 550, Reporting tax-exempt interest](https://www.irs.gov/publications/p550), [IRS Topic no. 559](https://www.irs.gov/taxtopics/tc559), and [26 U.S.C. § 57(a)(5)](https://www.law.cornell.edu/uscode/text/26/57)
- confidence: high — the AMT and net investment income tax points are directly sourced. Tax-exempt interest also affects other computations outside the scope of this document, such as the taxable part of Social Security benefits.

---

## Sources Used

| Document | URL |
|---|---|
| Rev. Proc. 2025-32 (2026 inflation adjustments) | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf |
| IRS Pub. 15 (Circular E), Employer's Tax Guide, 2026 | https://www.irs.gov/publications/p15 |
| IRS Pub. 525, Taxable and Nontaxable Income | https://www.irs.gov/publications/p525 |
| IRS Pub. 550, Investment Income and Expenses | https://www.irs.gov/publications/p550 |
| IRS Topic no. 409, Capital gains and losses | https://www.irs.gov/taxtopics/tc409 |
| IRS Topic no. 427, Stock options | https://www.irs.gov/taxtopics/tc427 |
| IRS Topic no. 559, Net investment income tax | https://www.irs.gov/taxtopics/tc559 |
| Instructions for Form 6251 (2025 revision) | https://www.irs.gov/instructions/i6251 |
| IRS Estimated taxes | https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes |
| IR-2024-273 (2025 figures, used for the AMT before/after comparison) | https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2025 |
| 26 U.S.C. § 53, Credit for prior year minimum tax liability | https://www.law.cornell.edu/uscode/text/26/53 |
| 26 U.S.C. § 55, Alternative minimum tax | https://www.law.cornell.edu/uscode/text/26/55 |
| 26 U.S.C. § 57, Items of tax preference | https://www.law.cornell.edu/uscode/text/26/57 |
| 26 U.S.C. § 83, Property transferred for services | https://www.law.cornell.edu/uscode/text/26/83 |
| 26 U.S.C. § 422, Incentive stock options | https://www.law.cornell.edu/uscode/text/26/422 |
| 26 U.S.C. § 423, Employee stock purchase plans | https://www.law.cornell.edu/uscode/text/26/423 |
| 26 U.S.C. § 1091, Loss from wash sales | https://www.law.cornell.edu/uscode/text/26/1091 |
| 26 U.S.C. § 1202, Qualified small business stock | https://www.law.cornell.edu/uscode/text/26/1202 |
| 26 U.S.C. § 6654, Failure to pay estimated income tax | https://www.law.cornell.edu/uscode/text/26/6654 |
| OBBBA, Public Law 119-21, July 4, 2025 | https://www.congress.gov/bill/119th-congress/house-bill/1/text |

**Note on the US Code links.** The Cornell Legal Information Institute pages reproduce the statutory text of the Internal Revenue Code together with the official amendment notes and effective-date notes. Every OBBBA amendment cited in this document was read from those notes, which name the Public Law section and the effective date.
