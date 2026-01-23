# 🏨 Hotel Management System

## Overview
A comprehensive hotel management system built with Python and MySQL. It provides complete functionality for managing customer reservations, room inventory, services, and billing operations.

## Features

### 1. **Customer Management**
- Register new guests with personal details
- Update customer information
- Track check-in/check-out dates
- Maintain customer profile with ID proof verification

### 2. **Room Management**
- Add and manage room inventory
- Track room types (Single, Double, Suite, Deluxe)
- Set pricing per night
- Monitor room availability status
- Allocate rooms by floor level

### 3. **Booking System**
- Book rooms for customers
- Automatic calculation of stay duration
- Real-time cost calculation (nights × rate)
- Booking confirmation and tracking

### 4. **Service Management**
- Request additional services (Room Service, Laundry, etc.)
- Track service status
- Maintain service costs

### 5. **Billing & Checkout**
- Generate itemized bills
- Track payment status
- Calculate tax on services
- Generate receipts

## Database Schema

### Tables
```sql
-- Customers Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(255),
    city VARCHAR(50),
    country VARCHAR(50),
    id_proof VARCHAR(50),
    check_in_date DATE,
    check_out_date DATE,
    status VARCHAR(20)
)

-- Rooms Table
CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) UNIQUE,
    room_type VARCHAR(50),
    capacity INT,
    price_per_night FLOAT,
    status VARCHAR(20),
    floor INT,
    description VARCHAR(255)
)

-- Bookings Table
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    room_id INT,
    check_in_date DATE,
    check_out_date DATE,
    number_of_nights INT,
    total_cost FLOAT,
    status VARCHAR(20),
    booking_date DATE,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(room_id) REFERENCES rooms(room_id)
)

-- Services Table
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    service_name VARCHAR(100),
    service_type VARCHAR(50),
    cost FLOAT,
    date_requested DATE,
    status VARCHAR(20),
    FOREIGN KEY(booking_id) REFERENCES bookings(booking_id)
)

-- Bills Table
CREATE TABLE bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    room_charges FLOAT,
    service_charges FLOAT,
    tax FLOAT,
    total_amount FLOAT,
    payment_status VARCHAR(20),
    bill_date DATE,
    FOREIGN KEY(booking_id) REFERENCES bookings(booking_id)
)
```

## Main Features in Code

### Key Methods

#### Customer Operations
- `add_customer()` - Register new guest
- `view_all_customers()` - List all customers
- `search_customer()` - Find customer by ID
- `update_customer()` - Modify customer details
- `delete_customer()` - Remove customer record

#### Room Operations
- `add_room()` - Add new room to inventory
- `view_all_rooms()` - Display all rooms
- `view_available_rooms()` - Show vacant rooms
- `update_room_status()` - Change room availability

#### Booking Operations
- `book_room()` - Create new reservation
- `view_bookings()` - List all bookings
- `cancel_booking()` - Cancel reservation
- `update_booking()` - Modify booking details

#### Service & Billing
- `request_service()` - Order additional services
- `view_services()` - Display services ordered
- `checkout_room()` - Process checkout and billing
- `view_bills()` - Display bills

## Installation & Setup

```bash
# 1. Install dependencies
pip install mysql-connector-python

# 2. Ensure MySQL is running
# 3. Create database
mysql -u root -p
CREATE DATABASE mydb;

# 4. Run the system
python hotelms.py
```

## Usage

```python
from hotelms import HotelManagementSystem

# Initialize system
hotel = HotelManagementSystem()

# Add a customer
hotel.add_customer()

# Add rooms
hotel.add_room()

# View available rooms
hotel.view_available_rooms()

# Book a room
hotel.book_room()

# Checkout and generate bill
hotel.checkout_room()
```

## Menu Options

```
HOTEL MANAGEMENT SYSTEM
═══════════════════════════

1. Customer Management
   - Add Customer
   - View All Customers
   - Search Customer
   - Update Customer
   - Delete Customer

2. Room Management
   - Add Room
   - View All Rooms
   - View Available Rooms
   - Update Room Status

3. Booking Management
   - Book Room
   - View Bookings
   - Cancel Booking
   - Update Booking

4. Services
   - Request Service
   - View Services

5. Billing
   - Checkout Room
   - View Bills

6. Reports
   - Revenue Report
   - Occupancy Report
   - Guest Report

7. Exit
```

## Sample Data

The system initializes with sample data:
- **5 Rooms** with different types and pricing
- **Sample Customers** for demonstration
- **Bookings** showing various scenarios

## Error Handling

- Database connection errors
- Invalid input validation
- Date format validation
- Room availability checks
- Booking conflict detection

## Reports Generated

1. **Revenue Report** - Total income from bookings
2. **Occupancy Report** - Room utilization percentage
3. **Guest Report** - Guest statistics
4. **Booking Summary** - Bookings by date/room
5. **Billing Summary** - Payment status overview

## Technical Details

| Aspect | Details |
|--------|---------|
| Language | Python 3.7+ |
| Database | MySQL |
| Tables | 6 main tables |
| CRUD Operations | Full support |
| Authentication | Database connection |
| Data Validation | Input validation implemented |
| Error Handling | Try-catch mechanism |

## Sample Operations

### Add a Room
```
Room Number: 101
Room Type: Deluxe
Capacity: 2
Price Per Night: 5000
Floor: 1
Description: Luxury room with sea view
✓ Room added successfully!
```

### Book a Room
```
Customer ID: 1
Room ID: 1
Check-in: 2026-01-25
Check-out: 2026-01-30
Number of nights: 5
Total Cost: ₹25000
✓ Room booked successfully!
```

### Generate Bill
```
Booking ID: 1
Room Charges: ₹25000
Service Charges: ₹2000
Tax (5%): ₹1350
Total Amount: ₹28350
✓ Bill generated successfully!
```

## Best Practices

1. **Data Backup** - Regular database backups
2. **Validation** - All inputs are validated
3. **Transactions** - Database transactions for data integrity
4. **Error Messages** - Clear user-friendly error messages
5. **Security** - SQL injection prevention using parameterized queries

## Troubleshooting

### Database Connection Error
```
Error: Can't connect to MySQL server
Solution: 
- Verify MySQL server is running
- Check host, user, password configuration
- Ensure database 'mydb' exists
```

### Room Not Available
```
Error: Room is already booked
Solution:
- Check room status
- Select a different room
- Adjust check-in/check-out dates
```

## Future Enhancements

- Online payment integration
- Email confirmation sending
- Guest feedback system
- Loyalty program
- Multi-language support
- Web interface (Flask/Django)
- Mobile app integration

## Academic Applications

This system is ideal for:
- Database design learning
- SQL operations practice
- Python OOP concepts
- Business logic implementation
- Project submission (Class 11/12)

## License

Educational use - CBSE Computer Science Curriculum

---

**Last Updated**: January 2026

For queries, refer to the code comments or system documentation.
