#!/usr/bin/env python
# coding: utf-8
from random import choice
from random import sample
from random import randint

# minor screens
dividend_screens = ['D','D','D','DH','DH','DVH']
cap_screens = ['SC', 'MC', 'LC', 'MG' ]
sector_screens = ['BI','BM','CG','CO','CS',
                  'DMM','F','H','I',
                  'IIP','IMM','IOG','MOG',
                  'OGD','REIT','T',
                  'U' ]

minor_screens = sum( [ dividend_screens,
                       cap_screens,
                       sector_screens ], [] )

# major screens
trend_screens = ['52WH', '52WL'] # 'BE', 'BU', 'GC',   
low_value_screens = ['LFPE','PER','PEG','PBVR','PCFR','PSR']
liquidity_screens = ['CR','QR']
profit_screens = ['EPSG','NM','OPM','ROA','ROE']
growth_screens = ['EPSG1','EPSG5']
price_screens = ['U5','U7','U10']
debt_screens = ['DER','LDER']
analyst_screens = ['AB','ABB','ASB','ASB']

major_screens = sum( [ trend_screens,
                       low_value_screens,
                       liquidity_screens,
                       profit_screens,
                       growth_screens,
                       price_screens,
                       debt_screens,
                       analyst_screens ], [] )

keywords = {'AB': ['Analyst','Sell'],
            'ABB': ['Analyst','Sell'],
            'ASB': ['Analyst','Sell'],          
            'BE': ['Losing', 'Slip', 'Bear', 'Fall'],
            'BI': ['Bio'],
            'BM': ['Basic Materials'],
            'BU': ['Gain','Bullish'],
            'CG': ['Consumer Goods'],
            'CR': ['Cash','Money','Liquid'],
            'CO': ['Conglomerate'],            
            'CS': ['Computer'],            
            'D': ['Dividend','Yield'],
            'DER': ['Debt','Low'],
            'DH': ['Dividend','Yield'],
            'DMM': ['Pharma'],
            'DVH': ['Dividend','Yield'],
            'QR': ['Cash','Money','Liquid'],
            'EPSG': ['Grow'],
            'EPSG1': ['Grow'],
            'EPSG5': ['Grow'],
            'F': ['Financ'],
            'FPER': ['Over','Premium','High'],
            'H': ['Health'],
            'I': ['Industrial'],
            'IIP': ['Internet'],
            'IMM': ['Industrial Metals & Minerals'],
            'IOG': ['Oil & Gas'],
            'LC': ['Large'],
            'LDER': ['Debt','Long','Low'],            
            'LFPE': ['Undervalued','Value','Cheap','Discount'],
            'MC': ['Mid'],
            'MG': ['Mega'],            
            'MOG': ['Major Oil & Gas'],
            'NM': ['Profit','Earning'],
            'OGD': ['Oil & Gas Drill'],
            'OPM': ['Profit','Earning'],
            'PEG': ['Undervalued','Value','Cheap','Discount'],
            'PER': ['Undervalued','Value','Cheap','Discount'],
            'PBVR': ['Undervalued','Value','Cheap','Discount'],
            'PCFR': ['Undervalued','Value','Cheap','Discount'],
            'PSR': ['Undervalued','Value','Cheap','Discount'],
            'REIT': ['REIT','Real Estate'],
            'ROA': ['Profit','Earning'],
            'ROE': ['Profit','Earning'],
            'SC': ['Small'],
            'T': ['Tech'],
            'U': ['Util'],
            'U5': ['$5'],
            'U7': ['$7'],
            'U10': ['$10'],
            }

