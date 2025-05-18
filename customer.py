class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)