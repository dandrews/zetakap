#!/usr/bin/env python

import screens
import random
from screens import make_finviz_url
import utils
from utils import get_pretty_html
from utils import find_between
from check_ticker_age import is_old_enough
from check_ticker_age import get_ticker_article_age
import os

pwd = os.path.dirname(__file__)
article_path = pwd + "/Articles"
excluded_tickers = ['AAPL','TGS','BMA','EFC','MTGE']

class TickerList:
    def __init__(self, screen ):
        self.screen = screen
        pending_tickers = self.get_pending_tickers()
        url = make_finviz_url( screen )
        pretty_html = get_pretty_html( url )
        self.tickers = []
        counter = 0
        max_len = random.randrange(6, 7) 
        while find_between( pretty_html, '<a href="quote.ashx?t=', '&amp;' ):
            if counter > max_len:
                break        
            ticker = find_between( pretty_html, '<a href="quote.ashx?t=', '&amp;' )
            pretty_html = pretty_html.replace('<a href="quote.ashx?t=','',1)
            if ticker in pending_tickers:
                continue
            if ticker in excluded_tickers:
                continue
            print "testing ticker " + ticker
            # only take tickers older than 25 days
            age = get_ticker_article_age( ticker )
            if is_old_enough( age ):
                self.tickers.append( ticker )
                counter = counter + 1

    def get_pending_tickers(self):
        f = open( article_path + '/tickers.txt','a+' )
        pending_tickers = filter( None, f.read().split(',') )
        f.close()
        return pending_tickers

    def update_pending_tickers(self):
        f = open( article_path + '/tickers.txt','a+' )
        f.write( ','.join( self.tickers ) + ',' )
        f.close()
        return True
