# 💼 Employee Payroll System

## Overview
A comprehensive employee payroll management system built with Python using CSV data storage. It provides complete functionality for employee management, salary structure configuration, and payroll processing.

## Features

### 1. **Employee Management**
- Add new employees with personal details
- Store employee information (ID, Name, Designation, Department)
- Update employee details
- Delete employee records
- Search employees by ID or name
- View all employees

### 2. **Salary Management**
- Configure salary structure for each employee
- Basic salary assignment
- HRA (House Rent Allowance) calculation
- DA (Dearness Allowance) calculation
- PF (Provident Fund) deduction
- Gross salary calculation
- Net salary calculation

### 3. **Payroll Processing**
- Generate payslips for employees
- Calculate monthly salary
- Deduct PF and other deductions
- Calculate net salary
- Generate salary reports

### 4. **Leave Management**
- Record employee leaves
- Track leave balance
- Calculate leave deductions
- Adjust salary based on leaves

### 5. **Reports & Analysis**
- Salary reports by department
- Employee salary summary
- Monthly payroll report
- Deduction summary
- Department-wise analysis

## Data Storage Structure

### CSV Files

#### employees.csv
```
ID,Name,Designation,Department
1001,John Doe,Manager,Sales
1002,Jane Smith,Executive,HR
1003,Bob Wilson,Developer,IT
```

#### salaries.csv
```
ID,BasicSalary,HRA,DA,PF,GrossSalary,NetSalary
1001,50000,15000,5000,5000,70000,65000
1002,40000,12000,4000,4000,56000,52000
1003,45000,13500,4500,4500,63000,58500
```

## Main Features in Code

### Key Methods

#### Employee Operations
- `add_employee()` - Register new employee
- `view_all_employees()` - List all employees
- `search_employee()` - Find by ID or name
- `update_employee()` - Modify details
- `delete_employee()` - Remove record

#### Salary Management
- `add_salary()` - Set salary structure
- `view_salary()` - Display salary details
- `update_salary()` - Modify salary components
- `calculate_salary()` - Compute net salary

#### Payroll Processing
- `generate_payslip()` - Create salary slip
- `process_payroll()` - Monthly processing
- `view_payroll()` - Display payroll data

#### Reports
- `department_report()` - By department analysis
- `salary_report()` - Salary summary
- `monthly_report()` - Monthly payroll

## Installation & Setup

```bash
# 1. No external database required - uses CSV files
# 2. Python 3.7+ required
# 3. Run the system
python employee_payroll_system.py
```

## Usage

```python
from employee_payroll_system import *

# Initialize CSV files
initialize_files()

# Add new employee
add_employee()
# Output: Employee added successfully! ID: 1001

# Add salary information
add_salary()

# Generate payslip
generate_payslip()

# View reports
department_report()
salary_report()
```

## Menu Options

```
EMPLOYEE PAYROLL SYSTEM
══════════════════════════════════════

1. Employee Management
   - Add New Employee
   - View All Employees
   - Search Employee
   - Update Employee
   - Delete Employee

2. Salary Management
   - Add Salary
   - View Salary
   - Update Salary
   - Calculate Salary

3. Payroll Processing
   - Generate Payslip
   - Process Monthly Payroll
   - View Payroll

4. Leave Management
   - Record Leave
   - View Leave Balance
   - Calculate Leave Deductions

5. Reports
   - Employee Report
   - Salary Report
   - Department-wise Report
   - Monthly Payroll Report
   - Deduction Summary

6. Exit
```

## Salary Calculation Formula

```
Gross Salary = Basic Salary + HRA + DA

Deductions:
- PF (Provident Fund): Usually 12% or fixed amount
- IT (Income Tax): If applicable
- Other deductions

Net Salary = Gross Salary - Total Deductions
```

### Example Calculation

```
Employee: John Doe
Basic Salary:        ₹50,000.00
HRA (30%):          ₹15,000.00
DA (10%):           ₹5,000.00
─────────────────────────────
Gross Salary:       ₹70,000.00

Less Deductions:
PF (12%):           ₹8,400.00
─────────────────────────────
Net Salary:         ₹61,600.00
```

## Sample Operations

### Add New Employee
```
═══════════════════════════════════════
ADD NEW EMPLOYEE
═══════════════════════════════════════

Enter employee name: John Doe
Enter designation: Senior Manager
Enter department: Sales

✓ Employee added successfully!
Employee ID: 1001
```

### Add Salary Information
```
═══════════════════════════════════════
ADD SALARY INFORMATION
═══════════════════════════════════════

Enter Employee ID: 1001
Enter Basic Salary: 50000
Enter HRA: 15000
Enter DA: 5000
Enter PF: 5000

✓ Salary added successfully!
```