titles = {'AB': ['That Analysts Rate As Buy'],
          'ABB': ['That Analysts Rate As Buy Or Better'],
          'ASB': ['That Analysts Rate As Strong Buy'],          
          'BE': ['That Are Losing Momentum',
                 'That Are Losing Steam',
                 'That Are Starting to Slip',
                 'Falling On Market Fears',
                 'With Bearish Momentum Pulling Them Lower'],
          'BU': ['That Are Gaining Bullish Momentum',
                 'That Are Gaining Momentum',
                 'That Are Gaining Steam',
                 'That Are Beating The Market',
                 'Which Are Rallying Higher',
                 'That Keep Topping The Market',
                 'Riding On Bullish Momentum',
                 'Gaining Bullish Momentum',
                 'That Can Keep Rocketing Higher',
                 'Running On Strong Momentum With Room To Go Higher'],
          '52WH': ['Trading Near Their 52-Week Highs',
                   'Hitting Their 52-Week Highs'],
          '52WL': ['Trading Near Their 52-Week Lows',
                   'Hitting Their 52-Week Lows'],          
          'CR': ['Hoarding Cash While Waiting For The Right Opportunities',
                 'Hoarding Cash For The Right Opportunities',
                 'With Plenty Of Cash',
                 'With Plenty Of Cash On Hand',
                 'With Fistfuls Of Cash',
                 'With Handfuls Of Cash',                 
                 'Hoarding Cash',
                 'With Strong Liquidity',
                 'With Strong Cash Reserves',
                 'With Strong Cash Reserves',                 
                 'With High Liquidity',
                 'With Good Liquidity',                 
                 'With Great Liquidity',                 
                 'Hoarding Money',
                 'Heavy on Cash',                 
                 'With Cash To Spend'],
          'QR': ['With Strong Cash Reserves'],
          'DER': ['With No Debt',
                  'With Little Debt',
                  'With Minimal Debt',
                  'That Can Manage Debt',                  
                  'With Manageable Debt Ratios'],
          'LDER': ['With Little Long Term Debt',
                   'With Minimal Long Term Debt'],
          'EPSG': ['With Strong Top Line Growth',
                   'With Strong Earnings Growth',
                   'With Impressive Profitability',
                   'With Great Profitability',
                   'Raking in Profits',                   
                   'Bringing in Strong Profitability',
                   'Killing it on Profitability',
                   'Bringing in Solid Profits',
                   'That Keep Returning Profits',
                   'With Strong Sources Of Profitability'
                   'Running Profitably',
                   'With Strong Profitability'],
          'EPSG1': ['With Strong Projected Growth',
                    'With Strong Expected Growth',
                    'With Strong Projected Growth Rates'],
          'EPSG5': ['With Strong Projected Growth',
                    'With Strong Expected Growth',
                    'With Strong Projected Growth Rates'],
          'FPER': ['Trading at Premium',
                   'That are Overvalued',
                   'With High Valuations'],
          'LFPE': ['Trading At A Discount',
                   'With Low Valuations'],
          'NM': ['With Strong Profitability',
                 'With Impressive Profitability',
                 'With Great Profitability',
                 'With Hearty Profits',
                 'With Strong Margins',
                 'With Impressive Margins',                 
                 'With Hearty Profitability',
                 'With Impressive Bottom Line Profitablity',
                 'Operating With Solid Profitability'],
          'OPM': ['That Are Profitable',
                  'With Strong Profits',
                  'With Hearty Profits',
                  'With Hearty Profitability',
                  'With Solid Profits',                  
                  'Operating With Impressive Profitability'],
          'PEG': ['Looking Undervalued',
                  'Looking Cheap',
                  'With Cheap Valuations',
                  'That Are Undervalued'],
          'PER': ['Looking Undervalued',
                  'Looking Cheap',
                  'With Cheap Valuations',
                  'Trading At A Discount',
                  'That Are Undervalued',
                  'Holding Low Valuations',
                  'With Low Valuations',
                  'Undervalued By P/E Trends'],
          'PBVR': ['That Are Undervalued',
                   'Undervalued By EPS Trends'],
          'PCFR': ['Trading At A Discount',
                   'Trading For Cheap',
                   'Trading Dirt Cheap'],
          'PSR': ['Trading At A Discount',
                  'Trading Dirt Cheap'],          
          'ROA': ['With Strong Profitability',
                  'With Sound Profitablity',
                  'With Solid Profits',
                  'With Hearty Profits',
                  'Killing it on Profits',                  
                  'With Hearty Profitability',
                  'With Hefty Profits',
                  'Commanding Profits',                  
                  'Showing Lean And Mean Profitability',
                  'With Strong Return On Assets Ratios'],
          'ROE': ['With Sound Profitablity',
                  'With Strong Profitability',
                  'With Strong Profits',                  
                  'Showing Lean And Mean Profitability'],
          'U5': ['Trading Under $5',
                 'Trading For Under $5'],
          'U7': ['Trading Under $7',
                 'Trading For Under $7'],
          'U10': ['Trading Under $10',
                  'Trading For Under $10']
          }

