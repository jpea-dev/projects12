import pickle
import os
from datetime import datetime
from typing import Dict, List

# ==================== GLOBAL COUNTERS ====================
patient_counter = 1000
doctor_counter = 100
appointment_counter = 500
room_counter = 200
billing_counter = 4000

# ==================== DATA STORAGE ====================
patients: List[Dict] = []
doctors: List[Dict] = []
appointments: List[Dict] = []
rooms: List[Dict] = []
billing: List[Dict] = []

# ==================== FILE MANAGEMENT ====================

def init_database():
    """Initialize database directory and load data"""
    data_dir = "hospital_data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    load_all_data()

def save_patients():
    """Save patients to binary file"""
    try:
        data_dir = "hospital_data"
        with open(os.path.join(data_dir, "patients.pkl"), 'wb') as f:
            pickle.dump(patients, f)
    except Exception as e:
        print(f"Error saving patients: {e}")

def save_doctors():
    """Save doctors to binary file"""
    try:
        data_dir = "hospital_data"
        with open(os.path.join(data_dir, "doctors.pkl"), 'wb') as f:
            pickle.dump(doctors, f)
    except Exception as e:
        print(f"Error saving doctors: {e}")

def save_appointments():
    """Save appointments to binary file"""
    try:
        data_dir = "hospital_data"
        with open(os.path.join(data_dir, "appointments.pkl"), 'wb') as f:
            pickle.dump(appointments, f)
    except Exception as e:
        print(f"Error saving appointments: {e}")

def save_rooms():
    """Save rooms to binary file"""
    try:
        data_dir = "hospital_data"
        with open(os.path.join(data_dir, "rooms.pkl"), 'wb') as f:
            pickle.dump(rooms, f)
    except Exception as e:
        print(f"Error saving rooms: {e}")

def save_billing():
    """Save billing to binary file"""
    try:
        data_dir = "hospital_data"
        with open(os.path.join(data_dir, "billing.pkl"), 'wb') as f:
            pickle.dump(billing, f)
    except Exception as e:
        print(f"Error saving billing: {e}")

def load_patients():
    """Load patients from binary file"""
    global patients
    try:
        data_dir = "hospital_data"
        filepath = os.path.join(data_dir, "patients.pkl")
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                patients = pickle.load(f)
    except Exception as e:
        print(f"Error loading patients: {e}")
        patients = []

def load_doctors():
    """Load doctors from binary file"""
    global doctors
    try:
        data_dir = "hospital_data"
        filepath = os.path.join(data_dir, "doctors.pkl")
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                doctors = pickle.load(f)
    except Exception as e:
        print(f"Error loading doctors: {e}")
        doctors = []

def load_appointments():
    """Load appointments from binary file"""
    global appointments
    try:
        data_dir = "hospital_data"
        filepath = os.path.join(data_dir, "appointments.pkl")
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                appointments = pickle.load(f)
    except Exception as e:
        print(f"Error loading appointments: {e}")
        appointments = []

def load_rooms():
    """Load rooms from binary file"""
    global rooms
    try:
        data_dir = "hospital_data"
        filepath = os.path.join(data_dir, "rooms.pkl")
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                rooms = pickle.load(f)
    except Exception as e:
        print(f"Error loading rooms: {e}")
        rooms = []

def load_billing():
    """Load billing from binary file"""
    global billing
    try:
        data_dir = "hospital_data"
        filepath = os.path.join(data_dir, "billing.pkl")
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                billing = pickle.load(f)
    except Exception as e:
        print(f"Error loading billing: {e}")
        billing = []

def load_all_data():
    """Load all data from binary files"""
    load_patients()
    load_doctors()
    load_appointments()
    load_rooms()
    load_billing()

def save_all_data():
    """Save all data to binary files"""
    save_patients()
    save_doctors()
    save_appointments()
    save_rooms()
    save_billing()

