# 🚆 Railway Reservation System

## Overview
A comprehensive railway ticket reservation system built with Python using CSV data storage. It manages passengers, trains, and ticket bookings with complete functionality for train reservations and seat management.

## Features

### 1. **Passenger Management**
- Register new passengers
- Store passenger details (Name, Age, Gender, Contact)
- Search passengers by ID or name
- Update passenger information
- Maintain passenger history

### 2. **Train Management**
- Add new trains to database
- Store train information (Name, Route, Seats, Fare)
- Update train details
- View available trains
- Track available seats

### 3. **Ticket Booking**
- Book tickets for passengers
- Automatic ticket number generation
- Check seat availability
- Confirm bookings
- Display booking confirmation

### 4. **Ticket Cancellation**
- Cancel existing bookings
- Refund calculations
- Update seat availability
- Cancellation history

### 5. **Booking Reports**
- View booking history
- Filter by train/passenger
- Revenue reports
- Occupancy analysis
- Booking statistics

### 6. **Query Options**
- Check train status
- View passenger bookings
- View available trains
- Search bookings

## Data Storage Structure

### CSV Files

#### trains.csv
```
TrainNumber,TrainName,Source,Destination,AvailableSeats,Fare
TR001,Rajdhani Express,Delhi,Mumbai,100,1500
TR002,Shatabdi Express,Delhi,Jaipur,80,800
TR003,Duronto Train,Mumbai,Bangalore,120,2000
```

#### passengers.csv
```
PassengerId,Name,Age,Gender,Phone,Email
P001,Raj Kumar,35,Male,9876543210,raj@email.com
P002,Priya Singh,28,Female,9876543211,priya@email.com
```

#### bookings.csv
```
TicketNumber,PassengerId,TrainNumber,BookingDate,BookingStatus
TKT5001,P001,TR001,2026-01-21,Confirmed
TKT5002,P002,TR002,2026-01-21,Confirmed
```

## Main Features in Code

### Key Methods

#### Passenger Operations
- `add_passenger()` - Register new passenger
- `view_all_passengers()` - List all passengers
- `search_passenger()` - Find by ID or name
- `update_passenger()` - Modify details
- `delete_passenger()` - Remove record

#### Train Operations
- `add_train()` - Add new train
- `view_all_trains()` - List trains
- `search_train()` - Find by number/name
- `update_train()` - Modify train info
- `check_seat_availability()` - Check seats

#### Booking Operations
- `book_ticket()` - Create new booking
- `view_bookings()` - List all bookings
- `cancel_ticket()` - Cancel booking
- `passenger_bookings()` - Get passenger bookings

#### Reports
- `booking_report()` - All bookings
- `revenue_report()` - Revenue analysis
- `occupancy_report()` - Seat occupancy
- `train_report()` - Train statistics

## Installation & Setup

```bash
# 1. No external database required - uses CSV files
# 2. Python 3.7+ required
# 3. Run the system
python railway_reservation.py
```

## Usage

```python
from railway_reservation import *

# Initialize files
initialize_files()

# Add passenger
add_passenger()
# Output: Passenger added! ID: P001

# Book ticket
book_ticket()

# View bookings
view_bookings()

# Cancel ticket
cancel_ticket()
```

## Menu Options

```
RAILWAY TICKET RESERVATION SYSTEM
═════════════════════════════════════════

1. Passenger Management
   - Add New Passenger
   - View All Passengers
   - Search Passenger
   - Update Passenger
   - Delete Passenger

2. Train Management
   - Add New Train
   - View All Trains
   - Search Train
   - Update Train Details
   - Check Seat Availability

3. Ticket Reservation
   - Book Ticket
   - View All Bookings
   - Passenger Bookings
   - Update Booking

4. Ticket Cancellation
   - Cancel Ticket
   - Cancellation History
   - Refund Information

5. Reports
   - Booking Report
   - Revenue Report
   - Occupancy Report
   - Train-wise Report
   - Passenger Report

6. Exit
```

## Sample Data

