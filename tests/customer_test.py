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

    def test_customer_orders_and_coffees(self):
        customer = Customer("Bob")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")
        customer.create_order(coffee1, 5.0)
        customer.create_order(coffee2, 7.0)
        customer.create_order(coffee1, 4.5)

        orders = customer.orders()
        coffees = customer.coffees()

        self.assertEqual(len(orders), 3)
        self.assertEqual(set(coffees), {coffee1, coffee2})