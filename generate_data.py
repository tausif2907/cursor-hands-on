import csv
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)

# Sample data for generation
first_names = ["John", "Jane", "Michael", "Sarah", "David", "Emily", "Robert", "Jessica", 
               "William", "Amanda", "James", "Lisa", "Christopher", "Michelle", "Daniel", 
               "Ashley", "Matthew", "Stephanie", "Anthony", "Nicole", "Mark", "Elizabeth"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
              "Rodriguez", "Martinez", "Hernandez", "Lopez", "Wilson", "Anderson", "Thomas",
              "Taylor", "Moore", "Jackson", "Martin", "Lee", "Thompson", "White"]

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", 
          "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville",
          "San Francisco", "Columbus", "Fort Worth", "Charlotte", "Seattle", "Denver"]

product_names = [
    ("Wireless Mouse", "Electronics", 29.99),
    ("USB-C Cable", "Electronics", 12.99),
    ("Laptop Stand", "Electronics", 39.99),
    ("Mechanical Keyboard", "Electronics", 89.99),
    ("Webcam HD", "Electronics", 59.99),
    ("Cotton T-Shirt", "Clothing", 19.99),
    ("Denim Jeans", "Clothing", 49.99),
    ("Running Shoes", "Clothing", 79.99),
    ("Winter Jacket", "Clothing", 99.99),
    ("Baseball Cap", "Clothing", 24.99),
    ("Coffee Maker", "Home & Kitchen", 45.99),
    ("Blender", "Home & Kitchen", 69.99),
    ("Dinner Set", "Home & Kitchen", 89.99),
    ("Bed Sheets", "Home & Kitchen", 34.99),
    ("Desk Lamp", "Home & Kitchen", 29.99),
    ("Novel - Mystery", "Books", 14.99),
    ("Cookbook", "Books", 24.99),
    ("Notebook Set", "Books", 12.99),
    ("Yoga Mat", "Sports", 29.99),
    ("Dumbbells Set", "Sports", 79.99),
    ("Basketball", "Sports", 24.99),
    ("Tennis Racket", "Sports", 89.99)
]

payment_methods = ["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Cash on Delivery"]

# Generate customers.csv
def generate_customers():
    customers = []
    for i in range(1, 21):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = f"{first_name} {last_name}"
        email = f"{first_name.lower()}.{last_name.lower()}@email.com"
        city = random.choice(cities)
        customers.append([i, name, email, city])
    
    with open('customers.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['customer_id', 'name', 'email', 'city'])
        writer.writerows(customers)
    print("Generated customers.csv with 20 rows")

# Generate products.csv
def generate_products():
    products = []
    for i in range(1, 21):
        product_name, category, price = random.choice(product_names)
        products.append([i, product_name, category, price])
    
    with open('products.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['product_id', 'product_name', 'category', 'price'])
        writer.writerows(products)
    print("Generated products.csv with 20 rows")

# Generate orders.csv
def generate_orders():
    orders = []
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    for i in range(1, 21):
        customer_id = random.randint(1, 20)
        # Generate random date between start and end date
        time_between = end_date - start_date
        days_between = time_between.days
        random_days = random.randrange(days_between)
        order_date = start_date + timedelta(days=random_days)
        orders.append([i, customer_id, order_date.strftime('%Y-%m-%d')])
    
    with open('orders.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['order_id', 'customer_id', 'order_date'])
        writer.writerows(orders)
    print("Generated orders.csv with 20 rows")

# Generate order_items.csv
def generate_order_items():
    order_items = []
    order_item_id = 1
    
    # Generate 1-3 items per order
    for order_id in range(1, 21):
        num_items = random.randint(1, 3)
        for _ in range(num_items):
            product_id = random.randint(1, 20)
            quantity = random.randint(1, 5)
            order_items.append([order_item_id, order_id, product_id, quantity])
            order_item_id += 1
    
    with open('order_items.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['order_item_id', 'order_id', 'product_id', 'quantity'])
        writer.writerows(order_items)
    print(f"Generated order_items.csv with {len(order_items)} rows")

# Generate payments.csv
def generate_payments():
    payments = []
    
    # Read orders to get order_ids
    order_ids = list(range(1, 21))
    
    for i in range(1, 21):
        order_id = random.choice(order_ids)
        # Amount will be calculated based on order items, but for simplicity, use random
        amount = round(random.uniform(20.00, 500.00), 2)
        payment_method = random.choice(payment_methods)
        payments.append([i, order_id, amount, payment_method])
    
    with open('payments.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['payment_id', 'order_id', 'amount', 'payment_method'])
        writer.writerows(payments)
    print("Generated payments.csv with 20 rows")

# Main function to generate all files
def main():
    print("Generating synthetic e-commerce CSV files...")
    print("-" * 50)
    generate_customers()
    generate_products()
    generate_orders()
    generate_order_items()
    generate_payments()
    print("-" * 50)
    print("All CSV files generated successfully!")

if __name__ == "__main__":
    main()


# update
