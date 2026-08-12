#!/usr/bin/env python3
"""Emit the rule set for index.html, and refuse to emit a broken one.

Two collections come out of this file.

RULES are drawn on the chart. A rule earns a bar only if it has an edge on the
income axis. "Wash sale" and "file an 83(b) within 30 days" are real and
important, and neither has a dollar edge, so neither is a bar. They are notes.

LIMITS are driven by age, not income, so they cannot sit on a dollar axis at
all. They appear in the summary panel instead.

Measures, and why there are six of them:
  taxable    taxable income        ordinary brackets, capital gain bands, QBI
  agi        adjusted gross income charitable ceilings, medical floor
  magi       modified AGI          Roth IRA, NIIT, the new OBBBA deductions
  wages      FICA wages            Additional Medicare Tax, wage base
  amti       alt. minimum taxable  AMT exemption phase-out
  priorwages last year, one employer   mandatory Roth catch-up

Every figure below is tax year 2026 and comes from the corpus in ../research,
which was checked against the primary documents. Sources ride on each rule.
"""

import sys

# ---------------------------------------------------------------- sources ---

S = {
 'iso':     ('IRC 422(d)', 'https://www.law.cornell.edu/uscode/text/26/422'),
 'espp':    ('IRC 423(b)(8)', 'https://www.law.cornell.edu/uscode/text/26/423'),
 'caploss': ('IRC 1211(b)', 'https://www.law.cornell.edu/uscode/text/26/1211'),
 'sec121':  ('IRC 121', 'https://www.law.cornell.edu/uscode/text/26/121'),
 'iso':     ('IRC 422(d)', 'https://www.law.cornell.edu/uscode/text/26/422'),
 'espp':    ('IRC 423(b)(8)', 'https://www.law.cornell.edu/uscode/text/26/423'),
 'caploss': ('IRC 1211(b)', 'https://www.law.cornell.edu/uscode/text/26/1211'),
 'sec121':  ('IRC 121', 'https://www.law.cornell.edu/uscode/text/26/121'),
 'rp2532':   ('Rev. Proc. 2025-32', 'https://www.irs.gov/pub/irs-drop/rp-25-32.pdf'),
 'n2567':    ('Notice 2025-67',     'https://www.irs.gov/pub/irs-drop/n-25-67.pdf'),
 'rp2519':   ('Rev. Proc. 2025-19', 'https://www.irs.gov/pub/irs-drop/rp-25-19.pdf'),
 'rp2525':   ('Rev. Proc. 2025-25', 'https://www.irs.gov/pub/irs-drop/rp-25-25.pdf'),
 's1a':      ('Draft Schedule 1-A', 'https://www.irs.gov/pub/irs-dft/f1040s1a--dft.pdf'),
 'ssacbb':   ('SSA wage base',      'https://www.ssa.gov/oact/cola/cbb.html'),
 'ssacola':  ('SSA 2026 COLA',      'https://www.ssa.gov/news/en/cola/factsheets/2026.html'),
 'niit':     ('IRS: NIIT',          'https://www.irs.gov/individuals/net-investment-income-tax'),
 'addmed':   ('IRS: Additional Medicare Tax', 'https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax'),
 'amt':      ('IRC 55',             'https://www.law.cornell.edu/uscode/text/26/55'),
 'rothira':  ('IRS: Roth IRA limits', 'https://www.irs.gov/retirement-plans/roth-iras'),
 'tradira':  ('IRS: IRA deduction limits', 'https://www.irs.gov/retirement-plans/ira-deduction-limits'),
 'savers':   ('IRS: Saver\u2019s Credit', 'https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-savings-contributions-savers-credit'),
 'ctc':      ('IRS: Child Tax Credit', 'https://www.irs.gov/credits-deductions/individuals/child-tax-credit'),
 'sli':      ('IRS: student loan interest', 'https://www.irs.gov/taxtopics/tc456'),
 'edu':      ('IRS: education credits', 'https://www.irs.gov/credits-deductions/individuals/education-credits-aotc-llc'),
 'qbi':      ('IRS: QBI deduction', 'https://www.irs.gov/newsroom/qualified-business-income-deduction'),
 'salt':     ('IRC 164',            'https://www.law.cornell.edu/uscode/text/26/164'),
 'irmaa':    ('CMS 2026 premiums',  'https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles'),
 'ptc':      ('IRS: premium tax credit', 'https://www.irs.gov/affordable-care-act/individuals-and-families/the-premium-tax-credit-the-basics'),
 'fpl':      ('HHS poverty guidelines', 'https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines'),
 'supp':     ('IRS Pub 15',         'https://www.irs.gov/publications/p15'),
 'estim':    ('IRS: estimated taxes', 'https://www.irs.gov/faqs/estimated-tax'),
 'hsa':      ('IRS: HSA',           'https://www.irs.gov/publications/p969'),
 'ssben':    ('IRC 86',             'https://www.law.cornell.edu/uscode/text/26/86'),
 'itemcap':  ('IRC 68',             'https://www.law.cornell.edu/uscode/text/26/68'),
 'adopt':    ('IRS: adoption credit', 'https://www.irs.gov/taxtopics/tc607'),
 'cdcc':     ('IRS Pub 503',        'https://www.irs.gov/publications/p503'),
}

def src(*keys):
    return [S[k] for k in keys]

# Filing statuses. 'mfj' also stands in for a qualifying surviving spouse.
STATUSES = ['single', 'mfj', 'mfs', 'hoh']

def by(single, mfj, mfs, hoh):
    return {'single': single, 'mfj': mfj, 'mfs': mfs, 'hoh': hoh}

def flat(v):
    return {k: v for k in STATUSES}

# ---------------------------------------------------------------- lanes ---
# One row of the chart. Rules in the same lane never overlap, so they sit on a
# single line as segments. A lane of one is just an ordinary row.
LANES = {
 'ordinary': dict(section='rates', title='Federal tax brackets',
                  short='Tax brackets', order=0, gap='No tax'),
 'ltcg':     dict(section='rates', title='Long-term gain bands',
                  short='Gain bands', order=1, gap='No tax'),
 'irmaa':    dict(section='health', title='Medicare surcharge',
                  short='Medicare', order=40, gap='No surcharge'),
 'care':     dict(section='credits', title='Care credit rate',
                  short='Care credit', order=10, gap=None),
}