The system initializes with sample data:
- **5 Sample Trains** with different routes and fares
- **Sample Passengers** for demonstration
- **Sample Bookings** showing various scenarios

### Sample Trains
```
Train Number | Name                | Route            | Seats | Fare
TR001        | Rajdhani Express    | Delhi-Mumbai     | 100   | ₹1500
TR002        | Shatabdi Express    | Delhi-Jaipur     | 80    | ₹800
TR003        | Duronto Train       | Mumbai-Bangalore | 120   | ₹2000
TR004        | Express Train       | Bangalore-Chennai| 95    | ₹600
TR005        | Local Train         | Delhi-Agra       | 150   | ₹500
```

## Sample Operations

### Add New Passenger
```
═════════════════════════════════════════
ADD NEW PASSENGER
═════════════════════════════════════════

Enter passenger name: Raj Kumar
Enter age: 35
Enter gender: Male
Enter phone number: 9876543210
Enter email: raj@email.com

✓ Passenger added successfully!
Passenger ID: P001
```

### View All Trains
```
═════════════════════════════════════════
AVAILABLE TRAINS
═════════════════════════════════════════

Train# | Name                 | Source      | Destination | Seats | Fare
────────────────────────────────────────────────────────────────────────
TR001  | Rajdhani Express     | Delhi       | Mumbai      | 95    | ₹1500
TR002  | Shatabdi Express     | Delhi       | Jaipur      | 75    | ₹800
TR003  | Duronto Train        | Mumbai      | Bangalore   | 118   | ₹2000
TR004  | Express Train        | Bangalore   | Chennai     | 90    | ₹600
TR005  | Local Train          | Delhi       | Agra        | 145   | ₹500
```

### Book Ticket
```
═════════════════════════════════════════
BOOK TICKET
═════════════════════════════════════════

Enter passenger ID: P001
Enter train number: TR001
Enter number of seats: 2

═════════════════════════════════════════
        BOOKING CONFIRMATION
═════════════════════════════════════════

Ticket Number: TKT5001
Passenger ID: P001
Passenger Name: Raj Kumar
Train: TR001 (Rajdhani Express)
Route: Delhi → Mumbai
Date: 2026-01-21
Number of Seats: 2
Fare per Seat: ₹1500
Total Fare: ₹3000

Booking Status: Confirmed
Booking Date: 21-01-2026

═════════════════════════════════════════

✓ Ticket booked successfully!
```

### Cancel Ticket
```
═════════════════════════════════════════
CANCEL TICKET
═════════════════════════════════════════

Enter ticket number: TKT5001

Ticket Details:
Ticket Number: TKT5001
Passenger: Raj Kumar
Train: TR001 (Rajdhani Express)
Original Fare: ₹3000
Cancellation Charge (10%): ₹300
Refund Amount: ₹2700

✓ Ticket cancelled successfully!
Refund amount: ₹2700
```

### Booking Report
```
═════════════════════════════════════════
BOOKING REPORT
═════════════════════════════════════════

Total Bookings: 15
Confirmed Bookings: 14
Cancelled Bookings: 1

Train-wise Bookings:
TR001 (Rajdhani Express): 5 bookings
TR002 (Shatabdi Express): 3 bookings
TR003 (Duronto Train): 4 bookings
TR004 (Express Train): 2 bookings
TR005 (Local Train): 1 booking

═════════════════════════════════════════
```

### Revenue Report
```
═════════════════════════════════════════
REVENUE REPORT
═════════════════════════════════════════

Total Revenue: ₹42,000
From Confirmed Bookings: ₹42,000
Refunds Paid: ₹2,700

Train-wise Revenue:
TR001: ₹7,500
TR002: ₹2,400
TR003: ₹8,000
TR004: ₹1,200
TR005: ₹500

Average Booking Value: ₹2,800
Booking Count: 15

═════════════════════════════════════════
```

