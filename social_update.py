#!/usr/bin/env python
import bitly
import posterous
import blogspot
import smtplib
import credentials
import xml.etree.ElementTree as ET
import urllib2
import sys

def make_tweet(title,url,tickers):

    tickers = ' '.join( tickers )
    tweet = title + ' ' + url + ' ' + tickers
    if len(tweet) > 140:
        tweet = url + ' ' + tickers
        new_title = ''
        for word in title.split():
            if len( new_title + ' ' + word + '... ' + tweet) < 140 :
                new_title = new_title + ' ' + word
            else:
                new_title = new_title + '... '
                break
        tweet = new_title + ' ' + tweet
    assert( len(tweet) > 0 and len(tweet) <= 140 )
    return tweet

zeta_url = 'http://zetakap.posterous.com/rss.xml'
sa_url = 'http://seekingalpha.com/author/zetakap.xml'

zeta_xml = urllib2.urlopen( zeta_url ).read()
zeta_root = ET.fromstring( zeta_xml )

sa_xml = urllib2.urlopen( sa_url ).read()
sa_root = ET.fromstring( sa_xml )

last_post = zeta_root.findall('channel/item')[0]
pubdate = last_post.find('pubDate').text

from email.utils import mktime_tz, parsedate_tz
from time import asctime, gmtime, mktime
last_post_mktime = mktime(gmtime(mktime_tz(parsedate_tz(pubdate))))
last_post_asctime = asctime(gmtime(last_post_mktime))

tweets = []

for item in sa_root.findall('channel/item'):

    sa_pubdate = item.find('pubDate').text
    sa_mktime = mktime(gmtime(mktime_tz(parsedate_tz(sa_pubdate))))
    sa_asctime = asctime(gmtime(sa_mktime))

    tickers = []
    for symbol in item.findall('category')[:-1]:
        tickers.append( '$' + symbol.text )

    if sa_mktime > last_post_mktime:
        title = item.find('title').text        
        text = item.find('content').text.replace('<p>','').replace('</p>','')
        link = item.find('link').text
        if link.find('?') > 0:
            link = link[0:link.find('?')]

        # bitly
        short_url = bitly.Api( login = bitly.API_USERNAME, apikey = bitly.API_KEY ).shorten(link)
        print 'Short URL: ' + short_url

        # twitter
        tweet = make_tweet( title, short_url, tickers ).strip()
        if len( tweet ) + len( ' @ZetaKap' ) < 140:
            tweet = tweet + ' @ZetaKap'
        tweets.append( tweet )
        
        # posterous
        post = posterous.Posterous( title, text, short_url )
        post.text = post.text
        print post.text
        post.send_post()

        # blogspot
        blog_entry = blogspot.CreatePublicPost(title, text, short_url)
        print blog_entry
    else:
        break

# only send an email when there are new tweets    
if len( tweets ) == 0:
    sys.exit()

FROM = 'daniel.raymond.andrews@gmail.com'
TO = ['daniel.raymond.andrews+zetakap@gmail.com',
      'zetakap.media@gmail.com']
    
SUBJECT = "Seeking Alpha - Make Social Update"

TEXT = "\n"
for tweet in tweets:
    print tweet
    TEXT = TEXT + tweet + "\n\n"

# Prepare actual message
message = """\
From: %s
To: %s
Subject: %s

%s

http://seekingalpha.com/author/zetakap/stocktalk

""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login( credentials.USERNAME, credentials.PASSWORD )  
server.sendmail(FROM, TO, message)  
server.quit()