# ------------------------------------------------------------------ rules ---

RULES = []

DEFAULT_STATES = {
 'band':     (None, None, None),
 'open':     ('No', 'Yes', None),
 'phaseout': ('Full', 'Reduced', 'None'),
 'step':     ('Full', 'Less each step', 'None'),
 'cliff':    ('Yes', 'No', None),
}

# yes = you have the whole thing. partial = it is shrinking. on = it is in
# force. no = you do not have it. Read left to right: before, inside, after.
DEFAULT_KINDS = {
 'band':     ('band', 'band', 'band'),
 'open':     ('no', 'on', 'on'),
 'phaseout': ('yes', 'partial', 'no'),
 'step':     ('yes', 'partial', 'no'),
 'cliff':    ('no', 'on', 'on'),
}

def rule(**kw):
    kw.setdefault('order', 50)
    kw.setdefault('states', DEFAULT_STATES[kw['shape']])
    kw.setdefault('kinds', DEFAULT_KINDS[kw['shape']])
    RULES.append(kw)

# ---- section: rates --------------------------------------------------------

ORDINARY = {
 'single': [(0,12400,10),(12400,50400,12),(50400,105700,22),(105700,201775,24),
            (201775,256225,32),(256225,640600,35),(640600,None,37)],
 'mfj':    [(0,24800,10),(24800,100800,12),(100800,211400,22),(211400,403550,24),
            (403550,512450,32),(512450,768700,35),(768700,None,37)],
 'mfs':    [(0,12400,10),(12400,50400,12),(50400,105700,22),(105700,201775,24),
            (201775,256225,32),(256225,384350,35),(384350,None,37)],
 'hoh':    [(0,17700,10),(17700,67450,12),(67450,105700,22),(105700,201750,24),
            (201750,256200,32),(256200,640600,35),(640600,None,37)],
}

for i, pct in enumerate([10, 12, 22, 24, 32, 35, 37]):
    rule(
      id='bracket_%d' % pct, section='rates', title='%d%% bracket' % pct, order=i,
      lane='ordinary', seg='%d%%' % pct, states=(None, None, None),
      measure='taxable', shape='open' if pct == 37 else 'band',
      edges={st: (ORDINARY[st][i][0], ORDINARY[st][i][1]) for st in STATUSES},
      d=('A band is a range of income. This rate applies only to the income '
         'inside this band, and not to all of your income. Your first dollars '
         'still pay 10 percent. The band uses taxable income, which is your '
         'income after the standard deduction, or after the deductions you '
         'list yourself.'),
      s=src('rp2532'))

LTCG = {'single': (49450, 545500), 'mfj': (98900, 613700),
        'mfs': (49450, 306850), 'hoh': (66200, 579600)}

rule(id='ltcg_0', section='rates', title='0% capital gains band', order=10, measure='taxable',
     shape='band', edges={st: (0, LTCG[st][0]) for st in STATUSES},
     d=('Long-term gain and qualified dividends pay no tax in this band. The '
        'band uses your total taxable income, and not the gain alone. Your '
        'other income fills the band first. Only the room that is left holds '
        'gain at zero.'),
     s=src('rp2532'))
rule(id='ltcg_15', section='rates', title='15% capital gains band', order=11, measure='taxable',
     shape='band', edges={st: LTCG[st] for st in STATUSES},
     d=('Long-term gain and qualified dividends pay 15 percent in this band. '
        'To get this rate you must own the asset for more than one year. A '
        'gain on an asset you owned for one year or less pays your normal '
        'income tax rate instead.'),
     s=src('rp2532'))
rule(id='ltcg_20', section='rates', title='20% capital gains band', order=12, measure='taxable',
     shape='open', edges={st: (LTCG[st][1], None) for st in STATUSES},
     d=('Long-term gain more than this point is taxed at 20 percent. The Net '
    'Investment Income Tax of 3.8 percent can apply to the same gain. The two '
    'use different measures of income, so the real rate becomes 23.8 percent.'),
     s=src('rp2532', 'niit'))

rule(id='niit', section='rates', title='Net Investment Income Tax', order=30, measure='magi',
     shape='open', edges=by((200000, None), (250000, None), (125000, None), (200000, None)),
     d=('A tax of 3.8 percent on investment income. It applies to the smaller of '
    'two amounts: your net investment income, or the amount of MAGI more than '
    'the threshold. MAGI is your adjusted gross income with a few items added '
    'back. The tax grows with that excess. It does not start at the full rate '
    'on the first dollar. The threshold was never raised for inflation, so '
    'more people cross it each year.'),
     s=src('niit'))

rule(id='addl_medicare', section='rates', title='Additional Medicare Tax', order=21, measure='wages',
     shape='open', edges=by((200000, None), (250000, None), (125000, None), (200000, None)),
     d=('An extra 0.9 percent on wages more than the threshold. Only the excess '
    'is taxed. Your employer begins to take it from your pay at $200,000 from '
    'that employer. Your filing status does not change that point. A two- '
    'earner couple can therefore have too little taken, and can owe the tax '
    'when they file. A qualifying surviving spouse uses the $200,000 figure here, not the joint figure.'),
     s=src('addmed'))

rule(id='ss_wage_base', section='rates', title='Social Security wage base', order=20, measure='wages',
     shape='band', edges=flat((0, 184500)),
     d=('Social Security tax of 6.2 percent applies to wages up to this point. '
    'Wages more than this point pay none. The ceiling is per employer, not '
    'per person. If you change jobs during the year, both employers take the '
    'tax up to the full base. You then claim the excess as a credit.'),
     s=src('ssacbb'))

rule(id='amt_phaseout', section='rates', title='AMT exemption phase-out', order=31, measure='amti',
     shape='phaseout',
     edges=by((500000, 680200), (1000000, 1280400), (500000, 640200), (500000, 680200)),
     d=('The Alternative Minimum Tax is a second calculation that can raise what '
    'you owe. Its exemption shrinks by 50 cents for each dollar more than the '
    'start. The exemption reaches zero after a short range. The 2025 law '
    'moved the start down and doubled the rate from 25 percent. When you buy '
    'shares under an incentive stock option, the discount adds to this '
    'measure. That is why this matters most in the year you buy.'),
     s=src('rp2532', 'amt'))

