import mysql.connector
from datetime import datetime

# Database connection settings
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'mydb'
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price DECIMAL(10,2) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            user_id INT,
            quantity INT,
            sale_date DATETIME,
            FOREIGN KEY (product_id) REFERENCES product(id),
            FOREIGN KEY (user_id) REFERENCES user(id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchase (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            user_id INT,
            quantity INT,
            purchase_date DATETIME,
            FOREIGN KEY (product_id) REFERENCES product(id),
            FOREIGN KEY (user_id) REFERENCES user(id)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# CRUD for user
def create_user(username, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user (username, email) VALUES (%s, %s)", (username, email))
    conn.commit()
    cursor.close()
    conn.close()

def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def update_user(user_id, username, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET username=%s, email=%s WHERE id=%s", (username, email, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user WHERE id=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD for product
def create_product(name, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (name, price) VALUES (%s, %s)", (name, price))
    conn.commit()
    cursor.close()
    conn.close()

def get_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products

def update_product(product_id, name, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE product SET name=%s, price=%s WHERE id=%s", (name, price, product_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE id=%s", (product_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD for sales
def create_sale(product_id, user_id, quantity, sale_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sales (product_id, user_id, quantity, sale_date) VALUES (%s, %s, %s, %s)",
        (product_id, user_id, quantity, sale_date)
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_sales():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sales")
    sales = cursor.fetchall()
    cursor.close()
    conn.close()
    return sales

def update_sale(sale_id, product_id, user_id, quantity, sale_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE sales SET product_id=%s, user_id=%s, quantity=%s, sale_date=%s WHERE id=%s",
        (product_id, user_id, quantity, sale_date, sale_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_sale(sale_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sales WHERE id=%s", (sale_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD for purchase
def create_purchase(product_id, user_id, quantity, purchase_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO purchase (product_id, user_id, quantity, purchase_date) VALUES (%s, %s, %s, %s)",
        (product_id, user_id, quantity, purchase_date)
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_purchases():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM purchase")
    purchases = cursor.fetchall()
    cursor.close()
    conn.close()
    return purchases

def update_purchase(purchase_id, product_id, user_id, quantity, purchase_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE purchase SET product_id=%s, user_id=%s, quantity=%s, purchase_date=%s WHERE id=%s",
        (product_id, user_id, quantity, purchase_date, purchase_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_purchase(purchase_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM purchase WHERE id=%s", (purchase_id,))
    conn.commit()
    cursor.close()
    conn.close()


# Helper functions (module level)
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def input_date(prompt):
    s = input(prompt + " (YYYY-MM-DD HH:MM:SS or YYYY-MM-DD, leave blank for now): ").strip()
    if not s:
        return datetime.now()
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    print("Invalid date format, using current time.")
    return datetime.now()


def pause():
    input("Press Enter to continue...")


def list_rows(rows):
    if not rows:
        print("No records.")
    else:
        for r in rows:
            print(r)


# CLI wrappers for Users
def insert_user_cli():
    uname = input("Username: ").strip()
    email = input("Email: ").strip()
    try:
        create_user(uname, email)
        print("User created.")
    except Exception as e:
        print("Error:", e)


def list_users_cli():
    list_rows(get_users())


def update_user_cli():
    uid = input_int("User ID to update: ")
    uname = input("New username: ").strip()
    email = input("New email: ").strip()
    try:
        update_user(uid, uname, email)
        print("User updated.")
    except Exception as e:
        print("Error:", e)


def delete_user_cli():
    uid = input_int("User ID to delete: ")
    try:
        delete_user(uid)
        print("User deleted.")
    except Exception as e:
        print("Error:", e)


# CLI wrappers for Products
def insert_product_cli():
    name = input("Name: ").strip()
    price = input_float("Price: ")
    try:
        create_product(name, price)
        print("Product created.")
    except Exception as e:
        print("Error:", e)


def list_products_cli():
    list_rows(get_products())


def update_product_cli():
    pid = input_int("Product ID to update: ")
    name = input("New name: ").strip()
    price = input_float("New price: ")
    try:
        update_product(pid, name, price)
        print("Product updated.")
    except Exception as e:
        print("Error:", e)


def delete_product_cli():
    pid = input_int("Product ID to delete: ")
    try:
        delete_product(pid)
        print("Product deleted.")
    except Exception as e:
        print("Error:", e)


# CLI wrappers for Sales
def insert_sale_cli():
    pid = input_int("Product ID: ")
    uid = input_int("User ID: ")
    qty = input_int("Quantity: ")
    sdate = input_date("Sale date")
    try:

        create_sale(pid, uid, qty, sdate)
        print("Sale recorded.")
    except Exception as e:
        print("Error:", e)


def list_sales_cli():
    list_rows(get_sales())


def update_sale_cli():
    sid = input_int("Sale ID to update: ")
    pid = input_int("Product ID: ")
    uid = input_int("User ID: ")
    qty = input_int("Quantity: ")
    sdate = input_date("Sale date")
    try:
        update_sale(sid, pid, uid, qty, sdate)
        print("Sale updated.")
    except Exception as e:
        print("Error:", e)


def delete_sale_cli():
    sid = input_int("Sale ID to delete: ")
    try:
        delete_sale(sid)
        print("Sale deleted.")
    except Exception as e:
        print("Error:", e)


# CLI wrappers for Purchases
def insert_purchase_cli():
    pid = input_int("Product ID: ")
    uid = input_int("User ID: ")
    qty = input_int("Quantity: ")
    pdate = input_date("Purchase date")
    try:
        create_purchase(pid, uid, qty, pdate)
        print("Purchase recorded.")
    except Exception as e:
        print("Error:", e)


def list_purchases_cli():
    list_rows(get_purchases())


def update_purchase_cli():
    pidc = input_int("Purchase ID to update: ")
    pid = input_int("Product ID: ")
    uid = input_int("User ID: ")
    qty = input_int("Quantity: ")
    pdate = input_date("Purchase date")
    try:
        update_purchase(pidc, pid, uid, qty, pdate)
        print("Purchase updated.")
    except Exception as e:
        print("Error:", e)


def delete_purchase_cli():
    pidc = input_int("Purchase ID to delete: ")
    try:
        delete_purchase(pidc)
        print("Purchase deleted.")
    except Exception as e:
        print("Error:", e)


# Main application loop
if __name__ == "__main__":
    create_tables()

    while True:
        print("\n=== Main Menu ===")
        print("1. Users")
        print("2. Products")
        print("3. Sales")
        print("4. Purchases")
        print("5. Create tables")
        print("0. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            while True:
                print("\n-- Users Menu --")
                print("1. List users")
                print("2. Create user")
                print("3. Update user")
                print("4. Delete user")
                print("0. Back")
                c = input("Choose: ").strip()
                if c == "1":
                    list_users_cli()
                    pause()
                elif c == "2":
                    insert_user_cli()
                    pause()
                elif c == "3":
                    update_user_cli()
                    pause()
                elif c == "4":
                    delete_user_cli()
                    pause()
                elif c == "0":
                    break
                else:
                    print("Invalid choice.")

        elif choice == "2":
            while True:
                print("\n-- Products Menu --")
                print("1. List products")
                print("2. Create product")
                print("3. Update product")
                print("4. Delete product")
                print("0. Back")
                c = input("Choose: ").strip()
                if c == "1":
                    list_products_cli()
                    pause()
                elif c == "2":
                    insert_product_cli()
                    pause()
                elif c == "3":
                    update_product_cli()
                    pause()
                elif c == "4":
                    delete_product_cli()
                    pause()
                elif c == "0":
                    break
                else:
                    print("Invalid choice.")

        elif choice == "3":
            while True:
                print("\n-- Sales Menu --")
                print("1. List sales")
                print("2. Create sale")
                print("3. Update sale")
                print("4. Delete sale")
                print("0. Back")
                c = input("Choose: ").strip()
                if c == "1":
                    list_sales_cli()
                    pause()
                elif c == "2":
                    insert_sale_cli()
                    pause()
                elif c == "3":
                    update_sale_cli()
                    pause()
                elif c == "4":
                    delete_sale_cli()
                    pause()
                elif c == "0":
                    break
                else:
                    print("Invalid choice.")

        elif choice == "4":
            while True:
                print("\n-- Purchases Menu --")
                print("1. List purchases")
                print("2. Create purchase")
                print("3. Update purchase")
                print("4. Delete purchase")
                print("0. Back")
                c = input("Choose: ").strip()
                if c == "1":
                    list_purchases_cli()
                    pause()
                elif c == "2":
                    insert_purchase_cli()
                    pause()
                elif c == "3":
                    update_purchase_cli()
                    pause()
                elif c == "4":
                    delete_purchase_cli()
                    pause()
                elif c == "0":
                    break
                else:
                    print("Invalid choice.")

        elif choice == "5":
            create_tables()
            print("Tables created/verified.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")