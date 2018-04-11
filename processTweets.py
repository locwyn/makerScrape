import json
import mysql.connector
from credentials import *

def databaseConnect():
  return mysql.connector.connect(user=dbUser, password=dbPassword, host=dbHost, database='makerTweets')

def checkDatabaseForTweet(tweetID):
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = "SELECT tweetID FROM testing WHERE tweetID = " + str(tweetID)
  cursor.execute(tweetQuery)
  results = 0
  for x in cursor:
    results += 1
  cnx.close() 
  return results

def loadTestingData(tweetJSON):
  tweetID = tweetJSON['id']
  userID = tweetJSON['user']['id']
#  n = None
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = ("INSERT INTO testing "
                "(tweetID, userID) "
                "VALUES (%s, %s)")
  values = (tweetID, userID)
  cursor.execute(tweetQuery, values)
  cnx.commit()
  cnx.close()

def loadTweetIntoDatabase(tweetJSON):
  values = pullTweetData(tweetJSON)
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = ("INSERT INTO tweets "
                "(tweetID, tweetText, user_id, "
                "created_at, retweet_count) "
                "VALUES (%s, %s, %s, %s, %s)")
  cursor.execute(tweetQuery, values)
  cnx.commit()
  cnx.close()

def loadUserIntoDatabase(tweetJSON):
  values = pullMakerData(tweetJSON)
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = ("INSERT INTO makers "
                "(user_id, user_name, user_screen_name, "
                "location, description, followers_count, "
                "friends_count, created_at) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
  cursor.execute(tweetQuery, values)
  cnx.commit()
  cnx.close()

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
  tweetData = (tweetID, tweetText, userID, createdAt,
               retweetCount)
  return tweetData

def pullMakerData(tweetJSON):
  userID = tweetJSON['user']['id']
  userName = tweetJSON['user']['name']
  userScreenName = tweetJSON['user']['screen_name']
  location = tweetJSON['user']['location']
  description = tweetJSON['user']['description']
  followersCount = tweetJSON['user']['followers_count']
  friendsCount = tweetJSON['user']['friends_count']
  createdAt = tweetJSON['user']['created_at']
  makerData = (userID, userName, userScreenName, location,
               description, followersCount, freindsCount,
               createdAt)
  return makerData
  
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
  with open('2018_04_10_maker.json') as f:
    tweets = f.readlines()
  for y in tweets:
    tweetJSON = json.loads(y)
#    pullMakerData(tweetJSON)
    if checkDatabaseForTweet(tweetJSON['id']) == 0:
      loadTestingData(tweetJSON)
      print("BooYa!")
    else:
      print("Nada")

#print(checkDatabaseForTweet(982383049898971141))
runTests()
