"""
================================================================================
            SCHOOL FEE MANAGEMENT SYSTEM (SFMS)
                    Class 11/12 Practical Project
================================================================================
This program manages student information, fee assignment, payment processing,
and generates various reports. It uses MySQL database for data persistence.

Author: Computer Science Practical
Date: January 2026
================================================================================
"""

import mysql.connector
from mysql.connector import Error
from datetime import datetime
import time

# ============================================================================
# DATABASE CONNECTION CONFIGURATION
# ============================================================================

def get_database_connection():
    """
    Establish connection to MySQL database.
    Returns database connection object or None if connection fails.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='mydb'
        )
        return connection
    except Error as e:
        print(f"\n❌ DATABASE CONNECTION ERROR: {e}")
        return None


def create_tables():
    """
    Create required tables in the database if they don't exist.
    Tables: student, fee, payment_record
    """
    try:
        connection = get_database_connection()
        if connection is None:
            print("\n❌ Cannot create tables - Database connection failed!")
            return False
        
        cursor = connection.cursor()
        
        # Create Student table
        student_table = """
        CREATE TABLE IF NOT EXISTS student (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            roll_number VARCHAR(20) UNIQUE NOT NULL,
            class VARCHAR(20) NOT NULL,
            email VARCHAR(100),
            phone VARCHAR(15),
            address VARCHAR(200),
            date_of_admission DATE NOT NULL
        )
        """
        
        # Create Fee table
        fee_table = """
        CREATE TABLE IF NOT EXISTS fee (
            fee_id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            total_fee DECIMAL(10, 2) NOT NULL,
            paid_amount DECIMAL(10, 2) DEFAULT 0,
            pending_amount DECIMAL(10, 2) NOT NULL,
            status ENUM('PAID', 'PENDING', 'PARTIAL') DEFAULT 'PENDING',
            assigned_date DATE NOT NULL,
            FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE
        )
        """
        
        # Create Payment Record table
        payment_table = """
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
        )
        """
        
        cursor.execute(student_table)
        cursor.execute(fee_table)
        cursor.execute(payment_table)
        connection.commit()
        print("\n✓ Tables created successfully!")
        cursor.close()
        connection.close()
        return True
        
    except Error as e:
        print(f"\n❌ ERROR creating tables: {e}")
        return False


# ============================================================================
# STUDENT MANAGEMENT MODULE
# ============================================================================

def add_student():
    """
    Add a new student to the system.
    Accepts: Name, Roll Number, Class, Email, Phone, Address
    """
    try:
        print("\n" + "="*60)
        print("ADD NEW STUDENT")
        print("="*60)
        
        name = input("Enter Student Name: ").strip()
        if not name or len(name) < 2:
            print("❌ Invalid name! Name must be at least 2 characters.")
            return
        
        roll_number = input("Enter Roll Number (unique): ").strip()
        if not roll_number:
            print("❌ Roll number cannot be empty!")
            return
        
        class_name = input("Enter Class (e.g., 11-A): ").strip()
        if not class_name:
            print("❌ Class cannot be empty!")
            return
        
        email = input("Enter Email: ").strip()
        if email and '@' not in email:
            print("❌ Invalid email format!")
            return
        
        phone = input("Enter Phone Number: ").strip()
        if phone and not phone.isdigit():
            print("❌ Phone number must contain only digits!")
            return
        
        address = input("Enter Address: ").strip()
        
        connection = get_database_connection()
        if connection is None:
            print("❌ Database connection failed!")
            return
        
        cursor = connection.cursor()
        
        # Check if roll number already exists
        check_query = "SELECT student_id FROM student WHERE roll_number = %s"
        cursor.execute(check_query, (roll_number,))
        
        if cursor.fetchone():
            print(f"\n❌ ERROR: Roll Number '{roll_number}' already exists!")
            cursor.close()
            connection.close()
            return
        
        # Insert new student
        insert_query = """
        INSERT INTO student (name, roll_number, class, email, phone, address, date_of_admission)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        
        cursor.execute(insert_query, (name, roll_number, class_name, email, phone, address, datetime.now().date()))
        connection.commit()
        
        print(f"\n✓ SUCCESS: Student '{name}' added successfully!")
        print(f"  Student ID: {cursor.lastrowid}")
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"\n❌ ERROR: {e}")


