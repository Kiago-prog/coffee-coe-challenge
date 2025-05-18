import unittest
from coffee import Coffee
from customer import Customer
from order import Order


class TestCoffee(unittest.TestCase):

    def setUp(self):
        Order.all_orders.clear()

    def test_name_immutable_and_validation(self):
        c = Coffee("Espresso")
        self.assertEqual(c.name, "Espresso")
        with self.assertRaises(AttributeError):
            c.name = "Latte"
        with self.assertRaises(ValueError):
            Coffee("ab")  # Too short

    def test_orders_and_customers(self):
        coffee = Coffee("Latte")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")

        o1 = customer1.create_order(coffee, 3.5)
        o2 = customer2.create_order(coffee, 4.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), (3.5 + 4.0) / 2)
        self.assertCountEqual(coffee.customers(), [customer1, customer2])


if __name__ == "__main__":
    unittest.main()
