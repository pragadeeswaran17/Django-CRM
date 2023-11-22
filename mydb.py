# Install mySql on your computer
# pip Install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Pragadeeshwaran&2000'
)

# prepare acurser object

cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE crmdb")

print("All Done!")