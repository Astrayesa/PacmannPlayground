import os
import mysql.connector as connector

# create connection to mysql
conn = connector.connect(
    host="localhost", 
    user=os.environ["MYSQL_USER"], 
    password=os.environ["MYSQL_PASSWORD"],
    database="cars_retail")

# create cursor
cur = conn.cursor()

query = """
SELECT
    productLine,
    productName,
    productScale,
    quantityOrdered AS qty,
    priceEach AS price
FROM
    orders
INNER JOIN orderdetails USING(orderNumber)
INNER JOIN products USING(productCode)
INNER JOIN productlines USING(ProductLine)
"""

# execute query
cur.execute(query)
# fetch result
query_result = cur.fetchall()
result = []
# print result
for i in query_result:
    # print(i)
    result.append([str(x) for x in i])

print(result)

# close cursor
cur.close()
# close connection
conn.close()
# create cursor
