import sqlite3

def main():
    """Connect to database and execute join query on all 5 tables"""
    
    # Connect to the SQLite database
    conn = sqlite3.connect('ecom.db')
    cursor = conn.cursor()
    
    try:
        # SQL query joining all 5 tables
        query = '''
        SELECT 
            c.name AS customer_name,
            p.product_name,
            p.category,
            oi.quantity,
            p.price,
            (p.price * oi.quantity) AS total_amount,
            pay.payment_method,
            o.order_date
        FROM 
            order_items oi
        INNER JOIN orders o ON oi.order_id = o.order_id
        INNER JOIN customers c ON o.customer_id = c.customer_id
        INNER JOIN products p ON oi.product_id = p.product_id
        INNER JOIN payments pay ON o.order_id = pay.order_id
        ORDER BY o.order_date
        '''
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch all results
        results = cursor.fetchall()
        
        # Print header
        print("=" * 120)
        print(f"{'Customer Name':<20} {'Product Name':<25} {'Category':<20} {'Qty':<5} "
              f"{'Price':<10} {'Total Amount':<12} {'Payment Method':<18} {'Order Date':<12}")
        print("=" * 120)
        
        # Print each row
        for row in results:
            customer_name, product_name, category, quantity, price, total_amount, payment_method, order_date = row
            print(f"{customer_name:<20} {product_name:<25} {category:<20} {quantity:<5} "
                  f"${price:<9.2f} ${total_amount:<11.2f} {payment_method:<18} {order_date:<12}")
        
        print("=" * 120)
        print(f"\nTotal records: {len(results)}")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()


