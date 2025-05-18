import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order.all_orders.clear()

    def test_order_valid_init(self):
        customer = Customer("Sam")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 4.5)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 4.5)