rule(id='supplemental_million', section='rates', title='37% supplemental withholding', order=22,
     measure='supplemental', shape='open', needs='supp', edges=flat((1000000, None)),
     d=('Bonuses and vesting stock are taxed at a flat 22 percent until they pass '
    '$1,000,000 for the year. After that the rate is 37 percent. Vesting '
    'stock is stock that becomes yours this year. Twenty-two percent is less '
    'than the rate most people at this income pay. That is why a large vest '
    'often leaves a bill when you file.'),
     s=src('supp'))

# ---- section: accounts -----------------------------------------------------

rule(id='roth_ira', section='accounts', title='Roth IRA phase-out', measure='magi',
     shape='phaseout',
     edges=by((153000, 168000), (242000, 252000), (0, 10000), (153000, 168000)),
     d=('A Roth IRA takes money you already paid tax on, and the growth can be '
    'tax free later. After the start you can contribute less than the full '
    'amount. After the end you cannot contribute directly at all. Married '
    'filing separately runs from zero to $10,000. Almost nobody who files '
    'that way can contribute. A married person who files separately, and who lived apart from their spouse for the whole year, uses the single range instead.'),
     s=src('n2567', 'rothira'))

rule(id='trad_ira_deduction', section='accounts', title='IRA deduction phase-out',
     measure='magi', shape='phaseout',
     edges=by((81000, 91000), (129000, 149000), (0, 10000), (81000, 91000)),
     d=('This range applies when a workplace retirement plan covers you. After '
    'the end you can still contribute, but you cannot deduct it. If no plan '
    'covers you, there is no income limit at all. A married person who files separately, and who lived apart from their spouse for the whole year, uses the single range instead.'),
     s=src('n2567', 'tradira'))

rule(id='roth_catch_up', section='accounts', age_min=50, title='Roth catch-up required',
     measure='priorwages', shape='cliff', edges=flat((150000, None)),
     d=('New for 2026. Catch-up is the extra amount a person aged 50 or over can '
    'contribute. Roth means you pay the tax now, and the growth can be tax '
    'free later. Say you earned more than this last year from the employer '
    'that sponsors your plan. All of your catch-up must then be Roth. This '
    'edge does not move with the slider, because it reads last year and one '
    'employer. If the plan has no Roth option, your catch-up is zero.'),
     s=src('n2567'))

rule(id='hce', section='accounts', title='Highly compensated employee',
     measure='priorwages', shape='cliff', edges=flat((160000, None)),
     d=('If you earn more than this, your plan treats you as highly compensated. '
    'Testing rules can then cap your contribution. Some plans refund part of '
    'it after year end. The test reads last year’s pay.'),
     s=src('n2567'))

SAVERS = {
 'iso':     ('IRC 422(d)', 'https://www.law.cornell.edu/uscode/text/26/422'),
 'espp':    ('IRC 423(b)(8)', 'https://www.law.cornell.edu/uscode/text/26/423'),
 'caploss': ('IRC 1211(b)', 'https://www.law.cornell.edu/uscode/text/26/1211'),
 'sec121':  ('IRC 121', 'https://www.law.cornell.edu/uscode/text/26/121'),'single': 40250, 'mfj': 80500, 'mfs': 40250, 'hoh': 60375}
rule(id='savers_credit', section='accounts', title='Saver\u2019s Credit',
     measure='agi', shape='step', edges={st: (0, SAVERS[st]) for st in STATUSES},
     d=('A credit worth 50, 20, or 10 percent of what you contribute to a '
    'retirement account, on the first $2,000. The rate drops in steps and '
    'does not slide. One dollar of extra income can therefore cut the credit '
    'sharply. The credit ends at the top of this band.'),
     s=src('savers', 'rp2532'))

# ---- section: deductions ---------------------------------------------------

rule(id='salt_phasedown', section='deductions', title='SALT cap phase-out', measure='magi',
     shape='phaseout', floor=True,
     edges=by((505000, 606333), (505000, 606333), (252500, 303167), (505000, 606333)),
     d=('SALT means state and local tax. The cap on that deduction is $40,400 for '
    '2026, far more than the old $10,000. After the start the cap falls by 30 '
    'cents for each dollar of income. The floor is $10,000.'),
     s=src('salt', 'rp2532'))

rule(id='qbi_phasein', section='deductions', title='QBI deduction limits', measure='taxable',
     shape='phaseout',
     edges=by((201750, 276750), (403500, 553500), (201775, 276775), (201750, 276750)),
     d=('QBI means qualified business income. Under the start, the 20 percent '
    'deduction on that income has no wage test and no restriction on the type '
    'of work. Across this range a limit based on the wages the business pays '
    'takes effect. For professional service work the deduction disappears '
    'completely.'),
     s=src('qbi'))

rule(id='senior_deduction', section='deductions', title='Senior deduction phase-out',
     measure='magi', shape='phaseout', age_min=65,
     edges=by((75000, 175000), (150000, 250000), (None, None), (75000, 175000)),
     d=('A deduction of $6,000 for each person aged 65 or over. It is separate '
    'from the extra standard deduction for age. It falls by 6 cents for each '
    'dollar more than the start. A couple where both qualify get two of them, '
    'and both reach zero at the same income. It ends after 2028.'),
     s=src('s1a', 'rp2532'))

rule(id='tips_deduction', section='deductions', title='Tips deduction phase-out',
     measure='magi', shape='step', needs='tips',
     edges=by((150000, None), (300000, None), (None, None), (150000, None)),
     d=('Up to $25,000 of tip income is deductible. After the start it falls by '
    '$100 for each full $1,000 of income, so it drops in steps and does not '
    'slide. Where it reaches zero depends on how much you earned in tips. It '
    'does not depend on the cap. It ends after 2028.'),
     s=src('s1a'))

rule(id='overtime_deduction', section='deductions', title='Overtime deduction phase-out',
     measure='magi', shape='step', needs='overtime',
     edges=by((150000, None), (300000, None), (None, None), (150000, None)),
     d=('Up to $12,500 of overtime pay is deductible, or $25,000 on a joint '
    'return. It falls by $100 for each full $1,000 of income more than the '
    'start, in steps. It ends after 2028.'),
     s=src('s1a'))

