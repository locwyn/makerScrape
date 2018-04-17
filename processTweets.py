import json
import mysql.connector
from credentials import *

def databaseConnect():
  return mysql.connector.connect(user=dbUser, password=dbPassword, 
           host=dbHost, database='makerTweets', charset='utf8mb4',
           collation='utf8mb4_unicode_ci')

def checkDatabaseForTweet(tweetID):
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = "SELECT tweetID FROM tweets WHERE tweetID = " + str(tweetID)
  cursor.execute(tweetQuery)
  results = 0
  for x in cursor:
    results += 1
  cnx.close() 
  return results

def checkDatabaseForMaker(userID):
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = "SELECT user_id FROM makers WHERE user_id = " + str(userID)
  cursor.execute(tweetQuery)
  results = 0
  for x in cursor:
    results += 1
  cnx.close() 
  return results

def checkDatabaseForHashtag(tag):
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = "SELECT tags FROM hashtags WHERE tags = " + tag
  cursor.execute(tweetQuery)
  results = 0
  for x in cursor:
    results += 1
  cnx.close() 
  return results

def loadTweetIntoDatabase(tweetJSON):
  if checkDatabaseForTweet(tweetJSON['id']) == 0:
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
  if checkDatabaseForMaker(tweetJSON['user']['id']) == 0:
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
   
def loadHashtagIntoDatabase(tag):
  values = (tag, 1)
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = ("INSERT INTO hashtags "
                "(tags, total) "
                "VALUES (%s, %s)")
  cursor.execute(tweetQuery, values)
  cnx.commit()
  cnx.close()
  
def updateHashtagTotals(tag):
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tweetQuery = ("UPDATE hastags SET "
                "total = total + 1 "
                "WHERE tags = " + tag)
  cursor.execute(tweetQuery, values)
  cnx.commit()
  cnx.close()

def checkForEnglish(tweetJSON):
  if tweetJSON['lang'] == "en":
    return True
  else:
    return False

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
               description, followersCount, friendsCount,
               createdAt)
  return makerData
  
def processHashtagData(tweetJSON):
  numHashtags = len(tweetJSON['entities']['hashtags'])
  hashtags = []
  if numHashtags == 0:
    print('NONE')
  else:
    for x in range(0, numHashtags):
      tag = lower(tweetJSON['entities']['hashtags'][x]['text'])
      if checkDatabaseForHashtag(tag) == 0:
        loadHashtagIntoDatabase(tag)
        print('LOAD')
      else:
        updateHashtagTotals(tag)
        print('UPDATE')

def runTests():
  with open('2018_04_10_maker.json') as f:
    tweets = f.readlines()
  for y in tweets:
    tweetJSON = json.loads(y)
#    pullMakerData(tweetJSON)
#    if checkDatabaseForTweet(tweetJSON['id']) == 0:
#      loadTestingData(tweetJSON)
    if tweetJSON.get('retweeted_status'):
      pass
    else:
      if checkForEnglish(tweetJSON):
        #loadTweetIntoDatabase(tweetJSON)
        #loadUserIntoDatabase(tweetJSON)
        processHashtagData(tweetJSON)

#print(checkDatabaseForTweet(982383049898971141))
runTests()
