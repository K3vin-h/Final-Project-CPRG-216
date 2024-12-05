

def main():
    print("Welcome to Alberta Hospital (AH) Managment system ")
    while True:
        menu = input("Select from the following options, or select 3 to stop:\n1 - 	Doctors\n2 - 	Patients\n3 -	Exit Program\n")
        if menu == "1":
            docmenu()

        elif menu == "2":
            patientmenu()

        elif menu == "3":
            print("Thanks for using the program. Bye!")
            break

def docmenu():
    from classes.doctorManager import doctorManager
    doctor_manager = doctorManager()
    while True:
        menu = input("\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n")
        if menu == "1":
            doctor_manager.display_doctors_list()
        elif menu == "2":
            doctor_manager.search_doctor_by_id()
        elif menu == "3":
            doctor_manager.search_doctor_by_name()
        elif menu == "4":
            doctor_manager.add_dr_to_file()
        elif menu == "5":
            doctor_manager.edit_doctor_info()
        elif menu == "6":
            break

def patientmenu():
    from classes.patientManager import PatientManager
    patient_manager = PatientManager()
    while True:
        menu = input("\nPatients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n")
        if menu == "1":
            patient_manager.display_patient_list()
        elif menu == "2":
            patient_manager.search_patient_by_id()
        elif menu == "3":
            patient_manager.add_patient_to_file()
        elif menu == "4":
            patient_manager.edit_patient_info_by_id()
        elif menu == "5":
            break
    
if __name__ == "__main__":
    main()