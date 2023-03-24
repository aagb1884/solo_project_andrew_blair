class Order:

    def __init__(self, name, phone_no, address, items, id = None):
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.items = []
        self.id = id