class ShoppingCart:
    def __init__(self, items=None):
        self.items = [] if items is None else items
    def add_item(self, name, price, quantity):
        self.items.append({"name":name, "price":price, "quantity":quantity})