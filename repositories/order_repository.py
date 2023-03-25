from db.run_sql import run_sql

from models.order import Order
from models.item import Item

def save(order):
    sql = "INSERT INTO orders (name, phone_no, address) VALUES ( %s, %s, %s ) RETURNING id"
    values = [order.name, order.phone_no, order.address]
    results = run_sql( sql, values )
    order.id = results[0]['id']
    return order

def select_all():
    orders = []

    sql = "SELECT * FROM orders"
    results = run_sql(sql)
    for row in results:
        order = Order(row['name'], row['phone_no'], row['address'], row['id'])
        orders.append(order)
    return orders

def select(id):
    order = None
    sql = "SELECT * FROM orders WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        order = Order(result['name'], result['phone_no'], result['address'], result['id'] )
    return order

# def items(order):
#     items = []

#     sql = """SELECT items.*
#             FROM items 
#             INNER JOIN orders_items
#             ON orders_items.item_id = items.id
#             WHERE order_id = %s"""
#     values = [item.id]
#     results = run_sql(sql, values)

#     for row in results:
#         item = Item(row['name'], row['price'], row['id'])
#         items.append(item)

#     return item

def delete_all():
    sql = "DELETE FROM orders"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM orders WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(order):
    sql = "UPDATE orders SET (name, phone_no, address) = (%s, %s, %s) WHERE id = %s"
    values = [order.name, order.phone_no, order.address, order.id]
    run_sql(sql, values)

def add_item_to_order(id):
    items = []
    sql = """SELECT items.*
            FROM items 
            INNER JOIN orders_items
            ON orders_items.item_id = items.id
            WHERE order_id = %s"""
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        item = Item(result['name'], result['price'])
        items.append(item)
    return items