intros = {'AB': ["Do you prefer investing in stocks that analysts have weighed in on?",
                 "Do you prefer stocks that analysts rate as 'Buy'?"],
          'ABB': ["Are you after stocks that analysts are calling 'buy' or 'strong buy'?",
                  "Do you prefer stocks that analysts rate as 'Buy', or better?"],
          'ASB': ["Do you prefer investing in stocks that analysts rate as 'strong buy'?",
                  "Do you prefer stocks that analysts rate as 'Strong Buy'?"],          
          'BM':
              ["Do you like gaining exposure to commodities for their diversification benefits? One way to get this exposure is through basic materials companies, although keep in mind they also have business risks separate from the risks of the commodities they produce."],
          'D':
              ["Do you like to be able to rely on a stock's dividend income as a source of return?",
               "Do you like to be able to rely on a stock's dividend income?",
               "Do you prefer stocks that pay back their investors with dividend income?",
               "Do you like stocks that pay dividends?",
               "Do you prefer dividend stocks?",
               "Do you prefer stocks that pay their fair share in dividend income?",
               "Looking for dividends you can rely on?",
               "Interested in finding stocks that pay reliable dividends?",
               "Interested in stocks paying significant dividends?",
               "Interested in stocks paying dividend income?",
               "Interested in stocks paying dividend income, but don't know where to start?",
               "Interested in earning dividend income?",
               "In search of attractive dividend stocks?"],
          'DH':
              ["Do you like stocks with high dividend yield?",
               "Are you after stocks with high dividend yield?",
               "Are you after stocks with high dividend yield, over 5%?",               
               "Do you prefer stocks with high dividend yield?",
               "Do you like to be able to rely on a stock's dividend income as a source of return?",
               "Do you like to be able to rely on a stock's dividend income?",
               "Do you prefer stocks that pay back their investors with dividend income?",
               "Do you like stocks that pay dividends?",
               "Do you prefer dividend stocks?",
               "Do you prefer stocks that pay their fair share in dividend income?",
               "Looking for dividends you can rely on?",
               "Interested in finding stocks that pay reliable dividends?",
               "Interested in stocks paying significant dividends?",
               "Interested in stocks paying dividend income?",
               "Interested in stocks paying dividend income, but don't know where to start?",
               "Interested in earning dividend income?",
               "In search of attractive dividend stocks?"],
          'DVH':
              ["Do you prefer stocks with very high dividend yield?",
               "Do you prefer stocks with double digit dividend yield?",
               "High yield investing can be interesting, even more so in times of low interest rates. The M.O. of high yield investing is to trade stocks with very high yields (double-digit yields). Are double-digit dividend yield stocks what you prefer?",
               "Are you looking for stocks with the highest dividend yield?",
               "Are you after very high dividend yield stocks, with yields over 10%?",               
               "Do you prefer stocks that the highest dividend yield?",
               "Do you like to be able to rely on a stock's dividend income as a source of return?",
               "Do you like to be able to rely on a stock's dividend income?",
               "Do you prefer stocks that pay back their investors with dividend income?",
               "Do you like stocks that pay dividends?",
               "Do you prefer dividend stocks?",
               "Do you prefer stocks that pay their fair share in dividend income?",
               "Looking for dividends you can rely on?",
               "Interested in finding stocks that pay reliable dividends?",
               "Interested in stocks paying significant dividends?",
               "Interested in stocks paying dividend income?",
               "Interested in stocks paying dividend income, but don't know where to start?",
               "Interested in earning dividend income?",
               "In search of attractive dividend stocks?"],
          'liquidity':          
              ["Do you value companies holding large amounts of cash?",
               "Do you feel better knowing your favorite companies have enough cash to cover their operating expenses for a very long time?",
               "Do you prefer companies with high liquidity?",
               "Interested in companies with high liquidity?",                   
               "Company liquidity is an important consideration in any stock analysis. Liquidity gives a company the ability to make big acquisitions if it sees investment opportunities, a cushion for future lulls in demand, and most importantly, it keeps a company’s doors open. Are these the types of stocks that you're looking for?"],
          'debt':
              ["Interested in companies with minimal debt?",
               "Do you look for companies with low debt?",
               "Do you value companies that can keep their debt down?",
               "In search of companies that can manage their debt well?"],
          'DER':
              ["Interested in companies with minimal debt?",
               "Do you look for companies with low debt?",
               "In search of companies that can manage their debt well?"],
          'LDER':
              ["Interested in companies with minimal long term debt?",
               "Do you prefer companies that can manage their long term debt?",
               "Are you after companies that have manageable long term debt?"],
          'DMM': ["Do you follow Big Pharmaceutical companies?",
                  "Do you prefer investing in the Pharmaceutical industry?",
                  "Do you diversify your portfolio with Pharmaceutical companies?"],
          'ETF': ["Do you prefer ETFs?",
                  "Do you prefer Exchange Traded Funds?",
                  "Do you diversify your portfolio with Exchange Traded Funds?"],
          'EPSG1': ["Do you prefer stocks with high projected earnings over the next year?",
                    "Do you prefer stocks that can bring in profits over the next year?",
                    "Do you prefer stocks that are projected to grow over the next year?",
                    "Do you prefer high-growth stocks?"],
          'EPSG5': ["Do you prefer stocks with high projected earnings over the long term?",
                    "Do you prefer stocks that can bring in profits over the long term?",
                    "Do you prefer stocks that are projected to grow over the long term?",
                    "Do you prefer high-growth stocks?"],
          'IIP': ["Do you prefer stocks in the tech industry?"],
          'IMM': ["Do you prefer investing in the tools of industry?"],
          'IOG': ["Do you seek Oil and Gas stocks?"],
          'MOG': ["Do you invest in the Big Dogs of the Oil and Gas industry?"],
          'OGD': ["Interested in Oil and Gas Drilling companies?",
                  "Do you invest in the Oil and Gas industry?"],
          'low_value':
              ["Looking for undervalued stocks?"],
          # Sector
          'sector':
              ["Interested in gaining exposure to %s companies?",
               "Interested in %s companies?",
               "Interested in %s stocks?"],
          # trend
          'trend':
              ["Are you a momentum investor?",
               "Do you look for stocks near their 52-week highs or lows?",
               "Do you watch for stocks where you can ride their momentum?",               
               "Do you look for stocks with strong momentum?"],
           # Market cap
          'LC':
              ["Are you looking for large-cap companies that still have room to grow?",
               "Do you prefer the largest cap stocks?",
               "Do you prefer the largest and established stocks?"],
          'MC':
              ["Are you looking for mid-sized companies that still have room to grow?"],
          'MG':
              ["Are you looking for large to mega-sized companies?",
               "Are you interested in investing in the bohemoths of the S&P 500?",
               "Do you prefer the largest and most established companies?",
               "Do you want to invest in the giants of the S&P 500?",
               "Do you want to stand on the shoulders of giants, by investing in mega cap companies?"],
          'SC':
              ["Small-cap stocks tend to offer investors greater growth opportunities than large-cap alternatives, although this comes with its fair share of added risk. Are you looking for small-caps?",
               "Interested in following smaller companies?"],
          'profit':
              ["Looking for ways to dig deeper into a company's profitability?",
               "Do you prefer companies with strong profits?"],
          'U5':
              ["Looking for stocks trading at low prices?",
               "Do you prefer stocks trading under $5?",
               "Do you prefer stocks trading for less than $5?"],
          'U7':
              ["Looking for stocks priced under $7?",
               "Do you prefer companies trading under $7?",
               "Do you prefer stocks trading for less than $7?"],
          'U10':
              ["Looking for stocks priced under $10?",
               "Do you prefer companies priced under $10?",               
               "Do you prefer companies with share prices under $10?"],
          '':
              ["Interested in finding stocks that may be trading below their fair value?",
               "Interested in stocks that may have more upside to price in?",
               "Interested in finding stocks that may be trading at too low of a valuation?",
               "Do you like to look for a bargain, even among stocks?"]}

