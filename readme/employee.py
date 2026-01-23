from mysql.connector import Error
import datetime
import mysql.connector

class EmployeeManagementSystem:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect_db()
    
    def connect_db(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='mydb'
            )
            self.cursor = self.connection..cursor()
            print("✓ Database connected successfully!")
            self.create_tables()
        except Error as e:
            print(f"Error: {e}")
    
    def create_tables(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS employees (
                    emp_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE,
                    phone VARCHAR(15),
                    department VARCHAR(50),
                    salary FLOAT,
                    position VARCHAR(50),
                    joining_date DATE,
                    status VARCHAR(20) DEFAULT 'Active'
                )
            ''')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS attendance (
                    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
                    emp_id INT,
                    date DATE,
                    status VARCHAR(20),
                    FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
                )
            ''')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS salary (
                    salary_id INT AUTO_INCREMENT PRIMARY KEY,
                    emp_id INT,
                    month INT,
                    year INT,
                    amount FLOAT,
                    paid_date DATE,
                    FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
                )
            ''')
            
            self.connection.commit()
        except Error as e:
            print(f"Table creation error: {e}")
    
    def add_employee(self):
        print("\n--- Add New Employee ---")
        try:
            name = input("Enter Employee Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            position = input("Enter Position: ")
            joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
            
            query = '''INSERT INTO employees 
                      (name, email, phone, department, salary, position, joining_date) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            
            self.cursor.execute(query, (name, email, phone, department, salary, position, joining_date))
            self.connection.commit()
            print("✓ Employee added successfully!")
        except Error as e:
            print(f"Error: {e}")
    
    def view_all_employees(self):
        print("\n--- All Employees ---")
        try:
            self.cursor.execute("SELECT * FROM employees")
            employees = self.cursor.fetchall()
            
            if employees:
                headers = ["ID", "Name", "Email", "Phone", "Department", "Salary", "Position", "Joining Date", "Status"]
                print(" | ".join(headers))
                print("-" * 100)
                for emp in employees:
                    emp_id, name, email, phone, department, salary, position, joining_date, status = emp
                    print(f"{emp_id} | {name} | {email or ''} | {phone or ''} | {department or ''} | {salary:.2f} | {position or ''} | {joining_date} | {status}")
            else:
                print("No employees found!")
        except Error as e:
            print(f"Error: {e}")
    
    def search_employee(self):
        print("\n--- Search Employee ---")
        try:
            emp_id = int(input("Enter Employee ID: "))
            self.cursor.execute("SELECT * FROM employees WHERE emp_id = %s", (emp_id,))
            employee = self.cursor.fetchone()
            
            if employee:
                headers = ["ID", "Name", "Email", "Phone", "Department", "Salary", "Position", "Joining Date", "Status"]
                print(" | ".join(headers))
                print("-" * 100)
                emp_id, name, email, phone, department, salary, position, joining_date, status = employee
                print(f"{emp_id} | {name} | {email or ''} | {phone or ''} | {department or ''} | {salary:.2f} | {position or ''} | {joining_date} | {status}")
            else:
                print("Employee not found!")
        except Error as e:
            print(f"Error: {e}")
    
    def update_employee(self):
        print("\n--- Update Employee ---")
        try:
            emp_id = int(input("Enter Employee ID: "))
            print("1. Update Salary")
            print("2. Update Position")
            print("3. Update Department")
            print("4. Update Status")
            choice = input("Select option: ")
            
            if choice == "1":
                salary = float(input("Enter new salary: "))
                self.cursor.execute("UPDATE employees SET salary = %s WHERE emp_id = %s", (salary, emp_id))
            elif choice == "2":
                position = input("Enter new position: ")
                self.cursor.execute("UPDATE employees SET position = %s WHERE emp_id = %s", (position, emp_id))
            elif choice == "3":
                department = input("Enter new department: ")
                self.cursor.execute("UPDATE employees SET department = %s WHERE emp_id = %s", (department, emp_id))
            elif choice == "4":
                status = input("Enter status (Active/Inactive): ")
                self.cursor.execute("UPDATE employees SET status = %s WHERE emp_id = %s", (status, emp_id))
            
            self.connection.commit()
            print("✓ Employee updated successfully!")
        except Error as e:
            print(f"Error: {e}")
    
    def delete_employee(self):
        print("\n--- Delete Employee ---")
        try:
            emp_id = int(input("Enter Employee ID: "))
            confirm = input("Are you sure? (yes/no): ")
            
            if confirm.lower() == "yes":
                self.cursor.execute("DELETE FROM employees WHERE emp_id = %s", (emp_id,))
                self.connection.commit()
                print("✓ Employee deleted!")
            else:
                print("Deletion cancelled!")
        except Error as e:
            print(f"Error: {e}")
    
    def mark_attendance(self):
        print("\n--- Mark Attendance ---")
        try:
            emp_id = int(input("Enter Employee ID: "))
            date = input("Enter Date (YYYY-MM-DD): ")
            status = input("Enter Status (Present/Absent/Leave): ")
            
            query = "INSERT INTO attendance (emp_id, date, status) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (emp_id, date, status))
            self.connection.commit()
            print("✓ Attendance marked!")
        except Error as e:
            print(f"Error: {e}")
    
    def view_attendance(self):
        print("\n--- View Attendance ---")
        try:
            emp_id = int(input("Enter Employee ID: "))
            self.cursor.execute('''SELECT a.date, a.status, e.name 
                                  FROM attendance a 
                                  JOIN employees e ON a.emp_id = e.emp_id 
                                  WHERE a.emp_id = %s ORDER BY a.date DESC''', (emp_id,))
            records = self.cursor.fetchall()
            
            if records:
                headers = ["Date", "Status", "Employee Name"]
                print(" | ".join(headers))
                print("-" * 60)
                for date, status, name in records:
                    print(f"{date} | {status} | {name}")
            else:
                print("No attendance records found!")
        except Error as e:
            print(f"Error: {e}")
    
    def process_salary(self):
        print("\n--- Process Salary ---")
        try:
            emp_id = int(input("Enter Employee ID: "))
            month = int(input("Enter Month (1-12): "))
            year = int(input("Enter Year: "))
            
            self.cursor.execute("SELECT salary FROM employees WHERE emp_id = %s", (emp_id,))
            result = self.cursor.fetchone()
            
            if result:
                amount = result[0]
                paid_date = datetime.date.today()
                query = "INSERT INTO salary (emp_id, month, year, amount, paid_date) VALUES (%s, %s, %s, %s, %s)"
                self.cursor.execute(query, (emp_id, month, year, amount, paid_date))
                self.connection.commit()
                print(f"✓ Salary processed! Amount: {amount}")
            else:
                print("Employee not found!")
        except Error as e:
            print(f"Error: {e}")
    
    def view_salary_records(self):
        print("\n--- Salary Records ---")
        try:
            emp_id = int(input("Enter Employee ID: "))
            self.cursor.execute('''SELECT s.salary_id, e.name, s.month, s.year, s.amount, s.paid_date 
                                  FROM salary s 
                                  JOIN employees e ON s.emp_id = e.emp_id 
                                  WHERE s.emp_id = %s''', (emp_id,))
            records = self.cursor.fetchall()
            
            if records:
                headers = ["ID", "Name", "Month", "Year", "Amount", "Paid Date"]
                print(" | ".join(headers))
                print("-" * 80)
                for salary_id, name, month, year, amount, paid_date in records:
                    print(f"{salary_id} | {name} | {month} | {year} | {amount:.2f} | {paid_date}")
            else:
                print("No salary records found!")
        except Error as e:
            print(f"Error: {e}")
    
    def department_report(self):
        print("\n--- Department Report ---")
        try:
            self.cursor.execute('''SELECT department, COUNT(*) as count, AVG(salary) as avg_salary 
                                  FROM employees 
                                  GROUP BY department''')
            records = self.cursor.fetchall()
            
            if records:
                headers = ["Department", "Employee Count", "Average Salary"]
                print(" | ".join(headers))
                print("-" * 60)
                for dept, count, avg_salary in records:
                    avg_str = f"{avg_salary:.2f}" if avg_salary is not None else "0.00"
                    print(f"{dept or 'N/A'} | {count} | {avg_str}")
            else:
                print("No data found!")
        except Error as e:
            print(f"Error: {e}")
    
    def main_menu(self):
        while True:
            print("\n" + "="*50)
            print("   EMPLOYEE MANAGEMENT SYSTEM")
            print("="*50)
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Mark Attendance")
            print("7. View Attendance")
            print("8. Process Salary")
            print("9. View Salary Records")
            print("10. Department Report")
            print("11. Exit")
            print("="*50)
            
            choice = input("Enter your choice (1-11): ")
            
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                self.mark_attendance()
            elif choice == "7":
                self.view_attendance()
            elif choice == "8":
                self.process_salary()
            elif choice == "9":
                self.view_salary_records()
            elif choice == "10":
                self.department_report()
            elif choice == "11":
                print("Thank you for using EMS!")
                self.cursor.close()
                self.connection.close()
                break
            else:
                print("Invalid choice! Try again.")

if __name__ == "__main__":
    ems = EmployeeManagementSystem()
    ems.main_menu()