### Occupancy Report
```
═════════════════════════════════════════
OCCUPANCY REPORT
═════════════════════════════════════════

Train# | Name                | Total | Booked | Avail. | Occupancy
────────────────────────────────────────────────────────────────────
TR001  | Rajdhani Express    | 100   | 5      | 95     | 5%
TR002  | Shatabdi Express    | 80    | 3      | 77     | 3.75%
TR003  | Duronto Train       | 120   | 2      | 118    | 1.67%
TR004  | Express Train       | 95    | 2      | 93     | 2.1%
TR005  | Local Train         | 150   | 1      | 149    | 0.67%

Total Seats: 545
Total Booked: 13
Overall Occupancy: 2.39%

═════════════════════════════════════════
```

## Technical Details

| Aspect | Details |
|--------|---------|
| Language | Python 3.7+ |
| Storage | CSV Files |
| Files | 4 CSV files + 1 counter file |
| CRUD Operations | Full support |
| Data Validation | Input validation implemented |
| Error Handling | Try-catch mechanism |
| ID Generation | Auto-generated IDs |

## ID Generation

### Ticket Number
```
Format: TKT + 4-digit counter
Example: TKT5001, TKT5002, TKT5003
```

### Passenger ID
```
Format: P + 3-digit number
Example: P001, P002, P003
```

### Train Number
```
Format: TR + 3-digit number
Example: TR001, TR002, TR003
```

## Validation Rules

### Passenger Data
```
- Name: Required, alphabetic characters
- Age: 5-100 years
- Gender: Male/Female/Other
- Phone: 10 digits
- Email: Valid email format
```

### Train Data
```
- Train Name: Required
- Source & Destination: Different cities
- Available Seats: Greater than 0
- Fare: Positive amount
```

### Booking Rules
```
- Valid passenger ID
- Valid train number
- Seats available
- No duplicate bookings for same date
```

## File Operations

### CSV File Handling
- Auto-creation if missing
- Header row included
- Comma-separated format
- UTF-8 encoding

### Data Persistence
- Automatic save on changes
- File backup on modification
- Counter file for ticket numbers

## Error Handling

```
Error: Insufficient seats available
Solution: Choose different train or date

Error: Invalid passenger ID
Solution: Register passenger first

Error: Train not found
Solution: Check train number

Error: Cannot cancel - already cancelled
Solution: Use valid ticket number
```

## Refund Policy

```
Cancellation Charges: 10% of ticket fare
Refund Amount = Ticket Fare - Cancellation Charges

Example:
Original Fare: ₹1500
Cancellation Charge (10%): ₹150
Refund Amount: ₹1350
```

## Reports Generated

1. **Booking Report** - All bookings with details
2. **Revenue Report** - Total income analysis
3. **Occupancy Report** - Seat utilization
4. **Train Report** - Train statistics
5. **Passenger Report** - Passenger statistics
6. **Cancellation Report** - Cancellations and refunds

## Best Practices

1. **Data Verification** - Verify passenger info
2. **Booking Confirmation** - Keep confirmation number
3. **Seat Management** - Track availability
4. **Revenue Tracking** - Monitor income
5. **Backup Files** - Keep CSV backups

## Troubleshooting

### CSV File Not Found
```
Solution:
- Run initialize_files() first
- Check file permissions
- Verify file path
```

### Duplicate Ticket Numbers
```
Solution:
- Check ticket_counter.txt
- Reset counter if corrupted
- Initialize files fresh
```

### Cannot Book - Seats Full
```
Solution:
- Check available trains
- Choose different date
- Select alternative route
```

## Academic Applications

Ideal for learning:
- CSV file operations
- ID generation and tracking
- Reservation systems
- Report generation
- Business logic
- Project submission (Class 11/12)

## Future Enhancements

- Database migration (MySQL)
- Web booking interface
- Mobile app
- Payment integration
- Email confirmations
- SMS notifications
- Train tracking
- Seat selection UI
- Dynamic pricing
- Group bookings

## License

Educational use - CBSE Computer Science Curriculum

---

**Last Updated**: January 2026

For queries, refer to the code comments or system documentation.
