#!/usr/bin/env python

import re, datetime
import utils
from screens import abbrevs
from screens import ignored
from screens import html_maps
from utils import get_pretty_html
from utils import find_between

class Company:
    def __init__(self, ticker, screen):
        self.ticker = ticker
        #print "ticker"
        #print ticker
        self.screen = screen
        self.screen_pairs = []
        self.screen_desc = ''
        profile_url = "http://finviz.com/quote.ashx?t=" + ticker
        #print profile_url
        self.html = get_pretty_html( profile_url )

    def set_name(self):
        begin = 'target="_blank" class="tab-link">'
        end = '</a>'
        name = find_between( self.html, begin, end )
        self.name = name.replace('<b>','').replace('</b>','').strip()

    def set_desc(self):
        begin = '<td class="fullview-profile" align="left">'
        end = '</td>'
        desc = find_between( self.html, begin, end )
        num_periods = self.name.count('.') + 3
        self.desc = '.'.join( desc.strip().split('.')[0:num_periods] ) + '.'
        
    def set_sector(self):
        begin = '<a href="screener.ashx?v=111&amp;f=sec_'
        end = '" class="tab-link">'
        sec = find_between( self.html, begin, end )
        begin = '<a href="screener.ashx?v=111&amp;f=sec_' + sec + '" class="tab-link">'
        end = '</a>'
        sector = find_between( self.html, begin, end )
        self.sector = sector.strip()
        
    def set_industry(self):
        begin = '<a href="screener.ashx?v=111&amp;f=ind_'
        end = '" class="tab-link">'
        ind = find_between( self.html, begin, end )
        begin = '<a href="screener.ashx?v=111&amp;f=ind_' + ind + '" class="tab-link">'
        end = '</a>'
        industry = find_between( self.html, begin, end )
        self.industry = industry.strip()

    def set_cap(self):
        begin = 'body=[Market capitalization]'
        end = '</b>'
        cap_html = find_between( self.html, begin, end )
        if cap_html == '' or len(cap_html) == 1:
            self.cap = cap_html
            return
        cap = cap_html.split('<b>')[1]
        self.cap = re.sub(r'<[^>]*?>', '', cap).strip()

    def set_short(self):
        begin = 'body=[Short interest share]'
        end = '</b>'
        short_html = find_between( self.html, begin, end )
        if short_html == '' or len(short_html) == 1:
            self.short_interest = short_html
            return
        short = short_html.split('<b>')[1]
        self.short_interest = re.sub(r'<[^>]*?>', '', short).strip()

    def set_screen_pairs(self):
        ind = 0
        for screen in self.screen:
            if screen in ['D','DH','DVH']:
                ind = self.screen.index(screen) + 1
                self.screen.insert( ind,'PO' )
                break
        for screen in self.screen:
            if screen == '' or screen in ignored:
                continue
            begin = "body=[%s]" % html_maps[screen]
            end = '</b>'
            screen_html = find_between( self.html, begin, end )
            if screen_html == '' or len(screen_html) == 1:
                continue
            screen_value = screen_html.split('<b>')[1]
            pair = [ abbrevs[screen], re.sub(r'<[^>]*?>', '', screen_value).strip() ]
            self.screen_pairs.append( pair )
        if 'PO' in self.screen:
            self.screen.remove('PO')

    def set_screen_desc(self):
        if self.name != '':
            screen_desc = "\n" + self.name + " has a "
        else:
            screen_desc = "\n" + "This company" + " has a "
        desc = []
        for screen_pair in self.screen_pairs:
            name = screen_pair[0]
            value = str(screen_pair[1])            
            if name in set(['Dividend', 'High Yield Dividend', 'Very High Yield Dividend']):
                name = 'Dividend Yield'
                
            if name == '52 Week High':
                desc.append( "trading below it's " + name + " by " + value )                
                continue
            elif name == '52 Week Low':
                desc.append( "trading above it's " + name + " by " + value )
                continue
            else:
                desc.append( name + " of " + value )
        self.screen_desc = screen_desc + " and ".join( desc ) + "."

    def set_beta(self):
        begin = 'body=[Beta]'
        end = '</b>'
        beta_html = find_between( self.html, begin, end )
        if beta_html == '' or len(beta_html) == 1:
            self.beta = beta_html
            return
        beta = beta_html.split('<b>')[1]
        self.beta = re.sub(r'<[^>]*?>', '', beta).strip()

    def get_profile(self):
        date = datetime.datetime.now()

        self.profile = "\n".join(
            [ "<b>" + self.name + " (" + self.ticker + ")" + "</b>",
              "<table>",
                  "<tr>",
                      "<td>",
                      "Sector: ",
                      "</td>",
                      "<td>",
                      self.sector,
                      "</td>",
                  "</tr>",
                  "<tr>",
                      "<td>",              
                      "Industry: ",
                      "</td>",
                      "<td>",              
                      self.industry,
                      "</td>",
                  "</tr>",
                  "<tr>",
                      "<td>",              
                      "Market Cap: ",
                      "</td>",
                       "<td>",              
                      "$" + self.cap,
                      "</td>",
                  "</tr>",
                  "<tr>",
                      "<td>",              
                      "Beta: ",
                      "</td>",
                       "<td>",              
                      self.beta,
                      "</td>",
                  "</tr>",
              "</table>",
              "<p>",
              self.screen_desc,
              "The short interest was " + self.short_interest + " as of " + date.strftime("%m/%d/%Y") + ".",
              self.desc,
              "</p>"]
            )
        
    def populate(self):
        self.set_name()
        self.set_desc()
        self.set_sector()
        self.set_industry()
        self.set_cap()
        self.set_beta()
        self.set_screen_pairs()
        self.set_screen_desc()
        self.set_short()
        # fill in profile
        self.get_profile()
        
