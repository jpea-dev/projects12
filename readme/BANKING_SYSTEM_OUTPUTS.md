# BANKING MANAGEMENT SYSTEM - SAMPLE OUTPUTS
## Complete Module Outputs Documentation

---

## TABLE OF CONTENTS
1. [Program Initialization](#program-initialization)
2. [Create New Account](#create-new-account)
3. [Display Account Details](#display-account-details)
4. [Deposit Money](#deposit-money)
5. [Withdraw Money](#withdraw-money)
6. [Check Balance](#check-balance)
7. [Transfer Money](#transfer-money)
8. [View Transaction History](#view-transaction-history)
9. [Update Account Information](#update-account-information)
10. [Delete Account](#delete-account)
11. [Admin Login](#admin-login)
12. [Admin Functions](#admin-functions)
13. [Error Handling Examples](#error-handling-examples)

---

## PROGRAM INITIALIZATION

### Output: Program Start

```
==================================================
BANKING MANAGEMENT SYSTEM
==================================================
Initializing...
✓ Connected to database: mydb
✓ Tables created successfully
✓ System ready!

==================================================
BANKING MANAGEMENT SYSTEM
==================================================
1. Create New Account
2. Display Account Details
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. Transfer Money
7. View Transaction History
8. Update Account Information
9. Delete Account
10. Admin Login
11. Exit

Enter your choice (1-11): 
```

---

## CREATE NEW ACCOUNT

### Output: Successful Account Creation

```
==================================================
CREATE NEW ACCOUNT
==================================================
Enter account holder name: Rajesh Kumar
Enter email: rajesh@bank.com
Enter phone number: 9876543210
Set 4-digit PIN: 1234

Account Types:
1. Savings
2. Current
3. Checking
Select account type (1-3): 1

✓ Account created successfully!
Account Number: ACC1705859123456
Account Type: Savings
Account Holder: Rajesh Kumar

==================================================
```

### Output: Alternative Successful Creation

```
==================================================
CREATE NEW ACCOUNT
==================================================
Enter account holder name: Priya Sharma
Enter email: priya@bank.com
Enter phone number: 9123456789
Set 4-digit PIN: 5678

Account Types:
1. Savings
2. Current
3. Checking
Select account type (1-3): 2

✓ Account created successfully!
Account Number: ACC1705859234567
Account Type: Current
Account Holder: Priya Sharma

==================================================
```

### Output: Error - Invalid PIN

```
==================================================
CREATE NEW ACCOUNT
==================================================
Enter account holder name: Arjun Singh
Enter email: arjun@bank.com
Enter phone number: 8765432109
Set 4-digit PIN: 12

✗ PIN must be 4 digits
```

### Output: Error - Empty Name

```
==================================================
CREATE NEW ACCOUNT
==================================================
Enter account holder name: 

✗ Name cannot be empty
```

---

## DISPLAY ACCOUNT DETAILS

### Output: Valid Account Display

```
==================================================
DISPLAY ACCOUNT DETAILS
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234

==================================================
ACCOUNT DETAILS
==================================================
Account Number: ACC1705859123456
Account Holder: Rajesh Kumar
Account Type: Savings
Balance: ₹50000.00
Email: rajesh@bank.com
Phone: 9876543210
Creation Date: 2024-01-21 10:30:45
Status: Active
==================================================
```

### Output: Invalid Credentials

```
==================================================
DISPLAY ACCOUNT DETAILS
==================================================
Enter account number: ACC1705859123456
Enter PIN: 9999

✗ Invalid account number or PIN
```

---

## DEPOSIT MONEY

### Output: Successful Deposit

```
==================================================
DEPOSIT MONEY
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234
Enter amount to deposit: 25000

✓ Deposit successful!
Amount deposited: ₹25000.00
New balance: ₹75000.00
```

### Output: Another Successful Deposit

```
==================================================
DEPOSIT MONEY
==================================================
Enter account number: ACC1705859234567
Enter PIN: 5678
Enter amount to deposit: 100000

✓ Deposit successful!
Amount deposited: ₹100000.00
New balance: ₹100000.00
```

### Output: Error - Negative Amount

```
==================================================
DEPOSIT MONEY
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234
Enter amount to deposit: -5000

✗ Amount must be greater than 0
```

### Output: Error - Invalid Amount Format

```
==================================================
DEPOSIT MONEY
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234
Enter amount to deposit: abc

✗ Invalid amount entered
```

---

## WITHDRAW MONEY

### Output: Successful Withdrawal

```
==================================================
WITHDRAW MONEY
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234
Enter amount to withdraw: 15000

✓ Withdrawal successful!
Amount withdrawn: ₹15000.00
New balance: ₹60000.00
```

### Output: Another Successful Withdrawal

```
==================================================
WITHDRAW MONEY
==================================================
Enter account number: ACC1705859234567
Enter PIN: 5678
Enter amount to withdraw: 50000

✓ Withdrawal successful!
Amount withdrawn: ₹50000.00
New balance: ₹50000.00
```

### Output: Error - Insufficient Balance

```
==================================================
WITHDRAW MONEY
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234
Enter amount to withdraw: 100000

✗ Insufficient balance! Current balance: ₹60000.00
```

### Output: Error - Invalid PIN

```
==================================================
WITHDRAW MONEY
==================================================
Enter account number: ACC1705859123456
Enter PIN: 9999
Enter amount to withdraw: 5000

✗ Invalid account number or PIN
```

---

## CHECK BALANCE

### Output: Successful Balance Check

```
==================================================
CHECK BALANCE
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234

✓ Account Holder: Rajesh Kumar
Current Balance: ₹60000.00
```

### Output: Another Balance Check

```
==================================================
CHECK BALANCE
==================================================
Enter account number: ACC1705859234567
Enter PIN: 5678

✓ Account Holder: Priya Sharma
Current Balance: ₹50000.00
```

### Output: Error - Invalid Credentials

```
==================================================
CHECK BALANCE
==================================================
Enter account number: ACC1705859123456
Enter PIN: 0000

✗ Invalid account number or PIN
```

---

## TRANSFER MONEY

### Output: Successful Transfer

```
==================================================
TRANSFER MONEY
==================================================
Enter your account number: ACC1705859123456
Enter your PIN: 1234
Enter recipient account number: ACC1705859234567
Enter amount to transfer: 20000

✓ Transfer successful!
Amount transferred: ₹20000.00
Your new balance: ₹40000.00
```

### Output: Another Successful Transfer

```
==================================================
TRANSFER MONEY
==================================================
Enter your account number: ACC1705859234567
Enter your PIN: 5678
Enter recipient account number: ACC1705859123456
Enter amount to transfer: 15000

✓ Transfer successful!
Amount transferred: ₹15000.00
Your new balance: ₹35000.00
```

### Output: Error - Invalid Sender PIN

```
==================================================
TRANSFER MONEY
==================================================
Enter your account number: ACC1705859123456
Enter your PIN: 0000
Enter recipient account number: ACC1705859234567
Enter amount to transfer: 20000

✗ Invalid sender account or PIN
```

### Output: Error - Invalid Recipient Account

```
==================================================
TRANSFER MONEY
==================================================
Enter your account number: ACC1705859123456
Enter your PIN: 1234
Enter recipient account number: ACC9999999999
Enter amount to transfer: 20000

✗ Invalid recipient account
```

### Output: Error - Insufficient Balance

```
==================================================
TRANSFER MONEY
==================================================
Enter your account number: ACC1705859123456
Enter your PIN: 1234
Enter recipient account number: ACC1705859234567
Enter amount to transfer: 500000

✗ Insufficient balance! Current balance: ₹40000.00
```

### Output: Error - Negative Amount

```
==================================================
TRANSFER MONEY
==================================================
Enter your account number: ACC1705859123456
Enter your PIN: 1234
Enter recipient account number: ACC1705859234567
Enter amount to transfer: -10000

✗ Amount must be greater than 0
```

---

## VIEW TRANSACTION HISTORY

### Output: Successful Transaction History

```
==================================================
TRANSACTION HISTORY
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234

Last 10 Transactions:
────────────────────────────────────────────────────────────────────────────────────────────────────
ID    Type            Amount       Balance      Date                 Description               
────────────────────────────────────────────────────────────────────────────────────────────────────
15    Transfer Out    ₹20000.00    ₹40000.00    2024-01-21 15:45:30  Transfer to ACC1705859234567
14    Deposit         ₹25000.00    ₹60000.00    2024-01-21 15:30:15  Cash Deposit              
13    Transfer Out    ₹15000.00    ₹35000.00    2024-01-21 15:15:45  Transfer to ACC1705859234567
12    Transfer In     ₹15000.00    ₹50000.00    2024-01-21 15:10:20  Transfer from ACC1705859234567
11    Withdrawal      ₹10000.00    ₹35000.00    2024-01-21 14:50:00  Cash Withdrawal           
10    Deposit         ₹50000.00    ₹45000.00    2024-01-21 14:30:10  Cash Deposit              
9     Withdrawal      ₹5000.00     ₹-5000.00    2024-01-21 14:15:25  Cash Withdrawal           
8     Transfer Out    ₹25000.00    ₹0.00        2024-01-21 13:45:40  Transfer to ACC1705859234567
────────────────────────────────────────────────────────────────────────────────────────────────────
```

### Output: Another Transaction History

```
==================================================
TRANSACTION HISTORY
==================================================
Enter account number: ACC1705859234567
Enter PIN: 5678

Last 10 Transactions:
────────────────────────────────────────────────────────────────────────────────────────────────────
ID    Type            Amount       Balance      Date                 Description               
────────────────────────────────────────────────────────────────────────────────────────────────────
12    Transfer Out    ₹15000.00    ₹35000.00    2024-01-21 15:50:30  Transfer to ACC1705859123456
11    Deposit         ₹100000.00   ₹50000.00    2024-01-21 15:35:00  Cash Deposit              
10    Transfer In     ₹20000.00    ₹-50000.00   2024-01-21 15:45:30  Transfer from ACC1705859123456
9     Withdrawal      ₹50000.00    ₹-70000.00   2024-01-21 15:25:15  Cash Withdrawal           
────────────────────────────────────────────────────────────────────────────────────────────────────
```

### Output: Error - No Transactions

```
==================================================
TRANSACTION HISTORY
==================================================
Enter account number: ACC1705859300000
Enter PIN: 4321

✗ No transactions found
```

### Output: Error - Invalid Credentials

```
==================================================
TRANSACTION HISTORY
==================================================
Enter account number: ACC1705859123456
Enter PIN: 0000

✗ Invalid account number or PIN
```

---

## UPDATE ACCOUNT INFORMATION

### Output: Update Email

```
==================================================
UPDATE ACCOUNT INFORMATION
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234

What do you want to update?
1. Email
2. Phone
3. PIN

Enter your choice (1-3): 1
Enter new email: rajesh.kumar@newbank.com
✓ Email updated successfully
```

### Output: Update Phone

```
==================================================
UPDATE ACCOUNT INFORMATION
==================================================
Enter account number: ACC1705859234567
Enter PIN: 5678

What do you want to update?
1. Email
2. Phone
3. PIN

Enter your choice (1-3): 2
Enter new phone: 9988776655
✓ Phone updated successfully
```

### Output: Update PIN

```
==================================================
UPDATE ACCOUNT INFORMATION
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234

What do you want to update?
1. Email
2. Phone
3. PIN

Enter your choice (1-3): 3
Enter new 4-digit PIN: 9876
✓ PIN updated successfully
```

### Output: Error - Invalid PIN Format

```
==================================================
UPDATE ACCOUNT INFORMATION
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234

What do you want to update?
1. Email
2. Phone
3. PIN

Enter your choice (1-3): 3
Enter new 4-digit PIN: 12

✗ PIN must be 4 digits
```

### Output: Error - Invalid Choice

```
==================================================
UPDATE ACCOUNT INFORMATION
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234

What do you want to update?
1. Email
2. Phone
3. PIN

Enter your choice (1-3): 5

✗ Invalid choice
```

---

## DELETE ACCOUNT

### Output: Successful Account Deletion

```
==================================================
DELETE ACCOUNT
==================================================
Enter account number: ACC1705859300000
Enter PIN: 4321
Are you sure you want to delete this account? (yes/no): yes

✓ Account deleted successfully
```

### Output: Deletion Cancelled

```
==================================================
DELETE ACCOUNT
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234
Are you sure you want to delete this account? (yes/no): no

✗ Account deletion cancelled
```

### Output: Error - Balance Remaining

```
==================================================
DELETE ACCOUNT
==================================================
Enter account number: ACC1705859123456
Enter PIN: 1234
Are you sure you want to delete this account? (yes/no): yes

✗ Cannot delete account with balance. Current balance: ₹40000.00
Please withdraw your balance first.
```

### Output: Error - Invalid Credentials

```
==================================================
DELETE ACCOUNT
==================================================
Enter account number: ACC1705859999999
Enter PIN: 0000
Are you sure you want to delete this account? (yes/no): yes

✗ Invalid account number or PIN
```

---

## ADMIN LOGIN

### Output: Successful Admin Login

```
==================================================
ADMIN LOGIN
==================================================
Enter username: admin
Enter password: 

✓ Admin login successful!

==================================================
ADMIN MENU
==================================================
1. View All Accounts
2. View All Transactions
3. View Account Details
4. Delete Account (Force)
5. Back to Main Menu

Enter your choice (1-5): 
```

### Output: Failed Admin Login - Wrong Username

```
==================================================
ADMIN LOGIN
==================================================
Enter username: administrator
Enter password: 

✗ Invalid username or password
```

### Output: Failed Admin Login - Wrong Password

```
==================================================
ADMIN LOGIN
==================================================
Enter username: admin
Enter password: 

✗ Invalid username or password
```

---

## ADMIN FUNCTIONS

### Output 1: View All Accounts

```
==================================================
ALL ACCOUNTS (ADMIN VIEW)
==================================================

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
ID    Account #       Holder Name          Type         Balance             Status     Date                
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
1     ACC1705859123456 Rajesh Kumar         Savings      ₹40000.00           Active     2024-01-21 10:30:45 
2     ACC1705859234567 Priya Sharma         Current      ₹35000.00           Active     2024-01-21 11:15:30 
3     ACC1705859345678 Arjun Singh          Checking     ₹75000.00           Active     2024-01-21 12:00:15 
4     ACC1705859456789 Neha Patel           Savings      ₹120000.00          Active     2024-01-21 13:45:00 
5     ACC1705859567890 Vikram Reddy         Current      ₹85000.00           Active     2024-01-21 14:20:30 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Total Accounts: 5
```

### Output 2: View All Transactions

```
==================================================
ALL TRANSACTIONS (ADMIN VIEW)
==================================================

Last 20 Transactions:
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
ID    Account         Type            Amount       Balance      Date                 Description               
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
30    ACC1705859567890 Transfer Out    ₹15000.00    ₹70000.00    2024-01-21 16:00:00  Transfer to ACC1705859345678
29    ACC1705859345678 Transfer In     ₹15000.00    ₹90000.00    2024-01-21 16:00:00  Transfer from ACC1705859567890
28    ACC1705859123456 Transfer Out    ₹20000.00    ₹40000.00    2024-01-21 15:45:30  Transfer to ACC1705859234567
27    ACC1705859234567 Transfer In     ₹20000.00    ₹55000.00    2024-01-21 15:45:30  Transfer from ACC1705859123456
26    ACC1705859456789 Deposit         ₹50000.00    ₹120000.00   2024-01-21 15:30:00  Cash Deposit              
25    ACC1705859123456 Withdrawal      ₹10000.00    ₹60000.00    2024-01-21 15:20:15  Cash Withdrawal           
24    ACC1705859234567 Deposit         ₹40000.00    ₹35000.00    2024-01-21 15:10:45  Cash Deposit              
23    ACC1705859345678 Withdrawal      ₹15000.00    ₹75000.00    2024-01-21 14:55:30  Cash Withdrawal           
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

### Output 3: View Account Details (Admin)

```
==================================================
ADMIN MENU
==================================================
1. View All Accounts
2. View All Transactions
3. View Account Details
4. Delete Account (Force)
5. Back to Main Menu

Enter your choice (1-5): 3
Enter account number: ACC1705859123456

==================================================
ACCOUNT DETAILS
==================================================
Account Number: ACC1705859123456
Holder: Rajesh Kumar
Type: Savings
Balance: ₹40000.00
Email: rajesh.kumar@newbank.com
Phone: 9876543210
Created: 2024-01-21 10:30:45
Status: Active
```

### Output 4: Force Delete Account (Admin)

```
==================================================
ADMIN MENU
==================================================
1. View All Accounts
2. View All Transactions
3. View Account Details
4. Delete Account (Force)
5. Back to Main Menu

Enter your choice (1-5): 4
Enter account number: ACC1705859300000
Force delete this account? (yes/no): yes

✓ Account force deleted
```

### Output 5: Back to Main Menu

```
==================================================
ADMIN MENU
==================================================
1. View All Accounts
2. View All Transactions
3. View Account Details
4. Delete Account (Force)
5. Back to Main Menu

Enter your choice (1-5): 5

==================================================
BANKING MANAGEMENT SYSTEM
==================================================
1. Create New Account
2. Display Account Details
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. Transfer Money
7. View Transaction History
8. Update Account Information
9. Delete Account
10. Admin Login
11. Exit

Enter your choice (1-11): 
```

---

## ERROR HANDLING EXAMPLES

### Error 1: Invalid Menu Choice

```
==================================================
BANKING MANAGEMENT SYSTEM
==================================================
1. Create New Account
2. Display Account Details
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. Transfer Money
7. View Transaction History
8. Update Account Information
9. Delete Account
10. Admin Login
11. Exit

Enter your choice (1-11): 15

✗ Invalid choice. Please try again.
```

### Error 2: Invalid Account Type Selection

```
==================================================
CREATE NEW ACCOUNT
==================================================
Enter account holder name: Test User
Enter email: test@bank.com
Enter phone number: 9999999999
Set 4-digit PIN: 1111

Account Types:
1. Savings
2. Current
3. Checking
Select account type (1-3): 5

✗ Invalid account type
```

### Error 3: Database Connection Error

```
==================================================
BANKING MANAGEMENT SYSTEM
==================================================
Initializing...
✗ Connected to database: mydb
✗ Database connection failed

✗ Failed to initialize the system. Please check your database connection.
```

### Error 4: Transaction Not Found

```
==================================================
TRANSACTION HISTORY
==================================================
Enter account number: ACC1705859200000
Enter PIN: 1111

✗ No transactions found
```

### Error 5: Empty Name Field

```
==================================================
CREATE NEW ACCOUNT
==================================================
Enter account holder name: 

✗ Name cannot be empty
```

---

## PROGRAM EXIT

### Output: Program Termination

```
==================================================
BANKING MANAGEMENT SYSTEM
==================================================
1. Create New Account
2. Display Account Details
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. Transfer Money
7. View Transaction History
8. Update Account Information
9. Delete Account
10. Admin Login
11. Exit

Enter your choice (1-11): 11

✓ Thank you for using Banking Management System
✓ Have a great day!
✓ Database connection closed
```

---

## COMPLETE USER SESSION EXAMPLE

### Scenario: New Customer Creating Account and Performing Transactions

```
==================================================
BANKING MANAGEMENT SYSTEM
==================================================
Initializing...
✓ Connected to database: mydb
✓ Tables created successfully
✓ System ready!

==================================================
BANKING MANAGEMENT SYSTEM
==================================================
1. Create New Account
2. Display Account Details
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. Transfer Money
7. View Transaction History
8. Update Account Information
9. Delete Account
10. Admin Login
11. Exit

Enter your choice (1-11): 1

==================================================
CREATE NEW ACCOUNT
==================================================
Enter account holder name: Rohit Patel
Enter email: rohit@bank.com
Enter phone number: 9876543210
Set 4-digit PIN: 5432

Account Types:
1. Savings
2. Current
3. Checking
Select account type (1-3): 1

✓ Account created successfully!
Account Number: ACC1705859111111
Account Type: Savings
Account Holder: Rohit Patel

==================================================
BANKING MANAGEMENT SYSTEM
==================================================
...
Enter your choice (1-11): 3

==================================================
DEPOSIT MONEY
==================================================
Enter account number: ACC1705859111111
Enter PIN: 5432
Enter amount to deposit: 100000

✓ Deposit successful!
Amount deposited: ₹100000.00
New balance: ₹100000.00

==================================================
BANKING MANAGEMENT SYSTEM
==================================================
...
Enter your choice (1-11): 5

==================================================
CHECK BALANCE
==================================================
Enter account number: ACC1705859111111
Enter PIN: 5432

✓ Account Holder: Rohit Patel
Current Balance: ₹100000.00

==================================================
BANKING MANAGEMENT SYSTEM
==================================================
...
Enter your choice (1-11): 7

==================================================
TRANSACTION HISTORY
==================================================
Enter account number: ACC1705859111111
Enter PIN: 5432

Last 10 Transactions:
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
ID    Type            Amount       Balance      Date                 Description               
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
1     Deposit         ₹100000.00   ₹100000.00   2024-01-21 17:00:00  Cash Deposit              
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

==================================================
BANKING MANAGEMENT SYSTEM
==================================================
...
Enter your choice (1-11): 8

==================================================
UPDATE ACCOUNT INFORMATION
==================================================
Enter account number: ACC1705859111111
Enter PIN: 5432

What do you want to update?
1. Email
2. Phone
3. PIN

Enter your choice (1-3): 1
Enter new email: rohit.patel@newbank.com
✓ Email updated successfully

==================================================
BANKING MANAGEMENT SYSTEM
==================================================
...
Enter your choice (1-11): 11

✓ Thank you for using Banking Management System
✓ Have a great day!
✓ Database connection closed
```

---

## SUMMARY OF MODULE OUTPUTS

| Module | Output Type | Status Code |
|--------|------------|-------------|
| Create Account | Success | ✓ |
| Display Details | Success | ✓ |
| Deposit Money | Success | ✓ |
| Withdraw Money | Success | ✓ |
| Check Balance | Success | ✓ |
| Transfer Money | Success | ✓ |
| View History | Success | ✓ |
| Update Info | Success | ✓ |
| Delete Account | Success | ✓ |
| Admin Login | Success | ✓ |
| Error Handling | Error | ✗ |

---

## DATABASE SCHEMA (Referenced in Outputs)

### Accounts Table Structure
```
account_id | account_holder_name | account_type | balance | account_number | pin | email | phone | creation_date | status
```

### Transactions Table Structure
```
transaction_id | account_id | transaction_type | amount | balance_after | transaction_date | description
```

### Transfers Table Structure
```
transfer_id | from_account_id | to_account_id | amount | transfer_date | description
```

---

**Document Version:** 1.0  
**Created:** January 2026  
**Purpose:** Sample outputs for all Banking Management System modules  
**Status:** Complete ✓
