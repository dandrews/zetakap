#!/usr/bin/env python
import twitter_post
import credentials
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
             'AlenKarabegovic',
             'tonymmeyer']

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

# only send an email when there are new followed        
if len( following ) == 0:
    exit()

FROM = 'daniel.raymond.andrews@gmail.com'
TO = ['daniel.raymond.andrews+zetakap@gmail.com',
      'zetakap.media@gmail.com']

SUBJECT = "@ZetaKap twitter - newly following"

TEXT = "\n"
for name in following:
    TEXT = TEXT + name + "\n"

# Prepare actual message
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login( credentials.USERNAME, credentials.PASSWORD )  
server.sendmail(FROM, TO, message)  
server.quit()
