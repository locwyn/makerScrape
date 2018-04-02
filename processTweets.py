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



with open('2018_03_14_maker.json') as f:
  tweets = f.readlines()

count = 0
"""
for x in tweets:
  tjson = json.loads(x)
  if tjson['user']['followers_count'] >= 2000:  
    try:
      tjson['retweeted_status']
    except KeyError:    
      count += 1
"""
for y in tweets:
#  tjson = json.loads(y)
  if 'retweeted_status' in y:
    count += 1

print(count)
checkDatabaseForTweet(12345)
