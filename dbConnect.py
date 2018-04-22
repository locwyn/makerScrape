import mysql.connector
from mysql.connector import (connection)
from credentials import *

def databaseConnect():
  return mysql.connector.connect(user=dbUser, password=dbPassword, 
           host=dbHost, database='takerTweets', charset='utf8mb4',
           collation='utf8mb4_unicode_ci')
try:
  cnx = databaseConnect()
  cnx.close()
except mysql.connector.Error as e:
  print("Error Code: " + str(e.errno))
  print("SQLSTATE Value: " + e.sqlstate)
  print("Error Message: " + e.msg)
  print("Error: " + str(e))
