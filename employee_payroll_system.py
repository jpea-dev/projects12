"""
Employee Payroll System
A menu-driven console application for managing employee records and calculating payroll
"""

import csv
import os

EMPLOYEES_FILE = "employees.csv"
SALARIES_FILE = "salaries.csv"


def initialize_files():
    """Initialize CSV files if they don't exist"""
    if not os.path.exists(EMPLOYEES_FILE):
        with open(EMPLOYEES_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Designation', 'Department'])
    
    if not os.path.exists(SALARIES_FILE):
        with open(SALARIES_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'BasicSalary', 'HRA', 'DA', 'PF', 'GrossSalary', 'NetSalary'])


def load_employees():
    """Load all employees from CSV file"""
    employees = []
    try:
        with open(EMPLOYEES_FILE, 'r') as f:
            reader = csv.DictReader(f)
            employees = list(reader)
    except FileNotFoundError:
        pass
    return employees


def save_employees(employees):
    """Save employees to CSV file"""
    try:
        with open(EMPLOYEES_FILE, 'w', newline='') as f:
            if employees:
                fieldnames = ['ID', 'Name', 'Designation', 'Department']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(employees)
        return True
    except Exception as e:
        print(f"Error saving employees: {e}")
        return False


def load_salaries():
    """Load all salary records from CSV file"""
    salaries = []
    try:
        with open(SALARIES_FILE, 'r') as f:
            reader = csv.DictReader(f)
            salaries = list(reader)
    except FileNotFoundError:
        pass
    return salaries


def save_salaries(salaries):
    """Save salary records to CSV file"""
    try:
        with open(SALARIES_FILE, 'w', newline='') as f:
            if salaries:
                fieldnames = ['ID', 'BasicSalary', 'HRA', 'DA', 'PF', 'GrossSalary', 'NetSalary']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(salaries)
        return True
    except Exception as e:
        print(f"Error saving salaries: {e}")
        return False


def get_next_employee_id():
    """Get the next available employee ID"""
    employees = load_employees()
    if not employees:
        return "1001"
    ids = [int(emp['ID']) for emp in employees]
    return str(max(ids) + 1)


def add_employee():
    """Add a new employee to the system"""
    print("\n" + "="*50)
    print("ADD NEW EMPLOYEE")
    print("="*50)
    
    try:
        employees = load_employees()
        
        emp_id = get_next_employee_id()
        
        name = input("Enter employee name: ").strip()
        if not name:
            print("Error: Name cannot be empty!")
            return
        
        designation = input("Enter designation (e.g., Manager, Developer): ").strip()
        if not designation:
            print("Error: Designation cannot be empty!")
            return
        
        department = input("Enter department (e.g., IT, HR, Sales): ").strip()
        if not department:
            print("Error: Department cannot be empty!")
            return
        
        new_employee = {
            'ID': emp_id,
            'Name': name,
            'Designation': designation,
            'Department': department
        }
        
        employees.append(new_employee)
        
        if save_employees(employees):
            print("\nSuccess: Employee added successfully!")
            print(f"Employee ID: {emp_id}")
        else:
            print("Error: Failed to save employee!")
    
    except Exception as e:
        print(f"Error: {e}")


def view_employee():
    """View employee details by ID"""
    print("\n" + "="*50)
    print("VIEW EMPLOYEE DETAILS")
    print("="*50)
    
    try:
        emp_id = input("Enter employee ID: ").strip()
        if not emp_id:
            print("Error: Employee ID cannot be empty!")
            return
        
        employees = load_employees()
        found = False
        
        for emp in employees:
            if emp['ID'] == emp_id:
                print("\n" + "-"*50)
                print("Employee Information:")
                print("-"*50)
                print(f"ID: {emp['ID']}")
                print(f"Name: {emp['Name']}")
                print(f"Designation: {emp['Designation']}")
                print(f"Department: {emp['Department']}")
                print("-"*50)
                found = True
                break
        
        if not found:
            print("Error: Employee not found!")
    
    except Exception as e:
        print(f"Error: {e}")


