#!/bin/dev/env python

import mysql.connector
from credentials import *

def databaseConnect():
  return mysql.connector.connect(user=dbUser, password=dbPassword, 
           host=dbHost, database='makerTweets', charset='utf8mb4',
           collation='utf8mb4_unicode_ci')

def checkDatabaseForItem(selectQuery):
  cnx = databaseConnect()
  cursor = cnx.cursor()
  try:
    cursor.execute(selectQuery)
    results = 0
    for x in cursor:
      results += 1
    cnx.close()
  except mysql.connector.Error as e:
    writeErrorLog(e)
  return results

def writeErrorLog(e):
#  filePath = '/home/gbk/data/makerScrape/logs/'
  errorFile = (datetime.datetime.now().strftime('%Y_%m_%d') + 
              '_reorg_error.log')
  try:
    with open(errorFile, 'a') as f:
      f.write(str(e))
  except BaseException as e:
    with open(errorFile, 'a') as f:
      f.write("Unable to write error")

def findDuplicates(allTweets):
  while len(allTweets) > 0:
    searchValue = allTweets.pop(0)
    searchForAllDuplicates(searchValue, allTweets)
  
def searchForAllDuplicates(searchValue, allTweets):
  duplicatesIndex = []
  for x in range(0, len(allTweets)):
    print(searchValue[1], " == ", allTweets[x][1])
    if searchValue[1] == allTweets[x][1]:
      duplicatesIndex.append(x)
  if len(duplicatesIndex) > 0:
    print(duplicatesIndex)

#merge sort the tweet/user ids, then check for duplicates
#may run faster since my data will keep increasing

if __name__ == "__main__":
  allTweets = []
  selectAllTweets = "SELECT id, user_id FROM makers"
  cnx = databaseConnect()
  cursor = cnx.cursor()
  cursor.execute(selectAllTweets)
  for i in cursor:
    allTweets.append(i)
  cnx.close()
  findDuplicates(allTweets)
