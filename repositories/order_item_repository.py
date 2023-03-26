from db.run_sql import run_sql

from models.order_item import Order_Item


# def save(order-item):
#     sql = "INSERT INTO orders_items ( order, item ) VALUES ( %s, %s ) RETURNING id"
#     values = [order_item.]
#     results = run_sql( sql, values )
#     order_item.id = results[0]['id']
#     return order_item

def select_all():
    order_items = []

    sql = "SELECT * FROM orders_items"
    results = run_sql(sql)
    for row in results:
        order_item = Order_Item(row['order'], row['item'], row['id'])
        order_items.append(order_item)
    return order_items

def delete_all():
    sql = "DELETE FROM orders_items"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM orders_items WHERE id = %s"
    values = [id]
    run_sql(sql, values)