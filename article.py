#!/usr/bin/env python

from random import choice
from random import shuffle
import screens
import re, datetime
from screens import abbrevs
from screens import intros
from screens import intro_endings
from screens import summaries
from screens import titles
from tickerlist import TickerList
from company import Company
from descriptions import descriptions as descs
from utils import find_between
from utils import get_pretty_html

# BM - Basic Materials
# CO - Conglomerates
# CG - Consumer Goods
# F  - Financial
# H  - healthcare
# IG - Industrial Goods
# S  - Services
# T  - Technology
# U  - Utilities

trend_screens = set(['52WH', '52WL']) #'BE', 'BU', 
type_screens = set(['D'])
cap_screens = set(['SC', 'MC', 'LC', 'MG' ])
liquidity_screens = set(['CR','QR'])
yield_screens = set(['DH','DVH'])
sector_screens = set(['BI','BM','CG','CO','CS','DMM','F',
                      'H','I','IIP','IMM',
                      'IOG','MOG','OGD','REIT',
                      'T','U']) 
low_value_screens = set(['LFPE','PER','PEG','PBVR','PCFR','PSR'])
debt_screens = set(['DER','LDER'])
profit_screens = set(['EPSG','NM','OPM','ROA','ROE'])

def make_profit_title():
    adj = choice( ['Disciplined', 'Strong', 'Impressive', 'Great', 'Sound',
                   'Solid', 'Hearty', 'Killer', 'Lean And Mean', 'High',
                   'Hefty', 'Legit', 'Strong Sources Of', 'Outperforming' ] )    
    subj = choice(['Profitability','Profits', 'Earnings', 'Earnings Trends'])
    title = choice( [ 'With ' + adj + ' ' + subj,
                      choice(['Raking In', 
                              'Bringing In',
                              'Killing It On',
                              'Keep Returning',                   
                              'Commanding',
                              'Returning',                              
                              'Showing Lean And Mean',
                              'With Lean/Mean',                              
                              'Operating With']) + ' Profits' ] )
    return title