def view_student_details():
    """
    View details of a student by Student ID.
    """
    try:
        print("\n" + "="*60)
        print("VIEW STUDENT DETAILS")
        print("="*60)
        
        student_id = input("Enter Student ID: ").strip()
        if not student_id.isdigit():
            print("❌ Student ID must be a number!")
            return
        
        connection = get_database_connection()
        if connection is None:
            print("❌ Database connection failed!")
            return
        
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT * FROM student WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()
        
        if not student:
            print(f"\n❌ No student found with ID {student_id}!")
            cursor.close()
            connection.close()
            return
        
        print("\n" + "-"*60)
        print("STUDENT INFORMATION")
        print("-"*60)
        print(f"Student ID:          {student['student_id']}")
        print(f"Name:                {student['name']}")
        print(f"Roll Number:         {student['roll_number']}")
        print(f"Class:               {student['class']}")
        print(f"Email:               {student['email']}")
        print(f"Phone:               {student['phone']}")
        print(f"Address:             {student['address']}")
        print(f"Date of Admission:   {student['date_of_admission']}")
        print("-"*60)
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"\n❌ ERROR: {e}")


def update_student_info():
    """
    Update student information by Student ID.
    """
    try:
        print("\n" + "="*60)
        print("UPDATE STUDENT INFORMATION")
        print("="*60)
        
        student_id = input("Enter Student ID to update: ").strip()
        if not student_id.isdigit():
            print("❌ Student ID must be a number!")
            return
        
        connection = get_database_connection()
        if connection is None:
            print("❌ Database connection failed!")
            return
        
        cursor = connection.cursor(dictionary=True)
        
        # Check if student exists
        query = "SELECT * FROM student WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()
        
        if not student:
            print(f"\n❌ No student found with ID {student_id}!")
            cursor.close()
            connection.close()
            return
        
        print(f"\nCurrent Details for {student['name']}:")
        print(f"Email: {student['email']}")
        print(f"Phone: {student['phone']}")
        print(f"Address: {student['address']}")
        
        print("\nWhat would you like to update?")
        print("1. Email")
        print("2. Phone")
        print("3. Address")
        print("4. All")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        update_query = "UPDATE student SET "
        update_params = []
        
        if choice == '1' or choice == '4':
            email = input("Enter new Email: ").strip()
            if email and '@' not in email:
                print("❌ Invalid email format!")
                return
            update_query += "email = %s, "
            update_params.append(email)
        
        if choice == '2' or choice == '4':
            phone = input("Enter new Phone: ").strip()
            if phone and not phone.isdigit():
                print("❌ Phone number must contain only digits!")
                return
            update_query += "phone = %s, "
            update_params.append(phone)
        
        if choice == '3' or choice == '4':
            address = input("Enter new Address: ").strip()
            update_query += "address = %s, "
            update_params.append(address)
        
        if not update_params:
            print("❌ No updates made!")
            return
        
        update_query = update_query.rstrip(", ")
        update_query += " WHERE student_id = %s"
        update_params.append(student_id)
        
        cursor.execute(update_query, update_params)
        connection.commit()
        
        print(f"\n✓ SUCCESS: Student information updated successfully!")
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"\n❌ ERROR: {e}")


def delete_student_record():
    """
    Delete a student record by Student ID.
    """
    try:
        print("\n" + "="*60)
        print("DELETE STUDENT RECORD")
        print("="*60)
        
        student_id = input("Enter Student ID to delete: ").strip()
        if not student_id.isdigit():
            print("❌ Student ID must be a number!")
            return
        
        connection = get_database_connection()
        if connection is None:
            print("❌ Database connection failed!")
            return
        
        cursor = connection.cursor(dictionary=True)
        
        # Check if student exists
        query = "SELECT name FROM student WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()
        
        if not student:
            print(f"\n❌ No student found with ID {student_id}!")
            cursor.close()
            connection.close()
            return
        
        confirm = input(f"\n⚠️  WARNING: You are about to delete '{student['name']}' and all associated records!\n"
                       "Are you sure? (YES/NO): ").strip().upper()
        
        if confirm != 'YES':
            print("❌ Deletion cancelled!")
            cursor.close()
            connection.close()
            return
        
        # Delete student record (cascading delete will handle related records)
        delete_query = "DELETE FROM student WHERE student_id = %s"
        cursor.execute(delete_query, (student_id,))
        connection.commit()
        
        print(f"\n✓ SUCCESS: Student record deleted successfully!")
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"\n❌ ERROR: {e}")


# ============================================================================
# FEE MANAGEMENT MODULE
# ============================================================================

