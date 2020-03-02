# -*- coding: utf-8 -*-

#pip install --upgrade pip
#pip install TwitterSearch
#pip install twitter


from TwitterSearch import *

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Guttenberg', 'Doktorarbeit']) # let's define all words we would like to have a look for
    tso.set_language('de') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(consumer_key='aiWCEBiWFiEnjnR2gW5fIcggi',
  consumer_secret='I9ra25juAZTVQbxOledUv0OW67dhWorol0DcYbFHszL5uQiXSs',
  access_token_key='1149066632087646208-ZpxWSHbu4yQcagbHUAfeLEQDxlowqQ',
  access_token_secret='0eqzpuFDI1E2H5Zl8pxTfWDxOFAXwoGIKn0dIdU8NL3in'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
import  twitter


api = twitter.Api()


print(api.VerifyCredentials())


busca = api.GetSearch("previdência") # Replace happy with your search
for tweet in busca:
    print(tweet.id, tweet.text)
