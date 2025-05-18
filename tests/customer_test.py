import unittest
from customer import Customer
from coffee import Coffee
from order import Order


class TestCustomer(unittest.TestCase):

    def setUp(self):
        # Clear all orders before each test
        Order.all_orders.clear()

    def test_name_setter_getter_valid(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")
        c.name = "Bob"
        self.assertEqual(c.name, "Bob")

    def test_name_setter_invalid_type(self):
        with self.assertRaises(ValueError):
            Customer(123)  # Not a string

    def test_name_setter_invalid_length(self):
        with self.assertRaises(ValueError):
            Customer("")  # Too short
        with self.assertRaises(ValueError):
            Customer("a" * 16)  # Too long

    def test_orders_and_coffees(self):
        c = Customer("Alice")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Mocha")

        order1 = c.create_order(coffee1, 3.5)
        order2 = c.create_order(coffee2, 4.5)
        order3 = c.create_order(coffee1, 5.0)

        self.assertEqual(len(c.orders()), 3)
        self.assertCountEqual(c.coffees(), [coffee1, coffee2])


if __name__ == "__main__":
    unittest.main()
