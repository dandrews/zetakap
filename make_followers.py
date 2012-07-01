#!/usr/bin/env python

import twitter_post
import update_email
import smtplib
import xml.etree.ElementTree as ET
import urllib2

sa_url = 'http://seekingalpha.com/author/zetakap.xml'
sa_xml = urllib2.urlopen( sa_url ).read()
sa_root = ET.fromstring( sa_xml )

friends = twitter_post.client.GetFriends()
followers = ['ZetaKap',
             'jazzmantic',
             'SeekingAlpha',
             'biztradenews',
             'WallStJesus',
             'AlenKarabegovic']
for friend in friends:
    followers.append( friend.screen_name )

# follow anyone who tweets your articles
for item in sa_root.findall('channel/item'):
    title = item.find('title').text        
    results = twitter_post.client.GetSearch(title)
    for result in results:
        screen_name = result.user.screen_name
        if screen_name not in followers:
            print screen_name
            print twitter_post.client.CreateFriendship(screen_name)

# make sure to follow people who follow you
following = []            
current_followers = twitter_post.client.GetFollowers()
for follow in current_followers:
    screen_name = follow.screen_name
    if screen_name not in followers:
        twitter_post.client.CreateFriendship(screen_name)
        following.append( screen_name )

msg = "New following:\n"
for name in following:
    msg = msg + name + "\n"
    
# Send an update email
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login( update_email.USERNAME, update_email.PASSWORD )  
server.sendmail(update_email.fromaddr, update_email.toaddrs, msg)  
server.quit()

        
