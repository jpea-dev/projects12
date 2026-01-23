# 🎓 School Fee Management System

## Overview
A comprehensive school fee management system built with Python and MySQL. It manages student information, fee assignment, payment processing, and generates reports for educational institutions.

## Features

### 1. **Student Management**
- Register new students with complete profile
- Store student information (Name, Roll Number, Class, Contact)
- Update student details
- Search students by various criteria
- Maintain student admission records
- View student profile

### 2. **Fee Assignment**
- Assign fees to students
- Track total fee amount
- Monitor paid and pending amounts
- Set payment due dates
- Define fee status (Paid, Pending, Partial)
- Fee structure configuration

### 3. **Payment Processing**
- Record fee payments
- Accept partial payments
- Track payment methods
- Maintain payment history
- Generate payment receipts
- Auto-update fee status

### 4. **Payment Tracking**
- View payment records
- Filter by student/date range
- Track payment status
- Generate payment schedules
- Outstanding fee reports

### 5. **Fee Reports**
- Student fee status
- Payment collection report
- Outstanding fee analysis
- Class-wise fee summary
- Month-wise collection
- Student defaulter list

### 6. **Reminders & Management**
- Fine and penalty calculation
- Fee reminder tracking
- Late payment fine
- Discount management
- Concession handling

## Database Schema

### Tables

#### Student Table
```sql
CREATE TABLE student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    class VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(200),
    date_of_admission DATE NOT NULL
)
```

#### Fee Table
```sql
CREATE TABLE fee (
    fee_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    total_fee DECIMAL(10, 2) NOT NULL,
    paid_amount DECIMAL(10, 2) DEFAULT 0,
    pending_amount DECIMAL(10, 2) NOT NULL,
    status ENUM('PAID', 'PENDING', 'PARTIAL') DEFAULT 'PENDING',
    assigned_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student(student_id)
)
```

#### Payment Record Table
```sql
CREATE TABLE payment_record (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    fee_id INT NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    remarks VARCHAR(200),
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (fee_id) REFERENCES fee(fee_id)
)
```

## Main Features in Code

### Key Methods

#### Student Operations
- `add_student()` - Register new student
- `view_all_students()` - List all students
- `search_student()` - Find by ID or roll number
- `update_student()` - Modify student details
- `delete_student()` - Remove record
- `view_student_profile()` - Detailed profile

#### Fee Management
- `assign_fee()` - Assign fee to student
- `view_fees()` - Display fee records
- `update_fee()` - Modify fee amount
- `calculate_fine()` - Calculate late fee

#### Payment Operations
- `record_payment()` - Record fee payment
- `view_payments()` - Display payments
- `generate_receipt()` - Create receipt
- `process_partial_payment()` - Partial payment handling

#### Reports
- `fee_status_report()` - Student fee status
- `payment_report()` - Payment collection
- `outstanding_report()` - Outstanding fees
- `class_report()` - Class-wise summary

## Installation & Setup

```bash
# 1. Install dependencies
pip install mysql-connector-python

# 2. Ensure MySQL is running
# 3. Create database
mysql -u root -p
CREATE DATABASE mydb;

# 4. Run the system
python school_fee_management.py
```

## Usage

```python
from school_fee_management import *

# Initialize database
connection = get_database_connection()
create_tables()

# Add student
add_student()
# Output: Student added successfully! ID: 1001

# Assign fee
assign_fee()

# Record payment
record_payment()

# Generate report
fee_status_report()
```

## Menu Options

```
SCHOOL FEE MANAGEMENT SYSTEM (SFMS)
═══════════════════════════════════════════

1. Student Management
   - Add New Student
   - View All Students
   - Search Student
   - Update Student Details
   - Delete Student Record
   - View Student Profile

2. Fee Management
   - Assign Fee to Student
   - View All Fees
   - Update Fee Amount
   - Calculate Fine
   - Fee Concession
   - Waive Fee

3. Payment Processing
   - Record Payment
   - View Payments
   - Generate Receipt
   - Partial Payment
   - Payment Verification
   - Refund Processing

4. Fee Status & Tracking
   - View Fee Status
   - Track Pending Fees
   - Payment History
   - Payment Schedule
   - Outstanding Analysis

5. Reports
   - Student Fee Status
   - Payment Collection Report
   - Outstanding Fee Report
   - Class-wise Summary
   - Month-wise Collection
   - Defaulter List
   - Fee Analysis

6. Settings
   - Configure Fee Structure
   - Set Fine Percentage
   - Payment Methods
   - System Settings

7. Exit
```

