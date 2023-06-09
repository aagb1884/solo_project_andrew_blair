from db.run_sql import run_sql

from models.order import Order
from models.item import Item

import repositories.order_repository as order_repo
import repositories.item_repository as item_repo

def save(order):
    items = []
    sql = """INSERT INTO orders (name, phone_no, address) 
            VALUES ( %s, %s, %s ) 
            RETURNING id"""
    values = [order.name, order.phone_no, order.address]
    results = run_sql( sql, values )
    order.id = results[0]['id']
    for row in results:
        items.append(item_repo.get_items_for_order(id))
        
        order = Order(row['name'], row['phone_no'], row['address'], items, row['id'])
        
    return order

# issue with item value?
# right function for items = ?

def select_all():
    orders = []
    sql = "SELECT * FROM orders"
    results = run_sql(sql)
    for row in results:
        
        items = item_repo.get_items_for_order(id)
        order = Order(row['name'], row['phone_no'], row['address'], items, row['id'])
        orders.append(order)
    return orders

def select(id):
    order = None
    sql = "SELECT * FROM orders WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        items = item_repo.get_items_for_order(id)
        order = Order(result['name'], result['phone_no'], result['address'], items, result['id'] )
    return order

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
            FROM items, orders_items
            WHERE items.id = orders_items.item_id
            AND orders_items.order_id = %s"""  
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        item = Item(result['name'], result['price'])
        items.append(item)
    return items

