import sqlite3

# data url https://drive.google.com/file/d/1giqBhW11LO4Th0wXxsl_pVGABtknmg1_/view
# create connection to data/olist.db
conn = sqlite3.connect('data/olist.db')

# create cursor
cursor = conn.cursor()

# get data from payments, orders, order_items, and products tables
str_query = """
SELECT 
    orders.order_id,
    orders.customer_id,
    orders.order_status,
    payments.payment_sequential,
    payments.payment_type,
    payments.payment_installments,
    items.price,
    products.product_id
    
FROM olist_order_payments_dataset payments
INNER JOIN olist_order_dataset orders USING (order_id)
INNER JOIN olist_order_items_dataset items USING (order_id)
INNER JOIN olist_products_dataset products USING (product_id);
"""

# execute query
cursor.execute(str_query)
query_result = cursor.fetchall()

unique_order_id = set()
unique_customer_id = set()
unique_product_id = set()

result = []
# print query results
for row in query_result:
    # print(int(row[0], base=16))
    unique_order_id.add(row[0])
    unique_customer_id.add(row[1])
    unique_product_id.add(row[7])
    result.append(list(row))
    # result.append(f"[{', '.join(str(int(x, base=16)) if type(x) == str and len(x) > 15 else str(x) for x in row)}]")

# print(result[:10])

order_id_dict = {}
for index, value in enumerate(unique_order_id):
    order_id_dict[value] = index

print(f"Number of unique order_id: {len(order_id_dict)}")

customer_id_dict = {}
for index, value in enumerate(unique_customer_id):
    customer_id_dict[value] = index

print(f"Number of unique customer_id: {len(customer_id_dict)}")

prodcut_id_dict = {}
for index, value in enumerate(unique_product_id):
    prodcut_id_dict[value] = index

print(f"Number of unique product_id: {len(prodcut_id_dict)}")

for i in result:
    i[0] = order_id_dict[i[0]]
    i[1] = customer_id_dict[i[1]]
    i[7] = prodcut_id_dict[i[7]]

# print(result[:10])