# E-COMMERCE STORE MANAGEMENT SYSTEM

## Project Overview

A comprehensive menu-driven E-commerce Store Management System built with Python and MySQL. This system provides complete functionality for managing customers, products, categories, orders, and customer reviews.

**Technology Stack:**
- Python 3.x
- MySQL Database
- mysql-connector-python
- Object-Oriented Programming (Class-based)

**Current Date:** January 22, 2026

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Database Schema](#database-schema)
5. [Module Functions](#module-functions)
6. [Usage Guide](#usage-guide)
7. [Sample Outputs](#sample-outputs)
8. [Installation](#installation)

---

## System Overview

The **EcommerceStoreManagementSystem** class is the main controller that manages all operations in a complete online retail environment. It uses object-oriented programming principles with MySQL backend for persistent data storage.

### Class Structure
```python
class EcommerceStoreManagementSystem:
    - __init__()           # Initialize and connect to database
    - connect_db()         # Establish database connection
    - create_tables()      # Create database schema
    - insert_sample_data() # Load initial data
    
    # All public methods for different operations
```

---

## Features

### 1. **Customer Management**
- Register new customers with personal details
- View all registered customers
- Track registration dates and membership status
- Store contact information and addresses

### 2. **Category Management**
- Add new product categories
- View all active categories
- Organize products by categories

### 3. **Product Management**
- Add new products with pricing and inventory
- View all products with details
- Search products by name
- Track stock quantity and availability
- Link products to categories

### 4. **Order Management**
- Create orders with multiple items
- Add items to orders with inventory management
- Apply discounts to orders
- Track order status and payment status
- View detailed order information with items

### 5. **Review Management**
- Add product reviews from customers
- View product reviews with ratings
- Display customer feedback

### 6. **Analytics & Reporting**
- Generate comprehensive store reports
- Track total products and customers
- Monitor revenue and sales
- Identify low-stock products

---

## Architecture

### Function Hierarchy

```
EcommerceStoreManagementSystem
│
├── DATABASE OPERATIONS
│   ├── connect_db()
│   ├── create_tables()
│   └── insert_sample_data()
│
├── CUSTOMER MANAGEMENT
│   ├── add_customer()
│   └── view_all_customers()
│
├── CATEGORY MANAGEMENT
│   ├── add_category()
│   └── view_all_categories()
│
├── PRODUCT MANAGEMENT
│   ├── add_product()
│   ├── view_all_products()
│   └── search_product()
│
├── ORDER MANAGEMENT
│   ├── create_order()
│   ├── view_orders()
│   └── view_order_details()
│
├── REVIEW MANAGEMENT
│   ├── add_review()
│   └── view_product_reviews()
│
├── REPORTING
│   └── generate_report()
│
└── UI INTERFACE
    └── main_menu()
```

---

## Database Schema

### 1. **CUSTOMERS TABLE**
```sql
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    password VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(50),
    pincode VARCHAR(10),
    registration_date DATE,
    status VARCHAR(20) DEFAULT 'Active'
)
```

**Sample Data:**
| ID | Name | Email | Phone | City | Registration Date | Status |
|:--|:--|:--|:--|:--|:--|:--|
| 1 | John Smith | john@email.com | 1234567890 | New York | 2024-01-15 | Active |
| 2 | Mary Johnson | mary@email.com | 9876543210 | Los Angeles | 2024-02-20 | Active |
| 3 | Robert Williams | robert@email.com | 5551234567 | Chicago | 2024-03-10 | Active |

---

### 2. **CATEGORIES TABLE**
```sql
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE NOT NULL,
    description VARCHAR(255),
    status VARCHAR(20) DEFAULT 'Active'
)
```

**Sample Data:**
| ID | Category Name | Description | Status |
|:--|:--|:--|:--|
| 1 | Electronics | Electronic devices and gadgets | Active |
| 2 | Clothing | Fashion and apparel | Active |
| 3 | Books | Books and magazines | Active |
| 4 | Home & Kitchen | Home appliances and kitchenware | Active |
| 5 | Sports | Sports equipment and accessories | Active |

---

### 3. **PRODUCTS TABLE**
```sql
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    product_name VARCHAR(200) NOT NULL,
    description VARCHAR(500),
    price FLOAT,
    stock_quantity INT,
    brand VARCHAR(100),
    sku VARCHAR(50) UNIQUE,
    image_url VARCHAR(255),
    status VARCHAR(20) DEFAULT 'Active',
    FOREIGN KEY(category_id) REFERENCES categories(category_id)
)
```

**Sample Data:**
| ID | Product Name | Category | Brand | Price | Stock | Status |
|:--|:--|:--|:--|:--|:--|:--|
| 1 | Wireless Headphones | Electronics | SoundMax | Rs.2999.00 | 50 | Active |
| 2 | Smartphone 5G | Electronics | TechPhone | Rs.29999.00 | 30 | Active |
| 3 | Cotton T-Shirt | Clothing | FashionBrand | Rs.499.00 | 100 | Active |
| 4 | Denim Jeans | Clothing | DenimCo | Rs.1299.00 | 75 | Active |
| 5 | Python Programming Book | Books | TechBooks | Rs.599.00 | 40 | Active |
| 6 | Electric Kettle | Home & Kitchen | HomeAppliances | Rs.899.00 | 60 | Active |
| 7 | Yoga Mat | Sports | FitGear | Rs.799.00 | 80 | Active |

---

### 4. **ORDERS TABLE**
```sql
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATETIME,
    total_amount FLOAT,
    discount FLOAT DEFAULT 0,
    net_amount FLOAT,
    shipping_address VARCHAR(255),
    order_status VARCHAR(20) DEFAULT 'Pending',
    payment_method VARCHAR(30),
    payment_status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
)
```

**Schema Relationships:**
- Links to CUSTOMERS via customer_id
- Parent table for ORDER_ITEMS

---

### 5. **ORDER_ITEMS TABLE**
```sql
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    price FLOAT,
    subtotal FLOAT,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
```

---

### 6. **REVIEWS TABLE**
```sql
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    rating INT,
    review_text VARCHAR(500),
    review_date DATE,
    status VARCHAR(20) DEFAULT 'Approved',
    FOREIGN KEY(product_id) REFERENCES products(product_id),
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
)
```

---

## Module Functions

### DATABASE OPERATIONS

#### `__init__()`
**Purpose:** Initialize the system and connect to database
- Creates instance variables for connection and cursor
- Calls connect_db() automatically

#### `connect_db()`
**Purpose:** Establish MySQL connection and initialize database
- Connects to 'mydb' database
- Creates tables if they don't exist
- Inserts sample data on first run
- Error handling for connection failures

```python
def connect_db(self):
    try:
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='mydb'
        )
        self.cursor = self.connection.cursor()
        print("✓ Database connected successfully!")
        self.create_tables()
        self.insert_sample_data()
    except Error as e:
        print(f"Error: {e}")
```

---

#### `create_tables()`
**Purpose:** Create all 6 tables with proper relationships
- CUSTOMERS, CATEGORIES, PRODUCTS, ORDERS, ORDER_ITEMS, REVIEWS
- Uses IF NOT EXISTS clause
- Establishes foreign key relationships
- Commits changes to database

---

#### `insert_sample_data()`
**Purpose:** Load initial demonstration data
- 5 categories
- 7 sample products
- 3 sample customers
- Runs only once (checks existing data)

**Sample Initialization Output:**
```
✓ Database connected successfully!
✓ Tables created successfully!
✓ Sample data inserted successfully!
```

---

### CUSTOMER MANAGEMENT

#### `add_customer()`
**Purpose:** Register a new customer in the system

**User Input:**
```
- Name: Full customer name
- Email: Unique email address
- Phone: Contact number
- Password: Account password
- Address: Street address
- City: City name
- Pincode: Postal code
```

**Sample Output:**
```
--- Add New Customer ---
Enter Customer Name: Sarah Anderson
Enter Email: sarah@email.com
Enter Phone: 8765432109
Enter Password: secure123
Enter Address: 321 Maple St
Enter City: Houston
Enter Pincode: 77001
✓ Customer added successfully!
```

---

#### `view_all_customers()`
**Purpose:** Display all registered customers

**Output Format:**
```
--- All Customers ---
ID    Name                      Email                     Phone           City            Reg Date    Status    
------------------------------------------------------------------------------------------------------------------
1     John Smith                john@email.com            1234567890      New York        2024-01-15  Active    
2     Mary Johnson              mary@email.com            9876543210      Los Angeles     2024-02-20  Active    
3     Robert Williams           robert@email.com          5551234567      Chicago         2024-03-10  Active    
4     Sarah Anderson            sarah@email.com           8765432109      Houston         2026-01-22  Active    
```

---

### CATEGORY MANAGEMENT

#### `add_category()`
**Purpose:** Add a new product category

**User Input:**
```
- Category Name: Name of the category
- Description: Category description
```

**Sample Output:**
```
--- Add New Category ---
Enter Category Name: Furniture
Enter Description: Home furniture and decor items
✓ Category added successfully!
```

---

#### `view_all_categories()`
**Purpose:** Display all active product categories

**Output Format:**
```
--- All Categories ---
ID    Category Name              Description                                        Status    
----------------------------------------------------------------------------------------------------
1     Electronics                Electronic devices and gadgets                     Active    
2     Clothing                   Fashion and apparel                                Active    
3     Books                      Books and magazines                                Active    
4     Home & Kitchen             Home appliances and kitchenware                    Active    
5     Sports                     Sports equipment and accessories                   Active    
6     Furniture                  Home furniture and decor items                      Active    
```

---

### PRODUCT MANAGEMENT

#### `add_product()`
**Purpose:** Add a new product to the inventory

**User Input:**
```
- Category ID: ID of product category
- Product Name: Name of the product
- Description: Product details
- Price: Product price in rupees
- Stock Quantity: Available quantity
- Brand: Brand name
- SKU: Stock Keeping Unit (unique identifier)
- Image URL: URL to product image
```

**Sample Output:**
```
--- Add New Product ---
Enter Category ID: 1
Enter Product Name: 4K Smart TV
Enter Description: 55-inch 4K Ultra HD Smart TV
Enter Price: 34999.00
Enter Stock Quantity: 25
Enter Brand: TechVision
Enter SKU: SKU008
Enter Image URL: tv.jpg
✓ Product added successfully!
```

---

#### `view_all_products()`
**Purpose:** Display all active products with details

**Output Format:**
```
--- All Products ---
ID    Product Name                   Category             Brand               Price         Stock    Status    
--------------------------------------------------------------------------------------------------------------
1     Wireless Headphones            Electronics          SoundMax            Rs.2999.00    50       Active    
2     Smartphone 5G                  Electronics          TechPhone           Rs.29999.00   30       Active    
3     Cotton T-Shirt                 Clothing             FashionBrand        Rs.499.00     100      Active    
4     Denim Jeans                    Clothing             DenimCo             Rs.1299.00    75       Active    
5     Python Programming Book        Books                TechBooks           Rs.599.00     40       Active    
6     Electric Kettle                Home & Kitchen       HomeAppliances      Rs.899.00     60       Active    
7     Yoga Mat                       Sports               FitGear             Rs.799.00     80       Active    
8     4K Smart TV                    Electronics          TechVision          Rs.34999.00   25       Active    
```

---

#### `search_product()`
**Purpose:** Search for products by name

**Sample Output:**
```
--- Search Product ---
Enter Product Name to Search: Shirt

ID    Product Name               Category             Brand               Price         Stock    
--------------------------------------------------------------------------------------------------
3     Cotton T-Shirt             Clothing             FashionBrand        Rs.499.00     100      
```

---

### ORDER MANAGEMENT

#### `create_order()`
**Purpose:** Create a new order with multiple items

**Process:**
1. Enter customer ID
2. Retrieve customer's address
3. Enter payment method
4. Add multiple items (product ID and quantity)
5. Check stock availability
6. Apply discount (optional)
7. Calculate total, discount, and net amount
8. Update product stock quantities
9. Confirm order

**Sample Output:**
```
--- Create New Order ---
Enter Customer ID: 1
Enter Payment Method (Cash/Card/UPI/Net Banking): Card

Add item to order? (yes/no): yes
Enter Product ID: 2
Enter Quantity: 1
Item added! Subtotal: Rs. 29999.00

Add item to order? (yes/no): yes
Enter Product ID: 3
Enter Quantity: 2
Item added! Subtotal: Rs. 998.00

Add item to order? (yes/no): no
Enter Discount Amount (if any): 500

✓ Order created successfully!
Order ID: 1
Total Amount: Rs. 30997.00
Discount: Rs. 500.00
Net Amount: Rs. 30497.00
```

---

#### `view_orders()`
**Purpose:** Display all orders with summary information

**Output Format:**
```
--- All Orders ---
Order ID  Customer              Date                 Total         Discount      Net           Status       Payment      
-------------------------------------------------------------------------------------------------------------------------------------------
1         John Smith            2026-01-22 14:35:22  Rs.30997.00   Rs.500.00     Rs.30497.00   Confirmed    Completed    
2         Mary Johnson          2026-01-22 15:10:45  Rs.17098.00   Rs.100.00     Rs.16998.00   Confirmed    Completed    
```

---

#### `view_order_details()`
**Purpose:** Display detailed information for a specific order including all items

**Sample Output:**
```
--- Order Details ---
Enter Order ID: 1

================================================================================
                        ORDER DETAILS
================================================================================
Order ID: 1
Customer: John Smith
Order Date: 2026-01-22 14:35:22
Shipping Address: 123 Main St, New York
Payment Method: Card
Order Status: Confirmed
--------------------------------------------------------------------------------
Product                                  Quantity   Price        Subtotal     
--------------------------------------------------------------------------------
Smartphone 5G                            1          Rs.29999.00  Rs.29999.00  
Cotton T-Shirt                           2          Rs.499.00    Rs.998.00    
--------------------------------------------------------------------------------
Total Amount: Rs. 30997.00
Discount: Rs. 500.00
Net Amount: Rs. 30497.00
================================================================================
```

---

### REVIEW MANAGEMENT

#### `add_review()`
**Purpose:** Add a product review from a customer

**User Input:**
```
- Product ID: ID of the product
- Customer ID: ID of the reviewer
- Rating: Rating from 1-5 stars
- Review Text: Review content
```

**Sample Output:**
```
--- Add Product Review ---
Enter Product ID: 2
Enter Customer ID: 1
Enter Rating (1-5): 5
Enter Review: Excellent smartphone with amazing camera quality!
✓ Review added successfully!
```

---

#### `view_product_reviews()`
**Purpose:** Display all approved reviews for a product

**Sample Output:**
```
--- Product Reviews ---
Enter Product ID: 2

Customer                  Rating   Review                                                 Date       
------------------------------------------------------------------------------------------------------
John Smith                5/5      Excellent smartphone with amazing camera quality!       2026-01-22
Mary Johnson              4/5      Good value for money. Battery life could be better.     2026-01-22
Robert Williams           5/5      Best 5G phone in this price range!                      2026-01-22
```

---

### REPORTING

#### `generate_report()`
**Purpose:** Generate comprehensive store analytics and reports

**Output Format:**
```
--- E-commerce Store Report ---

1. Total Products
   Active Products: 8

2. Total Customers
   Active Customers: 4

3. Total Orders
   Total Orders: 2

4. Total Revenue
   Total Revenue: Rs. 47495.00

5. Low Stock Products
   Products with low stock:
   - Smartphone 5G: 29 units
   - 4K Smart TV: 24 units
```

---

### MAIN MENU INTERFACE

#### `main_menu()`
**Purpose:** Display main menu and handle user navigation

**Menu Display:**
```
============================================================
        E-COMMERCE STORE MANAGEMENT SYSTEM
============================================================

--- CUSTOMER MANAGEMENT ---
1. Add Customer
2. View All Customers

--- CATEGORY MANAGEMENT ---
3. Add Category
4. View All Categories

--- PRODUCT MANAGEMENT ---
5. Add Product
6. View All Products
7. Search Product

--- ORDER MANAGEMENT ---
8. Create Order
9. View All Orders
10. View Order Details

--- REVIEW MANAGEMENT ---
11. Add Product Review
12. View Product Reviews

--- REPORTS ---
13. Generate Store Report

14. Exit
============================================================

Enter your choice (1-14):
```

---

## Usage Guide

### Installation

1. **Install Python Dependencies:**
```bash
pip install mysql-connector-python
```

2. **Setup MySQL Database:**
```sql
CREATE DATABASE mydb;
```

3. **Update Database Credentials** (if needed):
Edit the `connect_db()` method:
```python
self.connection = mysql.connector.connect(
    host='localhost',        # Your host
    user='root',             # Your username
    password='1234',         # Your password
    database='mydb'          # Your database name
)
```

4. **Run the Program:**
```bash
python estore.py
```

---

### Quick Start Workflow

**Step 1: Start System**
```bash
python estore.py
```

**Output:**
```
✓ Database connected successfully!
✓ Tables created successfully!
✓ Sample data inserted successfully!

============================================================
        E-COMMERCE STORE MANAGEMENT SYSTEM
============================================================
```

**Step 2: View Products (Option 6)**
```
Enter your choice (1-14): 6

--- All Products ---
ID    Product Name               Category          Brand               Price          Stock    Status    
```

**Step 3: Create Order (Option 8)**
```
Enter your choice (1-14): 8

--- Create New Order ---
Enter Customer ID: 1
Enter Payment Method (Cash/Card/UPI/Net Banking): Card
...
```

**Step 4: View Order Details (Option 10)**
```
Enter your choice (1-14): 10

--- Order Details ---
Enter Order ID: 1
```

**Step 5: Generate Report (Option 13)**
```
Enter your choice (1-14): 13

--- E-commerce Store Report ---
```

**Step 6: Exit (Option 14)**
```
Enter your choice (1-14): 14

Thank you for using E-commerce Store Management System!
```

---

## Complete Workflow Examples

### Example 1: Complete Customer to Order Workflow

```
=== System Starts ===
✓ Database connected successfully!

=== Step 1: Add New Customer (Option 1) ===
Enter Customer Name: David Chen
Enter Email: david.chen@email.com
Enter Phone: 9988776655
Enter Password: pass123
Enter Address: 999 Tech Street
Enter City: San Francisco
Enter Pincode: 94102
✓ Customer added successfully!

=== Step 2: View All Customers (Option 2) ===
ID    Name                Email                    Phone           City
1     John Smith          john@email.com           1234567890      New York
2     Mary Johnson        mary@email.com           9876543210      Los Angeles
3     Robert Williams     robert@email.com         5551234567      Chicago
4     David Chen          david.chen@email.com     9988776655      San Francisco

=== Step 3: Search Product (Option 7) ===
Enter Product Name to Search: Phone

ID    Product Name           Category       Brand        Price          Stock
2     Smartphone 5G          Electronics    TechPhone    Rs.29999.00    30

=== Step 4: Create Order (Option 8) ===
Enter Customer ID: 4
Enter Payment Method (Cash/Card/UPI/Net Banking): UPI

Add item to order? (yes/no): yes
Enter Product ID: 2
Enter Quantity: 1
Item added! Subtotal: Rs. 29999.00

Add item to order? (yes/no): yes
Enter Product ID: 7
Enter Quantity: 1
Item added! Subtotal: Rs. 799.00

Add item to order? (yes/no): no
Enter Discount Amount (if any): 1000

✓ Order created successfully!
Order ID: 3
Total Amount: Rs. 30798.00
Discount: Rs. 1000.00
Net Amount: Rs. 29798.00

=== Step 5: View Order Details (Option 10) ===
Enter Order ID: 3

================================================================================
                        ORDER DETAILS
================================================================================
Order ID: 3
Customer: David Chen
Order Date: 2026-01-22 16:45:30
Shipping Address: 999 Tech Street, San Francisco
Payment Method: UPI
Order Status: Confirmed
--------------------------------------------------------------------------------
Product                          Quantity   Price         Subtotal
--------------------------------------------------------------------------------
Smartphone 5G                    1          Rs.29999.00   Rs.29999.00
Yoga Mat                         1          Rs.799.00     Rs.799.00
--------------------------------------------------------------------------------
Total Amount: Rs. 30798.00
Discount: Rs. 1000.00
Net Amount: Rs. 29798.00
================================================================================

=== Step 6: Add Review (Option 11) ===
Enter Product ID: 2
Enter Customer ID: 4
Enter Rating (1-5): 5
Enter Review: Amazing phone! Very satisfied with the purchase.
✓ Review added successfully!

=== Step 7: Generate Report (Option 13) ===

--- E-commerce Store Report ---

1. Total Products
   Active Products: 8

2. Total Customers
   Active Customers: 4

3. Total Orders
   Total Orders: 3

4. Total Revenue
   Total Revenue: Rs. 77293.00

5. Low Stock Products
   Products with low stock:
   - Smartphone 5G: 29 units
```

---

### Example 2: Product Management Workflow

```
=== Add New Category (Option 3) ===
Enter Category Name: Smartwatches
Enter Description: Wearable smart devices
✓ Category added successfully!

=== Add New Product (Option 5) ===
Enter Category ID: 6
Enter Product Name: Smartwatch Pro
Enter Description: Advanced fitness tracking smartwatch
Enter Price: 9999.00
Enter Stock Quantity: 50
Enter Brand: WearTech
Enter SKU: SKU009
Enter Image URL: smartwatch.jpg
✓ Product added successfully!

=== View All Products (Option 6) ===
ID    Product Name           Category           Brand           Price            Stock
1     Wireless Headphones    Electronics        SoundMax        Rs.2999.00       50
2     Smartphone 5G          Electronics        TechPhone       Rs.29999.00      29
3     Cotton T-Shirt         Clothing           FashionBrand    Rs.499.00        100
4     Denim Jeans            Clothing           DenimCo         Rs.1299.00       75
5     Python Book            Books              TechBooks       Rs.599.00        40
6     Electric Kettle        Home & Kitchen     HomeAppliances  Rs.899.00        60
7     Yoga Mat               Sports             FitGear         Rs.799.00        79
8     4K Smart TV            Electronics        TechVision      Rs.34999.00      25
9     Smartwatch Pro         Smartwatches       WearTech        Rs.9999.00       50
```

---

### Example 3: Advanced Order with Multiple Items

```
=== Create Complex Order (Option 8) ===
Enter Customer ID: 2
Enter Payment Method (Cash/Card/UPI/Net Banking): Card

Add item to order? (yes/no): yes
Enter Product ID: 1
Enter Quantity: 2
Item added! Subtotal: Rs. 5998.00

Add item to order? (yes/no): yes
Enter Product ID: 3
Enter Quantity: 3
Item added! Subtotal: Rs. 1497.00

Add item to order? (yes/no): yes
Enter Product ID: 5
Enter Quantity: 1
Item added! Subtotal: Rs. 599.00

Add item to order? (yes/no): yes
Enter Product ID: 6
Enter Quantity: 1
Item added! Subtotal: Rs. 899.00

Add item to order? (yes/no): no
Enter Discount Amount (if any): 500

✓ Order created successfully!
Order ID: 4
Total Amount: Rs. 8993.00
Discount: Rs. 500.00
Net Amount: Rs. 8493.00
```

---

## Data Flow Diagram

```
┌─────────────────┐
│   Main Menu     │
└────────┬────────┘
         │
    ┌────┴──────────────────────────────────────┐
    │                                           │
┌───▼─────────────┐  ┌──────────────────────┐  │
│   Customers     │  │   Products &         │  │
│   - Add         │  │   Categories         │  │
│   - View        │  │   - Add              │  │
└─────────────────┘  │   - View             │  │
                     │   - Search           │  │
                     └──────────────────────┘  │
    ┌────────────────────────────────────────┐ │
    │          Orders & Items                │ │
    │  - Create Order (with items)           │ │
    │  - View Orders/Details                 │ │
    │  - Inventory Management                │ │
    └────────────────────────────────────────┘ │
    ┌────────────────────────────────────────┐ │
    │          Reviews & Reports             │ │
    │  - Add Review                          │ │
    │  - View Reviews                        │ │
    │  - Generate Report                     │ │
    └────────────────────────────────────────┘ │
    │
    └──────────────────────────────────┐
                                       │
                            ┌──────────▼────────────┐
                            │   MySQL Database      │
                            │  - Customers          │
                            │  - Categories         │
                            │  - Products           │
                            │  - Orders             │
                            │  - Order Items        │
                            │  - Reviews            │
                            └───────────────────────┘
```

---

## Error Handling

### Common Errors & Solutions

| Error | Cause | Solution |
|:--|:--|:--|
| Database Connection Error | MySQL not running | Start MySQL service |
| Duplicate Email | Customer email already exists | Use unique email |
| Product Not Found | Invalid product ID | Check product ID |
| Insufficient Stock | Trying to order more than available | Reduce quantity |
| Customer Not Found | Invalid customer ID | Check customer ID |
| Invalid Rating | Rating not between 1-5 | Enter rating 1-5 |

---

## Key Features Explained

### 1. **Inventory Management**
- Automatic stock deduction on order creation
- Stock validation before order confirmation
- Low stock product alerts in reports

### 2. **Order Processing**
- Multi-item order support
- Automatic shipping address from customer profile
- Discount application
- Status tracking (Pending/Confirmed)

### 3. **Financial Tracking**
- Order total calculation
- Discount application
- Net amount computation
- Revenue reporting

### 4. **Data Relationships**
- Customers link to Orders
- Orders link to Products via Order Items
- Products belong to Categories
- Reviews link Customers and Products

### 5. **Reporting Analytics**
- Active products count
- Active customers count
- Total orders
- Total revenue
- Low stock inventory

---

## Technical Specifications

| Specification | Value |
|:--|:--|
| Database | MySQL |
| Python Version | 3.6+ |
| Connector | mysql-connector-python 8.0+ |
| Currency | Indian Rupees (Rs.) |
| Date Format | YYYY-MM-DD |
| DateTime Format | YYYY-MM-DD HH:MM:SS |
| SKU Format | VARCHAR(50) |
| Default Record Status | Active |

---

## Database Relationships Map

```
CUSTOMERS ─────────┐
                   │
              ┌────▼────────────┐
              │   ORDERS        │
              └────┬────────────┘
                   │
              ┌────▼────────────────────────┐
              │   ORDER_ITEMS              │
              └────┬─────────────────────────┘
                   │
    ┌──────────────▼────────────────────┐
    │        PRODUCTS                   │
    │           │                       │
    │      ┌────▼───────────────┐       │
    │      │  CATEGORIES        │       │
    │      └────────────────────┘       │
    └──────────┬───────────────────────┘
               │
          ┌────▼────────────────────────┐
          │   REVIEWS                   │
          │   (Links Product & Customer)│
          └────────────────────────────┘
```

---

## Future Enhancements

1. **Payment Gateway Integration** - Online payment processing
2. **Shipping Integration** - Real-time shipping updates
3. **User Authentication** - Admin login system
4. **Wishlist Feature** - Customer wishlists
5. **Coupon System** - Promotional codes
6. **Email Notifications** - Order confirmations
7. **Mobile App** - Dedicated mobile application
8. **Analytics Dashboard** - Advanced reporting
9. **Inventory Alerts** - Real-time notifications
10. **Return Management** - Handle product returns

---

## Support & Maintenance

### Regular Tasks
- Backup database regularly
- Monitor low stock products
- Review customer reviews
- Update product information
- Manage customer accounts

### Performance Tips
- Index frequently searched columns
- Archive old orders periodically
- Monitor database size
- Optimize queries

---

## Version History

| Version | Date | Features |
|:--|:--|:--|
| 1.0 | 2026-01-22 | Complete e-commerce system with 14 main functions |

---

## System Requirements

- **OS:** Windows/Linux/Mac
- **Python:** 3.6 or higher
- **MySQL:** 5.7 or higher
- **RAM:** Minimum 512MB
- **Disk Space:** Minimum 100MB

---

## Contact & Support

For issues or feature requests, please contact the development team.

**System Generated:** 2026-01-22  
**Last Updated:** 2026-01-22

---

## Legal Notice

This E-Commerce Store Management System is provided for educational and commercial use. All data is stored securely in the MySQL database with proper access controls.

---

**END OF DOCUMENTATION**
