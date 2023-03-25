from flask import Flask, render_template
from flask import Blueprint

from models.item import Item

import repositories.item_repository as item_repo

items_blueprint = Blueprint("items", __name__)

@items_blueprint.route("/items")
def items():
    all_items = item_repo.select_all()
    return render_template("items/index.html", items = all_items)