intro_endings = ["For ideas on where to look, we ran a screen you may be interested in.",
                 "For ideas on where to look, we ran a screen you might find interesting.",
                 "For ideas on how to start your search, we ran a screen you may find helpful.",
                 "If so, here's a list you might be interested in.",
                 "If so, here are some ideas to start your stock search.",
                 "Here are some interesting ideas to get you started.",
                 "If the answer is 'yes', here are some interesting ideas to get you started.",
                 "If yes, here are a few ideas to start your search.",
                 "If so, we ran a screen keeping this idea in mind.",
                 "If so, you’ll probably like this list.",
                 "You might be interested in this list.",
                 "You might like what we've put in our list.",
                 "If so, here are some interesting ideas for you.",               
                 "If so, here are some ideas to get you started on your search.",
                 "For ideas on how to start your own search, we ran a screen.",
                 "For a closer look at stocks of this nature, we ran a screen.",
                 "We ran a screen you might be interested in.",
                 "We ran a screen you might find helpful.",
                 "We ran a screen you might find useful.",
                 "We ran a screen you could find useful.",               
                 "Keeping this idea in mind, we ran a screen you might be interested in.",
                 "For ideas on how to go about your analysis, here is a list you might be interested in.",
                 "For ideas on how to evaluate this, we ran a screen."]

