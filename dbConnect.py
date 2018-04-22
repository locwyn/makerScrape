from mysql.connector import (connection)
import datetime
from credentials import *

def databaseConnect():
  return mysql.connector.connect(user=dbUser, password=dbPassword, 
           host=dbHost, database='makerTweets', charset='utf8mb4',
           collation='utf8mb4_unicode_ci')
try:
  cnx = databaseConnect()
except mysql.connector.Error as e:
  errorFile = datetime.datetime.now().strftime('%Y_%m_%d') + '_error.log'
    try:
      with open(errorFile, 'a') as f:
        f.write(str(e))
    except BaseException as e:
      print("Error on_data: %s" % str(e))
cnx.close()
