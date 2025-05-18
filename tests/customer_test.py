import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

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

    def test_most_aficionado(self):
        coffee = Coffee("Cappuccino")
        c1 = Customer("Ana")
        c2 = Customer("Ben")
        c1.create_order(coffee, 6.0)
        c2.create_order(coffee, 4.0)
        c1.create_order(coffee, 3.0)

        self.assertEqual(Customer.most_aficionado(coffee), c1)

if __name__ == "__main__":
    unittest.main()