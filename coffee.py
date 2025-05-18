class Coffee:
    all_coffees = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            Coffee.all_coffees.append(self)
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")

    @property
    def name(self):
        return self._name  # Immutable

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]