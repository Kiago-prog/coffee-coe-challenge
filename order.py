# order.py

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer import Customer
    from coffee import Coffee


class Order:
    all_orders = []

    def __init__(self, customer: "Customer", coffee: "Coffee", price: float):
        if not isinstance(price, float):
            raise TypeError("Price must be a float.")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)

    @property
    def customer(self) -> "Customer":
        return self._customer

    @property
    def coffee(self) -> "Coffee":
        return self._coffee

    @property
    def price(self) -> float:
        return self._price
