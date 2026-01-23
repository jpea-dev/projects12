from mysql.connector import Error
import datetime
import mysql.connector

# Global database connection variables
connection = None
cursor = None

def connect_db():
    """Establish connection with MySQL database"""
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
    """Create required database tables"""
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                book_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                author VARCHAR(100),
                isbn VARCHAR(20) UNIQUE,
                category VARCHAR(50),
                publisher VARCHAR(100),
                publication_year INT,
                quantity INT DEFAULT 1,
                available INT DEFAULT 1,
                price FLOAT,
                shelf_location VARCHAR(20)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS members (
                member_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100),
                phone VARCHAR(15),
                address VARCHAR(255),
                membership_date DATE,
                membership_type VARCHAR(20),
                status VARCHAR(20) DEFAULT 'Active'
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT,
                book_id INT,
                issue_date DATE NOT NULL,
                due_date DATE NOT NULL,
                return_date DATE,
                fine FLOAT DEFAULT 0,
                status VARCHAR(20) DEFAULT 'Issued',
                FOREIGN KEY(member_id) REFERENCES members(member_id),
                FOREIGN KEY(book_id) REFERENCES books(book_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fines (
                fine_id INT AUTO_INCREMENT PRIMARY KEY,
                transaction_id INT,
                amount FLOAT,
                reason VARCHAR(100),
                payment_status VARCHAR(20) DEFAULT 'Unpaid',
                payment_date DATE,
                FOREIGN KEY(transaction_id) REFERENCES transactions(transaction_id)
            )
        ''')

        connection.commit()
        print("✓ Tables created successfully!")
    except Error as e:
        print(f"Table creation error: {e}")

def insert_sample_data():
    """Insert initial sample data into tables"""
    try:
        cursor.execute("SELECT COUNT(*) FROM books")
        if cursor.fetchone()[0] == 0:
            books_data = [
                ("Python Programming", "John Smith", "ISBN001", "Programming", "Tech Books", 2020, 5, 5, 450.00, "A1"),
                ("Data Science Basics", "Jane Doe", "ISBN002", "Data Science", "Science Pub", 2021, 3, 3, 650.00, "A2"),
                ("Web Development", "Mike Johnson", "ISBN003", "Programming", "Web Books", 2019, 4, 4, 550.00, "B1"),
                ("Machine Learning", "Sarah Williams", "ISBN004", "AI", "ML Press", 2022, 2, 2, 750.00, "B2"),
                ("Database Design", "Robert Brown", "ISBN005", "Database", "DB Publishers", 2020, 3, 3, 500.00, "C1")
            ]

            query = '''INSERT INTO books (title, author, isbn, category, publisher, publication_year, quantity, available, price, shelf_location)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.executemany(query, books_data)

            members_data = [
                ("Alice Johnson", "alice@email.com", "1234567890", "123 Main St", "2023-01-15", "Student", "Active"),
                ("Bob Smith", "bob@email.com", "9876543210", "456 Oak Ave", "2023-02-20", "Regular", "Active"),
                ("Carol White", "carol@email.com", "5551234567", "789 Pine Rd", "2023-03-10", "Premium", "Active")
            ]

            query = '''INSERT INTO members (name, email, phone, address, membership_date, membership_type, status)
                      VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            cursor.executemany(query, members_data)

            connection.commit()
            print("✓ Sample data inserted successfully!")
    except Error as e:
        pass

def add_book():
    """Add a new book to the library database"""
    print("\n--- Add New Book ---")
    try:
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        isbn = input("Enter ISBN: ")
        category = input("Enter Category: ")
        publisher = input("Enter Publisher: ")
        publication_year = int(input("Enter Publication Year: "))
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        shelf_location = input("Enter Shelf Location: ")

        query = '''INSERT INTO books (title, author, isbn, category, publisher, publication_year, quantity, available, price, shelf_location)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

        cursor.execute(query, (title, author, isbn, category, publisher, publication_year, quantity, quantity, price, shelf_location))
        connection.commit()
        print("✓ Book added successfully!")
    except Error as e:
        print(f"Error: {e}")

def view_all_books():
    """Display all books in the library"""
    print("\n--- All Books ---")
    try:
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        if books:
            print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Category':<15} {'Available':<10} {'Price':<10}")
            print("-" * 100)
            for book in books:
                book_id, title, author, isbn, category, publisher, year, quantity, available, price, shelf = book
                print(f"{book_id:<5} {title:<30} {author:<20} {category:<15} {available}/{quantity:<8} Rs.{price:<8.2f}")
        else:
            print("No books found!")
    except Error as e:
        print(f"Error: {e}")

def search_book():
    """Search for books using various criteria"""
    print("\n--- Search Book ---")
    print("1. Search by Title")
    print("2. Search by Author")
    print("3. Search by ISBN")
    choice = input("Enter choice: ")

    try:
        if choice == "1":
            title = input("Enter Book Title: ")
            cursor.execute("SELECT * FROM books WHERE title LIKE %s", (f"%{title}%",))
        elif choice == "2":
            author = input("Enter Author Name: ")
            cursor.execute("SELECT * FROM books WHERE author LIKE %s", (f"%{author}%",))
        elif choice == "3":
            isbn = input("Enter ISBN: ")
            cursor.execute("SELECT * FROM books WHERE isbn = %s", (isbn,))
        else:
            print("Invalid choice!")
            return

        books = cursor.fetchall()
        if books:
            print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'ISBN':<15} {'Available':<10}")
            print("-" * 90)
            for book in books:
                book_id, title, author, isbn, category, publisher, year, quantity, available, price, shelf = book
                print(f"{book_id:<5} {title:<30} {author:<20} {isbn:<15} {available}/{quantity}")
        else:
            print("No books found!")
    except Error as e:
        print(f"Error: {e}")

