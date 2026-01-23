"""
Railway Ticket Reservation System
A menu-driven console application for managing train reservations
"""

import os
import csv
from datetime import datetime

# File names for data storage
PASSENGERS_FILE = "passengers.csv"
TRAINS_FILE = "trains.csv"
BOOKINGS_FILE = "bookings.csv"
TICKET_COUNTER_FILE = "ticket_counter.txt"


def initialize_files():
    """Initialize data files with default values if they don't exist"""
    
    # Create trains file with sample data
    if not os.path.exists(TRAINS_FILE):
        with open(TRAINS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['TrainNumber', 'TrainName', 'Source', 'Destination', 'AvailableSeats', 'Fare'])
            writer.writerow(['TR001', 'Rajdhani Express', 'Delhi', 'Mumbai', 100, 1500])
            writer.writerow(['TR002', 'Shatabdi Express', 'Delhi', 'Jaipur', 80, 800])
            writer.writerow(['TR003', 'Duronto Train', 'Mumbai', 'Bangalore', 120, 2000])
            writer.writerow(['TR004', 'Express Train', 'Bangalore', 'Chennai', 95, 600])
            writer.writerow(['TR005', 'Local Train', 'Delhi', 'Agra', 150, 500])
    
    # Create passengers file with header if it doesn't exist
    if not os.path.exists(PASSENGERS_FILE):
        with open(PASSENGERS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['PassengerId', 'Name', 'Age', 'Gender', 'Phone', 'Email'])
    
    # Create bookings file with header if it doesn't exist
    if not os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['TicketNumber', 'PassengerId', 'TrainNumber', 'BookingDate', 'BookingStatus'])
    
    # Create ticket counter file if it doesn't exist
    if not os.path.exists(TICKET_COUNTER_FILE):
        with open(TICKET_COUNTER_FILE, 'w') as f:
            f.write('5000')


def get_next_ticket_number():
    """Generate next ticket number"""
    with open(TICKET_COUNTER_FILE, 'r') as f:
        ticket_num = int(f.read())
    
    ticket_num += 1
    with open(TICKET_COUNTER_FILE, 'w') as f:
        f.write(str(ticket_num))
    
    return f'TKT{ticket_num}'