def update_employee():
    """Update employee information"""
    print("\n" + "="*50)
    print("UPDATE EMPLOYEE INFORMATION")
    print("="*50)
    
    try:
        emp_id = input("Enter employee ID to update: ").strip()
        if not emp_id:
            print("Error: Employee ID cannot be empty!")
            return
        
        employees = load_employees()
        found = False
        
        for emp in employees:
            if emp['ID'] == emp_id:
                print("\nCurrent Information:")
                print(f"Name: {emp['Name']}")
                print(f"Designation: {emp['Designation']}")
                print(f"Department: {emp['Department']}")
                
                print("\nEnter new information (press Enter to skip):")
                
                new_name = input("New name: ").strip()
                if new_name:
                    emp['Name'] = new_name
                
                new_desig = input("New designation: ").strip()
                if new_desig:
                    emp['Designation'] = new_desig
                
                new_dept = input("New department: ").strip()
                if new_dept:
                    emp['Department'] = new_dept
                
                if save_employees(employees):
                    print("\nSuccess: Employee information updated!")
                else:
                    print("Error: Failed to update employee!")
                
                found = True
                break
        
        if not found:
            print("Error: Employee not found!")
    
    except Exception as e:
        print(f"Error: {e}")


def delete_employee():
    """Delete an employee record"""
    print("\n" + "="*50)
    print("DELETE EMPLOYEE RECORD")
    print("="*50)
    
    try:
        emp_id = input("Enter employee ID to delete: ").strip()
        if not emp_id:
            print("Error: Employee ID cannot be empty!")
            return
        
        confirm = input("Are you sure? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Deletion cancelled!")
            return
        
        employees = load_employees()
        salaries = load_salaries()
        initial_count = len(employees)
        
        employees = [emp for emp in employees if emp['ID'] != emp_id]
        salaries = [sal for sal in salaries if sal['ID'] != emp_id]
        
        if len(employees) < initial_count:
            save_employees(employees)
            save_salaries(salaries)
            print("\nSuccess: Employee record deleted!")
        else:
            print("Error: Employee not found!")
    
    except Exception as e:
        print(f"Error: {e}")


def enter_salary():
    """Enter basic salary for an employee"""
    print("\n" + "="*50)
    print("ENTER SALARY INFORMATION")
    print("="*50)
    
    try:
        emp_id = input("Enter employee ID: ").strip()
        if not emp_id:
            print("Error: Employee ID cannot be empty!")
            return
        
        employees = load_employees()
        emp_found = False
        
        for emp in employees:
            if emp['ID'] == emp_id:
                emp_found = True
                emp_name = emp['Name']
                break
        
        if not emp_found:
            print("Error: Employee not found!")
            return
        
        try:
            basic_salary = float(input("Enter basic salary: ").strip())
            if basic_salary < 0:
                print("Error: Salary cannot be negative!")
                return
        except ValueError:
            print("Error: Please enter a valid number!")
            return
        
        hra = calculate_hra(basic_salary)
        da = calculate_da(basic_salary)
        pf = calculate_pf(basic_salary)
        gross_salary = basic_salary + hra + da - pf
        net_salary = gross_salary
        
        salaries = load_salaries()
        salary_found = False
        
        for sal in salaries:
            if sal['ID'] == emp_id:
                sal['BasicSalary'] = str(basic_salary)
                sal['HRA'] = str(hra)
                sal['DA'] = str(da)
                sal['PF'] = str(pf)
                sal['GrossSalary'] = str(gross_salary)
                sal['NetSalary'] = str(net_salary)
                salary_found = True
                break
        
        if not salary_found:
            salaries.append({
                'ID': emp_id,
                'BasicSalary': str(basic_salary),
                'HRA': str(hra),
                'DA': str(da),
                'PF': str(pf),
                'GrossSalary': str(gross_salary),
                'NetSalary': str(net_salary)
            })
        
        if save_salaries(salaries):
            print("\nSuccess: Salary information saved!")
            print(f"Employee: {emp_name}")
            print(f"Basic Salary: Rs. {basic_salary:.2f}")
            print(f"HRA: Rs. {hra:.2f}")
            print(f"DA: Rs. {da:.2f}")
            print(f"PF: Rs. {pf:.2f}")
            print(f"Gross Salary: Rs. {gross_salary:.2f}")
            print(f"Net Salary: Rs. {net_salary:.2f}")
        else:
            print("Error: Failed to save salary!")
    
    except Exception as e:
        print(f"Error: {e}")


