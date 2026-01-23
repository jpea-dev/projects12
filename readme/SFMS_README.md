# SCHOOL FEE MANAGEMENT SYSTEM (SFMS)
## Class 11/12 Computer Science Practical Project

---

## PROJECT TITLE
**School Fee Management System (SFMS) - A Console-Based Application**

---

## PROJECT DESCRIPTION

The School Fee Management System (SFMS) is a menu-driven, console-based application designed to manage student information, fee assignment, payment tracking, and financial reporting in an educational institution. 

This system provides a simple yet effective solution for school administrators to:
- Maintain student records efficiently
- Track fee assignments and payments
- Monitor fee collection status
- Generate comprehensive financial reports

The system uses MySQL database for persistent data storage and is developed in Python using simple functions for easy understanding and modification.

---

## FEATURES

### ✓ Core Features
1. **Student Management**
   - Add new student with complete information
   - View student details by ID
   - Update student contact information
   - Delete student records with cascading deletion

2. **Fee Management**
   - Assign annual/monthly fee to students
   - Record fee payments (full or partial)
   - Track pending fee amounts
   - Update fee status automatically

3. **Payment Records**
   - Store detailed payment information
   - Include payment date, method, and remarks
   - View complete payment history for each student
   - Payment method tracking (Cash/Cheque/Online)

4. **Reports & Analytics**
   - Generate all students report
   - List students with pending fees
   - Calculate total fee collected
   - View collection percentage
   - Student-wise payment breakdown

5. **Data Validation & Error Handling**
   - Input validation for all fields
   - Duplicate entry prevention
   - Meaningful error messages
   - Database connection verification

---

## MODULES DESCRIPTION

### 1. Database Connection Module
- **Function**: `get_database_connection()`
  - Establishes connection to MySQL database
  - Returns connection object or None on failure
  
- **Function**: `create_tables()`
  - Creates three tables: student, fee, payment_record
  - Handles foreign key relationships
  - Uses cascading delete for data integrity

### 2. Student Management Module
Handles all student-related operations:

| Function | Purpose |
|----------|---------|
| `add_student()` | Add new student with validation |
| `view_student_details()` | Display student information |
| `update_student_info()` | Update email, phone, address |
| `delete_student_record()` | Remove student with confirmation |

### 3. Fee Management Module
Manages fee assignment and payment:

| Function | Purpose |
|----------|---------|
| `assign_fee()` | Assign fee to student |
| `pay_fee()` | Record fee payment (full/partial) |
| `view_fee_status()` | Display fee status |

### 4. Payment Records Module
Tracks payment history:

| Function | Purpose |
|----------|---------|
| `view_payment_history()` | Display all payments for a student |

### 5. Reports Module
Generates various reports:

| Function | Purpose |
|----------|---------|
| `view_all_students()` | List all students with details |
| `view_pending_fees()` | Show students with pending fees |
| `view_total_fee_collected()` | Financial summary and statistics |

### 6. Menu System Module
Provides user interface:

| Function | Purpose |
|----------|---------|
| `display_main_menu()` | Display main menu options |
| `student_management_menu()` | Student operations submenu |
| `fee_management_menu()` | Fee operations submenu |
| `payment_records_menu()` | Payment history submenu |
| `reports_menu()` | Reports submenu |
| `main()` | Main program flow controller |

---

## DATABASE SCHEMA

### Table 1: STUDENT
```sql
CREATE TABLE IF NOT EXISTS student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    class VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(200),
    date_of_admission DATE NOT NULL
);
```

**Purpose**: Stores student information  
**Fields**:
- `student_id`: Unique identifier (Auto-increment)
- `name`: Student's full name
- `roll_number`: Unique roll number
- `class`: Class and section (e.g., 11-A)
- `email`: Email address
- `phone`: Contact number
- `address`: Residential address
- `date_of_admission`: Admission date

---

