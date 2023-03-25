from flask import Flask, render_template
from flask import Blueprint

from models.order import Order

import repositories.order_repository as order_repo

order_blueprint = Blueprint("order", __name__)

@order_blueprint.route("/orders")
def orders():
    all_orders = order_repo.select_all()
    return render_template("orders/index.html", orders = all_orders)