def add_member():
    """Add a new member to the library"""
    print("\n--- Add New Member ---")
    try:
        name = input("Enter Member Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        address = input("Enter Address: ")
        membership_type = input("Enter Membership Type (Student/Regular/Premium): ")
        membership_date = datetime.date.today()

        query = '''INSERT INTO members (name, email, phone, address, membership_date, membership_type)
                  VALUES (%s, %s, %s, %s, %s, %s)'''

        cursor.execute(query, (name, email, phone, address, membership_date, membership_type))
        connection.commit()
        print("✓ Member added successfully!")
    except Error as e:
        print(f"Error: {e}")

def view_all_members():
    """Display all library members"""
    print("\n--- All Members ---")
    try:
        cursor.execute("SELECT * FROM members")
        members = cursor.fetchall()

        if members:
            print(f"{'ID':<5} {'Name':<25} {'Email':<25} {'Phone':<15} {'Type':<15} {'Status':<10}")
            print("-" * 100)
            for member in members:
                member_id, name, email, phone, address, mem_date, mem_type, status = member
                print(f"{member_id:<5} {name:<25} {email or 'N/A':<25} {phone or 'N/A':<15} {mem_type:<15} {status:<10}")
        else:
            print("No members found!")
    except Error as e:
        print(f"Error: {e}")

def issue_book():
    """Issue a book to a member"""
    print("\n--- Issue Book ---")
    try:
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))

        cursor.execute("SELECT available FROM books WHERE book_id = %s", (book_id,))
        result = cursor.fetchone()

        if result and result[0] > 0:
            issue_date = datetime.date.today()
            due_date = issue_date + datetime.timedelta(days=14)

            query = '''INSERT INTO transactions (member_id, book_id, issue_date, due_date)
                      VALUES (%s, %s, %s, %s)'''

            cursor.execute(query, (member_id, book_id, issue_date, due_date))
            cursor.execute("UPDATE books SET available = available - 1 WHERE book_id = %s", (book_id,))

            connection.commit()
            print(f"✓ Book issued successfully! Due date: {due_date}")
        else:
            print("Book not available!")
    except Error as e:
        print(f"Error: {e}")

def return_book():
    """Return a book to the library"""
    print("\n--- Return Book ---")
    try:
        transaction_id = int(input("Enter Transaction ID: "))

        cursor.execute('''SELECT book_id, due_date FROM transactions
                          WHERE transaction_id = %s AND status = 'Issued' ''', (transaction_id,))
        result = cursor.fetchone()

        if result:
            book_id, due_date = result
            return_date = datetime.date.today()

            fine = 0
            if return_date > due_date:
                days_late = (return_date - due_date).days
                fine = days_late * 10

            cursor.execute('''UPDATE transactions SET return_date = %s, fine = %s, status = 'Returned'
                              WHERE transaction_id = %s''', (return_date, fine, transaction_id))

            cursor.execute("UPDATE books SET available = available + 1 WHERE book_id = %s", (book_id,))

            if fine > 0:
                cursor.execute('''INSERT INTO fines (transaction_id, amount, reason)
                                  VALUES (%s, %s, %s)''', (transaction_id, fine, "Late Return"))

            connection.commit()
            print(f"✓ Book returned successfully!")
            if fine > 0:
                print(f"Fine Amount: Rs. {fine:.2f}")
        else:
            print("Transaction not found or already returned!")
    except Error as e:
        print(f"Error: {e}")

