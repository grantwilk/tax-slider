# Leg A — US Federal Core Income-Tax Parameters, Tax Year 2026

Tax year 2026. Returns are filed in early 2027. Research date: August 11, 2026.

All inflation-adjusted figures come from IRS Revenue Procedure 2025-32 (released October 9, 2025).
That document states the 2026 amounts for the Code as in effect on October 9, 2025, after the
One Big Beautiful Bill Act (OBBBA, Public Law 119-21, July 4, 2025). Statutory changes are cited to
the enacted public law text on govinfo.gov. No 2025 figure is reported here as a 2026 figure.

Out of scope for this leg: state taxes, retirement account limits, itemized deductions, credits,
equity compensation.

---

### Ordinary Income Tax Brackets and Rates

- id: ordinary_income_tax_brackets
- kind: bracket
- driven_by: taxable income and filing status
- values:

  Single (§ 1(j)(2)(C)):

  | Rate | Taxable income band | Tax |
  |---|---|---|
  | 10% | $0 to $12,400 | 10% of taxable income |
  | 12% | over $12,400 to $50,400 | $1,240 + 12% of the excess over $12,400 |
  | 22% | over $50,400 to $105,700 | $5,800 + 22% of the excess over $50,400 |
  | 24% | over $105,700 to $201,775 | $17,966 + 24% of the excess over $105,700 |
  | 32% | over $201,775 to $256,225 | $41,024 + 32% of the excess over $201,775 |
  | 35% | over $256,225 to $640,600 | $58,448 + 35% of the excess over $256,225 |
  | 37% | over $640,600 | $192,979.25 + 37% of the excess over $640,600 |

  Married Filing Jointly and Surviving Spouses (§ 1(j)(2)(A)):

  | Rate | Taxable income band | Tax |
  |---|---|---|
  | 10% | $0 to $24,800 | 10% of taxable income |
  | 12% | over $24,800 to $100,800 | $2,480 + 12% of the excess over $24,800 |
  | 22% | over $100,800 to $211,400 | $11,600 + 22% of the excess over $100,800 |
  | 24% | over $211,400 to $403,550 | $35,932 + 24% of the excess over $211,400 |
  | 32% | over $403,550 to $512,450 | $82,048 + 32% of the excess over $403,550 |
  | 35% | over $512,450 to $768,700 | $116,896 + 35% of the excess over $512,450 |
  | 37% | over $768,700 | $206,583.50 + 37% of the excess over $768,700 |

  Married Filing Separately (§ 1(j)(2)(D)):

  | Rate | Taxable income band | Tax |
  |---|---|---|
  | 10% | $0 to $12,400 | 10% of taxable income |
  | 12% | over $12,400 to $50,400 | $1,240 + 12% of the excess over $12,400 |
  | 22% | over $50,400 to $105,700 | $5,800 + 22% of the excess over $50,400 |
  | 24% | over $105,700 to $201,775 | $17,966 + 24% of the excess over $105,700 |
  | 32% | over $201,775 to $256,225 | $41,024 + 32% of the excess over $201,775 |
  | 35% | over $256,225 to $384,350 | $58,448 + 35% of the excess over $256,225 |
  | 37% | over $384,350 | $103,291.75 + 37% of the excess over $384,350 |

  Head of Household (§ 1(j)(2)(B)):

  | Rate | Taxable income band | Tax |
  |---|---|---|
  | 10% | $0 to $17,700 | 10% of taxable income |
  | 12% | over $17,700 to $67,450 | $1,770 + 12% of the excess over $17,700 |
  | 22% | over $67,450 to $105,700 | $7,740 + 22% of the excess over $67,450 |
  | 24% | over $105,700 to $201,750 | $16,155 + 24% of the excess over $105,700 |
  | 32% | over $201,750 to $256,200 | $39,207 + 32% of the excess over $201,750 |
  | 35% | over $256,200 to $640,600 | $56,631 + 35% of the excess over $256,200 |
  | 37% | over $640,600 | $191,171 + 37% of the excess over $640,600 |

  Estates and trusts (§ 1(j)(2)(E)), for reference: 10% to $3,300, 24% to $11,700,
  35% to $16,000, 37% over $16,000.
- shape: seven marginal bands per filing status. Each rate applies only to the income inside its
  band. The MFS 37% band starts at $384,350, which is one half of the MFJ start of $768,700.
  The HoH 24% and 32% band edges ($201,750 and $256,200) are $25 and $25 below the Single
  edges ($201,775 and $256,225). This small split is real and appears in the Revenue Procedure.
