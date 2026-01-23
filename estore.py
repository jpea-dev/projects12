from mysql.connector import Error
import datetime
import mysql.connector

# Global database connection variables
connection = None
cursor = None

def connect_db():
    """Connect to MySQL database"""
    global connection, cursor
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='mydb'
        )
        cursor = connection.cursor()
        print("✓ Database connected successfully!")
        create_tables()
        insert_sample_data()
    except Error as e:
        print(f"Error: {e}")

def create_tables():
    """Create all required database tables"""
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE,
                phone VARCHAR(15),
                password VARCHAR(100),
                address VARCHAR(255),
                city VARCHAR(50),
                pincode VARCHAR(10),
                registration_date DATE,
                status VARCHAR(20) DEFAULT 'Active'
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                category_id INT AUTO_INCREMENT PRIMARY KEY,
                category_name VARCHAR(100) UNIQUE NOT NULL,
                description VARCHAR(255),
                status VARCHAR(20) DEFAULT 'Active'
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INT AUTO_INCREMENT PRIMARY KEY,
                category_id INT,
                product_name VARCHAR(200) NOT NULL,
                description VARCHAR(500),
                price FLOAT,
                stock_quantity INT,
                brand VARCHAR(100),
                sku VARCHAR(50) UNIQUE,
                image_url VARCHAR(255),
                status VARCHAR(20) DEFAULT 'Active',
                FOREIGN KEY(category_id) REFERENCES categories(category_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT,
                order_date DATETIME,
                total_amount FLOAT,
                discount FLOAT DEFAULT 0,
                net_amount FLOAT,
                shipping_address VARCHAR(255),
                order_status VARCHAR(20) DEFAULT 'Pending',
                payment_method VARCHAR(30),
                payment_status VARCHAR(20) DEFAULT 'Pending',
                FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS order_items (
                order_item_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT,
                product_id INT,
                quantity INT,
                price FLOAT,
                subtotal FLOAT,
                FOREIGN KEY(order_id) REFERENCES orders(order_id),
                FOREIGN KEY(product_id) REFERENCES products(product_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                review_id INT AUTO_INCREMENT PRIMARY KEY,
                product_id INT,
                customer_id INT,
                rating INT,
                review_text VARCHAR(500),
                review_date DATE,
                status VARCHAR(20) DEFAULT 'Approved',
                FOREIGN KEY(product_id) REFERENCES products(product_id),
                FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
            )
        ''')

        connection.commit()
        print("✓ Tables created successfully!")
    except Error as e:
        print(f"Table creation error: {e}")

def insert_sample_data():
    """Insert sample data into database"""
    try:
        cursor.execute("SELECT COUNT(*) FROM categories")
        if cursor.fetchone()[0] == 0:
            categories_data = [
                ("Electronics", "Electronic devices and gadgets", "Active"),
                ("Clothing", "Fashion and apparel", "Active"),
                ("Books", "Books and magazines", "Active"),
                ("Home & Kitchen", "Home appliances and kitchenware", "Active"),
                ("Sports", "Sports equipment and accessories", "Active")
            ]

            query = '''INSERT INTO categories (category_name, description, status)
                      VALUES (%s, %s, %s)'''
            cursor.executemany(query, categories_data)

            products_data = [
                (1, "Wireless Headphones", "Premium noise-cancelling headphones", 2999.00, 50, "SoundMax", "SKU001", "headphones.jpg", "Active"),
                (1, "Smartphone 5G", "Latest 5G smartphone with 128GB storage", 29999.00, 30, "TechPhone", "SKU002", "phone.jpg", "Active"),
                (2, "Cotton T-Shirt", "100% cotton comfortable t-shirt", 499.00, 100, "FashionBrand", "SKU003", "tshirt.jpg", "Active"),
                (2, "Denim Jeans", "Classic blue denim jeans", 1299.00, 75, "DenimCo", "SKU004", "jeans.jpg", "Active"),
                (3, "Python Programming Book", "Complete guide to Python programming", 599.00, 40, "TechBooks", "SKU005", "book.jpg", "Active"),
                (4, "Electric Kettle", "1.5L stainless steel electric kettle", 899.00, 60, "HomeAppliances", "SKU006", "kettle.jpg", "Active"),
                (5, "Yoga Mat", "Premium anti-slip yoga mat", 799.00, 80, "FitGear", "SKU007", "yogamat.jpg", "Active")
            ]

            query = '''INSERT INTO products (category_id, product_name, description, price, stock_quantity, brand, sku, image_url, status)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.executemany(query, products_data)

            customers_data = [
                ("John Smith", "john@email.com", "1234567890", "pass123", "123 Main St", "New York", "10001", "2024-01-15", "Active"),
                ("Mary Johnson", "mary@email.com", "9876543210", "pass456", "456 Oak Ave", "Los Angeles", "90001", "2024-02-20", "Active"),
                ("Robert Williams", "robert@email.com", "5551234567", "pass789", "789 Pine Rd", "Chicago", "60601", "2024-03-10", "Active")
            ]

            query = '''INSERT INTO customers (name, email, phone, password, address, city, pincode, registration_date, status)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.executemany(query, customers_data)

            connection.commit()
            print("✓ Sample data inserted successfully!")
    except Error as e:
        pass

# ==================== CUSTOMER FUNCTIONS ====================

def add_customer():
    """Add a new customer to the system"""
    print("\n--- Add New Customer ---")
    try:
        name = input("Enter Customer Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        password = input("Enter Password: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        pincode = input("Enter Pincode: ")
        registration_date = datetime.date.today()

        query = '''INSERT INTO customers (name, email, phone, password, address, city, pincode, registration_date)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

        cursor.execute(query, (name, email, phone, password, address, city, pincode, registration_date))
        connection.commit()
        print("✓ Customer added successfully!")
    except Error as e:
        print(f"Error: {e}")

def view_all_customers():
    """Display all customers"""
    print("\n--- All Customers ---")
    try:
        cursor.execute("SELECT customer_id, name, email, phone, city, registration_date, status FROM customers")
        customers = cursor.fetchall()

        if customers:
            print(f"{'ID':<5} {'Name':<25} {'Email':<25} {'Phone':<15} {'City':<15} {'Reg Date':<12} {'Status':<10}")
            print("-" * 120)
            for customer in customers:
                cust_id, name, email, phone, city, reg_date, status = customer
                print(f"{cust_id:<5} {name:<25} {email or 'N/A':<25} {phone or 'N/A':<15} {city or 'N/A':<15} {reg_date} {status:<10}")
        else:
            print("No customers found!")
    except Error as e:
        print(f"Error: {e}")

# ==================== CATEGORY FUNCTIONS ====================

def add_category():
    """Add a new product category"""
    print("\n--- Add New Category ---")
    try:
        category_name = input("Enter Category Name: ")
        description = input("Enter Description: ")

        query = '''INSERT INTO categories (category_name, description)
                  VALUES (%s, %s)'''

        cursor.execute(query, (category_name, description))
        connection.commit()
        print("✓ Category added successfully!")
    except Error as e:
        print(f"Error: {e}")

def view_all_categories():
    """Display all categories"""
    print("\n--- All Categories ---")
    try:
        cursor.execute("SELECT * FROM categories WHERE status = 'Active'")
        categories = cursor.fetchall()

        if categories:
            print(f"{'ID':<5} {'Category Name':<30} {'Description':<50} {'Status':<10}")
            print("-" * 100)
            for category in categories:
                cat_id, name, desc, status = category
                print(f"{cat_id:<5} {name:<30} {desc or 'N/A':<50} {status:<10}")
        else:
            print("No categories found!")
    except Error as e:
        print(f"Error: {e}")

# ==================== PRODUCT FUNCTIONS ====================

def add_product():
    """Add a new product"""
    print("\n--- Add New Product ---")
    try:
        category_id = int(input("Enter Category ID: "))
        product_name = input("Enter Product Name: ")
        description = input("Enter Description: ")
        price = float(input("Enter Price: "))
        stock_quantity = int(input("Enter Stock Quantity: "))
        brand = input("Enter Brand: ")
        sku = input("Enter SKU: ")
        image_url = input("Enter Image URL: ")

        query = '''INSERT INTO products (category_id, product_name, description, price, stock_quantity, brand, sku, image_url)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

        cursor.execute(query, (category_id, product_name, description, price, stock_quantity, brand, sku, image_url))
        connection.commit()
        print("✓ Product added successfully!")
    except Error as e:
        print(f"Error: {e}")

def view_all_products():
    """Display all products"""
    print("\n--- All Products ---")
    try:
        cursor.execute('''SELECT p.product_id, p.product_name, c.category_name, p.brand, p.price, p.stock_quantity, p.status
                          FROM products p
                          JOIN categories c ON p.category_id = c.category_id
                          WHERE p.status = 'Active' ''')
        products = cursor.fetchall()

        if products:
            print(f"{'ID':<5} {'Product Name':<30} {'Category':<20} {'Brand':<15} {'Price':<12} {'Stock':<8} {'Status':<10}")
            print("-" * 110)
            for product in products:
                prod_id, name, category, brand, price, stock, status = product
                print(f"{prod_id:<5} {name:<30} {category:<20} {brand:<15} Rs.{price:<10.2f} {stock:<8} {status:<10}")
        else:
            print("No products found!")
    except Error as e:
        print(f"Error: {e}")

def search_product():
    """Search for products by name"""
    print("\n--- Search Product ---")
    try:
        search_term = input("Enter Product Name to Search: ")
        cursor.execute('''SELECT p.product_id, p.product_name, c.category_name, p.brand, p.price, p.stock_quantity
                          FROM products p
                          JOIN categories c ON p.category_id = c.category_id
                          WHERE p.product_name LIKE %s AND p.status = 'Active' ''', (f"%{search_term}%",))
        products = cursor.fetchall()

        if products:
            print(f"{'ID':<5} {'Product Name':<30} {'Category':<20} {'Brand':<15} {'Price':<12} {'Stock':<8}")
            print("-" * 100)
            for product in products:
                prod_id, name, category, brand, price, stock = product
                print(f"{prod_id:<5} {name:<30} {category:<20} {brand:<15} Rs.{price:<10.2f} {stock:<8}")
        else:
            print("No products found!")
    except Error as e:
        print(f"Error: {e}")

# ==================== ORDER FUNCTIONS ====================

def create_order():
    """Create a new order"""
    print("\n--- Create New Order ---")
    try:
        customer_id = int(input("Enter Customer ID: "))

        cursor.execute("SELECT address, city FROM customers WHERE customer_id = %s", (customer_id,))
        customer_result = cursor.fetchone()

        if customer_result:
            shipping_address = f"{customer_result[0]}, {customer_result[1]}"

            order_date = datetime.datetime.now()
            payment_method = input("Enter Payment Method (Cash/Card/UPI/Net Banking): ")

            query = '''INSERT INTO orders (customer_id, order_date, total_amount, net_amount, shipping_address, payment_method, payment_status)
                      VALUES (%s, %s, %s, %s, %s, %s, %s)'''

            cursor.execute(query, (customer_id, order_date, 0, 0, shipping_address, payment_method, "Pending"))
            order_id = cursor.lastrowid

            total_amount = 0

            while True:
                add_item = input("\nAdd item to order? (yes/no): ")
                if add_item.lower() != 'yes':
                    break

                product_id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity: "))

                cursor.execute("SELECT price, stock_quantity FROM products WHERE product_id = %s", (product_id,))
                product_result = cursor.fetchone()

                if product_result:
                    price, stock = product_result

                    if stock >= quantity:
                        subtotal = price * quantity
                        total_amount += subtotal

                        query = '''INSERT INTO order_items (order_id, product_id, quantity, price, subtotal)
                                  VALUES (%s, %s, %s, %s, %s)'''

                        cursor.execute(query, (order_id, product_id, quantity, price, subtotal))

                        cursor.execute("UPDATE products SET stock_quantity = stock_quantity - %s WHERE product_id = %s", (quantity, product_id))

                        print(f"Item added! Subtotal: Rs. {subtotal:.2f}")
                    else:
                        print(f"Insufficient stock! Only {stock} available.")
                else:
                    print("Product not found!")

            discount = float(input("\nEnter Discount Amount (if any): ") or 0)
            net_amount = total_amount - discount

            cursor.execute("UPDATE orders SET total_amount = %s, discount = %s, net_amount = %s, order_status = 'Confirmed', payment_status = 'Completed' WHERE order_id = %s",
                           (total_amount, discount, net_amount, order_id))

            connection.commit()

            print(f"\n✓ Order created successfully!")
            print(f"Order ID: {order_id}")
            print(f"Total Amount: Rs. {total_amount:.2f}")
            print(f"Discount: Rs. {discount:.2f}")
            print(f"Net Amount: Rs. {net_amount:.2f}")
        else:
            print("Customer not found!")
    except Error as e:
        print(f"Error: {e}")

def view_orders():
    """Display all orders"""
    print("\n--- All Orders ---")
    try:
        cursor.execute('''SELECT o.order_id, c.name, o.order_date, o.total_amount, o.discount, o.net_amount, o.order_status, o.payment_status
                          FROM orders o
                          JOIN customers c ON o.customer_id = c.customer_id
                          ORDER BY o.order_date DESC''')
        orders = cursor.fetchall()

        if orders:
            print(f"{'Order ID':<10} {'Customer':<25} {'Date':<20} {'Total':<12} {'Discount':<12} {'Net':<12} {'Status':<12} {'Payment':<12}")
            print("-" * 130)
            for order in orders:
                order_id, customer, date, total, discount, net, status, payment = order
                print(f"{order_id:<10} {customer:<25} {str(date):<20} Rs.{total:<10.2f} Rs.{discount:<10.2f} Rs.{net:<10.2f} {status:<12} {payment:<12}")
        else:
            print("No orders found!")
    except Error as e:
        print(f"Error: {e}")

def view_order_details():
    """Display details of a specific order"""
    print("\n--- Order Details ---")
    try:
        order_id = int(input("Enter Order ID: "))

        cursor.execute('''SELECT o.order_id, c.name, o.order_date, o.shipping_address, o.total_amount, o.discount, o.net_amount, o.payment_method, o.order_status
                          FROM orders o
                          JOIN customers c ON o.customer_id = c.customer_id
                          WHERE o.order_id = %s''', (order_id,))
        order = cursor.fetchone()

        if order:
            order_id, customer, date, address, total, discount, net, payment, status = order

            print("\n" + "="*80)
            print("                        ORDER DETAILS")
            print("="*80)
            print(f"Order ID: {order_id}")
            print(f"Customer: {customer}")
            print(f"Order Date: {date}")
            print(f"Shipping Address: {address}")
            print(f"Payment Method: {payment}")
            print(f"Order Status: {status}")
            print("-"*80)

            cursor.execute('''SELECT p.product_name, oi.quantity, oi.price, oi.subtotal
                              FROM order_items oi
                              JOIN products p ON oi.product_id = p.product_id
                              WHERE oi.order_id = %s''', (order_id,))
            items = cursor.fetchall()

            print(f"{'Product':<40} {'Quantity':<10} {'Price':<12} {'Subtotal':<12}")
            print("-"*80)
            for item in items:
                product, quantity, price, subtotal = item
                print(f"{product:<40} {quantity:<10} Rs.{price:<10.2f} Rs.{subtotal:<10.2f}")

            print("-"*80)
            print(f"Total Amount: Rs. {total:.2f}")
            print(f"Discount: Rs. {discount:.2f}")
            print(f"Net Amount: Rs. {net:.2f}")
            print("="*80)
        else:
            print("Order not found!")
    except Error as e:
        print(f"Error: {e}")

# ==================== REVIEW FUNCTIONS ====================

def add_review():
    """Add a product review"""
    print("\n--- Add Product Review ---")
    try:
        product_id = int(input("Enter Product ID: "))
        customer_id = int(input("Enter Customer ID: "))
        rating = int(input("Enter Rating (1-5): "))
        review_text = input("Enter Review: ")
        review_date = datetime.date.today()

        query = '''INSERT INTO reviews (product_id, customer_id, rating, review_text, review_date)
                  VALUES (%s, %s, %s, %s, %s)'''

        cursor.execute(query, (product_id, customer_id, rating, review_text, review_date))
        connection.commit()
        print("✓ Review added successfully!")
    except Error as e:
        print(f"Error: {e}")

def view_product_reviews():
    """Display reviews for a product"""
    print("\n--- Product Reviews ---")
    try:
        product_id = int(input("Enter Product ID: "))

        cursor.execute('''SELECT c.name, r.rating, r.review_text, r.review_date
                          FROM reviews r
                          JOIN customers c ON r.customer_id = c.customer_id
                          WHERE r.product_id = %s AND r.status = 'Approved'
                          ORDER BY r.review_date DESC''', (product_id,))
        reviews = cursor.fetchall()

        if reviews:
            print(f"{'Customer':<25} {'Rating':<8} {'Review':<50} {'Date':<12}")
            print("-" * 100)
            for review in reviews:
                customer, rating, text, date = review
                print(f"{customer:<25} {rating}/5 {text:<50} {date}")
        else:
            print("No reviews found!")
    except Error as e:
        print(f"Error: {e}")

# ==================== REPORT FUNCTIONS ====================

def generate_report():
    """Generate system report"""
    print("\n--- E-commerce Store Report ---")
    try:
        print("\n1. Total Products")
        cursor.execute("SELECT COUNT(*) FROM products WHERE status = 'Active'")
        products = cursor.fetchone()[0]
        print(f"Active Products: {products}")

        print("\n2. Total Customers")
        cursor.execute("SELECT COUNT(*) FROM customers WHERE status = 'Active'")
        customers = cursor.fetchone()[0]
        print(f"Active Customers: {customers}")

        print("\n3. Total Orders")
        cursor.execute("SELECT COUNT(*) FROM orders WHERE order_status = 'Confirmed'")
        orders = cursor.fetchone()[0]
        print(f"Total Orders: {orders}")

        print("\n4. Total Revenue")
        cursor.execute("SELECT SUM(net_amount) FROM orders WHERE payment_status = 'Completed'")
        revenue_result = cursor.fetchone()
        revenue = revenue_result[0] if revenue_result[0] else 0
        print(f"Total Revenue: Rs. {revenue:.2f}")

        print("\n5. Low Stock Products")
        cursor.execute("SELECT product_name, stock_quantity FROM products WHERE stock_quantity < 20 AND status = 'Active'")
        low_stock = cursor.fetchall()
        if low_stock:
            print("Products with low stock:")
            for product, stock in low_stock:
                print(f"  - {product}: {stock} units")
        else:
            print("No low stock products")
    except Error as e:
        print(f"Error: {e}")

# ==================== MENU FUNCTIONS ====================

def main_menu():
    """Display main menu and handle user choices"""
    while True:
        print("\n" + "="*60)
        print("        E-COMMERCE STORE MANAGEMENT SYSTEM")
        print("="*60)
        print("\n--- CUSTOMER MANAGEMENT ---")
        print("1. Add Customer")
        print("2. View All Customers")

        print("\n--- CATEGORY MANAGEMENT ---")
        print("3. Add Category")
        print("4. View All Categories")

        print("\n--- PRODUCT MANAGEMENT ---")
        print("5. Add Product")
        print("6. View All Products")
        print("7. Search Product")

        print("\n--- ORDER MANAGEMENT ---")
        print("8. Create Order")
        print("9. View All Orders")
        print("10. View Order Details")

        print("\n--- REVIEW MANAGEMENT ---")
        print("11. Add Product Review")
        print("12. View Product Reviews")

        print("\n--- REPORTS ---")
        print("13. Generate Store Report")

        print("\n14. Exit")
        print("="*60)

        choice = input("Enter your choice (1-14): ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_all_customers()
        elif choice == "3":
            add_category()
        elif choice == "4":
            view_all_categories()
        elif choice == "5":
            add_product()
        elif choice == "6":
            view_all_products()
        elif choice == "7":
            search_product()
        elif choice == "8":
            create_order()
        elif choice == "9":
            view_orders()
        elif choice == "10":
            view_order_details()
        elif choice == "11":
            add_review()
        elif choice == "12":
            view_product_reviews()
        elif choice == "13":
            generate_report()
        elif choice == "14":
            print("\nThank you for using E-commerce Store Management System!")
            cursor.close()
            connection.close()
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    connect_db()
    main_menu()
