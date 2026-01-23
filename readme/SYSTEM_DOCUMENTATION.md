# Integrated Management Systems - Comprehensive Documentation

**Date Generated:** January 17, 2026

---

## Table of Contents

1. [System Overview](#system-overview)
2. [System Requirements](#system-requirements)
3. [Installation & Setup](#installation--setup)
4. [Database Configuration](#database-configuration)
5. [Module Structure](#module-structure)
6. [Module 1: Employee Management System](#module-1-employee-management-system)
7. [Module 2: Hotel Management System](#module-2-hotel-management-system)
8. [Module 3: Sales & Purchase Management System](#module-3-sales--purchase-management-system)
9. [Architecture & Design](#architecture--design)
10. [Error Handling & Exceptions](#error-handling--exceptions)
11. [Usage Guide](#usage-guide)

---

## System Overview

This integrated management system consists of three independent modules designed to manage different business domains:

1. **Employee Management System (EMS)** - Manages employee data, attendance, and salary processing
2. **Hotel Management System (HMS)** - Manages customers, rooms, bookings, services, and billing
3. **Sales & Purchase Management System (SPMS)** - Manages users, products, sales, and purchases

All systems use MySQL database for persistent data storage and feature command-line interfaces with interactive menu systems.

---

## System Requirements

### Software Requirements

- **Operating System:** Windows, Linux, macOS, or any OS supporting Python
- **Python Version:** 3.6 or higher
- **MySQL Server:** 5.7 or higher
- **Database:** MySQL connector module

### Hardware Requirements

- **Processor:** Dual-core processor or higher
- **RAM:** Minimum 2GB (4GB recommended)
- **Storage:** Minimum 1GB free disk space
- **Network:** TCP/IP connectivity for database communication

### Python Dependencies

```
mysql-connector-python>=8.0.0
```

### System Libraries (Standard Python)

- `datetime` - For date/time operations
- `mysql.connector` - MySQL database connectivity
- `mysql.connector.Error` - Exception handling for MySQL operations

---

## Installation & Setup

### Step 1: Install Python

Ensure Python 3.6 or higher is installed. Verify with:
```bash
python --version
```

### Step 2: Install MySQL Connector

```bash
pip install mysql-connector-python
```

Or using conda:
```bash
conda install mysql-connector-python
```

### Step 3: Set Up MySQL Database

1. Start MySQL Server:
   ```bash
   # Windows
   net start MySQL80
   
   # Linux/macOS
   sudo systemctl start mysql
   ```

2. Create the database:
   ```sql
   CREATE DATABASE mydb;
   ```

3. Verify connection:
   ```bash
   mysql -u root -p
   ```

### Step 4: Update Database Credentials

For each module, update the database connection parameters in their respective files:

**employee.py, hotelms.py:**
```python
self.connection = mysql.connector.connect(
    host='localhost',      # MySQL server address
    user='root',          # MySQL username
    password='1234',      # MySQL password
    database='mydb'       # Database name
)
```

**salespurchase.py:**
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'mydb'
}
```

### Step 5: Run Applications

Execute each application independently:

```bash
# Employee Management System
python employee.py

# Hotel Management System
python hotelms.py

# Sales & Purchase Management System
python salespurchase.py
```

---

## Database Configuration

### Database Details

- **Database Name:** `mydb`
- **Host:** `localhost`
- **Port:** 3306 (default MySQL port)
- **User:** `root`
- **Password:** `1234`

### Connection Method

- **Type:** TCP/IP Connection
- **Library:** MySQL Connector for Python
- **Transaction Mode:** Auto-commit enabled for data persistence

### Database Backup Recommendation

Perform regular backups:
```bash
mysqldump -u root -p mydb > backup.sql
```

Restore from backup:
```bash
mysql -u root -p mydb < backup.sql
```

---

## Module Structure

### File Organization

```
workspace/
├── employee.py              # Employee Management System
├── hotelms.py              # Hotel Management System
├── salespurchase.py        # Sales & Purchase Management System
├── EMPL.md                 # Employee system documentation
├── report_file.ipynb       # Jupyter notebook for reports
├── SYSTEM_DOCUMENTATION.md # This file
└── __pycache__/            # Python cache directory
```

### Module Dependencies

```
Dependencies Flow:
├── employee.py
│   ├── mysql.connector
│   ├── mysql.connector.Error
│   └── datetime
│
├── hotelms.py
│   ├── mysql.connector
│   ├── mysql.connector.Error
│   └── datetime
│
└── salespurchase.py
    ├── mysql.connector
    └── datetime
```

---

## Module 1: Employee Management System

### File: `employee.py`

#### Class: `EmployeeManagementSystem`

Main class for managing employee operations.

**Constructor:**
```python
def __init__(self):
    """Initialize system and connect to database"""
    self.connection = None
    self.cursor = None
    self.connect_db()
```

#### Database Tables

##### Table 1: `employees`

Stores employee information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| emp_id | INT | AUTO_INCREMENT PRIMARY KEY | Unique employee identifier |
| name | VARCHAR(100) | NOT NULL | Employee name |
| email | VARCHAR(100) | UNIQUE | Employee email |
| phone | VARCHAR(15) | - | Contact phone number |
| department | VARCHAR(50) | - | Department assignment |
| salary | FLOAT | - | Monthly salary amount |
| position | VARCHAR(50) | - | Job position |
| joining_date | DATE | - | Date of joining |
| status | VARCHAR(20) | DEFAULT 'Active' | Employment status |

##### Table 2: `attendance`

Tracks employee attendance records.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| attendance_id | INT | AUTO_INCREMENT PRIMARY KEY | Unique attendance record ID |
| emp_id | INT | FOREIGN KEY | Reference to employee |
| date | DATE | - | Attendance date |
| status | VARCHAR(20) | - | Present/Absent/Leave |

##### Table 3: `salary`

Maintains salary payment records.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| salary_id | INT | AUTO_INCREMENT PRIMARY KEY | Unique salary record ID |
| emp_id | INT | FOREIGN KEY | Reference to employee |
| month | INT | - | Payment month (1-12) |
| year | INT | - | Payment year |
| amount | FLOAT | - | Salary amount paid |
| paid_date | DATE | - | Payment date |

#### Key Methods

##### 1. `connect_db()`
- **Purpose:** Establish database connection
- **Parameters:** None
- **Returns:** None
- **Exceptions:** Prints error if connection fails

##### 2. `create_tables()`
- **Purpose:** Create all necessary tables if they don't exist
- **Parameters:** None
- **Returns:** None
- **Exception Handling:** Catches and displays table creation errors

##### 3. `add_employee()`
- **Purpose:** Add new employee to the system
- **Input:** Employee name, email, phone, department, salary, position, joining date
- **Output:** Confirmation message
- **Database:** INSERT operation on `employees` table

##### 4. `view_all_employees()`
- **Purpose:** Display all employees in formatted table
- **Parameters:** None
- **Output:** Formatted table with all employee details
- **Database:** SELECT all from `employees` table

##### 5. `search_employee()`
- **Purpose:** Find employee by ID
- **Input:** Employee ID
- **Output:** Employee details in formatted table
- **Database:** SELECT with WHERE clause

##### 6. `update_employee()`
- **Purpose:** Modify employee information
- **Options:**
  - Update salary
  - Update position
  - Update department
  - Update status
- **Input:** Employee ID and new value
- **Database:** UPDATE operation on `employees` table

##### 7. `delete_employee()`
- **Purpose:** Remove employee from system
- **Input:** Employee ID and confirmation
- **Output:** Deletion confirmation
- **Database:** DELETE from `employees` table

##### 8. `mark_attendance()`
- **Purpose:** Record employee attendance
- **Input:** Employee ID, date, attendance status
- **Database:** INSERT into `attendance` table

##### 9. `view_attendance()`
- **Purpose:** Display attendance records for an employee
- **Input:** Employee ID
- **Output:** Formatted attendance history
- **Database:** SELECT with JOIN between `attendance` and `employees`

##### 10. `process_salary()`
- **Purpose:** Process salary payment
- **Input:** Employee ID, month, year
- **Process:**
  1. Fetch employee salary
  2. Record payment with current date
  3. Display payment amount
- **Database:** INSERT into `salary` table

##### 11. `view_salary_records()`
- **Purpose:** Display salary history for an employee
- **Input:** Employee ID
- **Output:** Formatted salary payment history
- **Database:** SELECT with JOIN between `salary` and `employees`

##### 12. `department_report()`
- **Purpose:** Generate department statistics
- **Output:** Department-wise employee count and average salary
- **Database:** GROUP BY department aggregation

##### 13. `main_menu()`
- **Purpose:** Interactive command-line menu
- **Features:**
  - 11 operational options
  - Input validation
  - Loop until exit selection

#### Menu Options

```
1. Add Employee
2. View All Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Mark Attendance
7. View Attendance
8. Process Salary
9. View Salary Records
10. Department Report
11. Exit
```

---

## Module 2: Hotel Management System

### File: `hotelms.py`

#### Class: `HotelManagementSystem`

Main class for managing hotel operations.

**Constructor:**
```python
def __init__(self):
    """Initialize system and connect to database"""
    self.connection = None
    self.cursor = None
    self.connect_db()
```

#### Database Tables

##### Table 1: `customers`

Stores customer/guest information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| customer_id | INT | AUTO_INCREMENT PRIMARY KEY | Unique customer ID |
| name | VARCHAR(100) | NOT NULL | Customer name |
| email | VARCHAR(100) | - | Email address |
| phone | VARCHAR(15) | - | Phone number |
| address | VARCHAR(255) | - | Residential address |
| city | VARCHAR(50) | - | City name |
| country | VARCHAR(50) | - | Country name |
| id_proof | VARCHAR(50) | - | ID proof number |
| check_in_date | DATE | - | Hotel check-in date |
| check_out_date | DATE | - | Hotel check-out date |
| status | VARCHAR(20) | DEFAULT 'Active' | Customer status |

##### Table 2: `rooms`

Stores room inventory information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| room_id | INT | AUTO_INCREMENT PRIMARY KEY | Unique room ID |
| room_number | VARCHAR(10) | UNIQUE NOT NULL | Room number |
| room_type | VARCHAR(50) | - | Single/Double/Suite/Deluxe |
| capacity | INT | - | Maximum occupancy |
| price_per_night | FLOAT | - | Nightly rate |
| status | VARCHAR(20) | DEFAULT 'Available' | Available/Booked |
| floor | INT | - | Floor number |
| description | VARCHAR(255) | - | Room description |

##### Table 3: `bookings`

Tracks room booking records.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| booking_id | INT | AUTO_INCREMENT PRIMARY KEY | Unique booking ID |
| customer_id | INT | FOREIGN KEY | Reference to customer |
| room_id | INT | FOREIGN KEY | Reference to room |
| check_in_date | DATE | NOT NULL | Booking check-in |
| check_out_date | DATE | NOT NULL | Booking check-out |
| number_of_nights | INT | - | Total nights booked |
| total_cost | FLOAT | - | Total booking cost |
| status | VARCHAR(20) | DEFAULT 'Booked' | Booked/Checked-out |
| booking_date | DATE | - | Date of booking |

##### Table 4: `services`

Stores additional services requested.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| service_id | INT | AUTO_INCREMENT PRIMARY KEY | Unique service ID |
| booking_id | INT | FOREIGN KEY | Reference to booking |
| service_name | VARCHAR(100) | - | Service type name |
| service_type | VARCHAR(50) | - | Room Service/Laundry/Spa |
| cost | FLOAT | - | Service cost |
| date_requested | DATE | - | Service request date |
| status | VARCHAR(20) | DEFAULT 'Pending' | Pending/Completed |
| description | VARCHAR(255) | - | Service details |

##### Table 5: `bills`

Stores billing information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| bill_id | INT | AUTO_INCREMENT PRIMARY KEY | Unique bill ID |
| booking_id | INT | FOREIGN KEY | Reference to booking |
| room_charges | FLOAT | - | Room cost |
| service_charges | FLOAT | - | Services total |
| tax | FLOAT | - | Tax amount (10%) |
| total_amount | FLOAT | - | Total bill amount |
| payment_status | VARCHAR(20) | DEFAULT 'Pending' | Pending/Paid |
| bill_date | DATE | - | Bill generation date |

#### Key Methods

##### Customer Management

**`add_customer()`**
- Captures customer details
- Stores in `customers` table
- Validates input before insertion

**`view_all_customers()`**
- Displays all customers in formatted table
- Shows key details: ID, name, email, phone, city, country, check-in/out

**`search_customer()`**
- Searches by customer ID
- Displays full customer details

##### Room Management

**`add_room()`**
- Adds new room to inventory
- Captures: room number, type, capacity, price, floor, description

**`view_all_rooms()`**
- Lists all rooms with complete details
- Shows availability status

**`view_available_rooms()`**
- Displays only available rooms
- Helps customer selection during booking

##### Booking Management

**`book_room()`**
- Creates booking record
- Automatically calculates:
  - Number of nights
  - Total cost (nights × price_per_night)
  - Booking date
- Updates room status to 'Booked'

**`view_bookings()`**
- Shows all bookings with customer and room details
- Displays booking status and total cost

**`checkout_room()`**
- Processes customer check-out
- Generates bill with:
  - Room charges
  - Service charges (summed from services)
  - Tax (10% of subtotal)
  - Total amount
- Updates room status back to 'Available'
- Updates customer status to 'Inactive'
- Creates bill record in `bills` table

##### Service Management

**`add_service()`**
- Records additional services requested
- Links to specific booking
- Tracks cost and date requested

**`view_services()`**
- Displays all services across bookings
- Shows customer name, service type, cost, status

##### Billing

**`view_bill()`**
- Displays formatted bill for a booking
- Shows all charges and payment status
- Professional bill format with rupee currency

##### Reporting

**`generate_report()`**
- **Room Occupancy Report:** Count by room type
- **Total Bookings:** Total booking count
- **Revenue:** Sum of paid bills
- **Pending Payments:** Sum of unpaid bills

#### Menu Options

```
CUSTOMER MANAGEMENT:
1. Add Customer
2. View All Customers
3. Search Customer

ROOM MANAGEMENT:
4. Add Room
5. View All Rooms
6. View Available Rooms

BOOKING MANAGEMENT:
7. Book a Room
8. View All Bookings
9. Check-out Room

SERVICE MANAGEMENT:
10. Add Service
11. View All Services

BILLING:
12. View Bill

REPORTS:
13. Generate Hotel Report

14. Exit
```

---

## Module 3: Sales & Purchase Management System

### File: `salespurchase.py`

#### Architecture: Functional Approach

This module uses a functional architecture with separate CRUD functions for each entity rather than a class-based approach.

#### Database Configuration

**Connection Configuration:**
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'mydb'
}
```

**Connection Function:**
```python
def get_connection():
    return mysql.connector.connect(**DB_CONFIG)
```

#### Database Tables

##### Table 1: `user`

Stores user information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INT | AUTO_INCREMENT PRIMARY KEY | Unique user ID |
| username | VARCHAR(50) | UNIQUE NOT NULL | Username |
| email | VARCHAR(100) | - | Email address |

##### Table 2: `product`

Stores product catalog.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INT | AUTO_INCREMENT PRIMARY KEY | Unique product ID |
| name | VARCHAR(100) | NOT NULL | Product name |
| price | DECIMAL(10,2) | NOT NULL | Product price |

##### Table 3: `sales`

Records sales transactions.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INT | AUTO_INCREMENT PRIMARY KEY | Unique sale ID |
| product_id | INT | FOREIGN KEY | Reference to product |
| user_id | INT | FOREIGN KEY | Reference to user |
| quantity | INT | - | Units sold |
| sale_date | DATETIME | - | Sale timestamp |

##### Table 4: `purchase`

Records purchase transactions.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INT | AUTO_INCREMENT PRIMARY KEY | Unique purchase ID |
| product_id | INT | FOREIGN KEY | Reference to product |
| user_id | INT | FOREIGN KEY | Reference to user |
| quantity | INT | - | Units purchased |
| purchase_date | DATETIME | - | Purchase timestamp |

#### CRUD Operations

##### User Operations

**`create_user(username, email)`**
- **Purpose:** Add new user
- **Parameters:** username (str), email (str)
- **Operation:** INSERT into `user` table

**`get_users()`**
- **Purpose:** Retrieve all users
- **Returns:** List of dictionaries with user data
- **Operation:** SELECT * from `user` table

**`update_user(user_id, username, email)`**
- **Purpose:** Modify user details
- **Parameters:** user_id (int), username (str), email (str)
- **Operation:** UPDATE `user` table

**`delete_user(user_id)`**
- **Purpose:** Remove user
- **Parameters:** user_id (int)
- **Operation:** DELETE from `user` table

##### Product Operations

**`create_product(name, price)`**
- **Purpose:** Add new product
- **Parameters:** name (str), price (float)
- **Operation:** INSERT into `product` table

**`get_products()`**
- **Purpose:** Retrieve all products
- **Returns:** List of dictionaries with product data
- **Operation:** SELECT * from `product` table

**`update_product(product_id, name, price)`**
- **Purpose:** Modify product details
- **Parameters:** product_id (int), name (str), price (float)
- **Operation:** UPDATE `product` table

**`delete_product(product_id)`**
- **Purpose:** Remove product
- **Parameters:** product_id (int)
- **Operation:** DELETE from `product` table

##### Sales Operations

**`create_sale(product_id, user_id, quantity, sale_date)`**
- **Purpose:** Record sale transaction
- **Parameters:** product_id (int), user_id (int), quantity (int), sale_date (datetime)
- **Operation:** INSERT into `sales` table

**`get_sales()`**
- **Purpose:** Retrieve all sales
- **Returns:** List of dictionaries with sale data
- **Operation:** SELECT * from `sales` table

**`update_sale(sale_id, product_id, user_id, quantity, sale_date)`**
- **Purpose:** Modify sale record
- **Parameters:** sale_id (int), product_id (int), user_id (int), quantity (int), sale_date (datetime)
- **Operation:** UPDATE `sales` table

**`delete_sale(sale_id)`**
- **Purpose:** Remove sale record
- **Parameters:** sale_id (int)
- **Operation:** DELETE from `sales` table

##### Purchase Operations

**`create_purchase(product_id, user_id, quantity, purchase_date)`**
- **Purpose:** Record purchase transaction
- **Parameters:** product_id (int), user_id (int), quantity (int), purchase_date (datetime)
- **Operation:** INSERT into `purchase` table

**`get_purchases()`**
- **Purpose:** Retrieve all purchases
- **Returns:** List of dictionaries with purchase data
- **Operation:** SELECT * from `purchase` table

**`update_purchase(purchase_id, product_id, user_id, quantity, purchase_date)`**
- **Purpose:** Modify purchase record
- **Parameters:** purchase_id (int), product_id (int), user_id (int), quantity (int), purchase_date (datetime)
- **Operation:** UPDATE `purchase` table

**`delete_purchase(purchase_id)`**
- **Purpose:** Remove purchase record
- **Parameters:** purchase_id (int)
- **Operation:** DELETE from `purchase` table

#### Helper Functions

**`input_int(prompt)`**
- Validates integer input
- Loops until valid integer received
- Returns: int value

**`input_float(prompt)`**
- Validates float input
- Loops until valid number received
- Returns: float value

**`input_date(prompt)`**
- Accepts date in formats: YYYY-MM-DD HH:MM:SS or YYYY-MM-DD
- Defaults to current time if blank
- Returns: datetime object

**`pause()`**
- Pauses execution until user presses Enter
- Used for readability in CLI

**`list_rows(rows)`**
- Displays list of records
- Shows "No records" if empty
- Prints each row individually

#### CLI Wrapper Functions

##### User Management CLI

**`insert_user_cli()`** - Interactive user creation
**`list_users_cli()`** - Display all users
**`update_user_cli()`** - Update existing user
**`delete_user_cli()`** - Delete user

##### Product Management CLI

**`insert_product_cli()`** - Interactive product creation
**`list_products_cli()`** - Display all products
**`update_product_cli()`** - Update product details
**`delete_product_cli()`** - Delete product

##### Sales Management CLI

**`insert_sale_cli()`** - Interactive sale recording
**`list_sales_cli()`** - Display all sales
**`update_sale_cli()`** - Modify sale record
**`delete_sale_cli()`** - Delete sale record

##### Purchase Management CLI

**`insert_purchase_cli()`** - Interactive purchase recording
**`list_purchases_cli()`** - Display all purchases
**`update_purchase_cli()`** - Modify purchase record
**`delete_purchase_cli()`** - Delete purchase record

#### Menu Structure

```
Main Menu:
1. Users
2. Products
3. Sales
4. Purchases
5. Create Tables
0. Exit

Users Submenu:
1. List users
2. Create user
3. Update user
4. Delete user
0. Back

Products Submenu:
1. List products
2. Create product
3. Update product
4. Delete product
0. Back

Sales Submenu:
1. List sales
2. Create sale
3. Update sale
4. Delete sale
0. Back

Purchases Submenu:
1. List purchases
2. Create purchase
3. Update purchase
4. Delete purchase
0. Back
```

---

## Architecture & Design

### Design Patterns Used

#### 1. Class-Based Architecture (EMS & HMS)

**Advantages:**
- Encapsulation of data and methods
- State management through instance variables
- Clean separation of concerns
- Easy to extend and maintain

**Structure:**
```
Class (EMS/HMS)
├── Instance Variables
│   ├── connection
│   └── cursor
├── Core Methods
│   ├── Database connectivity
│   ├── CRUD operations
│   └── Business logic
└── Main Menu
    └── Interactive CLI
```

#### 2. Functional Architecture (SPMS)

**Advantages:**
- Stateless operations
- Function composition
- Easy to test individual functions
- Lightweight and simple

**Structure:**
```
Module Functions
├── Database Helper
│   └── get_connection()
├── CRUD Functions (User/Product/Sales/Purchase)
├── Helper Functions (Input validation, display)
└── CLI Wrapper Functions
    └── Main Loop
```

### Database Connection Pattern

All modules use MySQL Connector with persistent connection pooling:

```python
# Connection establishment
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='mydb'
)

# Cursor creation
cursor = connection.cursor()

# Transaction execution
cursor.execute(query, params)
connection.commit()

# Resource cleanup
cursor.close()
connection.close()
```

### Data Flow Architecture

```
User Input (CLI)
    ↓
Input Validation (Helper Functions)
    ↓
Business Logic (Class Methods/Functions)
    ↓
Database Query Generation
    ↓
MySQL Execution
    ↓
Result Processing
    ↓
Output Formatting/Display
    ↓
User Output (Formatted Table/Message)
```

---

## Error Handling & Exceptions

### MySQL Error Handling

**Import:**
```python
from mysql.connector import Error
```

**Usage Pattern:**
```python
try:
    # Database operation
    self.cursor.execute(query)
    self.connection.commit()
except Error as e:
    print(f"Error: {e}")
```

### Error Types Handled

#### 1. Connection Errors
- Server unavailable
- Authentication failure
- Invalid credentials
- Database not found

#### 2. Data Integrity Errors
- Duplicate primary key
- Unique constraint violation
- Foreign key constraint violation

#### 3. Execution Errors
- SQL syntax errors
- Type mismatch
- Data truncation

#### 4. Input Validation Errors
- Invalid integer input
- Invalid float input
- Invalid date format

### Error Recovery Strategies

1. **Try-Catch Blocks:** Wrap all database operations
2. **User Feedback:** Display clear error messages
3. **Input Validation:** Prevent invalid data entry
4. **Default Values:** Handle missing optional fields
5. **Transaction Rollback:** Automatic on error

### Logging Recommendations

Consider implementing logging for production:

```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Usage
logging.info("Employee added successfully")
logging.error(f"Database error: {e}")
```

---

## Usage Guide

### Running Each Module

#### Employee Management System

```bash
cd c:\Users\noteb\OneDrive\Desktop\ws
python employee.py
```

**Initial Setup:**
1. System auto-creates tables on first run
2. Select option from main menu
3. Follow prompts for data entry

**Common Workflows:**

*Add Employee:*
```
Choose: 1
Enter Employee Name: John Doe
Enter Email: john@example.com
Enter Phone: 9876543210
Enter Department: IT
Enter Salary: 50000
Enter Position: Developer
Enter Joining Date (YYYY-MM-DD): 2024-01-15
```

*View Attendance:*
```
Choose: 7
Enter Employee ID: 1
```

#### Hotel Management System

```bash
cd c:\Users\noteb\OneDrive\Desktop\ws
python hotelms.py
```

**Workflow Example: Complete Booking**

1. **Add Customer (Option 1)**
2. **Add Room (Option 4)**
3. **Book Room (Option 7)**
4. **Add Service (Option 10)**
5. **Check-out (Option 9)** - Generates bill

#### Sales & Purchase Management System

```bash
cd c:\Users\noteb\OneDrive\Desktop\ws
python salespurchase.py
```

**Menu Navigation:**
```
Choose main menu option: 1 (Users)
    Choose user option: 2 (Create user)
    Username: seller1
    Email: seller1@example.com
```

### Data Entry Guidelines

#### Date Format
- **Required Format:** YYYY-MM-DD
- **Examples:** 2024-01-15, 2024-12-25
- **For SPMS:** YYYY-MM-DD HH:MM:SS or YYYY-MM-DD

#### Currency/Decimal
- All decimal values use standard floating-point format
- **Example:** 50000.50, 99.99

#### Status Fields
- **Employee Status:** Active, Inactive
- **Attendance Status:** Present, Absent, Leave
- **Room Status:** Available, Booked
- **Booking Status:** Booked, Checked-out
- **Service Status:** Pending, Completed
- **Payment Status:** Pending, Paid

### Best Practices

1. **Data Backup:** Regularly backup MySQL database
2. **Input Validation:** Always verify data before entry
3. **Record Checking:** Search before update/delete operations
4. **Confirmation:** Confirm deletions before execution
5. **Session Management:** Properly exit from applications
6. **Database Credentials:** Use strong passwords in production

### Troubleshooting

#### Connection Issues

**Problem:** "Error: Cannot connect to MySQL"
- **Solution:** 
  - Verify MySQL server is running
  - Check credentials (host, user, password, database)
  - Ensure database exists

#### Module Not Found

**Problem:** "ModuleNotFoundError: No module named 'mysql'"
- **Solution:** Install connector with `pip install mysql-connector-python`

#### Table Issues

**Problem:** "Table doesn't exist"
- **Solution:** 
  - Delete and recreate database
  - Restart application to auto-create tables

#### Data Validation

**Problem:** "Invalid input" or "Type error"
- **Solution:** 
  - For SPMS: Use wrapper functions for input validation
  - For dates: Use exact YYYY-MM-DD format
  - For numbers: Ensure correct data type

---

## Summary

This integrated management system provides three independent but similarly architected applications:

- **Employee Management System:** Complete HR management
- **Hotel Management System:** Full hospitality operation management
- **Sales & Purchase Management System:** Inventory and transaction tracking

All systems feature:
- Robust MySQL backend
- User-friendly CLI interfaces
- Comprehensive error handling
- Clear data organization with relational databases
- CRUD operations for all entities
- Reporting and analytics capabilities

For production deployment, consider:
- Enhanced security (password hashing, role-based access)
- Detailed logging and monitoring
- Database optimization and indexing
- Regular backup procedures
- API layer for multi-user access
- Web interface replacement for CLI

---

**Document Version:** 1.0  
**Last Updated:** January 17, 2026  
**Status:** Complete and Ready for Use
