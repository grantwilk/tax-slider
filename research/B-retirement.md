# Leg B — US Federal Retirement and Tax-Advantaged Savings Limits, Tax Year 2026

Scope: federal retirement and tax-advantaged savings parameters only. All figures are
tax year 2026. Primary sources are IRS Notice 2025-67 (retirement plans), IRS
Rev. Proc. 2025-19 (HSA/HDHP), IRS Rev. Proc. 2025-32 (cafeteria plans), the Internal
Revenue Code, and Treasury Decision 10033 (catch-up final regulations).

Two 2026 changes are not inflation adjustments and come from separate statutes:
the SECURE 2.0 Section 603 mandatory Roth catch-up (first effective year is 2026) and
the dependent care FSA increase from the One Big Beautiful Bill Act.

---

## 1. Workplace plan deferrals and catch-ups

### Elective deferral limit (401(k), 403(b), governmental 457(b), federal TSP)
- id: elective_deferral_limit_402g
- kind: limit
- driven_by: none (flat dollar cap per person, aggregated across all employers)
- values: $24,500 for 2026. Increased from $23,500 for 2025.
- shape: flat cap. The cap applies per person across all plans, not per plan. Governmental 457(b) plans have a separate $24,500 limit under section 457(e)(15) that does not aggregate with the 402(g) limit for 401(k)/403(b) plans.
- indexed: yes — section 415(d) cost-of-living method
- why_it_matters: This is the maximum an employee can defer from salary into a 401(k), 403(b), governmental 457(b), or the TSP in 2026 before catch-up contributions.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — "2026 Amounts Relating to Retirement Plans and IRAs, as Adjusted for Changes in Cost-of-Living"
- confidence: high

### Age 50 catch-up contribution
- id: catch_up_age_50
- kind: limit
- driven_by: age (attained by the end of the calendar year)
- values: $8,000 for 2026. Increased from $7,500 for 2025. Combined with the 402(g) limit, a participant aged 50 or older can defer up to $32,500.
- shape: age rule — available to a participant who attains age 50 by the end of the taxable year. Statutory definition of "eligible participant" is a participant "who would attain age 50 by the end of the taxable year" under section 414(v)(5)(A). A person who turns 50 on December 31, 2026 qualifies for the full 2026 amount.
- indexed: yes — section 414(v)(2)(C)
- why_it_matters: A participant aged 50 or older may defer this amount above the 402(g) limit if the plan permits catch-up contributions.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — limitation under section 414(v)(2)(B)(i)
- confidence: high

