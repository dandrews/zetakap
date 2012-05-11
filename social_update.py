#!/usr/bin/env python
import bitly
import twitter_post
import posterous
import blogspot
import xml.etree.ElementTree as ET
import urllib2
from random import choice
import sys

def make_tweet(title,url,tickers):
    intros = ['Check out the latest:',
              'Latest article:',
              'Fresh article:',
              '',
              '',
              '',
              'Fresh post:',
              'Another hot post:',
              'Our newest post:',
              'Just published:',
              'Just posted:',
              'Another good post:',
              'Another Goody:',
              'Newest:',
              'Latest:',
              'Brand new post:',
              'Newly Pressed:',
              'Just posted online:',
              'Our Newest:',
              'Fresh blog post:',
              'Out Now:',
              'Up & Running:',
              'Just Posted Up:',                    
              'Newly published:',                    
              'Latest post:',
              'Check the Latest:',
              'Check it out:',
              'Check it:',                    
              'Hot of the press:',
              'Our latest post:',                    
              'Newest post:']
    tweet = ''
    while len(tweet) == 0 or len(tweet) > 140:
        tweet = choice(intros) + ' ' + title + ' ' + url + tickers
    if len(tweet) + len('$$ ') < 140:
        tweet = '$$ ' + tweet
    assert( len(tweet) > 0 and len(tweet) <= 140 )
    return tweet


zeta_url = 'http://zetakap.posterous.com/rss.xml'
sa_url = 'http://seekingalpha.com/author/zetakap.xml'

zeta_xml = urllib2.urlopen( zeta_url ).read()
zeta_root = ET.fromstring( zeta_xml )

# blogspot_xml = urllib2.urlopen( blogspot_url ).read()
# blogspot_root = ET.fromstring( blogspot_xml )

sa_xml = urllib2.urlopen( sa_url ).read()
sa_root = ET.fromstring( sa_xml )

#print len( sa_root.findall('channel/item') ) - len( zeta_root.findall('channel/item') )    

last_post = zeta_root.findall('channel/item')[0]
pubdate = last_post.find('pubDate').text

# last_post = blogspot_root.findall('channel/item')[0]
# pubdate = last_post.find('pubDate').text

from email.utils import mktime_tz, parsedate_tz
from time import asctime, gmtime, mktime
last_post_mktime = mktime(gmtime(mktime_tz(parsedate_tz(pubdate))))
last_post_asctime = asctime(gmtime(last_post_mktime))

# print "\t last_post mktime: {0} - {1}".format(last_post_mktime, last_post_asctime)

for item in sa_root.findall('channel/item'):

    sa_pubdate = item.find('pubDate').text
    sa_mktime = mktime(gmtime(mktime_tz(parsedate_tz(sa_pubdate))))
    sa_asctime = asctime(gmtime(sa_mktime))
    # print "\t SA mktime: {0} - {1}".format(sa_mktime, sa_asctime)

    tickers = ''
    for symbol in item.findall('category')[:-1]:
        tickers = tickers + ' $' + symbol.text

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
        tweet = make_tweet( title, short_url, tickers )
        if len( tweet ) + len( ' #ZetaKap' ) < 140:
            tweet = tweet + ' #ZetaKap'
        update = twitter_post.client.PostUpdate( tweet )

        print tweet.replace("#", "@")
        
        # posterous
        post = posterous.Posterous( title, text, short_url )
        post.text = post.text # + ' ... <a href=\'' + short_url + '\'>Read the rest at SeekingAlpha.com</a>'
        print post.text
        post.send_post()

        # blogspot
        blog_entry = blogspot.CreatePublicPost(title, text, short_url)
        print blog_entry
    else:
        break

    # print item.find('link').text
    # if item.find('content'):
    #     print item.find('content').text.replace('<p>','').replace('</p>','')

