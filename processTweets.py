import json
import mysql.connector
from credentials import *

def databaseConnect():
  return mysql.connector.connect(user=dbUser, password=dbPassword, host=dbHost, database='makerTweets')

def checkDatabaseForTweet(tweetID):
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = "SELECT tweetID FROM tweets WHERE tweetID = " + str(tweetID)
  cursor.execute(tweetQuery)
  results = 0
  for (tweetID) in cursor:
    results += 1
  cnx.close() 
  return results

def loadTestingData(tweetJSON):
  tweetID = tweetJSON['id']
  userID = tweetJSON['user']['id']
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = "INSERT INTO testing (id, tweetID, userID) VALUES (NULL, " + str(tweetID) + ", " + str(userID) + ");"
  cursor.execute(tweetQuery)
  cnx.close()

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

def pullHashtagData(tweetJSON):
  numHashtags = len(tweetJSON['entities']['hashtags'])
  hashtags = []
  if numHashtags == 0:
    print('NONE')
  else:
    for x in range(0, numHashtags):
      hashtags.append(tweetJSON['entities']['hashtags'][x]['text'])
    print(','.join(hashtags))

def runTests():
  with open('2018_04_02_maker.json') as f:
    tweets = f.readlines()
  for y in tweets:
    tweetJSON = json.loads(y)
#    pullMakerData(tweetJSON)
    loadTestingData(tweetJSON)

#print(checkDatabaseForTweet(12345))
runTests()
