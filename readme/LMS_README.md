# Library Management System - Complete Documentation

## 1. INTRODUCTION

The Library Management System (LMS) is a comprehensive, function-driven command-line application designed to automate and streamline the operations of a modern library. This system provides a centralized platform for managing books, members, transactions, fines, and generating insightful reports. Built with Python and MySQL, it ensures efficient data handling, real-time availability tracking, and automated fine calculations for overdue books. The system is designed to be user-friendly, scalable, and suitable for libraries of all sizes, from small community libraries to large institutional libraries.

The LMS eliminates manual record-keeping, reduces human errors, and provides quick access to critical library information. It features a menu-driven interface that makes it accessible to users with varying levels of technical expertise. Whether you need to manage book inventories, track member activities, or generate comprehensive reports, this system handles it all efficiently and reliably.

## 2. SYNOPSIS

The Library Management System is a terminal-based application that provides eleven core functionalities organized into four major modules: Book Management, Member Management, Transaction Management, and Reports. The system operates on a function-driven architecture with no classes, making it lightweight and easy to understand. Each function performs a specific task related to library operations. 

The application connects to a MySQL database to persist all data permanently. Upon startup, it automatically initializes the required database tables and inserts sample data for testing purposes. Users navigate through an intuitive menu interface where they can select operations numerically. The system validates user input, manages database transactions, and provides immediate feedback on all operations.

The system follows a modular design where each function is independent and focused on a single responsibility. This approach makes the code maintainable, testable, and extensible for future enhancements. All database operations use parameterized queries to prevent SQL injection attacks and ensure data security.

## 3. SYSTEM REQUIREMENTS

### Hardware Requirements
- **Processor**: Intel Core i3 or equivalent (minimum 1.5 GHz)
- **RAM**: 2 GB minimum (4 GB recommended for optimal performance)
- **Storage**: 500 MB free disk space for application and database
- **Display**: Any standard monitor with 1024x768 or higher resolution

### Software Requirements
- **Operating System**: Windows 7 or later, Linux (Ubuntu 16.04+), or macOS 10.12+
- **Python**: Python 3.6 or higher
- **Database**: MySQL Server 5.7 or higher (or MariaDB 10.2+)
- **Terminal**: Any terminal emulator or command prompt

### Python Dependencies
```
mysql-connector-python == 8.0.33 or higher
datetime (built-in with Python)
```

### Installation Steps
1. Install Python 3.6+ from python.org
2. Install MySQL Server from mysql.com
3. Install required Python package: `pip install mysql-connector-python`
4. Ensure MySQL server is running on localhost:3306
5. Create a database: `CREATE DATABASE mydb;`
6. Download LMS.py and place it in your working directory
7. Run the application: `python LMS.py`

### Database Configuration
The application uses the following default credentials (modify as needed):
- **Host**: localhost
- **User**: root
- **Password**: 1234
- **Database**: mydb
- **Port**: 3306 (default MySQL port)

## 4. MAIN MENU STRUCTURE

When you launch the application, you will see the main menu with 11 options:

```
============================================================
        LIBRARY MANAGEMENT SYSTEM
============================================================

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
============================================================
```

## 5. MODULE DESCRIPTIONS & OUTPUT

### MODULE 1: BOOK MANAGEMENT

#### 1.1 Add Book (Option 1)
**Description**: This function allows library administrators to add new books to the inventory.

**Function**: `add_book()`

**Input Parameters**:
- Book Title (String): The name/title of the book
- Author Name (String): Author of the book
- ISBN (String): International Standard Book Number (unique identifier)
- Category (String): Book category (e.g., Programming, Fiction, Science)
- Publisher (String): Publishing company name
- Publication Year (Integer): Year the book was published
- Quantity (Integer): Number of copies to add
- Price (Float): Book price in currency units
- Shelf Location (String): Physical location in library (e.g., A1, B2)

**Sample Output**:
```
--- Add New Book ---
Enter Book Title: Python Advanced
Enter Author Name: Guido van Rossum
Enter ISBN: ISBN12345
Enter Category: Programming
Enter Publisher: Tech Publications
Enter Publication Year: 2023
Enter Quantity: 5
Enter Price: 650.00
Enter Shelf Location: A3
✓ Book added successfully!
```

**Database Table Updated**: books
**Validations**: ISBN must be unique, all fields are required

---

#### 1.2 View All Books (Option 2)
**Description**: Display a complete list of all books currently in the library with their details.

**Function**: `view_all_books()`