### Table 2: FEE
```sql
CREATE TABLE IF NOT EXISTS fee (
    fee_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    total_fee DECIMAL(10, 2) NOT NULL,
    paid_amount DECIMAL(10, 2) DEFAULT 0,
    pending_amount DECIMAL(10, 2) NOT NULL,
    status ENUM('PAID', 'PENDING', 'PARTIAL') DEFAULT 'PENDING',
    assigned_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE
);
```

**Purpose**: Tracks fee assignment and payment status  
**Fields**:
- `fee_id`: Unique identifier
- `student_id`: Reference to student
- `total_fee`: Total fee amount
- `paid_amount`: Amount paid so far
- `pending_amount`: Remaining amount
- `status`: PAID/PENDING/PARTIAL
- `assigned_date`: Date fee was assigned

---

### Table 3: PAYMENT_RECORD
```sql
CREATE TABLE IF NOT EXISTS payment_record (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    fee_id INT NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    remarks VARCHAR(200),
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (fee_id) REFERENCES fee(fee_id) ON DELETE CASCADE
);
```

**Purpose**: Records each payment transaction  
**Fields**:
- `payment_id`: Unique identifier
- `student_id`: Reference to student
- `fee_id`: Reference to fee record
- `payment_amount`: Amount paid in this transaction
- `payment_date`: Timestamp of payment
- `payment_method`: Cash/Cheque/Online
- `remarks`: Additional comments

---

## TOOLS & TECHNOLOGIES USED

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.8+ | Programming Language |
| MySQL | 5.7+ | Database Management System |
| mysql-connector-python | 8.0+ | Database Connectivity |
| Windows PowerShell / Command Prompt | - | Program Execution |

### Required Libraries
```
mysql-connector-python==8.0.33
```

---

## DATABASE DETAILS

### Connection Parameters
```
Host:       localhost
User:       root
Password:   1234
Database:   mydb
Port:       3306 (default)
```

### Database Creation Script
```sql
-- Create database (if not exists)
CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;
```

### Tables Creation Script
The program automatically creates all required tables when option 5 (Initialize Database) is selected from the main menu.

**Manual Table Creation (if needed)**:
```sql
USE mydb;

CREATE TABLE IF NOT EXISTS student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    class VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(200),
    date_of_admission DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS fee (
    fee_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    total_fee DECIMAL(10, 2) NOT NULL,
    paid_amount DECIMAL(10, 2) DEFAULT 0,
    pending_amount DECIMAL(10, 2) NOT NULL,
    status ENUM('PAID', 'PENDING', 'PARTIAL') DEFAULT 'PENDING',
    assigned_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS payment_record (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    fee_id INT NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    remarks VARCHAR(200),
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (fee_id) REFERENCES fee(fee_id) ON DELETE CASCADE
);
```

---

## HOW TO RUN THE PROGRAM

### Prerequisites
1. **Python Installation**
   - Python 3.8 or higher installed on your system
   - Verify: Open Command Prompt and type `python --version`

2. **MySQL Server**
   - MySQL Server running on localhost
   - Database 'mydb' created
   - User 'root' with password '1234'

3. **Python Packages**
   - mysql-connector-python

### Step-by-Step Installation & Execution

#### Step 1: Install Required Package
```powershell
pip install mysql-connector-python
```

#### Step 2: Verify MySQL Connection
```powershell
mysql -h localhost -u root -p1234 -e "CREATE DATABASE IF NOT EXISTS mydb;"
```

#### Step 3: Run the Program
```powershell
python school_fee_management.py
```

#### Step 4: Initialize Database (First Time Only)
- When the program starts, select option 5: "Initialize Database"
- This will create all required tables

#### Step 5: Start Using
- Select appropriate menu options to add students, assign fees, record payments
- Use reports section to view financial summaries

