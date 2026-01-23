# 🏥 Hospital Management System

## Overview
A comprehensive hospital management system built with Python using pickle (binary file storage). It manages patients, doctors, appointments, rooms, and billing with complete functionality for healthcare facility operations.

## Features

### 1. **Patient Management**
- Register new patients
- Maintain patient medical records
- Track patient admission and discharge
- Monitor patient status (Active/Discharged/Deceased)
- Store patient contact information
- Record disease/condition information

### 2. **Doctor Management**
- Register doctors with specializations
- Track doctor availability
- Assign doctors to patients
- Maintain doctor qualifications
- Schedule doctor working hours
- Doctor performance records

### 3. **Appointment Scheduling**
- Book patient-doctor appointments
- Check appointment availability
- Confirm appointments
- Cancel appointments
- Reschedule appointments
- Appointment history tracking

### 4. **Room Management**
- Track hospital rooms
- Assign rooms to patients
- Monitor room occupancy
- Room type categorization (General, Semi-Private, Private)
- Room charge management

### 5. **Billing System**
- Generate patient bills
- Track room charges
- Track medicine charges
- Track doctor consultation fees
- Payment status monitoring
- Bill settlement

### 6. **Medical Records**
- Maintain prescription records
- Track medicines prescribed
- Medical history documentation
- Test results storage
- Diagnosis recording

## Data Storage Structure

### Pickle Binary Files
The system stores data in binary format within `hospital_data/` directory:

```
hospital_data/
├── patients.pkl          # Patient records
├── doctors.pkl           # Doctor information
├── appointments.pkl      # Appointment details
├── rooms.pkl             # Room inventory
└── billing.pkl           # Billing records
```

## Main Features in Code

### Key Methods

#### Patient Operations
- `add_patient()` - Register new patient
- `view_all_patients()` - List all patients
- `view_patient_by_id()` - Specific patient details
- `update_patient()` - Modify patient info
- `discharge_patient()` - Discharge from hospital
- `search_patients()` - Search by criteria

#### Doctor Operations
- `add_doctor()` - Register new doctor
- `view_all_doctors()` - List doctors
- `view_doctor_by_id()` - Doctor details
- `update_doctor()` - Modify doctor info
- `search_doctors()` - Search by specialization

#### Appointment Management
- `book_appointment()` - Schedule appointment
- `view_appointments()` - List appointments
- `confirm_appointment()` - Confirm booking
- `cancel_appointment()` - Cancel appointment
- `reschedule_appointment()` - Change appointment time

#### Room Management
- `add_room()` - Add new room
- `view_rooms()` - List all rooms
- `assign_room()` - Assign to patient
- `discharge_room()` - Free up room

#### Billing Operations
- `generate_bill()` - Create bill
- `view_bills()` - List bills
- `process_payment()` - Record payment
- `generate_receipt()` - Create receipt

## Installation & Setup

```bash
# 1. Create hospital_data directory (auto-created on first run)
# 2. Python 3.7+ required
# 3. Run the system
python hospital_management.py
```

## Usage

```python
from hospital_management import *

# Initialize database
init_database()

# Add patient
add_patient()
# Output: Patient added successfully! Patient ID: 1000

# View all patients
view_all_patients()

# Add doctor
add_doctor()

# Book appointment
book_appointment()

# Generate bill
generate_bill()
```

## Menu Options

```
HOSPITAL MANAGEMENT SYSTEM
═════════════════════════════════════

1. Patient Management
   - Add New Patient
   - View All Patients
   - Search Patient
   - Update Patient
   - Discharge Patient

2. Doctor Management
   - Register Doctor
   - View All Doctors
   - Search Doctor
   - Update Doctor Details
   - View Doctor Schedule

3. Appointment Management
   - Book Appointment
   - View Appointments
   - Confirm Appointment
   - Cancel Appointment
   - Reschedule Appointment

4. Room Management
   - Add Room
   - View Rooms
   - Assign Room to Patient
   - Discharge Room
   - View Room Status

5. Billing & Payments
   - Generate Bill
   - View Bills
   - Process Payment
   - Generate Receipt
   - Payment History

6. Medical Records
   - Record Prescription
   - View Medical History
   - Record Test Results
   - Add Diagnosis

7. Reports
   - Patient Report
   - Doctor Report
   - Room Occupancy
   - Billing Report
   - Department Report

8. Exit
```