**Output Format**: Tabular display showing:
- Book ID
- Title
- Author
- Category
- Available copies/Total copies
- Price in rupees

**Sample Output**:
```
--- All Books ---
ID    Title                          Author               Category        Available  Price     
----------------------------------------------------------------------------------------------------
1     Python Programming             John Smith           Programming     5/5        Rs.450.00
2     Data Science Basics            Jane Doe             Data Science    3/3        Rs.650.00
3     Web Development                Mike Johnson         Programming     4/4        Rs.550.00
4     Machine Learning               Sarah Williams       AI              2/2        Rs.750.00
5     Database Design                Robert Brown         Database        3/3        Rs.500.00
```

**Data Source**: books table from database
**Sorting**: By book_id (creation order)

---

#### 1.3 Search Book (Option 3)
**Description**: Search for books using three different criteria: title, author, or ISBN.

**Function**: `search_book()`

**Search Options**:
1. Search by Title (partial match allowed)
2. Search by Author (partial match allowed)
3. Search by ISBN (exact match)

**Sample Output**:
```
--- Search Book ---
1. Search by Title
2. Search by Author
3. Search by ISBN
Enter choice: 1
Enter Book Title: Python
ID    Title                          Author               ISBN            Available
-------------------------------------------------------------------------------------------
1     Python Programming             John Smith           ISBN001         5/5
```

**Features**: Uses LIKE operator for flexible searching
**Return**: All matching books with availability information

---

### MODULE 2: MEMBER MANAGEMENT

#### 2.1 Add Member (Option 4)
**Description**: Register a new member to the library system.

**Function**: `add_member()`

**Input Parameters**:
- Member Name (String): Full name of the member
- Email (String): Email address for notifications
- Phone (String): Contact phone number
- Address (String): Residential address
- Membership Type (String): Student, Regular, or Premium
- Membership Date (Auto): Current date (automatically set)

**Sample Output**:
```
--- Add New Member ---
Enter Member Name: David Kumar
Enter Email: david@email.com
Enter Phone: 9876543210
Enter Address: 321 Elm Street
Enter Membership Type (Student/Regular/Premium): Student
✓ Member added successfully!
```

**Database Table Updated**: members
**Default Status**: Active (automatically set)
**Validations**: Name is required, email format should be valid

---

#### 2.2 View All Members (Option 5)
**Description**: Display information about all registered library members.

**Function**: `view_all_members()`

**Output Format**: Tabular display showing:
- Member ID
- Name
- Email
- Phone
- Membership Type
- Account Status

**Sample Output**:
```
--- All Members ---
ID    Name                      Email                     Phone           Type            Status    
----------------------------------------------------------------------------------------------------
1     Alice Johnson              alice@email.com           1234567890      Student         Active    
2     Bob Smith                  bob@email.com             9876543210      Regular         Active    
3     Carol White                carol@email.com           5551234567      Premium         Active    
4     David Kumar                david@email.com           9876543210      Student         Active    
```

**Filter**: Shows only active members by default
**Data Source**: members table

---

### MODULE 3: TRANSACTION MANAGEMENT

#### 3.1 Issue Book (Option 6)
**Description**: Issue a book to a library member. Updates availability and creates a transaction record.

**Function**: `issue_book()`

**Input Parameters**:
- Member ID (Integer): ID of the member borrowing the book
- Book ID (Integer): ID of the book being issued

**Processing Logic**:
1. Check if book is available (available > 0)
2. Calculate due date (14 days from issue date)
3. Create transaction record
4. Decrement available count
5. Display confirmation with due date

**Sample Output**:
```
--- Issue Book ---
Enter Member ID: 1
Enter Book ID: 2
✓ Book issued successfully! Due date: 2026-02-05
```

**Transaction Details Created**:
- Transaction ID (auto-generated)
- Member ID: 1
- Book ID: 2
- Issue Date: 2026-01-22
- Due Date: 2026-02-05
- Status: Issued
- Fine: 0

**Error Handling**: 
- "Book not available!" if no copies left
- Database error handling for invalid IDs

---

#### 3.2 Return Book (Option 7)
**Description**: Process book return, calculate fines for late returns, and update book availability.

**Function**: `return_book()`

**Input Parameters**:
- Transaction ID (Integer): ID of the original issue transaction

**Processing Logic**:
1. Find the transaction record
2. Check return date vs due date
3. Calculate fine if late (Rs. 10 per day)
4. Update transaction status to "Returned"
5. Increment available count
6. Create fine record if applicable
7. Display return confirmation and fine amount

