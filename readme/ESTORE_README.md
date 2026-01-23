# E-Commerce Store Management System

## Overview
A comprehensive Python-based e-commerce management system with MySQL database integration. This system is fully function-driven and menu-based, providing complete management of customers, products, categories, orders, and reviews.

**Version:** 2.0 ( Functions & Menu-Driven)  
**Author:** E-Commerce Development Team  
**Last Updated:** January 2026

---

## Table of Contents
1. [Features](#features)
2. [System Architecture](#system-architecture)
3. [Database Schema](#database-schema)
4. [Functions Overview](#functions-overview)
5. [Module Outputs](#module-outputs)
6. [Installation & Setup](#installation--setup)
7. [Usage Guide](#usage-guide)
8. [Menu Structure](#menu-structure)

---

## Features

### Core Features
✓ **Customer Management** - Add and manage customers with profiles  
✓ **Category Management** - Organize products into categories  
✓ **Product Management** - Add and view products with detailed information  
✓ **Order Processing** - Create and manage customer orders  
✓ **Review System** - Customer reviews and ratings for products  
✓ **Reporting** - Generate comprehensive business reports  
✓ **Inventory Management** - Track stock levels and low stock alerts  
✓ **Payment Processing** - Support for multiple payment methods  

---

## System Architecture

### File Structure
```
estore_refactored.py          # Main application file (functions-based)
ESTORE_README.md              # This documentation file
```

### Programming Paradigm
- **Approach:** Function-based programming (procedural)
- **Style:** Menu-driven interface
- **Database:** MySQL
- **Python Version:** 3.7+

---

## Database Schema

### Tables Structure

#### 1. CUSTOMERS Table
```
customer_id (INT, PRIMARY KEY, AUTO_INCREMENT)
name (VARCHAR 100)
email (VARCHAR 100, UNIQUE)
phone (VARCHAR 15)
password (VARCHAR 100)
address (VARCHAR 255)
city (VARCHAR 50)
pincode (VARCHAR 10)
registration_date (DATE)
status (VARCHAR 20) - Default: 'Active'
```

#### 2. CATEGORIES Table
```
category_id (INT, PRIMARY KEY, AUTO_INCREMENT)
category_name (VARCHAR 100, UNIQUE)
description (VARCHAR 255)
status (VARCHAR 20) - Default: 'Active'
```

#### 3. PRODUCTS Table
```
product_id (INT, PRIMARY KEY, AUTO_INCREMENT)
category_id (INT, FOREIGN KEY → categories)
product_name (VARCHAR 200)
description (VARCHAR 500)
price (FLOAT)
stock_quantity (INT)
brand (VARCHAR 100)
sku (VARCHAR 50, UNIQUE)
image_url (VARCHAR 255)
status (VARCHAR 20) - Default: 'Active'
```

#### 4. ORDERS Table
```
order_id (INT, PRIMARY KEY, AUTO_INCREMENT)
customer_id (INT, FOREIGN KEY → customers)
order_date (DATETIME)
total_amount (FLOAT)
discount (FLOAT) - Default: 0
net_amount (FLOAT)
shipping_address (VARCHAR 255)
order_status (VARCHAR 20) - Default: 'Pending'
payment_method (VARCHAR 30)
payment_status (VARCHAR 20) - Default: 'Pending'
```

#### 5. ORDER_ITEMS Table
```
order_item_id (INT, PRIMARY KEY, AUTO_INCREMENT)
order_id (INT, FOREIGN KEY → orders)
product_id (INT, FOREIGN KEY → products)
quantity (INT)
price (FLOAT)
subtotal (FLOAT)
```

#### 6. REVIEWS Table
```
review_id (INT, PRIMARY KEY, AUTO_INCREMENT)
product_id (INT, FOREIGN KEY → products)
customer_id (INT, FOREIGN KEY → customers)
rating (INT) - 1-5 scale
review_text (VARCHAR 500)
review_date (DATE)
status (VARCHAR 20) - Default: 'Approved'
```

---

## Functions Overview

### Database Connection Functions

#### `connect_db()`
- **Purpose:** Establish MySQL database connection
- **Parameters:** None
- **Returns:** Global connection and cursor objects
- **Calls:** `create_tables()`, `insert_sample_data()`
- **Output:**
```
✓ Database connected successfully!
✓ Tables created successfully!
✓ Sample data inserted successfully!
```

#### `create_tables()`
- **Purpose:** Create all required database tables with schema
- **Parameters:** None
- **Returns:** None
- **Output:** `✓ Tables created successfully!`

#### `insert_sample_data()`
- **Purpose:** Populate database with initial sample data
- **Parameters:** None
- **Returns:** None
- **Output:** `✓ Sample data inserted successfully!`

---

### Customer Management Functions

#### `add_customer()`
- **Purpose:** Add new customer to system
- **User Input:** Name, Email, Phone, Password, Address, City, Pincode
- **Output:** `✓ Customer added successfully!`

#### `view_all_customers()`
- **Purpose:** Display all registered customers
- **Parameters:** None
- **Output:**
```
--- All Customers ---
ID    Name                  Email                     Phone          City           Reg Date    Status    
---------------------------------------------------------------------------------------------------------
1     John Smith            john@email.com            1234567890     New York       2024-01-15  Active    
2     Mary Johnson          mary@email.com            9876543210     Los Angeles    2024-02-20  Active    
3     Robert Williams       robert@email.com          5551234567     Chicago        2024-03-10  Active    
```

---

### Category Management Functions

#### `add_category()`
- **Purpose:** Create new product category
- **User Input:** Category Name, Description
- **Output:** `✓ Category added successfully!`

#### `view_all_categories()`
- **Purpose:** Display all product categories
- **Parameters:** None
- **Output:**
```
--- All Categories ---
ID    Category Name                  Description                                        Status    
-----------------------------------------------------------------------------------------------------
1     Electronics                    Electronic devices and gadgets                    Active    
2     Clothing                       Fashion and apparel                               Active    
3     Books                          Books and magazines                               Active    
4     Home & Kitchen                 Home appliances and kitchenware                   Active    
5     Sports                         Sports equipment and accessories                  Active    
```

---

### Product Management Functions

#### `add_product()`
- **Purpose:** Add new product to inventory
- **User Input:** Category ID, Product Name, Description, Price, Stock Quantity, Brand, SKU, Image URL
- **Output:** `✓ Product added successfully!`

#### `view_all_products()`
- **Purpose:** Display all active products
- **Parameters:** None
- **Output:**
```
--- All Products ---
ID    Product Name                  Category         Brand          Price        Stock   Status    
----------------------------------------------------------------------------------------------------
1     Wireless Headphones           Electronics      SoundMax       Rs.2999.00   50      Active    
2     Smartphone 5G                 Electronics      TechPhone      Rs.29999.00  30      Active    
3     Cotton T-Shirt                Clothing         FashionBrand   Rs.499.00    100     Active    
4     Denim Jeans                   Clothing         DenimCo        Rs.1299.00   75      Active    
5     Python Programming Book       Books            TechBooks      Rs.599.00    40      Active    
6     Electric Kettle               Home & Kitchen   HomeAppliances Rs.899.00    60      Active    
7     Yoga Mat                      Sports           FitGear        Rs.799.00    80      Active    
```

#### `search_product()`
- **Purpose:** Search products by name
- **User Input:** Product Name (partial or full)
- **Output:**
```
--- Search Product ---
Enter Product Name to Search: Headphones
ID    Product Name                  Category         Brand          Price        Stock   
-------------------------------------------------------------------------------------------
1     Wireless Headphones           Electronics      SoundMax       Rs.2999.00   50      
```

---

### Order Management Functions

#### `create_order()`
- **Purpose:** Create new customer order with items
- **User Input:** Customer ID, Payment Method, Product IDs & Quantities, Discount
- **Process:**
  1. Validates customer exists
  2. Creates order record with auto-generated Order ID
  3. Allows multiple items to be added
  4. Validates stock availability
  5. Updates inventory
  6. Calculates total and net amounts
- **Output:**
```
--- Create New Order ---
Enter Customer ID: 1
Enter Payment Method (Cash/Card/UPI/Net Banking): Card
Add item to order? (yes/no): yes
Enter Product ID: 1
Enter Quantity: 2
Item added! Subtotal: Rs. 5998.00

Add item to order? (yes/no): yes
Enter Product ID: 3
Enter Quantity: 1
Item added! Subtotal: Rs. 499.00

Add item to order? (yes/no): no
Enter Discount Amount (if any): 100

✓ Order created successfully!
Order ID: 1
Total Amount: Rs. 6497.00
Discount: Rs. 100.00
Net Amount: Rs. 6397.00
```

#### `view_orders()`
- **Purpose:** Display all orders with summary
- **Parameters:** None
- **Output:**
```
--- All Orders ---
Order ID   Customer             Date                 Total        Discount     Net          Status       Payment      
-----------------------------------------------------------------------------------------------------------------------
1          John Smith           2024-11-15 14:30:00  Rs.6497.00   Rs.100.00    Rs.6397.00   Confirmed    Completed    
```

#### `view_order_details()`
- **Purpose:** Display complete details of specific order
- **User Input:** Order ID
- **Output:**
```
--- Order Details ---
Enter Order ID: 1

================================================================================
                        ORDER DETAILS
================================================================================
Order ID: 1
Customer: John Smith
Order Date: 2024-11-15 14:30:00
Shipping Address: 123 Main St, New York
Payment Method: Card
Order Status: Confirmed
--------------------------------------------------------------------------------
Product                                  Quantity   Price        Subtotal     
--------------------------------------------------------------------------------
Wireless Headphones                      2          Rs.2999.00   Rs.5998.00   
Cotton T-Shirt                           1          Rs.499.00    Rs.499.00    
--------------------------------------------------------------------------------
Total Amount: Rs. 6497.00
Discount: Rs. 100.00
Net Amount: Rs. 6397.00
================================================================================
```

---

### Review Management Functions

#### `add_review()`
- **Purpose:** Add customer review for product
- **User Input:** Product ID, Customer ID, Rating (1-5), Review Text
- **Output:** `✓ Review added successfully!`

#### `view_product_reviews()`
- **Purpose:** Display all reviews for a product
- **User Input:** Product ID
- **Output:**
```
--- Product Reviews ---
Enter Product ID: 1
Customer               Rating   Review                                             Date      
--------------------------------------------------------------------------------------------
John Smith             5/5      Excellent sound quality and very comfortable!      2024-11-10
Mary Johnson           4/5      Good product, battery could be better              2024-11-12
```

---

### Report Functions

#### `generate_report()`
- **Purpose:** Generate comprehensive business report
- **Parameters:** None
- **Output:**
```
--- E-commerce Store Report ---

1. Total Products
Active Products: 7

2. Total Customers
Active Customers: 3

3. Total Orders
Total Orders: 1

4. Total Revenue
Total Revenue: Rs. 6397.00

5. Low Stock Products
No low stock products
```

---

### Menu Functions

#### `main_menu()`
- **Purpose:** Display interactive menu and handle user navigation
- **Features:**
  - Organized menu structure with 14 options
  - Continuous loop until exit
  - Input validation
  - Error handling
- **Menu Options:**
  1. Add Customer
  2. View All Customers
  3. Add Category
  4. View All Categories
  5. Add Product
  6. View All Products
  7. Search Product
  8. Create Order
  9. View All Orders
  10. View Order Details
  11. Add Product Review
  12. View Product Reviews
  13. Generate Store Report
  14. Exit

---

## Module Outputs

### Sample Data Initialization
```
✓ Database connected successfully!
✓ Tables created successfully!
✓ Sample data inserted successfully!
```

### Sample Output: View All Customers
```
--- All Customers ---
ID    Name                  Email                     Phone          City           Reg Date    Status    
---------------------------------------------------------------------------------------------------------
1     John Smith            john@email.com            1234567890     New York       2024-01-15  Active    
2     Mary Johnson          mary@email.com            9876543210     Los Angeles    2024-02-20  Active    
3     Robert Williams       robert@email.com          5551234567     Chicago        2024-03-10  Active    
```

### Sample Output: View All Products
```
--- All Products ---
ID    Product Name                  Category         Brand          Price        Stock   Status    
----------------------------------------------------------------------------------------------------
1     Wireless Headphones           Electronics      SoundMax       Rs.2999.00   50      Active    
2     Smartphone 5G                 Electronics      TechPhone      Rs.29999.00  30      Active    
3     Cotton T-Shirt                Clothing         FashionBrand   Rs.499.00    100     Active    
4     Denim Jeans                   Clothing         DenimCo        Rs.1299.00   75      Active    
5     Python Programming Book       Books            TechBooks      Rs.599.00    40      Active    
6     Electric Kettle               Home & Kitchen   HomeAppliances Rs.899.00    60      Active    
7     Yoga Mat                      Sports           FitGear        Rs.799.00    80      Active    
```

### Sample Output: Generate Report
```
--- E-commerce Store Report ---

1. Total Products
Active Products: 7

2. Total Customers
Active Customers: 3

3. Total Orders
Total Orders: 1

4. Total Revenue
Total Revenue: Rs. 6397.00

5. Low Stock Products
No low stock products
```

---

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- MySQL Server (5.7+)
- MySQL Connector for Python

### Step 1: Install Python Package
```bash
pip install mysql-connector-python
```

### Step 2: Database Setup
```sql
-- Create database
CREATE DATABASE mydb;

-- Use database
USE mydb;
```

### Step 3: Update Database Credentials
Edit the connection parameters in `estore_refactored.py`:
```python
connection = mysql.connector.connect(
    host='localhost',      # Your MySQL host
    user='root',           # Your MySQL username
    password='1234',       # Your MySQL password
    database='mydb'        # Your database name
)
```

### Step 4: Run Application
```bash
python estore_refactored.py
```

---

## Usage Guide

### Starting the Application
```bash
python estore_refactored.py
```

The application will:
1. Connect to MySQL database
2. Create all required tables
3. Insert sample data (if tables are empty)
4. Display the main menu

### Main Menu Navigation
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
```

### Typical Workflows

#### Workflow 1: Add and Manage Customer
1. Select Option 1 → Add Customer
2. Enter customer details
3. Select Option 2 → View All Customers to verify

#### Workflow 2: Add Products and Categories
1. Select Option 3 → Add Category
2. Select Option 5 → Add Product
3. Select Option 6 → View All Products to verify

#### Workflow 3: Create and View Orders
1. Select Option 8 → Create Order
2. Enter customer ID, payment method, and items
3. Select Option 9 → View All Orders to verify
4. Select Option 10 → View Order Details for specific order

#### Workflow 4: Generate Business Report
1. Select Option 13 → Generate Store Report
2. View all business metrics and inventory status

---

## Menu Structure

```
┌─ Main Menu
│
├─ CUSTOMER MANAGEMENT
│  ├─ 1. Add Customer
│  └─ 2. View All Customers
│
├─ CATEGORY MANAGEMENT
│  ├─ 3. Add Category
│  └─ 4. View All Categories
│
├─ PRODUCT MANAGEMENT
│  ├─ 5. Add Product
│  ├─ 6. View All Products
│  └─ 7. Search Product
│
├─ ORDER MANAGEMENT
│  ├─ 8. Create Order
│  ├─ 9. View All Orders
│  └─ 10. View Order Details
│
├─ REVIEW MANAGEMENT
│  ├─ 11. Add Product Review
│  └─ 12. View Product Reviews
│
├─ REPORTS
│  └─ 13. Generate Store Report
│
└─ 14. Exit
```

---

## Error Handling

The system includes comprehensive error handling for:
- Database connection failures
- Missing records
- Invalid input
- Insufficient stock
- Duplicate entries (email, SKU)
- Transaction rollbacks on failure

---

## Data Validation

The system validates:
- Customer existence before orders
- Product existence and stock availability
- Email uniqueness
- SKU uniqueness
- Payment method format
- Order status transitions
- Review ratings (1-5 scale)

---

## Sample Execution Scenario

### Step-by-Step Example

**1. Application Startup**
```
✓ Database connected successfully!
✓ Tables created successfully!
✓ Sample data inserted successfully!
```

**2. Main Menu Displayed**
```
============================================================
        E-COMMERCE STORE MANAGEMENT SYSTEM
============================================================
[Menu options displayed]
Enter your choice (1-14): 
```

**3. View All Customers (Option 2)**
```
--- All Customers ---
ID    Name                  Email                     Phone          City           Reg Date    Status    
---------------------------------------------------------------------------------------------------------
1     John Smith            john@email.com            1234567890     New York       2024-01-15  Active    
2     Mary Johnson          mary@email.com            9876543210     Los Angeles    2024-02-20  Active    
3     Robert Williams       robert@email.com          5551234567     Chicago        2024-03-10  Active    
```

**4. View All Products (Option 6)**
```
--- All Products ---
ID    Product Name                  Category         Brand          Price        Stock   Status    
----------------------------------------------------------------------------------------------------
1     Wireless Headphones           Electronics      SoundMax       Rs.2999.00   50      Active    
2     Smartphone 5G                 Electronics      TechPhone      Rs.29999.00  30      Active    
[More products listed]
```

**5. Create Order (Option 8)**
```
--- Create New Order ---
Enter Customer ID: 1
Enter Payment Method (Cash/Card/UPI/Net Banking): Card
Add item to order? (yes/no): yes
Enter Product ID: 1
Enter Quantity: 2
Item added! Subtotal: Rs. 5998.00

Add item to order? (yes/no): no
Enter Discount Amount (if any): 100

✓ Order created successfully!
Order ID: 1
Total Amount: Rs. 6497.00
Discount: Rs. 100.00
Net Amount: Rs. 6397.00
```

**6. Generate Report (Option 13)**
```
--- E-commerce Store Report ---

1. Total Products
Active Products: 7

2. Total Customers
Active Customers: 3

3. Total Orders
Total Orders: 1

4. Total Revenue
Total Revenue: Rs. 6397.00

5. Low Stock Products
No low stock products
```

---

## Advantages of Function-Based Approach

✓ **Modularity** - Each function has single responsibility  
✓ **Reusability** - Functions can be called independently  
✓ **Maintainability** - Easy to update and debug individual functions  
✓ **Testability** - Functions can be unit tested  
✓ **Readability** - Clear function names and documentation  
✓ **Scalability** - Easy to add new functions for new features  

---

## Future Enhancements

- User authentication system
- Advanced search and filtering
- Inventory notifications
- Email notifications
- Export reports to CSV/PDF
- Web interface with Flask/Django
- API endpoints for mobile apps
- Advanced analytics and charts
- Payment gateway integration

---

## Support & Documentation

For additional support or questions:
- Refer to function docstrings in code
- Check database schema documentation
- Review sample workflow examples
- Test with provided sample data

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-10 | Initial class-based implementation |
| 2.0 | 2026-01 | Refactored to functions and menu-driven approach |

---

**End of Documentation**

Generated: January 2026  
System: E-Commerce Store Management System v2.0