## Sample Data Structure

### Patient Record
```python
{
    "patient_id": 1000,
    "name": "Raj Kumar",
    "age": 45,
    "gender": "Male",
    "address": "123 Main St, City",
    "phone": "9876543210",
    "disease": "Diabetes",
    "admission_date": "2026-01-21 10:30:00",
    "discharge_date": None,
    "status": "Active"
}
```

### Doctor Record
```python
{
    "doctor_id": 100,
    "name": "Dr. Priya Sharma",
    "qualification": "MBBS, MD",
    "specialization": "Cardiology",
    "phone": "9876543211",
    "email": "priya@hospital.com",
    "experience": 10,
    "available": True
}
```

### Appointment Record
```python
{
    "appointment_id": 500,
    "patient_id": 1000,
    "doctor_id": 100,
    "appointment_date": "2026-01-25 10:00:00",
    "reason": "Heart Checkup",
    "status": "Confirmed",
    "created_date": "2026-01-21 10:30:00"
}
```

## Sample Operations

### Add New Patient
```
═════════════════════════════════════
ADD NEW PATIENT
═════════════════════════════════════

Enter patient name: Raj Kumar
Enter age: 45
Enter gender: Male
Enter address: 123 Main St, City
Enter phone number: 9876543210
Enter disease/reason: Diabetes Mellitus

✓ Patient added successfully!
Patient ID: 1000
Admission Date: 2026-01-21 10:30:00
```

### Register Doctor
```
═════════════════════════════════════
REGISTER DOCTOR
═════════════════════════════════════

Enter doctor name: Dr. Priya Sharma
Enter qualification: MBBS, MD
Enter specialization: Cardiology
Enter phone number: 9876543211
Enter email: priya@hospital.com
Enter years of experience: 10

✓ Doctor registered successfully!
Doctor ID: 100
```

### Book Appointment
```
═════════════════════════════════════
BOOK APPOINTMENT
═════════════════════════════════════

Enter patient ID: 1000
Enter doctor ID: 100
Enter appointment date (YYYY-MM-DD HH:MM:SS): 2026-01-25 10:00:00
Enter reason: Heart Checkup

✓ Appointment booked successfully!
Appointment ID: 500
Date: 2026-01-25 10:00:00
```

### Assign Room to Patient
```
═════════════════════════════════════
ASSIGN ROOM TO PATIENT
═════════════════════════════════════

Enter patient ID: 1000
Enter room ID: 1
Room Type: Private
Room Charges per day: ₹5000

✓ Room assigned successfully!
Patient ID: 1000
Room: 101
Check-in Date: 2026-01-21
```

### Generate Bill
```
═════════════════════════════════════
PATIENT BILL
═════════════════════════════════════

Patient ID: 1000
Patient Name: Raj Kumar
Admission Date: 2026-01-21
Discharge Date: 2026-01-28
Number of Days: 7

CHARGES:
Room Charges (7 days @ ₹5000): ₹35,000.00
Medicine Charges:              ₹8,500.00
Doctor Consultation:           ₹3,000.00
Tests & Diagnostics:           ₹5,000.00
Other Charges:                 ₹2,000.00
─────────────────────────────────────
Subtotal:                       ₹53,500.00
Tax (5%):                       ₹2,675.00
─────────────────────────────────────
TOTAL AMOUNT:                   ₹56,175.00
Payment Status: Pending
═════════════════════════════════════
```