**Sample Output**:
```
--- Return Book ---
Enter Transaction ID: 1
✓ Book returned successfully!
Fine Amount: Rs. 50.00
```

**Fine Calculation**: 
- Days late × Rs. 10 per day
- Only charged if return date > due date

**Database Updates**:
- transactions table (return_date, fine, status)
- books table (increment available)
- fines table (if fine > 0)

---

#### 3.3 View All Transactions (Option 8)
**Description**: Display comprehensive record of all book transactions with member and book details.

**Function**: `view_transactions()`

**Output Format**: Tabular display showing:
- Transaction ID
- Member Name
- Book Title
- Issue Date
- Due Date
- Return Date (or N/A if not returned)
- Fine Amount (or 0)
- Status (Issued or Returned)

**Sample Output**:
```
--- All Transactions ---
ID    Member               Book                           Issue Date  Due Date    Return Date  Fine     Status    
--------------------------------------------------------------------------------------------------------------------
1     Alice Johnson        Python Programming             2026-01-08  2026-01-22  N/A          Rs.0.00  Issued    
2     Bob Smith            Data Science Basics            2026-01-15  2026-01-29  2026-02-05   Rs.50.00 Returned  
3     Carol White          Web Development                2026-01-10  2026-01-24  2026-01-25   Rs.10.00 Returned  
```

**Joins**: Combines data from transactions, members, and books tables
**Data Source**: All transaction records

---

#### 3.4 View Overdue Books (Option 9)
**Description**: Identify and display all books that have not been returned by their due date.

**Function**: `view_overdue_books()`

**Output Format**: Tabular display showing:
- Transaction ID
- Member Name
- Book Title
- Due Date
- Days Overdue

**Sample Output**:
```
--- Overdue Books ---
Trans ID   Member               Book                           Due Date     Days Overdue   
-------------------------------------------------------------------------------------------
1          Alice Johnson        Python Programming             2026-01-22   5              
5          Emma Davis          Machine Learning               2026-01-20   7              
```

**Calculation**: Days Overdue = Today's Date - Due Date

**Filters**: Shows only records where:
- Status = 'Issued'
- Due Date < Today's Date

**Alert Purpose**: Helps library staff identify members to contact for book recovery

---

### MODULE 4: REPORTS & ANALYTICS

#### 4.1 Generate Library Report (Option 10)
**Description**: Generate comprehensive statistics and analytics about library operations.

**Function**: `generate_report()`

**Report Sections**:

**1. Total Books Statistics**
- Total number of unique book titles in database
- Total number of book copies across all titles
- Sample Output:
```
1. Total Books
Total Book Titles: 5
Total Book Copies: 17
```

**2. Book Availability**
- Number of books currently available for borrowing
- Sample Output:
```
2. Available Books
Available Books: 12
```

**3. Member Statistics**
- Count of active members in the system
- Sample Output:
```
3. Total Members
Active Members: 4
```

**4. Circulation Statistics**
- Number of books currently issued (not yet returned)
- Sample Output:
```
4. Books Issued
Currently Issued: 5
```

**5. Financial Report**
- Total fines collected from all members
- Shows only paid fines
- Sample Output:
```
5. Total Fines Collected
Total Fines Collected: Rs. 3500.00
```

**Complete Sample Output**:
```
--- Library Report ---

1. Total Books
Total Book Titles: 5
Total Book Copies: 17

2. Available Books
Available Books: 12

3. Total Members
Active Members: 4

4. Books Issued
Currently Issued: 5

5. Total Fines Collected
Total Fines Collected: Rs. 3500.00
```

**Uses**: Strategic decision-making, performance evaluation, inventory management

---

## 6. DATABASE SCHEMA

### Table: books
```
Column Name          | Data Type      | Constraints
book_id              | INT            | PRIMARY KEY, AUTO_INCREMENT
title                | VARCHAR(200)   | NOT NULL
author               | VARCHAR(100)   | 
isbn                 | VARCHAR(20)    | UNIQUE
category             | VARCHAR(50)    | 
publisher            | VARCHAR(100)   | 
publication_year     | INT            | 
quantity             | INT            | DEFAULT 1
available            | INT            | DEFAULT 1
price                | FLOAT          | 
shelf_location       | VARCHAR(20)    | 
```