def calculate_hra(basic_salary):
    """Calculate HRA (10% of basic salary)"""
    return basic_salary * 0.10


def calculate_da(basic_salary):
    """Calculate DA (5% of basic salary)"""
    return basic_salary * 0.05


def calculate_pf(basic_salary):
    """Calculate PF (12% of basic salary)"""
    return basic_salary * 0.12


def generate_salary_slip():
    """Generate salary slip for an employee"""
    print("\n" + "="*50)
    print("GENERATE SALARY SLIP")
    print("="*50)
    
    try:
        emp_id = input("Enter employee ID: ").strip()
        if not emp_id:
            print("Error: Employee ID cannot be empty!")
            return
        
        employees = load_employees()
        emp_found = False
        emp_name = ""
        emp_desig = ""
        emp_dept = ""
        
        for emp in employees:
            if emp['ID'] == emp_id:
                emp_found = True
                emp_name = emp['Name']
                emp_desig = emp['Designation']
                emp_dept = emp['Department']
                break
        
        if not emp_found:
            print("Error: Employee not found!")
            return
        
        salaries = load_salaries()
        salary_found = False
        
        for sal in salaries:
            if sal['ID'] == emp_id:
                salary_found = True
                
                print("\n" + "="*60)
                print(" "*15 + "SALARY SLIP")
                print("="*60)
                print(f"Employee ID: {emp_id:15} Name: {emp_name}")
                print(f"Designation: {emp_desig:15} Department: {emp_dept}")
                print("-"*60)
                print("EARNINGS:")
                print(f"  Basic Salary:          Rs. {float(sal['BasicSalary']):>10.2f}")
                print(f"  HRA (10%):             Rs. {float(sal['HRA']):>10.2f}")
                print(f"  DA (5%):               Rs. {float(sal['DA']):>10.2f}")
                print("-"*60)
                print(f"  Gross Salary:          Rs. {float(sal['GrossSalary']):>10.2f}")
                print("-"*60)
                print("DEDUCTIONS:")
                print(f"  PF (12%):              Rs. {float(sal['PF']):>10.2f}")
                print("-"*60)
                print(f"  Net Salary:            Rs. {float(sal['NetSalary']):>10.2f}")
                print("="*60)
                break
        
        if not salary_found:
            print("Error: Salary information not found for this employee!")
    
    except Exception as e:
        print(f"Error: {e}")


def view_all_employees():
    """View all employees in the system"""
    print("\n" + "="*50)
    print("ALL EMPLOYEES")
    print("="*50)
    
    try:
        employees = load_employees()
        
        if not employees:
            print("No employees found in the system!")
            return
        
        print(f"\n{'ID':<10} {'Name':<20} {'Designation':<15} {'Department':<15}")
        print("-"*60)
        
        for emp in employees:
            print(f"{emp['ID']:<10} {emp['Name']:<20} {emp['Designation']:<15} {emp['Department']:<15}")
        
        print("-"*60)
        print(f"Total Employees: {len(employees)}")
    
    except Exception as e:
        print(f"Error: {e}")