rule(id='car_loan_deduction', section='deductions', title='Car loan interest phase-out',
     measure='magi', shape='step', needs='carloan',
     edges=by((100000, None), (200000, None), (None, None), (100000, None)),
     d=('Up to $10,000 of interest on a loan for a new car assembled in the '
    'United States. It falls by $200 for each $1,000 of income more than the '
    'start. This one rounds the income up rather than down, so you lose the '
    'deduction one step sooner. It ends after 2028.'),
     s=src('s1a'))

rule(id='student_loan_interest', section='deductions', title='Student loan interest phase-out',
     measure='magi', shape='phaseout',
     edges=by((85000, 100000), (175000, 205000), (None, None), (85000, 100000)),
     d=('Up to $2,500 of student loan interest is deductible without itemizing. '
        'The deduction slides to zero across this range. Married filing '
        'separately cannot claim it at all.'),
     s=src('sli'))

rule(id='itemized_top_limit', section='deductions', title='Itemized deduction limit',
     measure='taxable', shape='open',
     edges=by((640600, None), (768700, None), (384350, None), (640600, None)),
     d=('To itemize is to list your deductions instead of taking the standard '
    'deduction. Once you reach the top bracket, your itemized deductions are '
    'cut by about 5.4 percent of the amount more than this point. The effect '
    'is to cap their value at 35 cents in the dollar rather than 37. The test adds your itemized deductions back before it compares, so it can start earlier than this bar shows.'),
     s=src('itemcap'))

# ---- section: credits ------------------------------------------------------

rule(id='ctc_phaseout', section='credits', title='Child Tax Credit phase-out', measure='magi',
     shape='step', needs='children',
     edges=by((200000, None), (400000, None), (200000, None), (200000, None)),
     d=('The credit is $2,200 for each qualifying child. After the start it falls '
    'by $50 for each $1,000 of income. Where the credit reaches zero depends '
    'on how many children you have. The end of this band therefore moves with '
    'your family, and it is not a fixed amount.'),
     s=src('ctc', 'rp2532'))

rule(id='education_credits', section='credits', title='Education credits phase-out',
     measure='magi', shape='phaseout',
     edges=by((80000, 90000), (160000, 180000), (None, None), (80000, 90000)),
     d=('Both education credits use the same range. The American Opportunity '
        'credit is worth up to $2,500 per student and the Lifetime Learning '
        'credit up to $2,000 per return. Neither is available to a person who '
        'files separately.'),
     s=src('edu'))

rule(id='adoption_credit', section='credits', title='Adoption credit phase-out',
     measure='magi', shape='phaseout',
     edges=flat((265080, 305080)),
     d=('The credit is up to $17,670 for each child you adopt. Of that amount, '
    '$5,120 is refundable, so you can receive it even if you owe no tax. The '
    'credit slides to zero across this range.'),
     s=src('adopt', 'rp2532'))

rule(id='cdcc_rate', section='credits', title='Care credit rate falls',
     short='Care credit', measure='agi', shape='step', floor=True,
     edges=by((15000, 43001), (15000, 43001), (15000, 43001), (15000, 43001)),
     d=('The child and dependent care credit starts at 50 percent of what you '
        'spend. It falls one point for every $2,000 of income more than '
        '$15,000. It stops at 35 percent. The rate then holds at 35 percent '
        'until the second fall starts.'),
     s=src('cdcc'), order=0)

rule(id='cdcc_rate_2', section='credits', title='Care credit falls again',
     short='Care credit 2', measure='agi', shape='step', floor=True,
     edges=by((75000, 103001), (150000, 206001), (75000, 103001), (75000, 103001)),
     d=('The second fall takes the care credit rate from 35 percent to 20 '
        'percent. It drops one point for every $2,000 of income more than '
        '$75,000. On a joint return it drops one point for every $4,000 more '
        'than $150,000. The rate stops at 20 percent and stays there.'),
     s=src('cdcc'), order=1)

# ---- section: health -------------------------------------------------------

rule(id='ss_earnings_test', section='health', title='Social Security earnings test',
     measure='wages', shape='open', age_min=62, age_max=66, needs='ssben',
     edges=flat((24480, None)),
     d=('Full retirement age is the age at which you can draw your whole benefit. '
    'Say you draw Social Security before that age and you still work. SSA '
    'then keeps back $1 of benefit for each $2 you earn more than this point. '
    'The money is not lost. SSA raises your benefit again when you reach full '
    'retirement age.'),
     s=src('ssacola'))


rule(id='aca_cliff', section='health', title='ACA subsidy cliff', measure='magiTei',
     shape='cliff', needs='ownplan',
     edges=flat((62600, None)),  # 400% of FPL, household of one; scaled at runtime
     d=('This is the sharpest edge in the tax code, and it returned for 2026. If '
    'your income is less than 400 percent of the poverty level, you can get '
    'help to pay for a health plan you buy yourself. One dollar more and you '
    'get nothing. The 2025 law also removed the cap on repaying help you '
    'already received.'),
     s=src('ptc', 'fpl', 'rp2525'))

IRMAA = [(109000, 218000, 81.20, 14.50), (137000, 274000, 202.90, 37.50),
         (171000, 342000, 324.60, 60.40), (205000, 410000, 446.30, 83.30),
         (500000, 750000, 487.00, 91.00)]
# A separate return has three steps: nothing, then the fourth surcharge from
# $109,000, then the fifth from $391,000. Tiers one to three do not exist.
IRMAA_MFS = {
 'iso':     ('IRC 422(d)', 'https://www.law.cornell.edu/uscode/text/26/422'),
 'espp':    ('IRC 423(b)(8)', 'https://www.law.cornell.edu/uscode/text/26/423'),
 'caploss': ('IRC 1211(b)', 'https://www.law.cornell.edu/uscode/text/26/1211'),
 'sec121':  ('IRC 121', 'https://www.law.cornell.edu/uscode/text/26/121'),3: 109000, 4: 391000}
