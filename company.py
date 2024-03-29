#!/usr/bin/env python

import re
import utils
from screens import abbrevs
from screens import ignored
from screens import html_maps
from utils import get_pretty_html
from utils import find_between

class Company:
    def __init__(self, ticker, screen):
        self.ticker = ticker
        self.screen = screen
        self.screen_pairs = []
        self.screen_table = ''
        profile_url = "http://finviz.com/quote.ashx?t=" + ticker
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
        self.desc = desc.strip()
        
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
        cap = re.sub(r'<[^>]*?>', '', cap).strip()
        if 'M' in cap:
            temp_cap = cap.replace('M','')
            if long(float(temp_cap)) < 100:
                self.cap = '0'
                return
        self.cap = cap

    def set_short(self):
        begin = 'body=[Short interest share]'
        end = '</b>'
        short_html = find_between( self.html, begin, end )
        if short_html == '' or len(short_html) == 1:
            self.short_interest = short_html
            return
        short = short_html.split('<b>')[1]
        short = re.sub(r'<[^>]*?>', '', short).strip()
        temp_short = short.replace('%','')
        if temp_short == '-' or float(temp_short) > 12:
            self.short_interest = '100%'
            return
        self.short_interest = short

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

    def set_chart_html(self):
        self.chart_html = '<p><img src="http://finviz.com/chart.ashx?t=' + self.ticker + '&amp;ty=c&amp;ta=1&amp;p=d&amp;s=l" alt="' + self.ticker + ' stock chart" /></p>'

    def set_screen_table(self):
        screen_table = '<p><strong>Key Metrics</strong></p>'
        screen_table = screen_table + '<table border="1" cellpadding="1" cellspacing="1" class="designed_table"><tbody>'
        for screen_pair in self.screen_pairs:
            name = screen_pair[0]
            value = str(screen_pair[1])            
            if name in set(['Dividend', 'High Yield Dividend', 'Very High Yield Dividend']):
                name = 'Dividend Yield'
            if name == 'Payout Ratio':
                if value == '-' or value == '0.00%':
                    continue
            screen_table = screen_table + '<tr><td>' + name + '</td><td>' + value + '</td></tr>'
        screen_table = screen_table + '<tr><td>' + "Short Interest" + '</td><td>' + self.short_interest  + '</td></tr>'
        self.screen_table = screen_table + '</tbody></table>'
        
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
        self.profile = "\n".join(
            [ "<b>" + self.name + " (" + self.ticker + ")" + "</b>",
              '<table border="1" cellpadding="1" cellspacing="1" class="designed_table">',
                  "<tr>",
                      "<td>",
                      "Sector",
                      "</td>",
                      "<td>",
                      self.sector,
                      "</td>",
                  "</tr>",
                  "<tr>",
                      "<td>",              
                      "Industry",
                      "</td>",
                      "<td>",              
                      self.industry,
                      "</td>",
                  "</tr>",
                  "<tr>",
                      "<td>",              
                      "Market Cap",
                      "</td>",
                       "<td>",              
                      "$" + self.cap,
                      "</td>",
                  "</tr>",
                  "<tr>",
                      "<td>",              
                      "Beta",
                      "</td>",
                       "<td>",              
                      self.beta,
                      "</td>",
                  "</tr>",
              "</table>",
              "<p>",
              self.chart_html,              
              self.screen_table,
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
        self.set_short()
        self.set_chart_html()
        self.set_screen_table()
        # fill in profile
        self.get_profile()
        
