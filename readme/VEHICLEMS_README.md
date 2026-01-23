# Vehicle Service Management System (functions-only)

This workspace contains a functions-only, menu-driven Vehicle Service Management System implemented in `vehiclems.py`.

Overview
- `vehiclems.py` uses global `conn` and `cursor` for a MySQL connection and exposes a simple CLI menu to manage customers, vehicles, services, bookings, invoices and reports.

Modules / Functions
- `connect_db(host, user, password, database)` — opens DB connection, creates schema and inserts sample data.
- `create_tables()` — creates required tables if missing.
- `insert_sample_data()` — inserts sample services, customers, vehicles and mechanics (runs only if tables are empty).
- `add_customer()` — prompts and inserts a customer.
- `view_all_customers()` — lists active customers.
- `add_vehicle()` — prompts and inserts a vehicle for an existing customer.
- `view_all_vehicles()` — lists vehicles with owner.
- `view_all_services()` — displays available services.
- `book_service()` — interactive booking flow; attach services to a booking.
- `view_bookings()` — lists all bookings.
- `complete_service()` — calculates invoice, inserts into `invoices`, and marks booking completed.
- `view_invoices()` — lists invoices and payment status.
- `view_mechanics()` — lists mechanics.
- `generate_report()` — summary metrics (customers, vehicles, revenue, popular service).
- `main_menu()` — interactive menu entrypoint.

Requirements
- Python 3.8+
- `mysql-connector-python` (install with `pip install mysql-connector-python`)

How to run
1. Ensure MySQL is running and update credentials in `vehiclems.py` if needed.
2. Run:

```powershell
python vehiclems.py
```

Minimal sample outputs

- On successful DB connect:

```
✓ Database connected successfully!
✓ Tables created successfully!
✓ Sample data inserted successfully!
```

- Menu header:

```
============================================================
        VEHICLE SERVICE MANAGEMENT SYSTEM
============================================================
--- CUSTOMER MANAGEMENT ---
1. Add Customer
2. View All Customers
...
12. Exit
```

- Example: add customer

```
--- Add New Customer ---
Enter Customer Name: John Doe
Enter Email: john@example.com
Enter Phone: 9999999999
Enter Address: 1 Main St
✓ Customer added successfully!
```

- Example: view services

```
--- Available Services ---
ID    Service Name             Description                              Price        Time (min)
--------------------------------------------------------------------------------------------
1     General Service          Complete vehicle checkup and maintenance Rs.1500.00   180
2     Oil Change               Engine oil and filter replacement         Rs.800.00    45
```

Notes
- The script expects a reachable MySQL server. If the DB is unreachable, some operations will fail; sample data insertion is intentionally tolerant and will not crash the script.
- This file intentionally uses simple input() prompts and minimal validation for clarity; consider adding stricter input checks for production use.

Next steps I can do for you
- Add `requirements.txt` with `mysql-connector-python`.
- Produce a sample CLI session logged to `vehiclems_sample_output.txt`.
- Add basic input validation and helpful error messages.

Tell me which next step you'd like me to take.
