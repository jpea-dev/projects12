
#### 1. Database Connection Module
- `connect_database()` - Establish MySQL connection
- `disconnect_database()` - Close database connection
- `create_tables()` - Create necessary database tables

#### 2. Account Management Module
- `generate_account_number()` - Generate unique account ID
- `create_account()` - Create new bank account
- `display_account()` - Show account details
- `update_account_info()` - Update email, phone, or PIN
- `delete_account()` - Delete/close account

#### 3. Transaction Module
- `deposit_amount()` - Process deposits
- `withdraw_amount()` - Process withdrawals with balance check
- `check_balance()` - View account balance
- `view_transaction_history()` - View last 10 transactions

#### 4. Transfer Module
- `transfer_amount()` - Transfer money between accounts
- Automatic balance updates for both accounts
- Transaction logging for both sender and receiver

#### 5. Admin Module
- `admin_login()` - Admin authentication
- `admin_menu()` - Admin operations menu
- `view_all_accounts()` - List all accounts
- `view_all_transactions()` - View all transactions

## Database Schema

### Accounts Table
```
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    account_holder_name VARCHAR(100),
    account_type VARCHAR(50),
    balance DECIMAL(15, 2),
    account_number VARCHAR(20) UNIQUE,
    pin VARCHAR(4),
    email VARCHAR(100),
    phone VARCHAR(15),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Active'
)
```

### Transactions Table
```
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    transaction_type VARCHAR(50),
    amount DECIMAL(15, 2),
    balance_after DECIMAL(15, 2),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(200),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
)
```

### Transfers Table
```
CREATE TABLE transfers (
    transfer_id INT AUTO_INCREMENT PRIMARY KEY,
    from_account_id INT NOT NULL,
    to_account_id INT NOT NULL,
    amount DECIMAL(15, 2),
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(200),
    FOREIGN KEY (from_account_id) REFERENCES accounts(account_id),
    FOREIGN KEY (to_account_id) REFERENCES accounts(account_id)
)
```

## Usage Examples

### Creating an Account
```
Enter choice: 1
Enter account holder name: John Doe
Select account type (1-3): 1 (for Savings)
Enter email: john@example.com
Enter phone number: 9876543210
Set 4-digit PIN: 1234
```

### Depositing Money
```
Enter choice: 3
Enter account number: ACC1234567890
Enter PIN: 1234
Enter amount to deposit: 5000
```

### Withdrawing Money
```
Enter choice: 4
Enter account number: ACC1234567890
Enter PIN: 1234
Enter amount to withdraw: 2000
```

### Transferring Money
```
Enter choice: 6
Enter your account number: ACC1234567890
Enter your PIN: 1234
Enter recipient account number: ACC9876543210
Enter amount to transfer: 1000
```

### Admin Login
```
Enter choice: 10
Enter username: admin
Enter password: admin123
```

## Account Types Supported

1. **Savings Account** - For regular savings with emphasis on accumulating funds
2. **Current Account** - For frequent business transactions
3. **Checking Account** - Standard checking account for everyday banking

## Security Features

1. **PIN Authentication** - 4-digit PIN for all account operations
2. **Password Protected Admin** - Admin access requires username and password
3. **Balance Verification** - Withdrawal and transfer operations verify sufficient balance
4. **Unique Account Numbers** - Auto-generated unique account numbers
5. **Transaction Logging** - All transactions are logged with timestamps

## Error Handling

The system includes comprehensive error handling for:
- Invalid PIN/Account Number combinations
- Insufficient balance for withdrawals
- Invalid data entry (non-numeric amounts)
- Database connection errors
- Duplicate account numbers
- Invalid account types

## Troubleshooting

### Connection Error: "Can't connect to MySQL server"
1. Verify MySQL Server is running
2. Check credentials: user=root, password=1234, host=localhost
3. Ensure database 'mydb' exists

### Package Import Error: "No module named 'mysql'"
```bash
pip install mysql-connector-python
```

### PIN Authentication Failed
- Ensure you enter exactly 4 digits
- Check that account number is correct
- Verify case sensitivity (if any)

## Future Enhancements

- Email notifications for transactions
- Account interest calculation
- Loan management system
- Online bill payment module
- Mobile app integration
- Advanced reporting and analytics
- SMS notifications
- Multi-currency support
- Investment options
- Customer support ticket system

## Code Structure

```
banking_management_system.py
├── Database Configuration
├── Database Connection Functions
│   ├── connect_database()
│   ├── disconnect_database()
│   └── create_tables()
├── Account Management Module
│   ├── create_account()
│   ├── display_account()
│   ├── update_account_info()
│   └── delete_account()
├── Transaction Module
│   ├── deposit_amount()
│   ├── withdraw_amount()
│   ├── check_balance()
│   └── view_transaction_history()
├── Transfer Module
│   └── transfer_amount()
├── Admin Module
│   ├── admin_login()
│   ├── admin_menu()
│   ├── view_all_accounts()
│   ├── view_all_transactions()
│   └── [Admin operations]
└── Main Menu
    └── main_menu()
```

## Testing the System

### Test Case 1: Create Account
1. Run the application
2. Choose option 1 (Create New Account)
3. Fill in the required details
4. Verify account is created successfully

### Test Case 2: Deposit and Withdraw
1. Create an account
2. Choose option 3 (Deposit Money)
3. Enter valid amount
4. Choose option 4 (Withdraw Money)
5. Verify balance updates correctly

### Test Case 3: Transfer Money
1. Create two accounts
2. Deposit money in first account
3. Choose option 6 (Transfer Money)
4. Transfer between accounts
5. Verify both balances updated

### Test Case 4: Admin Functions
1. Choose option 10 (Admin Login)
2. Login with admin/admin123
3. View all accounts and transactions
4. Verify admin operations work correctly

## Support

For issues or questions, please ensure:
- MySQL is running properly
- All packages are installed correctly
- Database credentials are accurate
- Python version is 3.6 or higher


---

**Version**: 1.0  
**Last Updated**: January 2026  
**Status**: Production Ready
