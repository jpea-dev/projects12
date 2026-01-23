# Employee Management System - Documentation

## Overview
The Employee Management System (EMS) is a Python-based application that provides comprehensive employee data management, attendance tracking, and salary processing functionalities. It uses MySQL database for persistent data storage and features a command-line interface with an interactive menu system.

---

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation & Setup](#installation--setup)
3. [Database Configuration](#database-configuration)
4. [Module Structure](#module-structure)
5. [Class Documentation](#class-documentation)
6. [Method Documentation](#method-documentation)
7. [Features](#features)
8. [Usage Guide](#usage-guide)
9. [Error Handling](#error-handling)

---

## System Requirements

### Dependencies
- Python 3.6 or higher
- MySQL Server 5.7 or higher
- MySQL Connector for Python (`mysql-connector-python`)

### Required Packages
```
mysql-connector-python
```

### System Libraries
- Python Standard Library modules:
  - `datetime` - For date/time operations
  - Error handling from `mysql.connector`

---

## Installation & Setup

### Step 1: Install Python Package
```bash
pip install mysql-connector-python
```

### Step 2: MySQL Database Setup
Create a MySQL database named `mydb`:
```sql
CREATE DATABASE mydb;
```

### Step 3: Update Connection Credentials
Modify the database connection parameters in the `connect_db()` method:
- **Host**: localhost (or your MySQL server address)
- **User**: root (or your MySQL username)
- **Password**: 1234 (or your MySQL password)
- **Database**: mydb (or your database name)

### Step 4: Run the Application
```bash
python employee.py
```

---

## Database Configuration

### Database Name
- **Database**: `mydb`
- **Host**: `localhost`
- **Port**: 3306 (default)
- **User**: `root`
- **Password**: `1234`

### Connection Type
- TCP/IP Connection using MySQL Connector for Python
- Committed transactions ensure data persistence

---

## Module Structure

### Imports Section

```
from mysql.connector import Error
```
- Used for exception handling specific to MySQL operations

```
import datetime
```
- Used for date/time operations, particularly in salary processing

```
import mysql.connector
```
- Main MySQL connectivity library for database operations

---

## Class Documentation

### EmployeeManagementSystem Class

**Purpose**: Main class that encapsulates all employee management operations and database interactions.

**Attributes**:
- `connection` - MySQL database connection object (initialized as None)
- `cursor` - MySQL cursor object for executing queries (initialized as None)

**Initialization**:
The `__init__()` method is automatically called when creating an instance, which:
1. Initializes connection and cursor to None
2. Automatically calls `connect_db()` to establish database connection
3. Sets up required database tables

**Example Usage**:
```python
ems = EmployeeManagementSystem()
```

---

## Method Documentation

### 1. `__init__(self)`

**Purpose**: Constructor that initializes the Employee Management System.

**Parameters**: None

**Returns**: None

**Functionality**:
- Sets `self.connection` to None
- Sets `self.cursor` to None
- Automatically calls `connect_db()` to establish database connection

**Exceptions**: Handled by `connect_db()` method

---

### 2. `connect_db(self)`

**Purpose**: Establishes connection to MySQL database and creates necessary tables.

**Parameters**: None

**Returns**: None

**Functionality**:
- Attempts to connect to MySQL server using provided credentials
- Creates cursor object for query execution
- Displays success message: "✓ Database connected successfully!"
- Calls `create_tables()` to initialize database schema
- Catches and displays any connection errors

**Connection Parameters**:
- Host: 'localhost'
- User: 'root'
- Password: '1234'
- Database: 'mydb'

**Exception Handling**: Catches `Error` exceptions from mysql.connector

**Output**:
- Success: "✓ Database connected successfully!"
- Failure: Displays error message with exception details

---

### 3. `create_tables(self)`

**Purpose**: Creates three essential database tables if they don't exist.

**Parameters**: None

**Returns**: None

**Tables Created**:

#### Table 1: `employees`
Stores employee information with the following columns:
- `emp_id` (INT, AUTO_INCREMENT, PRIMARY KEY) - Unique employee identifier
- `name` (VARCHAR(100), NOT NULL) - Employee full name
- `email` (VARCHAR(100), UNIQUE) - Employee email address (unique constraint)
- `phone` (VARCHAR(15)) - Employee contact number
- `department` (VARCHAR(50)) - Department name
- `salary` (FLOAT) - Basic salary amount
- `position` (VARCHAR(50)) - Job position/title
- `joining_date` (DATE) - Date of joining the organization
- `status` (VARCHAR(20), DEFAULT='Active') - Employment status (Active/Inactive)

#### Table 2: `attendance`
Stores employee attendance records:
- `attendance_id` (INT, AUTO_INCREMENT, PRIMARY KEY) - Unique attendance record identifier
- `emp_id` (INT, FOREIGN KEY) - References employees.emp_id
- `date` (DATE) - Attendance date
- `status` (VARCHAR(20)) - Attendance status (Present/Absent/Leave)

#### Table 3: `salary`
Stores salary processing records:
- `salary_id` (INT, AUTO_INCREMENT, PRIMARY KEY) - Unique salary record identifier
- `emp_id` (INT, FOREIGN KEY) - References employees.emp_id
- `month` (INT) - Month (1-12)
- `year` (INT) - Year of salary processing
- `amount` (FLOAT) - Salary amount paid
- `paid_date` (DATE) - Date of salary payment

**Functionality**:
- Uses CREATE TABLE IF NOT EXISTS to avoid duplicate table errors
- Establishes foreign key relationships between tables
- Commits changes to database after creating all tables

**Exception Handling**: Catches and displays table creation errors

---

### 4. `add_employee(self)`

**Purpose**: Adds a new employee record to the database.

**Parameters**: None (user provides input via prompts)

**Returns**: None

**Input Prompts**:
1. Employee Name (VARCHAR)
2. Email (VARCHAR, must be unique)
3. Phone (VARCHAR)
4. Department (VARCHAR)
5. Salary (FLOAT)
6. Position (VARCHAR)
7. Joining Date (DATE format: YYYY-MM-DD)

**Database Operation**:
- SQL Query: `INSERT INTO employees (name, email, phone, department, salary, position, joining_date) VALUES (%s, %s, %s, %s, %s, %s, %s)`
- Uses parameterized queries to prevent SQL injection

**Output**:
- Success: "✓ Employee added successfully!"
- Failure: Displays error message with exception details

**Exception Handling**: Catches duplicate email errors and other database errors

---

### 5. `view_all_employees(self)`

**Purpose**: Displays all employees in the database with formatted table output.

**Parameters**: None

**Returns**: None

**Database Operation**:
- SQL Query: `SELECT * FROM employees`
- Fetches all employee records

**Display Format**:
- Tabular display with headers: ID | Name | Email | Phone | Department | Salary | Position | Joining Date | Status
- Formatted output with proper alignment and separators
- Shows "No employees found!" if database is empty

**Output Data**:
- Employee ID
- Employee Name
- Email Address
- Phone Number
- Department
- Salary (formatted to 2 decimal places)
- Position
- Joining Date
- Employment Status

**Exception Handling**: Catches database query errors

---

### 6. `search_employee(self)`

**Purpose**: Searches for a specific employee by Employee ID.

**Parameters**: None (user provides Employee ID via input)

**Returns**: None

**Input Prompt**:
- Enter Employee ID (INTEGER)

**Database Operation**:
- SQL Query: `SELECT * FROM employees WHERE emp_id = %s`
- Retrieves single employee record matching the ID

**Display Format**:
- Same tabular format as `view_all_employees()`
- Shows complete employee information
- Displays "Employee not found!" if ID doesn't exist

**Output Data**:
- All employee columns if found
- Not found message if employee doesn't exist

**Exception Handling**: Catches invalid input and database errors

---

### 7. `update_employee(self)`

**Purpose**: Updates specific employee information with multiple update options.

**Parameters**: None (user provides Employee ID and update choice via input)

**Returns**: None

**Input Prompts**:
1. Enter Employee ID (INTEGER)
2. Select update option:
   - Option 1: Update Salary (FLOAT)
   - Option 2: Update Position (VARCHAR)
   - Option 3: Update Department (VARCHAR)
   - Option 4: Update Status (VARCHAR: Active/Inactive)

**Database Operations**:
- **Salary Update**: `UPDATE employees SET salary = %s WHERE emp_id = %s`
- **Position Update**: `UPDATE employees SET position = %s WHERE emp_id = %s`
- **Department Update**: `UPDATE employees SET department = %s WHERE emp_id = %s`
- **Status Update**: `UPDATE employees SET status = %s WHERE emp_id = %s`

**Output**:
- Success: "✓ Employee updated successfully!"
- Failure: Displays error message with exception details

**Exception Handling**: Catches database errors and invalid input

---

### 8. `delete_employee(self)`

**Purpose**: Deletes an employee record from the database with confirmation.

**Parameters**: None (user provides Employee ID and confirmation via input)

**Returns**: None

**Input Prompts**:
1. Enter Employee ID (INTEGER)
2. Confirm deletion (yes/no)

**Database Operation**:
- SQL Query: `DELETE FROM employees WHERE emp_id = %s`
- Executes only if user confirms with "yes"

**Output**:
- Confirmation: "✓ Employee deleted!"
- Cancellation: "Deletion cancelled!"
- Failure: Displays error message with exception details

**Safety Features**:
- Requires explicit "yes" confirmation before deletion
- Prevents accidental data loss

**Exception Handling**: Catches database errors

---

### 9. `mark_attendance(self)`

**Purpose**: Records attendance for an employee on a specific date.

**Parameters**: None (user provides attendance details via input)

**Returns**: None

**Input Prompts**:
1. Enter Employee ID (INTEGER)
2. Enter Date (DATE format: YYYY-MM-DD)
3. Enter Status (VARCHAR: Present/Absent/Leave)

**Database Operation**:
- SQL Query: `INSERT INTO attendance (emp_id, date, status) VALUES (%s, %s, %s)`
- Creates new attendance record

**Output**:
- Success: "✓ Attendance marked!"
- Failure: Displays error message with exception details

**Valid Status Values**:
- Present
- Absent
- Leave
- (Extensible for custom status values)

**Exception Handling**: Catches database errors and invalid employee IDs

---

### 10. `view_attendance(self)`

**Purpose**: Displays attendance records for a specific employee.

**Parameters**: None (user provides Employee ID via input)

**Returns**: None

**Input Prompt**:
- Enter Employee ID (INTEGER)

**Database Operation**:
- SQL Query: `SELECT a.date, a.status, e.name FROM attendance a JOIN employees e ON a.emp_id = e.emp_id WHERE a.emp_id = %s ORDER BY a.date DESC`
- Joins attendance and employees tables
- Sorts records in descending order by date (most recent first)

**Display Format**:
- Tabular display with headers: Date | Status | Employee Name
- Shows records in reverse chronological order

**Output Data**:
- Attendance Date
- Attendance Status
- Employee Name

**Exception Handling**: Catches database errors and invalid employee IDs

---

### 11. `process_salary(self)`

**Purpose**: Processes and records salary payment for an employee.

**Parameters**: None (user provides salary details via input)

**Returns**: None

**Input Prompts**:
1. Enter Employee ID (INTEGER)
2. Enter Month (INTEGER: 1-12)
3. Enter Year (INTEGER)

**Functionality**:
- Retrieves base salary from employees table
- Uses current date as payment date
- Creates salary record with processed amount

**Database Operations**:
1. Query: `SELECT salary FROM employees WHERE emp_id = %s` - Retrieves salary amount
2. Insert: `INSERT INTO salary (emp_id, month, year, amount, paid_date) VALUES (%s, %s, %s, %s, %s)`

**Output**:
- Success: "✓ Salary processed! Amount: {amount}"
- Failure: "Employee not found!" or error message with exception details

**Date Usage**:
- `paid_date` automatically set to current date via `datetime.date.today()`

**Exception Handling**: Catches database errors and invalid employee IDs

---

### 12. `view_salary_records(self)`

**Purpose**: Displays all salary records for a specific employee.

**Parameters**: None (user provides Employee ID via input)

**Returns**: None

**Input Prompt**:
- Enter Employee ID (INTEGER)

**Database Operation**:
- SQL Query: `SELECT s.salary_id, e.name, s.month, s.year, s.amount, s.paid_date FROM salary s JOIN employees e ON s.emp_id = e.emp_id WHERE s.emp_id = %s`
- Joins salary and employees tables
- Retrieves all salary records for the employee

**Display Format**:
- Tabular display with headers: ID | Name | Month | Year | Amount | Paid Date
- Salary amount formatted to 2 decimal places

**Output Data**:
- Salary Record ID
- Employee Name
- Month (1-12)
- Year
- Salary Amount
- Payment Date

**Exception Handling**: Catches database errors and invalid employee IDs

---

### 13. `department_report(self)`

**Purpose**: Generates a statistical report for each department.

**Parameters**: None

**Returns**: None

**Database Operation**:
- SQL Query: `SELECT department, COUNT(*) as count, AVG(salary) as avg_salary FROM employees GROUP BY department`
- Groups employees by department
- Calculates count and average salary per department

**Display Format**:
- Tabular display with headers: Department | Employee Count | Average Salary
- Average salary formatted to 2 decimal places
- Handles NULL values by displaying "N/A"

**Output Data**:
- Department Name
- Number of Employees in Department
- Average Salary in Department

**Exception Handling**: Catches database errors

---

### 14. `main_menu(self)`

**Purpose**: Main interactive menu loop for user interaction with the system.

**Parameters**: None

**Returns**: None

**Functionality**:
- Displays formatted menu with 11 options
- Accepts user choice (1-11)
- Routes to appropriate method based on selection
- Continues looping until user selects exit option

**Menu Options**:
1. **Add Employee** - Calls `add_employee()`
2. **View All Employees** - Calls `view_all_employees()`
3. **Search Employee** - Calls `search_employee()`
4. **Update Employee** - Calls `update_employee()`
5. **Delete Employee** - Calls `delete_employee()`
6. **Mark Attendance** - Calls `mark_attendance()`
7. **View Attendance** - Calls `view_attendance()`
8. **Process Salary** - Calls `process_salary()`
9. **View Salary Records** - Calls `view_salary_records()`
10. **Department Report** - Calls `department_report()`
11. **Exit** - Closes connection and terminates program

**Exit Procedure**:
- Displays: "Thank you for using EMS!"
- Closes cursor connection: `self.cursor.close()`
- Closes database connection: `self.connection.close()`
- Breaks the loop to end program

**Output**:
- "Invalid choice! Try again." - For invalid menu selections

---

## Features

### Employee Management
- ✓ Add new employee with complete information
- ✓ View all employees in tabular format
- ✓ Search employee by ID
- ✓ Update employee details (salary, position, department, status)
- ✓ Delete employee records with confirmation

### Attendance Tracking
- ✓ Mark daily attendance (Present/Absent/Leave)
- ✓ View attendance history per employee
- ✓ Sort attendance by most recent date
- ✓ Join employee data with attendance records

### Salary Management
- ✓ Process salary for employees
- ✓ Track salary by month and year
- ✓ View salary payment history
- ✓ Record payment date automatically

### Reporting
- ✓ Department-wise employee statistics
- ✓ Calculate department average salary
- ✓ Count employees per department

### Data Integrity
- ✓ Unique email constraint to prevent duplicates
- ✓ Foreign key relationships between tables
- ✓ Parameterized queries to prevent SQL injection
- ✓ Transaction commits for data persistence

---

## Usage Guide

### Starting the Application

```python
if __name__ == "__main__":
    ems = EmployeeManagementSystem()
    ems.main_menu()
```

This code:
1. Creates an instance of EmployeeManagementSystem class
2. Initializes database connection
3. Creates necessary tables if they don't exist
4. Displays interactive menu for user operations

### Workflow Example

1. **Run the program**: `python employee.py`
2. **System automatically**:
   - Connects to MySQL database
   - Creates tables if needed
3. **User interaction**:
   - View main menu with 11 options
   - Enter choice (1-11)
   - Follow input prompts
   - View results
   - Return to menu or exit

### Common Operations

**Adding an Employee**:
1. Select option 1
2. Enter: name, email, phone, department, salary, position, joining date
3. Confirmation message displays

**Searching an Employee**:
1. Select option 3
2. Enter employee ID
3. Complete employee details displayed

**Processing Salary**:
1. Select option 8
2. Enter: employee ID, month, year
3. Salary amount automatically fetched and recorded

**Viewing Reports**:
1. Select option 10
2. Department summary displays automatically

---

## Error Handling

### Exception Types

**MySQL-Specific Errors** (`mysql.connector.Error`):
- Database connection failures
- Table creation errors
- Query execution errors
- Constraint violations (e.g., duplicate email)

### Error Messages

All error messages follow the format:
```
Error: {exception_details}
```

### Error Scenarios

1. **Database Connection Failed**:
   - Cause: Wrong credentials or MySQL server not running
   - Message: Specific connection error displayed

2. **Invalid Input**:
   - Cause: User enters non-numeric value when integer expected
   - Message: ValueError caught during int() conversion

3. **Duplicate Email**:
   - Cause: Email already exists in database
   - Message: MySQL constraint violation error

4. **Employee Not Found**:
   - Cause: Searching for non-existent employee ID
   - Message: "Employee not found!" or "No attendance records found!"

5. **Invalid Date Format**:
   - Cause: Date not in YYYY-MM-DD format
   - Message: MySQL date format error

### Recovery

- Most errors are non-fatal and return user to menu
- Program continues running after error
- User can retry operation or select different option
- Only data integrity errors may require data cleanup

---

## Database Schema Diagram

```
EMPLOYEES TABLE
├── emp_id (PK, AI)
├── name
├── email (UNIQUE)
├── phone
├── department
├── salary
├── position
├── joining_date
└── status

ATTENDANCE TABLE                    SALARY TABLE
├── attendance_id (PK, AI)         ├── salary_id (PK, AI)
├── emp_id (FK)─────────────────┬──├── emp_id (FK)─────────────┐
├── date                         │  ├── month                    │
└── status                       │  ├── year                     │
                                 │  ├── amount                   │
                                 │  └── paid_date                │
                                 │                               │
                                 └───────────────────────────────┘
                                 (Foreign Key Relationships)
```

---

## Connection Details Summary

| Parameter | Value | Notes |
|-----------|-------|-------|
| Host | localhost | MySQL server address |
| User | root | MySQL username |
| Password | 1234 | MySQL password (CHANGE IN PRODUCTION) |
| Database | mydb | Database name |
| Charset | UTF-8 | Default encoding |
| Port | 3306 | Default MySQL port |

---

## Security Notes

⚠️ **Important Security Considerations**:
1. **Hardcoded Credentials**: Current code has hardcoded database credentials. Use environment variables in production.
2. **SQL Injection Prevention**: Code uses parameterized queries (good practice).
3. **Password Security**: Database password should be changed from default value.
4. **Access Control**: Implement user authentication for the application.

---

## Performance Considerations

- Indexes recommended on: emp_id, email, department, attendance date
- Consider pagination for large employee datasets in `view_all_employees()`
- Archive old salary records for better query performance
- Regular database backups recommended

---

## Future Enhancements

- User authentication and role-based access
- Export reports to PDF/Excel
- Leave management system
- Performance appraisal module
- Multi-user support
- Web interface using Flask/Django
- Data validation on input
- Batch employee import/export

---

## Troubleshooting

### Issue: "Can't connect to MySQL server"
- **Solution**: Check if MySQL is running, verify host/user/password credentials

### Issue: "Table already exists"
- **Solution**: Safe to ignore, tables are created with IF NOT EXISTS clause

### Issue: "Access denied for user 'root'"
- **Solution**: Verify MySQL password matches the one in code, check user permissions

### Issue: "Column doesn't have a default value"
- **Solution**: Ensure all required fields are provided during insert operations

### Issue: "Duplicate entry for key 'email'"
- **Solution**: Use different email address, check existing employees with same email

---

## Support & Contact

For issues or questions regarding the Employee Management System:
- Review this documentation
- Check error messages displayed by the system
- Verify database configuration
- Ensure all dependencies are properly installed

---

**Documentation Version**: 1.0
**Last Updated**: January 16, 2026
**System Version**: 1.0

