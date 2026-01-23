# Railway Ticket Reservation System

## Project Title
**Railway Ticket Reservation System - A Console-Based Application**

---

## Project Description

The Railway Ticket Reservation System is a menu-driven, console-based application developed in Python. It is designed to manage passenger information, train details, ticket reservations, and cancellations for a railway network. This system provides an easy-to-use interface suitable for railway staff and ticket booking counters.

The system maintains persistent data using CSV file storage, ensuring that all information is retained between program runs. It follows the CBSE Computer Science curriculum standards and is designed for Class 11/12 students to understand practical application development.

---

## Features

### 1. Passenger Management
- Add new passenger with complete details (Name, Age, Gender, Phone, Email)
- View passenger details using unique Passenger ID
- Automatic passenger ID generation
- Input validation for all passenger fields
- Data persists in CSV file

### 2. Train Management
- View all available trains with complete details
- Display train information including:
  - Train Number
  - Train Name
  - Source and Destination
  - Available Seats
  - Ticket Fare
- View detailed information for specific trains
- Real-time seat availability update

### 3. Ticket Reservation Module
- Book tickets for registered passengers
- Automatic ticket number generation (TKT5001, TKT5002, etc.)
- Automatic seat count reduction after successful booking
- Prevents overbooking when seats are full
- Booking confirmation with all details
- Booking date recording

### 4. Ticket Cancellation Module
- Cancel existing ticket using ticket number
- Automatic seat count restoration
- Status update to "Cancelled" in records
- Prevents cancellation of already cancelled tickets
- Displays cancellation confirmation

### 5. Reports Module
- View all booked tickets with summary statistics
- Display confirmed and cancelled booking counts
- View available seats on all trains
- Real-time seat availability report
- Seat status indicator (Available/Full)

---

## Module Description

### Module 1: Initialization Module
**Functions:**
- `initialize_files()` - Creates required CSV files with default data
- Initializes trains with sample data
- Sets up passenger and booking records
- Creates ticket counter for ID generation

### Module 2: ID Generation Module
**Functions:**
- `get_next_ticket_number()` - Generates unique ticket numbers
- `get_next_passenger_id()` - Generates unique passenger IDs
- Maintains counters in files for persistence

### Module 3: Passenger Management Module
**Functions:**
- `add_passenger()` - Add new passenger to system
- `view_passenger()` - Retrieve passenger details by ID
- `passenger_menu()` - Submenu for passenger operations
- Validates: Name length, Age range, Gender format, Phone length, Email format

### Module 4: Train Management Module
**Functions:**
- `view_trains()` - Display all trains in formatted table
- `get_train_details()` - Retrieve train info by train number
- `train_menu()` - Submenu for train operations
- `update_train_seats()` - Update seat count after booking/cancellation

### Module 5: Ticket Reservation Module
**Functions:**
- `book_ticket()` - Create new ticket reservation
- Verifies passenger existence
- Checks seat availability
- Updates seat count automatically
- Generates booking confirmation

### Module 6: Cancellation Module
**Functions:**
- `cancel_ticket()` - Cancel existing booking
- Updates booking status to "Cancelled"
- Restores available seats
- Prevents duplicate cancellation

### Module 7: Reports Module
**Functions:**
- `view_all_bookings()` - Display all bookings with statistics
- `view_available_seats()` - Show seat availability on all trains
- `reports_menu()` - Submenu for report options

### Module 8: Menu Interface
**Functions:**
- `display_menu()` - Main menu display
- `main()` - Program entry point with main loop

---

## Data Storage Method

### File 1: passengers.csv
- **Fields:** PassengerId, Name, Age, Gender, Phone, Email
- **Storage:** Text-based CSV format
- **Purpose:** Stores all passenger information
- **Record Type:** One row per passenger

### File 2: trains.csv
- **Fields:** TrainNumber, TrainName, Source, Destination, AvailableSeats, Fare
- **Storage:** Text-based CSV format
- **Purpose:** Stores train information and seat availability
- **Record Type:** One row per train
- **Sample Data:** 5 pre-loaded trains

### File 3: bookings.csv
- **Fields:** TicketNumber, PassengerId, TrainNumber, BookingDate, BookingStatus
- **Storage:** Text-based CSV format
- **Purpose:** Stores ticket booking records
- **Record Type:** One row per booking

