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

#def findDuplicates(cursor):
  

if __name__ == "__main__":
  allTweets = []
  selectAllTweets = "SELECT id, tweetID FROM tweets"
  cnx = databaseConnect()
  cursor = cnx.cursor()
  cursor.execute(selectAllTweets)
  for i in cursor:
    allTweets.append(i)
  cnx.close()
  print allTweets