for i, (s1, mj, partb, partd) in enumerate(IRMAA):
    rule(id='irmaa_%d' % (i + 1), section='health',
         title='Medicare surcharge, tier %d' % (i + 1),
         measure='magiTei', shape='cliff', age_min=63,
         edges=by((s1, None), (mj, None), (IRMAA_MFS.get(i), None), (s1, None)),
         d=('After this point Medicare charges $%.2f more each month for Part B '
            'and $%.2f more for Part D, for each person. Every tier is a hard '
            'edge and not a slope. One dollar can therefore cost hundreds over '
            'a year. It reads your income from two years earlier, so what you '
            'earn now sets your premium at 65.' % (partb, partd)),
         s=src('irmaa'))

rule(id='ss_benefit_tax_mfs', section='health',
     title='Benefits taxed, separate return', short='SS, separate',
     measure='provisional', shape='open', age_min=62, needs='ssben',
     edges=by((None, None), (None, None), (0, None), (None, None)),
     d=('A married person who files separately, and who lived with their spouse '
        'at any time in the year, gets no threshold. Up to 85 percent of the '
        'benefit is taxable from the first dollar. This is the hardest version '
        'of the rule. Living apart for the whole year moves you to the single '
        'thresholds instead.'),
     s=src('ssben'), order=1)

rule(id='ss_benefit_tax', section='health', title='Social Security benefits taxed',
     measure='provisional', shape='phaseout', age_min=62, needs='ssben',
     edges=by((25000, 34000), (32000, 44000), (None, None), (25000, 34000)),
     d=('Part of your Social Security benefit becomes taxable after these points. '
    'Up to half is taxed in the lower band and up to 85 percent after it. '
    'These figures were set in 1983 and 1993, and they were never raised for '
    'inflation. A married person who files separately and lived with their '
    'spouse gets no threshold. For that person, up to 85 percent is taxable '
    'from the first dollar.'),
     s=src('ssben'))

# The audit found these absent. Each one binds for a salaried person at a
# large employer, which is the reader this page is for.

rule(id='comp_limit', section='accounts', title='Pay a plan can count',
     short='Plan pay cap', measure='wages', shape='open',
     edges=by((360000, None), (360000, None), (360000, None), (360000, None)),
     d=('A retirement plan cannot count pay of more than $360,000 for the year. '
        'Pay more than this earns no further employer match, and it does not '
        'raise a contribution that is set as a percent of pay. A person who '
        'earns more than this gets the whole match earlier in the year.'),
     s=src('n2567'), order=5)

rule(id='amt_rate_step', section='rates', title='AMT rate steps to 28%',
     short='AMT 28% step', measure='amti', shape='open',
     edges=by((334600, None), (384700, None), (192350, None), (334600, None)),
     d=('The alternative minimum tax charges 26 percent, then 28 percent past '
        'this point. The step is on income more than $244,500, or $122,250 on '
        'a separate return, after the exemption. The figures here add the full '
        'exemption back, so the step reads on the same measure as the '
        'exemption phase-out.'),
     s=src('rp2532'), order=9)

# ---- section: filing -------------------------------------------------------

rule(id='estimated_110', section='filing', title='110% safe harbor', measure='agi',
     shape='open', edges=by((150000, None), (150000, None), (75000, None), (150000, None)),
     d=('To avoid a penalty you normally pay 100 percent of last year’s tax '
    'during the year. If your income is more than this, the figure rises to '
    '110 percent. The rule is called a safe harbor. It catches people in the '
    'year after a large vest or a large gain.'),
     s=src('estim'))

# ------------------------------------------------------ age-driven limits ---
# These have no edge on a dollar axis, so they are not bars. They are computed
# from age and shown in the summary panel.

