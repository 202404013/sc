import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 's4brinacarp',
	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE sabrina")

print("All Done!")