#!/usr/bin/env python

import screens
import random
from screens import make_finviz_url
import utils
from utils import get_pretty_html
from utils import find_between
from check_ticker_age import is_old_enough
from check_ticker_age import get_ticker_article_age

class TickerList:
    def __init__(self, screen ):
        self.screen = screen
        url = make_finviz_url( screen )
        pretty_html = get_pretty_html( url )
        self.tickers = []
        counter = 0
        max_len = random.randrange(6, 8) 
        while find_between( pretty_html, '<a href="quote.ashx?t=', '&amp;' ):
            if counter > max_len:
                break        
            ticker = find_between( pretty_html, '<a href="quote.ashx?t=', '&amp;' )
            print "testing ticker " + ticker
            # only take tickers older than 25 days
            age = get_ticker_article_age( ticker )
            if is_old_enough( age ):
                self.tickers.append(ticker)
                counter = counter + 1
            pretty_html = pretty_html.replace('<a href="quote.ashx?t=','',1)

    def get_tickers(self):
        print "Num of Stocks: " + str(len(self.tickers))
        for symbol in self.tickers:
            print symbol

top_tickers = ['AAPL',
               'C',
               'CSCO',
               'BAC',
               'GE',
               'GOOG',
               'F',
               'NLY',
               'MSFT',
               'INTC',
               'T',
               'ALU',
               'GLD',
               'CMCSA',
               'SPY',
               'VZ',
               'XOM',
               'JNJ',
               'SBUX',
               'DVY',
               'MCD',
               'IVE',
               'CAT',
               'MO',
               'AGNC',
               'SLV',
               'COP',
               'FCX',
               'QQQ',
               'PFE',
               'CHK',
               'IBM',
               'BIDU',
               'AMZN',
               'PG',
               'SIRI',
               'JPM',
               'CVX',
               'KO',
               'AA',
               'ABT',
               'KMP',
               'NFLX',
               'WFC',
               'SH',
               'RIMM',
               'PM',
               'POT',
               'ORCL',
               'GLW',
               'BP',
               'IDV',
               'SLW',
               'HPQ',
               'QCOM',
               'GS',
               'PEP',
               'WMT',
               'EPD',
               'FTR',
               'HAL',
               'CIM',
               'NOK',
               'MRK',
               'LINE',
               'DUK',
               'S',
               'IYR',
               'DE',
               'SDRL',
               'EMC',
               'BRK.B',
               'BMY',
               'AGG',
               'BA',
               'KFT',
               'DD',
               'TEVA',
               'WPRT',
               'KOG',
               'V',
               'RIG',
               'SLB',
               'CLNE',
               'EXC',
               'ETP',
               'IYH',
               'IJS',
               'MCP',
               'SD',
               'VALE',
               'GM',
               'DNDN',
               'HD',
               'MOS',
               'VOD',
               'CTL',
               'WIN',
               'SCCO',
               'PBR',
               'MS',
               'FSLR',
               'LVS',
               'GMCR',
               'YHOO',
               'LLY',
               'MMM',
               'DIS',
               'SO',
               'GG',
               'NVDA',
               'VVUS',
               'BTU',
               'CMI',
               'PFF',
               'WM',
               'UNG',
               'PCLN',
               'YUM',
               'GDX',
               'ZNGA',
               'TEF',
               'ABX',
               'CMG',
               'ARNA',
               'CRM',
               'LULU',
               'APA',
               'LNG',
               'SU',
               'BRCM',
               'CSX',
               'AUY',
               'DRYS',
               'KMB',
               'TOT',
               'AIG',
               'ERF',
               'ARR',
               'BHP',
               'VXX',
               'DVN',
               'MA',
               'MU',
               'ISRG',
               'VLO',
               'EWZ',
               'DELL',
               'MRO',
               'WAG',
               'COST',
               'SINA',
               'DIA',
               'DOW',
               'CLF',
               'MON',
               'X',
               'EOG',
               'TBT',
               'EMR',
               'AMD',
               'HL',
               'AXP',
               'ED',
               'NOV',
               'AMAT',
               'FXI',
               'VMW',
               'RENN',
               'IVR',
               'NUAN',
               'IAU',
               'EEM',
               'EBAY',
               'JCI',
               'USO',
               'MDT',
               'PWE',
               'RIO',
               'ATVI',
               'FXE',
               'ECA',
               'STD',
               'TGT',
               'USB',
               'ANR',
               'WFM',
               'TWO',
               'AFL',
               'SNDK',
               'PAA',
               'SDT',
               'NEM',
               'WYNN',
               'NVS',
               'UTX',
               'TVIX',
               'HON',
               'ARMH',
               'XLF',
               'NKE',
               'AEP',
               'STX',
               'NUE',
               'CF',
               'CCJ',
               'LNKD',
               'LMT',
               'WFT',
               'TNH',
               'BHI',
               'PGH',
               'DANG',
               'UPS',
               'KERX',
               'CELG',
               'FFIV',
               'CREE',
               'ACI',
               'GILD',
               'HTS',
               'LOW',
               'CYS',
               'PSEC',
               'CVS',
               'BBY',
               'D',
               'P',
               'AKAM',
               'O',
               'STO',
               'AIS',
               'GDXJ',
               'APC',
               'FAS',
               'TLT',
               'SNY',
               'AMGN',
               'GIS',
               'MT']
            
