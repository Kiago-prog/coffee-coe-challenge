class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("price must be a float between 1.0 and 10.0.")