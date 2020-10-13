import tweepy
import time 

auth = tweepy.OAuthHandler('this is where the authkey goes')
auth.set_access_token(#place your unique access token here)
api = tweepy.API(auth)


user = api.me()
#there is a little issue with this function go back to it later 
def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


#follow bot
""" for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print(follower.name) """

#likes based off of keywords
search = 'matthew yauch'
numoftweets = 2
for tweet in tweepy.Cursor(api.search, search).items(numoftweets):
    try:
        tweet.favorite()
        print('i liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