LIMITS = [
 dict(id='stdded', group='take', title='Standard deduction',
      base=by(16100, 32200, 16100, 24150), catch={},
      d=('What you subtract before the brackets apply, if you do not itemize. '
         'A person aged 65 or over adds more, and a blind person adds the same '
         'amount again.'),
      s=src('rp2532')),
 dict(id='aged', group='take', title='Extra deduction at 65',
      base=by(2050, 1650, 1650, 2050), catch={}, ageMin=65,
      d=('On top of the standard deduction, and separate from the $6,000 senior '
         'deduction that the 2025 law added. A blind person adds the same amount '
         'a second time.'),
      s=src('rp2532')),
 dict(id='deferral', group='put', title='401(k) and 403(b) deferral', base=24500,
      catch={50: 8000, 60: 11250, 64: 8000},
      d=('The most you can contribute to a workplace plan from your own pay. '
    'Employer money does not count against this. The extra amount allowed at '
    '50 rises again for the four years from 60 to 63, then drops back at 64.'),
      s=src('n2567')),
 dict(id='ira', group='put', title='IRA contribution', base=7500, catch={50: 1100},
      d=('One limit across every traditional and Roth IRA you own. It is not a '
    'limit for each account. You need earned income at least equal to the '
    'amount you contribute.'),
      s=src('n2567')),
 dict(id='hsa_self', group='put', title='HSA, self-only cover', base=4400, catch={55: 1000},
      needs='hdhp',
      d=('Only available with a qualifying high-deductible plan. Employer money '
         'counts against this limit. Contributions can no longer be made once '
         'Medicare starts.'),
      s=src('rp2519')),
 dict(id='hsa_family', group='put', title='HSA, family cover', base=8750, catch={55: 1000},
      needs='hdhp',
      d=('Only available with a qualifying high-deductible plan. The extra at 55 '
         'is per person, so two spouses need two accounts to claim it twice.'),
      s=src('rp2519')),
 dict(id='fsa', group='put', title='Health FSA', base=3400, catch={},
      d=('Money set aside for medical costs, from your pay before tax. If you have '
    'a general-purpose FSA, you cannot contribute to an HSA.'),
      s=src('rp2532')),
 dict(id='dcfsa', group='put', title='Dependent care FSA',
     base={'single':7500,'mfj':7500,'mfs':3750,'hoh':7500}, catch={},
      d=('Raised from $5,000 for 2026, the first change since 1986. It is a '
         'household limit, not a per-person one.'),
      s=src('rp2532')),
 dict(id='additions', group='put', title='Total 401(k) additions', base=72000, catch={},
      d=('Everything that can land in the plan for you in one year: your own '
    'contribution, the employer match, and after-tax money. Catch-up sits '
    'outside this. The gap between this limit and your own contribution is '
    'the room for a large after-tax contribution. Some plans let that money '
    'move to a Roth account later.'),
      s=src('n2567')),
 dict(id='simple', group='put', title='SIMPLE IRA deferral', base=17000,
      catch={50: 4000},
      d=('A smaller workplace plan, common at small employers. A plan for an '
         'employer with 25 or fewer people can use a higher limit of $18,100.'),
      s=src('n2567')),
 dict(id='qcd', group='give', title='Charity gift from an IRA', base=111000, catch={}, ageMin=70,
      d=('From age 70 and a half you can send money straight from an IRA to a '
    'charity. The gift is not part of your income, so it does not raise any '
    'income measure on this page. It also counts toward the minimum amount '
    'you must take from the IRA each year.'),
      s=src('n2567')),
 dict(id='gift', group='give', title='Gift to one person, tax free', base=19000, catch={},
      d=('You can give this much to any one person in the year with no gift tax '
    'return. It does not reduce the lifetime amount you can give before gift '
    'tax applies. A married couple can give twice this to the same person.'),
      s=src('rp2532')),

 # The audit found these four absent. Every one of them binds for a salaried
 # person at a large employer, which is the reader this page is for.
 dict(id='iso_100k', group='put', title='ISO that can vest in a year',
      base=100000, catch={},
      d=('An incentive stock option keeps its tax treatment only up to $100,000 '
         'of grant-date value that can first be exercised in one year. The part '
         'more than this becomes a normal option. That part is taxed as pay at '
         'exercise, with withholding, and not as an AMT item.'),
      s=src('iso')),
 dict(id='espp_25k', group='put', title='ESPP purchase in a year',
      base=25000, catch={},
      d=('A share purchase plan under section 423 lets you buy up to $25,000 of '
         'stock in a year. The figure uses the price on the day of the grant, '
         'not the price you pay. So the number of shares is fixed at the grant, '
         'even when the purchase price is lower.'),
      s=src('espp')),
 dict(id='cap_loss', group='take', title='Capital loss against pay',
      base={'single':3000,'mfj':3000,'mfs':1500,'hoh':3000}, catch={},
      d=('A net capital loss offsets capital gain without limit. What is left '
         'can reduce other income by $3,000 a year, or $1,500 on a separate '
         'return. The rest carries forward to later years, and it keeps its '
         'character as long-term or short-term.'),
      s=src('caploss')),
 dict(id='home_sale', group='take', title='Gain on a main home',
      base={'single':250000,'mfj':500000,'mfs':250000,'hoh':250000}, catch={},
      d=('Gain on the sale of a main home is not taxed up to this amount. You '
         'must have owned the home, and lived in it as your main home, for two '
         'of the five years before the sale. Neither figure rises with '
         'inflation. The gain you exclude also stays outside the investment tax.'),
      s=src('sec121')),
]

# A phone gives a label about eighteen characters before it is cut off, so the
# longer titles carry a short form. Anything not listed here already fits.
SHORT = {'ltcg_0': '0% gains band', 'ltcg_15': '15% gains band', 'ltcg_20': '20% gains band', 'niit': 'Investment tax', 'addl_medicare': 'Extra Medicare tax', 'ss_wage_base': 'SS wage base', 'amt_phaseout': 'AMT exemption', 'supplemental_million': '37% withholding', 'roth_ira': 'Roth IRA', 'trad_ira_deduction': 'IRA deduction', 'roth_catch_up': 'Roth catch-up', 'hce': 'Highly compensated', 'savers_credit': 'Saver’s Credit', 'salt_phasedown': 'SALT cap', 'qbi_phasein': 'QBI limits', 'senior_deduction': 'Senior deduction', 'tips_deduction': 'Tips deduction', 'overtime_deduction': 'Overtime deduction', 'car_loan_deduction': 'Car loan interest', 'student_loan_interest': 'Student loan', 'itemized_top_limit': 'Itemized limit', 'ctc_phaseout': 'Child Tax Credit', 'education_credits': 'Education credits', 'adoption_credit': 'Adoption credit', 'cdcc_rate': 'Care credit', 'aca_cliff': 'ACA cliff', 'ss_benefit_tax': 'SS benefits taxed', 'ss_earnings_test': 'SS earnings test', 'irmaa_1': 'Surcharge tier 1', 'irmaa_2': 'Surcharge tier 2', 'irmaa_3': 'Surcharge tier 3', 'irmaa_4': 'Surcharge tier 4', 'irmaa_5': 'Surcharge tier 5'}

for _r in RULES:
    if _r['id'] in SHORT:
        _r['short'] = SHORT[_r['id']]