summaries = {'AB': ['that analysts rate as "Buy" (2 < mean recommendation < 3)'],
             'ABB': ['that analysts rate as "Buy" or "Strong Buy" (mean recommendation < 3)'],
             'ASB': ['that analysts rate as "Strong Buy" (mean recommendation < 2)'],
             'CR': ['that have a substantial amount of cash on hand (Current Ratio>2)',
                    'with a large amount of cash on hand (Current Ratio>2)',
                    'that have strong liquidity (Current Ratio>2)'],
             'QR': ['that have a substantial amount of cash on hand (Quick Ratio>2)',
                    'with a large amount of cash on hand (Quick Ratio>2)',
                    'that have strong liquidity (Quick Ratio>2)'],             
             '52WH': ['that are currently trading at no less than 20% below their 52-week highs. Why you wonder? The number shows these firms are doing something right consistently. The real question is "as an investor do you think the firms listed here have room to go even higher?"'],
             '52WL': ['that are currently trading at no more than 10% above their 52-week lows'],
             'DH': ['that have a high dividend yield (Div. Yield > 5%)',
                    'with a very high yield (more than 5%)'],
             'DVH': ['that have a very high dividend yield (Div. Yield > 10%)',
                     'with a very high yield (more than 10%)'],             
             'DER': ['that operate with little to no debt (D/E Ratio<.1)',
                     'that have maintained a sound capital structure (D/E Ratio<.1)'],
             'LDER': ['that operate with little to no long term debt (Long Term D/E Ratio<.1)',
                      'that have maintained a sound long term capital structure (Long Term D/E Ratio<.1)'],             
             'EPSG': ['that have shown strong bottom line growth over the last year (1-year fiscal EPS growth rate>10%)',
                      'that have posted strong earnings growth for shareholders over an extended period of time (1-year fiscal EPS growth rate>10%)',
                      'that have strong profitability (1-year fiscal EPS Growth Rate>10%)'],
             'EPSG1': ['that have expected earnings per share growth of more than 25 percent for next year(1-year projected EPS Growth Rate>25%)',
                       'that have high future earnings per share growth forecasts(1-year projected EPS Growth Rate>25%)',
                       'with projected high growth, measured by 1-year projected EPS growth above 25%',
                       'that are considered high-growth, with 1-year projected EPS growth above 25%',
                       'with estimated high-growth, with 1-year projected EPS growth above 25%'],
             'EPSG5': ['that have expected earnings per share growth of more than 25 percent for the next five years(5-year projected EPS Growth Rate>25%)',
                       'that have high future earnings per share growth forecasts(5-year projected EPS Growth Rate>25%)',
                       'with projected high growth, measured by 5-year projected EPS growth above 25%',
                       'that are considered high-growth, with 5-year projected EPS growth above 25%',
                       'with estimated high-growth, with 5-year projected EPS growth above 25%'],
             'FPER': ['with a high price-multiple premium (forward P/E>20)'],
             'LFPE': ['with a low price-multiple premium (forward P/E<10)'],             
             'NM': ['with strong profitability (Net Margin [TTM] >10%)',
                    'that have been able to retain strong profit margins on the bottom line (Net Margin [TTM]>10%)',
                    'that have achieved strong bottom line profitability (Net Margin [TTM]>10%)',
                    'that have strong bottom line profitability (Net Margin [TTM]>10%)'],
             'OPM': ['with strong profit margins (1-year operating margin>15%)'],
             'PBVR': ['that are undervalued (P/BV<1)',
                      'that are undervalued from a price-multiple valuation standpoint (P/BV<1)'],
             'PCFR': ['that are trading at low price-multiple valuations (P/CFO<10)'],
             'PEG': ['that are trading at a discount when considering the company growth rate (PEG Ratio < 1)',
                     'that appear undervalued to earnings growth (PEG < 1)',
                     'that are undervalued when company growth rate is taken into account (PEG Ratio < 1)'],
             'PER': ['that are trading at a discount (P/E<10)',
                     'that appear undervalued from a price-multiple perspective (P/E<10)',
                     'that are trading at a discount (P/E<10)'],
             'PSR': ['that are trading at a discount (P/S<1)'],
             'ROA': [ 'with strong profitability (ROA > 10%)',
                      'that have strong profitability relative to their asset base (ROA [TTM]>10%)'],
             'ROE': ['that have been able to maintain a sound level of profitability for shareholders (ROE [TTM]>30%)'],
             'U5': ['that are trading at under $5',
                    'with share prices under $5'],
             'U7': ['that are trading at under $7',
                    'with share prices under $7'],
             'U10': ['that are trading at under $10',
                     'with share prices under $10']             
             }