def view_transactions():
    """Display all book transactions"""
    print("\n--- All Transactions ---")
    try:
        cursor.execute('''SELECT t.transaction_id, m.name, b.title, t.issue_date, t.due_date, t.return_date, t.fine, t.status
                          FROM transactions t
                          JOIN members m ON t.member_id = m.member_id
                          JOIN books b ON t.book_id = b.book_id''')
        transactions = cursor.fetchall()

        if transactions:
            print(f"{'ID':<5} {'Member':<20} {'Book':<30} {'Issue Date':<12} {'Due Date':<12} {'Return Date':<12} {'Fine':<8} {'Status':<10}")
            print("-" * 120)
            for trans in transactions:
                trans_id, member, book, issue, due, ret, fine, status = trans
                ret_date = ret if ret else "N/A"
                print(f"{trans_id:<5} {member:<20} {book:<30} {issue} {due} {str(ret_date):<12} Rs.{fine:<6.2f} {status:<10}")
        else:
            print("No transactions found!")
    except Error as e:
        print(f"Error: {e}")

def view_overdue_books():
    """Display all overdue books"""
    print("\n--- Overdue Books ---")
    try:
        today = datetime.date.today()
        cursor.execute('''SELECT t.transaction_id, m.name, b.title, t.issue_date, t.due_date,
                          DATEDIFF(%s, t.due_date) as days_overdue
                          FROM transactions t
                          JOIN members m ON t.member_id = m.member_id
                          JOIN books b ON t.book_id = b.book_id
                          WHERE t.status = 'Issued' AND t.due_date < %s''', (today, today))
        overdue = cursor.fetchall()

        if overdue:
            print(f"{'Trans ID':<10} {'Member':<20} {'Book':<30} {'Due Date':<12} {'Days Overdue':<15}")
            print("-" * 100)
            for item in overdue:
                trans_id, member, book, issue, due, days = item
                print(f"{trans_id:<10} {member:<20} {book:<30} {due} {days:<15}")
        else:
            print("No overdue books!")
    except Error as e:
        print(f"Error: {e}")

def generate_report():
    """Generate comprehensive library report"""
    print("\n--- Library Report ---")
    try:
        print("\n1. Total Books")
        cursor.execute("SELECT COUNT(*), SUM(quantity) FROM books")
        result = cursor.fetchone()
        print(f"Total Book Titles: {result[0]}")
        print(f"Total Book Copies: {result[1]}")

        print("\n2. Available Books")
        cursor.execute("SELECT SUM(available) FROM books")
        available = cursor.fetchone()[0]
        print(f"Available Books: {available}")

        print("\n3. Total Members")
        cursor.execute("SELECT COUNT(*) FROM members WHERE status = 'Active'")
        members = cursor.fetchone()[0]
        print(f"Active Members: {members}")

        print("\n4. Books Issued")
        cursor.execute("SELECT COUNT(*) FROM transactions WHERE status = 'Issued'")
        issued = cursor.fetchone()[0]
        print(f"Currently Issued: {issued}")

        print("\n5. Total Fines Collected")
        cursor.execute("SELECT SUM(amount) FROM fines WHERE payment_status = 'Paid'")
        fines_result = cursor.fetchone()
        fines = fines_result[0] if fines_result[0] else 0
        print(f"Total Fines Collected: Rs. {fines:.2f}")
    except Error as e:
        print(f"Error: {e}")

def main_menu():
    """Main menu for the Library Management System"""
    while True:
        print("\n" + "="*60)
        print("        LIBRARY MANAGEMENT SYSTEM")
        print("="*60)
        print("\n--- BOOK MANAGEMENT ---")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")

        print("\n--- MEMBER MANAGEMENT ---")
        print("4. Add Member")
        print("5. View All Members")

        print("\n--- TRANSACTION MANAGEMENT ---")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. View All Transactions")
        print("9. View Overdue Books")

        print("\n--- REPORTS ---")
        print("10. Generate Library Report")

        print("\n11. Exit")
        print("="*60)

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_all_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            add_member()
        elif choice == "5":
            view_all_members()
        elif choice == "6":
            issue_book()
        elif choice == "7":
            return_book()
        elif choice == "8":
            view_transactions()
        elif choice == "9":
            view_overdue_books()
        elif choice == "10":
            generate_report()
        elif choice == "11":
            print("\nThank you for using Library Management System!")
            cursor.close()
            connection.close()
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    connect_db()
    main_menu()
