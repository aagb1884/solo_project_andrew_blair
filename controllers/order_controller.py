from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.order import Order
from models.item import Item

import repositories.order_repository as order_repo
import repositories.item_repository as item_repo

order_blueprint = Blueprint("order", __name__)

@order_blueprint.route("/orders")
def orders():
    all_orders = order_repo.select_all()
    order_items = []
    for order in all_orders:
        order_items = item_repo.get_items_for_order(order.id)
        order.items = order_items    
   
    return render_template("orders/index.html", orders = all_orders)

@order_blueprint.route('/orders/<id>')
def show_order(id):
    specific_order = order_repo.select(id)
    order_items = item_repo.get_items_for_order(specific_order.id)
    specific_order.items = order_items
    
    return render_template("orders/show.html", order = specific_order, item = order_items)


@order_blueprint.route('/orders/new')
def new_order():
    items = item_repo.select_all()
    
    return render_template("orders/new.html", items=items)

@order_blueprint.route('/orders', methods=['POST'])
def create_order():
    name = request.form["name"]
    phone_no = request.form["phone-number"]
    address = request.form["address"]
    items = request.form["items"]
    new_order = Order(name, phone_no, address, items)
    order_repo.save(new_order)
    return redirect("/orders")

@order_blueprint.route('/orders/<id>/edit')
def edit_order(id):
    items = item_repo.select_all()
    order = order_repo.select(id)
    potato = [item.id for item in order.items]
    return render_template('orders/edit.html', order = order, items=items, potato=potato)

@order_blueprint.route('/orders/<id>', methods=['POST'])
def update_order(id):
    name = request.form["name"]
    phone_no = request.form["phone-number"]
    address = request.form["address"]
    items = request.form["items"]
    order = Order(name, phone_no, address, items, id)
    order_repo.update(order)
    return redirect('/orders')

@order_blueprint.route('/orders/<id>/delete', methods=['POST'])
def delete_order(id):
    order_repo.delete(id)
    return redirect('/orders')
