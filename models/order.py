class Order:

    def __init__(self, name, phone_no, address,id = None, items = []):
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.items = items
        self.id = id