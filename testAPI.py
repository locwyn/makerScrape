import tweepy
from tweepy import OAuthHandler

consumer_key = 'dgmlPcoo2F3Ws6LWJLmuTgOVb'
consumer_secret = 'cME0sSMXOXHO3qG06tEwSyejzvlYlqLzx1ynKRBqGjbuYRIOZz'
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
