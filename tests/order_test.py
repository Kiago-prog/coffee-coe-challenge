import unittest
from customer import Customer
from coffee import Coffee
from order import Order


class TestOrder(unittest.TestCase):

    def setUp(self):
        Order.all_orders.clear()

    def test_order_valid_init(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.5)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.5)

    def test_order_invalid_price_type(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        with self.assertRaises(TypeError):
            Order(customer, coffee, "5.5")  # price not float

    def test_order_invalid_price_range(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        with self.assertRaises(ValueError):
            Order(customer, coffee, 0.5)  # less than 1.0
        with self.assertRaises(ValueError):
            Order(customer, coffee, 15.0)  # greater than 10.0


if __name__ == "__main__":
    unittest.main()
