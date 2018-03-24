import tweepy
import datetime
import time
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
filePath = '/home/gbk/data/makerScrape/'
class MyListener(StreamListener):

  def __init__(self, start_time, time_limit=2700):
    self.time = start_time
    self.limit = time_limit

  def on_data(self, data):
    jsonFile = filePath + datetime.datetime.now().strftime('%Y_%m_%d') + '_maker.json'
    while (time.time() - self.time) < self.limit:
      print(str(time.time() - self.time) + ' ' + str(self.limit))
      try:
        with open(jsonFile, 'a') as f:
          f.write(data)
          return True
      except BaseException as e:
        print("Error on_data: %s" % str(e))
      return True
    return False

  def on_error(self, status):
    print(status)
    return True
startTime = time.time()
twitter_stream = Stream(auth, MyListener(startTime))
twitter_stream.filter(track=['#maker'])