### File 4: ticket_counter.txt
- **Content:** Current ticket number counter
- **Purpose:** Maintains sequential ticket number generation
- **Format:** Plain text integer

### Data Persistence
- All data is saved immediately after each operation
- CSV format ensures compatibility and readability
- Data remains available between program sessions
- Easy to backup and transfer files

---

## How to Run the Program

### Prerequisites
- Python 3.x installed on your system
- Text editor or IDE (VS Code, PyCharm, IDLE, etc.)
- Command prompt or terminal access

### Installation Steps

1. **Download the file**
   - Save `railway_reservation.py` to your desired folder

2. **Navigate to the folder**
   ```
   cd path/to/your/folder
   ```

3. **Run the program**
   ```
   python railway_reservation.py
   ```

### Using the Program

1. **Main Menu appears with 6 options:**
   - Option 1: Passenger Management
   - Option 2: Train Management
   - Option 3: Ticket Reservation
   - Option 4: Ticket Cancellation
   - Option 5: View Reports
   - Option 6: Exit

2. **Select an option** by entering the corresponding number

3. **Follow the prompts** to enter required information

4. **Input validation** will guide you if any field is incorrect

5. **Success/Error messages** will confirm the operation status

---

## Limitations

1. **No User Authentication:** System does not require login/password
2. **Single File Submission:** All code in one Python file
3. **Basic Search:** Can only search passenger by ID, not by name
4. **No Advanced Filtering:** Reports show all records without date filtering
5. **Local Storage Only:** No database or online connectivity
6. **Console Only:** No graphical user interface
7. **No Transaction History:** Only current ticket status is shown
8. **No Email Integration:** Booking confirmations not sent via email
9. **No Payment Processing:** System assumes pre-payment
10. **Basic Error Handling:** Limited error recovery options

---

## Future Enhancements

1. **Database Integration**
   - Replace CSV files with MySQL/SQLite database
   - Improved data integrity and backup capabilities

2. **User Authentication**
   - Login system for staff and passengers
   - Role-based access control

3. **Advanced Search Features**
   - Search passenger by name
   - Filter bookings by date range
   - Train search by route

4. **Graphical User Interface**
   - Tkinter-based GUI
   - Web interface using Flask/Django

5. **Email Integration**
   - Automated booking confirmations
   - Cancellation receipts

6. **Payment Processing**
   - Online payment gateway integration
   - Ticket payment tracking

7. **Seat Mapping**
   - Visual seat layout display
   - Specific seat selection

8. **Reporting**
   - Generate PDF reports
   - Revenue analysis
   - Occupancy statistics

9. **Schedule Management**
   - Add train schedule/timing information
   - Display journey duration

10. **Mobile Application**
    - Mobile app for ticket booking
    - Real-time notification system

---

## Conclusion

The Railway Ticket Reservation System is a comprehensive, beginner-friendly application designed for educational purposes. It demonstrates fundamental programming concepts including:

- File handling and data persistence
- Menu-driven interface design
- Input validation and error handling
- CSV file manipulation
- Function-based programming approach
- Data organization and management

This system provides a solid foundation for understanding real-world applications and can be extended with advanced features. Students can use this project as a reference for practical file submission requirements in their Computer Science curriculum.

The system is fully functional, easy to understand, and ready for academic submission.

---

## Technical Specifications

- **Language:** Python 3.x
- **Paradigm:** Procedural Programming
- **Data Storage:** CSV Files (Text-based)
- **Interface:** Console/Terminal Based
- **File I/O:** Built-in Python libraries
- **Line Count:** Approximately 600+ lines
- **Modules:** 8 functional modules

---

## Usage Guidelines for Practical File

### For Class 11/12 Students:

1. **Understanding the Code:**
   - Study each function separately
   - Understand file handling operations
   - Learn menu-driven design pattern

2. **Testing the System:**
   - Test each module individually
   - Try various input combinations
   - Observe error messages for invalid inputs

3. **Documentation:**
   - Include this README in your practical file
   - Document your modifications (if any)
   - Keep sample outputs for reference

4. **Submission Requirements:**
   - Source code file (railway_reservation.py)
   - This README document
   - Sample output screenshots/text
   - Any modifications or enhancements made

---

**Status:** Complete and Ready for Submission
**Version:** 1.0
**Last Updated:** January 2026