def view_payroll_summary():
    """View payroll summary for all employees"""
    print("\n" + "="*50)
    print("PAYROLL SUMMARY")
    print("="*50)
    
    try:
        employees = load_employees()
        salaries = load_salaries()
        
        if not employees:
            print("No employees found in the system!")
            return
        
        if not salaries:
            print("No salary information found!")
            return
        
        print(f"\n{'ID':<10} {'Name':<20} {'Basic':<12} {'Gross':<12} {'Net':<12}")
        print("-"*70)
        
        for emp in employees:
            for sal in salaries:
                if emp['ID'] == sal['ID']:
                    basic = float(sal['BasicSalary'])
                    gross = float(sal['GrossSalary'])
                    net = float(sal['NetSalary'])
                    print(f"{emp['ID']:<10} {emp['Name']:<20} Rs.{basic:<10.2f} Rs.{gross:<10.2f} Rs.{net:<10.2f}")
        
        print("-"*70)
    
    except Exception as e:
        print(f"Error: {e}")


def view_total_expenditure():
    """View total salary expenditure"""
    print("\n" + "="*50)
    print("TOTAL SALARY EXPENDITURE")
    print("="*50)
    
    try:
        salaries = load_salaries()
        employees = load_employees()
        
        if not salaries:
            print("No salary information found!")
            return
        
        total_basic = 0
        total_hra = 0
        total_da = 0
        total_pf = 0
        total_gross = 0
        total_net = 0
        
        for sal in salaries:
            total_basic += float(sal['BasicSalary'])
            total_hra += float(sal['HRA'])
            total_da += float(sal['DA'])
            total_pf += float(sal['PF'])
            total_gross += float(sal['GrossSalary'])
            total_net += float(sal['NetSalary'])
        
        print("\n" + "-"*50)
        print("TOTAL EARNINGS:")
        print(f"  Total Basic Salary:    Rs. {total_basic:>10.2f}")
        print(f"  Total HRA:             Rs. {total_hra:>10.2f}")
        print(f"  Total DA:              Rs. {total_da:>10.2f}")
        print("-"*50)
        print(f"  Total Gross Salary:    Rs. {total_gross:>10.2f}")
        print("-"*50)
        print("TOTAL DEDUCTIONS:")
        print(f"  Total PF:              Rs. {total_pf:>10.2f}")
        print("-"*50)
        print(f"  Total Net Salary:      Rs. {total_net:>10.2f}")
        print("-"*50)
        print(f"  Number of Employees:   {len(salaries)}")
        print("-"*50)
    
    except Exception as e:
        print(f"Error: {e}")


def display_main_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("EMPLOYEE PAYROLL SYSTEM")
    print("="*50)
    print("\n1. EMPLOYEE MANAGEMENT")
    print("   1.1 Add New Employee")
    print("   1.2 View Employee Details")
    print("   1.3 Update Employee Information")
    print("   1.4 Delete Employee Record")
    print("\n2. PAYROLL MANAGEMENT")
    print("   2.1 Enter Salary Information")
    print("\n3. SALARY SLIP")
    print("   3.1 Generate Salary Slip")
    print("\n4. REPORTS")
    print("   4.1 View All Employees")
    print("   4.2 View Payroll Summary")
    print("   4.3 View Total Salary Expenditure")
    print("\n5. Exit")
    print("="*50)


def main_menu():
    """Main menu loop"""
    while True:
        display_main_menu()
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1.1":
            add_employee()
        elif choice == "1.2":
            view_employee()
        elif choice == "1.3":
            update_employee()
        elif choice == "1.4":
            delete_employee()
        elif choice == "2.1":
            enter_salary()
        elif choice == "3.1":
            generate_salary_slip()
        elif choice == "4.1":
            view_all_employees()
        elif choice == "4.2":
            view_payroll_summary()
        elif choice == "4.3":
            view_total_expenditure()
        elif choice == "5":
            print("\nThank you for using Employee Payroll System!")
            print("Program terminated successfully.")
            break
        else:
            print("Error: Invalid choice! Please try again.")


def main():
    """Main program entry point"""
    initialize_files()
    main_menu()


if __name__ == "__main__":
    main()
