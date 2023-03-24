from flask import Flask, render_template

from controllers.order_item_controller import order_items_blueprint
from controllers.order_controller import order_blueprint
from controllers.item_controller import items_blueprint


app = Flask(__name__)

app.register_blueprint(order_blueprint)
app.register_blueprint(items_blueprint)
app.register_blueprint(order_items_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