- indexed: yes, to chained CPI-U (C-CPI-U) under § 1(f)(3). OBBBA § 70101(b) limited the
  2017 base-year substitution in § 1(j)(3)(B)(i) to the ends of brackets above 12% and the
  starts of brackets above 22%. As a result the 10% and 12% band edges received one extra year
  of inflation adjustment for 2026 and rose about 4%, while the higher edges rose about 2.3%.
- why_it_matters: These bands set the marginal and total tax on ordinary income.
- source: [Rev. Proc. 2025-32 § 4.01](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); statutory
  change at [P.L. 119-21 § 70101](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm);
  cross-check at [IRS IR-2025-103](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill)
- confidence: high. Every cumulative tax figure was recomputed from the band edges and matches
  the Revenue Procedure exactly.

---

### Basic Standard Deduction

- id: standard_deduction
- kind: limit
- driven_by: filing status
- values:

  | Filing status | 2026 amount |
  |---|---|
  | Married Filing Jointly and Surviving Spouses | $32,200 |
  | Head of Household | $24,150 |
  | Single | $16,100 |
  | Married Filing Separately | $16,100 |

- shape: a flat subtraction from adjusted gross income. There is no phase-out and no income limit.
  A taxpayer takes either this amount or total itemized deductions, not both.
- indexed: yes, to C-CPI-U under § 63(c)(4), from a 2025 base year set by OBBBA.
- why_it_matters: This amount reduces adjusted gross income to taxable income for a taxpayer who
  does not itemize.
- source: [Rev. Proc. 2025-32 § 4.14(1)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); statutory
  change at [P.L. 119-21 § 70102](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)
- confidence: high

---

### Additional Standard Deduction for Age 65+ and for Blindness

- id: additional_standard_deduction_aged_or_blind
- kind: limit
- driven_by: age at the end of the tax year, blindness, and marital status
- values:
  - $1,650 per qualifying condition if the taxpayer is married (MFJ or MFS) or a surviving spouse.
  - $2,050 per qualifying condition if the taxpayer is unmarried and not a surviving spouse
    (Single or Head of Household).
- shape: this is an addition to the basic standard deduction, not a separate deduction. The amount
  is counted once for age 65 or over and once for blindness. One person can therefore claim it
  twice. Examples: a Single filer who is 65 or over and blind adds $4,100, for a total standard
  deduction of $20,200. An MFJ couple in which both spouses are 65 or over and both are blind
  adds $6,600, for a total of $38,800. An MFJ couple in which one spouse is 65 or over adds
  $1,650, for a total of $33,850. There is no income phase-out.
- indexed: yes, to C-CPI-U under § 63(c)(4).
- why_it_matters: A taxpayer who is 65 or over, or blind, and who does not itemize, subtracts this
  amount in addition to the basic standard deduction.