class Article:
    def __init__(self, screen):
        self.screen = screen
        self.tickerlist = TickerList( screen )
        tickers = set( self.tickerlist.tickers )
        # get at least 3 companies        
        num_companies = len( self.tickerlist.tickers )
        if num_companies < 3:
            self.num_companies = 0
        else:
            self.num_companies = num_companies

    def make_title(self):
        title = str(self.num_companies)
        screen = self.screen

        if screen[0] != '':
            title = title + " " + abbrevs[ screen[0] ]
        if screen[1] != '':
            title = title + " " + abbrevs[ screen[1] ]
        if screen[2] != '':
            title = title + " " + abbrevs[ screen[2] ]
        title = title + " Stocks"

        profit = 0        
        low_value = 0
        liquid = 0
        debt = 0        
        qualifier = 0
        for major_screen in screen[3:]:
            if major_screen == '':
                continue
            if major_screen in list(profit_screens):
                if profit == 0:
                    profit = 1
                    qualifier = qualifier + 1
                    addition = make_profit_title()
                else:
                    continue
            elif major_screen in list(low_value_screens):
                if low_value == 0:
                    low_value = 1
                    qualifier = qualifier + 1
                    addition = choice( titles[ major_screen ] )
                else:
                    continue
            elif major_screen in list(liquidity_screens):
                if liquid == 0:
                    liquid = 1
                    qualifier = qualifier + 1
                    addition = choice( titles[ major_screen ] )
                else:
                    continue
            elif major_screen in list(debt_screens):
                if debt == 0:
                    debt = 1
                    qualifier = qualifier + 1
                    addition = choice( titles[ major_screen ] )
                else:
                    continue
            else:
                qualifier = qualifier + 1                
                addition = choice( titles[ major_screen ] )

            if qualifier == 1:
                title = title + " " + addition
            elif qualifier == 2:
                title = title + " But " + addition
            elif qualifier == 2:
                title = title + " And " + addition

        self.title = title
        
    def make_intro(self):
        intro = []
        sector = 0        
        low_value = 0
        profit = 0
        liquidity = 0
        debt = 0        
        trend = 0
        for screen in self.screen:
            if screen == '':
                continue
            key = screen
            if screen in sector_screens:
                if sector == 0:
                    key = 'sector'
                    sector = 1                    
                else:
                    continue
            elif screen in low_value_screens:
                if low_value == 0:
                    key = 'low_value'
                    low_value = 1                    
                else:
                    continue
            elif screen in profit_screens:
                if profit == 0:
                    key = 'profit'
                    profit = 1                    
                else:
                    continue
            elif screen in trend_screens:
                if trend == 0:
                    key = 'trend'
                    trend = 1                    
                else:
                    continue
            if screen in liquidity_screens:
                if liquidity == 0:
                    key = 'liquidity'
                    liquidity = 1                    
                else:
                    continue
            if screen in debt_screens:
                if debt == 0:
                    key = 'debt'
                    debt = 1                    
                else:
                    continue
            start = choice( intros[ key ] )
            if key == 'sector':
                start = start % abbrevs[screen].lower()
            intro.append( start )
                    
        intro.append( choice( intro_endings ) )
        intro = ' '.join( intro )
        self.intro = intro

    def scrape_intros(self):
        
        base_url = 'http://seekingalpha.com/author/zetakap/articles'
        begin = '<a class="dashboard_article_link" '
        end = '</a>'
        page = 4
        article_candidates = {}

        keywords = screens.get_keywords( self.screen )

        while len( article_candidates ) < 4:
            page = page + 1
            if page > 17:
                break
            url = base_url + '/' + str( page )
            print url
            pretty_html = get_pretty_html( url )
            while find_between( pretty_html, begin, end ):
                counter = 0
                author_content = find_between( pretty_html, begin, end )
                content_array = author_content.split('>')
                title = content_array[1].strip()
                for keyword_set in keywords:
                    for keyword in keyword_set:
                        if keyword in title:
                            counter = counter + 1
                            break
                if counter >= len(keywords) - 1:
                    link = content_array[0].strip()
                    article_link = 'http://seekingalpha.com' + link.replace('href="','').replace('"','')
                    article_candidates[title] = article_link
                    if len( article_candidates ) == 3:
                        break
                pretty_html = pretty_html.replace( begin, '', 1 )

        scraped_titles = []
        scraped_intros = []
        for title, link in article_candidates.items():
            print title
            scraped_titles.append( title )
            article_html = get_pretty_html( link )
            begin = '<div id="article_body" itemprop="articleBody">'
            end = '</p>'
            article_content = find_between( article_html, begin, end )
            scraped_intros.append( article_content.strip() + '</p>' )
            
        self.scraped_titles = scraped_titles            
        self.scraped_intros = scraped_intros

    def print_scraped_titles(self):
        titles = ''
        for title in self.scraped_titles:
            title = str(self.num_companies) + title[1:]
            titles = titles + "\n<p>" + title + "\n</p>"
        return titles
        
    def print_scraped_intros(self):
        intros = ''
        for intro in self.scraped_intros:
            intros = intros + "\n" + intro + "\n"
        return intros
    
    def make_descs(self):
        self.descs = []        
        for screen in self.screen:
            if screen != '':
                self.descs.append( descs[screen] )

    def print_descs(self):
        descs = ''
        for desc in self.descs:
            descs = descs + "\n<p>" + desc + "</p>"
        return descs

    def make_conclusion(self):
        qualifier = ''        
        if self.screen[0] != '':
            qualifier = abbrevs[ self.screen[0] ]
            qualifier = qualifier.lower().replace(' ','-') + ' '
        beginning = "Do you think these %sstocks "
        middle = choice( [ "hold value that has yet to be priced in?",
                           "have strong enough fundamentals to move higher?",
                           "have more value to price in?",
                           "are undervalued and should be trading higher?",
                           "will continue to see such strong profitability?",
                           "offer both value and growth?",
                           "have what it takes to grow?",
                           "failed to price their value accurately?",
                           "are worth more than the market currently says?",
                           "deserve to grow higher?",
                           "deserve to trade higher?",
                           "are undervalued?",                           
                           "have higher to rise?",
                           "are in strong positions for future growth?",
                           "have strong fundamentals?",
                           "have strong operations?",
                           "will break through to new highs?",
                           "hold solid value?",
                           "have a positive future in store?",
                           "have a strong outlook?",                           
                           "will outperform?",
                           "should be trading higher?",
                           "can offer attractive returns?",
                           "will offer healthy returns?",
                           "will perform well?",                           
                           "should have higher valuations?",
                           "should be priced higher?",                           
                           "are undervalued and have room to trade higher?",
                           "are at too low of valuations, given their fundamentals?",
                           "are worth more than their current valuations?",
                           "will trade at a higher valuation?",
                           "will go up in valuation?",
                           "will go up in price?"                       
                           ] ) 
        end = choice( [" Use our screened list as a starting point for your own analysis.",
                       " Use our list along with your own analysis.",
                       " Please use our list to assist with your own analysis.",
                       " Use our list to help with your own analysis.",                       
                       " Use this list as a starting-off point for your own analysis."] )
                      
        conclusion = beginning + middle + end
        self.conclusion = conclusion % qualifier
        
    def make_summary(self, screen):
        joiners = ["We then looked for companies",
                   "We then looked for businesses",
                   "We then screened for businesses",
                   "Next, we then screened for businesses",
                   "We next screened for businesses",
                   "From here, we then looked for companies"]
        
        summary = []
        minor_yield = ''
        summary.append( "We first looked for" )
        for minor in [screen[0],screen[1],screen[2]]:
            if minor != '' and minor in set.union( type_screens, cap_screens, sector_screens):            
                summary.append( abbrevs[ minor ].lower() )
            elif minor in yield_screens:
                minor_yield = minor
        if minor_yield != '':
            summary.append("stocks" + ' ' + choice( summaries[ minor_yield ] ) )            
        else:
            summary.append("stocks")             
    
        summary = [ ' '.join( summary ) ]
        
        profit = 0        
        low_value = 0
        liquid = 0
        additions = []
        group = False
        
        for major_screen in screen[3:]:
            if major_screen == '':
                continue
            addition = choice( summaries[ major_screen ] )            
            if major_screen in profit_screens:
                if profit == 0:
                    profit = 1
                else:
                    addition = "(" + addition[addition.find("(")+1:addition.find(")")] + ")"
                    group = True
            elif major_screen in low_value_screens:
                if low_value == 0:
                    low_value = 1
                else:
                    addition = "(" + addition[addition.find("(")+1:addition.find(")")] + ")"
                    group = True                    
            elif major_screen in liquidity_screens:
                if liquid == 0:
                    liquid = 1
                else:
                    addition = "(" + addition[addition.find("(")+1:addition.find(")")] + ")"
                    group = True
            if group:
                additions[-1] = additions[-1].replace('.','') + addition + '.'
                group = False
            else:
                additions.append( choice(joiners) + ' ' + addition + '.' )

        summary = [ summary[0] + '. '  + (' '.join( additions ) ) ]
        
        not_screened = []
        if screen[0] == '':
            not_screened.append( "market caps" )
        if screen[1] == '':
            not_screened.append( "sectors" )
        if len( not_screened ) > 0:
            not_screened = " or ".join( not_screened ) + "."            
            not_screened = "We did not screen out any " + not_screened
            summary.append( not_screened )
        
        summary = ' '.join( summary )
        self.summary = summary
        
    def make_profiles(self):
        num_companies_removed = 0
        self.profiles = []
        shuffle(self.tickerlist.tickers)
        for ticker in self.tickerlist.tickers[:self.num_companies]:                
            company = Company( ticker, self.screen )
            company.populate()
            if company.cap == '0':
                num_companies_removed = num_companies_removed + 1
                continue
            self.profiles.append( company.profile )
        self.num_companies = self.num_companies - num_companies_removed

    def print_profiles(self):
        profiles = ''
        list_order = 1
        for profile in self.profiles:
            profiles = profiles + "\n<p>" + "<b>" + str(list_order) + ")</b> " + profile + "</p>"
            list_order = list_order + 1
        return profiles
        
    def make_disclaimer(self):
        date = datetime.datetime.now()
        self.disclaimer = "\n\n*Company profiles were sourced from Google Finance and Yahoo Finance. Financial data was sourced from Finviz" + " on " + date.strftime("%m/%d/%Y") + ".\n"

    def make_article(self):
        self.make_profiles()
        if self.num_companies < 3:
            return False
        self.make_intro()
        self.scrape_intros()        
        self.make_descs()
        self.make_summary(self.screen)
        self.make_conclusion()
        self.make_disclaimer()
        # make title last so that num_companies is updated
        self.make_title()
        
    def print_article(self):
        article_text = ''
        article_text = article_text + "<p>" + "--------- The title below is a computer generated template title ----------------------------" + "</p>\n"        
        article_text = self.title + "\n\n"
        article_text = article_text + "<p>" + "--------- The following titles are from past published articles -----------------------------" + "</p>\n"        
        article_text = article_text + self.print_scraped_titles() + "\n\n"
        article_text = article_text + "<p>" + "--------- The following intro is computer generated and should probably just be deleted -----" + "</p>\n"        
        article_text = article_text + "<p>" + self.intro + "</p>\n"
        article_text = article_text + "<p>" + "--------- The following paragraphs are intros from past published articles ------------------" + "</p>\n"
        article_text = article_text + self.print_scraped_intros() + "\n"
        article_text = article_text + "<p>" + "--------- You shouldn't have to edit anything below this line -------------------------------" + "</p>\n"
        article_text = article_text + self.print_descs() + "\n"       
        article_text = article_text + "<p>" + self.summary + "</p>\n"
        article_text = article_text + "<div>" + self.conclusion + "</div>\n"
        article_text = article_text + "<div>" + self.print_profiles() + "</div>\n"
        article_text = article_text + "<p>" + self.disclaimer + "</p>"

        print article_text
        return article_text

        
