from patient import Patient
from storage import save_to_file, load_from_file
all_patients = []
current_id_counter = 100
def input_number(message):
    while True:
        try:
            val = float(input(message))
            if val > 0:
                return val
            else:
                print("Please enter a positive value.")
        except:
            print("That's not a valid number. Try again.")
def find_patient(target_id):
    for p in all_patients:
        if str(p.pid) == str(target_id):
            return p
    return None
def create_patient():
    global current_id_counter
    print("\n--- Add New Patient ---")
    
    name = input("Enter Patient Name: ")
    age = int(input_number("Enter Age: "))
    h = input_number("Enter Height (in meters, e.g. 1.75): ")
    w = input_number("Enter Weight (in kg, e.g. 70.5): ")
    new_p = Patient(name, age, h, w, pid=current_id_counter)
    all_patients.append(new_p)
    
    print("\nSuccess! Patient added with ID:", current_id_counter)
def update_vitals():
    pid = input("\nEnter Patient ID to update: ")
    person = find_patient(pid)
    
    if person:
        print("Updating records for:", person.name)
        person.height = input_number("New Height (m): ")
        person.weight = input_number("New Weight (kg): ")
        date_str = input("Enter today's date (YYYY-MM-DD): ")
        person.add_record(date_str)
    else:
        print("Patient not found!")
def view_details():
    pid = input("\nEnter Patient ID to search: ")
    person = find_patient(pid)
    
    if person:
        person.show_info()
        person.show_history()
    else:
        print("Patient not found!")
def start_app():
    global all_patients, current_id_counter
    all_patients = load_from_file()
    if len(all_patients) > 0:
        highest_id = 0
        for p in all_patients:
            if int(p.pid) > highest_id:
                highest_id = int(p.pid)
        current_id_counter = highest_id + 1
    while True:
        print("\n==========================")
        print(" CLINIC HEALTH TRACKER")
        print("==========================")
        print("1. Register Patient")
        print("2. Update Vitals (BMI)")
        print("3. View Patient History")
        print("4. Show All IDs")
        print("5. Save & Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            create_patient()
        elif choice == '2':
            update_vitals()
        elif choice == '3':
            view_details()
        elif choice == '4':
            print("\n--- List of Patients ---")
            for p in all_patients:
                print("ID:", p.pid, "- Name:", p.name)
        elif choice == '5':
            save_to_file(all_patients)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
start_app()