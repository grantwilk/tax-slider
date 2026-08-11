# Tax Year 2026 — Federal Deductions and Credits (Working Professional Scope)

Research date: 2026-08-11  
Primary anchors: IRS Revenue Procedure 2025-32; IRS.gov fact sheets / topic pages; P.L. 119-21 (OBBBA, July 4, 2025); current IRC as compiled post-OBBBA.

Figures below are for **tax year 2026** unless a provision first applies in 2025 and continues unchanged through 2026.

---

### SALT deduction cap (2026 indexed amount)
- id: salt_deduction_cap_2026
- kind: cap
- driven_by: MAGI; filing status; itemized state and local taxes paid
- values: $40,400 for all filing statuses other than MFS; $20,200 for married filing separately
- shape: limits the aggregate itemized deduction for state and local income (or sales) tax plus property tax; OBBBA raised the prior $10,000 cap and indexes the higher amount (1% annual step from the 2025 $40,000 base)
- indexed: yes (1% annual increase for 2026–2029 under OBBBA)
- expires: higher cap scheduled through tax year 2029; reverts to $10,000 ($5,000 MFS) for 2030+ unless Congress extends
- why_it_matters: The deductible amount of state and local taxes on Schedule A cannot exceed this cap before any MAGI phase-down.
- source: [NYC Comptroller SALT analysis citing OBBBA / IRC §275(b)](https://comptroller.nyc.gov/reports/the-salt-deduction-in-the-house-budget-bill/); secondary confirmation [TurboTax OBBB SALT table](https://turbotax.intuit.com/tax-tips/tax-deductions-and-credits/unlocking-the-new-salt-cap-how-to-save-up-to-40000-this-tax-season/c3JPyW2bC); statute P.L. 119-21
- confidence: high for $40,400 / $20,200 and 2026 indexing math; medium for exact post-2029 legislative path (multiple secondary sources say revert in 2030)

### SALT MAGI phase-down
- id: salt_magi_phase_down_2026
- kind: phase_out
- driven_by: MAGI; filing status
- values: phase-down starts at MAGI $505,000 (all statuses other than MFS) / $252,500 (MFS); reduction rate 30% of MAGI above the threshold; floor $10,000 ($5,000 MFS)
- shape: start $505,000 ($252,500 MFS); rate reduce allowable SALT cap by $0.30 per $1 of MAGI over start; end when cap reaches floor (~$606,333 MAGI for non-MFS: $505,000 + ($40,400−$10,000)/0.30); floor $10,000 ($5,000 MFS) cannot be breached
- indexed: yes (threshold indexed with the cap for 2026–2029)
- expires: with the higher SALT cap (scheduled through 2029)
- why_it_matters: High-MAGI taxpayers lose part or all of the OBBBA SALT increase and can fall back to the $10,000 floor.
- source: [NYC Comptroller SALT report](https://comptroller.nyc.gov/reports/the-salt-deduction-in-the-house-budget-bill/); [TurboTax OBBB SALT phase-out table](https://turbotax.intuit.com/tax-tips/tax-deductions-and-credits/unlocking-the-new-salt-cap-how-to-save-up-to-40000-this-tax-season/c3JPyW2bC)
- confidence: high

### Mortgage interest — acquisition debt limit
- id: mortgage_interest_acquisition_debt_cap
- kind: cap
- driven_by: acquisition indebtedness principal; loan date; filing status; itemizing
- values: interest deductible only on up to $750,000 of home acquisition debt ($375,000 MFS) for debt incurred after Dec. 15, 2017; grandfathered pre–Dec. 16, 2017 acquisition debt retains $1,000,000 ($500,000 MFS)
- shape: caps the principal amount of acquisition indebtedness on which qualified residence interest may be deducted; applies to principal residence plus one other qualified residence
- indexed: no
- expires: permanent (OBBBA made the TCJA $750,000 limit permanent)
- why_it_matters: Interest on acquisition debt above the cap is not deductible as qualified residence interest.
- source: [IRS Publication 936 (Home Mortgage Interest Deduction)](https://www.irs.gov/publications/p936); OBBBA permanence summarized in practitioner analyses of P.L. 119-21
- confidence: high for dollar caps and grandfather rule; high that OBBBA made the TCJA limit permanent

### Mortgage interest — home equity rules
- id: mortgage_interest_home_equity_rules
- kind: deduction
- driven_by: use of loan proceeds; whether debt is acquisition indebtedness; overall acquisition-debt cap
- values: home-equity / HELOC interest deductible only if proceeds buy, build, or substantially improve a qualified residence and the debt is secured by that residence; still counts toward the $750,000 / $375,000 (or grandfathered) acquisition-debt limit; interest on equity debt used for personal expenses is not deductible
- shape: limits which home-secured interest qualifies; does not create a separate dollar cap beyond the acquisition-debt limit
- indexed: no
- expires: permanent (OBBBA retained TCJA treatment)
- why_it_matters: Interest on a home-equity loan used for non-home purposes does not qualify as deductible residence interest.
- source: [IRS Publication 936](https://www.irs.gov/publications/p936)
- confidence: high

### Charitable contributions — AGI percentage ceilings
- id: charitable_agi_percentage_ceilings
- kind: cap
- driven_by: AGI; gift type; donee type; itemizing
- values: common individual ceilings under IRC §170 — cash to public charities (50%-limit organizations), generally 60% of AGI (OBBBA made the TCJA 60% cash limit permanent); other contributions to public charities generally 50% of AGI; capital-gain property to public charities generally 30% of AGI; cash to private foundations generally 30%; capital-gain property to private foundations generally 20%; excess generally carries forward up to 5 years
- shape: percentage-of-AGI ceilings on the amount deductible in the contribution year before the new 0.5% floor and overall itemized-deduction limitation
- indexed: no (percentage limits)
- expires: 60% cash-to-public-charity ceiling made permanent by OBBBA; other §170 ceilings ongoing
- why_it_matters: These percentages set the maximum charitable deduction relative to AGI before the 2026 floor and top-bracket haircut.
- source: IRC §170; [CCH / Wolters Kluwer OBBBA charitable summary PDF](https://business.cch.com/AllContentPageWhitePapers/VB_OBBBA-charitable-contributions.pdf); [Fidelity Charitable OBBB summary](https://www.fidelitycharitable.org/articles/obbb-tax-reform.html)
- confidence: high for structure; medium for every specialty category nuance (e.g., conservation easements) not fully tabulated here

### Charitable contributions — 0.5%-of-AGI floor for itemizers (new 2026)
- id: charitable_itemizer_half_percent_floor
- kind: deduction
- driven_by: AGI; total otherwise allowable charitable contributions; itemizing
- values: only charitable contributions exceeding 0.5% of AGI are deductible by itemizers; example: AGI $400,000 → first $2,000 of contributions nondeductible
- shape: floor — reduce otherwise allowable charitable deduction by 0.5% of AGI (contributions below the floor are not deductible in the current year under the new rule)
- indexed: no
- expires: permanent under OBBBA (effective for tax years beginning after Dec. 31, 2025)
- why_it_matters: Itemizers lose the first half-percent of AGI of charitable giving as a deduction starting in 2026.
- source: [Lowenstein Sandler OBBBA charitable alert](https://www.lowenstein.com/news-insights/publications/client-alerts/obbba-provisions-impact-charitable-contribution-deductions-te); [CCH OBBBA charitable PDF](https://business.cch.com/AllContentPageWhitePapers/VB_OBBBA-charitable-contributions.pdf); P.L. 119-21
- confidence: high

### Charitable contributions — above-the-line deduction for non-itemizers (new 2026)
- id: charitable_nonitemizer_atl_deduction
- kind: deduction
- driven_by: cash contributions to qualifying public charities; election not to itemize; filing status
- values: up to $1,000 (single / other non-joint) or $2,000 (married filing jointly) of qualifying cash contributions; excludes donor-advised funds and supporting organizations under §509(a)(3)
- shape: dollar cap on an above-the-line / non-itemizer charitable deduction; not subject to the 0.5% itemizer floor
- indexed: no
- expires: permanent under OBBBA starting tax years after Dec. 31, 2025 (no stated sunset in secondary summaries)
- why_it_matters: Taxpayers who take the standard deduction can still deduct limited cash charity gifts starting in 2026.
- source: [Lowenstein Sandler OBBBA charitable alert](https://www.lowenstein.com/news-insights/publications/client-alerts/obbba-provisions-impact-charitable-contribution-deductions-te); [Fidelity Charitable OBBB summary](https://www.fidelitycharitable.org/articles/obbb-tax-reform.html)
- confidence: high for amounts and start year; medium on formal statutory “permanent” label vs. open-ended effective date

### Overall limitation on itemized deductions (35% / 2/37 haircut)
- id: itemized_deduction_top_bracket_limitation
- kind: phase_out
- driven_by: taxable income relative to the 37% bracket threshold; total itemized deductions after other floors/caps
- values: 2026 37% bracket starts at taxable income $768,700 (MFJ/QSS), $640,600 (single and HOH), $384,350 (MFS — half of MFJ from Rev. Proc. 2025-32 Table 4 structure); reduction = (2/37) × lesser of (a) total itemized deductions or (b) taxable income over the 37% threshold
- shape: start at taxable income entering the 37% bracket; rate 2/37 (~5.405%) of the lesser amount above; effect is to limit the marginal tax benefit of itemized deductions in the top bracket to 35% rather than 37%; applies after other itemized floors/limits
- indexed: yes (via inflation-adjusted 37% bracket thresholds in Rev. Proc. 2025-32)
- expires: permanent (OBBBA replaced Pease with this rule for years after 2025)
- why_it_matters: Taxpayers in the 37% bracket lose part of the tax value of their itemized deductions.
- source: [Rev. Proc. 2025-32 §4.01 tax tables](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Thomson Reuters Checkpoint on OBBB §68](https://tax.thomsonreuters.com/news/what-obbb-means-for-your-clients-itemized-deductions-2/); IRC §68 as amended by OBBBA
- confidence: high for formula and 2026 bracket starts for MFJ/single/HOH; medium for exact MFS start if relying on half-of-joint convention without re-checking Table 4 line-by-line ($384,350 commonly cited)

### Qualified Business Income deduction — 20% rate
- id: qbi_20_percent_rate
- kind: deduction
- driven_by: qualified business income; taxable income; filing status; W-2 wages / UBIA for higher incomes; SSTB status
- values: generally 20% of qualified business income under IRC §199A, subject to taxable-income thresholds, wage/UBIA limits, and SSTB rules
- shape: percentage deduction from taxable income (not an itemized deduction)
- indexed: rate fixed at 20%
- expires: permanent (OBBBA removed the prior Dec. 31, 2025 sunset)
- why_it_matters: Pass-through business owners may reduce taxable income by up to one-fifth of QBI.
- source: [Rev. Proc. 2025-32 §2 / §4.26 and OBBBA §70105 notes in RP text](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

### Qualified Business Income — taxable income thresholds and phase-in ranges (2026)
- id: qbi_thresholds_phase_in_2026
- kind: phase_out
- driven_by: taxable income; filing status
- values: threshold / phase-in completion — MFJ $403,500 / $553,500; MFS $201,775 / $276,775; all other returns $201,750 / $276,750 (phase-in width $150,000 MFJ / $75,000 others under OBBBA)
- shape: start at threshold amount; full wage/UBIA limitation (and SSTB disallowance) completes at phase-in range amount; OBBBA widened prior $100k/$50k ranges to $150k/$75k
- indexed: yes (thresholds annually; phase-in widths statutory)
- expires: permanent with §199A
- why_it_matters: Above these taxable-income levels, the QBI deduction is limited or, for SSTBs, reduced to zero over the phase-in range.
- source: [Rev. Proc. 2025-32 §4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

### Qualified Business Income — SSTB rules
- id: qbi_sstb_rules
- kind: deduction
- driven_by: whether the trade or business is a specified service trade or business; taxable income vs. thresholds
- values: SSTBs (health, law, accounting, consulting, athletics, financial services, brokerage, investing/trading, and businesses whose principal asset is the reputation/skill of owners/employees, with customary exceptions) — full QBI treatment below the threshold; deduction phases out over the phase-in range; no QBI deduction from SSTB income once taxable income exceeds the phase-in completion amount
- shape: SSTB limitation keyed to the same taxable-income thresholds/ranges as the wage/UBIA limitation
- indexed: thresholds yes; SSTB definition statutory
- expires: permanent with §199A
- why_it_matters: High-income owners of SSTBs lose the QBI deduction as taxable income moves through and above the phase-in range.
- source: IRC §199A(d); [Rev. Proc. 2025-32 §4.26 thresholds](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high for mechanic; medium for edge-case classification of any particular business

### Qualified Business Income — OBBBA minimum deduction
- id: qbi_minimum_deduction
- kind: deduction
- driven_by: presence of at least $1,000 of QBI from an active qualified trade or business
- values: minimum §199A deduction of $400 if the taxpayer has at least $1,000 of qualifying QBI (amounts first apply for years beginning after Dec. 31, 2025; inflation adjustments begin after 2026)
- shape: floor on the QBI deduction for small active QBI amounts meeting the $1,000 gate
- indexed: yes after 2026
- expires: permanent
- why_it_matters: Taxpayers with small active QBI may still receive a $400 deduction rather than 20% of a tiny QBI figure.
- source: [Rev. Proc. 2025-32 §2.12 describing OBBBA §70105 / IRC §199A(i)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

### Deduction for qualified tips
- id: qualified_tips_deduction
- kind: deduction
- driven_by: qualified tip income in IRS-listed tipped occupations; MAGI; filing status; SSN; reporting on W-2/1099/4137
- values: maximum $25,000; MAGI phase-out starts $150,000 (non-joint) / $300,000 (MFJ); reduced by $100 for each $1,000 (or fraction) of MAGI above the start; fully phased out at $400,000 / $550,000; married taxpayers must file jointly; SSTB employers/self-employed SSTBs ineligible per IRS fact sheet
- shape: start $150k / $300k MFJ; rate $100 per $1,000 MAGI; end $400k / $550k MFJ
- indexed: no (statutory fixed amounts for 2025–2028)
- expires: tax years 2025 through 2028
- why_it_matters: Eligible tipped workers can subtract up to $25,000 of reported qualified tips from federal taxable income.
- source: [IRS FS-2025-03 Working Families Tax Cuts](https://www.irs.gov/newsroom/one-big-beautiful-bill-act-tax-deductions-for-working-americans-and-seniors); phase-out rate confirmed in [U. of Illinois Tax School OBBBA update](https://taxschool.illinois.edu/post/obbba-update-qualified-tips-and-overtime-compensation-for-tax-year-2025/)
- confidence: high for cap, years, start thresholds; high for $100/$1,000 rate from multiple professional summaries of §70201 (IRS fact sheet states phase-out starts but not the per-$1,000 rate)

### Deduction for qualified overtime compensation
- id: qualified_overtime_deduction
- kind: deduction
- driven_by: FLSA-required overtime premium (amount above regular rate); MAGI; filing status; SSN; reporting
- values: maximum $12,500 ($25,000 MFJ); MAGI phase-out starts $150,000 / $300,000 MFJ; same $100 per $1,000 MAGI reduction as tips; fully phased out at $275,000 (non-joint with $12,500 max) / $550,000 (MFJ); married must file jointly
- shape: start $150k / $300k MFJ; rate $100 per $1,000 MAGI; end when reduced max reaches $0
- indexed: no
- expires: tax years 2025 through 2028
- why_it_matters: Workers can deduct the FLSA overtime premium portion of pay, up to the annual cap, for federal income tax.
- source: [IRS FS-2025-03](https://www.irs.gov/newsroom/one-big-beautiful-bill-act-tax-deductions-for-working-americans-and-seniors); [U. of Illinois Tax School OBBBA update](https://taxschool.illinois.edu/post/obbba-update-qualified-tips-and-overtime-compensation-for-tax-year-2025/)
- confidence: high

### Deduction for qualified car loan interest
- id: car_loan_interest_deduction
- kind: deduction
- driven_by: interest on qualifying new personal-use US-assembled vehicle loan originated after Dec. 31, 2024; MAGI; VIN reported on return
- values: maximum $10,000; MAGI phase-out starts $100,000 / $200,000 MFJ; reduced by $200 for each $1,000 of MAGI above the start (fully out at $150,000 / $250,000); lease payments do not qualify; GVWR under 14,000 lbs; final assembly in the United States
- shape: start $100k / $200k MFJ; rate $200 per $1,000 MAGI; end $150k / $250k MFJ
- indexed: no
- expires: tax years 2025 through 2028
- why_it_matters: Buyers of new US-assembled personal vehicles can deduct up to $10,000 of qualifying loan interest.
- source: [IRS FS-2025-03](https://www.irs.gov/newsroom/one-big-beautiful-bill-act-tax-deductions-for-working-americans-and-seniors); phase-out rate from [CPA Validated OBBBA personal deductions](https://cpavalidated.com/senior-tip-overtime-obbba-deductions.html) summarizing P.L. 119-21 §70203
- confidence: high for max and start thresholds (IRS); medium-high for $200/$1,000 rate (statute/secondary; not spelled out on IRS fact sheet)

### Additional senior deduction (age 65+)
- id: additional_senior_deduction
- kind: deduction
- driven_by: age 65+ by year-end; MAGI; filing status; SSN of qualifying individual(s)
- values: $6,000 per eligible individual ($12,000 if both spouses on a joint return qualify); MAGI phase-out starts $75,000 / $150,000 MFJ; reduced by 6% of MAGI above the threshold ($60 per $1,000); fully phased out at $175,000 / $250,000 MFJ; stacks with the existing additional standard deduction for seniors; available to itemizers and non-itemizers; married must file jointly
- shape: start $75k / $150k MFJ; rate 6% of excess MAGI; end $175k / $250k MFJ
- indexed: no (for 2025–2028 statutory amounts)
- expires: tax years 2025 through 2028
- why_it_matters: Taxpayers age 65 or older may deduct an extra $6,000 (per eligible person) against federal taxable income, subject to MAGI phase-out.
- source: [IRS FS-2025-03](https://www.irs.gov/newsroom/one-big-beautiful-bill-act-tax-deductions-for-working-americans-and-seniors); rate mechanics [TurboTax senior deduction](https://turbotax.intuit.com/tax-tips/tax-deductions-and-credits/the-new-one-big-beautiful-bill-senior-deduction-do-you-qualify/c0fGsWtvm)
- confidence: high for amount/years/start (IRS); high for 6% rate from multiple consistent secondary sources of §70103

### Child Tax Credit — maximum amount
- id: child_tax_credit_amount
- kind: credit
- driven_by: number of qualifying children under 17 with valid SSN; MAGI; filing status
- values: maximum $2,200 per qualifying child for 2026
- shape: per-child credit amount under IRC §24
- indexed: yes (OBBBA set $2,200 for 2025 and indexes for years after 2025; 2026 amount confirmed in Rev. Proc. 2025-32)
- expires: permanent (OBBBA)
- why_it_matters: Each qualifying child can reduce tax by up to $2,200 before phase-out and refundability limits.
- source: [Rev. Proc. 2025-32 §4.05(1)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [IRS Child Tax Credit page](https://www.irs.gov/credits-deductions/individuals/child-tax-credit)
- confidence: high

### Child Tax Credit — refundable portion (ACTC)
- id: child_tax_credit_refundable_portion
- kind: credit
- driven_by: unused CTC; earned income (minimum $2,500); other ACTC statutory limits
- values: amount used under §24(d)(1)(A) for 2026 is $1,700 per qualifying child
- shape: caps the refundable Additional Child Tax Credit calculation input for 2026
- indexed: yes
- expires: permanent with expanded CTC
- why_it_matters: Families with little or no tax liability may still receive up to $1,700 per child as a refundable credit.
- source: [Rev. Proc. 2025-32 §4.05(2)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [IRS Child Tax Credit page](https://www.irs.gov/credits-deductions/individuals/child-tax-credit)
- confidence: high

### Child Tax Credit — MAGI phase-out
- id: child_tax_credit_phase_out
- kind: phase_out
- driven_by: MAGI; filing status; total CTC/ODC
- values: phase-out begins at MAGI $200,000 (single, HOH, MFS) / $400,000 (MFJ); credit reduced by $50 for each $1,000 (or fraction) of MAGI above the threshold
- shape: start $200k / $400k MFJ; rate $50 per $1,000 MAGI; end depends on total credit amount
- indexed: no (statutory TCJA/OBBBA thresholds)
- expires: permanent
- why_it_matters: Higher-income parents lose CTC in $50 steps as MAGI rises above the threshold.
- source: [IRS Child Tax Credit page](https://www.irs.gov/credits-deductions/individuals/child-tax-credit); IRC §24(b)/(h)
- confidence: high

### Credit for Other Dependents
- id: credit_for_other_dependents
- kind: credit
- driven_by: dependents who are not qualifying children for CTC; AGI/MAGI; filing status
- values: $500 nonrefundable credit per eligible dependent; same phase-out as CTC ($200,000 / $400,000 MFJ, $50 per $1,000)
- shape: flat per-dependent nonrefundable credit with CTC-aligned phase-out
- indexed: no
- expires: permanent (OBBBA retained)
- why_it_matters: Dependents who do not qualify for the CTC (for example, age 17+) may still generate a $500 credit.
- source: [IRS Child Tax Credit / ODC page](https://www.irs.gov/credits-deductions/individuals/child-tax-credit)
- confidence: high

### Child and Dependent Care Credit — expense limits
- id: cdcc_expense_limits
- kind: cap
- driven_by: number of qualifying individuals; employment-related care expenses; earned income limits
- values: qualifying expenses limited to $3,000 (one qualifying individual) or $6,000 (two or more)
- shape: dollar ceiling on expenses eligible for the credit percentage
- indexed: no
- expires: permanent (unchanged by OBBBA)
- why_it_matters: Only care expenses up to these caps enter the CDCC percentage calculation.
- source: [IRC §21(c) (Cornell LII / House USC)](https://www.law.cornell.edu/uscode/text/26/21)
- confidence: high

### Child and Dependent Care Credit — percentage table (OBBBA 2026)
- id: cdcc_percentage_table_2026
- kind: credit
- driven_by: AGI; filing status; qualifying expenses
- values: applicable percentage starts at 50% for AGI ≤ $15,000; reduced (not below 35%) by 1 percentage point for each $2,000 (or fraction) of AGI over $15,000; further reduced (not below 20%) by 1 percentage point for each $2,000 of AGI over $75,000 ($4,000 of AGI over $150,000 on a joint return); maximum credit at 50% = $1,500 / $3,000
- shape: two-stage AGI phase-down from 50% → 35% plateau → 20% floor
- indexed: no
- expires: permanent (OBBBA rewrite of §21(a)(2) for years after Dec. 31, 2025)
- why_it_matters: OBBBA raises the top CDCC rate from 35% to 50% and adds a second AGI reduction stage before the 20% floor.
- source: [26 U.S.C. §21 (current text)](https://www.law.cornell.edu/uscode/text/26/21); [House USC §21](https://uscode.house.gov/quicksearch/get.plx?section=21&title=26)
- confidence: high for OBBBA 50%/35%/20% formula; medium regarding any separate ARPA-era high-income ($400,000) further phaseout still appearing in some USC compilations—verify against 2026 Form 2441 instructions before relying on a second cliff above $400k

### Student loan interest deduction
- id: student_loan_interest_deduction
- kind: deduction
- driven_by: qualified student loan interest paid; MAGI; filing status (MFS ineligible)
- values: maximum $2,500; 2026 MAGI phase-out $85,000–$100,000 (single/HOH/QSS) and $175,000–$205,000 (MFJ)
- shape: start $85k / $175k MFJ; end $100k / $205k MFJ; linear phase-out across the range
- indexed: phase-out thresholds yes; $2,500 cap no
- expires: permanent
- why_it_matters: Borrowers can deduct up to $2,500 of student loan interest above the line if MAGI is below the phase-out end.
- source: [Rev. Proc. 2025-32 §4.29](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

### American Opportunity Tax Credit
- id: american_opportunity_tax_credit
- kind: credit
- driven_by: adjusted qualified education expenses per eligible student; MAGI; filing status; student eligibility (first four years, half-time, etc.); beginning 2026, work-authorized SSN required per IRS education-credits page
- values: up to $2,500 per eligible student (100% of first $2,000 + 25% of next $2,000); 40% refundable (up to $1,000); MAGI phase-out $80,000–$90,000 (single/HOH/QSS) / $160,000–$180,000 (MFJ); no credit at MAGI ≥ $90,000 / $180,000 MFJ
- shape: start of phase-out $80k / $160k MFJ; complete $90k / $180k MFJ
- indexed: no (phase-out frozen after 2020)
- expires: permanent
- why_it_matters: Eligible undergrad expenses can produce up to $2,500 credit per student, partly refundable.
- source: [IRS Education credits AOTC/LLC page](https://www.irs.gov/credits-deductions/individuals/education-credits-aotc-and-llc); [IRS Instructions for Form 8863](https://www.irs.gov/instructions/i8863)
- confidence: high

### Lifetime Learning Credit
- id: lifetime_learning_credit
- kind: credit
- driven_by: adjusted qualified education expenses (all students on the return); MAGI; filing status
- values: 20% of up to $10,000 of expenses = maximum $2,000 per return; same MAGI phase-out as AOTC ($80k–$90k / $160k–$180k MFJ); nonrefundable
- shape: start $80k / $160k MFJ; end $90k / $180k MFJ
- indexed: no
- expires: permanent
- why_it_matters: Graduate and job-skill courses can generate up to $2,000 of nonrefundable credit per return.
- source: [IRS Education credits AOTC/LLC page](https://www.irs.gov/credits-deductions/individuals/education-credits-aotc-and-llc); [IRS Instructions for Form 8863](https://www.irs.gov/instructions/i8863)
- confidence: high

### Medical expense deduction AGI floor
- id: medical_expense_agi_floor
- kind: deduction
- driven_by: AGI; unreimbursed medical/dental expenses; itemizing
- values: deductible only to the extent expenses exceed 7.5% of AGI
- shape: 7.5% AGI floor on Schedule A medical deduction
- indexed: no
- expires: permanent at 7.5% (CAA 2021 permanence; OBBBA did not raise the floor)
- why_it_matters: Only medical costs above 7.5% of AGI can be itemized.
- source: [IRS Topic No. 502](https://www.irs.gov/taxtopics/tc502); IRC §213(a)
- confidence: high

### Adoption credit — maximum and phase-out
- id: adoption_credit_maximum_phase_out
- kind: credit
- driven_by: qualified adoption expenses (or special-needs adoption); MAGI
- values: 2026 maximum $17,670; phase-out begins MAGI > $265,080 and completes at MAGI ≥ $305,080
- shape: start $265,080; end $305,080; dollar-for-dollar phase-out over $40,000 MAGI window
- indexed: yes
- expires: ongoing (refundability feature added by OBBBA)
- why_it_matters: Adoption expenses (or the special-needs amount) can generate a credit up to $17,670, reduced for high MAGI.
- source: [Rev. Proc. 2025-32 §4.04](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

### Adoption credit — refundable portion (OBBBA)
- id: adoption_credit_refundable_portion
- kind: credit
- driven_by: adoption credit after nonrefundable limitation; §23(a)(4) refundable amount
- values: 2026 refundable portion amount $5,120
- shape: portion of the adoption credit that may be refundable under §23(a)(4)
- indexed: yes
- expires: ongoing under OBBBA refundability rules
- why_it_matters: Part of the adoption credit can create a refund even when tax liability is low.
- source: [Rev. Proc. 2025-32 §4.04(3)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

### Residential clean energy credit (§25D) — terminated
- id: residential_clean_energy_credit_25d_repealed
- kind: repealed
- driven_by: timing of expenditures / installation completion
- values: credit not allowed for expenditures treated as made after December 31, 2025 (installation completion controls under §25D(e)(8))
- shape: terminated — no 2026 credit for post-2025 installations even if paid in 2025
- indexed: n/a
- expires: ended after Dec. 31, 2025
- why_it_matters: Solar and other residential clean-energy property installed in 2026 does not qualify for §25D.
- source: [IRS FS-2025-05 OBBB energy credit FAQs](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb)
- confidence: high

### Energy efficient home improvement credit (§25C) — terminated
- id: energy_efficient_home_improvement_credit_25c_repealed
- kind: repealed
- driven_by: placed-in-service date
- values: credit not allowed for property placed in service after December 31, 2025
- shape: terminated for post-2025 placed-in-service dates
- indexed: n/a
- expires: ended after Dec. 31, 2025
- why_it_matters: 2026 home-efficiency improvements do not qualify for §25C.
- source: [IRS FS-2025-05](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb)
- confidence: high

### New clean vehicle credit (§30D) — terminated
- id: new_clean_vehicle_credit_30d_repealed
- kind: repealed
- driven_by: vehicle acquisition date (binding contract + payment)
- values: credit not allowed for vehicles acquired after September 30, 2025
- shape: terminated for acquisitions after Sept. 30, 2025; vehicles acquired on/before that date may still qualify when later placed in service
- indexed: n/a
- expires: ended for acquisitions after Sept. 30, 2025
- why_it_matters: New EVs acquired in 2026 do not qualify for §30D.
- source: [IRS FS-2025-05](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb)
- confidence: high

### Previously-owned clean vehicle credit (§25E) — terminated
- id: used_clean_vehicle_credit_25e_repealed
- kind: repealed
- driven_by: vehicle acquisition date
- values: credit not allowed for vehicles acquired after September 30, 2025
- shape: terminated for acquisitions after Sept. 30, 2025
- indexed: n/a
- expires: ended for acquisitions after Sept. 30, 2025
- why_it_matters: Used EVs acquired in 2026 do not qualify for §25E.
- source: [IRS FS-2025-05](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb)
- confidence: high

### Alternative fuel vehicle refueling property credit (§30C) — terminating mid-2026
- id: alt_fuel_refueling_credit_30c_repealed
- kind: repealed
- driven_by: placed-in-service date
- values: credit not allowed for property placed in service after June 30, 2026
- shape: available only for property placed in service on or before June 30, 2026
- indexed: n/a
- expires: after June 30, 2026
- why_it_matters: Home/business EV chargers placed in service in the second half of 2026 do not qualify for §30C.
- source: [IRS FS-2025-05](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb)
- confidence: high

---

## Parameter count
Documented parameter blocks above: **33**.

## Notes on confirmation gaps
- Exact statutory text of P.L. 119-21 was not successfully fetched as PDF in this pass; several OBBBA mechanics rely on IRS fact sheets + consistent professional summaries (JCT/CRS/Tax Foundation-class and firm alerts).
- SALT post-2029 duration: secondary sources mostly say revert in 2030; at least one local-government analysis described indexing through 2033 — treat sunset year with care against the enrolled bill.
- CDCC: confirm whether any additional >$400k AGI phaseout from older temporary rules appears on 2026 Form 2441.
- Car-loan and tip/overtime *rates* of phase-out: IRS FS-2025-03 gives starts and maxima; per-$1,000 rates come from statute summaries / Schedule 1-A practitioner writeups.