### Table: members
```
Column Name          | Data Type      | Constraints
member_id            | INT            | PRIMARY KEY, AUTO_INCREMENT
name                 | VARCHAR(100)   | NOT NULL
email                | VARCHAR(100)   | 
phone                | VARCHAR(15)    | 
address              | VARCHAR(255)   | 
membership_date      | DATE           | 
membership_type      | VARCHAR(20)    | 
status               | VARCHAR(20)    | DEFAULT 'Active'
```

### Table: transactions
```
Column Name          | Data Type      | Constraints
transaction_id       | INT            | PRIMARY KEY, AUTO_INCREMENT
member_id            | INT            | FOREIGN KEY (members)
book_id              | INT            | FOREIGN KEY (books)
issue_date           | DATE           | NOT NULL
due_date             | DATE           | NOT NULL
return_date          | DATE           | 
fine                 | FLOAT          | DEFAULT 0
status               | VARCHAR(20)    | DEFAULT 'Issued'
```

### Table: fines
```
Column Name          | Data Type      | Constraints
fine_id              | INT            | PRIMARY KEY, AUTO_INCREMENT
transaction_id       | INT            | FOREIGN KEY (transactions)
amount               | FLOAT          | 
reason               | VARCHAR(100)   | 
payment_status       | VARCHAR(20)    | DEFAULT 'Unpaid'
payment_date         | DATE           | 
```

---

## 7. FEATURES & BENEFITS

### Core Features
1. **Complete Book Inventory Management**: Add, view, and search books
2. **Member Registration & Management**: Register and manage library members
3. **Automated Transaction Processing**: Issue and return books with automatic status updates
4. **Dynamic Fine Calculation**: Automatic fine generation for overdue books (Rs. 10/day)
5. **Real-time Availability Tracking**: Instant updates to book availability
6. **Comprehensive Reporting**: Statistics-driven insights into library operations
7. **Data Persistence**: All data stored in MySQL for permanent storage
8. **Error Handling**: Robust error management and user feedback
9. **User-Friendly Interface**: Intuitive menu-driven navigation
10. **SQL Injection Protection**: Parameterized queries for data security

### Benefits
- Reduces manual errors in record-keeping
- Saves time in book tracking and member management
- Provides instant access to library information
- Automates fine calculation processes
- Enables data-driven decision making
- Improves library operational efficiency
- Supports multiple membership types
- Maintains transaction history for auditing

---

## 8. USAGE EXAMPLES

### Example 1: Adding and Searching for a Book
```
User Input Sequence:
1. Select Option 1 (Add Book)
2. Enter: Title="Advanced Python", Author="Expert Dev", ISBN="NEW001"
   Category="Programming", Publisher="Tech Press", Year=2024
   Quantity=10, Price=899.99, Location="D2"
3. System confirms: "✓ Book added successfully!"
4. Select Option 3 (Search Book)
5. Choose Search by Title
6. Enter: "Advanced Python"
7. System displays the newly added book in results
```

### Example 2: Issuing and Returning a Book
```
User Input Sequence:
1. Select Option 6 (Issue Book)
2. Enter Member ID: 2, Book ID: 3
3. System confirms: "✓ Book issued successfully! Due date: 2026-02-05"
4. (After 5 days) Select Option 7 (Return Book)
5. Enter Transaction ID: 1
6. System calculates fine for late return (if applicable)
7. System confirms: "✓ Book returned successfully! Fine Amount: Rs. 50.00"
```

### Example 3: Generating Library Statistics
```
User Input Sequence:
1. Select Option 10 (Generate Library Report)
2. System displays:
   - Total Books: 5 titles, 17 copies
   - Available Books: 12
   - Active Members: 4
   - Currently Issued: 5
   - Total Fines Collected: Rs. 3500.00
3. User can use this information for management decisions
```

---

## 9. TROUBLESHOOTING

### Issue: Database Connection Error
**Solution**: Ensure MySQL is running, check host/user/password settings

### Issue: Module 'mysql.connector' not found
**Solution**: Run `pip install mysql-connector-python`

### Issue: No books/members found
**Solution**: Run Add Book/Member first, or check database connection

### Issue: Invalid Transaction ID
**Solution**: Verify the transaction ID exists using View Transactions

---

## 10. CONCLUSION

The Library Management System provides a robust, efficient, and user-friendly solution for modern library operations. With its comprehensive set of features, intuitive interface, and reliable database backend, it streamlines all aspects of library management from book acquisition to member management and transaction processing. Whether you're managing a small community library or a large institutional library, this system adapts to your needs and helps you deliver better service to your patrons.