### SECURE 2.0 super catch-up, ages 60 through 63
- id: super_catch_up_age_60_63
- kind: limit
- driven_by: age (attained during the calendar year)
- values: $11,250 for 2026. This amount is unchanged from 2025. It replaces the $8,000 age 50 catch-up rather than adding to it. Combined with the 402(g) limit, a participant aged 60 to 63 can defer up to $35,750.
- shape: age band rule. The statute at section 414(v)(2)(B)(i) grants the higher amount to "an eligible participant who would attain age 60 but would not attain age 64 before the close of the taxable year." Applied to 2026, the participant must reach age 60, 61, 62, or 63 at some point during calendar year 2026. In the calendar year the participant reaches age 64, the amount reverts to the standard $8,000 age 50 catch-up. Eligibility keys off the age reached during the year, not the age on January 1 or on the contribution date.
- indexed: yes — SECURE 2.0 section 109(c) directs annual adjustment for years beginning after December 31, 2025, with a base period of the calendar quarter beginning July 1, 2024. The computed 2026 amount stayed at $11,250.
- why_it_matters: A participant who reaches age 60, 61, 62, or 63 during 2026 may make this larger catch-up instead of the $8,000 amount if the plan offers it.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — limitation under section 414(v)(2)(E)(i); [26 U.S.C. 414(v)(2)(B)(i)](https://www.law.cornell.edu/uscode/text/26/414)
- confidence: high — one caveat: the super catch-up is optional for plans. A plan is not required to offer it. Confirm the plan document permits it.

### Combined deferral ceilings by age band
- id: combined_deferral_ceiling_by_age
- kind: limit
- driven_by: age
- values: Under 50 — $24,500 employee deferral, $72,000 total annual additions. Ages 50 through 59 — $32,500 employee deferral, $80,000 total. Ages 60 through 63 — $35,750 employee deferral, $83,250 total. Age 64 and older — $32,500 employee deferral, $80,000 total.
- shape: four age bands with a non-monotonic pattern. The ceiling rises at age 50, rises again at age 60, then falls back at age 64.
- indexed: yes — all component amounts are indexed
- why_it_matters: These are the total 2026 amounts that can flow into a workplace defined contribution plan account for one person at each age band.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [IRS: Retirement topics — 401(k) and profit-sharing plan contribution limits](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-401k-and-profit-sharing-plan-contribution-limits)
- confidence: high

---

## 2. SECURE 2.0 Section 603 mandatory Roth catch-up

### Mandatory Roth catch-up wage threshold
- id: roth_catch_up_wage_threshold
- kind: cliff
- driven_by: prior-year FICA wages from the employer that sponsors the plan
- values: $150,000. For 2026 the test is whether the participant's calendar year 2025 FICA wages from the plan-sponsoring employer exceeded $150,000. Notice 2025-67 states this explicitly: "The Roth catch-up wage threshold for 2025, which under section 414(v)(7)(A) is used to determine whether an individual's catch-up contributions to an applicable employer plan (other than a plan described in section 408(k) or (p)) for 2026 must be designated as Roth contributions, is increased from $145,000 to $150,000."
- shape: hard cliff, not a phase-out. Wages of exactly $150,000 do not trigger it, because the statute requires wages that "exceed" the threshold. At $150,000.01 the participant must make all catch-up contributions as designated Roth contributions. The measured amount is FICA wages under section 3121(a) for the taxes imposed by sections 3101(a) and 3111(a), which is the Social Security wages figure in Box 3 of Form W-2. It is not adjusted gross income, not total compensation, and not Medicare wages from Box 5. Wages are counted from the participant's common law employer only. Wages are not annualized if the participant worked only part of the prior year. A plan may optionally aggregate wages across a common paymaster, across controlled group members, or across a predecessor and successor employer in the year of an asset purchase, but aggregation is a plan election, not a requirement. Aggregation across disregarded entities and their owners is required.
- indexed: yes — section 414(v)(7)(E) directs annual adjustment using the section 415(d) method with a base period of the calendar quarter beginning July 1, 2023, and rounding down to the next lower multiple of $5,000. The statutory starting figure is $145,000; $150,000 is the indexed 2025 figure that governs 2026 contributions.
- why_it_matters: A participant aged 50 or older who exceeded this prior-year wage figure at the plan-sponsoring employer cannot make pre-tax catch-up contributions in 2026 and must make them as designated Roth contributions.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [26 U.S.C. 414(v)(7)](https://www.law.cornell.edu/uscode/text/26/414); [26 CFR 1.414(v)-2](https://www.govinfo.gov/content/pkg/FR-2025-09-16/pdf/2025-17865.pdf) (Treasury Decision 10033, 90 FR 44527, September 16, 2025)
- confidence: high

### Mandatory Roth catch-up — effective date and 2026 transition
- id: roth_catch_up_effective_date
- kind: rule
- driven_by: tax year
- values: The statutory requirement applies to taxable years beginning on or after January 1, 2026. The transition relief in Notice 2023-62, which allowed pre-tax catch-ups for 2024 and 2025, ended December 31, 2025 and was not extended. The final regulations themselves generally apply to contributions in taxable years beginning after December 31, 2026. For 2026 only, plans may implement the requirement under a reasonable, good-faith interpretation of the statute. Certain governmental plans and collectively bargained plans have a later applicability date.
- shape: 2026 is the first year the mandate binds and is also a good-faith compliance year. It is not a non-enforcement year.
- indexed: not applicable
- why_it_matters: 2026 is the first tax year in which affected participants must direct catch-up contributions to Roth, though plan administration in 2026 is judged under a good-faith standard.
- source: [IRS IR-2025-91, Treasury, IRS issue final regulations on new Roth catch-up rule](https://www.irs.gov/newsroom/treasury-irs-issue-final-regulations-on-new-roth-catch-up-rule-other-secure-20-act-provisions); [Treasury Decision 10033](https://www.govinfo.gov/content/pkg/FR-2025-09-16/pdf/2025-17865.pdf)
- confidence: high

### Mandatory Roth catch-up — new employer, no prior-year wages
- id: roth_catch_up_new_employer
- kind: rule
- driven_by: prior-year FICA wages from the specific plan-sponsoring employer
- values: A participant who had no FICA wages from the plan-sponsoring employer in the preceding calendar year is not subject to the Roth catch-up requirement for the current year. A person who started with a new employer in 2026 had zero 2025 FICA wages from that employer, so the requirement does not apply to that person in 2026 at that employer, no matter how high 2026 pay is. The requirement can first apply in 2027, based on 2026 wages. Prior-year wages from a former employer do not carry over to the new employer's plan.
- shape: rule with a per-employer test. Where one plan has more than one unaggregated sponsoring employer, wages from each employer are tested separately, and deferrals from one employer's compensation are subject to the Roth requirement only if that same employer's prior-year wages exceeded the threshold.
- indexed: not applicable
- why_it_matters: Changing employers resets the prior-year wage test to zero at the new employer, so a high earner who changed jobs may make pre-tax catch-up contributions in the first calendar year at the new employer.
- source: [Treasury Decision 10033, 26 CFR 1.414(v)-2(a)(2) and (b)(5)](https://www.govinfo.gov/content/pkg/FR-2025-09-16/pdf/2025-17865.pdf); [Internal Revenue Bulletin 2025-40](https://www.irs.gov/irb/2025-40_IRB)
- confidence: high

### Mandatory Roth catch-up — plan with no Roth option
- id: roth_catch_up_no_roth_program
- kind: rule
- driven_by: plan design plus prior-year FICA wages
- values: If the plan does not include a qualified Roth contribution program under section 402A(b), then for a catch-up eligible participant who is subject to the Roth catch-up requirement the maximum catch-up contribution permitted is $0. The participant is not allowed to make any catch-up contribution at all, in Roth form or pre-tax form. Such a plan does not fail the universal availability requirement solely for that reason. Separately, if the plan does permit any affected participant to make Roth catch-up contributions, it must permit all catch-up eligible participants to do so. A plan may not require participants below the wage threshold to use Roth for catch-ups.
- shape: binary rule. Affected participant plus no Roth program equals no catch-up capacity, capped at $0.
- indexed: not applicable
- why_it_matters: A high earner in a plan without a Roth feature loses the ability to make catch-up contributions to that plan in 2026 and is limited to the $24,500 elective deferral amount.
- source: [Treasury Decision 10033, 26 CFR 1.414(v)-2(a)(5) and (b)(2)](https://www.govinfo.gov/content/pkg/FR-2025-09-16/pdf/2025-17865.pdf); [26 U.S.C. 414(v)(7)(B)](https://www.law.cornell.edu/uscode/text/26/414)
- confidence: high

### Mandatory Roth catch-up — persons with no FICA wages
- id: roth_catch_up_no_fica_wages
- kind: rule
- driven_by: character of prior-year compensation
- values: A participant who had no FICA wages from the plan-sponsoring employer in the preceding calendar year is outside the requirement. The final regulations name specific cases: a partner whose income from the firm is only self-employment income; a person whose pay is subject to the Railroad Retirement Tax Act under section 3231(e) rather than FICA; and a state or local government employee whose services are excluded from employment under section 3121(b)(7). Where a person had both FICA wages and self-employment income from the same firm in the prior year, only the FICA wages are tested. A partner who earned $156,000 in FICA wages before becoming a partner mid-year is subject to the requirement; a partner with $60,000 in FICA wages plus $155,000 of self-employment income is not.
- shape: rule based on the character of prior-year compensation, not its size.
- indexed: not applicable
- why_it_matters: Self-employment income and partnership distributive shares are not FICA wages, so they do not count toward the threshold test.
- source: [Treasury Decision 10033, 26 CFR 1.414(v)-2(a)(2) and examples at (d)(1) and (d)(2)](https://www.govinfo.gov/content/pkg/FR-2025-09-16/pdf/2025-17865.pdf)
- confidence: high

### Mandatory Roth catch-up — plans excluded
- id: roth_catch_up_excluded_plans
- kind: rule
- driven_by: plan type
- values: The requirement does not apply to a SEP under section 408(k) or a SIMPLE IRA plan under section 408(p). It applies to 401(k) plans, 403(b) plans, and governmental 457(b) plans.
- shape: plan-type exclusion under section 414(v)(7)(C), cross-referencing section 414(v)(6)(A)(iv).
- indexed: not applicable
- why_it_matters: SIMPLE IRA and SEP catch-up contributions are not affected by the mandatory Roth rule in 2026.
- source: [26 U.S.C. 414(v)(7)(C)](https://www.law.cornell.edu/uscode/text/26/414); [26 CFR 1.414(v)-2(a)(4)](https://www.govinfo.gov/content/pkg/FR-2025-09-16/pdf/2025-17865.pdf)
- confidence: high

### Mandatory Roth catch-up — de minimis and W-2 correction relief
- id: roth_catch_up_de_minimis
- kind: rule
- driven_by: size of the failure
- values: A failure does not need to be corrected if the pre-tax elective deferral that should have been Roth does not exceed $250. A failure also does not need correction if the participant became subject to the rule only because an amended Form W-2 established that prior-year wages exceeded the threshold after the correction deadline had passed.
- shape: dollar threshold of $250 plus a timing-based exception.
- indexed: no
- why_it_matters: Small mis-designations of catch-up contributions are disregarded and the contribution is still treated as a valid catch-up contribution.
- source: [Treasury Decision 10033, 26 CFR 1.414(v)-2(c)(4)](https://www.govinfo.gov/content/pkg/FR-2025-09-16/pdf/2025-17865.pdf)
- confidence: high

---

## 3. Plan-level limits

### Total annual additions limit, section 415(c)
- id: annual_additions_limit_415c
- kind: limit
- driven_by: compensation, employer contributions, age
- values: The lesser of 100% of the participant's compensation or $72,000 for 2026. Increased from $70,000 for 2025. Catch-up contributions sit outside this limit, so the practical total is $80,000 for a participant aged 50 to 59 or 64 and older, and $83,250 for a participant aged 60 to 63.
- shape: applies to the sum of elective deferrals (excluding catch-ups), employer matching contributions, employer nonelective contributions, after-tax employee contributions, and allocations of forfeitures. The limit applies per employer, so plans of genuinely unrelated employers each get their own 415(c) limit, while plans of related employers are aggregated.
- indexed: yes — section 415(d)
- why_it_matters: This caps everything that can be added to one participant's defined contribution account from all sources in a year and sets the ceiling for after-tax contributions used in a mega-backdoor Roth.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — section 415(c)(1)(A); [IRS: Retirement topics — 401(k) and profit-sharing plan contribution limits](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-401k-and-profit-sharing-plan-contribution-limits)
- confidence: high

### Annual compensation limit, section 401(a)(17)
- id: compensation_limit_401a17
- kind: limit
- driven_by: compensation
- values: $360,000 for 2026. Increased from $350,000 for 2025. A separate grandfathered limit of $535,000 applies to eligible participants in certain governmental plans that allowed cost-of-living adjustments under the plan as in effect on July 1, 1993.
- shape: caps the amount of compensation that can be counted when computing contributions and benefits. Compensation above the cap is ignored for plan purposes.
- indexed: yes — section 415(d)
- why_it_matters: Employer contributions expressed as a percentage of pay are computed only on compensation up to this amount, so a percentage match stops accruing once pay passes the cap.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — sections 401(a)(17), 404(l), 408(k)(3)(C), 408(k)(6)(D)(ii)
- confidence: high

### Highly compensated employee threshold
- id: hce_threshold
- kind: cliff
- driven_by: prior-year compensation, or ownership percentage
- values: $160,000 for 2026. Unchanged from $160,000 for 2025. A person is also a highly compensated employee, regardless of pay, if they owned more than 5% of the business at any time during the current or preceding year.
- shape: prior-year lookback. Highly compensated employee status for the 2026 plan year rests on 2025 compensation exceeding the 2025 threshold of $160,000. Because the 2025 and 2026 thresholds are both $160,000, the figure is the same either way for 2026. An employer may optionally add a top-paid group election limiting the compensation test to the top 20% of employees ranked by pay.
- indexed: yes — section 414(q)(1)(B), adjusted under section 415(d); the computed 2026 amount stayed at $160,000
- why_it_matters: Highly compensated employee status subjects a participant's deferrals to nondiscrimination testing, which can force a refund of contributions if the plan fails the test.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — section 414(q)(1)(B)
- confidence: high — note: the IRS "Retirement plans definitions" page has not been updated past a 2024 lookback figure, so Notice 2025-67 is the controlling source for 2026.

### Key employee threshold, top-heavy testing
- id: key_employee_threshold
- kind: cliff
- driven_by: prior-year compensation, ownership
- values: $235,000 for 2026. Increased from $230,000 for 2025.
- shape: officer compensation test under section 416(i)(1)(A)(i), used with separate 5% and 1% ownership tests.
- indexed: yes — section 415(d)
- why_it_matters: Key employee status is used to determine whether a plan is top-heavy and owes minimum contributions to other participants.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — section 416(i)(1)(A)(i)
- confidence: high

---

## 4. IRAs

### Traditional and Roth IRA contribution limit
- id: ira_contribution_limit
- kind: limit
- driven_by: taxable compensation, age
- values: $7,500 for 2026. Increased from $7,000 for 2025. The limit is the lesser of $7,500 or the person's taxable compensation for the year.
- shape: single aggregate cap across all traditional and Roth IRAs owned by one person. It is not $7,500 per account. Rollover contributions and qualified reservist repayments do not count against it. There is no upper age limit on contributing. Under the spousal IRA rule, a person filing jointly may contribute based on the couple's combined taxable compensation, so each spouse can reach the full limit even if only one has earnings.
- indexed: yes — section 219(b)(5)(A)
- why_it_matters: This is the total that one person can put into traditional and Roth IRAs combined for 2026 before catch-up contributions.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — section 219(b)(5)(A); [IRS: Retirement topics — IRA contribution limits](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-ira-contribution-limits)
- confidence: high

### IRA age 50 catch-up
- id: ira_catch_up_age_50
- kind: limit
- driven_by: age
- values: $1,100 for 2026. Increased from $1,000 for 2025. Total IRA contribution for a person aged 50 or older is $8,600.
- shape: age rule — the person must attain age 50 before the close of the taxable year. There is no separate super catch-up for IRAs; the ages 60 to 63 rule applies only to workplace plans.
- indexed: yes — SECURE 2.0 added cost-of-living adjustment to this amount; 2026 is the first year it moved above the long-standing $1,000
- why_it_matters: A person aged 50 or older may contribute this amount to IRAs above the standard limit.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — section 219(b)(5)(B)(ii); [IRS IR-2025-111](https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500)
- confidence: high

### Roth IRA income phase-out
- id: roth_ira_income_phase_out
- kind: phase_out
- driven_by: modified adjusted gross income, filing status
- values: Single and head of household — start $153,000, end $168,000. Married filing jointly and qualifying surviving spouse — start $242,000, end $252,000. Married filing separately — start $0, end $10,000.
- shape: linear pro-rata reduction. The allowed contribution is reduced by the full limit multiplied by (MAGI minus start) divided by the range width. Range width is $15,000 for single and head of household, $10,000 for married filing jointly, and $10,000 for married filing separately. The reduced limit is rounded up to the next $10, and if the computed result is above $0 but below $200, the allowed contribution is $200. At or above the end of the range, direct Roth IRA contribution is $0.
- indexed: yes for single, head of household, and married filing jointly. The married filing separately range of $0 to $10,000 is fixed by statute and is not adjusted.
- why_it_matters: MAGI above the end of the range removes the ability to contribute directly to a Roth IRA for 2026.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — section 408A(c)(3); [IRS IR-2025-111](https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500)
- confidence: high

### Traditional IRA deduction phase-out — person covered by a workplace plan
- id: trad_ira_deduction_phase_out_covered
- kind: phase_out
- driven_by: modified adjusted gross income, filing status, workplace plan coverage
- values: Single and head of household — start $81,000, end $91,000. Married filing jointly where the contributing spouse is the covered person — start $129,000, end $149,000. Married filing separately — start $0, end $10,000.
- shape: linear pro-rata reduction of the deduction across the range. Range width is $10,000 for single and head of household, $20,000 for married filing jointly, and $10,000 for married filing separately. The deduction is rounded to the nearest $10 and has a $200 floor if the computed amount is above $0. Above the end of the range the contribution may still be made as a nondeductible contribution reported on Form 8606.
- indexed: yes for single, head of household, and married filing jointly. The married filing separately range is fixed and is not adjusted.
- why_it_matters: A person covered by a workplace retirement plan loses part or all of the traditional IRA deduction once MAGI enters this range.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — section 219(g)(2)(A) and 219(g)(3)(B); [IRS IR-2025-111](https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500)
- confidence: high

### Traditional IRA deduction phase-out — person not covered, spouse covered
- id: trad_ira_deduction_phase_out_spouse_covered
- kind: phase_out
- driven_by: joint modified adjusted gross income, spouse's workplace plan coverage
- values: Start $242,000, end $252,000. Increased from $236,000 to $246,000 for 2025.
- shape: linear pro-rata reduction over a $10,000 range, using the couple's combined income. This applies only to a married person filing jointly who is not an active participant in a workplace plan but whose spouse is. A married person filing separately who is not covered but whose spouse is uses the fixed $0 to $10,000 range.
- indexed: yes — section 219(g)(7)(A)
- why_it_matters: A person with no workplace plan can still lose the traditional IRA deduction because of a spouse's plan coverage once joint income enters this range.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — section 219(g)(7)(A); [IRS IR-2025-111](https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500)
- confidence: high

### Traditional IRA deduction — neither person covered by a workplace plan
- id: trad_ira_deduction_not_covered
- kind: rule
- driven_by: workplace plan coverage
- values: No income phase-out applies. The full traditional IRA contribution is deductible up to $7,500, or $8,600 at age 50 or older, limited by taxable compensation.
- shape: no phase-out. The IRS states directly: "If neither the taxpayer nor the spouse is covered by a retirement plan at work, the phase-outs of the deduction do not apply."
- indexed: not applicable — the underlying contribution limit is indexed
- why_it_matters: A person with no workplace plan, and whose spouse has none either, can deduct the full traditional IRA contribution at any income level.
- source: [IRS IR-2025-111](https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500); [IRS: Retirement topics — IRA contribution limits](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-ira-contribution-limits)
- confidence: high

---

## 5. Backdoor Roth strategies

### Backdoor Roth IRA
- id: backdoor_roth_ira
- kind: rule
- driven_by: MAGI above the Roth IRA phase-out, existing pre-tax IRA balances
- values: Two steps. First, make a nondeductible contribution to a traditional IRA, capped at $7,500 for 2026 or $8,600 at age 50 or older. Second, convert the traditional IRA to a Roth IRA. There is no income limit on either step. Roth conversions have had no income limit since 2010. The nondeductible contribution is reported on Form 8606 Part I, which establishes basis; the conversion is reported on Form 8606 Part II and on Form 1099-R. Basis carries forward on Form 8606 across years, so the form must be filed for every year a nondeductible contribution is made.
- shape: mechanical sequence, not a separate account type. The conversion is reported in the calendar year it occurs, even if the contribution was designated for a prior tax year. Failing to file Form 8606 risks the same dollars being taxed twice.
- indexed: yes for the contribution amount
- why_it_matters: This sequence lets a person whose MAGI exceeds the Roth IRA phase-out move IRA money into Roth form.
- source: [IRS Instructions for Form 8606](https://www.irs.gov/instructions/i8606); [IRS Publication 590-A](https://www.irs.gov/publications/p590a)
- confidence: high — note: the IRS does not publish a page using the term "backdoor Roth." The mechanics come from Form 8606 instructions and Publication 590-A, which document each step but not the label.

### IRA pro-rata rule
- id: ira_pro_rata_rule
- kind: rule
- driven_by: total pre-tax balance across all traditional, SEP, and SIMPLE IRAs on December 31
- values: For a Roth conversion, all of a person's traditional IRAs, SEP IRAs, and SIMPLE IRAs are treated as one combined account. The tax-free share of a conversion equals total after-tax basis divided by the total year-end value of all such IRAs plus distributions and conversions made during the year. A person cannot isolate the nondeductible dollars by opening a separate IRA or by converting only the new contribution.
- shape: proportional formula computed on Form 8606 using the aggregate December 31 value of all traditional, SEP, and SIMPLE IRAs, not the balance on the conversion date. Balances in 401(k), 403(b), and 457(b) plans are excluded from the calculation. Roth IRAs are excluded. Each spouse's IRAs are calculated separately; a spouse's IRA balance does not affect the other spouse's ratio. A common way to clear the denominator is to roll pre-tax IRA money into an employer plan that accepts incoming rollovers before December 31 of the conversion year.
- indexed: not applicable
- why_it_matters: Existing pre-tax IRA balances make part of a backdoor Roth conversion taxable in proportion to the pre-tax share of all IRAs combined.
- source: [IRS Instructions for Form 8606, line 6 and Part II](https://www.irs.gov/instructions/i8606); [IRS Publication 590-A](https://www.irs.gov/publications/p590a)
- confidence: high

### Mega-backdoor Roth
- id: mega_backdoor_roth
- kind: rule
- driven_by: plan features, section 415(c) headroom, employer contributions
- values: Make voluntary after-tax (non-Roth) contributions to a 401(k) in the space between total contributions already made and the $72,000 section 415(c) limit, then move those dollars to Roth. For 2026, the theoretical maximum after-tax room is $72,000 minus the $24,500 elective deferral minus any employer contributions, which is $47,500 when there is no employer contribution. Two plan features are required: the plan must permit voluntary after-tax contributions, and the plan must permit either in-plan Roth conversions under section 402A(c)(4) or in-service distributions that can be rolled out.
- shape: total contributions cannot exceed the lesser of 100% of compensation or $72,000, and the after-tax amount is what remains after deferrals and employer contributions. Earnings that accrue in the after-tax account before conversion are pre-tax amounts and are taxable when converted, so converting soon after each contribution limits taxable earnings. Under Notice 2014-54, distributions sent to multiple destinations at the same time are treated as a single distribution for allocating pre-tax and after-tax amounts, so a person can roll the after-tax basis to a Roth IRA and the pre-tax earnings to a traditional IRA. A partial distribution must still include a proportional share of pre-tax and after-tax amounts; a person cannot withdraw only the after-tax portion. The IRA pro-rata rule does not apply to this route, because 401(k) balances are not aggregated with IRAs.
- indexed: yes — the section 415(c) limit is indexed
- why_it_matters: This route can move substantially more into Roth accounts than the IRA or elective deferral limits allow, but only if the employer's plan supports both required features.
- source: [IRS: Rollovers of after-tax contributions in retirement plans](https://www.irs.gov/retirement-plans/rollovers-of-after-tax-contributions-in-retirement-plans); [IRS Notice 2014-54](https://www.irs.gov/pub/irs-drop/n-14-54.pdf); [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) for the section 415(c) figure
- confidence: high — note: as with the backdoor Roth, the IRS documents each mechanical step but does not publish a page using the term "mega-backdoor Roth."

---

## 6. Health Savings Accounts and HDHPs

### HSA contribution limit
- id: hsa_contribution_limit
- kind: limit
- driven_by: coverage tier (self-only or family), months of HSA eligibility
- values: Self-only coverage — $4,400 for 2026, up from $4,300 for 2025. Family coverage — $8,750 for 2026, up from $8,550 for 2025.
- shape: annual cap covering the combined total of employee and employer contributions. Eligibility is determined month by month; a person eligible for only part of the year is generally limited to one-twelfth of the annual amount per eligible month, subject to the last-month rule and its testing period. The family limit is shared between spouses, not doubled.
- indexed: yes — section 223(b)(2)
- why_it_matters: This is the maximum that can go into an HSA for 2026 from all sources combined, including any employer contribution.
- source: [IRS Rev. Proc. 2025-19](https://www.irs.gov/pub/irs-drop/rp-25-19.pdf) — section 2.01(1); [Internal Revenue Bulletin 2025-21](https://www.irs.gov/irb/2025-21_IRB)
- confidence: high

### HSA age 55 catch-up
- id: hsa_catch_up_age_55
- kind: limit
- driven_by: age
- values: $1,000. Unchanged. Total for a person aged 55 or older is $5,400 with self-only coverage or $9,750 with family coverage.
- shape: age rule — available to an HSA-eligible person who is age 55 or older by the end of the tax year, and only until the person enrolls in Medicare. The catch-up is per person, not per HSA and not per couple. If both spouses are 55 or older and want both catch-ups, each spouse must have their own HSA in their own name, because the catch-up cannot be contributed to a spouse's account.
- indexed: no — the $1,000 amount is fixed by section 223(b)(3)(B) and is not inflation-adjusted
- why_it_matters: A person aged 55 or older may contribute this amount above the coverage-tier limit, and each spouse needs a separate HSA to claim two catch-ups.
- source: [26 U.S.C. 223(b)(3)](https://www.law.cornell.edu/uscode/text/26/223); [IRS Publication 969](https://www.irs.gov/publications/p969)
- confidence: high — note: Rev. Proc. 2025-19 does not restate this amount because it is not indexed; the statute fixes it at $1,000.

### HDHP minimum annual deductible
- id: hdhp_min_deductible
- kind: limit
- driven_by: coverage tier
- values: Self-only coverage — not less than $1,700 for 2026, up from $1,650 for 2025. Family coverage — not less than $3,400 for 2026, up from $3,300 for 2025.
- shape: floor, not a cap. A plan with a deductible below these amounts is not a high deductible health plan, so enrollment in it does not make a person HSA-eligible.
- indexed: yes — section 223(c)(2)(A)
- why_it_matters: A health plan must have at least this deductible for the enrollee to be eligible to contribute to an HSA.
- source: [IRS Rev. Proc. 2025-19](https://www.irs.gov/pub/irs-drop/rp-25-19.pdf) — section 2.01(2)
- confidence: high

### HDHP maximum annual out-of-pocket
- id: hdhp_max_out_of_pocket
- kind: limit
- driven_by: coverage tier
- values: Self-only coverage — must not exceed $8,500 for 2026, up from $8,300 for 2025. Family coverage — must not exceed $17,000 for 2026, up from $16,600 for 2025.
- shape: ceiling. Out-of-pocket expenses include deductibles, co-payments, and other amounts, but exclude premiums. A plan whose out-of-pocket maximum exceeds these amounts is not a high deductible health plan.
- indexed: yes — section 223(c)(2)(A)
- why_it_matters: A health plan must keep out-of-pocket exposure at or below this amount for the enrollee to be eligible to contribute to an HSA.
- source: [IRS Rev. Proc. 2025-19](https://www.irs.gov/pub/irs-drop/rp-25-19.pdf) — section 2.01(2)
- confidence: high

---

## 7. Flexible Spending Arrangements

### Health FSA salary reduction limit
- id: health_fsa_limit
- kind: limit
- driven_by: none (flat cap per employee per employer)
- values: $3,400 for taxable years beginning in 2026. Increased from $3,300 for 2025.
- shape: flat cap on voluntary employee salary reductions under section 125(i). An employer may set a lower limit. Employer non-elective contributions are generally outside this cap. Spouses with separate employers may each elect up to the limit.
- indexed: yes — section 125(i)
- why_it_matters: This caps how much an employee can direct into a health FSA through pre-tax salary reduction for the 2026 plan year.
- source: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) — section 3.15, Cafeteria Plans
- confidence: high

### Health FSA carryover
- id: health_fsa_carryover
- kind: limit
- driven_by: plan design
- values: $680 maximum carryover for 2026. Increased from $660 for 2025.
- shape: cap on unused health FSA funds that may roll into the following plan year, available only if the cafeteria plan permits carryovers. An employer may set a lower carryover limit. A plan may offer a carryover or a grace period, but not both.
- indexed: yes
- why_it_matters: Health FSA funds above this amount that are unused at plan year end are forfeited under the use-or-lose rule.
- source: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) — section 3.15, Cafeteria Plans
- confidence: high

### Dependent care FSA limit
- id: dependent_care_fsa_limit
- kind: limit
- driven_by: filing status, earned income of both spouses
- values: $7,500 for 2026, or $3,750 for a married person filing separately. This is a statutory increase from the flat $5,000 and $2,500 amounts that had been unchanged since 1986.
- shape: household-level cap on the income exclusion under section 129, not a per-employee cap. The exclusion is further limited to the lesser-earning spouse's earned income, so a household with a non-working spouse who is not a full-time student and not incapable of self-care has an effective limit of $0. The increase is permissive rather than automatic; the employer's section 125 plan must be amended to adopt it.
- indexed: no — the $7,500 and $3,750 amounts are fixed by statute and are not annually adjusted
- why_it_matters: This caps the amount of dependent care benefits a household can exclude from income in 2026, and dependent care FSA use reduces expenses eligible for the child and dependent care credit dollar for dollar.
- source: [One Big Beautiful Bill Act, Pub. L. 119-21, section 70404](https://www.congress.gov/bill/119th-congress/house-bill/1/text), amending [26 U.S.C. 129(a)(2)(A)](https://www.law.cornell.edu/uscode/text/26/129)
- confidence: high for the amount and effective date — note: Rev. Proc. 2025-32 does not list a section 129 amount, because the change comes from statute and is not an inflation adjustment. I did not locate an IRS notice or revenue procedure restating the $7,500 figure, so the statute is the primary source here.

---

## 8. Saver's Credit and Saver's Match

### Saver's Credit income limits
- id: savers_credit
- kind: phase_out
- driven_by: adjusted gross income, filing status, age, student and dependent status
- values: Married filing jointly — 50% credit rate at AGI not more than $48,500; 20% rate from $48,501 to $52,500; 10% rate from $52,501 to $80,500; 0% above $80,500. Head of household — 50% at AGI not more than $36,375; 20% from $36,376 to $39,375; 10% from $39,376 to $60,375; 0% above $60,375. Single, married filing separately, and qualifying surviving spouse — 50% at AGI not more than $24,250; 20% from $24,251 to $26,250; 10% from $26,251 to $40,250; 0% above $40,250.
- shape: three-tier step function, not a smooth phase-out. The rate drops in discrete steps at each AGI boundary. The credit applies to the first $2,000 of qualifying contributions per person, or $4,000 on a joint return, so the maximum credit is $1,000 per person or $2,000 for a couple. Eligibility also requires being age 18 or older, not claimed as a dependent on another person's return, and not a student. Recent distributions from retirement accounts reduce the contributions that count.
- indexed: yes — section 25B(b)(1), adjusted using a variation of the section 1(f)(3) method
- why_it_matters: A person within these income ranges who contributes to a retirement account may claim a nonrefundable credit of up to $1,000 for 2026, capped at their tax liability.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — sections 25B(b)(1)(A) through (D); [IRS IR-2025-111](https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500)
- confidence: high for the dollar boundaries, which come directly from Notice 2025-67 — note: the IRS Saver's Credit topic page has not published a 2026 rate table (its most recent table is 2024), so the tier boundaries above are assembled from the Notice 2025-67 section 25B(b)(1)(A), (B), and (C)/(D) figures applied to the fixed statutory 50/20/10 percent structure.

### Saver's Credit to Saver's Match transition
- id: savers_match_transition
- kind: rule
- driven_by: tax year
- values: 2026 is the last tax year for the Saver's Credit as applied to retirement contributions. For taxable years beginning after December 31, 2026, SECURE 2.0 section 103 replaces it with the Saver's Match under new section 6433. The Saver's Match is a 50% federal match on up to $2,000 of contributions, capped at $1,000, paid directly into the person's retirement account rather than claimed as a credit, and available even with zero tax liability. Match payments are expected to begin in 2028 for the 2027 tax year. The Saver's Credit continues after 2026 only for contributions to ABLE accounts under section 529A, per section 70116 of the One Big Beautiful Bill Act.
- shape: hard switchover at the 2026/2027 tax year boundary. The Saver's Match will be claimed on a new Form 8880-A. Announced Saver's Match thresholds are MAGI below $20,500 (single) or $41,000 (married filing jointly) for the full match, with a reduced match phasing out $15,000 above that for single filers and $30,000 above for joint filers. Those thresholds are for the 2027 tax year and will be cost-of-living adjusted for years after 2027.
- indexed: the Saver's Match thresholds are adjusted for years after 2027
- why_it_matters: A person relying on the Saver's Credit for retirement contributions will see it replaced by a direct account deposit mechanism starting with the 2027 tax year.
- source: [IRS Notice 2026-48](https://www.irs.gov/pub/irs-drop/n-26-48.pdf), Notice of Intent to Issue Regulations with Respect to Saver's Match Contributions; [SECURE 2.0 Act section 103, Pub. L. 117-328](https://www.congress.gov/bill/117th-congress/house-bill/2617/text); [CRS In Focus IF11159](https://www.congress.gov/crs-product/IF11159)
- confidence: high for the 2027 effective date and the replacement mechanism — the specific 2027 Saver's Match income thresholds are from the CRS report rather than final IRS guidance, since proposed regulations are still pending.

---

## 9. Small business and self-employed plans

### SEP-IRA contribution limit
- id: sep_ira_limit
- kind: limit
- driven_by: compensation
- values: The lesser of 25% of the employee's compensation or $72,000 for 2026. Compensation counted is capped at $360,000 under section 401(a)(17).
- shape: percentage-of-pay limit with a dollar ceiling. Elective salary deferrals and catch-up contributions are not permitted in a SEP, so there is no age 50 or ages 60 to 63 addition. For a self-employed person the 25% is applied to net earnings from self-employment after deducting one-half of self-employment tax and the contribution itself, which works out to an effective rate near 20% of net profit; the rate table and worksheets in Chapter 5 of Publication 560 do this calculation. Grandfathered SARSEPs established before 1997 may still take elective deferrals up to $24,500 or 25% of compensation, whichever is less.
- indexed: yes — the dollar ceiling tracks section 415(c)
- why_it_matters: This caps what an employer, including a self-employed person acting as their own employer, can contribute to a SEP-IRA for one person in 2026.
- source: [IRS: SEP contribution limits](https://www.irs.gov/retirement-plans/plan-participant-employee/sep-contribution-limits-including-grandfathered-sarseps); [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf)
- confidence: high

### SEP participation compensation threshold
- id: sep_comp_threshold
- kind: cliff
- driven_by: compensation received from the employer
- values: $800 for 2026. Increased from $750 for 2025.
- shape: minimum compensation an employee must receive during the year for the employer to be required to include them in the SEP. Employees earning less may be excluded.
- indexed: yes — section 408(k)(2)(C)
- why_it_matters: An employee earning at least this amount from an employer that maintains a SEP generally must be covered by it if the other eligibility conditions are met.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — section 408(k)(2)(C)
- confidence: high

### Solo 401(k) limit
- id: solo_401k_limit
- kind: limit
- driven_by: earned income, age
- values: A one-participant 401(k) is a regular 401(k) covering only a business owner, or the owner and spouse, and uses the same limits. Employee elective deferrals up to $24,500, plus employer nonelective contributions of up to 25% of compensation, with total annual additions capped at the lesser of 100% of compensation or $72,000. Catch-ups apply on top: $8,000 at age 50 to 59 and 64 or older, or $11,250 at ages 60 to 63.
- shape: two contribution capacities for the same person, as employee and as employer. The $24,500 elective deferral limit is per person across all employers, so an owner who also defers in a day-job 401(k) has that much less deferral capacity in the solo plan; the $72,000 section 415(c) limit, in contrast, applies per unrelated employer. For a self-employed owner, compensation means earned income, defined as net earnings from self-employment after deducting one-half of self-employment tax and the contributions made for the owner. A Form 5500-EZ filing is generally required once plan assets reach $250,000 at year end.
- indexed: yes — all component amounts are indexed
- why_it_matters: A self-employed person can contribute in both employee and employer capacities, reaching a higher total than a SEP allows at the same income level.
- source: [IRS: One-participant 401(k) plans](https://www.irs.gov/retirement-plans/one-participant-401k-plans); [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf)
- confidence: high

### SIMPLE IRA deferral limit
- id: simple_ira_limit
- kind: limit
- driven_by: employer size and plan type
- values: $17,000 for 2026 generally, up from $16,500 for 2025. A higher limit of $18,100 applies to certain SIMPLE plans under section 408(p)(2)(E)(i)(I) or (II), up from $17,600 for 2025. The higher amount is available under a SECURE 2.0 change for employers with 25 or fewer employees, and for employers with 26 to 100 employees that make enhanced employer contributions.
- shape: two-tier limit determined by employer size and employer contribution level, not by the participant.
- indexed: yes — section 408(p)(2)(E)
- why_it_matters: This caps salary reduction contributions to a SIMPLE IRA or SIMPLE 401(k) for 2026.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — sections 408(p)(2)(E)(i)(I), (II), and (III); [IRS IR-2025-111](https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500)
- confidence: high

### SIMPLE plan catch-up contributions
- id: simple_ira_catch_up
- kind: limit
- driven_by: age, employer size and plan type
- values: Age 50 or older, general SIMPLE plans — $4,000 for 2026, up from $3,500 for 2025. Age 50 or older, certain applicable SIMPLE plans under section 414(v)(2)(B)(iii) — remains $3,850. Ages 60 to 63, all SIMPLE plans — remains $5,250.
- shape: age bands mirroring the workplace plan structure. The ages 60 to 63 amount uses the same statutory age rule: the participant must reach age 60, 61, 62, or 63 during the calendar year, and reverts at age 64. The $3,850 figure for certain applicable plans is now lower than the $4,000 general amount because it was set at 110% of the 2024 base and has not kept pace.
- indexed: yes for the $4,000 amount; the $3,850 and $5,250 amounts were computed and remained unchanged for 2026
- why_it_matters: These are the additional amounts a SIMPLE plan participant may defer above the standard SIMPLE limit based on age.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — sections 414(v)(2)(B)(ii), 414(v)(2)(B)(iii), and 414(v)(2)(E)(ii); [IRS IR-2025-111](https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500)
- confidence: high — note: the mandatory Roth catch-up rule does not apply to SIMPLE IRA plans.

---

## 10. Early withdrawals

### Section 72(t) early withdrawal penalty and age 59½
- id: early_withdrawal_penalty_72t
- kind: rule
- driven_by: age at the time of distribution, plan type
- values: A 10% additional tax applies to amounts withdrawn from an IRA or retirement plan before the owner reaches age 59½, unless an exception applies. This is in addition to ordinary income tax on the taxable portion. Distributions from a SIMPLE IRA within the first two years of participation carry a 25% additional tax instead of 10%. Distributions from a governmental 457(b) plan are generally not subject to the 10% additional tax, except for amounts attributable to rollovers from another plan type or from an IRA.
- shape: age threshold at exactly 59½, measured as six calendar months after the 59th birthday, not a year boundary. The tax is reported on Form 5329 where the Form 1099-R does not already show the correct exception code.
- indexed: not applicable — the 10% rate is fixed
- why_it_matters: Withdrawing retirement funds before age 59½ triggers an extra 10% tax on top of ordinary income tax unless a listed exception applies.
- source: [IRS: Retirement topics — Exceptions to tax on early distributions](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-exceptions-to-tax-on-early-distributions); [26 U.S.C. 72(t)](https://www.law.cornell.edu/uscode/text/26/72)
- confidence: high

### Rule of 55
- id: rule_of_55
- kind: rule
- driven_by: age at separation from service, plan type
- values: The 10% additional tax does not apply if the employee separates from service during or after the calendar year in which the employee reaches age 55. For qualified public safety employees of a state or political subdivision in a governmental defined benefit or defined contribution plan, the age is 50 instead of 55.
- shape: age and event rule with two conditions that must both hold. The separation must occur in or after the year age 55 is reached; separating at 54 and waiting until 55 does not qualify. It applies only to distributions from the qualified plan of the employer the person separated from. It does not apply to IRAs, and rolling the plan balance into an IRA forfeits it. The expanded public safety category covers specified federal law enforcement officers, corrections officers, customs and border protection officers, federal firefighters, private-sector firefighters, and air traffic controllers, and applies to defined benefit plans, defined contribution plans, and other governmental plans such as the TSP.
- indexed: not applicable
- why_it_matters: An employee who leaves a job in or after the year they turn 55 can take distributions from that employer's plan without the 10% additional tax, even though they are under 59½.
- source: [IRS: Retirement topics — Exceptions to tax on early distributions](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-exceptions-to-tax-on-early-distributions) — sections 72(t)(2)(A)(v) and 72(t)(10)
- confidence: high for the age 55 and age 50 rules as stated on the IRS page — medium on one detail: section 72(t)(10)(A) as amended by SECURE 2.0 also refers to separation after 25 years of service under the plan, whichever comes earlier, for qualified public safety employees. The IRS topic page states only the age 50 test, so verify the 25-year alternative against the statute before relying on it.

### Main exceptions to the 10% additional tax
- id: early_withdrawal_exceptions
- kind: rule
- driven_by: circumstance, plan type, age
- values: Available for both plans and IRAs — age 59½ or older; death of the owner; total and permanent disability; a series of substantially equal periodic payments under section 72(t)(2)(A)(iv); unreimbursed medical expenses above 7.5% of AGI; IRS levy on the account; qualified military reservist called to active duty; birth or adoption expenses up to $5,000 per child; one emergency personal expense per calendar year up to the lesser of $1,000 or the vested balance over $1,000; domestic abuse victim distributions up to the lesser of $10,500 for 2026 or 50% of the account; federally declared disaster recovery distributions up to $22,000; and 60-day rollovers. Available only for plans, not IRAs — separation from service in or after the year age 55 is reached; qualified domestic relations order payments to an alternate payee; ESOP dividend pass-through; terminal illness certified by a physician; pension-linked emergency savings account distributions; permissive withdrawals from an automatic enrollment arrangement; and timely corrective distributions of excess contributions or deferrals. Available only for IRAs, not plans — qualified higher education expenses; first-time homebuyer expenses up to $10,000 lifetime; health insurance premiums paid while unemployed; and returned IRA contributions withdrawn by the extended due date.
- shape: circumstance-based list. Availability differs by account type, so the same circumstance may be an exception for an IRA but not for a 401(k), or the reverse. Exceptions remove the 10% additional tax only; ordinary income tax on the taxable portion still applies.
- indexed: the domestic abuse victim limit is indexed and rose from $10,300 for 2025 to $10,500 for 2026; the $5,000, $1,000, $10,000, and $22,000 amounts are fixed
- why_it_matters: An early distribution that fits one of these circumstances avoids the 10% additional tax but is still subject to ordinary income tax on the taxable portion.
- source: [IRS: Retirement topics — Exceptions to tax on early distributions](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-exceptions-to-tax-on-early-distributions); [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) for the section 72(t)(2)(K)(ii)(I) domestic abuse amount
- confidence: high

---

## Age thresholds summary

| Age | What changes in 2026 |
| --- | --- |
| 18 | Minimum age for the Saver's Credit (plus not a dependent and not a student) |
| 50 | Workplace plan catch-up of $8,000 and IRA catch-up of $1,100 become available; measured as age attained by the end of the taxable year. Also the public safety employee separation-from-service age |
| 55 | HSA catch-up of $1,000 becomes available. Also the Rule of 55 separation-from-service age for qualified plans |
| 59½ | Section 72(t) 10% additional tax on early distributions no longer applies |
| 60 | Super catch-up of $11,250 replaces the $8,000 catch-up; triggered by reaching age 60 at any point in the calendar year |
| 63 | Last year of the super catch-up |
| 64 | Super catch-up ends; the catch-up returns to $8,000 in the calendar year age 64 is reached |
| 65 | Medicare enrollment ends HSA contribution eligibility (Medicare itself is out of scope for this leg) |

## Notes on sourcing

Every dollar figure above traces to one of five primary documents: IRS Notice 2025-67,
IRS Rev. Proc. 2025-19, IRS Rev. Proc. 2025-32, Treasury Decision 10033, or the
Internal Revenue Code. IRS.gov retirement topic pages supply the narrative rules for
early distribution exceptions, solo 401(k) mechanics, and SEP limits. Brokerage and
law firm material was used only to locate primary documents and was not the sole
source for any figure.