### Medical Records
```
═════════════════════════════════════
MEDICAL RECORDS - PATIENT 1000
═════════════════════════════════════

Patient Name: Raj Kumar
Patient ID: 1000

MEDICAL HISTORY:
- Diabetes Mellitus (diagnosed 10 years ago)
- Hypertension (diagnosed 5 years ago)
- Allergic to Aspirin

CURRENT MEDICATIONS:
- Metformin 500mg - 2 tablets daily
- Amlodipine 5mg - 1 tablet daily
- Aspirin alternative prescribed

RECENT TESTS:
- Blood Sugar: 185 mg/dL (High)
- BP: 140/90 mmHg (High)
- Cholesterol: 220 mg/dL (High)

DIAGNOSIS: Type 2 Diabetes with Hypertension
═════════════════════════════════════
```

## Technical Details

| Aspect | Details |
|--------|---------|
| Language | Python 3.7+ |
| Storage | Pickle (Binary files) |
| Files | 5 pickle files |
| CRUD Operations | Full support |
| Data Validation | Input validation implemented |
| Error Handling | Try-catch mechanism |
| ID Generation | Auto-incrementing |

## Data Models

### Patient Model
```
patient_id: Unique ID (auto-generated)
name: Patient full name
age: Age in years
gender: Male/Female/Other
address: Residential address
phone: Contact number
disease: Primary disease/condition
admission_date: Check-in timestamp
discharge_date: Check-out timestamp
status: Active/Discharged/Deceased
```

### Doctor Model
```
doctor_id: Unique ID (auto-generated)
name: Doctor full name
qualification: Medical qualifications
specialization: Area of specialization
phone: Contact number
email: Email address
experience: Years of experience
available: Availability status
```

### Room Model
```
room_id: Unique ID
room_number: Physical room number
room_type: General/Semi-Private/Private
capacity: Beds in room
charge_per_day: Daily rate
status: Available/Occupied
floor: Floor number
features: Room amenities
```

## Reporting Features

### Patient Report
```
Total Patients: 15
Active Patients: 10
Discharged Patients: 4
Deceased: 1

Average Stay: 5.2 days
Average Bill: ₹45,000
```

### Doctor Report
```
Total Doctors: 8
By Specialization:
- Cardiology: 2
- Orthopedics: 2
- Neurology: 1
- General Surgery: 2
- Pediatrics: 1
```

### Room Occupancy Report
```
Total Rooms: 20
Occupied: 12
Available: 8
Occupancy Rate: 60%

By Type:
- Private: 10 (occupied: 8)
- Semi-Private: 7 (occupied: 3)
- General: 3 (occupied: 1)
```

## Best Practices

1. **Data Accuracy** - Verify patient information
2. **Confidentiality** - Maintain medical privacy
3. **Regular Backups** - Back up pickle files
4. **Error Logging** - Track errors
5. **User Authentication** - Use login systems in production

## Error Handling

```
Error: Patient not found
Solution: Verify patient ID

Error: Doctor unavailable
Solution: Check doctor schedule

Error: Room not available
Solution: Select different room

Error: File corrupted
Solution: Restore from backup
```

## File Operations

### Pickle File Handling
- Binary format storage
- Automatic serialization
- Data integrity checks
- Automatic directory creation

### Data Persistence
- All changes saved to pickle files
- No database required
- Easy data export/import

## Troubleshooting

### Data Not Saving
```
Solution:
- Check write permissions
- Verify hospital_data directory exists
- Check disk space
```

### Cannot Load Data
```
Solution:
- Verify file integrity
- Restore from backup
- Re-initialize if corrupted
```

### Appointment Conflicts
```
Solution:
- Check doctor availability
- Select alternate time slot
- Consult scheduling calendar
```

## Academic Applications

Ideal for learning:
- Pickle file operations
- Data management
- Object serialization
- Healthcare system design
- Complex data structures
- Project submission (Class 11/12)

## Future Enhancements

- Database migration (MySQL)
- Web interface (Flask/Django)
- Mobile app
- Email notifications
- SMS alerts
- Online appointment booking
- Medical imaging integration
- Insurance processing
- Telemedicine support

## License

Educational use - CBSE Computer Science Curriculum

---

**Last Updated**: January 2026

For queries, refer to the code comments or system documentation.