def add_sample_data():
    """Add sample data to the database"""
    global patient_counter, doctor_counter, room_counter, appointment_counter, billing_counter
    
    print("Adding sample data...")
    
    # Add sample patients
    if not patients:
        sample_patients = [
            {"patient_id": 1000, "name": "Rajesh Kumar", "age": 45, "gender": "Male", "address": "123 Main St", "phone": "9876543210", "disease": "Diabetes", "admission_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "status": "Active"},
            {"patient_id": 1001, "name": "Priya Singh", "age": 38, "gender": "Female", "address": "456 Oak Ave", "phone": "9876543211", "disease": "Asthma", "admission_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "status": "Active"},
            {"patient_id": 1002, "name": "Amit Patel", "age": 52, "gender": "Male", "address": "789 Pine Rd", "phone": "9876543212", "disease": "Heart Disease", "admission_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "status": "Active"},
            {"patient_id": 1003, "name": "Neha Sharma", "age": 28, "gender": "Female", "address": "321 Elm St", "phone": "9876543213", "disease": "Migraine", "admission_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "status": "Active"},
            {"patient_id": 1004, "name": "Vikram Das", "age": 65, "gender": "Male", "address": "654 Maple Dr", "phone": "9876543214", "disease": "Arthritis", "admission_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "status": "Active"},
        ]
        patients.extend(sample_patients)
        patient_counter = 1005
    
    # Add sample doctors
    if not doctors:
        sample_doctors = [
            {"doctor_id": 100, "name": "Dr. Suresh Gupta", "specialty": "Cardiology", "qualification": "MBBS, MD", "phone": "9876543220", "experience": 15, "status": "Active"},
            {"doctor_id": 101, "name": "Dr. Anjali Verma", "specialty": "Neurology", "qualification": "MBBS, DM", "phone": "9876543221", "experience": 12, "status": "Active"},
            {"doctor_id": 102, "name": "Dr. Rahul Sharma", "specialty": "General Medicine", "qualification": "MBBS", "phone": "9876543222", "experience": 10, "status": "Active"},
            {"doctor_id": 103, "name": "Dr. Meera Nair", "specialty": "Pediatrics", "qualification": "MBBS, DCH", "phone": "9876543223", "experience": 8, "status": "Active"},
            {"doctor_id": 104, "name": "Dr. Vikram Singh", "specialty": "Orthopedics", "qualification": "MBBS, MS", "phone": "9876543224", "experience": 20, "status": "Active"},
        ]
        doctors.extend(sample_doctors)
        doctor_counter = 105
    
    # Add sample rooms
    if not rooms:
        sample_rooms = [
            {"room_id": 200, "room_type": "ICU", "capacity": 1, "charges_per_day": 5000, "is_available": True, "current_patient_id": None},
            {"room_id": 201, "room_type": "ICU", "capacity": 1, "charges_per_day": 5000, "is_available": True, "current_patient_id": None},
            {"room_id": 202, "room_type": "General Ward", "capacity": 4, "charges_per_day": 1000, "is_available": True, "current_patient_id": None},
            {"room_id": 203, "room_type": "General Ward", "capacity": 4, "charges_per_day": 1000, "is_available": True, "current_patient_id": None},
            {"room_id": 204, "room_type": "General Ward", "capacity": 4, "charges_per_day": 1000, "is_available": True, "current_patient_id": None},
            {"room_id": 205, "room_type": "Semi-Private", "capacity": 2, "charges_per_day": 2000, "is_available": True, "current_patient_id": None},
            {"room_id": 206, "room_type": "Semi-Private", "capacity": 2, "charges_per_day": 2000, "is_available": True, "current_patient_id": None},
            {"room_id": 207, "room_type": "Private", "capacity": 1, "charges_per_day": 3000, "is_available": True, "current_patient_id": None},
            {"room_id": 208, "room_type": "Private", "capacity": 1, "charges_per_day": 3000, "is_available": True, "current_patient_id": None},
        ]
        rooms.extend(sample_rooms)
        room_counter = 209
    
    # Add sample appointments
    if not appointments:
        sample_appointments = [
            {"appointment_id": 500, "patient_id": 1000, "doctor_id": 100, "appointment_date": "2026-01-25 10:00:00", "reason": "Routine Checkup", "status": "Scheduled", "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"appointment_id": 501, "patient_id": 1001, "doctor_id": 101, "appointment_date": "2026-01-26 14:30:00", "reason": "Heart Consultation", "status": "Scheduled", "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"appointment_id": 502, "patient_id": 1002, "doctor_id": 102, "appointment_date": "2026-01-27 09:00:00", "reason": "General Examination", "status": "Scheduled", "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
        ]
        appointments.extend(sample_appointments)
        appointment_counter = 503
    
    # Add sample billing
    if not billing:
        sample_billing = [
            {"bill_id": 4000, "patient_id": 1000, "room_charges": 5000, "medicine_charges": 2000, "doctor_consultation": 1000, "other_charges": 0, "total_amount": 8000, "bill_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "payment_status": "Pending"},
            {"bill_id": 4001, "patient_id": 1001, "room_charges": 3000, "medicine_charges": 1500, "doctor_consultation": 1500, "other_charges": 0, "total_amount": 6000, "bill_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "payment_status": "Pending"},
            {"bill_id": 4002, "patient_id": 1002, "room_charges": 1000, "medicine_charges": 800, "doctor_consultation": 500, "other_charges": 0, "total_amount": 2300, "bill_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "payment_status": "Pending"},
        ]
        billing.extend(sample_billing)
        billing_counter = 4003
    
    save_all_data()
    print("Sample data added successfully!\n")


# ==================== PATIENT FUNCTIONS ====================

def add_patient():
    """Create a new patient"""
    global patient_counter
    try:
        print("\n" + "="*50)
        print("ADD NEW PATIENT")
        print("="*50)
        name = input("Enter patient name: ").strip()
        age = int(input("Enter age: "))
        gender = input("Enter gender (Male/Female/Other): ").strip()
        address = input("Enter address: ").strip()
        phone = input("Enter phone number: ").strip()
        disease = input("Enter disease/reason: ").strip()
        
        patient = {
            "patient_id": patient_counter,
            "name": name,
            "age": age,
            "gender": gender,
            "address": address,
            "phone": phone,
            "disease": disease,
            "admission_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Active"
        }
        patients.append(patient)
        patient_counter += 1
        save_patients()
        print(f"\n✓ Patient added successfully! Patient ID: {patient['patient_id']}\n")
        return True
    except ValueError:
        print("Invalid input! Please enter valid data.\n")
        return False
    except Exception as e:
        print(f"Error: {e}\n")
        return False

def view_all_patients():
    """Display all patients"""
    if not patients:
        print("\nNo patients found!\n")
        return
    
    print("\n" + "="*50)
    print("ALL PATIENTS")
    print("="*50)
    for patient in patients:
        print(f"""
    Patient ID: {patient['patient_id']}
    Name: {patient['name']}
    Age: {patient['age']}
    Gender: {patient['gender']}
    Address: {patient['address']}
    Phone: {patient['phone']}
    Disease: {patient['disease']}
    Admission Date: {patient['admission_date']}
    Status: {patient['status']}
        """)

def view_patient_by_id():
    """Display a specific patient by ID"""
    try:
        patient_id = int(input("Enter patient ID: "))
        patient = next((p for p in patients if p['patient_id'] == patient_id), None)
        
        if patient:
            print("\n" + "="*50)
            print("PATIENT DETAILS")
            print("="*50)
            print(f"""
    Patient ID: {patient['patient_id']}
    Name: {patient['name']}
    Age: {patient['age']}
    Gender: {patient['gender']}
    Address: {patient['address']}
    Phone: {patient['phone']}
    Disease: {patient['disease']}
    Admission Date: {patient['admission_date']}
    Status: {patient['status']}
            """)
        else:
            print(f"\nPatient with ID {patient_id} not found!\n")
    except ValueError:
        print("Invalid patient ID!\n")

def update_patient():
    """Update patient information"""
    try:
        patient_id = int(input("Enter patient ID to update: "))
        patient = next((p for p in patients if p['patient_id'] == patient_id), None)
        
        if not patient:
            print(f"\nPatient with ID {patient_id} not found!\n")
            return
        
        print("\n" + "="*50)
        print("UPDATE PATIENT")
        print("="*50)
        print("1. Name")
        print("2. Age")
        print("3. Address")
        print("4. Phone")
        print("5. Disease")
        print("6. Status")
        
        choice = input("What to update (1-6): ").strip()
        
        if choice == "1":
            patient['name'] = input("Enter new name: ").strip()
        elif choice == "2":
            patient['age'] = int(input("Enter new age: "))
        elif choice == "3":
            patient['address'] = input("Enter new address: ").strip()
        elif choice == "4":
            patient['phone'] = input("Enter new phone: ").strip()
        elif choice == "5":
            patient['disease'] = input("Enter new disease: ").strip()
        elif choice == "6":
            patient['status'] = input("Enter new status (Active/Discharged/Deceased): ").strip()
        else:
            print("Invalid choice!\n")
            return
        
        save_patients()
        print(f"\n✓ Patient updated successfully!\n")
    except ValueError:
        print("Invalid input!\n")

def delete_patient():
    """Delete a patient"""
    try:
        patient_id = int(input("Enter patient ID to delete: "))
        patient = next((p for p in patients if p['patient_id'] == patient_id), None)
        
        if not patient:
            print(f"\nPatient with ID {patient_id} not found!\n")
            return
        
        confirm = input(f"Are you sure you want to delete patient {patient['name']}? (yes/no): ").lower()
        if confirm == "yes":
            patients.remove(patient)
            save_patients()
            print(f"\n✓ Patient deleted successfully!\n")
        else:
            print("Deletion cancelled.\n")
    except ValueError:
        print("Invalid patient ID!\n")


# ==================== DOCTOR FUNCTIONS ====================

def add_doctor():
    """Create a new doctor"""
    global doctor_counter
    try:
        print("\n" + "="*50)
        print("ADD NEW DOCTOR")
        print("="*50)
        name = input("Enter doctor name: ").strip()
        specialty = input("Enter specialty: ").strip()
        qualification = input("Enter qualification: ").strip()
        phone = input("Enter phone number: ").strip()
        experience = int(input("Enter years of experience: "))
        
        doctor = {
            "doctor_id": doctor_counter,
            "name": name,
            "specialty": specialty,
            "qualification": qualification,
            "phone": phone,
            "experience": experience,
            "status": "Active"
        }
        doctors.append(doctor)
        doctor_counter += 1
        save_doctors()
        print(f"\n✓ Doctor added successfully! Doctor ID: {doctor['doctor_id']}\n")
        return True
    except ValueError:
        print("Invalid input! Please enter valid data.\n")
        return False

def view_all_doctors():
    """Display all doctors"""
    if not doctors:
        print("\nNo doctors found!\n")
        return
    
    print("\n" + "="*50)
    print("ALL DOCTORS")
    print("="*50)
    for doctor in doctors:
        print(f"""
    Doctor ID: {doctor['doctor_id']}
    Name: {doctor['name']}
    Specialty: {doctor['specialty']}
    Qualification: {doctor['qualification']}
    Phone: {doctor['phone']}
    Experience: {doctor['experience']} years
    Status: {doctor['status']}
        """)

def view_doctor_by_id():
    """Display a specific doctor by ID"""
    try:
        doctor_id = int(input("Enter doctor ID: "))
        doctor = next((d for d in doctors if d['doctor_id'] == doctor_id), None)
        
        if doctor:
            print("\n" + "="*50)
            print("DOCTOR DETAILS")
            print("="*50)
            print(f"""
    Doctor ID: {doctor['doctor_id']}
    Name: {doctor['name']}
    Specialty: {doctor['specialty']}
    Qualification: {doctor['qualification']}
    Phone: {doctor['phone']}
    Experience: {doctor['experience']} years
    Status: {doctor['status']}
            """)
        else:
            print(f"\nDoctor with ID {doctor_id} not found!\n")
    except ValueError:
        print("Invalid doctor ID!\n")

def update_doctor():
    """Update doctor information"""
    try:
        doctor_id = int(input("Enter doctor ID to update: "))
        doctor = next((d for d in doctors if d['doctor_id'] == doctor_id), None)
        
        if not doctor:
            print(f"\nDoctor with ID {doctor_id} not found!\n")
            return
        
        print("\n" + "="*50)
        print("UPDATE DOCTOR")
        print("="*50)
        print("1. Name")
        print("2. Specialty")
        print("3. Qualification")
        print("4. Phone")
        print("5. Experience")
        print("6. Status")
        
        choice = input("What to update (1-6): ").strip()
        
        if choice == "1":
            doctor['name'] = input("Enter new name: ").strip()
        elif choice == "2":
            doctor['specialty'] = input("Enter new specialty: ").strip()
        elif choice == "3":
            doctor['qualification'] = input("Enter new qualification: ").strip()
        elif choice == "4":
            doctor['phone'] = input("Enter new phone: ").strip()
        elif choice == "5":
            doctor['experience'] = int(input("Enter new experience (years): "))
        elif choice == "6":
            doctor['status'] = input("Enter new status (Active/On Leave/Inactive): ").strip()
        else:
            print("Invalid choice!\n")
            return
        
        save_doctors()
        print(f"\n✓ Doctor updated successfully!\n")
    except ValueError:
        print("Invalid input!\n")

def delete_doctor():
    """Delete a doctor"""
    try:
        doctor_id = int(input("Enter doctor ID to delete: "))
        doctor = next((d for d in doctors if d['doctor_id'] == doctor_id), None)
        
        if not doctor:
            print(f"\nDoctor with ID {doctor_id} not found!\n")
            return
        
        confirm = input(f"Are you sure you want to delete doctor {doctor['name']}? (yes/no): ").lower()
        if confirm == "yes":
            doctors.remove(doctor)
            save_doctors()
            print(f"\n✓ Doctor deleted successfully!\n")
        else:
            print("Deletion cancelled.\n")
    except ValueError:
        print("Invalid doctor ID!\n")


# ==================== APPOINTMENT FUNCTIONS ====================

def add_appointment():
    """Create a new appointment"""
    global appointment_counter
    try:
        print("\n" + "="*50)
        print("SCHEDULE NEW APPOINTMENT")
        print("="*50)
        
        patient_id = int(input("Enter patient ID: "))
        if not any(p['patient_id'] == patient_id for p in patients):
            print("Patient not found!\n")
            return False
        
        doctor_id = int(input("Enter doctor ID: "))
        if not any(d['doctor_id'] == doctor_id for d in doctors):
            print("Doctor not found!\n")
            return False
        
        appointment_date = input("Enter appointment date and time (YYYY-MM-DD HH:MM:SS): ").strip()
        reason = input("Enter reason for appointment: ").strip()
        
        appointment = {
            "appointment_id": appointment_counter,
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "appointment_date": appointment_date,
            "reason": reason,
            "status": "Scheduled",
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        appointments.append(appointment)
        appointment_counter += 1
        save_appointments()
        print(f"\n✓ Appointment scheduled successfully! Appointment ID: {appointment['appointment_id']}\n")
        return True
    except ValueError:
        print("Invalid input! Please enter valid data.\n")
        return False

def view_all_appointments():
    """Display all appointments"""
    if not appointments:
        print("\nNo appointments found!\n")
        return
    
    print("\n" + "="*50)
    print("ALL APPOINTMENTS")
    print("="*50)
    for appt in appointments:
        print(f"""
    Appointment ID: {appt['appointment_id']}
    Patient ID: {appt['patient_id']}
    Doctor ID: {appt['doctor_id']}
    Appointment Date: {appt['appointment_date']}
    Reason: {appt['reason']}
    Status: {appt['status']}
    Created Date: {appt['created_date']}
        """)

def view_appointments_by_patient():
    """Display appointments for a specific patient"""
    try:
        patient_id = int(input("Enter patient ID: "))
        appts = [a for a in appointments if a['patient_id'] == patient_id]
        
        if not appts:
            print(f"\nNo appointments found for patient ID {patient_id}!\n")
            return
        
        print("\n" + "="*50)
        print(f"APPOINTMENTS FOR PATIENT {patient_id}")
        print("="*50)
        for appt in appts:
            print(f"""
    Appointment ID: {appt['appointment_id']}
    Patient ID: {appt['patient_id']}
    Doctor ID: {appt['doctor_id']}
    Appointment Date: {appt['appointment_date']}
    Reason: {appt['reason']}
    Status: {appt['status']}
    Created Date: {appt['created_date']}
            """)
    except ValueError:
        print("Invalid patient ID!\n")

def update_appointment():
    """Update appointment information"""
    try:
        appointment_id = int(input("Enter appointment ID to update: "))
        appointment = next((a for a in appointments if a['appointment_id'] == appointment_id), None)
        
        if not appointment:
            print(f"\nAppointment with ID {appointment_id} not found!\n")
            return
        
        print("\n" + "="*50)
        print("UPDATE APPOINTMENT")
        print("="*50)
        print("1. Date and Time")
        print("2. Reason")
        print("3. Status")
        
        choice = input("What to update (1-3): ").strip()
        
        if choice == "1":
            appointment['appointment_date'] = input("Enter new date and time (YYYY-MM-DD HH:MM:SS): ").strip()
        elif choice == "2":
            appointment['reason'] = input("Enter new reason: ").strip()
        elif choice == "3":
            appointment['status'] = input("Enter new status (Scheduled/Completed/Cancelled): ").strip()
        else:
            print("Invalid choice!\n")
            return
        
        save_appointments()
        print(f"\n✓ Appointment updated successfully!\n")
    except ValueError:
        print("Invalid input!\n")

def delete_appointment():
    """Delete an appointment"""
    try:
        appointment_id = int(input("Enter appointment ID to delete: "))
        appointment = next((a for a in appointments if a['appointment_id'] == appointment_id), None)
        
        if not appointment:
            print(f"\nAppointment with ID {appointment_id} not found!\n")
            return
        
        confirm = input(f"Are you sure you want to delete appointment {appointment['appointment_id']}? (yes/no): ").lower()
        if confirm == "yes":
            appointments.remove(appointment)
            save_appointments()
            print(f"\n✓ Appointment deleted successfully!\n")
        else:
            print("Deletion cancelled.\n")
    except ValueError:
        print("Invalid appointment ID!\n")


# ==================== ROOM FUNCTIONS ====================

def add_room():
    """Create a new room"""
    global room_counter
    try:
        print("\n" + "="*50)
        print("ADD NEW ROOM")
        print("="*50)
        room_type = input("Enter room type (ICU/General Ward/Semi-Private/Private): ").strip()
        capacity = int(input("Enter capacity (number of beds): "))
        charges = float(input("Enter charges per day (Rs.): "))
        
        room = {
            "room_id": room_counter,
            "room_type": room_type,
            "capacity": capacity,
            "charges_per_day": charges,
            "is_available": True,
            "current_patient_id": None
        }
        rooms.append(room)
        room_counter += 1
        save_rooms()
        print(f"\n✓ Room added successfully! Room ID: {room['room_id']}\n")
        return True
    except ValueError:
        print("Invalid input! Please enter valid data.\n")
        return False

def view_all_rooms():
    """Display all rooms"""
    if not rooms:
        print("\nNo rooms found!\n")
        return
    
    print("\n" + "="*50)
    print("ALL ROOMS")
    print("="*50)
    for room in rooms:
        availability = "Available" if room['is_available'] else "Occupied"
        print(f"""
    Room ID: {room['room_id']}
    Type: {room['room_type']}
    Capacity: {room['capacity']} beds
    Charges per Day: Rs. {room['charges_per_day']}
    Status: {availability}
    Current Patient ID: {room['current_patient_id'] if room['current_patient_id'] else "None"}
        """)

def view_available_rooms():
    """Display available rooms"""
    available = [r for r in rooms if r['is_available']]
    
    if not available:
        print("\nNo available rooms!\n")
        return
    
    print("\n" + "="*50)
    print("AVAILABLE ROOMS")
    print("="*50)
    for room in available:
        print(f"""
    Room ID: {room['room_id']}
    Type: {room['room_type']}
    Capacity: {room['capacity']} beds
    Charges per Day: Rs. {room['charges_per_day']}
    Status: Available
        """)

def update_room_availability():
    """Update room availability"""
    try:
        room_id = int(input("Enter room ID: "))
        room = next((r for r in rooms if r['room_id'] == room_id), None)
        
        if not room:
            print(f"\nRoom with ID {room_id} not found!\n")
            return
        
        patient_id = int(input("Enter patient ID occupying this room (0 if empty): "))
        
        if patient_id > 0:
            room['is_available'] = False
            room['current_patient_id'] = patient_id
            print(f"\n✓ Patient {patient_id} assigned to room {room_id}\n")
        else:
            room['is_available'] = True
            room['current_patient_id'] = None
            print(f"\n✓ Room {room_id} marked as available\n")
        
        save_rooms()
    except ValueError:
        print("Invalid input!\n")

def delete_room():
    """Delete a room"""
    try:
        room_id = int(input("Enter room ID to delete: "))
        room = next((r for r in rooms if r['room_id'] == room_id), None)
        
        if not room:
            print(f"\nRoom with ID {room_id} not found!\n")
            return
        
        confirm = input(f"Are you sure you want to delete room {room['room_id']}? (yes/no): ").lower()
        if confirm == "yes":
            rooms.remove(room)
            save_rooms()
            print(f"\n✓ Room deleted successfully!\n")
        else:
            print("Deletion cancelled.\n")
    except ValueError:
        print("Invalid room ID!\n")


# ==================== BILLING FUNCTIONS ====================

def add_bill():
    """Create a new bill"""
    global billing_counter
    try:
        print("\n" + "="*50)
        print("CREATE NEW BILL")
        print("="*50)
        
        patient_id = int(input("Enter patient ID: "))
        if not any(p['patient_id'] == patient_id for p in patients):
            print("Patient not found!\n")
            return False
        
        room_charges = float(input("Enter room charges (Rs.): "))
        medicine_charges = float(input("Enter medicine charges (Rs.): "))
        doctor_consultation = float(input("Enter doctor consultation charges (Rs.): "))
        other_charges = float(input("Enter other charges if any (Rs.) [0 for none]: "))
        
        bill = {
            "bill_id": billing_counter,
            "patient_id": patient_id,
            "room_charges": room_charges,
            "medicine_charges": medicine_charges,
            "doctor_consultation": doctor_consultation,
            "other_charges": other_charges,
            "total_amount": room_charges + medicine_charges + doctor_consultation + other_charges,
            "bill_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "payment_status": "Pending"
        }
        billing.append(bill)
        billing_counter += 1
        save_billing()
        print(f"\n✓ Bill created successfully! Bill ID: {bill['bill_id']}\n")
        return True
    except ValueError:
        print("Invalid input! Please enter valid data.\n")
        return False

def view_all_bills():
    """Display all bills"""
    if not billing:
        print("\nNo bills found!\n")
        return
    
    print("\n" + "="*50)
    print("ALL BILLS")
    print("="*50)
    for bill in billing:
        print(f"""
    Bill ID: {bill['bill_id']}
    Patient ID: {bill['patient_id']}
    Room Charges: Rs. {bill['room_charges']}
    Medicine Charges: Rs. {bill['medicine_charges']}
    Doctor Consultation: Rs. {bill['doctor_consultation']}
    Other Charges: Rs. {bill['other_charges']}
    Total Amount: Rs. {bill['total_amount']}
    Bill Date: {bill['bill_date']}
    Payment Status: {bill['payment_status']}
        """)

def view_bills_by_patient():
    """Display bills for a specific patient"""
    try:
        patient_id = int(input("Enter patient ID: "))
        bills = [b for b in billing if b['patient_id'] == patient_id]
        
        if not bills:
            print(f"\nNo bills found for patient ID {patient_id}!\n")
            return
        
        print("\n" + "="*50)
        print(f"BILLS FOR PATIENT {patient_id}")
        print("="*50)
        total = 0
        for bill in bills:
            print(f"""
    Bill ID: {bill['bill_id']}
    Patient ID: {bill['patient_id']}
    Room Charges: Rs. {bill['room_charges']}
    Medicine Charges: Rs. {bill['medicine_charges']}
    Doctor Consultation: Rs. {bill['doctor_consultation']}
    Other Charges: Rs. {bill['other_charges']}
    Total Amount: Rs. {bill['total_amount']}
    Bill Date: {bill['bill_date']}
    Payment Status: {bill['payment_status']}
            """)
            total += bill['total_amount']
        print(f"\nTotal Amount Due: Rs. {total}\n")
    except ValueError:
        print("Invalid patient ID!\n")

def update_payment_status():
    """Update payment status"""
    try:
        bill_id = int(input("Enter bill ID: "))
        bill = next((b for b in billing if b['bill_id'] == bill_id), None)
        
        if not bill:
            print(f"\nBill with ID {bill_id} not found!\n")
            return
        
        print("\n" + "="*50)
        print("UPDATE PAYMENT STATUS")
        print("="*50)
        print("1. Pending")
        print("2. Partial")
        print("3. Paid")
        
        choice = input("Select status (1-3): ").strip()
        
        if choice == "1":
            bill['payment_status'] = "Pending"
        elif choice == "2":
            bill['payment_status'] = "Partial"
        elif choice == "3":
            bill['payment_status'] = "Paid"
        else:
            print("Invalid choice!\n")
            return
        
        save_billing()
        print(f"\n✓ Payment status updated successfully!\n")
    except ValueError:
        print("Invalid input!\n")


# ==================== MENU FUNCTIONS ====================

def display_main_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Appointment Management")
    print("4. Room Management")
    print("5. Billing Management")
    print("6. Reports")
    print("7. Load Sample Data")
    print("8. Exit")
    print("="*50)

def patient_menu():
    """Patient management submenu"""
    while True:
        print("\n" + "="*50)
        print("PATIENT MANAGEMENT")
        print("="*50)
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient by ID")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Back to Main Menu")
        print("="*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_all_patients()
        elif choice == "3":
            view_patient_by_id()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")

def doctor_menu():
    """Doctor management submenu"""
    while True:
        print("\n" + "="*50)
        print("DOCTOR MANAGEMENT")
        print("="*50)
        print("1. Add Doctor")
        print("2. View All Doctors")
        print("3. Search Doctor by ID")
        print("4. Update Doctor")
        print("5. Delete Doctor")
        print("6. Back to Main Menu")
        print("="*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_doctor()
        elif choice == "2":
            view_all_doctors()
        elif choice == "3":
            view_doctor_by_id()
        elif choice == "4":
            update_doctor()
        elif choice == "5":
            delete_doctor()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")

def appointment_menu():
    """Appointment management submenu"""
    while True:
        print("\n" + "="*50)
        print("APPOINTMENT MANAGEMENT")
        print("="*50)
        print("1. Schedule Appointment")
        print("2. View All Appointments")
        print("3. View Appointments by Patient")
        print("4. Update Appointment")
        print("5. Delete Appointment")
        print("6. Back to Main Menu")
        print("="*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_appointment()
        elif choice == "2":
            view_all_appointments()
        elif choice == "3":
            view_appointments_by_patient()
        elif choice == "4":
            update_appointment()
        elif choice == "5":
            delete_appointment()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")

def room_menu():
    """Room management submenu"""
    while True:
        print("\n" + "="*50)
        print("ROOM MANAGEMENT")
        print("="*50)
        print("1. Add Room")
        print("2. View All Rooms")
        print("3. View Available Rooms")
        print("4. Assign/Update Room")
        print("5. Delete Room")
        print("6. Back to Main Menu")
        print("="*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_room()
        elif choice == "2":
            view_all_rooms()
        elif choice == "3":
            view_available_rooms()
        elif choice == "4":
            update_room_availability()
        elif choice == "5":
            delete_room()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")

def billing_menu():
    """Billing management submenu"""
    while True:
        print("\n" + "="*50)
        print("BILLING MANAGEMENT")
        print("="*50)
        print("1. Create Bill")
        print("2. View All Bills")
        print("3. View Bills by Patient")
        print("4. Update Payment Status")
        print("5. Back to Main Menu")
        print("="*50)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_bill()
        elif choice == "2":
            view_all_bills()
        elif choice == "3":
            view_bills_by_patient()
        elif choice == "4":
            update_payment_status()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

def reports_menu():
    """Reports submenu"""
    print("\n" + "="*50)
    print("REPORTS")
    print("="*50)
    print(f"Total Patients: {len(patients)}")
    print(f"Total Doctors: {len(doctors)}")
    print(f"Total Appointments: {len(appointments)}")
    print(f"Total Rooms: {len(rooms)}")
    print(f"Total Bills: {len(billing)}")
    print("="*50)
    
    if billing:
        total_revenue = sum(b['total_amount'] for b in billing)
        pending_amount = sum(b['total_amount'] for b in billing if b['payment_status'] == "Pending")
        paid_amount = sum(b['total_amount'] for b in billing if b['payment_status'] == "Paid")
        
        print(f"\nTotal Revenue (All Bills): Rs. {total_revenue}")
        print(f"Amount Paid: Rs. {paid_amount}")
        print(f"Amount Pending: Rs. {pending_amount}")
        print("="*50 + "\n")

def main():
    """Main application loop"""
    print("\n" + "="*50)
    print("WELCOME TO HOSPITAL MANAGEMENT SYSTEM")
    print("="*50 + "\n")
    
    init_database()
    
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            patient_menu()
        elif choice == "2":
            doctor_menu()
        elif choice == "3":
            appointment_menu()
        elif choice == "4":
            room_menu()
        elif choice == "5":
            billing_menu()
        elif choice == "6":
            reports_menu()
        elif choice == "7":
            add_sample_data()
        elif choice == "8":
            print("\nThank you for using Hospital Management System!")
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...\n")
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
