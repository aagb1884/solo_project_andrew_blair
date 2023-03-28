import pdb

from models.item import Item
from models.order import Order

import repositories.item_repository as item_repo
import repositories.order_repository as order_repo

order1 = Order('Megan', '0131 987 654', '33 Hardaker Street', [1])
order_repo.save(order1)

# print(order_repo.select_all()[0].id)

# items = order_repo.items(order1)

for item in items:
    print(item.__dict__)