import tweepy
import time 

auth = tweepy.OAuthHandler('gwrB0lVHt6rilqMEZ3moqhw9B','vUyNmYn3VUtySREe0635n0WPCVFyiYwgPGIzps73RIUtCXXsA1')
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


#1239550280850649094-iWgIQUejrUthuO8oegB66e6qh96pZ1 Access token
#5ggmVnuJBVB8NXr6yI33BiS3MjRhWZ0Vze0LqB9D9B4Im Acess token secret
#gwrB0lVHt6rilqMEZ3moqhw9B API Key
#vUyNmYn3VUtySREe0635n0WPCVFyiYwgPGIzps73RIUtCXXsA1 API Secret
