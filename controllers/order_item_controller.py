from flask import Flask, render_template
from flask import Blueprint

from models.order_item import Order_Item

import repositories.order_item_repository as order_item_repo

order_items_blueprint = Blueprint("order_items",__name__)