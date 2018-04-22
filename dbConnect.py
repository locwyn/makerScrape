import mysql.connector
from mysql.connector import (connection)
import datetime
from credentials import *

def databaseConnect():
  return mysql.connector.connect(user=dbUser, password=dbPassword, 
           host=dbHost, database='takerTweets', charset='utf8mb4',
           collation='utf8mb4_unicode_ci')

def writeErrorLog(e):
  errorFile = datetime.datetime.now().strftime('%Y_%m_%d') + '_error.log'
    try:
      with open(errorFile, 'a') as f:
        f.write(str(e))
    except BaseException as e:
      with open(errorFile, 'a') as f:
        f.write("Unable to write error")

try:
  cnx = databaseConnect()
  cnx.close()
except mysql.connector.Error as e:
  writeErrorLog(e)


