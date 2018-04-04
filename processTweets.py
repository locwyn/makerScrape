import json
import mysql.connector

def databaseConnect():
  return mysql.connector.connect(user='pycon', password='fuzzywuzzy', host='localhost', database='makerTweets')

def checkDatabaseForTweet(tweetID):
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = "SELECT tweetID FROM tweets WHERE tweetID = 12345"
  cursor.execute(tweetQuery)
  results = 0
  for (tweetID) in cursor:
    results += 1
  cnx.close() 
  return results

#def loadTweetIntoDatabase(tweetJSON):
#  return

#def loadUserIntoDatabase(tweetJSON):
#  return

#def checkForRetweet(tweetJSON):
#  return

#def checkForEnglish(tweetJSON):
#  return

#need to set a minimum threshold for popularity
#def checkFollowerCount(tweetJSON):
#  return

#def collectHashtags(tweetJSON):
#  return

def pullTweetData(tweetJSON):
  tweetID = tweetJSON['id']
  tweetText = tweetJSON['text']
  userID = tweetJSON['user']['id']
  createdAt = tweetJSON['created_at']
  retweetCount = tweetJSON['retweet_count']
  print(','.join([str(tweetID), str(userID), createdAt, str(retweetCount)]))

def pullMakerData(tweetJSON):
  userID = tweetJSON['user']['id']
  userName = tweetJSON['user']['name']
  userScreenName = tweetJSON['user']['screen_name']
  location = tweetJSON['user']['location']
  description = tweetJSON['user']['description']
  followersCount = tweetJSON['user']['followers_count']
  friendsCount = tweetJSON['user']['friends_count']
  createdAt = tweetJSON['user']['created_at']
  print(','.join([str(userID), userName, userScreenName])) 
  print(','.join([location, str(followersCount), str(friendsCount)]))


def runTests():
  with open('2018_04_02_maker.json') as f:
    tweets = f.readlines()
  for y in tweets:
    tweetJSON = json.loads(y)
    pullMakerData(tweetJSON)

#checkDatabaseForTweet(12345)
runTests()
