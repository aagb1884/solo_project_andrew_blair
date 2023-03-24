from db.run_sql import run_sql

from models.order import Order
from models.item import Item

def save(order):
    sql = "INSERT INTO orders (name, phone_no, address) VALUES ( %s, %s, %s ) RETURNING id"
    values = [order.name]
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

def items(order):
    items = []

    sql = """SELECT items.*
            FROM items
            INNER JOIN orders_items
            ON orders_items.item_id = items.id
            WHERE order_id = %s"""
    values = [item.id]
    results = run_sql(sql, values)

    for row in results:
        item = Item(row['name'], row['price'], row['id'])
        items.append(item)

    return item