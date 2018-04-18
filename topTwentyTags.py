import mysql.connector
from credentials import *

def databaseConnect():
  return mysql.connector.connect(user=dbUser, password=dbPassword,
           host=dbHost, database='makerTweets', charset='utf8mb4',
           collation='utf8mb4_unicode_ci')

def sortTopTwentyTags():
  results = []
  cnx = databaseConnect()
  cursor = cnx.cursor()
  tagQuery = ("SELECT tags, total FROM hashtags "
              "ORDER BY total DESC")
  cursor.execute(tagQuery)
  for x in cursor:
    results.append(x)
  cnx.close()
  return results

def printTopTwentyTags(results):
  print('Top Twenty Hashtags')
  for i in range(0, 20):
    print(str(i + 1) + '. ' + results[i][0] + ' - ' + 
         str(results[i][1]))

printTopTwentyTags(sortTopTwentyTags())
