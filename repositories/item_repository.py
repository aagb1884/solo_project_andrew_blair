from db.run_sql import run_sql

from models.item import Item
from models.order import Order

def save(item):
    sql = "INSERT INTO items ( name, price ) VALUES ( %s, %s ) RETURNING id"
    values = [item.name]
    results = run_sql( sql, values )
    item.id = results[0]['id']
    return item

def select_all():
    items = []

    sql = "SELECT * FROM items"
    results = run_sql(sql)
    for row in results:
        item = Item(row['name'], row['price'], row['id'])
        items.append(item)
    return items

def select(id):
    item = None
    sql = "SELECT * FROM items WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        item = Item(result['name'], result['price'], result['id'] )
    return item

def order(items):
    orders = []

    sql = """SELECT orders.*
            FROM orders
            INNER JOIN orders_items
            ON orders_items.order_id = orders.id
            WHERE item_id = %s"""
    values = [items.id]
    results = run_sql(sql, values)

    for row in results:
        order = Order(row['name'], row['phone_no'], 
                      row['address'], row['items'], row['id'])
        orders.append(order)

    return orders

def delete_all():
    sql = "DELETE FROM items"
    run_sql(sql)