# Lane membership and the wording of each segment, kept in one table so the
# chart reads the same way for every rule.
SEGMENTS = {
 'ltcg_0': dict(lane='ltcg', seg='0%', states=(None, None, None)),
 'ltcg_15': dict(lane='ltcg', seg='15%', states=(None, None, None)),
 'ltcg_20': dict(lane='ltcg', seg='20%', states=(None, None, None)),
 'irmaa_1': dict(lane='irmaa', seg='Tier 1', states=(None, 'Tier 1', None)),
 'irmaa_2': dict(lane='irmaa', seg='Tier 2', states=(None, 'Tier 2', None)),
 'irmaa_3': dict(lane='irmaa', seg='Tier 3', states=(None, 'Tier 3', None)),
 'irmaa_4': dict(lane='irmaa', seg='Tier 4', states=(None, 'Tier 4', None)),
 'irmaa_5': dict(lane='irmaa', seg='Tier 5', states=(None, 'Tier 5', None)),
 'cdcc_rate': dict(lane='care', seg='50 to 35%', states=(None, '50 to 35%', None)),
 'cdcc_rate_2': dict(lane='care', seg='35 to 20%', states=(None, '35 to 20%', None)),
 'roth_ira': dict(states=('Full amount', 'Reduced', 'Not allowed')),
 'trad_ira_deduction': dict(states=('Full deduction', 'Reduced', 'None')),
 'student_loan_interest': dict(states=('Full deduction', 'Reduced', 'None')),
 'education_credits': dict(states=('Full credit', 'Reduced', 'None')),
 'adoption_credit': dict(states=('Full credit', 'Reduced', 'None')),
 'ctc_phaseout': dict(states=('Full credit', 'Less each step', 'None')),
 'savers_credit': dict(states=('Credit', 'Less each step', 'None')),
 'senior_deduction': dict(states=('Full $6,000', 'Reduced', 'None')),
 'tips_deduction': dict(states=('Full deduction', 'Less each step', 'None')),
 'overtime_deduction': dict(states=('Full deduction', 'Less each step', 'None')),
 'car_loan_deduction': dict(states=('Full deduction', 'Less each step', 'None')),
 'amt_phaseout': dict(states=('Full exemption', 'Reduced', 'None')),
 'salt_phasedown': dict(states=('Full $40,400', 'Less each step', '$10,000 floor')),
 'qbi_phasein': dict(states=('No limit', 'Limits arrive', 'Limits apply')),
 'niit': dict(states=('No', 'Applies', None)),
 'addl_medicare': dict(states=('No', 'Applies', None)),
 'ss_wage_base': dict(states=(None, 'Taxed', 'No more tax')),
 'supplemental_million': dict(states=('22%', '37%', None)),
 'itemized_top_limit': dict(states=('No limit', 'Limit applies', None)),
 'comp_limit': dict(states=('Pay counts', 'No longer counts', None)),
 'amt_rate_step': dict(states=('26%', '28%', None)),
 'estimated_110': dict(states=('100% is enough', '110% needed', None)),
 'ss_earnings_test': dict(states=('Keep it all', 'Part withheld', None)),
 'roth_catch_up': dict(states=('Either kind', 'Roth only', None)),
 'hce': dict(states=('No', 'Highly paid', None)),
 'aca_cliff': dict(states=('Help available', 'No help', None)),
 'ss_benefit_tax': dict(states=('None taxed', 'Up to 50%', 'Up to 85%')),
 'ss_benefit_tax_mfs': dict(states=(None, 'Up to 85%', None)),
}

for _r in RULES:
    _r.update(SEGMENTS.get(_r['id'], {}))

# Where a fill would otherwise read the wrong way round.
KINDS = {
 'aca_cliff': ('yes', 'no', None),
 'ss_wage_base': ('band', 'on', 'no'),
 'supplemental_million': ('band', 'on', None),
 'amt_rate_step': ('band', 'on', None),
 'estimated_110': ('yes', 'on', None),
 'ss_earnings_test': ('yes', 'on', None),
 'comp_limit': ('yes', 'no', None),
 'itemized_top_limit': ('yes', 'on', None),
 'roth_catch_up': ('yes', 'on', None),
 'qbi_phasein': ('yes', 'partial', 'on'),
 'salt_phasedown': ('yes', 'partial', 'on'),
 'ss_benefit_tax': ('yes', 'partial', 'on'),
 'ss_benefit_tax_mfs': (None, 'on', None),
}

for _r in RULES:
    if _r['id'] in KINDS: _r['kinds'] = KINDS[_r['id']]

# Why a rule is not drawn, phrased for the reader. The page shows these
# instead of leaving a section silently empty.
NEEDS_REASON = {
 'tips':     'tip income',
 'overtime': 'overtime pay',
 'carloan':  'car loan interest',
 'children': 'a child under 17',
 'ownplan':  'your own health plan',
 'ssben':    'a Social Security benefit',
 'supp':     'a bonus or vesting stock',
}

# --------------------------------------------------------------- emitters ---

def js(v):
    if v is None: return 'null'
    if isinstance(v, bool): return 'true' if v else 'false'
    if isinstance(v, (int, float)): return repr(v)
    return '"' + str(v).replace('\\', '\\\\').replace('"', '\\"') + '"'

def emit():
    out = ['const RULES = [']
    for r in RULES:
        e = ','.join('%s:[%s,%s]' % (st, js(r['edges'][st][0]), js(r['edges'][st][1]))
                     for st in STATUSES)
        out.append('  {id:%s, sec:%s, t:%s, m:%s, shape:%s, o:%d,'
                   % (js(r['id']), js(r['section']), js(r['title']),
                      js(r['measure']), js(r['shape']), r['order']))
        out.append('   e:{%s},' % e)
        if r.get('short'): out.append('   st:%s,' % js(r['short']))
        if r.get('age_min'): out.append('   ageMin:%d,' % r['age_min'])
        if r.get('age_max'): out.append('   ageMax:%d,' % r['age_max'])
        if r.get('needs'):   out.append('   needs:%s,' % js(r['needs']))
        if r.get('floor'):   out.append('   floor:true,')
        if r.get('lane'):    out.append('   lane:%s,' % js(r['lane']))
        if r.get('seg'):     out.append('   sg:%s,' % js(r['seg']))
        out.append('   sv:[%s],' % ','.join(js(x) for x in r['states']))
        out.append('   sk:[%s],' % ','.join(js(x) for x in r['kinds']))
        out.append('   d:%s,' % js(r['d']))
        out.append('   s:[%s]},' % ','.join('[%s,%s]' % (js(a), js(b)) for a, b in r['s']))
    out.append('];')
    out.append('')
    out.append('const LANES = {')
    for lid, l in LANES.items():
        out.append('  %s:{t:%s, st:%s, sec:%s, o:%d, gap:%s},'
                   % (lid, js(l['title']), js(l['short']), js(l['section']),
                      l['order'], js(l['gap'])))
    out.append('};')
    out.append('')
    out.append('const NEEDS_REASON = {%s};'
               % ','.join('%s:%s' % (js(k), js(v))
                          for k, v in sorted(NEEDS_REASON.items())))
    out.append('')
    out.append('/* Driven by age, not by income, so these are not bars. */')
    out.append('const LIMITS = [')
    for l in LIMITS:
        c = ','.join('%d:%d' % (k, v) for k, v in sorted(l['catch'].items()))
        b = l['base']
        bj = ('{%s}' % ','.join('%s:%d' % (k, b[k]) for k in STATUSES)
              if isinstance(b, dict) else str(b))
        out.append('  {id:%s, t:%s, base:%s, catch:{%s}, g:%s,'
                   % (js(l['id']), js(l['title']), bj, c, js(l['group'])))
        if l.get('ageMin'): out.append('   ageMin:%d,' % l['ageMin'])
        if l.get('needs'): out.append('   needs:%s,' % js(l['needs']))
        out.append('   d:%s,' % js(l['d']))
        out.append('   s:[%s]},' % ','.join('[%s,%s]' % (js(a), js(b)) for a, b in l['s']))
    out.append('];')
    return '\n'.join(out)

