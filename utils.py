import urllib2
from tidylib import tidy_document
from BeautifulSoup import BeautifulSoup as bs

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ''

def get_pretty_html( url ):
    feed = urllib2.urlopen( url )
    html = feed.read()
    OPTIONS = {
        "output-xhtml": 1,
        "indent": 1,
        "tidy-mark": 0,
        "wrap": 0,
        "alt-text": "",
        "doctype": 'strict',
        "force-output": 1,
        }
    document,errors = tidy_document( html, OPTIONS )
    root = str( document )
    soup = bs( root, convertEntities=bs.HTML_ENTITIES )     
    return soup.prettify()
    