## Sample Data

The system initializes with sample data:
- **Sample Students** from different classes
- **Assigned Fees** for various students
- **Payment Records** showing different scenarios

## Sample Operations

### Add New Student
```
═══════════════════════════════════════════
ADD NEW STUDENT
═══════════════════════════════════════════

Enter student name: Raj Kumar
Enter roll number: 1001
Enter class: 12-A
Enter email: raj@school.com
Enter phone number: 9876543210
Enter address: 123 Main St, City
Enter date of admission (YYYY-MM-DD): 2024-06-15

✓ Student added successfully!
Student ID: 1
Roll Number: 1001
```

### Assign Fee
```
═══════════════════════════════════════════
ASSIGN FEE TO STUDENT
═══════════════════════════════════════════

Enter student ID: 1
Enter total fee amount: 15000
Enter assignment date (YYYY-MM-DD): 2026-01-01

✓ Fee assigned successfully!
Fee ID: 1
Total Fee: ₹15,000
Status: PENDING
```

### Record Payment
```
═══════════════════════════════════════════
RECORD PAYMENT
═══════════════════════════════════════════

Enter student ID: 1
Enter fee ID: 1
Enter payment amount: 10000
Enter payment method: Bank Transfer
Enter remarks: Partial payment

✓ Payment recorded successfully!
Payment ID: 1001
Amount: ₹10,000
Date: 21-01-2026 10:30:45

Previous Fee Status: PENDING (₹15,000)
Updated Fee Status: PARTIAL (₹5,000 pending)
```

### Fee Status Report
```
═══════════════════════════════════════════
STUDENT FEE STATUS REPORT
═══════════════════════════════════════════

Student ID | Name          | Roll# | Class | Status    | Paid    | Pending
──────────────────────────────────────────────────────────────────────────
1          | Raj Kumar     | 1001  | 12-A  | PARTIAL   | 10,000  | 5,000
2          | Priya Singh   | 1002  | 12-A  | PAID      | 15,000  | 0
3          | Amit Patel    | 1003  | 12-B  | PENDING   | 0       | 15,000
4          | Neha Sharma   | 1004  | 12-A  | PAID      | 15,000  | 0
5          | Arjun Kumar   | 1005  | 12-B  | PENDING   | 0       | 15,000

═══════════════════════════════════════════
```

### Payment Receipt
```
═══════════════════════════════════════════
        PAYMENT RECEIPT
═══════════════════════════════════════════

Receipt Number: RCP/2026/001
Receipt Date: 21-01-2026 10:30:45

STUDENT DETAILS:
Name: Raj Kumar
Roll Number: 1001
Class: 12-A
Student ID: 1

PAYMENT DETAILS:
Fee ID: 1
Total Fee Amount: ₹15,000
Previously Paid: ₹0
Current Payment: ₹10,000
────────────────────
Total Paid: ₹10,000
Pending Amount: ₹5,000

Payment Method: Bank Transfer
Remarks: Partial payment

FEE STATUS: PARTIAL

═══════════════════════════════════════════
Thank you for your payment!
═══════════════════════════════════════════
```

### Outstanding Fee Report
```
═══════════════════════════════════════════
OUTSTANDING FEE REPORT
═══════════════════════════════════════════

Total Outstanding: ₹50,000
Number of Students with Pending Fees: 3

Pending Breakdown:
Student ID | Name          | Outstanding | Days Overdue
───────────────────────────────────────────────────────
3          | Amit Patel    | ₹15,000     | 21 days
5          | Arjun Kumar   | ₹15,000     | 15 days
1          | Raj Kumar     | ₹5,000      | 10 days

Total with Late Fine (10%):
Amit Patel: ₹16,500
Arjun Kumar: ₹16,500
Raj Kumar: ₹5,500

═══════════════════════════════════════════
```

