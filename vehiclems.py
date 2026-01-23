from mysql.connector import Error
import datetime
import mysql.connector

# Globals for DB connection
conn = None
cursor = None

def connect_db(host='localhost', user='root', password='1234', database='mydb'):
    """Establish a global DB connection and prepare schema/sample data."""
    global conn, cursor
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        cursor = conn.cursor()
        print("✓ Database connected successfully!")
        create_tables()
        insert_sample_data()
    except Error as e:
        print(f"Error connecting to DB: {e}")

def create_tables():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100),
                phone VARCHAR(15),
                address VARCHAR(255),
                registration_date DATE,
                status VARCHAR(20) DEFAULT 'Active'
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vehicles (
                vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT,
                vehicle_number VARCHAR(20) UNIQUE NOT NULL,
                make VARCHAR(50),
                model VARCHAR(50),
                year INT,
                color VARCHAR(30),
                fuel_type VARCHAR(20),
                registration_date DATE,
                status VARCHAR(20) DEFAULT 'Active',
                FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS services (
                service_id INT AUTO_INCREMENT PRIMARY KEY,
                service_name VARCHAR(100) NOT NULL,
                description VARCHAR(255),
                base_price FLOAT,
                estimated_time INT,
                status VARCHAR(20) DEFAULT 'Active'
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS service_bookings (
                booking_id INT AUTO_INCREMENT PRIMARY KEY,
                vehicle_id INT,
                booking_date DATE,
                service_date DATE,
                service_time TIME,
                pickup_required VARCHAR(5) DEFAULT 'No',
                status VARCHAR(20) DEFAULT 'Pending',
                FOREIGN KEY(vehicle_id) REFERENCES vehicles(vehicle_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS booking_services (
                booking_service_id INT AUTO_INCREMENT PRIMARY KEY,
                booking_id INT,
                service_id INT,
                quantity INT DEFAULT 1,
                price FLOAT,
                FOREIGN KEY(booking_id) REFERENCES service_bookings(booking_id),
                FOREIGN KEY(service_id) REFERENCES services(service_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS invoices (
                invoice_id INT AUTO_INCREMENT PRIMARY KEY,
                booking_id INT,
                invoice_date DATE,
                service_charges FLOAT,
                parts_charges FLOAT,
                tax FLOAT,
                total_amount FLOAT,
                payment_status VARCHAR(20) DEFAULT 'Pending',
                payment_method VARCHAR(30),
                FOREIGN KEY(booking_id) REFERENCES service_bookings(booking_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mechanics (
                mechanic_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                specialization VARCHAR(100),
                phone VARCHAR(15),
                experience_years INT,
                status VARCHAR(20) DEFAULT 'Active'
            )
        ''')

        conn.commit()
        print("✓ Tables created successfully!")
    except Error as e:
        print(f"Table creation error: {e}")

def insert_sample_data():
    try:
        cursor.execute("SELECT COUNT(*) FROM services")
        if cursor.fetchone()[0] == 0:
                services_data = [
                    ("General Service", "Complete vehicle checkup and maintenance", 1500.00, 180, "Active"),
                    ("Oil Change", "Engine oil and filter replacement", 800.00, 45, "Active"),
                    ("Wheel Alignment", "Front and rear wheel alignment", 600.00, 60, "Active"),
                    ("Brake Service", "Brake pad replacement and adjustment", 1200.00, 90, "Active"),
                    ("AC Service", "AC gas refill and cooling system check", 1000.00, 120, "Active"),
                    ("Battery Replacement", "Vehicle battery replacement", 3500.00, 30, "Active"),
                    ("Tire Rotation", "All four tire rotation service", 400.00, 45, "Active")
                ]

                query = '''INSERT INTO services (service_name, description, base_price, estimated_time, status)
                          VALUES (%s, %s, %s, %s, %s)'''
                cursor.executemany(query, services_data)

                customers_data = [
                    ("John Smith", "john@email.com", "1234567890", "123 Main St", "2024-01-15", "Active"),
                    ("Mary Johnson", "mary@email.com", "9876543210", "456 Oak Ave", "2024-02-20", "Active"),
                    ("Robert Williams", "robert@email.com", "5551234567", "789 Pine Rd", "2024-03-10", "Active")
                ]

                query = '''INSERT INTO customers (name, email, phone, address, registration_date, status)
                          VALUES (%s, %s, %s, %s, %s, %s)'''
                cursor.executemany(query, customers_data)

                vehicles_data = [
                    (1, "MH01AB1234", "Honda", "City", 2020, "White", "Petrol", "2020-05-15", "Active"),
                    (2, "MH02CD5678", "Toyota", "Innova", 2019, "Silver", "Diesel", "2019-08-20", "Active"),
                    (3, "MH03EF9012", "Maruti", "Swift", 2021, "Red", "Petrol", "2021-12-10", "Active")
                ]

                query = '''INSERT INTO vehicles (customer_id, vehicle_number, make, model, year, color, fuel_type, registration_date, status)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                cursor.executemany(query, vehicles_data)

                mechanics_data = [
                    ("Ravi Kumar", "Engine Specialist", "9876543211", 10, "Active"),
                    ("Suresh Patel", "Electrical Systems", "9876543212", 8, "Active"),
                    ("Amit Sharma", "Body & Paint", "9876543213", 12, "Active"),
                    ("Vijay Singh", "General Mechanic", "9876543214", 6, "Active")
                ]

                query = '''INSERT INTO mechanics (name, specialization, phone, experience_years, status)
                          VALUES (%s, %s, %s, %s, %s)'''
                cursor.executemany(query, mechanics_data)

                conn.commit()
                print("✓ Sample data inserted successfully!")
    except Error:
        # silent fail for sample data insertion if DB not available
        return

def add_customer():
    print("\n--- Add New Customer ---")
    try:
        name = input("Enter Customer Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        address = input("Enter Address: ")
        registration_date = datetime.date.today()

        query = '''INSERT INTO customers (name, email, phone, address, registration_date)
                  VALUES (%s, %s, %s, %s, %s)'''

        cursor.execute(query, (name, email, phone, address, registration_date))
        conn.commit()
        print("✓ Customer added successfully!")
    except Error as e:
        print(f"Error: {e}")

def view_all_customers():
    print("\n--- All Customers ---")
    try:
        cursor.execute("SELECT * FROM customers WHERE status = 'Active'")
        customers = cursor.fetchall()
        if customers:
            print(f"{'ID':<5} {'Name':<25} {'Email':<25} {'Phone':<15} {'Status':<10}")
            print("-" * 90)
            for customer in customers:
                cust_id, name, email, phone, address, reg_date, status = customer
                print(f"{cust_id:<5} {name:<25} {email or 'N/A':<25} {phone or 'N/A':<15} {status:<10}")
        else:
            print("No customers found!")
    except Error as e:
        print(f"Error: {e}")

def add_vehicle():
    print("\n--- Add New Vehicle ---")
    try:
        customer_id = int(input("Enter Customer ID: "))
        vehicle_number = input("Enter Vehicle Number: ")
        make = input("Enter Make (Brand): ")
        model = input("Enter Model: ")
        year = int(input("Enter Year: "))
        color = input("Enter Color: ")
        fuel_type = input("Enter Fuel Type (Petrol/Diesel/Electric/CNG): ")
        registration_date = datetime.date.today()

        query = '''INSERT INTO vehicles (customer_id, vehicle_number, make, model, year, color, fuel_type, registration_date)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

        cursor.execute(query, (customer_id, vehicle_number, make, model, year, color, fuel_type, registration_date))
        conn.commit()
        print("✓ Vehicle added successfully!")
    except Error as e:
        print(f"Error: {e}")

def view_all_vehicles():
    print("\n--- All Vehicles ---")
    try:
        cursor.execute('''SELECT v.vehicle_id, c.name, v.vehicle_number, v.make, v.model, v.year, v.color, v.fuel_type
                              FROM vehicles v
                              JOIN customers c ON v.customer_id = c.customer_id
                              WHERE v.status = 'Active' ''')
        vehicles = cursor.fetchall()
        if vehicles:
            print(f"{'ID':<5} {'Owner':<25} {'Vehicle No':<15} {'Make':<15} {'Model':<15} {'Year':<6} {'Color':<12} {'Fuel':<10}")
            print("-" * 115)
            for vehicle in vehicles:
                veh_id, owner, veh_no, make, model, year, color, fuel = vehicle
                print(f"{veh_id:<5} {owner:<25} {veh_no:<15} {make:<15} {model:<15} {year:<6} {color:<12} {fuel:<10}")
        else:
            print("No vehicles found!")
    except Error as e:
        print(f"Error: {e}")

def view_all_services():
    print("\n--- Available Services ---")
    try:
        cursor.execute("SELECT * FROM services WHERE status = 'Active'")
        services = cursor.fetchall()
        if services:
            print(f"{'ID':<5} {'Service Name':<25} {'Description':<40} {'Price':<12} {'Time (min)':<12}")
            print("-" * 100)
            for service in services:
                serv_id, name, desc, price, time, status = service
                print(f"{serv_id:<5} {name:<25} {desc:<40} Rs.{price:<10.2f} {time:<12}")
        else:
            print("No services found!")
    except Error as e:
        print(f"Error: {e}")

def book_service():
    print("\n--- Book Service ---")
    try:
        vehicle_id = int(input("Enter Vehicle ID: "))
        service_date = input("Enter Service Date (YYYY-MM-DD): ")
        service_time = input("Enter Service Time (HH:MM:SS): ")
        pickup_required = input("Pickup Required? (Yes/No): ")
        booking_date = datetime.date.today()

        query = '''INSERT INTO service_bookings (vehicle_id, booking_date, service_date, service_time, pickup_required)
                  VALUES (%s, %s, %s, %s, %s)'''

        cursor.execute(query, (vehicle_id, booking_date, service_date, service_time, pickup_required))
        booking_id = cursor.lastrowid

        total_cost = 0

        while True:
            add_service = input("\nAdd service to booking? (yes/no): ")
            if add_service.lower() != 'yes':
                break

            service_id = int(input("Enter Service ID: "))

            cursor.execute("SELECT base_price FROM services WHERE service_id = %s", (service_id,))
            result = cursor.fetchone()

            if result:
                price = result[0]
                total_cost += price

                query = '''INSERT INTO booking_services (booking_id, service_id, quantity, price)
                          VALUES (%s, %s, %s, %s)'''

                cursor.execute(query, (booking_id, service_id, 1, price))
                print(f"Service added! Price: Rs. {price:.2f}")
            else:
                print("Service not found!")

        conn.commit()

        print(f"\n✓ Service booked successfully!")
        print(f"Booking ID: {booking_id}")
        print(f"Total Estimated Cost: Rs. {total_cost:.2f}")
    except Error as e:
        print(f"Error: {e}")

def view_bookings():
    print("\n--- All Service Bookings ---")
    try:
        cursor.execute('''SELECT sb.booking_id, c.name, v.vehicle_number, v.make, v.model, sb.service_date, sb.service_time, sb.pickup_required, sb.status
                              FROM service_bookings sb
                              JOIN vehicles v ON sb.vehicle_id = v.vehicle_id
                              JOIN customers c ON v.customer_id = c.customer_id
                              ORDER BY sb.service_date DESC''')
        bookings = cursor.fetchall()
        if bookings:
            print(f"{'Booking ID':<12} {'Customer':<25} {'Vehicle':<15} {'Make':<12} {'Model':<12} {'Date':<12} {'Time':<10} {'Pickup':<8} {'Status':<12}")
            print("-" * 130)
            for booking in bookings:
                book_id, customer, veh_no, make, model, date, time, pickup, status = booking
                print(f"{book_id:<12} {customer:<25} {veh_no:<15} {make:<12} {model:<12} {date} {str(time):<10} {pickup:<8} {status:<12}")
        else:
            print("No bookings found!")
    except Error as e:
        print(f"Error: {e}")

def complete_service():
    print("\n--- Complete Service ---")
    try:
        booking_id = int(input("Enter Booking ID: "))

        cursor.execute('''SELECT SUM(price) FROM booking_services WHERE booking_id = %s''', (booking_id,))
        result = cursor.fetchone()

        if result:
            service_charges = result[0] if result[0] else 0
            parts_charges = float(input("Enter Parts Charges: "))

            total_before_tax = service_charges + parts_charges
            tax = total_before_tax * 0.18
            total_amount = total_before_tax + tax

            invoice_date = datetime.date.today()
            payment_method = input("Enter Payment Method (Cash/Card/UPI): ")

            query = '''INSERT INTO invoices (booking_id, invoice_date, service_charges, parts_charges, tax, total_amount, payment_status, payment_method)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

            cursor.execute(query, (booking_id, invoice_date, service_charges, parts_charges, tax, total_amount, "Paid", payment_method))

            cursor.execute("UPDATE service_bookings SET status = 'Completed' WHERE booking_id = %s", (booking_id,))

            conn.commit()

            print(f"\n✓ Service completed successfully!")
            print(f"Service Charges: Rs. {service_charges:.2f}")
            print(f"Parts Charges: Rs. {parts_charges:.2f}")
            print(f"Tax (18%): Rs. {tax:.2f}")
            print(f"Total Amount: Rs. {total_amount:.2f}")
        else:
            print("Booking not found!")
    except Error as e:
        print(f"Error: {e}")

def view_invoices():
    print("\n--- All Invoices ---")
    try:
        cursor.execute('''SELECT i.invoice_id, c.name, v.vehicle_number, i.invoice_date, i.service_charges, i.parts_charges, i.tax, i.total_amount, i.payment_status
                              FROM invoices i
                              JOIN service_bookings sb ON i.booking_id = sb.booking_id
                              JOIN vehicles v ON sb.vehicle_id = v.vehicle_id
                              JOIN customers c ON v.customer_id = c.customer_id
                              ORDER BY i.invoice_date DESC''')
        invoices = cursor.fetchall()
        if invoices:
            print(f"{'Invoice ID':<12} {'Customer':<25} {'Vehicle':<15} {'Date':<12} {'Service':<12} {'Parts':<12} {'Tax':<10} {'Total':<12} {'Status':<12}")
            print("-" * 130)
            for invoice in invoices:
                inv_id, customer, veh_no, date, service, parts, tax, total, status = invoice
                print(f"{inv_id:<12} {customer:<25} {veh_no:<15} {date} Rs.{service:<10.2f} Rs.{parts:<10.2f} Rs.{tax:<8.2f} Rs.{total:<10.2f} {status:<12}")
        else:
            print("No invoices found!")
    except Error as e:
        print(f"Error: {e}")

def view_mechanics():
    print("\n--- All Mechanics ---")
    try:
        cursor.execute("SELECT * FROM mechanics WHERE status = 'Active'")
        mechanics = cursor.fetchall()

        if mechanics:
            print(f"{'ID':<5} {'Name':<25} {'Specialization':<30} {'Phone':<15} {'Experience':<12} {'Status':<10}")
            print("-" * 110)
            for mechanic in mechanics:
                mech_id, name, spec, phone, exp, status = mechanic
                print(f"{mech_id:<5} {name:<25} {spec:<30} {phone or 'N/A':<15} {exp} years {status:<10}")
        else:
            print("No mechanics found!")
    except Error as e:
        print(f"Error: {e}")

def generate_report():
    print("\n--- Vehicle Service Report ---")
    try:
        print("\n1. Total Customers")
        cursor.execute("SELECT COUNT(*) FROM customers WHERE status = 'Active'")
        customers = cursor.fetchone()[0]
        print(f"Active Customers: {customers}")

        print("\n2. Total Vehicles")
        cursor.execute("SELECT COUNT(*) FROM vehicles WHERE status = 'Active'")
        vehicles = cursor.fetchone()[0]
        print(f"Registered Vehicles: {vehicles}")

        print("\n3. Total Bookings")
        cursor.execute("SELECT COUNT(*) FROM service_bookings")
        bookings = cursor.fetchone()[0]
        print(f"Total Bookings: {bookings}")

        print("\n4. Pending Services")
        cursor.execute("SELECT COUNT(*) FROM service_bookings WHERE status = 'Pending'")
        pending = cursor.fetchone()[0]
        print(f"Pending Services: {pending}")

        print("\n5. Total Revenue")
        cursor.execute("SELECT SUM(total_amount) FROM invoices WHERE payment_status = 'Paid'")
        revenue_result = cursor.fetchone()
        revenue = revenue_result[0] if revenue_result and revenue_result[0] else 0
        print(f"Total Revenue: Rs. {revenue:.2f}")

        print("\n6. Most Popular Service")
        cursor.execute('''SELECT s.service_name, COUNT(*) as count
                              FROM booking_services bs
                              JOIN services s ON bs.service_id = s.service_id
                              GROUP BY s.service_name
                              ORDER BY count DESC
                              LIMIT 1''')
        popular = cursor.fetchone()
        if popular:
            print(f"Most Popular Service: {popular[0]} ({popular[1]} bookings)")
    except Error as e:
        print(f"Error: {e}")

def main_menu():
    while True:
        print("\n" + "="*60)
        print("        VEHICLE SERVICE MANAGEMENT SYSTEM")
        print("="*60)
        print("\n--- CUSTOMER MANAGEMENT ---")
        print("1. Add Customer")
        print("2. View All Customers")

        print("\n--- VEHICLE MANAGEMENT ---")
        print("3. Add Vehicle")
        print("4. View All Vehicles")

        print("\n--- SERVICE MANAGEMENT ---")
        print("5. View All Services")
        print("6. Book Service")
        print("7. View All Bookings")
        print("8. Complete Service")

        print("\n--- INVOICE MANAGEMENT ---")
        print("9. View All Invoices")

        print("\n--- MECHANIC MANAGEMENT ---")
        print("10. View All Mechanics")

        print("\n--- REPORTS ---")
        print("11. Generate Report")

        print("\n12. Exit")
        print("="*60)

        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_all_customers()
        elif choice == "3":
            add_vehicle()
        elif choice == "4":
            view_all_vehicles()
        elif choice == "5":
            view_all_services()
        elif choice == "6":
            book_service()
        elif choice == "7":
            view_bookings()
        elif choice == "8":
            complete_service()
        elif choice == "9":
            view_invoices()
        elif choice == "10":
            view_mechanics()
        elif choice == "11":
            generate_report()
        elif choice == "12":
            print("\nThank you for using Vehicle Service Management System!")
            try:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            except Exception:
                pass
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    connect_db()
    main_menu()