### Generate Payslip
```
═══════════════════════════════════════
EMPLOYEE PAYSLIP
═══════════════════════════════════════

Employee ID: 1001
Employee Name: John Doe
Designation: Senior Manager
Department: Sales
Month: January 2026

EARNINGS:
Basic Salary:        ₹50,000.00
HRA:                 ₹15,000.00
DA:                  ₹5,000.00
───────────────────────────────────
Gross Salary:        ₹70,000.00

DEDUCTIONS:
Provident Fund (PF): ₹8,400.00
───────────────────────────────────
Net Salary:          ₹61,600.00

Payslip Generated: 21-01-2026
═══════════════════════════════════════
```

### Department Report
```
═══════════════════════════════════════
DEPARTMENT-WISE SALARY REPORT
═══════════════════════════════════════

Department: Sales
─────────────────────────────────────
Employee ID | Name        | Basic    | Net Salary
1001        | John Doe    | 50000    | 61600
1005        | Mike Brown  | 45000    | 55200

Total Department Salary: ₹116,800.00
Employee Count: 2

Department: IT
─────────────────────────────────────
Employee ID | Name        | Basic    | Net Salary
1003        | Bob Wilson  | 45000    | 55200
1004        | Alice Green | 48000    | 58800

Total Department Salary: ₹114,000.00
Employee Count: 2

═══════════════════════════════════════
```

### Salary Summary Report
```
═══════════════════════════════════════
SALARY SUMMARY REPORT
═══════════════════════════════════════

Total Employees: 4
Total Gross Salary: ₹280,000.00
Total Net Salary: ₹230,800.00
Total Deductions: ₹49,200.00

Average Basic Salary: ₹47,000.00
Average Net Salary: ₹57,700.00

Highest Salary: ₹70,000.00 (John Doe)
Lowest Salary: ₹55,000.00 (Mike Brown)

═══════════════════════════════════════
```

## Technical Details

| Aspect | Details |
|--------|---------|
| Language | Python 3.7+ |
| Storage | CSV Files |
| Tables | 2 (employees.csv, salaries.csv) |
| CRUD Operations | Full support |
| Data Validation | Input validation implemented |
| Error Handling | Try-catch mechanism |
| File Format | CSV (comma-separated values) |

## Salary Component Details

### Basic Salary
- Fixed monthly salary
- Foundation for calculations
- Determined by designation and experience

### HRA (House Rent Allowance)
- Typically 30-50% of basic salary
- Tax benefit applicable
- Varies by city/location

### DA (Dearness Allowance)
- Typically 10-50% of basic salary
- Adjusted for inflation
- Determined by government/company policy

### PF (Provident Fund)
- Employee contribution (typically 12%)
- Retirement benefits
- Employer also contributes

## Data Validation

```python
# Employee ID validation
- Must be 4-digit number
- Auto-generated if not provided

# Salary amount validation
- Must be positive numbers
- No negative values allowed
- Maximum limit checks

# Designation validation
- From predefined list
- Case-insensitive

# Department validation
- From predefined list
- Valid department codes
```

## File Operations

### CSV File Handling
- Auto-creation if missing
- Header row included
- Comma-separated format
- UTF-8 encoding

### Data Persistence
- Automatic save on changes
- File backup on modification
- Data consistency checks

## Error Handling

```
Error: Employee not found
Solution: Check employee ID or search by name

Error: Salary not configured
Solution: Add salary details before generating payslip

Error: File not found
Solution: Initialize files first

Error: Invalid input
Solution: Enter correct data type
```

## Reports Generated

1. **Employee Report** - All employee details
2. **Salary Report** - Salary structure and breakdown
3. **Department Report** - Department-wise analysis
4. **Monthly Payroll** - Monthly processing summary
5. **Deduction Summary** - All deductions total
6. **Leave Report** - Leave and adjustments

## Best Practices

1. **Data Accuracy** - Verify employee data before processing
2. **Regular Updates** - Update salary on promotion
3. **Leave Records** - Maintain accurate leave records
4. **Backup Files** - Keep CSV backups
5. **Confidentiality** - Keep salary information confidential

## Troubleshooting

### CSV File Not Found
```
Solution:
- Run initialize_files() first
- Check file permissions
- Verify file path
```

### Employee Not Found
```
Solution:
- Check employee ID
- Use search function
- Verify spelling
```

### Salary Calculation Error
```
Solution:
- Verify all salary components entered
- Check for negative values
- Ensure salary is added before processing
```

## Academic Applications

Ideal for learning:
- File handling in Python
- CSV operations
- Data structures
- Salary calculations
- Business logic
- Project submission (Class 11/12)

## Future Enhancements

- Database migration (MySQL)
- Advanced reporting
- Attendance integration
- Leave management module
- Performance ratings
- Bonus calculations
- Payroll automation
- Web interface

## License

Educational use - CBSE Computer Science Curriculum

---

**Last Updated**: January 2026

For queries, refer to the code comments or system documentation.
