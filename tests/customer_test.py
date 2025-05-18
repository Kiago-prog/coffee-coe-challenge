import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Customer.all_customers.clear()
        Order.all_orders.clear()

    def test_customer_init_valid_name(self):
        customer = Customer("Alice")
        self.assertEqual(customer.name, "Alice")

    def test_customer_invalid_name_type(self):
        with self.assertRaises(ValueError):
            Customer(123)

    def test_customer_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("x" * 16)