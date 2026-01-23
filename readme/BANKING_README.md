# 🏦 Banking Management System

## Overview
A secure banking management system built with Python and MySQL. It provides complete functionality for account management, fund transfers, and transaction tracking with PIN-based security.

## Features

### 1. **Account Management**
- Create multiple account types (Savings, Current, Checking)
- Unique account number generation
- 4-digit PIN security
- Account status tracking
- Profile management with email and phone

### 2. **Deposit & Withdrawal**
- Deposit money into account
- Withdraw funds with balance validation
- Real-time balance updates
- Transaction amount validation

### 3. **Fund Transfers**
- Transfer between accounts
- Transfer to external accounts
- Automatic balance updates
- Transfer history tracking

### 4. **Transaction Management**
- Complete transaction history
- Transaction type tracking (Deposit, Withdrawal, Transfer)
- Balance-after recording
- Description for each transaction

### 5. **Account Queries**
- Check balance
- View transaction history
- Account details display
- Statement generation

### 6. **Mini Statement**
- Last 10 transactions
- Quick balance check
- Recent activity summary

## Database Schema

### Tables
```sql
-- Accounts Table
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    account_holder_name VARCHAR(100) NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    pin VARCHAR(4) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Active'
)

-- Transactions Table
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    transaction_type VARCHAR(50) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    balance_after DECIMAL(15, 2),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(200),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
)

-- Transfers Table
CREATE TABLE transfers (
    transfer_id INT AUTO_INCREMENT PRIMARY KEY,
    from_account_id INT NOT NULL,
    to_account_id INT NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(200),
    FOREIGN KEY (from_account_id) REFERENCES accounts(account_id),
    FOREIGN KEY (to_account_id) REFERENCES accounts(account_id)
)

-- Loans Table
CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    loan_amount DECIMAL(15, 2),
    interest_rate FLOAT,
    tenure_months INT,
    loan_status VARCHAR(20),
    disbursement_date DATE,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
)
```

## Main Features in Code

### Key Methods

#### Account Operations
- `create_account()` - Create new account
- `display_account()` - Show account details
- `search_account()` - Find account by number
- `update_account()` - Modify account information
- `close_account()` - Deactivate account

#### Transactions
- `deposit_amount()` - Add funds
- `withdraw_amount()` - Withdraw funds
- `check_balance()` - View current balance
- `view_transactions()` - Show transaction history

#### Transfers
- `transfer_funds()` - Transfer between accounts
- `view_transfer_history()` - Show all transfers
- `verify_transfer()` - Validate transfer details

#### Reports
- `mini_statement()` - Last 10 transactions
- `account_statement()` - Complete statement
- `generate_report()` - Statistical reports

## Installation & Setup

```bash
# 1. Install dependencies
pip install mysql-connector-python

# 2. Ensure MySQL is running
# 3. Create database
mysql -u root -p
CREATE DATABASE mydb;

# 4. Run the system
python banking_management_system.py
```

## Usage

```python
from banking_management_system import *

# Connect to database
connect_database()

# Create account
create_account()
# Output: Account Number: ACC1234567890

# Deposit money
deposit_amount()
# Enter account number and PIN
# Enter amount to deposit

# Withdraw money
withdraw_amount()

# Check balance
check_balance()

# Transfer funds
transfer_funds()

# View transactions
view_transactions()

# Disconnect
disconnect_database()
```

## Menu Options

```
BANKING MANAGEMENT SYSTEM
═════════════════════════════════

1. Account Management
   - Create New Account
   - Display Account Details
   - Search Account
   - Update Account
   - Close Account

2. Transaction Management
   - Deposit Money
   - Withdraw Money
   - Check Balance
   - View Transactions

3. Fund Transfers
   - Transfer Funds
   - View Transfer History
   - Verify Transfer

4. Loan Management
   - Apply for Loan
   - View Loan Status
   - Make Loan Payment

5. Reports
   - Mini Statement
   - Account Statement
   - Monthly Report
   - Annual Report

6. Settings
   - Change PIN
   - Update Profile
   - Contact Details

7. Exit
```

## Security Features

### PIN Protection
- 4-digit PIN for all transactions
- PIN verification required
- No PIN display in console

### Account Validation
- Account number verification
- Balance validation before withdrawal
- Overdraft protection