- source: [Rev. Proc. 2025-32 § 4.14(3)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high. Note that a person born on January 1, 1962 is treated as 65 on
  December 31, 2026 under the standard "day before the birthday" rule.

---

### Standard Deduction Limit for a Person Claimed as a Dependent

- id: dependent_standard_deduction_limit
- kind: limit
- driven_by: earned income of the dependent
- values: the greater of $1,350, or the sum of $450 and the earned income of the dependent.
- shape: a floor and a formula, capped at the top by the normal standard deduction for the filing
  status of the dependent. With $0 earned income the deduction is $1,350. With $5,000 earned
  income it is $5,450. With $20,000 earned income it is capped at $16,100 for a Single dependent.
- indexed: yes, to C-CPI-U under § 63(c)(4). The $1,350 and $450 amounts are both adjusted.
- why_it_matters: This limit sets the standard deduction of a child or other dependent who files a
  return, and it feeds the kiddie tax calculation.
- source: [Rev. Proc. 2025-32 § 4.14(2)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

---

### OBBBA Senior Deduction (Age 65+)

- id: senior_deduction_obbba
- kind: phase_out
- driven_by: age 65 or over, and modified adjusted gross income (MAGI)
- values: $6,000 for each qualified individual. A qualified individual is the taxpayer if the
  taxpayer reaches age 65 before the close of the tax year, and, on a joint return, the spouse if
  the spouse reaches age 65 before the close of the tax year. The maximum on a joint return with
  two qualifying spouses is $12,000. Married Filing Separately is not eligible, because the
  statute requires a joint return for a married taxpayer.
- shape: phase-out start is MAGI of $75,000 (Single, HoH, Surviving Spouse) or $150,000 (MFJ).
  Rate is 6% of MAGI above the start, applied against the $6,000 per-person amount, not below
  zero. Complete phase-out is MAGI of $175,000 for a single filer. For MFJ the per-person $6,000
  reaches zero at MAGI of $250,000, whether one spouse or both spouses qualify. MAGI here is AGI
  increased by amounts excluded under § 911, § 931, or § 933.
- indexed: no. The $6,000 amount and both thresholds are fixed in statute. The deduction applies
  only to tax years that begin before January 1, 2029, so 2025 through 2028.
- why_it_matters: A taxpayer age 65 or over subtracts this amount whether the taxpayer itemizes or
  takes the standard deduction.
- source: [P.L. 119-21 § 70103, adding IRC § 151(d)(5)(C)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm);
  plain-language summary at [IRS FS-2025-03](https://www.irs.gov/newsroom/one-big-beautiful-bill-act-tax-deductions-for-working-americans-and-seniors);
  2026 confirmation at [Form 1040-ES (2026)](https://www.irs.gov/pub/irs-pdf/f1040es.pdf)
- confidence: high on the amount, the age test, the thresholds, the 6% rate, and the MFS
  exclusion. Medium on the $250,000 complete phase-out for a two-qualifying-spouse joint return.
  The statute reduces "the $6,000 amount", which is a per-individual amount, so both $6,000
  amounts reach zero at the same MAGI of $250,000. Some third-party calculators instead publish
  $350,000 for that case. The statutory text supports $250,000. This parameter overlaps the
  deductions and age-milestones legs.

---

### Long-Term Capital Gains and Qualified Dividend Brackets

- id: long_term_capital_gains_brackets
- kind: bracket
- driven_by: taxable income and filing status
- values:

  | Filing status | 0% applies up to | 15% applies up to | 20% applies above |
  |---|---|---|---|
  | Married Filing Jointly and Surviving Spouses | $98,900 | $613,700 | $613,700 |
  | Head of Household | $66,200 | $579,600 | $579,600 |
  | Single | $49,450 | $545,500 | $545,500 |
  | Married Filing Separately | $49,450 | $306,850 | $306,850 |
  | Estates and Trusts | $3,300 | $16,250 | $16,250 |

- shape: three bands measured against total taxable income, not against the gain alone. Long-term
  gain and qualified dividends stack on top of ordinary income. Ordinary income fills the lower
  bands first, and the remaining room decides how much gain is taxed at 0% and at 15%. The 20%
  rate applies only to the part of the gain above the 15% ceiling. Three separate maximum rates
  sit outside this schedule: 28% on collectibles, 28% on the taxable part of § 1202 qualified
  small business stock, and 25% on unrecaptured § 1250 gain.
- indexed: yes, to C-CPI-U under § 1(j)(5)(B).
- why_it_matters: These bands set the federal rate on net long-term capital gain and on qualified
  dividends.
- source: [Rev. Proc. 2025-32 § 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); rate
  structure and the 25%/28% exceptions at [IRS Topic no. 409](https://www.irs.gov/taxtopics/tc409)
- confidence: high for the 2026 amounts. Note that IRS Topic no. 409 still published tax year 2025
  breakpoints as of its February 25, 2026 review date, so the Revenue Procedure is the source for
  the 2026 figures.

---

### Net Investment Income Tax (NIIT), 3.8%

- id: niit_threshold
- kind: rate
- driven_by: modified adjusted gross income (MAGI) and net investment income
- values: rate is 3.8%. MAGI thresholds:

  | Filing status | Threshold |
  |---|---|
  | Married Filing Jointly | $250,000 |
  | Qualifying Surviving Spouse | $250,000 |
  | Married Filing Separately | $125,000 |
  | Single | $200,000 |
  | Head of Household | $200,000 |

- shape: not a cliff. The tax equals 3.8% of the lesser of two amounts: net investment income, or
  the amount by which MAGI exceeds the threshold. At MAGI one dollar over the threshold the tax is
  3.8 cents, so the tax phases in. MAGI here is AGI increased by the net foreign earned income
  excluded under § 911. Net investment income covers interest, dividends, capital gains, rents,
  royalties, non-qualified annuities, and passive business income. It excludes wages,
  self-employment income, Social Security benefits, tax-exempt interest, and distributions from
  qualified plans under § 401(a), § 403(a), § 403(b), § 408, § 408A, and § 457(b). Estates and
  trusts use a different test: undistributed net investment income, and AGI above the start of the
  top § 1(e) bracket, which is $16,000 for 2026. The tax is reported on Form 8960.
- indexed: no. The IRS states directly that these threshold amounts are not indexed for inflation.
  The amounts are fixed in § 1411(b) and have not changed since 2013.
- why_it_matters: This tax adds 3.8% on investment income above the MAGI threshold, on top of the
  ordinary or capital gains rate.
- source: [IRS, Net Investment Income Tax](https://www.irs.gov/individuals/net-investment-income-tax);
  indexing answer at [IRS, Questions and Answers on the Net Investment Income Tax, Q3](https://www.irs.gov/newsroom/questions-and-answers-on-the-net-investment-income-tax);
  trust threshold at [Rev. Proc. 2025-32 § 4.01 Table 5](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

---

### Additional Medicare Tax, 0.9%

- id: additional_medicare_tax
- kind: rate
- driven_by: wages, Railroad Retirement (RRTA) compensation, and self-employment income
- values: rate is 0.9%. Thresholds:

  | Filing status | Threshold |
  |---|---|
  | Married Filing Jointly | $250,000 |
  | Married Filing Separately | $125,000 |
  | Single | $200,000 |
  | Head of Household | $200,000 |
  | Qualifying Surviving Spouse | $200,000 |

- shape: the 0.9% applies only to the earnings above the threshold, not to the first dollar.
  Wages and self-employment income are combined against one threshold. A self-employment loss is
  ignored. RRTA compensation is compared to the threshold separately from FICA wages. An employer
  must withhold the 0.9% on wages above $200,000 paid by that employer, without regard to filing
  status or to wages from another employer. There is no employer match. Any difference between
  withholding and the true liability is settled on Form 8959 with the return.
- indexed: no. The dollar amounts are written into § 3101(b)(2) and carry no inflation adjustment.
- why_it_matters: This tax raises the employee Medicare rate from 1.45% to 2.35% on earnings above
  the threshold.
- source: [IRS, Questions and answers for the Additional Medicare Tax](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax);
  withholding rule at [IRS Topic no. 751](https://www.irs.gov/taxtopics/tc751);
  statute at [26 U.S.C. § 3101(b)(2)](https://www.law.cornell.edu/uscode/text/26/3101)
- confidence: high

---

### Social Security (OASDI) Wage Base

- id: social_security_wage_base
- kind: limit
- driven_by: wages and self-employment income
- values: $184,500 for 2026. The 2025 base was $176,100, so the increase is $8,400, or 4.8%.
- shape: a hard ceiling. Every dollar of covered earnings up to $184,500 carries the OASDI tax.
  Every dollar above it carries none. The maximum OASDI tax is $11,439.00 for the employee and
  $11,439.00 for the employer. The maximum for a self-employed person is $22,878.00. The same
  ceiling caps the earnings used in the Social Security benefit formula.
- indexed: yes, to the national average wage index (AWI) under § 230(b) of the Social Security Act,
  rounded to the nearest multiple of $300. This is wage indexing, not price indexing.
- why_it_matters: Earnings above $184,500 in 2026 carry no Social Security tax.
- source: [SSA, Contribution and Benefit Base](https://www.ssa.gov/oact/cola/cbb.html);
  computation at [SSA automatic adjustment notice, 90 FR, November 3, 2025](https://www.govinfo.gov/content/pkg/FR-2025-11-03/html/2025-19763.htm);
  cross-check at [IRS Topic no. 751](https://www.irs.gov/taxtopics/tc751)
- confidence: high

---

### Social Security (OASDI) Tax Rate

- id: social_security_tax_rate
- kind: rate
- driven_by: wages up to the wage base
- values: 6.2% employee and 6.2% employer, for 12.4% combined. Self-employed persons pay 12.4%.
- shape: a flat rate on covered wages up to $184,500. The rate drops to zero above the base.
- indexed: no. The rate is fixed by statute in § 3101(a) and § 3111(a).
- why_it_matters: This rate applies to the first $184,500 of covered earnings in 2026.
- source: [IRS Topic no. 751](https://www.irs.gov/taxtopics/tc751);
  [SSA, Contribution and Benefit Base](https://www.ssa.gov/oact/cola/cbb.html)
- confidence: high

---

### Medicare (Hospital Insurance) Tax Rate

- id: medicare_tax_rate
- kind: rate
- driven_by: all covered wages and self-employment income
- values: 1.45% employee and 1.45% employer, for 2.9% combined. Self-employed persons pay 2.9%.
- shape: a flat rate with no wage ceiling. The Additional Medicare Tax of 0.9% adds to the employee
  side above the thresholds in the block above, which brings the employee rate to 2.35% and the
  self-employed rate to 3.8% on that excess.
- indexed: no. The rate is fixed by statute in § 3101(b)(1) and § 3111(b).
- why_it_matters: This rate applies to every dollar of covered earnings, with no cap.
- source: [IRS Topic no. 751](https://www.irs.gov/taxtopics/tc751);
  [SSA, Contribution and Benefit Base](https://www.ssa.gov/oact/cola/cbb.html)
- confidence: high

---

### Self-Employment Tax Rate

- id: self_employment_tax_rate
- kind: rate
- driven_by: net earnings from self-employment
- values: 12.4% OASDI on net earnings up to $184,500, plus 2.9% Medicare on all net earnings, for
  15.3% combined below the base.
- shape: net earnings from self-employment equal 92.35% of net profit. One half of the resulting
  self-employment tax is deductible in computing AGI. The 0.9% Additional Medicare Tax applies on
  top, above the filing-status threshold, and that part is not deductible.
- indexed: the rates are fixed. The $184,500 OASDI ceiling is wage-indexed.
- why_it_matters: A self-employed person pays both the employee and employer halves of FICA.
- source: [SSA, Contribution and Benefit Base](https://www.ssa.gov/oact/cola/cbb.html);
  deduction mechanics at [Form 1040-ES (2026), self-employment worksheet](https://www.irs.gov/pub/irs-pdf/f1040es.pdf)
- confidence: high

---

### AMT Exemption Amount

- id: amt_exemption
- kind: limit
- driven_by: alternative minimum taxable income (AMTI) and filing status
- values:

  | Filing status | 2026 exemption |
  |---|---|
  | Married Filing Jointly and Surviving Spouses | $140,200 |
  | Unmarried Individuals, which includes Head of Household | $90,100 |
  | Married Filing Separately | $70,100 |
  | Estates and Trusts | $31,400 |

- shape: a flat subtraction from AMTI before the AMT rates apply. The AMT has no separate Head of
  Household category. A Head of Household filer uses the unmarried amount of $90,100. The
  exemption is reduced by the phase-out described in the next block.
- indexed: yes. Under § 55(d)(4)(B), the base exemption amounts of $109,400 and $70,300 keep a
  calendar year 2017 inflation base, so the exemption still rises each year.
- why_it_matters: AMT applies only when tentative minimum tax, computed after this exemption,
  exceeds regular tax.
- source: [Rev. Proc. 2025-32 § 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf);
  statutory change at [P.L. 119-21 § 70107](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)
- confidence: high

---

### AMT Exemption Phase-Out (Changed by OBBBA for 2026)

- id: amt_exemption_phase_out
- kind: phase_out
- driven_by: alternative minimum taxable income (AMTI)
- values:

  | Filing status | Phase-out starts | Rate | Exemption reaches zero |
  |---|---|---|---|
  | Married Filing Jointly and Surviving Spouses | $1,000,000 | 50% | $1,280,400 |
  | Unmarried Individuals, which includes Head of Household | $500,000 | 50% | $680,200 |
  | Married Filing Separately | $500,000 | 50% | $640,200 |
  | Estates and Trusts | $104,800 | 50% | $167,600 |

- shape: the exemption is reduced by 50 cents for each dollar of AMTI above the start, and not
  below zero. Inside the phase-out band each extra dollar of AMTI both adds to AMTI and removes
  50 cents of exemption, which produces an effective marginal AMT rate of about 39% (1.5 × 26%) or
  42% (1.5 × 28%) in that band. The complete phase-out points in the table are arithmetic:
  $1,000,000 + ($140,200 ÷ 0.50) = $1,280,400, and $500,000 + ($90,100 ÷ 0.50) = $680,200.
- indexed: the exemption amounts are indexed, but the phase-out start amounts are NOT indexed for
  2026. OBBBA § 70107(b) set the inflation base year for the $1,000,000 amount to calendar year
  2025, and Rev. Proc. 2025-32 § 2.07 states that the $1,000,000 amount is not adjusted for
  inflation for any tax year that begins before January 1, 2027. Indexing of the phase-out start
  restarts in 2027.
- why_it_matters: This phase-out removes the AMT exemption from higher-AMTI taxpayers and raises
  the effective marginal AMT rate inside the band.
- source: [Rev. Proc. 2025-32 §§ 2.07 and 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf);
  statute at [P.L. 119-21 § 70107(b) and (c)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm);
  cross-check at [IRS IR-2025-103](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill)
- confidence: high. WHAT OBBBA CHANGED, effective for tax years that begin after
  December 31, 2025: (1) the phase-out start was reset to the unindexed 2018 base amounts of
  $500,000 and $1,000,000. For 2025 the indexed starts were $626,350 (unmarried and MFS) and
  $1,252,700 (MFJ), per [Rev. Proc. 2024-40 § 4.11](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf),
  so the 2026 start is LOWER than the 2025 start by $126,350 and $252,700. (2) The
  phase-out rate rose from 25% to 50%, by inserting new § 55(d)(4)(A)(ii)(IV) with the words
  "by substituting '50 percent' for '25 percent'". Both changes are permanent and both widen AMT
  exposure. The 50% rate was verified two ways: from the enacted statute text, and by recomputing
  every complete phase-out figure in Rev. Proc. 2025-32 § 4.10, which only reconciles at 50%.

---

### AMT 26% / 28% Rate Breakpoint

- id: amt_rate_breakpoint
- kind: bracket
- driven_by: taxable excess, which is AMTI minus the AMT exemption
- values:

  | Filing status | 26% applies up to | 28% applies above |
  |---|---|---|
  | Married Filing Separately | $122,250 | $122,250 |
  | All other taxpayers | $244,500 | $244,500 |

- shape: two bands measured against the taxable excess under § 55(b)(1), not against AMTI and not
  against regular taxable income. The MFS breakpoint is one half of the amount for all other
  taxpayers. A separate rule in § 55(d)(3) increases AMTI for an MFS filer by the lesser of 25% of
  the excess of AMTI over the complete phase-out point, or the exemption amount.
- indexed: yes, to C-CPI-U under § 55(d)(4)(B).
- why_it_matters: The AMT charges 26% on the first band of taxable excess and 28% on the rest.
- source: [Rev. Proc. 2025-32 § 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

---

### Kiddie Tax Threshold

- id: kiddie_tax_threshold
- kind: cliff
- driven_by: unearned income of the child
- values: the § 1(g)(4)(A)(ii)(I) amount for 2026 is $1,350. Unearned income above $2,700
  (two times $1,350) is taxed at the marginal rate of the parent.
- shape: three tiers of unearned income for a child with no itemized deductions.
  Tier 1, the first $1,350, is offset by the standard deduction of the dependent and is untaxed.
  Tier 2, the next $1,350 (from $1,350 to $2,700), is taxed at the rate of the child.
  Tier 3, everything above $2,700, is taxed at the marginal rate of the parent.
  On each side of the $2,700 line: below it, no parent rate applies and Form 8615 is not needed.
  Above it, Form 8615 is required and the parent rate applies to the excess only, so there is no
  jump in total tax at the line. A child who must file Form 8615 can also owe NIIT.
- indexed: yes. The $1,350 amount tracks the § 63(c)(5)(A) dependent floor, which is adjusted to
  C-CPI-U. The $2,700 figure moves with it.
- why_it_matters: Above $2,700 of unearned income, the tax on a child's investment income is
  computed at the parent's marginal rate instead of the child's rate.
- source: [Rev. Proc. 2025-32 § 4.02](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf);
  mechanics at [IRS Topic no. 553](https://www.irs.gov/taxtopics/tc553)
- confidence: high. The 2025 amount was also $1,350, so IRS Topic no. 553 shows the same $2,700
  and $13,500 figures for both years. The 2026 figure is confirmed independently by
  Rev. Proc. 2025-32.

---

### Kiddie Tax Age and Support Test

- id: kiddie_tax_applicability
- kind: cliff
- driven_by: age at the end of the tax year, student status, and earned income relative to support
- values: the kiddie tax applies to a child who meets one of these age tests, and whose unearned
  income is more than $2,700:
  - under age 18 at the end of the tax year, with no support test, or
  - age 18 at the end of the tax year, and earned income is not more than half of the child's own
    support, or
  - age 19 through 23 at the end of the tax year, a full-time student, and earned income is not
    more than half of the child's own support.
- shape: three further conditions apply. At least one parent must be alive at the end of the year,
  the child must be required to file a return, and the child must not file a joint return. On each
  side of the "half of support" line: at or below half, the kiddie tax applies. Above half, it
  does not, and the child pays tax at the child's own rates.
- indexed: no. These are age and ratio tests written into § 1(g)(2), with no dollar amounts.
- why_it_matters: These tests decide whether a child's unearned income is taxed at the parent's
  rate at all.
- source: [IRS Topic no. 553](https://www.irs.gov/taxtopics/tc553)
- confidence: high

---

### Kiddie Tax Parental Election Limit (Form 8814)

- id: kiddie_tax_parental_election_limit
- kind: cliff
- driven_by: gross income of the child, and the type of that income
- values: the parent can elect to report the child's income on the parent's return when the child's
  gross income is more than $1,350 and less than $13,500 for 2026.
- shape: the ceiling is ten times the § 1(g)(4)(A)(ii)(I) amount. Further conditions: the child is
  under age 19, or under age 24 and a full-time student. The child's income comes only from
  interest and dividends, which includes capital gain distributions and Alaska Permanent Fund
  dividends. No estimated tax was paid for the child, and no backup withholding was taken. On each
  side of the $13,500 line: below it, the parent can file Form 8814 and the child files no return.
  At or above it, the child must file a return with Form 8615.
- indexed: yes, through the § 1(g)(4)(A)(ii)(I) amount.
- why_it_matters: This limit decides whether a child's investment income can appear on the parent's
  return instead of on a separate child return.
- source: [Rev. Proc. 2025-32 § 4.02](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf);
  conditions at [IRS Topic no. 553](https://www.irs.gov/taxtopics/tc553)
- confidence: high

---

### AMT Exemption for a Child Subject to the Kiddie Tax

- id: kiddie_tax_amt_exemption
- kind: limit
- driven_by: earned income of the child
- values: the AMT exemption of the child cannot exceed the earned income of the child plus $9,750.
- shape: a ceiling, not a separate exemption. The child uses the smaller of the normal unmarried
  AMT exemption of $90,100 or this formula amount.
- indexed: yes, to C-CPI-U under § 59(j).
- why_it_matters: This ceiling limits the AMT exemption of a child who is subject to the kiddie tax.
- source: [Rev. Proc. 2025-32 § 4.11](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

---

### Estimated Tax Safe Harbors

- id: estimated_tax_safe_harbor
- kind: limit
- driven_by: current-year tax, prior-year tax, and prior-year AGI
- values: a taxpayer avoids the underpayment penalty by paying, through withholding and estimated
  payments, the smaller of:
  - 90% of the tax shown on the 2026 return, or
  - 100% of the tax shown on the 2025 return, if that return covered all 12 months.

  If AGI on the 2025 return was more than $150,000, the 100% figure becomes 110%. For a taxpayer
  whose 2026 filing status is Married Filing Separately, that AGI trigger is $75,000.
  If at least two thirds of gross income for 2025 or 2026 came from farming or fishing, 90%
  becomes 66 2/3% and the 110% rule does not apply.
- shape: the prior-year test is a cliff at $150,000 of prior-year AGI ($75,000 MFS). At or below
  that AGI, the prior-year safe harbor is 100% of prior-year tax. Above it, the safe harbor rises
  to 110% of prior-year tax, applied to the whole amount and not only to the excess. Payments are
  normally due in four equal installments. The annualized income installment method can lower the
  required payment when income arrives unevenly. Form 2210 computes the penalty.
- indexed: no. The 90%, 100%, 110%, $150,000, and $75,000 amounts are written into § 6654(d)(1)
  with no inflation adjustment provision.
- why_it_matters: Meeting one safe harbor removes the underpayment penalty even when the final
  balance due is large.
- source: [Form 1040-ES (2026), General Rule and Special Rules](https://www.irs.gov/pub/irs-pdf/f1040es.pdf);
  statute at [26 U.S.C. § 6654(d)(1)(B) and (C)](https://www.law.cornell.edu/uscode/text/26/6654);
  [IRS Topic no. 306](https://www.irs.gov/taxtopics/tc306)
- confidence: high

---

### Estimated Tax De Minimis Exception

- id: estimated_tax_de_minimis
- kind: cliff
- driven_by: tax due after withholding and refundable credits
- values: $1,000.
- shape: a true cliff on the penalty, not on the tax. If the tax shown on the return, reduced by
  withholding credits under § 31, is less than $1,000, no underpayment penalty applies, whatever
  the safe harbors say. At $1,000 or more, the safe harbor tests apply. A second exception applies
  to a US citizen or resident who had zero tax liability for a full 12-month 2025 tax year.
- indexed: no. The $1,000 amount is fixed in § 6654(e)(1) and has stood since 1997.
- why_it_matters: A small balance due carries no underpayment penalty.
- source: [26 U.S.C. § 6654(e)(1)](https://www.law.cornell.edu/uscode/text/26/6654);
  [IRS Topic no. 306](https://www.irs.gov/taxtopics/tc306)
- confidence: high

---

### Capital Loss Deduction Limit Against Ordinary Income

- id: capital_loss_deduction_limit
- kind: limit
- driven_by: net capital loss for the year, and filing status
- values: $3,000 for all filing statuses except Married Filing Separately. $1,500 for Married
  Filing Separately.
- shape: an annual ceiling. Capital losses first offset capital gains without limit. Only the net
  loss that remains reaches ordinary income, and that part is capped at $3,000 ($1,500 MFS). The
  allowed amount is the lesser of $3,000 and the total net loss on Schedule D line 16. Losses on
  personal-use property, such as a home or a car, are not deductible at all.
- indexed: no. The $3,000 and $1,500 amounts are written into § 1211(b) with no inflation
  adjustment provision.
- why_it_matters: Net capital losses reduce ordinary income by no more than $3,000 per year
  ($1,500 MFS).
- source: [IRS Topic no. 409](https://www.irs.gov/taxtopics/tc409);
  statute at [26 U.S.C. § 1211(b)](https://www.law.cornell.edu/uscode/text/26/1211)
- confidence: high

---

### Capital Loss Carryforward

- id: capital_loss_carryforward
- kind: limit
- driven_by: unused net capital loss from prior years
- values: no dollar cap and no time limit on the carryforward itself. The annual $3,000 / $1,500
  ceiling applies again in each later year.
- shape: the net capital loss above the annual ceiling carries forward to later tax years until it
  is used. The loss keeps its character. A short-term loss carries forward as short-term, and a
  long-term loss carries forward as long-term. In each later year the carryforward first offsets
  capital gains of the same character, then gains of the other character, then up to $3,000
  ($1,500 MFS) of ordinary income. Individuals get no carryback. An unused carryforward ends at
  the death of the taxpayer and does not transfer to the estate or to heirs. The Capital Loss
  Carryover Worksheet in Publication 550 and in the Schedule D instructions computes the amount.
- indexed: not applicable. There is no dollar amount to index.
- why_it_matters: Unused capital losses stay available in later years instead of expiring at the
  end of the year in which they arise.
- source: [IRS Topic no. 409](https://www.irs.gov/taxtopics/tc409);
  statute at [26 U.S.C. § 1212(b)](https://www.law.cornell.edu/uscode/text/26/1212)
- confidence: high on the carryforward rule, the character rule, and the absence of a carryback.
  Medium on the "loss dies with the taxpayer" point, which comes from § 1212(b) read with the
  separate-taxpayer rule for an estate rather than from a single IRS page.

---

## Appendix: Where 2026 Differs From a 2025 Expectation

1. AMT exemption phase-out start FELL. 2025: $626,350 unmarried and $1,252,700 MFJ
   ([Rev. Proc. 2024-40 § 4.11](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf)).
   2026: $500,000 unmarried and $1,000,000 MFJ. OBBBA § 70107 reset the base and froze it for 2026.
2. AMT exemption phase-out rate DOUBLED, from 25% to 50%. The exemption now disappears over half
   the income span it used to take. Combined with item 1, the point at which the exemption reaches
   zero fell sharply: MFJ from $1,800,700 in 2025 to $1,280,400 in 2026, and unmarried from
   $978,750 to $680,200.
3. The 10% and 12% bracket edges rose about 4%, while the higher edges rose about 2.3%. OBBBA
   § 70101(b) gave the bottom two bands one extra year of inflation adjustment.
4. Nothing sunsets after 2025. The rates, the brackets, the higher standard deduction, and the AMT
   exemption are all permanent now. Pre-OBBBA projections that showed a 2026 return to 15%, 28%,
   31%, 36%, and 39.6% rates, a roughly $8,300 single standard deduction, and a restored personal
   exemption are all void.
5. The $6,000 senior deduction is available for 2026, and it is separate from and additional to
   the $1,650 / $2,050 aged or blind standard deduction addition.
6. Unchanged for 2026, and often mistaken for indexed items: NIIT thresholds, Additional Medicare
   Tax thresholds, the $3,000 capital loss limit, the $150,000 estimated tax AGI trigger, and the
   $1,000 estimated tax de minimis amount. None of these five are indexed.
