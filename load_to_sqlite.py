import sqlite3
import csv
import os

# Database file name
DB_NAME = 'ecom.db'

def create_tables(cursor):
    """Create all necessary tables in the database"""
    
    # Create customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            city TEXT NOT NULL
        )
    ''')
    
    # Create products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Create orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')
    
    # Create order_items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')
    
    # Create payments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            payment_method TEXT NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
    ''')
    
    print("Tables created successfully")

def load_customers(cursor, csv_file):
    """Load customers data from CSV"""
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO customers (customer_id, name, email, city)
                VALUES (?, ?, ?, ?)
            ''', (int(row['customer_id']), row['name'], row['email'], row['city']))
    print(f"Loaded data from {csv_file}")

def load_products(cursor, csv_file):
    """Load products data from CSV"""
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO products (product_id, product_name, category, price)
                VALUES (?, ?, ?, ?)
            ''', (int(row['product_id']), row['product_name'], row['category'], float(row['price'])))
    print(f"Loaded data from {csv_file}")

def load_orders(cursor, csv_file):
    """Load orders data from CSV"""
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO orders (order_id, customer_id, order_date)
                VALUES (?, ?, ?)
            ''', (int(row['order_id']), int(row['customer_id']), row['order_date']))
    print(f"Loaded data from {csv_file}")

def load_order_items(cursor, csv_file):
    """Load order_items data from CSV"""
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO order_items (order_item_id, order_id, product_id, quantity)
                VALUES (?, ?, ?, ?)
            ''', (int(row['order_item_id']), int(row['order_id']), 
                  int(row['product_id']), int(row['quantity'])))
    print(f"Loaded data from {csv_file}")

def load_payments(cursor, csv_file):
    """Load payments data from CSV"""
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO payments (payment_id, order_id, amount, payment_method)
                VALUES (?, ?, ?, ?)
            ''', (int(row['payment_id']), int(row['order_id']), 
                  float(row['amount']), row['payment_method']))
    print(f"Loaded data from {csv_file}")

def main():
    """Main function to create database and load all CSV files"""
    
    # Remove existing database if it exists
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"Removed existing {DB_NAME}")
    
    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        print("=" * 50)
        print("Creating SQLite database and tables...")
        print("=" * 50)
        
        # Create all tables
        create_tables(cursor)
        
        print("\n" + "=" * 50)
        print("Loading data from CSV files...")
        print("=" * 50)
        
        # Load data in the correct order (respecting foreign key constraints)
        # First: customers and products (no dependencies)
        load_customers(cursor, 'customers.csv')
        load_products(cursor, 'products.csv')
        
        # Second: orders (depends on customers)
        load_orders(cursor, 'orders.csv')
        
        # Third: order_items (depends on orders and products)
        load_order_items(cursor, 'order_items.csv')
        
        # Fourth: payments (depends on orders)
        load_payments(cursor, 'payments.csv')
        
        # Commit all changes
        conn.commit()
        
        print("\n" + "=" * 50)
        print("Data loading completed successfully!")
        print("=" * 50)
        
        # Display summary
        cursor.execute("SELECT COUNT(*) FROM customers")
        customer_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM products")
        product_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM orders")
        order_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM order_items")
        order_item_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM payments")
        payment_count = cursor.fetchone()[0]
        
        print(f"\nSummary:")
        print(f"  Customers: {customer_count} rows")
        print(f"  Products: {product_count} rows")
        print(f"  Orders: {order_count} rows")
        print(f"  Order Items: {order_item_count} rows")
        print(f"  Payments: {payment_count} rows")
        print(f"\nDatabase saved as: {DB_NAME}")
        
    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    main()


# update