abbrevs = {'AB':   "Analysts' Rating",
           'ABB':  "Analysts' Rating",
           'ASB':  "Analysts' Rating",
           'BU':   'Bullish',
           'BE':   'Bearish',
           'BI':   'Biotechnology',
           'BM':   'Basic Materials',
           '52WH': '52 Week High',
           '52WL': '52 Week Low',           
           'CG':   'Consumer',           
           'CR':   'Current Ratio',
           'QR':   'Quick Ratio',
           'CO':   'Conglomerate',           
           'CS':   'Computer Systems',
           'D':    'Dividend',
           'DH':   'High Yield Dividend',
           'DVH':  'Very High Yield Dividend',           
           'DER':  'Debt/Equity Ratio',
           'LDER': 'Long Term Debt/Equity Ratio',
           'DMM':  'Pharmaceutical',
           'EPSG': 'Earnings Per Share Growth Rate',
           'EPSG1':'1-Year Projected Earnings Per Share Growth Rate',           
           'EPSG5':'5-Year Projected Earnings Per Share Growth Rate',           
           'ETF':  'Exchange Traded Fund',
           'F':    'Financial',
           'FPER': 'Forward Price/Earnings Ratio',
           'LFPE': 'Forward Price/Earnings Ratio',           
           'H':    'Healthcare',
           'I':    'Industrial',
           'IIP':  'Internet',
           'IMM':  'Industrial Metals & Minerals',
           'IOG':  'Oil & Gas',
           'MOG':  'Major Oil & Gas',           
           'OGD':  'Oil & Gas Drilling',           
           'LC':   'Large Cap',
           'MC':   'Mid Cap',
           'MG':   'Mega Cap',
           'NM':   'Net Margin',           
           'OPM':  'Operating Profit Margin',
           'PBVR': 'Price/Book Value Ratio',
           'PCFR': 'Price/Cash Flow Ratio',
           'PEG':  'Price/Earnings to Growth Ratio',
           'PER':  'Price/Earnings Ratio',
           'PO':   'Payout Ratio',
           'PSR':  'Price/Sales Ratio',
           'REIT': 'REIT',
           'ROA':  'Return on Assets',
           'ROE':  'Return on Equity',
           'SC':   'Small Cap',
           'T':    'Technology', 
           'U':    'Utility',
           'U5':   'Share Price', #'Under $5',
           'U7':   'Share Price', #'Under $7',           
           'U10':  'Share Price', #'Under $10'           
           }

