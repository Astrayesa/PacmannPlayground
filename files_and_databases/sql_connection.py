import mysql.connector as connector
import os

conn = connector.connect(
    host="localhost",
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database="cars_retail"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM orders;")

for row in cursor.fetchall():
    print(row)
    break

conn.close()