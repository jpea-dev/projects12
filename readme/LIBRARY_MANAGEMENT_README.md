# LIBRARY MANAGEMENT SYSTEM

## Project Overview

A comprehensive menu-driven Library Management System built with Python and MySQL. This system provides complete functionality for managing books, members, transactions, and generating reports.

**Technology Stack:**
- Python 3.x
- MySQL Database
- mysql-connector-python

**Current Date:** January 22, 2026

---

## Table of Contents

1. [Features](#features)
2. [System Architecture](#system-architecture)
3. [Database Schema](#database-schema)
4. [Module Functions](#module-functions)
5. [Usage Guide](#usage-guide)
6. [Sample Outputs](#sample-outputs)
7. [Installation](#installation)

---

## Features

### 1. **Book Management**
- Add new books to the library
- View all books in inventory
- Search books by Title, Author, or ISBN
- Track book availability and quantity

### 2. **Member Management**
- Register new library members
- View all registered members
- Support for different membership types (Student, Regular, Premium)
- Track member status and contact information

### 3. **Transaction Management**
- Issue books to members
- Return books with automatic fine calculation
- View all transactions with detailed history
- Track overdue books

### 4. **Reporting & Analytics**
- Generate comprehensive library reports
- View total books and availability
- Monitor active members
- Track issued books and fines collected

---

## System Architecture

### Function Categories

```
DATABASE FUNCTIONS
├── connect_db()              - Database connection
├── create_tables()           - Create schema
└── insert_sample_data()      - Initialize sample data

BOOK MANAGEMENT
├── add_book()                - Add new book
├── view_all_books()          - Display all books
└── search_book()             - Search by criteria

MEMBER MANAGEMENT
├── add_member()              - Register new member
└── view_all_members()        - Display all members

TRANSACTION MANAGEMENT
├── issue_book()              - Issue book to member
├── return_book()             - Return book with fine
├── view_transactions()       - View all transactions
└── view_overdue_books()      - Display overdue books

REPORTING
└── generate_report()         - Generate library report

MENU INTERFACE
└── main_menu()               - Main program loop
```

---

## Database Schema

### 1. **BOOKS TABLE**
```sql
CREATE TABLE books (
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
```

**Sample Data:**
| ID | Title | Author | Category | Available | Price |
|:--|:--|:--|:--|:--|:--|
| 1 | Python Programming | John Smith | Programming | 5/5 | Rs.450.00 |
| 2 | Data Science Basics | Jane Doe | Data Science | 3/3 | Rs.650.00 |
| 3 | Web Development | Mike Johnson | Programming | 4/4 | Rs.550.00 |
| 4 | Machine Learning | Sarah Williams | AI | 2/2 | Rs.750.00 |
| 5 | Database Design | Robert Brown | Database | 3/3 | Rs.500.00 |

---

### 2. **MEMBERS TABLE**
```sql
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(255),
    membership_date DATE,
    membership_type VARCHAR(20),
    status VARCHAR(20) DEFAULT 'Active'
)
```

**Sample Data:**
| ID | Name | Email | Phone | Membership Type | Status |
|:--|:--|:--|:--|:--|:--|
| 1 | Alice Johnson | alice@email.com | 1234567890 | Student | Active |
| 2 | Bob Smith | bob@email.com | 9876543210 | Regular | Active |
| 3 | Carol White | carol@email.com | 5551234567 | Premium | Active |

---

### 3. **TRANSACTIONS TABLE**
```sql
CREATE TABLE transactions (
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
```

---

### 4. **FINES TABLE**
```sql
CREATE TABLE fines (
    fine_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT,
    amount FLOAT,
    reason VARCHAR(100),
    payment_status VARCHAR(20) DEFAULT 'Unpaid',
    payment_date DATE,
    FOREIGN KEY(transaction_id) REFERENCES transactions(transaction_id)
)
```

---

## Module Functions

### DATABASE INITIALIZATION

#### `connect_db()`
**Purpose:** Establish connection with MySQL database
- Connects to 'mydb' database
- Creates tables if not exist
- Inserts sample data on first run
- **Returns:** Boolean (True/False)

```python
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
        return True
    except Error as e:
        print(f"Error: {e}")
        return False
```

---

#### `create_tables()`
**Purpose:** Create required database tables with proper schema
- Creates 4 tables: books, members, transactions, fines
- Uses IF NOT EXISTS clause for idempotency
- Establishes foreign key relationships

---

#### `insert_sample_data()`
**Purpose:** Insert initial sample data for demonstration
- 5 sample books with pricing
- 3 sample members with different membership types
- Only runs once (checks existing data)

---

### BOOK MANAGEMENT

#### `add_book()`
**Purpose:** Add a new book to the library database

**User Input:**
```
- Title: Book name
- Author: Author name
- ISBN: Unique ISBN number
- Category: Book category (Programming, AI, Database, etc.)
- Publisher: Publisher name
- Publication Year: Year of publication (Integer)
- Quantity: Number of copies
- Price: Book price in rupees
- Shelf Location: Physical location code
```

**Output:**
```
--- Add New Book ---
Enter Book Title: Advanced Python
Enter Author Name: David Miller
Enter ISBN: ISBN006
Enter Category: Programming
Enter Publisher: Tech Academy
Enter Publication Year: 2023
Enter Quantity: 2
Enter Price: 599.00
Enter Shelf Location: D1
✓ Book added successfully!
```

---

#### `view_all_books()`
**Purpose:** Display all books in the library

**Output:**
```
--- All Books ---
ID    Title                          Author               Category        Available  Price     
---------------------------------------------------------------------------------------------------
1     Python Programming             John Smith           Programming     5/5        Rs.450.00 
2     Data Science Basics            Jane Doe             Data Science    3/3        Rs.650.00 
3     Web Development                Mike Johnson         Programming     4/4        Rs.550.00 
4     Machine Learning               Sarah Williams       AI              2/2        Rs.750.00 
5     Database Design                Robert Brown         Database        3/3        Rs.500.00 
```

---

#### `search_book()`
**Purpose:** Search for books using multiple criteria

**Options:**
1. Search by Title
2. Search by Author
3. Search by ISBN

**Example Output:**
```
--- Search Book ---
1. Search by Title
2. Search by Author
3. Search by ISBN
Enter choice: 1
Enter Book Title: Python

ID    Title                          Author               ISBN            Available 
------------------------------------------------------------------------------------------
1     Python Programming             John Smith           ISBN001         5/5
```

---

### MEMBER MANAGEMENT

#### `add_member()`
**Purpose:** Add a new member to the library

**User Input:**
```
- Name: Member full name
- Email: Email address
- Phone: Contact number
- Address: Physical address
- Membership Type: Student/Regular/Premium
```

**Output:**
```
--- Add New Member ---
Enter Member Name: David Kumar
Enter Email: david.kumar@email.com
Enter Phone: 7890123456
Enter Address: 321 Elm Street
Enter Membership Type (Student/Regular/Premium): Premium
✓ Member added successfully!
```

---

#### `view_all_members()`
**Purpose:** Display all library members

**Output:**
```
--- All Members ---
ID    Name                      Email                     Phone           Type            Status    
----------------------------------------------------------------------------------------------------
1     Alice Johnson              alice@email.com           1234567890      Student         Active    
2     Bob Smith                  bob@email.com             9876543210      Regular         Active    
3     Carol White                carol@email.com           5551234567      Premium         Active    
```

---

### TRANSACTION MANAGEMENT

#### `issue_book()`
**Purpose:** Issue a book to a member

**Process:**
1. Enter Member ID and Book ID
2. Check book availability
3. Create transaction record
4. Decrease available quantity
5. Set due date (14 days from issue)

**Output:**
```
--- Issue Book ---
Enter Member ID: 1
Enter Book ID: 2
✓ Book issued successfully! Due date: 2026-02-05
```

---

#### `return_book()`
**Purpose:** Return a book to the library with automatic fine calculation

**Process:**
1. Enter Transaction ID
2. Verify book is issued
3. Calculate fine if overdue (Rs. 10 per day)
4. Update transaction status
5. Increase book availability
6. Record fine if applicable

**Output - On Time Return:**
```
--- Return Book ---
Enter Transaction ID: 1
✓ Book returned successfully!
```

**Output - Late Return:**
```
--- Return Book ---
Enter Transaction ID: 2
✓ Book returned successfully!
Fine Amount: Rs. 30.00
```

---

#### `view_transactions()`
**Purpose:** Display all book transactions with details

**Output:**
```
--- All Transactions ---
ID    Member               Book                           Issue Date  Due Date    Return Date Fine     Status    
-----------------------------------------------------------------------------------------------------------------
1     Alice Johnson        Data Science Basics            2026-01-15  2026-01-29  2026-01-30  Rs.10.00  Returned  
2     Bob Smith            Web Development                2026-01-18  2026-02-01  N/A         Rs.0.00   Issued    
3     Carol White          Python Programming            2026-01-20  2026-02-03  N/A         Rs.0.00   Issued    
```

---

#### `view_overdue_books()`
**Purpose:** Display all books that are overdue

**Output:**
```
--- Overdue Books ---
Trans ID   Member               Book                           Due Date    Days Overdue   
---------------------------------------------------------------------------------------
2          Bob Smith            Web Development                2026-02-01  15            
```

---

### REPORTING

#### `generate_report()`
**Purpose:** Generate comprehensive library statistics and analytics

**Output:**
```
--- Library Report ---

1. Total Books
   Total Book Titles: 5
   Total Book Copies: 17

2. Available Books
   Available Books: 15

3. Total Members
   Active Members: 3

4. Books Issued
   Currently Issued: 2

5. Total Fines Collected
   Total Fines Collected: Rs. 40.00
```

---

## Usage Guide

### Installation

1. **Install Python Dependencies:**
```bash
pip install mysql-connector-python
```

2. **Setup MySQL Database:**
```sql
CREATE DATABASE mydb;
```

3. **Update Credentials:**
Edit the `connect_db()` function with your database credentials:
```python
connection = mysql.connector.connect(
    host='localhost',        # Your host
    user='root',             # Your username
    password='1234',         # Your password
    database='mydb'          # Your database name
)
```

4. **Run the Program:**
```bash
python estore.py
```

---

### Main Menu Navigation

**System Start:**
```
================================================================
        LIBRARY MANAGEMENT SYSTEM
================================================================

--- BOOK MANAGEMENT ---
1. Add Book
2. View All Books
3. Search Book

--- MEMBER MANAGEMENT ---
4. Add Member
5. View All Members

--- TRANSACTION MANAGEMENT ---
6. Issue Book
7. Return Book
8. View All Transactions
9. View Overdue Books

--- REPORTS ---
10. Generate Library Report

11. Exit
================================================================

Enter your choice (1-11): 
```

---

## Sample Outputs

### Sample 1: Complete Transaction Workflow

```
Enter your choice (1-11): 2

--- All Books ---
ID    Title                          Author               Category        Available  Price     
1     Python Programming             John Smith           Programming     5/5        Rs.450.00 
2     Data Science Basics            Jane Doe             Data Science    3/3        Rs.650.00 
3     Web Development                Mike Johnson         Programming     4/4        Rs.550.00 

Enter your choice (1-11): 5

--- All Members ---
ID    Name                      Email                     Phone           Type            Status    
1     Alice Johnson              alice@email.com           1234567890      Student         Active    
2     Bob Smith                  bob@email.com             9876543210      Regular         Active    
3     Carol White                carol@email.com           5551234567      Premium         Active    

Enter your choice (1-11): 6

--- Issue Book ---
Enter Member ID: 1
Enter Book ID: 2
✓ Book issued successfully! Due date: 2026-02-05

Enter your choice (1-11): 8

--- All Transactions ---
ID    Member               Book                           Issue Date  Due Date    Return Date Fine     Status    
1     Alice Johnson        Data Science Basics            2026-01-22  2026-02-05  N/A         Rs.0.00   Issued    
```

---

### Sample 2: Overdue and Fine Calculation

```
Enter your choice (1-11): 7

--- Return Book ---
Enter Transaction ID: 1
✓ Book returned successfully!
Fine Amount: Rs. 30.00

(Transaction was 3 days overdue: 3 × Rs.10 = Rs.30)
```

---

### Sample 3: Search and Add New Book

```
Enter your choice (1-11): 3

--- Search Book ---
1. Search by Title
2. Search by Author
3. Search by ISBN
Enter choice: 2

Enter Author Name: John Smith

ID    Title                          Author               ISBN            Available 
1     Python Programming             John Smith           ISBN001         5/5

Enter your choice (1-11): 1

--- Add New Book ---
Enter Book Title: Cloud Computing Basics
Enter Author Name: Emma Wilson
Enter ISBN: ISBN007
Enter Category: Cloud
Enter Publisher: Cloud Press
Enter Publication Year: 2024
Enter Quantity: 4
Enter Price: 699.00
Enter Shelf Location: E2
✓ Book added successfully!
```

---

### Sample 4: Generate Report

```
Enter your choice (1-11): 10

--- Library Report ---

1. Total Books
   Total Book Titles: 6
   Total Book Copies: 21

2. Available Books
   Available Books: 18

3. Total Members
   Active Members: 3

4. Books Issued
   Currently Issued: 3

5. Total Fines Collected
   Total Fines Collected: Rs. 70.00
```

---

## Error Handling

The system includes comprehensive error handling for:

1. **Database Connection Errors**
   ```
   Error: (1045, "Access denied for user 'root'@'localhost'")
   ```

2. **Data Validation Errors**
   ```
   Error: (1062, "Duplicate entry 'ISBN001' for key 'isbn'")
   ```

3. **Transaction Errors**
   ```
   Error: Book not available!
   ```

4. **Invalid User Input**
   ```
   Invalid choice! Try again.
   ```

---

## Key Features Explained

### 1. **Automatic Fine Calculation**
- Rs. 10 per day after due date
- Automatically calculated on return
- Fine records stored in database

### 2. **Book Availability Tracking**
- Automatic decrement on issue
- Automatic increment on return
- Prevents over-issuing

### 3. **Member Membership Types**
- **Student:** Educational discount eligible
- **Regular:** Standard membership
- **Premium:** Priority access

### 4. **Transaction History**
- Complete issue/return history
- Fine tracking
- Status monitoring (Issued/Returned)

### 5. **Reporting Analytics**
- Real-time statistics
- Inventory insights
- Member engagement metrics
- Fine collection tracking

---

## Database Relationships

```
BOOKS ─────────┐
                ├──→ TRANSACTIONS ──→ FINES
MEMBERS ────────┘
```

---

## Future Enhancements

1. **Advanced Search** - Multi-criteria search filters
2. **Renewal System** - Allow book renewals
3. **Reservation** - Reserve books in advance
4. **Email Notifications** - Automated due date reminders
5. **Payment Gateway** - Online fine payment
6. **User Authentication** - Login system for staff
7. **Import/Export** - Backup and restore functionality
8. **Mobile App** - Dedicated mobile application

---

## Support & Troubleshooting

### Issue: Database Connection Failed
**Solution:** 
1. Verify MySQL is running
2. Check database credentials
3. Ensure 'mydb' database exists

### Issue: Duplicate ISBN Error
**Solution:** Use unique ISBN for each book

### Issue: Fine Not Calculated
**Solution:** Ensure return date is after due date

### Issue: No Members Found
**Solution:** Add members first using option 4

---

## License

This project is for educational purposes.

---

## Version History

| Version | Date | Changes |
|:--|:--|:--|
| 1.0 | 2026-01-22 | Initial release with core functionality |

---

## Contact & Support

For issues or questions, please contact the library management team.

**System Generated:** 2026-01-22
**Last Updated:** 2026-01-22

---

## Technical Notes

- **Database:** MySQL
- **Python Version:** 3.6+
- **Connector:** mysql-connector-python 8.0+
- **Date Format:** YYYY-MM-DD
- **Currency:** Indian Rupees (Rs.)
- **Fine Rate:** Rs. 10 per day
- **Book Issue Duration:** 14 days

---

**END OF README**