### Class-wise Summary
```
═══════════════════════════════════════════
CLASS-WISE FEE SUMMARY
═══════════════════════════════════════════

CLASS 12-A:
Total Students: 3
Total Assigned: ₹45,000
Total Paid: ₹25,000
Total Pending: ₹20,000
Collection Rate: 55.56%

Breakdown:
- Fully Paid: 1 student
- Partially Paid: 1 student
- Pending: 1 student

CLASS 12-B:
Total Students: 2
Total Assigned: ₹30,000
Total Paid: ₹0
Total Pending: ₹30,000
Collection Rate: 0%

Breakdown:
- Fully Paid: 0 students
- Partially Paid: 0 students
- Pending: 2 students

═══════════════════════════════════════════
```

## Technical Details

| Aspect | Details |
|--------|---------|
| Language | Python 3.7+ |
| Database | MySQL |
| Tables | 3 main tables |
| CRUD Operations | Full support |
| Authentication | Database connection |
| Data Validation | Input validation implemented |
| Error Handling | Try-catch mechanism |
| Reports | Multiple reporting options |

## Fee Structure

### Typical Annual Fee
```
Class 11-12: ₹15,000 per year
Payment Plan: Monthly or Quarterly
Late Fee: 10% per month (optional)
Discount: Available for multiple siblings
```

## Fine & Penalty

### Late Payment Fine
```
Days Overdue | Fine Percentage
1-5 days    | 2% per month
6-15 days   | 5% per month
16+ days    | 10% per month
```

## Payment Methods Supported

- Bank Transfer
- Cheque
- Cash
- Online Payment
- Card Payment
- Digital Wallet

## Validation Rules

### Student Data
```
- Name: Alphabetic characters
- Roll Number: Unique
- Class: Valid class name
- Email: Valid email format
- Phone: 10 digits
```

### Fee Data
```
- Total Fee: Positive amount
- Assignment Date: Valid date
- Status: PAID/PENDING/PARTIAL
```

### Payment Data
```
- Amount: Greater than 0, ≤ pending amount
- Payment Date: Current or past date
- Method: Valid payment method
```

## Reports Generated

1. **Student Fee Status** - All student fee information
2. **Payment Collection** - Revenue collection report
3. **Outstanding Fees** - Pending fee analysis
4. **Class-wise Summary** - Class statistics
5. **Month-wise Collection** - Monthly breakdown
6. **Defaulter List** - Students with pending fees
7. **Fee Analysis** - Statistical analysis

## Error Handling

```
Error: Student not found
Solution: Verify student ID or search by roll number

Error: Insufficient payment amount
Solution: Enter amount ≤ pending fee

Error: Invalid fee amount
Solution: Enter positive amount

Error: Database connection failed
Solution: Check MySQL connection
```

## Best Practices

1. **Regular Backups** - Back up database regularly
2. **Payment Verification** - Verify all payments
3. **Record Keeping** - Maintain records for audits
4. **Parent Communication** - Send payment reminders
5. **Transparency** - Clear fee structure

## Troubleshooting

### Database Connection Error
```
Solution:
- Ensure MySQL server is running
- Verify connection parameters
- Check database exists
```

### Fee Not Updating
```
Solution:
- Verify student ID
- Check fee ID
- Ensure amount is correct
```

### Payment Receipt Not Generated
```
Solution:
- Verify payment details
- Check database transaction
- Ensure payment is recorded
```

## Academic Applications

Ideal for learning:
- Educational database design
- Financial management
- SQL operations
- Report generation
- Business logic
- Project submission (Class 11/12)

## Future Enhancements

- Online payment portal
- Email receipts
- Automated SMS reminders
- Parent portal
- Mobile app
- Financial analytics
- Multi-currency support
- Export reports (PDF, Excel)
- Online fee submission
- Scholarship management

## License

Educational use - CBSE Computer Science Curriculum

---

**Last Updated**: January 2026

For queries, refer to the code comments or system documentation.