### Program Menu Structure
```
MAIN MENU
├── 1. Student Management
│   ├── 1.1 Add New Student
│   ├── 1.2 View Student Details
│   ├── 1.3 Update Student Information
│   └── 1.4 Delete Student Record
├── 2. Fee Management
│   ├── 2.1 Assign Fee to Student
│   ├── 2.2 Pay Fee
│   └── 2.3 View Fee Status
├── 3. Payment Records
│   └── 3.1 View Payment History
├── 4. Reports
│   ├── 4.1 View All Students
│   ├── 4.2 View Students with Pending Fees
│   └── 4.3 View Total Fee Collected
├── 5. Initialize Database
└── 6. Exit
```

---

## IMPORTANT NOTES

1. **Database Connection**: Ensure MySQL server is running before starting the program
2. **Input Validation**: All inputs are validated. Invalid entries will show error messages
3. **Data Integrity**: Deleting a student will automatically delete associated fees and payments
4. **Fee Status**: Automatically updates based on payment amount
5. **Date Format**: All dates stored in YYYY-MM-DD format

---

## TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| "Database connection failed" | Check if MySQL server is running |
| "Access Denied" | Verify username/password (root/1234) |
| "Database does not exist" | Create database: `CREATE DATABASE mydb;` |
| "mysql-connector not found" | Install: `pip install mysql-connector-python` |

---

## FUTURE ENHANCEMENTS

1. Add fee discount functionality
2. Email notification for pending fees
3. SMS alerts for payment reminders
4. Excel report export feature
5. Graphical User Interface (GUI)
6. User authentication and role-based access
7. Multi-year fee tracking
8. Late fee calculation

---

## ACADEMIC NOTES FOR STUDENTS

### Learning Outcomes
After completing this project, students will understand:
- Database design and normalization
- SQL operations (CREATE, INSERT, UPDATE, DELETE, SELECT)
- Python database connectivity
- Menu-driven programming
- Input validation techniques
- Error handling in Python
- File organization and code structure

### Key Concepts Covered
- Functions and modular programming
- Data types and variables
- Control flow (if-else, loops)
- Exception handling
- Database operations
- User input/output
- Data validation

### CBSE Compliance
This project adheres to CBSE Computer Science practical requirements:
- Single Python file implementation
- Simple function-based approach
- Proper documentation and comments
- Clear menu-driven interface
- Real-world problem solving
- Use of appropriate data structures

---

## CONCLUSION

The School Fee Management System demonstrates practical application of programming concepts in a real-world scenario. It provides a complete solution for managing school fees with simplicity and efficiency. The system can be easily modified and extended for additional features as per institutional requirements.

This project serves as an excellent foundation for understanding database management, Python programming, and software development practices in an educational context.

---

## FILE INFORMATION

| Item | Details |
|------|---------|
| **Filename** | school_fee_management.py |
| **File Size** | ~35 KB |
| **Lines of Code** | ~1000+ |
| **Functions** | 20+ |
| **Database Tables** | 3 |
| **Target Users** | Class 11/12 Students, School Administrators |

---

## CONTACT & SUPPORT

For any issues or clarifications, refer to the inline code comments and error messages displayed during program execution.

**Program Version**: 1.0  
**Last Updated**: January 2026

---

## SQL INITIALIZATION SCRIPT

To manually initialize the database, run these SQL commands in MySQL:

```sql
-- Create Database
CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

-- Create Student Table
CREATE TABLE IF NOT EXISTS student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    class VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(200),
    date_of_admission DATE NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Create Fee Table
CREATE TABLE IF NOT EXISTS fee (
    fee_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    total_fee DECIMAL(10, 2) NOT NULL,
    paid_amount DECIMAL(10, 2) DEFAULT 0,
    pending_amount DECIMAL(10, 2) NOT NULL,
    status ENUM('PAID', 'PENDING', 'PARTIAL') DEFAULT 'PENDING',
    assigned_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Create Payment Record Table
CREATE TABLE IF NOT EXISTS payment_record (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    fee_id INT NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    remarks VARCHAR(200),
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (fee_id) REFERENCES fee(fee_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Display created tables
SHOW TABLES;
DESC student;
DESC fee;
DESC payment_record;
```

---

**END OF README**
