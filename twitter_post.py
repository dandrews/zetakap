#!/usr/bin/env python
import twitter

CONSUMER_KEY='jW2fTJyPktYZTiyKDC1GkQ'
CONSUMER_SECRET='xbDiMW43X7Qd3pZlTTEdk0CgeCL8Y5pOwghY9exOg'

# zetakap
ACCESS_TOKEN_KEY = '554914158-a9Dlek67wSnSM2Z3tup3XHfmQIzPApehdqmbnGEU'
ACCESS_TOKEN_SECRET = '2NsHfKhHbfAqRsn5yykutT0ZiCubcYT126p894ozEN4'

client = twitter.Api(consumer_key=CONSUMER_KEY
                     ,consumer_secret=CONSUMER_SECRET
                     ,access_token_key=ACCESS_TOKEN_KEY
                     ,access_token_secret=ACCESS_TOKEN_SECRET)

#print client
#print dir(client)

friends = client.GetFriends()
followers = []
for friend in friends:
    followers.append( friend.screen_name )
    
#print client.CreateFriendship('the_dan_bot')
#results = client.GetSearch('4 Mid-Cap Stocks With No Debt But Raking In Profits')

#for result in results:
#    print result.user.screen_name
    #print result.text
    #print result.user
    
# update = client.PostUpdate('ZetaKap now has a posterous blog: http://bit.ly/IDR2NY')

# print update
