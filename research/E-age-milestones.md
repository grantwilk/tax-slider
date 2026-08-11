# E — Age-Driven US Federal Tax and Benefit Thresholds (Tax Year 2026)

Compiled 2026-08-11. Primary sources preferred: IRS.gov, IRS Notice 2025-67, Rev. Proc. 2025-32, Rev. Proc. 2025-19, SSA.gov, Medicare.gov, CMS.gov.

---

### Age-50 retirement catch-up contributions
- id: age_50_retirement_catchup
- age: 50 — calendar-year rule: you may make catch-up contributions for a year if you are age 50 or over at the end of that calendar year (you need not have turned 50 on the contribution date)
- kind: limit
- driven_by: age (calendar year of turning 50); plan type
- values: 2026 catch-up limits — most 401(k)/403(b)/governmental 457(b)/TSP: $8,000 (on top of $24,500 elective deferral); SIMPLE IRA/SIMPLE 401(k): $4,000 (on top of $17,000); traditional/Roth IRA: $1,100 (on top of $7,500). Beginning 2026, if prior-year FICA wages from the plan sponsor exceeded $150,000, catch-up contributions to applicable employer plans (other than SIMPLE/SEP) must be designated Roth.
- shape: flat annual dollar limits by plan type; replaces (does not stack with) the ages-60–63 higher catch-up when that window applies
- indexed: yes (employer-plan and IRA catch-ups adjusted under Notice 2025-67 / SECURE 2.0 COLA rules)
- why_it_matters: Elective deferral capacity rises by the catch-up amount in any year you are 50 or older on December 31.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [IRS Catch-up contributions topic page](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-catch-up-contributions)
- confidence: high

