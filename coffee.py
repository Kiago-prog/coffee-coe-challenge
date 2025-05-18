# coffee.py

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from order import Order
    from customer import Customer


class Coffee:
    def __init__(self, name: str):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self._name = name

    @property
    def name(self) -> str:
        return self._name  # immutable, no setter

    def orders(self) -> List["Order"]:
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self) -> List["Customer"]:
        return list({order.customer for order in self.orders()})

    def num_orders(self) -> int:
        return len(self.orders())

    def average_price(self) -> float:
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(order.price for order in orders) / len(orders)