def assign_fee():
    """
    Assign fee to a student.
    """
    try:
        print("\n" + "="*60)
        print("ASSIGN FEE TO STUDENT")
        print("="*60)
        
        student_id = input("Enter Student ID: ").strip()
        if not student_id.isdigit():
            print("❌ Student ID must be a number!")
            return
        
        connection = get_database_connection()
        if connection is None:
            print("❌ Database connection failed!")
            return
        
        cursor = connection.cursor(dictionary=True)
        
        # Check if student exists
        query = "SELECT name FROM student WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()
        
        if not student:
            print(f"\n❌ No student found with ID {student_id}!")
            cursor.close()
            connection.close()
            return
        
        # Check if fee already assigned
        fee_query = "SELECT fee_id FROM fee WHERE student_id = %s AND status != 'PAID'"
        cursor.execute(fee_query, (student_id,))
        
        if cursor.fetchone():
            print(f"\n❌ Fee already assigned to this student!")
            cursor.close()
            connection.close()
            return
        
        try:
            total_fee = float(input("Enter Total Fee Amount (in Rs.): ").strip())
            if total_fee <= 0:
                print("❌ Fee amount must be greater than 0!")
                return
        except ValueError:
            print("❌ Invalid amount! Please enter a numeric value.")
            return
        
        insert_query = """
        INSERT INTO fee (student_id, total_fee, paid_amount, pending_amount, status, assigned_date)
        VALUES (%s, %s, 0, %s, 'PENDING', %s)
        """
        
        cursor.execute(insert_query, (student_id, total_fee, total_fee, datetime.now().date()))
        connection.commit()
        
        print(f"\n✓ SUCCESS: Fee of Rs. {total_fee} assigned to '{student['name']}'!")
        print(f"  Fee ID: {cursor.lastrowid}")
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"\n❌ ERROR: {e}")


