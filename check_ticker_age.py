#!/usr/bin/env python

from utils import find_between
from utils import get_pretty_html
import parsedatetime.parsedatetime as pdt
import parsedatetime.parsedatetime_consts as pdc
from time import mktime, gmtime

def is_old_enough( pub_date ):

    pub_time = mktime( pub_date )

    c = pdc.Constants()
    p = pdt.Calendar(c)
    
    today = p.parse("today")[0]
    today_time = mktime( ( today.tm_year,
                                today.tm_mon,
                                today.tm_mday,
                                0, 0, 0,
                                today.tm_wday,
                                today.tm_yday,
                                1 ) )

    min_age = 25 * 24 * 3600
    if today_time - pub_time > min_age:
        return True
    else:
        return False

def get_ticker_article_age( sym ):

    sym_url = 'http://seekingalpha.com/symbol/' + sym.lower()
    
    html = get_pretty_html( sym_url )

    begin = '<a href="/author/zetakap">'
    end = '</li>'
    author_content = find_between( html, begin, end )

    if author_content == '':
        return gmtime(0)
    else:
        begin = '</span>'
        end = '<span class="bullet">'              
        date = find_between( author_content, begin, end )

        date = date.strip()

        c = pdc.Constants()
        p = pdt.Calendar(c)
    
        most_recent_pub_date = date.replace('on','',1).strip()
        date = p.parse("this year")

        result = p.parseDateText( " ".join( [ most_recent_pub_date, str( date[0].tm_year ) ] ) )

        return result



