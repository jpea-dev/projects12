from mysql.connector import Error
import datetime
import mysql.connector

class HotelManagementSystem:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect_db()
    
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
        except Error as e:
            print(f"Error: {e}")
    
    def create_tables(self):
        try:
            # Customers Table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
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
                    status VARCHAR(20) DEFAULT 'Active'
                )
            ''')
            
            # Rooms Table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS rooms (
                    room_id INT AUTO_INCREMENT PRIMARY KEY,
                    room_number VARCHAR(10) UNIQUE NOT NULL,
                    room_type VARCHAR(50),
                    capacity INT,
                    price_per_night FLOAT,
                    status VARCHAR(20) DEFAULT 'Available',
                    floor INT,
                    description VARCHAR(255)
                )
            ''')
            
            # Bookings Table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS bookings (
                    booking_id INT AUTO_INCREMENT PRIMARY KEY,
                    customer_id INT,
                    room_id INT,
                    check_in_date DATE NOT NULL,
                    check_out_date DATE NOT NULL,
                    number_of_nights INT,
                    total_cost FLOAT,
                    status VARCHAR(20) DEFAULT 'Booked',
                    booking_date DATE,
                    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
                    FOREIGN KEY(room_id) REFERENCES rooms(room_id)
                )
            ''')
            
            # Services Table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS services (
                    service_id INT AUTO_INCREMENT PRIMARY KEY,
                    booking_id INT,
                    service_name VARCHAR(100),
                    service_type VARCHAR(50),
                    cost FLOAT,
                    date_requested DATE,
                    status VARCHAR(20) DEFAULT 'Pending',
                    description VARCHAR(255),
                    FOREIGN KEY(booking_id) REFERENCES bookings(booking_id)
                )
            ''')
            
            # Bills Table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS bills (
                    bill_id INT AUTO_INCREMENT PRIMARY KEY,
                    booking_id INT,
                    room_charges FLOAT,
                    service_charges FLOAT,
                    tax FLOAT,
                    total_amount FLOAT,
                    payment_status VARCHAR(20) DEFAULT 'Pending',
                    bill_date DATE,
                    FOREIGN KEY(booking_id) REFERENCES bookings(booking_id)
                )
            ''')
            
            self.connection.commit()
            print("✓ Tables created successfully!")
        except Error as e:
            print(f"Table creation error: {e}")
    
    def add_customer(self):
        print("\n--- Add New Customer ---")
        try:
            name = input("Enter Customer Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            country = input("Enter Country: ")
            id_proof = input("Enter ID Proof Number: ")
            check_in_date = input("Enter Check-in Date (YYYY-MM-DD): ")
            check_out_date = input("Enter Check-out Date (YYYY-MM-DD): ")
            
            query = '''INSERT INTO customers 
                      (name, email, phone, address, city, country, id_proof, check_in_date, check_out_date) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            
            self.cursor.execute(query, (name, email, phone, address, city, country, id_proof, check_in_date, check_out_date))
            self.connection.commit()
            print("✓ Customer added successfully!")
        except Error as e:
            print(f"Error: {e}")
    
    def view_all_customers(self):
        print("\n--- All Customers ---")
        try:
            self.cursor.execute("SELECT * FROM customers")
            customers = self.cursor.fetchall()
            
            if customers:
                headers = ["ID", "Name", "Email", "Phone", "City", "Country", "Check-in", "Check-out", "Status"]
                print(" | ".join(headers))
                print("-" * 120)
                for cust in customers:
                    customer_id, name, email, phone, address, city, country, id_proof, check_in, check_out, status = cust
                    print(f"{customer_id} | {name} | {email or 'N/A'} | {phone or 'N/A'} | {city or 'N/A'} | {country or 'N/A'} | {check_in} | {check_out} | {status}")
            else:
                print("No customers found!")
        except Error as e:
            print(f"Error: {e}")
    
    def search_customer(self):
        print("\n--- Search Customer ---")
        try:
            customer_id = int(input("Enter Customer ID: "))
            self.cursor.execute("SELECT * FROM customers WHERE customer_id = %s", (customer_id,))
            customer = self.cursor.fetchone()
            
            if customer:
                headers = ["ID", "Name", "Email", "Phone", "Address", "City", "Country", "ID Proof", "Check-in", "Check-out", "Status"]
                print(" | ".join(headers))
                print("-" * 150)
                customer_id, name, email, phone, address, city, country, id_proof, check_in, check_out, status = customer
                print(f"{customer_id} | {name} | {email or 'N/A'} | {phone or 'N/A'} | {address or 'N/A'} | {city or 'N/A'} | {country or 'N/A'} | {id_proof} | {check_in} | {check_out} | {status}")
            else:
                print("Customer not found!")
        except Error as e:
            print(f"Error: {e}")
    
    def add_room(self):
        print("\n--- Add New Room ---")
        try:
            room_number = input("Enter Room Number: ")
            room_type = input("Enter Room Type (Single/Double/Suite/Deluxe): ")
            capacity = int(input("Enter Room Capacity: "))
            price_per_night = float(input("Enter Price Per Night: "))
            floor = int(input("Enter Floor Number: "))
            description = input("Enter Room Description: ")
            
            query = '''INSERT INTO rooms 
                      (room_number, room_type, capacity, price_per_night, floor, description) 
                      VALUES (%s, %s, %s, %s, %s, %s)'''
            
            self.cursor.execute(query, (room_number, room_type, capacity, price_per_night, floor, description))
            self.connection.commit()
            print("✓ Room added successfully!")
        except Error as e:
            print(f"Error: {e}")
    
    def view_all_rooms(self):
        print("\n--- All Rooms ---")
        try:
            self.cursor.execute("SELECT * FROM rooms")
            rooms = self.cursor.fetchall()
            
            if rooms:
                headers = ["ID", "Room No", "Type", "Capacity", "Price/Night", "Status", "Floor", "Description"]
                print(" | ".join(headers))
                print("-" * 130)
                for room in rooms:
                    room_id, room_number, room_type, capacity, price, status, floor, description = room
                    print(f"{room_id} | {room_number} | {room_type} | {capacity} | {price:.2f} | {status} | {floor} | {description or 'N/A'}")
            else:
                print("No rooms found!")
        except Error as e:
            print(f"Error: {e}")
    
    def view_available_rooms(self):
        print("\n--- Available Rooms ---")
        try:
            self.cursor.execute("SELECT * FROM rooms WHERE status = 'Available'")
            rooms = self.cursor.fetchall()
            
            if rooms:
                headers = ["ID", "Room No", "Type", "Capacity", "Price/Night", "Floor"]
                print(" | ".join(headers))
                print("-" * 80)
                for room in rooms:
                    room_id, room_number, room_type, capacity, price, status, floor, description = room
                    print(f"{room_id} | {room_number} | {room_type} | {capacity} | {price:.2f} | {floor}")
            else:
                print("No available rooms found!")
        except Error as e:
            print(f"Error: {e}")
    
    def book_room(self):
        print("\n--- Book a Room ---")
        try:
            customer_id = int(input("Enter Customer ID: "))
            room_id = int(input("Enter Room ID: "))
            check_in = input("Enter Check-in Date (YYYY-MM-DD): ")
            check_out = input("Enter Check-out Date (YYYY-MM-DD): ")
            
            # Calculate nights
            check_in_date = datetime.datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.datetime.strptime(check_out, "%Y-%m-%d")
            nights = (check_out_date - check_in_date).days
            
            # Get room price
            self.cursor.execute("SELECT price_per_night FROM rooms WHERE room_id = %s", (room_id,))
            result = self.cursor.fetchone()
            
            if result:
                price_per_night = result[0]
                total_cost = price_per_night * nights
                booking_date = datetime.date.today()
                
                query = '''INSERT INTO bookings 
                          (customer_id, room_id, check_in_date, check_out_date, number_of_nights, total_cost, booking_date) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s)'''
                
                self.cursor.execute(query, (customer_id, room_id, check_in, check_out, nights, total_cost, booking_date))
                
                # Update room status
                self.cursor.execute("UPDATE rooms SET status = 'Booked' WHERE room_id = %s", (room_id,))
                
                self.connection.commit()
                print(f"✓ Room booked successfully! Total Cost: {total_cost:.2f}")
            else:
                print("Room not found!")
        except Error as e:
            print(f"Error: {e}")
    
    def view_bookings(self):
        print("\n--- All Bookings ---")
        try:
            self.cursor.execute('''SELECT b.booking_id, c.name, r.room_number, b.check_in_date, b.check_out_date, 
                                  b.number_of_nights, b.total_cost, b.status 
                                  FROM bookings b 
                                  JOIN customers c ON b.customer_id = c.customer_id 
                                  JOIN rooms r ON b.room_id = r.room_id''')
            bookings = self.cursor.fetchall()
            
            if bookings:
                headers = ["Booking ID", "Customer", "Room", "Check-in", "Check-out", "Nights", "Total Cost", "Status"]
                print(" | ".join(headers))
                print("-" * 120)
                for booking in bookings:
                    booking_id, customer, room, check_in, check_out, nights, cost, status = booking
                    print(f"{booking_id} | {customer} | {room} | {check_in} | {check_out} | {nights} | {cost:.2f} | {status}")
            else:
                print("No bookings found!")
        except Error as e:
            print(f"Error: {e}")
    
    def checkout_room(self):
        print("\n--- Check-out Room ---")
        try:
            booking_id = int(input("Enter Booking ID: "))
            
            # Get booking details
            self.cursor.execute('''SELECT b.room_id, b.total_cost, c.customer_id 
                                  FROM bookings b 
                                  JOIN customers c ON b.customer_id = c.customer_id 
                                  WHERE b.booking_id = %s''', (booking_id,))
            result = self.cursor.fetchone()
            
            if result:
                room_id, room_charges, customer_id = result
                
                # Get service charges
                self.cursor.execute("SELECT SUM(cost) FROM services WHERE booking_id = %s", (booking_id,))
                service_result = self.cursor.fetchone()
                service_charges = service_result[0] if service_result[0] else 0
                
                # Calculate tax (10%)
                tax = (room_charges + service_charges) * 0.10
                total_amount = room_charges + service_charges + tax
                
                # Create bill
                bill_date = datetime.date.today()
                bill_query = '''INSERT INTO bills 
                               (booking_id, room_charges, service_charges, tax, total_amount, bill_date) 
                               VALUES (%s, %s, %s, %s, %s, %s)'''
                
                self.cursor.execute(bill_query, (booking_id, room_charges, service_charges, tax, total_amount, bill_date))
                
                # Update booking status
                self.cursor.execute("UPDATE bookings SET status = 'Checked-out' WHERE booking_id = %s", (booking_id,))
                
                # Update room status
                self.cursor.execute("UPDATE rooms SET status = 'Available' WHERE room_id = %s", (room_id,))
                
                # Update customer status
                self.cursor.execute("UPDATE customers SET status = 'Inactive' WHERE customer_id = %s", (customer_id,))
                
                self.connection.commit()
                
                print(f"\n✓ Check-out Successful!")
                print(f"Room Charges: {room_charges:.2f}")
                print(f"Service Charges: {service_charges:.2f}")
                print(f"Tax (10%): {tax:.2f}")
                print(f"Total Amount: {total_amount:.2f}")
            else:
                print("Booking not found!")
        except Error as e:
            print(f"Error: {e}")
    
    def add_service(self):
        print("\n--- Add Service ---")
        try:
            booking_id = int(input("Enter Booking ID: "))
            service_name = input("Enter Service Name (Room Service/Laundry/Spa/Maintenance): ")
            service_type = input("Enter Service Type: ")
            cost = float(input("Enter Service Cost: "))
            description = input("Enter Description: ")
            
            date_requested = datetime.date.today()
            
            query = '''INSERT INTO services 
                      (booking_id, service_name, service_type, cost, date_requested, description) 
                      VALUES (%s, %s, %s, %s, %s, %s)'''
            
            self.cursor.execute(query, (booking_id, service_name, service_type, cost, date_requested, description))
            self.connection.commit()
            print("✓ Service added successfully!")
        except Error as e:
            print(f"Error: {e}")
    
    def view_services(self):
        print("\n--- All Services ---")
        try:
            self.cursor.execute('''SELECT s.service_id, b.booking_id, c.name, s.service_name, 
                                  s.cost, s.date_requested, s.status 
                                  FROM services s 
                                  JOIN bookings b ON s.booking_id = b.booking_id 
                                  JOIN customers c ON b.customer_id = c.customer_id''')
            services = self.cursor.fetchall()
            
            if services:
                headers = ["Service ID", "Booking ID", "Customer", "Service", "Cost", "Date", "Status"]
                print(" | ".join(headers))
                print("-" * 100)
                for service in services:
                    service_id, booking_id, customer, service_name, cost, date, status = service
                    print(f"{service_id} | {booking_id} | {customer} | {service_name} | {cost:.2f} | {date} | {status}")
            else:
                print("No services found!")
        except Error as e:
            print(f"Error: {e}")
    
    def view_bill(self):
        print("\n--- View Bill ---")
        try:
            booking_id = int(input("Enter Booking ID: "))
            self.cursor.execute('''SELECT b.bill_id, bk.booking_id, c.name, b.room_charges, 
                                  b.service_charges, b.tax, b.total_amount, b.payment_status, b.bill_date 
                                  FROM bills b 
                                  JOIN bookings bk ON b.booking_id = bk.booking_id 
                                  JOIN customers c ON bk.customer_id = c.customer_id 
                                  WHERE b.booking_id = %s''', (booking_id,))
            bill = self.cursor.fetchone()
            
            if bill:
                bill_id, booking_id, customer, room_charges, service_charges, tax, total_amount, payment_status, bill_date = bill
                print("\n" + "="*50)
                print("           HOTEL BILL")
                print("="*50)
                print(f"Bill ID: {bill_id}")
                print(f"Booking ID: {booking_id}")
                print(f"Customer: {customer}")
                print(f"Bill Date: {bill_date}")
                print("-"*50)
                print(f"Room Charges: Rs. {room_charges:.2f}")
                print(f"Service Charges: Rs. {service_charges:.2f}")
                print(f"Tax (10%): Rs. {tax:.2f}")
                print("-"*50)
                print(f"Total Amount: Rs. {total_amount:.2f}")
                print(f"Payment Status: {payment_status}")
                print("="*50)
            else:
                print("Bill not found!")
        except Error as e:
            print(f"Error: {e}")
    
    def generate_report(self):
        print("\n--- Hotel Report ---")
        try:
            print("\n1. Room Occupancy Report")
            self.cursor.execute("SELECT room_type, COUNT(*) as count FROM rooms GROUP BY room_type")
            room_types = self.cursor.fetchall()
            print("Room Type | Count")
            print("-" * 30)
            for room_type, count in room_types:
                print(f"{room_type} | {count}")
            
            print("\n2. Total Bookings")
            self.cursor.execute("SELECT COUNT(*) FROM bookings")
            total_bookings = self.cursor.fetchone()[0]
            print(f"Total Bookings: {total_bookings}")
            
            print("\n3. Revenue")
            self.cursor.execute("SELECT SUM(total_amount) FROM bills WHERE payment_status = 'Paid'")
            revenue_result = self.cursor.fetchone()
            revenue = revenue_result[0] if revenue_result[0] else 0
            print(f"Total Revenue: Rs. {revenue:.2f}")
            
            print("\n4. Pending Payments")
            self.cursor.execute("SELECT SUM(total_amount) FROM bills WHERE payment_status = 'Pending'")
            pending_result = self.cursor.fetchone()
            pending = pending_result[0] if pending_result[0] else 0
            print(f"Pending Payments: Rs. {pending:.2f}")
        except Error as e:
            print(f"Error: {e}")
    
    def main_menu(self):
        while True:
            print("\n" + "="*60)
            print("        HOTEL MANAGEMENT SYSTEM")
            print("="*60)
            print("\n--- CUSTOMER MANAGEMENT ---")
            print("1. Add Customer")
            print("2. View All Customers")
            print("3. Search Customer")
            
            print("\n--- ROOM MANAGEMENT ---")
            print("4. Add Room")
            print("5. View All Rooms")
            print("6. View Available Rooms")
            
            print("\n--- BOOKING MANAGEMENT ---")
            print("7. Book a Room")
            print("8. View All Bookings")
            print("9. Check-out Room")
            
            print("\n--- SERVICE MANAGEMENT ---")
            print("10. Add Service")
            print("11. View All Services")
            
            print("\n--- BILLING ---")
            print("12. View Bill")
            
            print("\n--- REPORTS ---")
            print("13. Generate Hotel Report")
            
            print("\n14. Exit")
            print("="*60)
            
            choice = input("Enter your choice (1-14): ")
            
            if choice == "1":
                self.add_customer()
            elif choice == "2":
                self.view_all_customers()
            elif choice == "3":
                self.search_customer()
            elif choice == "4":
                self.add_room()
            elif choice == "5":
                self.view_all_rooms()
            elif choice == "6":
                self.view_available_rooms()
            elif choice == "7":
                self.book_room()
            elif choice == "8":
                self.view_bookings()
            elif choice == "9":
                self.checkout_room()
            elif choice == "10":
                self.add_service()
            elif choice == "11":
                self.view_services()
            elif choice == "12":
                self.view_bill()
            elif choice == "13":
                self.generate_report()
            elif choice == "14":
                print("\nThank you for using Hotel Management System!")
                self.cursor.close()
                self.connection.close()
                break
            else:
                print("Invalid choice! Try again.")

if __name__ == "__main__":
    hms = HotelManagementSystem()
    hms.main_menu()