def pay_fee():
    """
    Record fee payment (full or partial).
    """
    try:
        print("\n" + "="*60)
        print("PAY FEE")
        print("="*60)
        
        student_id = input("Enter Student ID: ").strip()
        if not student_id.isdigit():
            print("❌ Student ID must be a number!")
            return
        
        connection = get_database_connection()
        if connection is None:
            print("❌ Database connection failed!")
            return
        
        cursor = connection.cursor(dictionary=True)
        
        # Check if student exists
        query = "SELECT name FROM student WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()
        
        if not student:
            print(f"\n❌ No student found with ID {student_id}!")
            cursor.close()
            connection.close()
            return
        
        # Get fee details
        fee_query = """
        SELECT fee_id, total_fee, paid_amount, pending_amount, status 
        FROM fee WHERE student_id = %s AND status != 'PAID'
        """
        cursor.execute(fee_query, (student_id,))
        fee = cursor.fetchone()
        
        if not fee:
            print(f"\n❌ No pending fee found for this student!")
            cursor.close()
            connection.close()
            return
        
        print(f"\nFee Details for '{student['name']}':")
        print(f"Total Fee:     Rs. {fee['total_fee']}")
        print(f"Paid Amount:   Rs. {fee['paid_amount']}")
        print(f"Pending:       Rs. {fee['pending_amount']}")
        print(f"Status:        {fee['status']}")
        
        try:
            payment_amount = float(input("\nEnter Payment Amount: ").strip())
            if payment_amount <= 0:
                print("❌ Payment amount must be greater than 0!")
                return
            if payment_amount > fee['pending_amount']:
                print(f"❌ Payment amount exceeds pending amount of Rs. {fee['pending_amount']}!")
                return
        except ValueError:
            print("❌ Invalid amount! Please enter a numeric value.")
            return
        
        payment_method = input("Enter Payment Method (Cash/Cheque/Online): ").strip()
        remarks = input("Enter Remarks (optional): ").strip()
        
        # Update fee record
        new_paid = fee['paid_amount'] + payment_amount
        new_pending = fee['total_fee'] - new_paid
        new_status = 'PAID' if new_pending == 0 else 'PARTIAL'
        
        update_query = """
        UPDATE fee SET paid_amount = %s, pending_amount = %s, status = %s
        WHERE fee_id = %s
        """
        cursor.execute(update_query, (new_paid, new_pending, new_status, fee['fee_id']))
        
        # Insert payment record
        payment_query = """
        INSERT INTO payment_record (student_id, fee_id, payment_amount, payment_method, remarks)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(payment_query, (student_id, fee['fee_id'], payment_amount, payment_method, remarks))
        
        connection.commit()
        
        print(f"\n✓ SUCCESS: Payment of Rs. {payment_amount} recorded!")
        print(f"  Remaining Pending: Rs. {new_pending}")
        print(f"  Status: {new_status}")
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"\n❌ ERROR: {e}")


def view_fee_status():
    """
    View fee status (paid/pending) for a student.
    """
    try:
        print("\n" + "="*60)
        print("VIEW FEE STATUS")
        print("="*60)
        
        student_id = input("Enter Student ID: ").strip()
        if not student_id.isdigit():
            print("❌ Student ID must be a number!")
            return
        
        connection = get_database_connection()
        if connection is None:
            print("❌ Database connection failed!")
            return
        
        cursor = connection.cursor(dictionary=True)
        
        # Get student details
        student_query = "SELECT name FROM student WHERE student_id = %s"
        cursor.execute(student_query, (student_id,))
        student = cursor.fetchone()
        
        if not student:
            print(f"\n❌ No student found with ID {student_id}!")
            cursor.close()
            connection.close()
            return
        
        # Get fee details
        fee_query = "SELECT * FROM fee WHERE student_id = %s"
        cursor.execute(fee_query, (student_id,))
        fee = cursor.fetchone()
        
        if not fee:
            print(f"\n❌ No fee record found for this student!")
            cursor.close()
            connection.close()
            return
        
        print("\n" + "-"*60)
        print("FEE STATUS")
        print("-"*60)
        print(f"Student Name:        {student['name']}")
        print(f"Fee ID:              {fee['fee_id']}")
        print(f"Total Fee:           Rs. {fee['total_fee']}")
        print(f"Paid Amount:         Rs. {fee['paid_amount']}")
        print(f"Pending Amount:      Rs. {fee['pending_amount']}")
        print(f"Status:              {fee['status']}")
        print(f"Date Assigned:       {fee['assigned_date']}")
        print("-"*60)
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"\n❌ ERROR: {e}")


# ============================================================================
# PAYMENT RECORDS MODULE
# ============================================================================

def view_payment_history():
    """
    View payment history of a student.
    """
    try:
        print("\n" + "="*60)
        print("VIEW PAYMENT HISTORY")
        print("="*60)
        
        student_id = input("Enter Student ID: ").strip()
        if not student_id.isdigit():
            print("❌ Student ID must be a number!")
            return
        
        connection = get_database_connection()
        if connection is None:
            print("❌ Database connection failed!")
            return
        
        cursor = connection.cursor(dictionary=True)
        
        # Get student details
        student_query = "SELECT name FROM student WHERE student_id = %s"
        cursor.execute(student_query, (student_id,))
        student = cursor.fetchone()
        
        if not student:
            print(f"\n❌ No student found with ID {student_id}!")
            cursor.close()
            connection.close()
            return
        
        # Get payment records
        payment_query = """
        SELECT payment_id, payment_amount, payment_date, payment_method, remarks
        FROM payment_record WHERE student_id = %s
        ORDER BY payment_date DESC
        """
        cursor.execute(payment_query, (student_id,))
        payments = cursor.fetchall()
        
        if not payments:
            print(f"\n❌ No payment records found for this student!")
            cursor.close()
            connection.close()
            return
        
        print(f"\nPayment History for '{student['name']}':")
        print("-"*80)
        print(f"{'Payment ID':<12} {'Amount':<15} {'Date':<20} {'Method':<15} {'Remarks':<18}")
        print("-"*80)
        
        total_paid = 0
        for payment in payments:
            print(f"{payment['payment_id']:<12} Rs. {payment['payment_amount']:<12.2f} {str(payment['payment_date']):<20} {payment['payment_method']:<15} {payment['remarks']:<18}")
            total_paid += payment['payment_amount']
        
        print("-"*80)
        print(f"{'TOTAL PAID:':<27} Rs. {total_paid:.2f}")
        print("-"*80)
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"\n❌ ERROR: {e}")


# ============================================================================
# REPORTS MODULE
# ============================================================================

def view_all_students():
    """
    Generate report: View all students in the system.
    """
    try:
        print("\n" + "="*60)
        print("ALL STUDENTS REPORT")
        print("="*60)
        
        connection = get_database_connection()
        if connection is None:
            print("❌ Database connection failed!")
            return
        
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT student_id, name, roll_number, class, email, phone FROM student ORDER BY student_id"
        cursor.execute(query)
        students = cursor.fetchall()
        
        if not students:
            print("\n❌ No students found in the system!")
            cursor.close()
            connection.close()
            return
        
        print(f"\nTotal Students: {len(students)}")
        print("-"*100)
        print(f"{'ID':<5} {'Name':<25} {'Roll No.':<12} {'Class':<10} {'Email':<25} {'Phone':<15}")
        print("-"*100)
        
        for student in students:
            email = student['email'] if student['email'] else 'N/A'
            phone = student['phone'] if student['phone'] else 'N/A'
            print(f"{student['student_id']:<5} {student['name']:<25} {student['roll_number']:<12} {student['class']:<10} {email:<25} {phone:<15}")
        
        print("-"*100)
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"\n❌ ERROR: {e}")


def view_pending_fees():
    """
    Generate report: View students with pending fees.
    """
    try:
        print("\n" + "="*60)
        print("PENDING FEES REPORT")
        print("="*60)
        
        connection = get_database_connection()
        if connection is None:
            print("❌ Database connection failed!")
            return
        
        cursor = connection.cursor(dictionary=True)
        
        query = """
        SELECT s.student_id, s.name, s.roll_number, s.class,
               f.fee_id, f.total_fee, f.paid_amount, f.pending_amount, f.status
        FROM student s
        JOIN fee f ON s.student_id = f.student_id
        WHERE f.status IN ('PENDING', 'PARTIAL')
        ORDER BY f.pending_amount DESC
        """
        
        cursor.execute(query)
        records = cursor.fetchall()
        
        if not records:
            print("\n✓ No students with pending fees!")
            cursor.close()
            connection.close()
            return
        
        print(f"\nStudents with Pending Fees: {len(records)}")
        print("-"*110)
        print(f"{'ID':<5} {'Name':<20} {'Roll No.':<10} {'Class':<8} {'Total':<12} {'Paid':<12} {'Pending':<12} {'Status':<10}")
        print("-"*110)
        
        total_pending = 0
        for record in records:
            print(f"{record['student_id']:<5} {record['name']:<20} {record['roll_number']:<10} {record['class']:<8} "
                  f"Rs. {record['total_fee']:<10.2f} Rs. {record['paid_amount']:<10.2f} Rs. {record['pending_amount']:<10.2f} {record['status']:<10}")
            total_pending += record['pending_amount']
        
        print("-"*110)
        print(f"{'TOTAL PENDING:':<57} Rs. {total_pending:.2f}")
        print("-"*110)
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"\n❌ ERROR: {e}")


def view_total_fee_collected():
    """
    Generate report: View total fee collected.
    """
    try:
        print("\n" + "="*60)
        print("TOTAL FEE COLLECTED REPORT")
        print("="*60)
        
        connection = get_database_connection()
        if connection is None:
            print("❌ Database connection failed!")
            return
        
        cursor = connection.cursor(dictionary=True)
        
        # Total fee collected
        collection_query = "SELECT SUM(payment_amount) as total_collected FROM payment_record"
        cursor.execute(collection_query)
        collection = cursor.fetchone()
        total_collected = collection['total_collected'] if collection['total_collected'] else 0
        
        # Total fee assigned
        total_query = "SELECT SUM(total_fee) as total_fee FROM fee"
        cursor.execute(total_query)
        total = cursor.fetchone()
        total_fee = total['total_fee'] if total['total_fee'] else 0
        
        # Total pending
        pending_query = "SELECT SUM(pending_amount) as total_pending FROM fee WHERE status IN ('PENDING', 'PARTIAL')"
        cursor.execute(pending_query)
        pending = cursor.fetchone()
        total_pending = pending['total_pending'] if pending['total_pending'] else 0
        
        # Fully paid students
        paid_query = "SELECT COUNT(*) as paid_count FROM fee WHERE status = 'PAID'"
        cursor.execute(paid_query)
        paid_result = cursor.fetchone()
        fully_paid = paid_result['paid_count']
        
        # Partial payment students
        partial_query = "SELECT COUNT(*) as partial_count FROM fee WHERE status = 'PARTIAL'"
        cursor.execute(partial_query)
        partial_result = cursor.fetchone()
        partially_paid = partial_result['partial_count']
        
        # Pending students
        pending_count_query = "SELECT COUNT(*) as pending_count FROM fee WHERE status = 'PENDING'"
        cursor.execute(pending_count_query)
        pending_count_result = cursor.fetchone()
        pending_count = pending_count_result['pending_count']
        
        print("\n" + "-"*60)
        print("FINANCIAL SUMMARY")
        print("-"*60)
        print(f"Total Fee Assigned:      Rs. {total_fee:>12,.2f}")
        print(f"Total Fee Collected:     Rs. {total_collected:>12,.2f}")
        print(f"Total Pending:           Rs. {total_pending:>12,.2f}")
        print("-"*60)
        print(f"Collection Percentage:   {(total_collected/total_fee*100 if total_fee > 0 else 0):>12.2f}%")
        print("-"*60)
        
        print("\nSTUDENT-WISE BREAKDOWN")
        print("-"*60)
        print(f"Fully Paid:              {fully_paid:>17}")
        print(f"Partial Payment:         {partially_paid:>17}")
        print(f"Pending:                 {pending_count:>17}")
        print("-"*60)
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"\n❌ ERROR: {e}")


# ============================================================================
# MAIN MENU SYSTEM
# ============================================================================

def display_main_menu():
    """
    Display the main menu.
    """
    print("\n" + "="*60)
    print("         SCHOOL FEE MANAGEMENT SYSTEM (SFMS)")
    print("="*60)
    print("\n1.  Student Management")
    print("2.  Fee Management")
    print("3.  Payment Records")
    print("4.  Reports")
    print("5.  Initialize Database")
    print("6.  Exit")
    print("\n" + "="*60)


def student_management_menu():
    """
    Student management submenu.
    """
    while True:
        print("\n" + "="*60)
        print("         STUDENT MANAGEMENT")
        print("="*60)
        print("\n1.  Add New Student")
        print("2.  View Student Details")
        print("3.  Update Student Information")
        print("4.  Delete Student Record")
        print("5.  Back to Main Menu")
        print("\n" + "="*60)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student_details()
        elif choice == '3':
            update_student_info()
        elif choice == '4':
            delete_student_record()
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")


def fee_management_menu():
    """
    Fee management submenu.
    """
    while True:
        print("\n" + "="*60)
        print("         FEE MANAGEMENT")
        print("="*60)
        print("\n1.  Assign Fee to Student")
        print("2.  Pay Fee")
        print("3.  View Fee Status")
        print("4.  Back to Main Menu")
        print("\n" + "="*60)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            assign_fee()
        elif choice == '2':
            pay_fee()
        elif choice == '3':
            view_fee_status()
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")


def payment_records_menu():
    """
    Payment records submenu.
    """
    while True:
        print("\n" + "="*60)
        print("         PAYMENT RECORDS")
        print("="*60)
        print("\n1.  View Payment History")
        print("2.  Back to Main Menu")
        print("\n" + "="*60)
        
        choice = input("Enter your choice (1-2): ").strip()
        
        if choice == '1':
            view_payment_history()
        elif choice == '2':
            break
        else:
            print("❌ Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")


def reports_menu():
    """
    Reports submenu.
    """
    while True:
        print("\n" + "="*60)
        print("         REPORTS")
        print("="*60)
        print("\n1.  View All Students")
        print("2.  View Students with Pending Fees")
        print("3.  View Total Fee Collected")
        print("4.  Back to Main Menu")
        print("\n" + "="*60)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            view_all_students()
        elif choice == '2':
            view_pending_fees()
        elif choice == '3':
            view_total_fee_collected()
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")


def main():
    """
    Main program flow.
    """
    print("\n" + "="*60)
    print("         WELCOME TO SCHOOL FEE MANAGEMENT SYSTEM")
    print("="*60)
    print("\nInitializing system...")
    
    # Check database connection
    connection = get_database_connection()
    if connection is None:
        print("\n❌ FATAL ERROR: Cannot connect to database!")
        print("Please ensure:")
        print("   - MySQL server is running")
        print("   - Database 'mydb' exists")
        print("   - Credentials are correct (localhost/root/1234)")
        return
    
    connection.close()
    print("✓ Database connection successful!")
    
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            student_management_menu()
        elif choice == '2':
            fee_management_menu()
        elif choice == '3':
            payment_records_menu()
        elif choice == '4':
            reports_menu()
        elif choice == '5':
            confirm = input("\n⚠️  This will create/reset all tables. Continue? (YES/NO): ").strip().upper()
            if confirm == 'YES':
                create_tables()
        elif choice == '6':
            print("\n" + "="*60)
            print("Thank you for using School Fee Management System!")
            print("Goodbye!")
            print("="*60 + "\n")
            break
        else:
            print("❌ Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()


# ================================================================================
# END OF SCHOOL FEE MANAGEMENT SYSTEM
# ================================================================================
