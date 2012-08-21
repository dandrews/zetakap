# coding: utf-8

descriptions = {'AB': "",
                'ABB': "",
                'ASB': "",
                'BU': "",
                'BE': "",
                'BI': "",                
                'BM': "",                
                'CG': "",
                '52WH': "",
                '52WL': "",                
                'CR':
                    "The Current ratio is a liquidity ratio used to determine a company's financial health. The metric illustrates how easily a firm can pay back its short obligations all at once through current assets. A company that has a current ratio of one or less is generally a liquidity red flag. Now this doesn't mean the company will go bankrupt tomorrow, but it also doesn't bode well for the company, and may indicate that it could have an issue paying back upcoming obligations.\n",
                'QR':
                    "The Quick ratio measures a company's ability to use its cash or assets to extinguish its current liabilities immediately. Quick assets include assets that presumably can be converted to cash at close to their book values. A company with a Quick Ratio of less than 1 cannot currently pay back its current liabilities. The quick ratio is more conservative than the Current Ratio because it excludes inventory from current assets, since some companies have difficulty turning their inventory into cash. If short-term obligations need to be paid off immediately, sometimes the current ratio would overestimate a company's short-term financial strength. In general, the higher the ratio, the greater the company's liquidity (i.e., the better able to meet current obligations using liquid assets).\n",
                'CO': "",
                'CS': "",                
                'D': "",
                'DH': "",
                'DVH': "",                
                'DER':
                    "The Debt/Equity Ratio illustrates how aggressively a company is financing its growth via debt. The more debt financing that is used in a capital structure, the more volatile earnings can become due to the additional interest expense. Should a company's potentially enhanced earnings fail to exceed the cost associated with debt financing over time, this can lead the company toward substantial trouble.\n",
                'LDER':
                    "The Long Term Debt/Equity Ratio is a variation of the traditional debt-to-equity ratio; this value computes the proportion of a company's long-term debt compared to its available capital. By using this ratio, investors can identify the amount of leverage utilized by a specific company and compare it to others to help analyze the company's risk exposure. Generally, companies that finance a greater portion of their capital via debt are considered riskier than those with lower leverage ratios.\n",
                'DMM': "",                
                'EPSG':
                    "EPS growth (earnings per share growth) illustrates the growth of earnings per share over time. EPS growth rates help investors identify stocks that are increasing or decreasing in profitability. This profitability metric is generally a key driver in the price of the stock as it directly correlates to the profitability of the company as a whole.\n",
                'EPSG1':
                    "EPS growth (earnings per share growth) illustrates the growth of earnings per share over time. The 1-Year Expected EPS Growth Rate is an annual growth estimate, where the growth projections are made by analysts, the company or other credible sources.\n",                
                'EPSG5':
                    "EPS growth (earnings per share growth) illustrates the growth of earnings per share over time. The 5-Year Expected EPS Growth Rate is a long term annual growth estimate, where the growth projections are made by analysts, the company or other credible sources.\n",
                'ETF': "",
                'F': "",
                'FPER':
                    "The forward P/E is a price multiple valuation metric, which is similar to the current P/E ratio, except that it uses the forecasted earnings instead. While this number might not be as accurate because it uses “forecasted” numbers, it does offer the benefit of illustrating analysts’ expectations of a firm. If the market believes that earnings will grow moving forward, then the forward P/E should be lower than the current P/E. Financial Leverage, also known as the Equity Multiplier, illustrates how a firm is financing its assets. The lower the number the more a firm is financing its assets internally through stockholder equity. The higher this metric is the more the firm is relying on debt to finance its assets.\n",
                'H': "",
                'I': "",
                'IIP': "",
                'IMM': "",                
                'IOG': "",
                'MOG': "",                
                'OGD': "",
                'LC': "",
                'LFPE':
                    "The forward P/E is a price multiple valuation metric, which is similar to the current P/E ratio, except that it uses the forecasted earnings instead. While this number might not be as accurate because it uses “forecasted” numbers, it does offer the benefit of illustrating analysts’ expectations of a firm. If the market believes that earnings will grow moving forward, then the forward P/E should be lower than the current P/E. Financial Leverage, also known as the Equity Multiplier, illustrates how a firm is financing its assets. The lower the number the more a firm is financing its assets internally through stockholder equity. The higher this metric is the more the firm is relying on debt to finance its assets.\n",
                'MC': "",
                'MG': "",
                'NM':
                    "The Net Margin is a profitability metric that illustrates, by percentage, how much of every dollar earned gets turned into a bottom line profit. This is just one of many profitability metrics used by investors and analysts to better understand what the company is being left with at the end of the day. Generally, a firm that can expand its net profit margins over a period of time will see its stock price rise as well due to the trend of increasing profitability.\nNet Margin = Net Income/Total Revenue\n",         
                'OPM':
                    "The Operating Profit Margin is a profitability ratio that measures the effectiveness of the company's operating efficiency. This metric allows investors to see how much profit is left after all variable costs are covered. If the company's margin is increasing over time this means that it's earning more per dollar of sales. Finding trends in the Operating Profit Margin helps investors identify companies that are improving profitability over time and managing the economic landscape better than competitors.\n",
                'PBVR':
                    "The Price/Book Value Ratio is a great price-multiple valuation metric to find companies that could be potentially undervalued or overvalued. If a firm has a Price/Book Value Ratio of less than 1 it is stated to be trading below “break up” value. A lower P/BV Ratio can indicate a potentially mispriced company or indicate that something is fundamentally wrong with it.\n",
                'PCFR':
                    "The Price/Cash Flow ratio is a price-multiple valuation metric that also measures a firm’s future financial health. An advantage of using cash flow is that it removes non-cash factors, which helps provide a clearer picture of how much money the firm is taking in from a valuation standpoint.\nPrice/Cash Flow Ratio = Current Stock Price/Cash Flow Per Share\n",
                'PEG':
                    "The PEG ratio (price/earnings to growth ratio) is a valuation metric for determining the relative trade-off between the price of a stock, the earnings generated per share [EPS], and the company's expected growth. In general, the P/E ratio is higher for a company with a higher growth rate. Thus using just the P/E ratio would make high-growth companies appear overvalued relative to others. It is assumed that by dividing the P/E ratio by the earnings growth rate, the resulting ratio is better for comparing companies with different growth rates. A lower ratio is 'better' (cheaper) and a higher ratio is 'worse' (expensive) - a PEG ratio of 1 means the company is fairly priced.\n",                
                'PER':
                    "The Price/Earnings ratio is one of the most commonly used price-multiple metrics. Often, EPS from the last four quarters is used to derive this number. A firm that has a high P/E ratio generally indicates that investors have high expectations of the firm relative to future earnings growth. By the opposite token, investors generally have lower expectations of a firm with a low P/E ratio. A firm that holds a P/E below 10 could be viewed as having \"value investment\" potential. One thing to remember is that EPS is an accounting measure that could be potentially manipulated. Thus the P/E is only as good as the quality of the earnings.\n",
                'PO': "",
                'PSR':
                    "The Price/Sales ratio is a price-multiple valuation metric used to help identify if a firm is cheap by its twelve month trailing sales numbers. In the most basic terms it let’s an investor know how much the investment community is willing to pay for every dollars worth of sales. A firm with a P/S ratio of one or lower would be viewed as cheap because investors are paying $1 or less for every dollars worth of a firm’s sales. On the other hand, a firm is generally considered to be expensive when the P/S ratio is above three. These are general guidelines used by the investment community not hard rules to be clear.\nPrice/Sales Ratio = Current Stock Price/Revenue (sales) per Share\n",
                'REIT': "",
                'ROA':
                    "Return on Assets [ROA] illustrates how much a company is generating in earnings from its assets alone. This metric gives investors a picture of how profitable the company is relative to the assets in current possession. As well, it lets investors see how efficient and effective management is at generating earnings from the company's assets. While most management teams can probably make money by throwing money at an issue very few can make very large profits with little investment.\n",
                'ROE':
                    "Return on Equity [ROE] is one way to identify great potential names relative to profitability. This ratio illustrates the percentage return on shareholder equity. As well, this metric segments the company into operational efficiency, asset use efficiency, and financial leverage. Why does this matter? Simply put, it allows investors to get a real picture of how the company is generating these returns and helps identify parts of the company that may be underperforming.\n",
                'S': "",
                'SC': "",
                'T': "",
                'U': "",
                'U5': "",
                'U7': "",
                'U10': "",                
                }
