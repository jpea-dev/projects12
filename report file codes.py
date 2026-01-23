# %% [markdown]
# Program 1: Input any number from user and calculate factorial of a number

# %%
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print("Factorial of " + str(n) + " is " + str(fact))

# Example call:
num = int(input("Enter a number: "))
factorial(num)

num = int(input("Enter a number: "))
factorial(num)

# %% [markdown]
# Program 2: Input any number from user and check it is Prime number or not

# %%
def is_prime(n):
    prime = True
    if n <= 1:
        prime = False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            prime = False
            break
    if prime:
        print(str(n) + " is a prime number.")
    else:
        print(str(n) + " is not a prime number.")

num = int(input("Enter a number: "))
is_prime(num)

num = int(input("Enter a number: "))
is_prime(num)

# %% [markdown]
# Program 3: Read a text file line by line and display each word separated by a #.
# 

# %%
def process_file_words(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                words = line.split()
                print('#'.join(words))

    except FileNotFoundError:
        print("Error: The file was not found")

# Call the function with the dummy file
process_file_words('sample.txt')

# %% [markdown]
# Program 4: Read a text file and display the number of vowels/consonants/uppercase/lowercase
# characters in the file.

# %%
def analyze_file_characters(filepath):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    uppercase_count = 0
    lowercase_count = 0

    try:
        with open(filepath, 'r') as file:
            content = file.read()
            for char in content:
                if char.isalpha():
                    if char.lower() in vowels:
                        vowel_count += 1
                    else:
                        consonant_count += 1

                    if char.isupper():
                        uppercase_count += 1
                    elif char.islower():
                        lowercase_count += 1

        print(f"File: {filepath}")
        print(f"Number of vowels: {vowel_count}")
        print(f"Number of consonants: {consonant_count}")
        print(f"Number of uppercase characters: {uppercase_count}")
        print(f"Number of lowercase characters: {lowercase_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the sample.txt file
analyze_file_characters('sample.txt')

# %% [markdown]
#  Program 5: Remove all the lines that contain the character 'a' in a file and write it to another
# file.

# %%
def filter_lines_without_char(input_filepath, output_filepath, char):
    records = []
    try:
        with open(input_filepath, 'r') as infile:
          records = infile.readlines()

        with open(output_filepath, 'w') as outfile:
            for line in records:
                if char not in line:
                    outfile.write(line)
        print("Lines without", char, "written to", output_filepath, "from", input_filepath)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print("An error occurred: ", e)

# Call the function to remove lines
# containing 'a' from 'sample.txt' and write to 'without_a.txt'
filter_lines_without_char('sample.txt', 'without_a.txt', 'a')

# %% [markdown]
# Program 6: Create a binary file with name and roll number. Search for a given roll number and
# display the name, if not found display appropriate message.

# %%
import pickle

file_name = 'students.dat'

def create_binary_file(filename):
    try:
        with open(filename, 'ab') as file:
            name = input("Enter name: ")
            roll_number = int(input("Enter roll number: "))
            data = [name, roll_number]
            pickle.dump(data, file)
        print("Record added successfully:", data)
    except Exception as e:
        print("Error creating file:", e)


def search_roll_number(filename, roll_number_to_find):
    found = False
    try:
        with open(filename, 'rb') as file:
            while True:
                data = pickle.load(file)
                if data[1] == roll_number_to_find:
                    print("Roll number found: ", roll_number_to_find)
                    print("Name:", data[0])
                    found = True
                    break
    except EOFError:
        pass
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error while searching:", e)

    if not found:
        print("Roll number", roll_number_to_find, "not found.")

def readdata(filename):
  data = []
  try:
    with open(filename, 'rb') as file:
      while True:
        data.append(pickle.load(file))
  except EOFError:
      pass
  for i in data:
    print("Roll number: ", i[1], "Name: ", i[0])

# Read Data
if input("Do you want to read data from binary file? (y/n): ").lower() == 'y':
    readdata(file_name)

# Create / Add records
if input("Do you want to create/add data in binary file? (y/n): ").lower() == 'y':
    create_binary_file(file_name)

# Search by roll number
if input("Do you want to search a name by roll number? (y/n): ").lower() == 'y':
    roll_number = int(input("Enter roll number to search: "))
    search_roll_number(file_name, roll_number)

# %% [markdown]
# Program 7: Create a binary file with roll number, name and marks. Input a roll number and
# update the marks.

# %%
import pickle

def create_student_binary_file(filename):
    try:
        with open(filename, 'ab') as file:
          roll = int(input("Enter roll number: "))
          name = input("Enter name: ")
          marks = int(input("Enter marks: "))
          record = (roll, name, marks)
          pickle.dump(record, file)
          print("Binary file created successfully.")
    except Exception as e:
        print("Error creating file:", e)

def update_student_marks_binary(filename, roll_number_to_update, new_marks):
    records = []
    updated = False

    try:
        with open(filename, 'rb') as file:
            while True:
                records.append(pickle.load(file))
    except EOFError:
        pass
    except FileNotFoundError:
        print("File not found.")
        return

    for i, record in enumerate(records):
        if record[0] == roll_number_to_update:
            records[i] = (record[0], record[1], new_marks)
            updated = True
            break

    if updated:
        with open(filename, 'wb') as file:
            for record in records:
                pickle.dump(record, file)
        print("Marks updated successfully.")
    else:
        print("Roll number not found.")


def display_all_students_binary(filename):
    try:
        with open(filename, 'rb') as file:
            print("\n--- Student Records ---")
            while True:
                roll, name, marks = pickle.load(file)
                print("Roll:", roll, "Name:", name, "Marks:", marks)
    except EOFError:
        pass
    except FileNotFoundError:
        print("File not found.")


# -------- Main Program --------

file_name = "students_data.dat"

if input("Create binary file? (y/n): ").lower() == 'y':
    create_student_binary_file(file_name)

if input("Display records? (y/n): ").lower() == 'y':
    display_all_students_binary(file_name)

if input("Update marks? (y/n): ").lower() == 'y':
    r = int(input("Enter roll number to update: "))
    m = int(input("Enter new marks: "))
    update_student_marks_binary(file_name, r, m)

if input("Display records again? (y/n): ").lower() == 'y':
    display_all_students_binary(file_name)

# %% [markdown]
# Program 8: Write a random number generator that generates random numbers between 1 and
# 6 (simulates a dice).

# %%
import random

def roll_dice():
    """Generates a random number between 1 and 6, simulating a dice roll."""
    return random.randint(1, 6)

# Example usage:
print(f"Dice roll: {roll_dice()}")
print(f"Another dice roll: {roll_dice()}")

# %% [markdown]
# Program 9: Write a Python program to implement a stack using list.

# %%
stack = [] # The global list that will act as our stack

def is_empty():
    """Returns True if the stack is empty, False otherwise."""
    return len(stack) == 0

def push(item):
    """Adds an item to the top of the stack."""
    stack.append(item)
    print(item, "pushed to stack.")

def pop():
    """Removes and returns the item from the top of the stack.
    Returns None and prints a message if the stack is empty."""
    if is_empty():
        print("Stack is empty. Cannot pop.")
        return None
    item = stack.pop()
    print(item, "popped from stack.")
    return item

def peek():
    """Returns the item at the top of the stack without removing it.
    Returns None and prints a message if the stack is empty."""
    if is_empty():
        print("Stack is empty. Cannot peek.")
        return None
    item = stack[-1]
    print("Top element: ", item)
    return item

def size():
    """Returns the number of items in the stack."""
    current_size = len(stack)
    print("Stack size: ", current_size)
    return current_size

def display_stack():
    """Displays the current contents of the stack."""
    if is_empty():
        print("Stack is empty.")
    else:
        print(f"Current stack: ", stack)

# --- Menu Driven Program ---
def stack_menu_program():
    while True:
        print("\n--- Stack Operations Menu ---")
        print("1. Push element")
        print("2. Pop element")
        print("3. Peek at top element")
        print("4. Check if stack is empty")
        print("5. Get stack size")
        print("6. Display stack")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter element to push: ")
            push(item)
        elif choice == '2':
            pop()
        elif choice == '3':
            peek()
        elif choice == '4':
            if is_empty():
                print("Stack is indeed empty.")
            else:
                print("Stack is not empty.")
        elif choice == '5':
            size()
        elif choice == '6':
            display_stack()
        elif choice == '7':
            print("Exiting stack program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu-driven program
stack_menu_program()


# %% [markdown]
# Program 10: Create a CSV file by entering user-id and password, read and search the password for given userid.

# %%
import csv

def add_user(filepath):
    try:
        with open(filepath, 'a', newline='') as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(['UserID', 'Password'])

            uid = input("Enter User ID: ")
            pwd = input("Enter Password: ")
            writer.writerow([uid, pwd])

        print("User credentials added successfully.")
    except Exception as e:
        print("Error:", e)

def search_user(filepath):
    try:
        uid = input("Enter User ID to search: ")
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[0] == uid:
                    print("Password:", row[1])
                    return
        print("User not found.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)

# Main Program
file = "user_credentials.csv"

while True:
    print("\n1. Add User Credentials")
    print("2. Search Password")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_user(file)
    elif choice == 2:
        search_user(file)
    elif choice == 3:
        break
    else:
        print("Invalid choice")


# %% [markdown]
# Program 11: Integrate SQL with Python by importing suitable module.

# %%
import mysql.connector

def connect_to_database():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="mydb",
        )

    if conn.is_connected():
        print("Connected to MySQL database successfully!")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        print("Query returned rows: ", len(rows))
        for r in rows:
            print(r)
        conn.close()
        cursor.close()
    else:
        print("Connection created but is_connected() returned False")


if __name__ == "__main__":
    connect_to_database()

# %% [markdown]
# ```
# PS C:\Users\noteb\OneDrive\Desktop\ws> mysql -u root -p
# Enter password: ****
# Welcome to the MySQL monitor.  Commands end with ; or \g.
# Your MySQL connection id is 9
# Server version: 8.0.44 MySQL Community Server - GPL
# 
# Copyright (c) 2000, 2025, Oracle and/or its affiliates.
# 
# Oracle is a registered trademark of Oracle Corporation and/or its
# affiliates. Other names may be trademarks of their respective
# owners.
# 
# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
# 
# mysql>
# mysql> show databases;
# +--------------------+
# | Database           |
# +--------------------+
# | information_schema |
# | mydb               |
# | mysql              |
# | performance_schema |
# | sys                |
# +--------------------+
# 5 rows in set (0.04 sec)
# 
# mysql> use mydb;
# Database changed
# mysql> CREATE TABLE Student (
#     ->     Roll_No INT PRIMARY KEY,
#     ->     Name VARCHAR(50),
#     ->     Class INT,
#     ->     Marks INT,
#     ->     Age INT
#     -> );
# Query OK, 0 rows affected (0.04 sec)
# 
# mysql> desc student;
# +---------+-------------+------+-----+---------+-------+
# | Field   | Type        | Null | Key | Default | Extra |
# +---------+-------------+------+-----+---------+-------+
# | Roll_No | int         | NO   | PRI | NULL    |       |
# | Name    | varchar(50) | YES  |     | NULL    |       |
# | Class   | int         | YES  |     | NULL    |       |
# | Marks   | int         | YES  |     | NULL    |       |
# | Age     | int         | YES  |     | NULL    |       |
# +---------+-------------+------+-----+---------+-------+
# 5 rows in set (0.01 sec)
# 
# mysql> INSERT INTO Student VALUES
#     -> (1, 'Aman', 12, 85, 17),
#     -> (2, 'Riya', 12, 92, 18),
#     -> (3, 'Karan', 11, 78, 16),
#     -> (4, 'Neha', 12, 88, 17),
#     -> (5, 'Arjun', 11, 69, 16);
# Query OK, 5 rows affected (0.01 sec)
# Records: 5  Duplicates: 0  Warnings: 0
# 
# mysql> select * from student;
# +---------+-------+-------+-------+------+
# | Roll_No | Name  | Class | Marks | Age  |
# +---------+-------+-------+-------+------+
# |       1 | Aman  |    12 |    85 |   17 |
# |       2 | Riya  |    12 |    92 |   18 |
# |       3 | Karan |    11 |    78 |   16 |
# |       4 | Neha  |    12 |    88 |   17 |
# |       5 | Arjun |    11 |    69 |   16 |
# +---------+-------+-------+-------+------+
# 5 rows in set (0.00 sec)
# 
# mysql> ALTER TABLE Student
#     -> ADD Section CHAR(1);
# Query OK, 0 rows affected (0.08 sec)
# Records: 0  Duplicates: 0  Warnings: 0
# 
# mysql> desc student;
# +---------+-------------+------+-----+---------+-------+
# | Field   | Type        | Null | Key | Default | Extra |
# +---------+-------------+------+-----+---------+-------+
# | Roll_No | int         | NO   | PRI | NULL    |       |
# | Name    | varchar(50) | YES  |     | NULL    |       |
# | Class   | int         | YES  |     | NULL    |       |
# | Marks   | int         | YES  |     | NULL    |       |
# | Age     | int         | YES  |     | NULL    |       |
# | Section | char(1)     | YES  |     | NULL    |       |
# +---------+-------------+------+-----+---------+-------+
# 6 rows in set (0.00 sec)
# 
# mysql> ALTER TABLE Student
#     -> MODIFY Name VARCHAR(100);
# Query OK, 5 rows affected (0.09 sec)
# Records: 5  Duplicates: 0  Warnings: 0
# 
# mysql> desc student;
# +---------+--------------+------+-----+---------+-------+
# | Field   | Type         | Null | Key | Default | Extra |
# +---------+--------------+------+-----+---------+-------+
# | Roll_No | int          | NO   | PRI | NULL    |       |
# | Name    | varchar(100) | YES  |     | NULL    |       |
# | Class   | int          | YES  |     | NULL    |       |
# | Marks   | int          | YES  |     | NULL    |       |
# | Age     | int          | YES  |     | NULL    |       |
# | Section | char(1)      | YES  |     | NULL    |       |
# +---------+--------------+------+-----+---------+-------+
# 6 rows in set (0.00 sec)
# 
# mysql> ALTER TABLE Student
#     -> DROP Age;
# Query OK, 0 rows affected (0.01 sec)
# Records: 0  Duplicates: 0  Warnings: 0
# 
# mysql> desc student;
# +---------+--------------+------+-----+---------+-------+
# | Field   | Type         | Null | Key | Default | Extra |
# +---------+--------------+------+-----+---------+-------+
# | Roll_No | int          | NO   | PRI | NULL    |       |
# | Name    | varchar(100) | YES  |     | NULL    |       |
# | Class   | int          | YES  |     | NULL    |       |
# | Marks   | int          | YES  |     | NULL    |       |
# | Section | char(1)      | YES  |     | NULL    |       |
# +---------+--------------+------+-----+---------+-------+
# 5 rows in set (0.00 sec)
# 
# mysql> UPDATE Student
#     -> SET Marks = 90
#     -> WHERE Roll_No = 1;
# Query OK, 1 row affected (0.00 sec)
# Rows matched: 1  Changed: 1  Warnings: 0
# 
# mysql> select * from student;
# +---------+-------+-------+-------+---------+
# | Roll_No | Name  | Class | Marks | Section |
# +---------+-------+-------+-------+---------+
# |       1 | Aman  |    12 |    90 | NULL    |
# |       2 | Riya  |    12 |    92 | NULL    |
# |       3 | Karan |    11 |    78 | NULL    |
# |       4 | Neha  |    12 |    88 | NULL    |
# |       5 | Arjun |    11 |    69 | NULL    |
# +---------+-------+-------+-------+---------+
# 5 rows in set (0.00 sec)
# 
# mysql> SELECT * FROM Student
#     -> ORDER BY Marks;
# +---------+-------+-------+-------+---------+
# | Roll_No | Name  | Class | Marks | Section |
# +---------+-------+-------+-------+---------+
# |       5 | Arjun |    11 |    69 | NULL    |
# |       3 | Karan |    11 |    78 | NULL    |
# |       4 | Neha  |    12 |    88 | NULL    |
# |       1 | Aman  |    12 |    90 | NULL    |
# |       2 | Riya  |    12 |    92 | NULL    |
# +---------+-------+-------+-------+---------+
# 5 rows in set (0.00 sec)
# 
# mysql> SELECT * FROM Student
#     -> ORDER BY Marks DESC;
# +---------+-------+-------+-------+---------+
# | Roll_No | Name  | Class | Marks | Section |
# +---------+-------+-------+-------+---------+
# |       2 | Riya  |    12 |    92 | NULL    |
# |       1 | Aman  |    12 |    90 | NULL    |
# |       4 | Neha  |    12 |    88 | NULL    |
# |       3 | Karan |    11 |    78 | NULL    |
# |       5 | Arjun |    11 |    69 | NULL    |
# +---------+-------+-------+-------+---------+
# 5 rows in set (0.00 sec)
# 
# mysql> DELETE FROM Student
#     -> WHERE Marks < 70;
# Query OK, 1 row affected (0.00 sec)
# 
# mysql> select * from student;
# +---------+-------+-------+-------+---------+
# | Roll_No | Name  | Class | Marks | Section |
# +---------+-------+-------+-------+---------+
# |       1 | Aman  |    12 |    90 | NULL    |
# |       2 | Riya  |    12 |    92 | NULL    |
# |       3 | Karan |    11 |    78 | NULL    |
# |       4 | Neha  |    12 |    88 | NULL    |
# +---------+-------+-------+-------+---------+
# 4 rows in set (0.00 sec)
# 
# mysql> SELECT Class, COUNT(*) AS Total_Students
#     -> FROM Student
#     -> GROUP BY Class;
# +-------+----------------+
# | Class | Total_Students |
# +-------+----------------+
# |    12 |              3 |
# |    11 |              1 |
# +-------+----------------+
# 2 rows in set (0.00 sec)
# 
# mysql> SELECT Class, MIN(Marks) AS Minimum_Marks
#     -> FROM Student
#     -> GROUP BY Class;
# +-------+---------------+
# | Class | Minimum_Marks |
# +-------+---------------+
# |    12 |            88 |
# |    11 |            78 |
# +-------+---------------+
# 2 rows in set (0.00 sec)
# 
# mysql> SELECT Class, MAX(Marks) AS Maximum_Marks
#     -> FROM Student
#     -> GROUP BY Class;
# +-------+---------------+
# | Class | Maximum_Marks |
# +-------+---------------+
# |    12 |            92 |
# |    11 |            78 |
# +-------+---------------+
# 2 rows in set (0.00 sec)
# 
# mysql> SELECT Class, SUM(Marks) AS Total_Marks
#     -> FROM Student
#     -> GROUP BY Class;
# +-------+-------------+
# | Class | Total_Marks |
# +-------+-------------+
# |    12 |         270 |
# |    11 |          78 |
# +-------+-------------+
# 2 rows in set (0.00 sec)
# 
# mysql> SELECT Class, AVG(Marks) AS Average_Marks
#     -> FROM Student
#     -> GROUP BY Class;
# +-------+---------------+
# | Class | Average_Marks |
# +-------+---------------+
# |    12 |       90.0000 |
# |    11 |       78.0000 |
# +-------+---------------+
# 2 rows in set (0.00 sec)
# 
# mysql>
# 
# ```
# 
# 

# %% [markdown]
# ```
# 1. Create STUDENT Table
# 
# CREATE TABLE Student (
#     Roll_No INT PRIMARY KEY,
#     Name VARCHAR(50),
#     Class INT,
#     Marks INT,
#     Age INT
# );
# 
# 2. Insert Data into STUDENT Table
# 
# INSERT INTO Student VALUES
# (1, 'Aman', 12, 85, 17),
# (2, 'Riya', 12, 92, 18),
# (3, 'Karan', 11, 78, 16),
# (4, 'Neha', 12, 88, 17),
# (5, 'Arjun', 11, 69, 16);
# 
# 3. ALTER TABLE Commands
# (a) Add a New Attribute
# 
# ALTER TABLE Student
# ADD Section CHAR(1);
# 
# (b) Modify Data Type of an Attribute
# 
# ALTER TABLE Student
# MODIFY Name VARCHAR(100);
# 
# (c) Drop an Attribute
# 
# ALTER TABLE Student
# DROP Age;
# 
# 4. UPDATE Table to Modify Data
# 
# UPDATE Student
# SET Marks = 90
# WHERE Roll_No = 1;
# 
# 5. ORDER BY Clause
# (a) Ascending Order (Default)
# 
# SELECT * FROM Student
# ORDER BY Marks;
# 
# (b) Descending Order
# 
# SELECT * FROM Student
# ORDER BY Marks DESC;
# 
# 6. DELETE Tuple(s) from Table
# 
# DELETE FROM Student
# WHERE Marks < 70;
# 
# 7. GROUP BY with Aggregate Functions
# (a) COUNT Students Class-wise
# 
# SELECT Class, COUNT(*) AS Total_Students
# FROM Student
# GROUP BY Class;
# 
# (b) MIN Marks Class-wise
# 
# SELECT Class, MIN(Marks) AS Minimum_Marks
# FROM Student
# GROUP BY Class;
# 
# (c) MAX Marks Class-wise
# 
# SELECT Class, MAX(Marks) AS Maximum_Marks
# FROM Student
# GROUP BY Class;
# 
# (d) SUM of Marks Class-wise
# 
# SELECT Class, SUM(Marks) AS Total_Marks
# FROM Student
# GROUP BY Class;
# 
# (e) AVERAGE Marks Class-wise
# 
# SELECT Class, AVG(Marks) AS Average_Marks
# FROM Student
# GROUP BY Class;
# ```

# %%
import sqlite3

DATABASE_NAME = 'student_database.db'

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            roll_no INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Table 'students' ensured to exist.")

def insert_student():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        cursor.execute("INSERT INTO students (roll_no, name, age, grade) VALUES (?, ?, ?, ?)",
                       (roll_no, name, age, grade))
        conn.commit()
        print(f"Student {name} added successfully.")
    except ValueError:
        print("Invalid input. Roll number and age must be integers.")
    except sqlite3.IntegrityError:
        print(f"Error: Student with Roll Number {roll_no} already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def view_students():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("No students found.")
    else:
        print("\n--- Student Records ---")
        for row in rows:
            print(f"Roll No: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
        print("-----------------------")
    conn.close()

def update_student():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        roll_no = int(input("Enter Roll Number of student to update: "))
        cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
        student = cursor.fetchone()
        if student:
            print(f"Current details for Roll No {roll_no}: Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
            new_name = input(f"Enter new name (leave blank to keep '{student[1]}'): ")
            new_age_str = input(f"Enter new age (leave blank to keep '{student[2]}'): ")
            new_grade = input(f"Enter new grade (leave blank to keep '{student[3]}'): ")

            update_fields = []
            update_values = []

            if new_name:
                update_fields.append("name = ?")
                update_values.append(new_name)
            if new_age_str:
                update_fields.append("age = ?")
                update_values.append(int(new_age_str))
            if new_grade:
                update_fields.append("grade = ?")
                update_values.append(new_grade)

            if update_fields:
                sql = f"UPDATE students SET {', '.join(update_fields)} WHERE roll_no = ?"
                update_values.append(roll_no)
                cursor.execute(sql, tuple(update_values))
                conn.commit()
                print(f"Student with Roll Number {roll_no} updated successfully.")
            else:
                print("No changes made.")
        else:
            print(f"Student with Roll Number {roll_no} not found.")
    except ValueError:
        print("Invalid age input.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def delete_student():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        roll_no = int(input("Enter Roll Number of student to delete: "))
        cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Student with Roll Number {roll_no} deleted successfully.")
        else:
            print(f"Student with Roll Number {roll_no} not found.")
    except ValueError:
        print("Invalid input. Roll number must be an integer.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def main_menu():
    create_table() # Ensure table exists when the program starts
    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Update Student Details")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()