def get_next_passenger_id():
    """Generate next passenger ID"""
    if not os.path.exists(PASSENGERS_FILE):
        return 'P001'
    
    with open(PASSENGERS_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        rows = list(reader)
    
    if len(rows) == 0:
        return 'P001'
    
    last_id = rows[-1][0]
    num = int(last_id[1:]) + 1
    return f'P{num:03d}'


def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("RAILWAY TICKET RESERVATION SYSTEM".center(60))
    print("="*60)
    print("\n1. Passenger Management")
    print("2. Train Management")
    print("3. Ticket Reservation")
    print("4. Ticket Cancellation")
    print("5. View Reports")
    print("6. Exit")
    print("\n" + "-"*60)


def add_passenger():
    """Add new passenger to the system"""
    print("\n" + "="*60)
    print("ADD NEW PASSENGER".center(60))
    print("="*60 + "\n")
    
    try:
        passenger_id = get_next_passenger_id()
        name = input("Enter Passenger Name: ").strip()
        
        if not name or len(name) < 2:
            print("\nError: Name must be at least 2 characters long.")
            return
        
        age = input("Enter Age: ").strip()
        try:
            age = int(age)
            if age < 1 or age > 120:
                print("\nError: Age must be between 1 and 120.")
                return
        except ValueError:
            print("\nError: Age must be a valid number.")
            return
        
        gender = input("Enter Gender (M/F/Other): ").strip().upper()
        if gender not in ['M', 'F', 'OTHER']:
            print("\nError: Please enter M, F, or Other.")
            return
        
        phone = input("Enter Phone Number: ").strip()
        if not phone.isdigit() or len(phone) < 10:
            print("\nError: Phone number must be at least 10 digits.")
            return
        
        email = input("Enter Email Address: ").strip()
        if '@' not in email or '.' not in email:
            print("\nError: Please enter a valid email address.")
            return
        
        # Add to file
        with open(PASSENGERS_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([passenger_id, name, age, gender, phone, email])
        
        print("\n" + "-"*60)
        print("Success: Passenger added successfully!")
        print(f"Passenger ID: {passenger_id}")
        print("-"*60)
        
    except Exception as e:
        print(f"\nError: {str(e)}")


def view_passenger():
    """View passenger details by ID"""
    print("\n" + "="*60)
    print("VIEW PASSENGER DETAILS".center(60))
    print("="*60 + "\n")
    
    try:
        passenger_id = input("Enter Passenger ID (e.g., P001): ").strip().upper()
        
        found = False
        with open(PASSENGERS_FILE, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            for row in reader:
                if row[0] == passenger_id:
                    found = True
                    print("\n" + "-"*60)
                    print("PASSENGER DETAILS")
                    print("-"*60)
                    print(f"Passenger ID: {row[0]}")
                    print(f"Name: {row[1]}")
                    print(f"Age: {row[2]}")
                    print(f"Gender: {row[3]}")
                    print(f"Phone: {row[4]}")
                    print(f"Email: {row[5]}")
                    print("-"*60)
                    break
        
        if not found:
            print(f"\nError: Passenger with ID {passenger_id} not found.")
    
    except Exception as e:
        print(f"\nError: {str(e)}")


def passenger_menu():
    """Passenger management submenu"""
    while True:
        print("\n" + "="*60)
        print("PASSENGER MANAGEMENT".center(60))
        print("="*60)
        print("\n1. Add New Passenger")
        print("2. View Passenger Details")
        print("3. Back to Main Menu")
        print("\n" + "-"*60)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            add_passenger()
        elif choice == '2':
            view_passenger()
        elif choice == '3':
            break
        else:
            print("\nError: Invalid choice. Please enter 1, 2, or 3.")


def view_trains():
    """Display all available trains"""
    print("\n" + "="*60)
    print("AVAILABLE TRAINS".center(60))
    print("="*60 + "\n")
    
    try:
        with open(TRAINS_FILE, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            print(f"{'Train No':<12} {'Train Name':<20} {'Source':<15} {'Dest':<15} {'Seats':<8} {'Fare':<8}")
            print("-"*80)
            
            trains = list(reader)
            if not trains:
                print("No trains available.")
            else:
                for row in trains:
                    print(f"{row[0]:<12} {row[1]:<20} {row[2]:<15} {row[3]:<15} {row[4]:<8} Rs.{row[5]:<6}")
            
            print("-"*80)
    
    except Exception as e:
        print(f"\nError: {str(e)}")


def get_train_details(train_number):
    """Get train details by train number"""
    try:
        with open(TRAINS_FILE, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            
            for row in reader:
                if row[0] == train_number:
                    return {
                        'number': row[0],
                        'name': row[1],
                        'source': row[2],
                        'destination': row[3],
                        'seats': int(row[4]),
                        'fare': int(row[5])
                    }
    except Exception as e:
        print(f"Error: {str(e)}")
    
    return None


def train_menu():
    """Train management submenu"""
    while True:
        print("\n" + "="*60)
        print("TRAIN MANAGEMENT".center(60))
        print("="*60)
        print("\n1. View All Trains")
        print("2. View Train Details")
        print("3. Back to Main Menu")
        print("\n" + "-"*60)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            view_trains()
        elif choice == '2':
            try:
                train_num = input("\nEnter Train Number: ").strip().upper()
                train = get_train_details(train_num)
                
                if train:
                    print("\n" + "-"*60)
                    print("TRAIN DETAILS")
                    print("-"*60)
                    print(f"Train Number: {train['number']}")
                    print(f"Train Name: {train['name']}")
                    print(f"Source: {train['source']}")
                    print(f"Destination: {train['destination']}")
                    print(f"Available Seats: {train['seats']}")
                    print(f"Ticket Fare: Rs. {train['fare']}")
                    print("-"*60)
                else:
                    print(f"\nError: Train {train_num} not found.")
            except Exception as e:
                print(f"\nError: {str(e)}")
        elif choice == '3':
            break
        else:
            print("\nError: Invalid choice. Please enter 1, 2, or 3.")


def book_ticket():
    """Book a ticket for passenger"""
    print("\n" + "="*60)
    print("BOOK TICKET".center(60))
    print("="*60 + "\n")
    
    try:
        # Get passenger ID
        passenger_id = input("Enter Passenger ID: ").strip().upper()
        
        # Verify passenger exists
        passenger_exists = False
        with open(PASSENGERS_FILE, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[0] == passenger_id:
                    passenger_exists = True
                    break
        
        if not passenger_exists:
            print(f"\nError: Passenger {passenger_id} not found. Please register first.")
            return
        
        # Display trains
        view_trains()
        
        # Get train number
        train_num = input("\nEnter Train Number for booking: ").strip().upper()
        
        train = get_train_details(train_num)
        if not train:
            print(f"\nError: Train {train_num} not found.")
            return
        
        # Check availability
        if train['seats'] <= 0:
            print(f"\nError: No seats available on train {train_num}.")
            return
        
        # Generate ticket and update data
        ticket_num = get_next_ticket_number()
        booking_date = datetime.now().strftime("%d-%m-%Y")
        
        # Add booking
        with open(BOOKINGS_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([ticket_num, passenger_id, train_num, booking_date, 'Confirmed'])
        
        # Update available seats
        update_train_seats(train_num, train['seats'] - 1)
        
        print("\n" + "-"*60)
        print("BOOKING CONFIRMED")
        print("-"*60)
        print(f"Ticket Number: {ticket_num}")
        print(f"Passenger ID: {passenger_id}")
        print(f"Train Number: {train_num}")
        print(f"Train Name: {train['name']}")
        print(f"From {train['source']} to {train['destination']}")
        print(f"Ticket Fare: Rs. {train['fare']}")
        print(f"Booking Date: {booking_date}")
        print("-"*60)
    
    except Exception as e:
        print(f"\nError: {str(e)}")


def update_train_seats(train_number, new_seat_count):
    """Update available seats for a train"""
    try:
        trains = []
        with open(TRAINS_FILE, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            trains.append(header)
            
            for row in reader:
                if row[0] == train_number:
                    row[4] = str(new_seat_count)
                trains.append(row)
        
        with open(TRAINS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(trains)
    
    except Exception as e:
        print(f"Error updating seats: {str(e)}")


def cancel_ticket():
    """Cancel a booked ticket"""
    print("\n" + "="*60)
    print("CANCEL TICKET".center(60))
    print("="*60 + "\n")
    
    try:
        ticket_num = input("Enter Ticket Number to cancel: ").strip().upper()
        
        # Find booking
        booking_found = False
        train_num = None
        
        bookings = []
        with open(BOOKINGS_FILE, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            bookings.append(header)
            
            for row in reader:
                if row[0] == ticket_num and row[4] == 'Confirmed':
                    booking_found = True
                    train_num = row[2]
                    row[4] = 'Cancelled'
                bookings.append(row)
        
        if not booking_found:
            print(f"\nError: Active booking with ticket {ticket_num} not found.")
            return
        
        # Update bookings file
        with open(BOOKINGS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(bookings)
        
        # Restore seats
        train = get_train_details(train_num)
        if train:
            update_train_seats(train_num, train['seats'] + 1)
        
        print("\n" + "-"*60)
        print("CANCELLATION SUCCESSFUL")
        print("-"*60)
        print(f"Ticket Number: {ticket_num}")
        print(f"Train Number: {train_num}")
        print(f"Status: Cancelled")
        print("-"*60)
    
    except Exception as e:
        print(f"\nError: {str(e)}")


def view_all_bookings():
    """View all booked tickets"""
    print("\n" + "="*60)
    print("ALL BOOKINGS".center(60))
    print("="*60 + "\n")
    
    try:
        with open(BOOKINGS_FILE, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            bookings = list(reader)
            
            if not bookings:
                print("No bookings found.")
                return
            
            print(f"{'Ticket No':<12} {'Passenger ID':<12} {'Train No':<10} {'Booking Date':<15} {'Status':<12}")
            print("-"*65)
            
            confirmed_count = 0
            cancelled_count = 0
            
            for row in bookings:
                print(f"{row[0]:<12} {row[1]:<12} {row[2]:<10} {row[3]:<15} {row[4]:<12}")
                if row[4] == 'Confirmed':
                    confirmed_count += 1
                elif row[4] == 'Cancelled':
                    cancelled_count += 1
            
            print("-"*65)
            print(f"Total Confirmed Bookings: {confirmed_count}")
            print(f"Total Cancelled Bookings: {cancelled_count}")
            print(f"Total Bookings: {len(bookings)}")
    
    except Exception as e:
        print(f"\nError: {str(e)}")


def view_available_seats():
    """View available seats on all trains"""
    print("\n" + "="*60)
    print("AVAILABLE SEATS REPORT".center(60))
    print("="*60 + "\n")
    
    try:
        with open(TRAINS_FILE, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            print(f"{'Train No':<12} {'Train Name':<20} {'Source':<15} {'Destination':<15} {'Available Seats':<15}")
            print("-"*80)
            
            trains = list(reader)
            
            if not trains:
                print("No trains available.")
                return
            
            for row in trains:
                available = int(row[4])
                if available > 0:
                    status = "Available"
                else:
                    status = "Full"
                
                print(f"{row[0]:<12} {row[1]:<20} {row[2]:<15} {row[3]:<15} {available:<15} ({status})")
            
            print("-"*80)
    
    except Exception as e:
        print(f"\nError: {str(e)}")


def reports_menu():
    """Reports submenu"""
    while True:
        print("\n" + "="*60)
        print("REPORTS".center(60))
        print("="*60)
        print("\n1. View All Bookings")
        print("2. View Available Seats")
        print("3. Back to Main Menu")
        print("\n" + "-"*60)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            view_all_bookings()
        elif choice == '2':
            view_available_seats()
        elif choice == '3':
            break
        else:
            print("\nError: Invalid choice. Please enter 1, 2, or 3.")


def main():
    """Main function - program entry point"""
    initialize_files()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            passenger_menu()
        elif choice == '2':
            train_menu()
        elif choice == '3':
            book_ticket()
        elif choice == '4':
            cancel_ticket()
        elif choice == '5':
            reports_menu()
        elif choice == '6':
            print("\n" + "="*60)
            print("Thank you for using Railway Reservation System".center(60))
            print("="*60 + "\n")
            break
        else:
            print("\nError: Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
