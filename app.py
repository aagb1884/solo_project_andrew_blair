from flask import Flask, render_template

from controllers.orders_items.controller import orders_items_blueprint
from controllers.orders.controller import orders_blueprint
from controllers.items.controller import items_blueprint


app = Flask(__name__)

app.register_blueprint(orders_blueprint)
app.register_blueprint(items_blueprint)
app.register_blueprint(orders_items_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
