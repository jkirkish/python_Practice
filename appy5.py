import mysql.connector


mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "root",
    database = "mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
    #print(x)

#mycursor.execute("Create Table customers (name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
    #print(x)

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