maps = {'AB':   'an_recom_buy',
        'ABB':  'an_recom_buybetter',
        'ASB':  'an_recom_strongbuy',
        'BM':   'sec_basicmaterials',
        'BI':   'ind_biotechnology',        
        'CG':   'sec_consumergoods',
        'CR':   'fa_curratio_o2',
        'QR':   'fa_quickratio_o2',
        'CO':   'sec_conglomerates',
        'CS':   'ind_diversifiedcomputersystems',
        'D':    'fa_div_o3,fa_payoutratio_u100',
        'DH':   'fa_div_high,fa_payoutratio_u100',
        'DVH':  'fa_div_veryhigh,fa_payoutratio_u100',        
        'DMM':  'ind_drugmanufacturersmajor',
        '52WH': 'ta_highlow52w_b80',
        '52WL': 'ta_highlow52w_a0to10h',        
        'DER':  'fa_debteq_low',
        'LDER': 'fa_ltdebteq_low',
        'EPSG': 'fa_epsyoy_o10',
        'EPSG1':'fa_epsyoy1_high',
        'EPSG5':'fa_estltgrowth_high',
        'ETF':  'ind_exchangetradedfund',
        'F':    'sec_financial',
        'FPER': 'fa_fpe_o20',
        'LFPE': 'fa_fpe_u10',        
        'H':    'sec_healthcare',
        'I':    'sec_industrialgoods',
        'IOG':  'ind_independentoilgas',
        'IIP':  'ind_internetinformationproviders',
        'IMM':  'ind_industrialmetalsminerals',
        'MOG':  'ind_majorintegratedoilgas',
        'OGD':  'ind_oilgasdrillingexploration',        
        'LC':   'cap_large',
        'NM':   'fa_netmargin_o10',        
        'MC':   'cap_mid',
        'MG':   'cap_mega',
        'NM':   'fa_netmargin_o10',
        'OPM':  'fa_opermargin_o20',
        'PBVR': 'fa_pb_low',
        'PCFR': 'fa_pfcf_u10',
        'PEG':  'fa_peg_low',        
        'PER':  'fa_pe_u10',
        'PSR':  'fa_ps_low',
        'REIT': 'ind_reitdiversified',
        'ROA':  'fa_roa_o10',
        'ROE':  'fa_roe_verypos',
        'SC':   'cap_small',
        'T':    'sec_technology',
        'U':    'sec_utilities',
        'U5':   'sh_price_u5',
        'U7':   'sh_price_u7',        
        'U10':  'sh_price_u10'        
        }

html_maps = {'AB': "Analysts' mean recommendation (1=Buy 5=Sell)",
             'ABB': "Analysts' mean recommendation (1=Buy 5=Sell)",
             'ASB': "Analysts' mean recommendation (1=Buy 5=Sell)",
             'CR': 'Current Ratio (mrq)',
             'QR': 'Quick Ratio (mrq)',
             'D' : 'Dividend yield (annual)',
             'DH' : 'Dividend yield (annual)',
             'DVH' : 'Dividend yield (annual)',             
             'DER': 'Total Debt to Equity (mrq)',
             'LDER': 'Long Term Debt to Equity (mrq)',
             '52WH':'Distance from 52-Week High',
             '52WL':'Distance from 52-Week Low',
             'EPSG': 'EPS growth this year',
             'EPSG1': 'EPS growth next year',             
             'EPSG5':'Long term annual growth estimate (5 years)',
             'FPER': 'Forward Price-to-Earnings (next fiscal year)',
             'LFPE': 'Forward Price-to-Earnings (next fiscal year)',
             'LC': 'Market capitalization',
             'MC': 'Market capitalization',
             'MG': 'Market capitalization',
             'NM': 'Net Profit Margin (ttm)',
             'OPM': 'Operating Margin (ttm)',
             'PBVR': 'Price-to-Book (mrq)',
             'PCFR': 'Price to cash per share (mrq)', # Price to Free Cash Flow (ttm)
             'PEG': 'Price-to-Earnings-to-Growth',
             'PER': 'Price-to-Earnings (ttm)',
             'PO':  'Dividend Payout Ratio (ttm)',
             'PSR': 'Price-to-Sales (ttm)',             
             'ROA': 'Return on Assets (ttm)',             
             'ROE': 'Return on Equity (ttm)',
             'SC': 'Market capitalization',
             'U5': 'Current stock price',
             'U7': 'Current stock price',
             'U10': 'Current stock price',
            }