### Data Protection
- Encrypted database connection
- SQL injection prevention
- Parameterized queries

## Sample Operations

### Create Account
```
Account Holder Name: John Doe
Account Type: Savings
Email: john@example.com
Phone: 9876543210
4-digit PIN: 1234

✓ Account created successfully!
Account Number: ACC1234567890
Account Type: Savings
Account Holder: John Doe
```

### Deposit Money
```
Account Number: ACC1234567890
PIN: 1234
Amount to Deposit: 50000

✓ Deposit successful!
Amount deposited: ₹50,000.00
New balance: ₹50,000.00
```

### Withdraw Money
```
Account Number: ACC1234567890
PIN: 1234
Amount to Withdraw: 10000

✓ Withdrawal successful!
Amount withdrawn: ₹10,000.00
New balance: ₹40,000.00
```

### Transfer Funds
```
From Account Number: ACC1111111111
To Account Number: ACC2222222222
PIN: 1234
Amount: 5000

✓ Transfer successful!
Amount transferred: ₹5,000.00
From Account Balance: ₹35,000.00
To Account: Updated
```

### Check Balance
```
Account Number: ACC1234567890
PIN: 1234

═════════════════════════════════
        ACCOUNT DETAILS
═════════════════════════════════
Account Number: ACC1234567890
Account Holder: John Doe
Account Type: Savings
Balance: ₹40,000.00
Email: john@example.com
Phone: 9876543210
Status: Active
═════════════════════════════════
```

### Mini Statement
```
═════════════════════════════════
        MINI STATEMENT
═════════════════════════════════

Last 10 Transactions:

1. Deposit      | ₹50,000.00  | Balance: ₹50,000.00   | 2026-01-21
2. Withdrawal   | ₹10,000.00  | Balance: ₹40,000.00   | 2026-01-21
3. Transfer     | ₹5,000.00   | Balance: ₹35,000.00   | 2026-01-21
4. Deposit      | ₹15,000.00  | Balance: ₹50,000.00   | 2026-01-21

═════════════════════════════════
```

## Technical Details

| Aspect | Details |
|--------|---------|
| Language | Python 3.7+ |
| Database | MySQL |
| Tables | 4 main tables |
| Security | PIN-based authentication |
| Transactions | Full support with history |
| Data Validation | Input validation implemented |
| Error Handling | Try-catch mechanism |

## Validation Rules

### PIN Validation
- Must be exactly 4 digits
- No special characters
- Numeric only

### Amount Validation
- Must be greater than 0
- Maximum transaction limit
- Minimum balance check

### Account Number Validation
- Format: ACC + 10 digits
- Unique account number
- Case-sensitive

## Error Handling

```python
# Insufficient Balance
Error: Insufficient balance! Current balance: ₹40,000.00

# Invalid PIN
Error: Invalid account number or PIN

# Invalid Amount
Error: Amount must be greater than 0

# Database Connection Error
Error connecting to MySQL: (error details)
```

## Reports Generated

1. **Mini Statement** - Last 10 transactions
2. **Full Statement** - All transactions
3. **Monthly Report** - Monthly transactions summary
4. **Annual Report** - Yearly financial summary
5. **Transfer Report** - All fund transfers
6. **Account Report** - Account details

## Best Practices

1. **Security** - Never share PIN
2. **Verification** - Always verify transfer details
3. **Record Keeping** - Keep transaction records
4. **Regular Checking** - Monitor account regularly
5. **Updates** - Keep profile information current

## Troubleshooting

### Database Connection Error
```
Solution:
- Ensure MySQL server is running
- Verify connection parameters
- Check database existence
```

### Invalid PIN Error
```
Solution:
- Verify PIN is 4 digits
- Check for typos
- Use correct case sensitivity
```

### Insufficient Balance
```
Solution:
- Check current balance
- Reduce withdrawal amount
- Deposit money first
```

## Academic Applications

This system is ideal for:
- Banking system understanding
- Database design
- SQL operations
- Security implementation
- Transaction processing
- Project submission (Class 11/12)

## Future Enhancements

- Online banking interface
- Mobile app
- Investment options
- Insurance products
- Bill payment
- Loan management
- Credit card integration
- Multi-currency support

## License

Educational use - CBSE Computer Science Curriculum

---

**Last Updated**: January 2026

For queries, refer to the code comments or system documentation.
