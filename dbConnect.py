from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='pycon', password='fuzzywuzzy', host='localhost', database='makerTweets')

cnx.close()
