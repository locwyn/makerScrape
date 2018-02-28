import tweepy
import datetime
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'dgmlPcoo2F3Ws6LWJLmuTgOVb'
consumer_secret = 'cME0sSMXOXHO3qG06tEwSyejzvlYlqLzx1ynKRBqGjbuYRIOZz'
access_token = '903791836791267328-otZ5372pWtzUDvSEOU9IWeSyPojrnz5'
access_secret = 'cfCMYG8815czjkRljOo1HAvg09pvu9GPyFVMmfKZOI4XD'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#for status in tweepy.Cursor(api.home_timeline).items(10):
#  #Process a single status
#  print(status.text)

#testing streaming
class MyListener(StreamListener):

  def on_data(self, data):
    jsonFile = datetime.datetime.now().strftime('%Y_%d_%m') + '_maker,json'
    try:
      with open(jsonFile, 'a') as f:
        f.write(data)
        return True
    except BaseException as e:
      print("Error on_data: %s" % str(e))
    return True

  def on_error(self, status):
    print(status)
    return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#maker'])

