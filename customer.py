# customer.py

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from order import Order
    from coffee import Coffee


class Customer:
    def __init__(self, name: str):
        self.name = name  # invokes setter

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self) -> List["Order"]:
        from order import Order
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self) -> List["Coffee"]:
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee: "Coffee", price: float) -> "Order":
        from order import Order
        return Order(self, coffee, price)