### Age-55 HSA catch-up contribution
- id: age_55_hsa_catchup
- age: 55 — calendar-year / tax-year-end rule: additional HSA contribution applies if you are age 55 or older at the end of your tax year (Pub. 969); full $1,000 is available for that year even if the birthday is late in the year
- kind: limit
- driven_by: age; HSA eligibility (HDHP coverage, not enrolled in Medicare, not claimed as a dependent)
- values: +$1,000 catch-up (statutory, not COLA-adjusted). 2026 base HSA limits: self-only $4,400; family $8,750 (Rev. Proc. 2025-19). Combined with catch-up: self-only $5,400; family $9,750 (one catch-up per person; each spouse 55+ must use their own HSA for their catch-up).
- shape: flat add-on to the annual §223 limit; contribution limit becomes zero for any month enrolled in Medicare (including retroactive months)
- indexed: no (catch-up fixed at $1,000); base HSA limits are indexed
- why_it_matters: HSA contribution capacity rises by $1,000 in every tax year you are 55 or older at year-end and still HSA-eligible.
- source: [IRS Pub. 969 (2025)](https://www.irs.gov/publications/p969); [Rev. Proc. 2025-19](https://www.irs.gov/pub/irs-drop/rp-25-19.pdf)
- confidence: high — Pub. 969 examples use 2025 base limits; 2026 bases confirmed in Rev. Proc. 2025-19

### Rule of 55 (employer-plan early withdrawal exception)
- id: rule_of_55
- age: 55 — calendar-year separation rule: exception applies when the distribution is made after separation from service with the employer maintaining the plan, and separation occurs in or after the calendar year in which you attain age 55 (IRC §72(t)(2)(A)(v)); public-safety employees have a parallel age-50 rule under §72(t)(10)
- kind: milestone
- driven_by: age at calendar year of separation; separation from that employer; account must remain in that employer’s qualified plan (not an IRA)
- values: waives the 10% additional tax on early distributions from that plan; ordinary income tax still applies
- shape: binary exception — does not apply to IRAs, SEP/SIMPLE IRAs, or plans of prior employers; rolling the balance to an IRA removes the exception for those dollars
- indexed: no
- why_it_matters: Leaving a job in the year you turn 55 (or later) can remove the 10% early-distribution tax from that employer’s plan distributions before age 59½.
- source: [IRC §72(t)(2)(A)(v)](https://www.law.cornell.edu/uscode/text/26/72) (statute text); IRS Form 5329 instructions (early-distribution exceptions)
- confidence: high on calendar-year rule and plan-only scope; medium on plan-document availability (plans may restrict distribution forms even when the Code waives the penalty)

### Age 59½ — end of 10% early-withdrawal additional tax
- id: age_59_half_early_withdrawal_penalty_ends
- age: 59½ — exact half-year (day-count) rule: the 10% additional tax under §72(t) stops applying to distributions made on or after the date you reach age 59 years and 6 months (six months after the 59th birthday). Being “in the year you turn 59½” is not enough; the distribution date must be on or after that calendar date.
- kind: milestone
- driven_by: age on the distribution date
- values: 10% additional tax no longer applies; ordinary income tax on pre-tax amounts still applies. SIMPLE IRA 25% two-year participation penalty is separate and can still apply after 59½ if the two-year period is unfinished.
- shape: cliff on the exact attainment date (not a phase-out)
- indexed: no
- why_it_matters: The statutory early-distribution additional tax ends on the day you turn 59½ for distributions from IRAs and most retirement plans.
- source: [IRS Instructions for Form 5329](https://www.irs.gov/instructions/i5329); [IRS Pub. 590-B](https://www.irs.gov/publications/p590b)
- confidence: high

### Ages 60–63 SECURE 2.0 higher (“super”) catch-up; age 64 reversion
- id: secure_2_super_catchup_60_to_63
- age: 60, 61, 62, or 63 — calendar-year attainment rule: higher catch-up applies for individuals who attain age 60, 61, 62, or 63 in the calendar year (Notice 2025-67 / IRS catch-up page). At age 64 (the year you attain 64 and are no longer in the 60–63 set), the higher limit ends and the ordinary age-50+ catch-up applies again.
- kind: limit
- driven_by: age attained in the calendar year; plan type
- values: 2026 higher catch-up — most 401(k)/403(b)/gov. 457/TSP: $11,250 instead of $8,000; SIMPLE plans: $5,250 instead of $4,000. These replace, not add to, the standard age-50 catch-up for that year.
- shape: window limited to the four calendar years of attaining 60–63; then reverts to standard catch-up while still age 50+
- indexed: yes (higher limit is the greater of $10,000 or 150% of the standard catch-up, then COLA-adjusted; for 2026 the non-SIMPLE amount remains $11,250)
- why_it_matters: Catch-up capacity is larger only in the years you turn 60, 61, 62, or 63, then drops back to the ordinary age-50 catch-up at 64.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [IRS Catch-up contributions](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-catch-up-contributions)
- confidence: high

### Age 62 — earliest Social Security retirement benefit
- id: ss_earliest_claim_age_62
- age: 62 — earliest month of entitlement for retired-worker benefits; SSA treats a birthday on the 1st of a month as if it were in the prior month for benefit-month figuring
- kind: milestone
- driven_by: age; claiming month relative to Full Retirement Age (FRA)
- values: Permanent reduction from Primary Insurance Amount (PIA). For FRA 67 (born 1960 or later): claiming at 62 pays 70.0% of PIA (30% permanent reduction); spouse’s benefit at 62 is 32.5% of the worker’s PIA (vs 50% at FRA). For FRA 66 years 10 months (born 1959): claiming at 62 pays 70.8% of PIA.
- shape: permanent percentage reduction that lessens for each month of delay until FRA; reduction is not recovered later by “catching up”
- indexed: benefit dollars are COLA-adjusted after entitlement; the early-claim percentage schedule is fixed by statute for each birth cohort
- why_it_matters: Age 62 is the first month a worker can receive retirement benefits, at a permanently lower monthly rate than waiting until FRA.
- source: [SSA Born in 1960 or later](https://www.ssa.gov/benefits/retirement/planner/1960.html); [SSA Born in 1959](https://www.ssa.gov/benefits/retirement/planner/1959.html); [SSA Publication EN-05-10035](https://www.ssa.gov/pubs/EN-05-10035.pdf)
- confidence: high

### Age 65 — Medicare eligibility, Initial Enrollment Period, late-enrollment penalties
- id: medicare_age_65_enrollment
- age: 65 — Initial Enrollment Period (IEP) is 7 months: the 3 months before the month you turn 65, the birthday month, and the 3 months after. Premium-free Part A generally starts the month you turn 65 (or the prior month if birthday is on the 1st). Part B (and premium Part A) start: month you turn 65 if you enroll before that month; otherwise the month after you enroll during IEP.
- kind: milestone
- driven_by: age 65; employment-based coverage can open an 8-month Special Enrollment Period after job/coverage ends
- values: Part B late enrollment penalty — extra 10% of the standard Part B premium for each full 12-month period you could have enrolled but did not (lifetime while on Part B). Example at 2026 standard $202.90: two full years → 20% → about $243.50/month including penalty. Premium Part A late penalty — 10% higher premium for twice the number of years you delayed. Part D — generally 1% of the national base beneficiary premium ($38.99 in 2026) per month without creditable coverage (lifetime while on Part D).
- shape: enrollment window cliff after IEP; penalties are percentage add-ons that persist (Part A premium penalty is time-limited to 2× years delayed)
- indexed: penalty dollars move with annual premium amounts; percentage rules are fixed
- why_it_matters: Turning 65 opens Medicare enrollment, and missing the IEP without qualifying coverage can raise Part B (and sometimes Part A/D) premiums for years.
- source: [Medicare.gov — When coverage starts](https://www.medicare.gov/basics/get-started-with-medicare/sign-up/when-does-medicare-coverage-start); [Medicare.gov — Avoid late enrollment penalties](https://www.medicare.gov/basics/costs/medicare-costs/avoid-penalties)
- confidence: high

### Age 65 — additional standard deduction for the aged (IRC §63(f))
- id: additional_standard_deduction_age_65
- age: 65 — day-before birthday rule: you are considered age 65 on the day before your 65th birthday, so a January 1 birthday counts as age 65 for the prior tax year (for 2026: born before January 2, 1962)
- kind: limit
- driven_by: age (and/or blindness); available only when taking the standard deduction (not when itemizing)
- values: Tax year 2026 additional amount under §63(f): $1,650 per qualifying condition (aged or blind) for married individuals; $2,050 if the individual is unmarried and not a surviving spouse. Both age and blindness can each add one amount. Stacks with the basic 2026 standard deduction ($16,100 single / $32,200 MFJ / $24,150 HoH per Rev. Proc. 2025-32).
- shape: flat add-on; no income phase-out
- indexed: yes (COLA under §63(c)(4) / Rev. Proc. 2025-32)
- why_it_matters: Standard-deduction filers who are 65 or older (or treated as 65 under the day-before rule) get a larger standard deduction.
- source: [Rev. Proc. 2025-32 §2.14(3)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [IRS Topic 551](https://www.irs.gov/taxtopics/tc551); [IRS Pub. 501](https://www.irs.gov/publications/p501)
- confidence: high

### Age 65 — OBBBA / enhanced senior deduction (separate from §63(f))
- id: obbba_enhanced_senior_deduction
- age: 65 — year-end / day-before rule: eligible if age 65 or older at year-end; Pub. 554 treats you as 65 at year-end if your 65th birthday is on or before January 1 of the following year (same day-before convention as the additional standard deduction)
- kind: phase_out
- driven_by: age; MAGI; filing status (married persons must file jointly); valid SSN; available whether itemizing or taking the standard deduction
- values: Up to $6,000 per qualifying individual ($12,000 if MFJ and both spouses qualify) for tax years 2025–2028. Phase-out: reduced by 6% of MAGI above $75,000 (unmarried) or $150,000 (MFJ). Fully phased out at $175,000 MAGI (one qualifying person) or $250,000 MAGI (MFJ with $6,000 base); MFJ with two qualifiers phases out over a $200,000 band from $150,000.
- shape: phase-out — start $75,000 / $150,000 MAGI; rate 6% of excess MAGI; end $175,000 / $250,000 for a $6,000 base (or $350,000 for a $12,000 base). Not a cliff.
- indexed: no (fixed statutory dollar amounts and thresholds for 2025–2028)
- why_it_matters: A temporary extra deduction of up to $6,000 per senior (separate from the §63(f) aged add-on) reduces taxable income for eligible filers age 65+.
- source: [IRS Tax Tip 2026-14 — 2026 filing season updates for seniors](https://www.irs.gov/newsroom/2026-filing-season-updates-and-resources-for-seniors); [IRS Pub. 554 (2025)](https://www.irs.gov/pub/irs-pdf/p554.pdf); [CRS RL34498](https://www.congress.gov/crs-product/RL34498) (6% phase-out formula and 2026 table)
- confidence: high on amount, age test, and start thresholds from IRS; high on 6% rate via CRS / IRC §151(d)(5)(C) descriptions — IRS tip states phase-out begins over $75k/$150k but does not reprint the 6% formula on that page

### Age 65 — HSA: contributions stop when enrolled in Medicare; 20% non-medical penalty ends
- id: age_65_hsa_medicare_and_penalty
- age: (a) Contributions: eligibility ends beginning with the first month enrolled in Medicare (any Part), including retroactive Part A months (can reach back up to 6 months). (b) 20% additional tax: ends on distributions made after the date you reach age 65 (even if not yet on Medicare); income tax still applies to non-qualified withdrawals.
- kind: milestone
- driven_by: Medicare enrollment month for contributions; chronological age 65 for the 20% penalty end
- values: Contribution limit = $0 in Medicare months. Non-medical HSA distributions before 65: income tax + 20% additional tax. On/after age 65: income tax only on non-qualified amounts; qualified medical expenses remain tax-free at any age.
- shape: hard stop on contributions at Medicare enrollment; penalty cliff at exact age-65 attainment date
- indexed: no (penalty rate and Medicare-disqualification rule are statutory)
- why_it_matters: Medicare enrollment bars new HSA contributions, while turning 65 removes the 20% extra tax on non-medical HSA withdrawals.
- source: [IRS Pub. 969 (2025)](https://www.irs.gov/publications/p969) (Enrolled in Medicare; Additional 20% tax exceptions)
- confidence: high

### Full Retirement Age (FRA) in 2026 and delayed retirement credits to age 70
- id: ss_full_retirement_age_and_delayed_credits
- age: People reaching FRA during calendar 2026 are primarily the 1959 birth cohort (FRA = 66 years and 10 months). Born 1960 or later: FRA = 67 (those people reach FRA in 2027+). SSA January 1 birthday rule: use the prior year of birth for FRA. Delayed retirement credits accrue from FRA until age 70 at ⅔ of 1% per month (8% per full year) for workers born 1943 or later; credits stop increasing at age 70.
- kind: milestone
- driven_by: year of birth; claiming age relative to FRA and 70
- values: At FRA: 100% of PIA. Born 1960+: delay to 70 → 124% of PIA (36 months × ⅔%). Born 1959: FRA 66y10m; delay to 70 yields about 125.3% of PIA. No earnings-test withholding beginning with the month of FRA.
- shape: step schedule by birth year for FRA; linear monthly delayed credits until age 70 cliff
- indexed: benefit dollars COLA-adjusted; credit rate schedule is fixed by birth cohort
- why_it_matters: FRA is the age of an unreduced retired-worker benefit, and delaying past FRA raises the monthly benefit until age 70.
- source: [SSA age-increase chart](https://www.ssa.gov/benefits/retirement/planner/ageincrease.html); [SSA delayed retirement — 1960+](https://www.ssa.gov/benefits/retirement/planner/1960-delay.html); [SSA EN-05-10035](https://www.ssa.gov/pubs/EN-05-10035.pdf)
- confidence: high

### Age 70½ — Qualified Charitable Distributions (QCDs)
- id: qcd_age_70_half
- age: 70½ — must be age 70½ or older on the date the distribution is made (QCD age did not move when RMD ages rose)
- kind: limit
- driven_by: age on distribution date; direct trustee-to-charity transfer from IRA
- values: 2026 annual QCD exclusion limit $111,000 per IRA owner (Notice 2025-67). One-time split-interest entity QCD election limit $55,000 for 2026. Spouses each have their own $111,000 limit from their own IRAs.
- shape: annual per-person cap; amounts excluded from gross income and can satisfy RMDs when rules are met
- indexed: yes (SECURE 2.0 §307 indexed the former $100,000 cap)
- why_it_matters: From age 70½, IRA owners can send up to the annual QCD limit directly to charity excluded from income.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [IRB 2025-49](https://www.irs.gov/irb/2025-49_IRB); CRS IF11377
- confidence: high

### Age 73 — Required Minimum Distributions (SECURE 2.0 current age)
- id: rmd_age_73
- age: 73 — first distribution year is the calendar year you attain age 73 (for individuals who attain age 72 after Dec 31, 2022, and age 73 before Jan 1, 2033 — generally birth years 1951–1959)
- kind: milestone
- driven_by: age; for workplace plans (non–5% owners), plan may allow delay until retirement
- values: First RMD due by April 1 of the year after the year you turn 73; all later RMDs due by December 31 each year. Delaying the first RMD to April 1 means two RMDs in that following calendar year. Excise tax for shortfall: 25% of the amount not distributed; reduced to 10% if corrected in a timely manner within the statutory correction window (generally 2 years). Roth IRAs (and designated Roth accounts during the owner’s life, post-SECURE 2.0) have no lifetime owner RMDs.
- shape: age cliff for the required beginning year; April 1 first-year deadline exception; then annual Dec 31 deadlines
- indexed: no (age and penalty rates are statutory); RMD dollar amounts use IRS life-expectancy tables and prior-year account balances
- why_it_matters: Owners subject to the age-73 rule must begin taxable minimum withdrawals, with a 25% (or 10% if timely corrected) excise tax on shortfalls.
- source: [IRS RMD topic page](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-required-minimum-distributions-rmds); [IRS RMD FAQs](https://www.irs.gov/retirement-plans/retirement-plan-and-ira-required-minimum-distributions-faqs); IRC §401(a)(9)(C)(v)
- confidence: high

### Age 75 — RMD age for people born in 1960 or later
- id: rmd_age_75_born_1960_or_later
- age: 75 — applies to individuals who attain age 74 after December 31, 2032, which the IRS/CRS map to persons born on or after January 1, 1960. First RMDs for this cohort begin in the 2030s (not in tax year 2026).
- kind: milestone
- driven_by: year of birth (applicable age under §401(a)(9)(C)(v)(II))
- values: Same first-year April 1 / subsequent Dec 31 deadline structure and 25%/10% excise-tax framework as age-73 RMDs, but the applicable age is 75. Persons born in 1959 are treated as age-73 under IRS proposed/final regulation clarification of the statutory gap.
- shape: birth-year cliff between age-73 and age-75 cohorts
- indexed: no
- why_it_matters: People born in 1960 or later start lifetime RMDs at 75 rather than 73.
- source: IRC §401(a)(9)(C)(v) as amended by SECURE 2.0 §107; [CRS IF12750](https://www.congress.gov/crs_external_products/IF/PDF/IF12750/IF12750.2.pdf); Federal Register final RMD regs (89 FR 58886)
- confidence: high for “born 1960 or later → 75”; note 1959 statutory ambiguity was reserved/clarified toward age 73 in IRS regs

### Social Security benefit taxation — provisional income thresholds
- id: ss_benefit_taxation_provisional_income
- age: no age gate (applies whenever benefits are received); listed here because it is a core retiree tax interaction on the age axis
- kind: cliff
- driven_by: filing status; provisional income ≈ AGI (with SS excluded) + tax-exempt interest + 50% of Social Security benefits
- values: |
    | Filing status | 0% taxable | Up to 50% taxable | Up to 85% taxable |
    | Single / HoH / QSS | ≤ $25,000 | > $25,000 to ≤ $34,000 | > $34,000 |
    | Married filing jointly | ≤ $32,000 | > $32,000 to ≤ $44,000 | > $44,000 |
    | Married filing separately (lived with spouse) | — | — | base amount $0 (up to 85%) |
- shape: two-tier inclusion cliffs (base amount and adjusted base amount); maximum inclusion is 85% of benefits
- indexed: no — thresholds fixed since 1983/1993 (26 U.S.C. §86)
- why_it_matters: Provisional income above fixed statutory amounts causes up to 50% or 85% of Social Security benefits to be included in taxable income.
- source: [26 U.S.C. §86](https://www.law.cornell.edu/uscode/text/26/86); [SSA research IP 2015-02](https://www.ssa.gov/policy/docs/issuepapers/ip2015-02.html); [CRS IF11397](https://www.congress.gov/crs_external_products/IF/PDF/IF11397/IF11397.4.pdf)
- confidence: high

### Social Security earnings test (before FRA) — 2026 limits
- id: ss_earnings_test_2026
- age: applies only before the month you reach FRA; higher limit in the calendar year you reach FRA for months before FRA; no limit beginning with the FRA month
- kind: limit
- driven_by: age vs FRA; earned income (wages/self-employment)
- values: 2026 — under FRA all year: $24,480 annual exempt amount; withhold $1 of benefits for every $2 of earnings above the limit. Year of FRA: $65,160 exempt on earnings before the FRA month; withhold $1 for every $3 above that limit. From FRA month onward: no earnings test.
- shape: two annual exempt amounts with different withholding ratios; ends at FRA
- indexed: yes (national average wage index; SSA COLA fact sheet)
- why_it_matters: Working while receiving benefits before FRA can cause SSA to withhold benefits when earnings exceed the annual exempt amount.
- source: [SSA 2026 COLA Fact Sheet](https://www.ssa.gov/news/en/cola/factsheets/2026.html); [SSA While Working planner](https://www.ssa.gov/benefits/retirement/planner/whileworking.html); [SSA Pub. EN-05-10069](https://www.ssa.gov/pubs/EN-05-10069.pdf)
- confidence: high

### Medicare IRMAA 2026 — Part B and Part D brackets
- id: medicare_irmaa_2026
- age: applies to Medicare enrollees with MAGI above the threshold (typically age 65+, or disabled under 65)
- kind: cliff
- driven_by: MAGI from tax year two years prior (2026 premiums use 2024 MAGI = AGI + tax-exempt interest); filing status
- values: |
    Standard Part B premium 2026: $202.90/month.
    | 2024 MAGI (individual) | 2024 MAGI (joint) | Part B IRMAA | Total Part B | Part D IRMAA |
    | ≤ $109,000 | ≤ $218,000 | $0 | $202.90 | $0 |
    | > $109,000–$137,000 | > $218,000–$274,000 | $81.20 | $284.10 | $14.50 |
    | > $137,000–$171,000 | > $274,000–$342,000 | $202.90 | $405.80 | $37.50 |
    | > $171,000–$205,000 | > $342,000–$410,000 | $324.60 | $527.50 | $60.40 |
    | > $205,000–< $500,000 | > $410,000–< $750,000 | $446.30 | $649.20 | $83.30 |
    | ≥ $500,000 | ≥ $750,000 | $487.00 | $689.90 | $91.00 |
    Married filing separately (lived with spouse): ≤ $109,000 → $0; > $109,000–< $391,000 → Part B IRMAA $446.30 / Part D $83.30; ≥ $391,000 → Part B $487.00 / Part D $91.00.
- shape: hard cliffs at each MAGI threshold (one dollar over jumps the full surcharge for the year); not a smooth phase-out
- indexed: yes (income thresholds and surcharges adjusted annually; top bracket inflation-adjusted under current law)
- why_it_matters: MAGI two years earlier can raise monthly Part B and Part D premiums by fixed IRMAA surcharges at each income cliff.
- source: [CMS 2026 Parts A & B Premiums fact sheet](https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles); [SSA POMS HI 01101.010](https://secure.ssa.gov/apps10/poms.nsf/lnx/0601101010)
- confidence: high

### Medicare Part B standard premium 2026 and Part A / Part B payroll tax rates
- id: medicare_part_b_premium_and_payroll_taxes
- age: Part B premium applies to Part B enrollees (generally from 65); payroll taxes apply to earned income at any age
- kind: rate
- driven_by: enrollment (premium); earned income (payroll tax); additional 0.9% HI tax above wage thresholds
- values: 2026 standard monthly Part B premium $202.90; Part B annual deductible $283. Employee OASDI 6.2% (to wage base $184,500 in 2026) + employee HI (Medicare) 1.45% on all wages = 7.65% combined employee rate; self-employed 15.30%. Additional 0.9% Medicare HI tax on earned income above $200,000 single / $250,000 MFJ (unchanged; not indexed). Employer also pays 6.2% OASDI + 1.45% HI.
- shape: flat premium for non-IRMAA enrollees; flat payroll rates with an uncapped HI base and a high-earner add-on cliff
- indexed: Part B premium set annually by CMS; OASDI wage base indexed; HI additional-tax thresholds not indexed
- why_it_matters: Part B has a stated 2026 standard premium, and Medicare Hospital Insurance is funded by a 1.45% (plus possible 0.9%) payroll tax on earnings.
- source: [CMS 2026 Parts A & B Premiums fact sheet](https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles); [SSA 2026 COLA Fact Sheet](https://www.ssa.gov/news/en/cola/factsheets/2026.html)
- confidence: high
