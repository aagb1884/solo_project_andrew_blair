from db.run_sql import run_sql

from models.order_item import Order_Item
from models.item import Item

def save(order_item):
    sql = """INSERT INTO orders_items (order_id, item_id) 
    VALUES (%s, %s) 
    RETURNING id, order_id, item_id"""
    values = [order_item.order.id, order_item.item.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    order_item.id = id
    return order_item

def add_item_by_id(item_id):
    order_items = []
    sql = """SELECT order_id, item_id FROM orders, orders_items
            WHERE orders.id = orders_items.order_id
            AND orders_items.order_id = %s"""
    results = run_sql(sql)
    
    # for result in results:
        # order_item = Order_Item(result['id'], result['order_id'], result['item_id'])
        # save(order_item)
    # item_id = results[0]['item_id']
    # item_id_list.append(item_id)
    for row in results:
        order_item = Item(row['name'], row['price'], row['id'])
        order_items.append(order_item)
    return order_items
