import mysql.connector
from mysql.connector import Error
from datetime import datetime
import getpass
import time

# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'mydb'
}

# Global connection variable
connection = None

# ====================== DATABASE CONNECTION FUNCTIONS ======================

def connect_database():
    """Establish connection to MySQL database"""
    global connection
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            print(f"✓ Connected to database: {db_name[0]}")
            cursor.close()
            return True
    except Error as e:
        print(f"✗ Error connecting to MySQL: {e}")
        return False

def disconnect_database():
    """Close database connection"""
    global connection
    if connection and connection.is_connected():
        connection.close()
        print("✓ Database connection closed")

def create_tables():
    """Create necessary tables for Banking Management System"""
    try:
        cursor = connection.cursor()
        
        # Create Accounts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
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
        """)
        
        # Create Transactions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                account_id INT NOT NULL,
                transaction_type VARCHAR(50) NOT NULL,
                amount DECIMAL(15, 2) NOT NULL,
                balance_after DECIMAL(15, 2),
                transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                description VARCHAR(200),
                FOREIGN KEY (account_id) REFERENCES accounts(account_id)
            )
        """)
        
        # Create Transfers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transfers (
                transfer_id INT AUTO_INCREMENT PRIMARY KEY,
                from_account_id INT NOT NULL,
                to_account_id INT NOT NULL,
                amount DECIMAL(15, 2) NOT NULL,
                transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                description VARCHAR(200),
                FOREIGN KEY (from_account_id) REFERENCES accounts(account_id),
                FOREIGN KEY (to_account_id) REFERENCES accounts(account_id)
            )
        """)
        
        connection.commit()
        print("✓ Tables created successfully")
    except Error as e:
        print(f"✗ Error creating tables: {e}")

# ====================== ACCOUNT MANAGEMENT FUNCTIONS ======================

def generate_account_number():
    """Generate unique account number"""
    timestamp = str(int(datetime.now().timestamp() * 1000))
    return "ACC" + timestamp[-10:]

def create_account():
    """Create a new bank account"""
    print("\n" + "="*50)
    print("CREATE NEW ACCOUNT")
    print("="*50)
    
    try:
        name = input("Enter account holder name: ").strip()
        if not name:
            print("✗ Name cannot be empty")
            return
        
        print("\nAccount Types:")
        print("1. Savings")
        print("2. Current")
        print("3. Checking")
        account_type = input("Select account type (1-3): ").strip()
        
        types = {'1': 'Savings', '2': 'Current', '3': 'Checking'}
        if account_type not in types:
            print("✗ Invalid account type")
            return
        
        email = input("Enter email: ").strip()
        phone = input("Enter phone number: ").strip()
        pin = input("Set 4-digit PIN: ").strip()
        
        if len(pin) != 4 or not pin.isdigit():
            print("✗ PIN must be 4 digits")
            return
        
        account_number = generate_account_number()
        
        cursor = connection.cursor()
        query = """
            INSERT INTO accounts (account_holder_name, account_type, account_number, pin, email, phone, balance)
            VALUES (%s, %s, %s, %s, %s, %s, 0.00)
        """
        cursor.execute(query, (name, types[account_type], account_number, pin, email, phone))
        connection.commit()
        
        print("\n✓ Account created successfully!")
        print(f"Account Number: {account_number}")
        print(f"Account Type: {types[account_type]}")
        print(f"Account Holder: {name}")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error creating account: {e}")

def display_account():
    """Display account details"""
    print("\n" + "="*50)
    print("DISPLAY ACCOUNT DETAILS")
    print("="*50)
    
    try:
        account_number = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()
        
        cursor = connection.cursor()
        cursor.execute("""
            SELECT account_id, account_holder_name, account_type, balance, email, phone, creation_date, status
            FROM accounts WHERE account_number = %s AND pin = %s
        """, (account_number, pin))
        
        account = cursor.fetchone()
        if account:
            print("\n" + "="*50)
            print("ACCOUNT DETAILS")
            print("="*50)
            print(f"Account Number: {account_number}")
            print(f"Account Holder: {account[1]}")
            print(f"Account Type: {account[2]}")
            print(f"Balance: ₹{account[3]:.2f}")
            print(f"Email: {account[4]}")
            print(f"Phone: {account[5]}")
            print(f"Creation Date: {account[6]}")
            print(f"Status: {account[7]}")
            print("="*50)
        else:
            print("✗ Invalid account number or PIN")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error displaying account: {e}")

def deposit_amount():
    """Deposit money into account"""
    print("\n" + "="*50)
    print("DEPOSIT MONEY")
    print("="*50)
    
    try:
        account_number = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()
        amount = float(input("Enter amount to deposit: "))
        
        if amount <= 0:
            print("✗ Amount must be greater than 0")
            return
        
        cursor = connection.cursor()
        cursor.execute("""
            SELECT account_id, balance FROM accounts WHERE account_number = %s AND pin = %s
        """, (account_number, pin))
        
        account = cursor.fetchone()
        if account:
            account_id = account[0]
            new_balance = account[1] + amount
            
            cursor.execute("""
                UPDATE accounts SET balance = %s WHERE account_id = %s
            """, (new_balance, account_id))
            
            cursor.execute("""
                INSERT INTO transactions (account_id, transaction_type, amount, balance_after, description)
                VALUES (%s, %s, %s, %s, %s)
            """, (account_id, 'Deposit', amount, new_balance, 'Cash Deposit'))
            
            connection.commit()
            print(f"\n✓ Deposit successful!")
            print(f"Amount deposited: ₹{amount:.2f}")
            print(f"New balance: ₹{new_balance:.2f}")
        else:
            print("✗ Invalid account number or PIN")
        
        cursor.close()
    except ValueError:
        print("✗ Invalid amount entered")
    except Error as e:
        print(f"✗ Error depositing amount: {e}")

def withdraw_amount():
    """Withdraw money from account"""
    print("\n" + "="*50)
    print("WITHDRAW MONEY")
    print("="*50)
    
    try:
        account_number = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()
        amount = float(input("Enter amount to withdraw: "))
        
        if amount <= 0:
            print("✗ Amount must be greater than 0")
            return
        
        cursor = connection.cursor()
        cursor.execute("""
            SELECT account_id, balance FROM accounts WHERE account_number = %s AND pin = %s
        """, (account_number, pin))
        
        account = cursor.fetchone()
        if account:
            account_id = account[0]
            current_balance = account[1]
            
            if current_balance >= amount:
                new_balance = current_balance - amount
                
                cursor.execute("""
                    UPDATE accounts SET balance = %s WHERE account_id = %s
                """, (new_balance, account_id))
                
                cursor.execute("""
                    INSERT INTO transactions (account_id, transaction_type, amount, balance_after, description)
                    VALUES (%s, %s, %s, %s, %s)
                """, (account_id, 'Withdrawal', amount, new_balance, 'Cash Withdrawal'))
                
                connection.commit()
                print(f"\n✓ Withdrawal successful!")
                print(f"Amount withdrawn: ₹{amount:.2f}")
                print(f"New balance: ₹{new_balance:.2f}")
            else:
                print(f"✗ Insufficient balance! Current balance: ₹{current_balance:.2f}")
        else:
            print("✗ Invalid account number or PIN")
        
        cursor.close()
    except ValueError:
        print("✗ Invalid amount entered")
    except Error as e:
        print(f"✗ Error withdrawing amount: {e}")

def check_balance():
    """Check account balance"""
    print("\n" + "="*50)
    print("CHECK BALANCE")
    print("="*50)
    
    try:
        account_number = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()
        
        cursor = connection.cursor()
        cursor.execute("""
            SELECT balance, account_holder_name FROM accounts WHERE account_number = %s AND pin = %s
        """, (account_number, pin))
        
        account = cursor.fetchone()
        if account:
            print(f"\n✓ Account Holder: {account[1]}")
            print(f"Current Balance: ₹{account[0]:.2f}")
        else:
            print("✗ Invalid account number or PIN")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error checking balance: {e}")

def transfer_amount():
    """Transfer money between accounts"""
    print("\n" + "="*50)
    print("TRANSFER MONEY")
    print("="*50)
    
    try:
        from_account = input("Enter your account number: ").strip()
        pin = input("Enter your PIN: ").strip()
        to_account = input("Enter recipient account number: ").strip()
        amount = float(input("Enter amount to transfer: "))
        
        if amount <= 0:
            print("✗ Amount must be greater than 0")
            return
        
        cursor = connection.cursor()
        
        # Verify sender account
        cursor.execute("""
            SELECT account_id, balance FROM accounts WHERE account_number = %s AND pin = %s
        """, (from_account, pin))
        
        sender = cursor.fetchone()
        
        # Verify recipient account
        cursor.execute("""
            SELECT account_id, balance FROM accounts WHERE account_number = %s
        """, (to_account,))
        
        receiver = cursor.fetchone()
        
        if not sender:
            print("✗ Invalid sender account or PIN")
        elif not receiver:
            print("✗ Invalid recipient account")
        elif sender[1] < amount:
            print(f"✗ Insufficient balance! Current balance: ₹{sender[1]:.2f}")
        else:
            # Perform transfer
            sender_id = sender[0]
            receiver_id = receiver[0]
            sender_new_balance = sender[1] - amount
            receiver_new_balance = receiver[1] + amount
            
            # Update sender balance
            cursor.execute("""
                UPDATE accounts SET balance = %s WHERE account_id = %s
            """, (sender_new_balance, sender_id))
            
            # Update receiver balance
            cursor.execute("""
                UPDATE accounts SET balance = %s WHERE account_id = %s
            """, (receiver_new_balance, receiver_id))
            
            # Record transfer
            cursor.execute("""
                INSERT INTO transfers (from_account_id, to_account_id, amount, description)
                VALUES (%s, %s, %s, %s)
            """, (sender_id, receiver_id, amount, f'Transfer to {to_account}'))
            
            # Record transaction for sender
            cursor.execute("""
                INSERT INTO transactions (account_id, transaction_type, amount, balance_after, description)
                VALUES (%s, %s, %s, %s, %s)
            """, (sender_id, 'Transfer Out', amount, sender_new_balance, f'Transfer to {to_account}'))
            
            # Record transaction for receiver
            cursor.execute("""
                INSERT INTO transactions (account_id, transaction_type, amount, balance_after, description)
                VALUES (%s, %s, %s, %s, %s)
            """, (receiver_id, 'Transfer In', amount, receiver_new_balance, f'Transfer from {from_account}'))
            
            connection.commit()
            print(f"\n✓ Transfer successful!")
            print(f"Amount transferred: ₹{amount:.2f}")
            print(f"Your new balance: ₹{sender_new_balance:.2f}")
        
        cursor.close()
    except ValueError:
        print("✗ Invalid amount entered")
    except Error as e:
        print(f"✗ Error transferring amount: {e}")

def view_transaction_history():
    """View transaction history of account"""
    print("\n" + "="*50)
    print("TRANSACTION HISTORY")
    print("="*50)
    
    try:
        account_number = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()
        
        cursor = connection.cursor()
        cursor.execute("""
            SELECT account_id FROM accounts WHERE account_number = %s AND pin = %s
        """, (account_number, pin))
        
        account = cursor.fetchone()
        if account:
            account_id = account[0]
            cursor.execute("""
                SELECT transaction_id, transaction_type, amount, balance_after, transaction_date, description
                FROM transactions WHERE account_id = %s ORDER BY transaction_date DESC LIMIT 10
            """, (account_id,))
            
            transactions = cursor.fetchall()
            if transactions:
                print("\nLast 10 Transactions:")
                print("-"*100)
                print(f"{'ID':<5} {'Type':<15} {'Amount':<12} {'Balance':<12} {'Date':<20} {'Description':<30}")
                print("-"*100)
                for trans in transactions:
                    print(f"{trans[0]:<5} {trans[1]:<15} ₹{trans[2]:<11.2f} ₹{trans[3]:<11.2f} {str(trans[4]):<20} {trans[5]:<30}")
                print("-"*100)
            else:
                print("✗ No transactions found")
        else:
            print("✗ Invalid account number or PIN")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error retrieving transaction history: {e}")

def update_account_info():
    """Update account information"""
    print("\n" + "="*50)
    print("UPDATE ACCOUNT INFORMATION")
    print("="*50)
    
    try:
        account_number = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()
        
        cursor = connection.cursor()
        cursor.execute("""
            SELECT account_id FROM accounts WHERE account_number = %s AND pin = %s
        """, (account_number, pin))
        
        account = cursor.fetchone()
        if account:
            account_id = account[0]
            print("\nWhat do you want to update?")
            print("1. Email")
            print("2. Phone")
            print("3. PIN")
            
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == '1':
                new_email = input("Enter new email: ").strip()
                cursor.execute("""
                    UPDATE accounts SET email = %s WHERE account_id = %s
                """, (new_email, account_id))
                print("✓ Email updated successfully")
            elif choice == '2':
                new_phone = input("Enter new phone: ").strip()
                cursor.execute("""
                    UPDATE accounts SET phone = %s WHERE account_id = %s
                """, (new_phone, account_id))
                print("✓ Phone updated successfully")
            elif choice == '3':
                new_pin = input("Enter new 4-digit PIN: ").strip()
                if len(new_pin) != 4 or not new_pin.isdigit():
                    print("✗ PIN must be 4 digits")
                    cursor.close()
                    return
                cursor.execute("""
                    UPDATE accounts SET pin = %s WHERE account_id = %s
                """, (new_pin, account_id))
                print("✓ PIN updated successfully")
            else:
                print("✗ Invalid choice")
                cursor.close()
                return
            
            connection.commit()
        else:
            print("✗ Invalid account number or PIN")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error updating account: {e}")

def delete_account():
    """Delete an account (close account)"""
    print("\n" + "="*50)
    print("DELETE ACCOUNT")
    print("="*50)
    
    try:
        account_number = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()
        confirmation = input("Are you sure you want to delete this account? (yes/no): ").strip().lower()
        
        if confirmation != 'yes':
            print("✗ Account deletion cancelled")
            return
        
        cursor = connection.cursor()
        cursor.execute("""
            SELECT account_id, balance FROM accounts WHERE account_number = %s AND pin = %s
        """, (account_number, pin))
        
        account = cursor.fetchone()
        if account:
            account_id = account[0]
            balance = account[1]
            
            if balance > 0:
                print(f"✗ Cannot delete account with balance. Current balance: ₹{balance:.2f}")
                print("Please withdraw your balance first.")
            else:
                cursor.execute("""
                    DELETE FROM transactions WHERE account_id = %s
                """, (account_id,))
                
                cursor.execute("""
                    DELETE FROM transfers WHERE from_account_id = %s OR to_account_id = %s
                """, (account_id, account_id))
                
                cursor.execute("""
                    DELETE FROM accounts WHERE account_id = %s
                """, (account_id,))
                
                connection.commit()
                print("✓ Account deleted successfully")
        else:
            print("✗ Invalid account number or PIN")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error deleting account: {e}")

# ====================== ADMIN FUNCTIONS ======================

def view_all_accounts():
    """View all accounts (Admin function)"""
    print("\n" + "="*50)
    print("ALL ACCOUNTS (ADMIN VIEW)")
    print("="*50)
    
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT account_id, account_number, account_holder_name, account_type, balance, status, creation_date
            FROM accounts ORDER BY account_id
        """)
        
        accounts = cursor.fetchall()
        if accounts:
            print("\n" + "-"*120)
            print(f"{'ID':<5} {'Account #':<15} {'Holder Name':<20} {'Type':<12} {'Balance':<15} {'Status':<10} {'Date':<20}")
            print("-"*120)
            for acc in accounts:
                print(f"{acc[0]:<5} {acc[1]:<15} {acc[2]:<20} {acc[3]:<12} ₹{acc[4]:<14.2f} {acc[5]:<10} {str(acc[6]):<20}")
            print("-"*120)
            print(f"Total Accounts: {len(accounts)}")
        else:
            print("✗ No accounts found")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error retrieving accounts: {e}")

