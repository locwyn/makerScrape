from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='digMonkeyMediaFourteen', host='127.0.0.1', database='makerTweets')

cnx.close()
