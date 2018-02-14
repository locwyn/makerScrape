import tweepy
from tweepy import OAuthHandler

consumer_key = 'dgmlPcoo2F3Ws6LWJLmuTgOVb'
consumer_secret = 'cME0sSMXOXHO3qG06tEwSyejzvlYlqLzx1ynKRBqGjbuYRIOZz'
access_token = '903791836791267328-otZ5372pWtzUDvSEOU9IWeSyPojrnz5'
access_secret = 'cfCMYG8815czjkRljOo1HAvg09pvu9GPyFVMmfKZOI4XD'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