def view_all_transactions():
    """View all transactions (Admin function)"""
    print("\n" + "="*50)
    print("ALL TRANSACTIONS (ADMIN VIEW)")
    print("="*50)
    
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT t.transaction_id, a.account_number, t.transaction_type, t.amount, 
                   t.balance_after, t.transaction_date, t.description
            FROM transactions t
            JOIN accounts a ON t.account_id = a.account_id
            ORDER BY t.transaction_date DESC LIMIT 20
        """)
        
        transactions = cursor.fetchall()
        if transactions:
            print("\nLast 20 Transactions:")
            print("-"*130)
            print(f"{'ID':<5} {'Account':<15} {'Type':<15} {'Amount':<12} {'Balance':<12} {'Date':<20} {'Description':<30}")
            print("-"*130)
            for trans in transactions:
                print(f"{trans[0]:<5} {trans[1]:<15} {trans[2]:<15} ₹{trans[3]:<11.2f} ₹{trans[4]:<11.2f} {str(trans[5]):<20} {trans[6]:<30}")
            print("-"*130)
        else:
            print("✗ No transactions found")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error retrieving transactions: {e}")

def admin_login():
    """Admin login function"""
    print("\n" + "="*50)
    print("ADMIN LOGIN")
    print("="*50)
    
    admin_username = "admin"
    admin_password = "admin123"
    
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ")
    
    if username == admin_username and password == admin_password:
        print("✓ Admin login successful!")
        admin_menu()
    else:
        print("✗ Invalid username or password")

def admin_menu():
    """Admin menu"""
    while True:
        print("\n" + "="*50)
        print("ADMIN MENU")
        print("="*50)
        print("1. View All Accounts")
        print("2. View All Transactions")
        print("3. View Account Details")
        print("4. Delete Account (Force)")
        print("5. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            view_all_accounts()
        elif choice == '2':
            view_all_transactions()
        elif choice == '3':
            account_number = input("Enter account number: ").strip()
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    SELECT account_id, account_holder_name, account_type, balance, email, phone, creation_date, status
                    FROM accounts WHERE account_number = %s
                """, (account_number,))
                
                account = cursor.fetchone()
                if account:
                    print("\n" + "="*50)
                    print("ACCOUNT DETAILS")
                    print("="*50)
                    print(f"Account Number: {account_number}")
                    print(f"Holder: {account[1]}")
                    print(f"Type: {account[2]}")
                    print(f"Balance: ₹{account[3]:.2f}")
                    print(f"Email: {account[4]}")
                    print(f"Phone: {account[5]}")
                    print(f"Created: {account[6]}")
                    print(f"Status: {account[7]}")
                else:
                    print("✗ Account not found")
                
                cursor.close()
            except Error as e:
                print(f"✗ Error: {e}")
        elif choice == '4':
            account_number = input("Enter account number: ").strip()
            confirmation = input("Force delete this account? (yes/no): ").strip().lower()
            if confirmation == 'yes':
                try:
                    cursor = connection.cursor()
                    cursor.execute("""
                        SELECT account_id FROM accounts WHERE account_number = %s
                    """, (account_number,))
                    
                    account = cursor.fetchone()
                    if account:
                        account_id = account[0]
                        cursor.execute("DELETE FROM transactions WHERE account_id = %s", (account_id,))
                        cursor.execute("DELETE FROM transfers WHERE from_account_id = %s OR to_account_id = %s", 
                                     (account_id, account_id))
                        cursor.execute("DELETE FROM accounts WHERE account_id = %s", (account_id,))
                        connection.commit()
                        print("✓ Account force deleted")
                    else:
                        print("✗ Account not found")
                    
                    cursor.close()
                except Error as e:
                    print(f"✗ Error: {e}")
        elif choice == '5':
            break
        else:
            print("✗ Invalid choice")

