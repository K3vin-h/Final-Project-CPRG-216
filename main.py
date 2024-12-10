class AlbertaHospitalManagement:
    def __init__(self):
        print("Welcome to Alberta Hospital (AH) Management System")

    def main_menu(self):
        while True:
            menu = input("Select from the following options, or select 3 to stop:\n"
                         "1 - Doctors\n"
                         "2 - Patients\n"
                         "3 - Exit Program\n")
            if menu == "1":
                self.doctor_menu()
            elif menu == "2":
                self.patient_menu()
            elif menu == "3":
                print("Thanks for using the program. Bye!")
                break

    def doctor_menu(self):
        from classes.doctorManager import doctorManager
        doctor_manager = doctorManager()
        while True:
            menu = input("\nDoctors Menu:\n"
                         "1 - Display Doctors list\n"
                         "2 - Search for doctor by ID\n"
                         "3 - Search for doctor by name\n"
                         "4 - Add doctor\n"
                         "5 - Edit doctor info\n"
                         "6 - Back to the Main Menu\n")
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

    def patient_menu(self):
        from classes.patientManager import PatientManager
        patient_manager = PatientManager()
        while True:
            menu = input("\nPatients Menu:\n"
                         "1 - Display patients list\n"
                         "2 - Search for patient by ID\n"
                         "3 - Add patient\n"
                         "4 - Edit patient info\n"
                         "5 - Back to the Main Menu\n")
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
    management = AlbertaHospitalManagement()
    management.main_menu()