order_suffixes = {'AB': '-recom',
                  'ABB': '-recom',
                  'ASB': '-recom',
                  'CR': '-curratio',
                  'D': '-dividendyield',
                  'DER': '-debteq',
                  'DH': '-dividendyield',
                  'DVH': '-dividendyield',
                  'LDER': '-ltdebteq',
                  '52WH': '-high52w',
                  '52WL': '-low52w',
                  'EPSG': '-epsyoy',
                  'EPSG1': '-epsyoy1',
                  'EPSG5': '-estltgrowth',
                  'PER': '-pe',
                  'PO': '-payoutratio',
                  'FPER': '-forwardpe',
                  'LFPE': '-forwardpe',
                  'LC': '-marketcap',
                  'MC': '-marketcap',
                  'MG': '-marketcap',
                  'SC ': '-marketcap',                  
                  'NM': '-netmargin',
                  'OPM': '-opermargin',
                  'PEG': '-peg',
                  'PBVR': '-pb',
                  'PCFR': '-pfcf',
                  'PSR': '-ps',
                  'QR': '-quickratio',
                  'ROA': '-roa',                  
                  'ROE': '-roe'
                  }

ignored = ['BI','BE','BM','BU','CG','CO','CS',
           'DMM','F','H','I','IIP','IOG','IMM','LC','MOG','MC','MG',  #'ETF',
           'OGD','REIT','SC','T','U'] # ,'U5','U7','U10']

def get_keywords( screen_list ):
    keyword_list = []
    for screen in screen_list:
        if screen != '':
            if keywords[ screen ] not in keyword_list:
                keyword_list.append( keywords[ screen ] )
    return keyword_list

def make_finviz_url( screen ):
    prefix = 'http://finviz.com/screener.ashx?v=111&f='
    suffix = '&ft=4'
    order_suffix = '&o='
    # geo = ',geo_usa'
    # idx = ',idx_sp500'
    screen_url = []
    for screen_type in screen:
        if screen_type != '':
            screen_url.append( maps[screen_type] )
    url = prefix + ','.join(screen_url) + suffix + order_suffix + order_suffixes[screen[3]] # + idx + geo
    print url
    return url

def make_minor_screen():
    minor_screen = ['','','']
    while minor_screen == ['','','']:
        minor_screen = [ choice( cap_screens + ['','','']),
                         choice( sector_screens + ['','','',''] ),
                         choice( dividend_screens + ['','',''] ) ]
    return minor_screen

def make_major_screen():
    screens = [ #[choice( trend_screens )],
                sample( low_value_screens, 2 ),
                liquidity_screens,
                sample( profit_screens, 2 ),
                [choice( growth_screens )],
                sample( debt_screens, randint(1,2) ),                
                [choice( analyst_screens )] ]
    # flatten the list
    screens = sum( sample( screens, 2 ), [])
    # pad the list
    if len( screens ) == 3:
        screens = screens + ['']
    return screens

# returns array of the form:
# ['market cap',
#  'sector',
#  'dividend',
#  'major screen 1',
#  'major screen 2',
#  'major screen 3',
#  'option major screen 4']
# Sample: ['LC','F','D','CR','QR','NM','OPM','']
#   minor screens: 'Large Cap', 'Financial', 'Dividend'
#   major screens: 'Current Ratio', 'Quick Ratio', 'Net Margin', 'Operating Profit Margin', n/a
def make_screen():
    return make_minor_screen() + make_major_screen()