# ====================== MAIN MENU ======================

def main_menu():
    """Main menu of the Banking Management System"""
    while True:
        print("\n" + "="*50)
        print("BANKING MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Create New Account")
        print("2. Display Account Details")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Transfer Money")
        print("7. View Transaction History")
        print("8. Update Account Information")
        print("9. Delete Account")
        print("10. Admin Login")
        print("11. Exit")
        
        choice = input("\nEnter your choice (1-11): ").strip()
        
        if choice == '1':
            create_account()
        elif choice == '2':
            display_account()
        elif choice == '3':
            deposit_amount()
        elif choice == '4':
            withdraw_amount()
        elif choice == '5':
            check_balance()
        elif choice == '6':
            transfer_amount()
        elif choice == '7':
            view_transaction_history()
        elif choice == '8':
            update_account_info()
        elif choice == '9':
            delete_account()
        elif choice == '10':
            admin_login()
        elif choice == '11':
            print("\n✓ Thank you for using Banking Management System")
            print("✓ Have a great day!")
            disconnect_database()
            break
        else:
            print("✗ Invalid choice. Please try again.")

# ====================== MAIN EXECUTION ======================

if __name__ == "__main__":
    print("\n" + "="*50)
    print("BANKING MANAGEMENT SYSTEM")
    print("="*50)
    print("Initializing...")
    
    if connect_database():
        create_tables()
        print("\n✓ System ready!")
        time.sleep(1)
        main_menu()
    else:
        print("\n✗ Failed to initialize the system. Please check your database connection.")
    
    disconnect_database()
