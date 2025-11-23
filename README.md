#Clinic Health Tracker

A Python-based program for small clinic patient health record management.

Overview of the project

Clinics can use this technology as a digital registry.By enabling staff to register patients, compute BMI automatically, and save visit history in a text file, it replaces human paperwork.

Features

1. Patient Registration: Make profiles that include your name, age, height, and weight.
2. Automated Vitals: Automatically determines BMI and classifies-Underweight, Normal, Obese.
3. History Tracking: Keeps a record of each patients checkup date and outcome.
4. Data Persistence: To prevent data loss upon leave, records are saved to `clinic_data.txt` via file handling.
5. Search: Locate patients using their unique IDs.

Technologies/tools used

1. Lang: Python 3
2. Concepts Used
3. Object oriented programming
4. File input and output
5. Data Structures
6. Control Flow and Function

Steps to install & run the project

1. Ensure you have python installed.
2. Download the repository files(patient.py, storage.py, main.py) 
3. Open terminal/Command prompt and navigate to the folder where you saved the file.
4. Run the main program by typing the following command and hit Enter: bash python main.py
5. Follow on-screen menu instructions to add patients.

Testing

1. Registratin Test:
   Select option 1 and enter valid data.Check if ID is generated.
2. Calculation Test:
   Select option 2 and enter a known height and weight and verify if the BMI is correct.
3. Persistence Test:
   Add a patient, "Save and Exit", then restart the app. The patient should still be there.

Screen shots

   Input
   
   <img width="940" height="1211" alt="image" src="https://github.com/user-attachments/assets/ff138378-219d-427d-ac5f-708af714d6f3" />
   <img width="940" height="873" alt="image" src="https://github.com/user-attachments/assets/62225b2a-f081-4003-9e4a-4ac030f27030" />
   <img width="940" height="1329" alt="image" src="https://github.com/user-attachments/assets/80f5f70b-8d53-4d48-bfa4-1f197533df5f" />
   <img width="806" height="1391" alt="image" src="https://github.com/user-attachments/assets/a6929595-3116-431f-b9aa-6e00fc7c12be" />
  
   Output
   
   <img width="779" height="1061" alt="image" src="https://github.com/user-attachments/assets/27c006cd-b2cf-4c4e-8813-4cd185ba51e6" />
   <img width="779" height="316" alt="image" src="https://github.com/user-attachments/assets/a9665160-aa95-4848-a512-0977d545ec9b" />





