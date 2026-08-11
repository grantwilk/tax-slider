# F — Health coverage, education savings, and gift/estate parameters (Tax Year 2026)

Compiled August 11, 2026. Figures are US federal. Primary sources are named in each block.

**Headline for ACA:** ARPA/IRA enhanced premium tax credits ended after tax year 2025. For 2026, IRC §36B returns to the pre-ARPA structure: household income must be at least 100% and not more than 400% of the federal poverty line (the “subsidy cliff” is back), and the indexed applicable-percentage table in Rev. Proc. 2025-25 applies. Separately, OBBBA (P.L. 119-21) removed APTC excess-repayment caps for tax years after 2025.

---

### ACA premium tax credit — enhanced subsidy expiration and 400% FPL cliff
- id: aca_ptc_cliff_2026
- kind: cliff
- driven_by: household MAGI as a percent of FPL for family size; filing and coverage month facts
- values: For tax years after 2025, PTC eligibility again requires household income of at least 100% and not more than 400% of the FPL for family size. The temporary rule that allowed income above 400% FPL (tax years 2021–2025) no longer applies. Continental 400% FPL using 2025 HHS guidelines (used for 2026 coverage): HH1 $62,600; HH2 $84,600; HH3 $106,600; HH4 $128,600; HH5 $150,600.
- shape: At or below 400% FPL (and otherwise eligible): PTC may apply using the applicable-percentage table. Above 400% FPL: no federal PTC (subsidy cliff). Below 100% FPL: generally outside the statutory PTC income band (separate Medicaid/CHIP rules may apply).
- indexed: FPL amounts yes (annual HHS guidelines); the 400% statutory ceiling itself is not a dollar index — it is a percent of FPL.
- why_it_matters: Household income above 400% of FPL for 2026 eliminates the federal premium tax credit that was available above that line for 2021–2025.
- source: [IRS FS-2025-10](https://www.irs.gov/pub/taxpros/fs-2025-10.pdf) (Questions and Answers about the Premium Tax Credit); [CRS R48290](https://www.congress.gov/crs-product/R48290) (Enhanced Premium Tax Credit and 2026 Exchange Premiums)
- confidence: high — IRS FS-2025-10 states the 2021–2025 expansion above 400% FPL and that ordinary eligibility is 100%–400% FPL; CRS confirms the IRA sunset date of January 1, 2026 for the enhancement.

### ACA premium tax credit — 2026 applicable percentage table
- id: aca_ptc_applicable_percentage_table_2026
- kind: phase_out
- driven_by: household income as a percentage of FPL
- values: For taxable years beginning in 2026 (Rev. Proc. 2025-25):

  | Household income % of FPL | Initial % | Final % |
  |---|---|---|
  | Less than 133% | 2.10% | 2.10% |
  | At least 133% but less than 150% | 3.14% | 4.19% |
  | At least 150% but less than 200% | 4.19% | 6.60% |
  | At least 200% but less than 250% | 6.60% | 8.44% |
  | At least 250% but less than 300% | 8.44% | 9.96% |
  | At least 300% but not more than 400% | 9.96% | 9.96% |

  Required contribution percentage for employer-coverage affordability (plan years beginning in 2026): 9.96%.
- shape: Within each band, the applicable figure rises linearly from the initial to the final percentage (except flat bands). The taxpayer’s expected contribution for benchmark (second-lowest-cost silver) coverage equals applicable figure × household income. PTC equals excess of benchmark premium over that amount (subject to eligibility). No row exists above 400% FPL for 2026.
- indexed: yes — annual indexing under §36B(b)(3)(A) (ARPA/IRA freeze of the table ended with the enhancement).
- why_it_matters: These percentages set how much of household income a PTC-eligible enrollee is expected to pay toward the benchmark silver premium in 2026.
- source: [IRS Rev. Proc. 2025-25](https://www.irs.gov/pub/irs-drop/rp-25-25.pdf)
- confidence: high

### Advance PTC excess repayment — caps removed for 2026
- id: aptc_excess_repayment_caps_2026
- kind: rule
- driven_by: advance PTC paid vs. final Form 8962 PTC; household income and filing status (caps were historically income-based)
- values: For tax years after 2025, there is no repayment cap. The taxpayer must repay the full excess of advance PTC over the allowable PTC. (For tax years before 2026, other than 2020, income-based caps applied only if household income was under 400% FPL.)
- shape: Excess APTC increases tax liability dollar-for-dollar for tax years after 2025; prior-year cap schedules do not limit 2026.
- indexed: n/a (caps repealed for years after 2025 by OBBBA amendment to §36B(f)(2))
- why_it_matters: Any overestimate of advance premium tax credit for 2026 must be repaid in full on the tax return.
- source: [IRS FS-2025-10](https://www.irs.gov/pub/taxpros/fs-2025-10.pdf); [IRS IR-2025-127](https://www.irs.gov/newsroom/irs-updates-frequently-asked-questions-on-the-premium-tax-credit); [IRS Working Families Tax Cuts](https://www.irs.gov/newsroom/working-families-tax-cuts) (PTC sections 71301–71305)
- confidence: high

### Federal poverty guidelines used for 2026 Marketplace PTC (HH sizes 1–5)
- id: fpl_2025_guidelines_hh1_to_5
- kind: limit
- driven_by: household/family size; state of residence (48 contiguous + DC vs Alaska vs Hawaii)
- values: 2025 HHS poverty guidelines (48 contiguous states and D.C.): HH1 $15,650; HH2 $21,150; HH3 $26,650; HH4 $32,150; HH5 $37,650. (Add $5,500 per person above 8.) Alaska and Hawaii have higher separate tables.
- shape: Dollar guideline rises with household size; PTC uses multiples of these amounts (100%, 133%, 150%, …, 400%).
- indexed: yes — HHS updates annually in the Federal Register.
- why_it_matters: These dollar amounts are the base used to compute FPL percentages that determine 2026 PTC eligibility and the applicable figure.
- source: [Federal Register 90 Fed. Reg. 5917 (Jan. 17, 2025)](https://www.govinfo.gov/content/pkg/FR-2025-01-17/pdf/2025-01377.pdf); [ASPE detailed guidelines PDF](https://aspe.hhs.gov/sites/default/files/documents/dd73d4f00d8a819d10b2fdb70d254f7b/detailed-guidelines-2025.pdf)
- confidence: high

### Which year’s FPL applies to 2026 coverage
- id: fpl_year_rule_for_2026_coverage
- kind: rule
- driven_by: coverage/taxable year and open-enrollment calendar
- values: Under Treas. Reg. §1.36B-1(h), the FPL is the most recently published HHS poverty guidelines as of the first day of the regular annual open enrollment period that precedes that taxable year. For 2026 coverage (open enrollment beginning November 1, 2025), that is the **2025** HHS poverty guidelines.
- shape: Prior-year (as of open enrollment start) guidelines apply for the coming coverage year; mid-year residence moves between states with different guidelines use the higher guideline.
- indexed: yes (via annual HHS publication)
- why_it_matters: 2026 Marketplace PTC calculations use the 2025 poverty guidelines, not the 2026 guidelines published later.
- source: [26 CFR §1.36B-1(h)](https://www.law.cornell.edu/cfr/text/26/1.36B-1); [HHS FR 2025-01377](https://www.govinfo.gov/content/pkg/FR-2025-01-17/pdf/2025-01377.pdf)
- confidence: high

### HDHP minimum annual deductible (2026)
- id: hdhp_minimum_deductible_2026
- kind: limit
- driven_by: self-only vs family HDHP coverage
- values: Self-only: not less than $1,700. Family: not less than $3,400. (Calendar year 2026.)
- shape: Plan deductible must meet or exceed the minimum to be an HDHP under §223(c)(2)(A), except bronze/catastrophic Exchange-available plans treated as HDHPs under OBBBA (see separate parameter).
- indexed: yes — Rev. Proc. 2025-19
- why_it_matters: A plan below these deductible floors is not a statutory HDHP for HSA eligibility unless an OBBBA bronze/catastrophic rule applies.
- source: [IRS Rev. Proc. 2025-19](https://www.irs.gov/pub/irs-drop/rp-25-19.pdf)
- confidence: high

### HDHP maximum out-of-pocket (2026)
- id: hdhp_maximum_oop_2026
- kind: limit
- driven_by: self-only vs family HDHP coverage
- values: Annual out-of-pocket expenses (deductibles, copayments, and other amounts, but not premiums) must not exceed $8,500 (self-only) or $17,000 (family) for calendar year 2026.
- shape: Exceeding the cap means the plan is not an HDHP under §223(c)(2)(A), subject to the OBBBA bronze/catastrophic treatment exception.
- indexed: yes — Rev. Proc. 2025-19
- why_it_matters: Out-of-pocket maximums above these amounts generally disqualify the plan as an HDHP for HSA purposes.
- source: [IRS Rev. Proc. 2025-19](https://www.irs.gov/pub/irs-drop/rp-25-19.pdf)
- confidence: high

### HSA annual contribution limits (2026)
- id: hsa_contribution_limit_2026
- kind: limit
- driven_by: self-only vs family HDHP coverage; age 55+ catch-up; months of eligibility / last-month rule
- values: Self-only: $4,400. Family: $8,750. Age-55+ catch-up: additional $1,000 (statutory §223(b)(3); not inflation-adjusted in Rev. Proc. 2025-19).
- shape: Annual deduction/contribution ceiling for an eligible individual; prorated by months of eligibility unless last-month rule applies.
- indexed: annual limits yes (Rev. Proc. 2025-19); catch-up $1,000 fixed in statute for 2026.
- why_it_matters: These amounts cap combined employer and individual HSA contributions for 2026.
- source: [IRS Rev. Proc. 2025-19](https://www.irs.gov/pub/irs-drop/rp-25-19.pdf); IRC §223(b)(3)
- confidence: high

### HSA — other coverage that disqualifies eligibility
- id: hsa_disqualifying_other_coverage
- kind: rule
- driven_by: whether the individual (and spouse coverage that covers the individual) has non-HDHP medical coverage
- values: An eligible individual must be covered by an HDHP and generally have no other health coverage. Disqualifying coverage includes most non-HDHP medical plans and a **general-purpose** health FSA or HRA that reimburses medical expenses before the HDHP deductible. Permitted coverage includes (examples from Pub. 969): accident, disability, dental, vision, long-term care, certain preventive care, limited-purpose FSA/HRA (dental/vision/preventive), and post-OBBBA certain telehealth and direct primary care arrangements under Notice 2026-05 / §71307.
- shape: HDHP + only permitted other coverage → can contribute. Any disqualifying first-dollar medical coverage for the individual → not an eligible individual for those months.
- indexed: no (statutory/regulatory categories; specific dollar HDHP tests are indexed separately)
- why_it_matters: Non-HDHP medical coverage or a general-purpose health FSA that covers the individual blocks HSA contributions for the months it applies.
- source: [IRS Publication 969](https://www.irs.gov/publications/p969); [IRS Notice 2026-05](https://www.irs.gov/pub/irs-drop/n-26-05.pdf)
- confidence: high for the general rule and FSA interaction; medium for the full post-OBBBA telehealth/DPC edge cases (rely on Notice 2026-05 text).

### HSA last-month rule
- id: hsa_last_month_rule
- kind: rule
- driven_by: eligibility status on December 1 (for calendar-year taxpayers) and continued eligibility during the testing period
- values: If you are an eligible individual on the first day of the last month of your tax year (December 1 for most taxpayers), you are treated as an eligible individual for the entire year and may contribute the full annual limit based on the HDHP coverage type on that day. Testing period: begins with that last month and ends on the last day of the 12th month following that month (e.g., Dec. 1, 2026–Dec. 31, 2027). Failure to remain eligible (other than death or disability) requires income inclusion of contributions that depended on the rule, plus a 10% additional tax.
- shape: Eligible on Dec. 1 → full-year contribution limit available; lose eligibility in testing period → clawback of last-month-rule amounts.
- indexed: no (procedural rule); contribution dollars indexed separately
- why_it_matters: Becoming HSA-eligible late in the year can still allow a full annual contribution if the December 1 test and testing period are met.
- source: [IRS Publication 969](https://www.irs.gov/publications/p969) (Last-month rule); IRC §223(b)(8)
- confidence: high

### OBBBA — bronze and catastrophic plans treated as HDHPs for HSA eligibility
- id: obbba_bronze_catastrophic_hsa_eligibility
- kind: rule
- driven_by: enrollment in a bronze or catastrophic plan available as individual coverage through an ACA Exchange (or identical off-Exchange plan)
- values: For months beginning after December 31, 2025, a bronze or catastrophic plan available as individual coverage through an Exchange under ACA §1311 or §1321 is treated as an HDHP even if it fails the §223(c)(2)(A) minimum deductible or maximum OOP tests. Off-Exchange purchase of the same plan also qualifies. IRS.gov states the treatment applies whether bought on or off Exchange. Notice 2026-05 Q&A-4 through Q&A-7 detail Exchange-availability and ICHRA-premium-only interactions.
- shape: Before 2026: many bronze/catastrophic plans failed HDHP tests. After Dec. 31, 2025: Exchange-available bronze/catastrophic → treated as HDHP → HSA contributions allowed if no other disqualifying coverage.
- indexed: no (statutory classification); HSA contribution and other HDHP dollar tests remain indexed
- why_it_matters: Enrollees in Exchange-available bronze or catastrophic individual coverage can be HSA-eligible in 2026 even when the plan’s deductible or OOP exceeds ordinary HDHP limits.
- source: [IRS Notice 2026-05](https://www.irs.gov/pub/irs-drop/n-26-05.pdf); [IRS Working Families Tax Cuts — HSA §71307](https://www.irs.gov/newsroom/working-families-tax-cuts)
- confidence: high

### Health FSA salary-reduction contribution limit (2026)
- id: health_fsa_contribution_limit_2026
- kind: limit
- driven_by: employee cafeteria-plan salary reduction election for the plan year
- values: $3,400 maximum voluntary employee salary reduction for health FSAs for plan years beginning in 2026 (§125(i)).
- shape: Cap per employee election; employer may set a lower plan limit.
- indexed: yes — Rev. Proc. 2025-32
- why_it_matters: Employee pre-tax health FSA contributions cannot exceed $3,400 for 2026 plan years under federal law.
- source: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) §4.15
- confidence: high

### Health FSA carryover maximum (2026)
- id: health_fsa_carryover_2026
- kind: limit
- driven_by: whether the employer’s cafeteria plan permits carryover of unused health FSA amounts
- values: If the plan permits carryover, the maximum carryover is $680 for plan years beginning in 2026 (20% of the $3,400 salary-reduction limit).
- shape: Unused amounts up to $680 may carry into the next plan year if the plan allows; otherwise use-or-lose applies (grace period rules are separate).
- indexed: yes — tied to the §125(i) limit in Rev. Proc. 2025-32
- why_it_matters: The federal maximum unused health FSA balance that may carry into the next plan year is $680 for 2026.
- source: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) §4.15
- confidence: high

### Health FSA interaction with HSA eligibility
- id: health_fsa_hsa_interaction
- kind: rule
- driven_by: type of FSA (general-purpose vs limited-purpose) and whether the FSA covers the HSA individual
- values: A general-purpose health FSA that can reimburse medical expenses before the HDHP deductible is other coverage that makes the individual ineligible for HSA contributions. A limited-purpose FSA (typically dental, vision, and/or preventive care only) does not disqualify HSA eligibility. (See also Pub. 969 “Other health coverage” / limited-purpose FSA.)
- shape: General-purpose FSA covering the person → no HSA contributions for those months. Limited-purpose only → HSA still allowed if HDHP rules otherwise met.
- indexed: no
- why_it_matters: Electing a general-purpose health FSA for a year generally prevents HSA contributions for that coverage period.
- source: [IRS Publication 969](https://www.irs.gov/publications/p969)
- confidence: high

### Dependent care FSA / dependent care assistance exclusion (2026)
- id: dependent_care_fsa_limit_2026
- kind: limit
- driven_by: filing status; employer plan adoption of the higher §129 limit
- values: OBBBA §70404 raises the §129 exclusion for employer-provided dependent care assistance to **$7,500** ($3,750 if married filing separately) for years beginning after December 31, 2025. Prior law was $5,000 / $2,500. Amounts are not indexed for inflation. Employers must amend plans to allow the higher election.
- shape: Exclusion/contribution ceiling per household under the plan; MFS is half. No automatic inflation increases after the statutory reset.
- indexed: no
- why_it_matters: The maximum pre-tax dependent care assistance amount rises to $7,500 for 2026 when the employer plan permits it.
- source: [CRS R48611](https://www.congress.gov/crs_external_products/R/PDF/R48611/R48611.1.pdf) (Tax Provisions in P.L. 119-21, §70404); IRC §129 as amended by OBBBA
- confidence: high

### 529 plan — annual gift exclusion that governs contributions (2026)
- id: gift_annual_exclusion_for_529_2026
- kind: exclusion
- driven_by: donor identity; number of donee beneficiaries; present-interest gifts
- values: Annual gift tax exclusion under §2503(b) for calendar year 2026 is **$19,000** per donee (Rev. Proc. 2025-32). A 529 contribution is generally a completed present-interest gift to the designated beneficiary.
- shape: Gifts to a single donee up to $19,000 in 2026 are excluded from taxable gifts; amounts above may use lifetime exclusion or the five-year 529 election.
- indexed: yes
- why_it_matters: Each donor can give up to $19,000 per 529 beneficiary in 2026 without using lifetime gift/estate exclusion, before any five-year election.
- source: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) §4.42(1); [IRC §529(c)(2)](https://www.law.cornell.edu/uscode/text/26/529)
- confidence: high

### 529 plan — five-year front-loading election
- id: five_year_529_front_load_election
- kind: rule
- driven_by: donor election under §529(c)(2)(B); annual exclusion amount
- values: If aggregate 529 contributions by a donor for a beneficiary in a calendar year exceed the §2503(b) annual exclusion, the donor may elect to treat the contribution as made ratably over five years beginning with that year. For 2026, five times $19,000 = **$95,000** per donor per beneficiary under a full front-load (assuming no other gifts to that donee that use the exclusion in those years).
- shape: Excess over one year’s exclusion is spread over five years; death before the five-year period ends pulls remaining unallocated amounts into the gross estate.
- indexed: yes (tracks the annual exclusion)
- why_it_matters: A donor can contribute up to five years of annual exclusions to a 529 in one year by electing the statutory five-year spread.
- source: [IRC §529(c)(2)(B)](https://www.law.cornell.edu/uscode/text/26/529); annual exclusion from [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- confidence: high

### OBBBA expansion of 529 qualified expenses
- id: obbba_529_qualified_expense_expansion
- kind: rule
- driven_by: type of expense; K-12 vs postsecondary credentialing; distribution date
- values: (1) K-12: eligible expenses expanded beyond tuition to include curricular materials, books/instructional materials, online education materials, certain tutoring, certain test fees, dual-enrollment fees, and certain educational therapies for students with disabilities — effective for distributions after July 4, 2025. (2) K-12 annual distribution cap increases from $10,000 to **$20,000** per beneficiary — effective after December 31, 2025 (i.e., for 2026). (3) Qualified postsecondary credentialing expenses (tuition, fees, books, supplies, certain testing/CE fees for recognized credential programs) — effective for distributions after enactment (July 4, 2025).
- shape: Distributions for newly qualified expenses after the effective dates are tax-free to the extent of earnings rules; K-12 dollars above the annual cap are not qualified.
- indexed: K-12 dollar cap is a statutory amount (now $20,000); not described as annually indexed in CRS summary.
- why_it_matters: 529 withdrawals for 2026 can cover a broader set of K-12 costs up to $20,000 and certain credentialing costs.
- source: [CRS R48611](https://www.congress.gov/crs_external_products/R/PDF/R48611/R48611.1.pdf) §§70413–70414; OBBBA / P.L. 119-21
- confidence: high for the dollar cap and effective dates from CRS; medium for exhaustive program lists (statute/regulations define “recognized” credentials).

### 529-to-Roth IRA rollover (SECURE 2.0)
- id: secure_2_529_to_roth_ira_rollover
- kind: rule
- driven_by: account age; beneficiary identity; annual IRA limit; prior rollovers
- values: Direct trustee-to-trustee rollover from a long-term §529 QTP to a Roth IRA for the same designated beneficiary: (1) 529 must have been maintained for the 15-year period ending on the distribution date; (2) amount limited to contributions (and attributable earnings) made before the 5-year period ending on the distribution date; (3) annual amount limited to the beneficiary’s IRA contribution limit for the year reduced by other IRA contributions; (4) aggregate lifetime limit **$35,000** per beneficiary. Effective for distributions after December 31, 2023.
- shape: Meets all tests → nontaxable rollover to beneficiary’s Roth IRA. Fails any test → ordinary 529 distribution tax rules.
- indexed: lifetime $35,000 is statutory (not annually indexed in the statute); annual piece tracks IRA limits.
- why_it_matters: Unused 529 funds can move to the beneficiary’s Roth IRA only within the 15-year, 5-year-lookback, annual IRA, and $35,000 lifetime limits.
- source: [SECURE 2.0 §126 / IRC §529(c)(3)(E)](https://assets.comptroller.texas.gov/tgtp/se/Sec%20126%20Secure%202.0%20Act.pdf) (statutory text); IRC §529(c)(3)(E)
- confidence: high on statutory limits; medium on open IRS guidance questions (e.g., whether a beneficiary change resets the 15-year clock).

### Coverdell ESA contribution and MAGI phase-out
- id: coverdell_esa_limits
- kind: phase_out
- driven_by: contributor MAGI and filing status; total contributions per beneficiary
- values: Maximum contribution **$2,000** per beneficiary per year across all Coverdell ESAs. Phase-out of the contributor’s limit: MAGI $95,000–$110,000 (single / not joint); $190,000–$220,000 (joint). At or above the top of the range, contribution limit is zero. Statutory amounts; unchanged for 2026. Contributions must generally stop when the beneficiary turns 18 (special-needs exception).
- shape: Below phase-out start → full $2,000 available (subject to aggregate-per-beneficiary cap). Inside range → proportional reduction. At/above end → no contribution by that individual.
- indexed: no
- why_it_matters: Coverdell contributions remain capped at $2,000 per child per year and phase out at fixed MAGI thresholds that are not inflation-adjusted.
- source: [IRS Topic No. 310](https://www.irs.gov/taxtopics/tc310); [IRS Publication 970](https://www.irs.gov/publications/p970) Ch. 6; IRC §530
- confidence: high

### Trump accounts (OBBBA §70204) for 2026
- id: trump_accounts_2026
- kind: limit
- driven_by: child’s age/SSN/citizenship; contributor type; birth year for pilot seed
- values: New IRC §530A Trump accounts exist for 2026. Key figures: (1) Individual contributions up to **$5,000** per year in cash until the beneficiary turns 18 (inflation adjustments after 2027 per CRS). (2) Accounts **cannot be funded before July 4, 2026** (IRS). (3) Employer contributions up to **$2,500** per year to an employee’s or dependent’s Trump account (excludable; inflation after 2027). (4) Pilot program: one-time **$1,000** Treasury contribution for a U.S. citizen child born after Dec. 31, 2024, and before Jan. 1, 2029 (born 2025–2028), with SSN, upon election (IRC §6434). Pilot contribution does not count toward the $5,000 limit (proposed regulations / FR summary). Invested in diversified U.S. equity index funds; no distributions before age 18 year rules.
- shape: Eligible minor with account → annual contribution room as above; pilot seed is one-time for qualifying birth years; funding window opens July 4, 2026.
- indexed: $5,000 and $2,500 scheduled for inflation after 2027 (CRS); $1,000 pilot fixed.
- why_it_matters: Starting July 4, 2026, adults can fund a child’s Trump account up to $5,000 per year, and eligible children born 2025–2028 can receive a one-time $1,000 federal contribution.
- source: [IRS Working Families Tax Cuts — Trump Accounts](https://www.irs.gov/newsroom/working-families-tax-cuts); [CRS R48611 §70204](https://www.congress.gov/crs_external_products/R/PDF/R48611/R48611.1.pdf); [IRC §6434](https://www.law.cornell.edu/uscode/text/26/6434); [IRS IR-2026-31 proposed regs announcement](https://www.irs.gov/newsroom/treasury-irs-issue-proposed-regulations-for-trump-accounts-contribution-pilot-program-treasury-department-to-deposit-1000-into-the-account-of-each-eligible-child)
- confidence: high on dollar amounts and July 4, 2026 funding start from IRS/CRS; medium on operational election mechanics still in proposed regulations.

### Annual gift tax exclusion (2026)
- id: annual_gift_tax_exclusion_2026
- kind: exclusion
- driven_by: donor; each donee; present vs future interest
- values: **$19,000** per donee for calendar year 2026 (§2503(b)).
- shape: Present-interest gifts ≤ $19,000 per donee are excluded from taxable gifts; future interests do not qualify for this exclusion.
- indexed: yes
- why_it_matters: A donor can transfer $19,000 to each recipient in 2026 without creating a taxable gift.
- source: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) §4.42(1)
- confidence: high

### Annual exclusion for gifts to a non-citizen spouse (2026)
- id: gift_exclusion_noncitizen_spouse_2026
- kind: exclusion
- driven_by: gifts to a spouse who is not a U.S. citizen
- values: **$194,000** for calendar year 2026 (§§2503 and 2523(i)(2)), in place of the ordinary $19,000 annual exclusion for that spouse.
- shape: Gifts to a non-citizen spouse up to $194,000 in 2026 are excluded; amounts above may be taxable gifts (unlimited marital deduction does not apply to non-citizen spouses).
- indexed: yes
- why_it_matters: Transfers to a non-citizen spouse use a special $194,000 annual exclusion for 2026 instead of the unlimited marital deduction.
- source: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) §4.42(2)
- confidence: high

### Lifetime estate and gift basic exclusion amount (2026) under OBBBA
- id: lifetime_estate_gift_exclusion_2026
- kind: exclusion
- driven_by: decedent dying or donor making taxable gifts in calendar year 2026; prior taxable gifts
- values: OBBBA §70106 sets the basic exclusion amount under §2010(c)(3) to **$15,000,000** for calendar year 2026 (inflation adjustments begin for 2027+). This cancels the scheduled TCJA sunset that would have roughly halved the exclusion for 2026.
- shape: Taxable estate/gifts above the applicable exclusion are taxed; unused exclusion may be portable to a surviving spouse if elected.
- indexed: yes starting after 2026 under OBBBA (2026 base is the statutory $15,000,000)
- why_it_matters: The unified estate and gift exclusion is $15 million per person for 2026, not the lower post-TCJA-sunset amount many earlier projections assumed.
- source: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) (OBBBA discussion §2 / related); [CRS R48611 §70106](https://www.congress.gov/crs_external_products/R/PDF/R48611/R48611.1.pdf)
- confidence: high

### Top estate (and gift) tax rate (2026)
- id: estate_tax_top_rate_2026
- kind: rule
- driven_by: size of the taxable estate / taxable gifts above exclusion
- values: Maximum rate remains **40%** on the amount of the taxable estate (or taxable gifts) over $1,000,000 under the §2001(c) rate schedule (tentative tax $345,800 plus 40% of the excess over $1,000,000). CRS states estates and gifts are taxed at 40% in excess of the lifetime exemption. OBBBA changed the exclusion amount, not the top rate.
- shape: Progressive unified rate schedule up to 40%; exclusion reduces the tax base via the unified credit.
- indexed: no (rate schedule fixed; exclusion indexed)
- why_it_matters: Amounts above the lifetime exclusion remain subject to a top 40% estate and gift tax rate in 2026.
- source: [IRC §2001(c)](https://www.law.cornell.edu/uscode/text/26/2001); [CRS R48611 §70106](https://www.congress.gov/crs_external_products/R/PDF/R48611/R48611.1.pdf)
- confidence: high

### Generation-skipping transfer (GST) tax exemption (2026)
- id: gst_exemption_2026
- kind: exclusion
- driven_by: transferor’s GST transfers in the calendar year; allocation of GST exemption
- values: **$15,000,000** for calendar year 2026 — equal to the basic exclusion amount under §2010(c), per §2631(c) and Rev. Proc. 2025-32’s OBBBA discussion.
- shape: GST exemption allocated to transfers reduces the inclusion ratio; unused exemption is personal to the transferor.
- indexed: yes in tandem with the basic exclusion after 2026 under OBBBA
- why_it_matters: The GST exemption matches the $15 million basic exclusion for 2026.
- source: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) (OBBBA §70106 discussion); [IRC §2631(c)](https://www.law.cornell.edu/uscode/text/26/2631)
- confidence: high

### Kiddie tax thresholds (2026) and custodial brokerage interaction
- id: kiddie_tax_thresholds_2026
- kind: cliff
- driven_by: child’s unearned income; age/student status under §1(g); parental election thresholds
- values: For taxable years beginning in 2026, the amount in §1(g)(4)(A)(ii)(I) is **$1,350**. That amount reduces net unearned income subject to the kiddie tax and is also used for the §1(g)(7) parental election (child’s gross income must be more than $1,350 but less than $13,500). Practically: first $1,350 of child’s unearned income is covered by the limited standard deduction; the next $1,350 is taxed at the child’s rates; unearned income above **$2,700** is taxed at the parents’ rates if §1(g) applies.
- shape: Unearned income ≤ $1,350 → no kiddie-tax net unearned income from that slice. Between $1,350 and $2,700 → child’s rates on the second slice. Above $2,700 → parental rates on the excess when the kiddie tax applies. Custodial brokerage (UTMA/UGMA) dividends, interest, and capital gains are unearned income of the child for this purpose.
- indexed: yes — Rev. Proc. 2025-32
- why_it_matters: Investment income in a custodial brokerage account above $2,700 in 2026 can be taxed at the parent’s marginal rates under the kiddie tax.
- source: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) §4.02; IRC §1(g)
- confidence: high on the $1,350 statutory inflation amount; high on the standard two-slice structure; confirm Form 8615 instructions for edge cases.

### Qualified charitable distribution (QCD) annual limit (2026)
- id: qcd_annual_limit_2026
- kind: limit
- driven_by: IRA owner age 70½+; amount transferred directly to eligible charity
- values: Aggregate QCDs excluded from gross income under §408(d)(8)(A): **$111,000** for 2026 (up from $108,000). One-time election QCDs to a split-interest entity under §408(d)(8)(F): **$55,000** for 2026 (counts against the annual limit).
- shape: Direct IRA-to-charity transfer up to the annual limit is excluded from income and can satisfy RMDs; excess is not a QCD.
- indexed: yes — SECURE 2.0; published in IRS Notice 2025-67
- why_it_matters: An IRA owner age 70½ or older can exclude up to $111,000 of direct charitable IRA transfers from 2026 income.
- source: [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf)
- confidence: high

### Foreign earned income exclusion (2026)
- id: foreign_earned_income_exclusion_2026
- kind: exclusion
- driven_by: qualifying foreign earned income; bona fide residence or physical presence test; election under §911
- values: **$132,900** for taxable years beginning in 2026 (§911(b)(2)(D)(i)).
- shape: Qualifying foreign earned income is excluded up to this ceiling (housing exclusion/deduction is separate).
- indexed: yes
- why_it_matters: A qualifying individual working abroad can exclude up to $132,900 of foreign earned income for 2026.
- source: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) §4.39
- confidence: high

---

## Source index (primary)

| Document | URL |
|---|---|
| Rev. Proc. 2025-32 | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf |
| Rev. Proc. 2025-19 | https://www.irs.gov/pub/irs-drop/rp-25-19.pdf |
| Rev. Proc. 2025-25 | https://www.irs.gov/pub/irs-drop/rp-25-25.pdf |
| Notice 2025-67 | https://www.irs.gov/pub/irs-drop/n-25-67.pdf |
| Notice 2026-05 | https://www.irs.gov/pub/irs-drop/n-26-05.pdf |
| FS-2025-10 | https://www.irs.gov/pub/taxpros/fs-2025-10.pdf |
| IR-2025-127 | https://www.irs.gov/newsroom/irs-updates-frequently-asked-questions-on-the-premium-tax-credit |
| IRS Working Families Tax Cuts | https://www.irs.gov/newsroom/working-families-tax-cuts |
| HHS 2025 poverty guidelines FR | https://www.govinfo.gov/content/pkg/FR-2025-01-17/pdf/2025-01377.pdf |
| Treas. Reg. §1.36B-1 | https://www.law.cornell.edu/cfr/text/26/1.36B-1 |
| CRS R48290 | https://www.congress.gov/crs-product/R48290 |
| CRS R48611 (P.L. 119-21) | https://www.congress.gov/crs_external_products/R/PDF/R48611/R48611.1.pdf |
| Pub. 969 / Pub. 970 / Topic 310 | irs.gov publications and tax topics |
| IRC §§2001, 2631, 529, 6434 | law.cornell.edu US Code |

## Items not fully pinned from a single primary page

1. **Exhaustive list of “recognized postsecondary credential” programs** for OBBBA §70414 — CRS describes categories; implementing regs/IRS lists may refine eligibility.
2. **Whether changing a 529 beneficiary resets the 15-year SECURE 2.0 Roth-rollover clock** — statute is ambiguous; IRS has not issued final clarifying guidance in the materials reviewed.
3. **Whether employer Trump-account contributions always count against the $5,000 individual limit** — CRS notes regulatory clarification may still be needed; IRS page states both limits without an explicit netting sentence in the excerpt used.
4. **Form 8962 draft instructions** still show legacy repayment-limitation table language in places; FS-2025-10 / IR-2025-127 control for tax years after 2025 (no cap).
