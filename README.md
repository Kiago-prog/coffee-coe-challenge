
---

## 🧩 Features

### ✅ Models

- **Customer**
  - Initializes with a name (string, 1–15 characters).
  - Property `name` with validation and setter.
  - Methods:
    - `orders()` → returns all orders for that customer.
    - `coffees()` → returns a unique list of coffees ordered.
    - `create_order(coffee, price)` → creates a new order.

- **Coffee**
  - Initializes with a name (string, at least 3 characters).
  - Property `name` is immutable after initialization.
  - Methods:
    - `orders()` → returns all orders for that coffee.
    - `customers()` → returns a unique list of customers who ordered it.
    - `num_orders()` → total number of orders.
    - `average_price()` → average price of all orders.

- **Order**
  - Initializes with a `Customer`, a `Coffee`, and a `price` (float, between 1.0 and 10.0).
  - Properties:
    - `customer`, `coffee`, and `price` are immutable.

### 🏅 Bonus

- **Customer**
  - `most_aficionado(coffee)` (classmethod) → returns the customer who spent the most on a given coffee.

---

## 🔗 Object Relationships

- `Order.customer` → returns associated `Customer`.
- `Order.coffee` → returns associated `Coffee`.
- `Customer.orders()` → all `Order` instances linked to the customer.
- `Customer.coffees()` → unique list of coffees the customer ordered.
- `Coffee.orders()` → all `Order` instances for that coffee.
- `Coffee.customers()` → unique list of customers who’ve ordered the coffee.

---

## 🧪 Running Tests

To run the unit tests:

1. Open your terminal inside the project root.
2. Activate the environment:
   ```bash
   pipenv shell

3 Run The Test
```bash
pytest
```

##GETTING STARTED
1.Clone the repository
```bash
git clone https://github.com/<your-username>/coffee-shop-challenge.git
cd coffee-shop-challenge
```

2. Install dependencies
3. ```bash
   pipenv install
    pipenv shell

   