# Words and forms that ASD-STE100 does not allow, with what to write instead.
# "above" and "below" are for physical position, not for amounts. The -ing
# forms are verbs here, which the standard reserves for nouns. The rest are
# phrasal verbs, which do not survive translation and are hard for a reader
# whose first language is not English.
BANNED = [
 (' above ',       'more than'),
 (' below ',       'less than'),
 ('has never',     'simple past'),
 ('have never',    'simple past'),
 ('starts withhold', 'begins to take'),
 (' starting',     'a simple verb'),
 ('shrinking',     'shrinks'),
 (' falling',      'falls'),
 ('keep working',  'you still work'),
 ('holds back',    'keeps back'),
 ('contributing',  'you contribute'),
 ('using up',      'a reduction of'),
 ('put in',        'contribute'),
 ('put into',      'contribute to'),
 ('work out',      'calculate'),
 ('fills in',      'appears'),
 ('comes out',     'is removed'),
 ('push up',       'raise'),
 ('lands in',      'is part of'),
 ('go in as',      'be'),
 ('come back to you', 'return to you'),
 ('claim the excess back', 'claim the excess'),
 ('shuts out',     'cannot contribute'),
 ('for good',      'delete it'),
 ('haircut',       'limit'),
]
MAX_WORDS = 25

def language_problems(where, text):
    """Flag the STE breaks that a reviewer found, so they cannot come back."""
    out = []
    low = ' ' + text.lower() + ' '
    for word, better in BANNED:
        if word in low:
            out.append('%s: %r is not allowed, use %s' % (where, word.strip(), better))
    import re as _re
    for sentence in _re.split(r'(?<=[.!?]) +', text):
        n = len(sentence.split())
        if n > MAX_WORDS:
            out.append('%s: sentence of %d words, limit is %d: %r'
                       % (where, n, MAX_WORDS, sentence[:70]))
    return out

RULE_KEYS = {'id','section','title','measure','shape','edges','d','s','order',
             'age_min','age_max','needs','short','floor','lane','seg','states','kinds'}
LIMIT_KEYS = {'id','title','base','catch','d','s','ageMin','needs','group'}

def check():
    bad = []
    for r in RULES:
        bad += language_problems('rule ' + r['id'], r['d'])
        for lab in list(r['states']) + [r.get('seg')]:
            if lab:
                bad += [b for b in language_problems('label ' + r['id'], lab)
                        if 'sentence of' not in b]
        bad += [b for b in language_problems('title ' + r['id'], r['title'])
                if 'sentence of' not in b]
        if r.get('short'):
            bad += [b for b in language_problems('short ' + r['id'], r['short'])
                    if 'sentence of' not in b]
    for l in LIMITS:
        bad += language_problems('limit ' + l['id'], l['d'])
        bad += [b for b in language_problems('limit title ' + l['id'], l['title'])
                if 'sentence of' not in b]
    for r in RULES:
        for k in set(r) - RULE_KEYS:
            bad.append('rule %s has an unknown key %r' % (r['id'], k))
    for l in LIMITS:
        for k in set(l) - LIMIT_KEYS:
            bad.append('limit %s has an unknown key %r' % (l['id'], k))
    seen = set()
    for r in RULES:
        if r['id'] in seen: bad.append('duplicate id: ' + r['id'])
        seen.add(r['id'])
        if len(r['title']) > 34:
            bad.append('title too long (%d): %s' % (len(r['title']), r['title']))
        short = r.get('short')
        if short and len(short) > 18:
            bad.append('short title too long (%d): %s' % (len(short), short))
        if not short and len(r['title']) > 18:
            bad.append('title needs a short form (%d): %s' % (len(r['title']), r['title']))
        for st in STATUSES:
            if st not in r['edges']: bad.append('%s missing status %s' % (r['id'], st))
            lo, hi = r['edges'][st]
            if lo is not None and hi is not None and hi <= lo:
                bad.append('%s [%s] end is not above start' % (r['id'], st))
        if not r['s']: bad.append('no source: ' + r['id'])
        for label, url in r['s']:
            if not url.startswith('https://'): bad.append('bad url on ' + r['id'])
        # A phase-out with no end is a step or an open band, not a phase-out.
        if r['shape'] == 'phaseout':
            for st in STATUSES:
                lo, hi = r['edges'][st]
                if lo is not None and hi is None:
                    bad.append('%s [%s] is shaped phaseout but has no end' % (r['id'], st))
    ids = set()
    for l in LIMITS:
        if not l['s']: bad.append('no source on limit ' + l['id'])
        if l.get('group') not in ('put', 'take', 'give'):
            bad.append('limit %s has no group' % l['id'])
        if l['id'] in ids: bad.append('duplicate limit id: ' + l['id'])
        ids.add(l['id'])
        if isinstance(l['base'], dict):
            for st in STATUSES:
                if st not in l['base']: bad.append('%s missing status %s' % (l['id'], st))
    for r in RULES:
        if r.get('age_max') and r.get('age_min') and r['age_max'] <= r['age_min']:
            bad.append('%s age range is empty' % r['id'])
    return bad

if __name__ == '__main__':
    problems = check()
    if problems:
        print('RULE PROBLEMS:', file=sys.stderr)
        for p in problems: print('  ' + p, file=sys.stderr)
        sys.exit(1)
    print(emit())
    secs = {}
    for r in RULES: secs[r['section']] = secs.get(r['section'], 0) + 1
    print('%d rules in %d sections, %d age-driven limits'
          % (len(RULES), len(secs), len(LIMITS)), file=sys.stderr)
    for k, v in secs.items(): print('  %-12s %d' % (k, v), file=sys.stderr)
