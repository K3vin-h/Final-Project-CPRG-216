#main file that runs the program
class Management:
    def __init__(self):
        '''Start of the program'''
        print("Welcome to Alberta Hospital (AH) Management System")

    def display_menu(self):
        '''Main menu of the program'''
        while True:
            menu = self.inputcheck(1, 3, "Select from the following options, or select 3 to stop:\n"
            # menu = input("Select from the following options, or select 3 to stop:\n"
                         "1 - Doctors\n"
                         "2 - Patients\n"
                         "3 - Exit Program\n")
            if menu == 1:
                self.doctor_menu()
            elif menu == 2:
                self.patient_menu()
            elif menu == 3:
                print("Thanks for using the program. Bye!")
                break

    def doctor_menu(self):
        '''Doctor menu of the program'''
        from classes.doctorManager import doctorManager
        doctor_manager = doctorManager()
        ''''import the doctorManager class from the doctorManager file'''
        '''the user gives an input and the program will do the following based on the input'''
        while True:
            menu = self.inputcheck(1, 6, "\nDoctors Menu:\n"
            # menu = input("\nDoctors Menu:\n"
                         "1 - Display Doctors list\n"
                         "2 - Search for doctor by ID\n"
                         "3 - Search for doctor by name\n"
                         "4 - Add doctor\n"
                         "5 - Edit doctor info\n"
                         "6 - Back to the Main Menu\n")
            if menu == 1:
                doctor_manager.display_doctors_list()
            elif menu == 2:
                doctor_manager.search_doctor_by_id()
            elif menu == 3:
                doctor_manager.search_doctor_by_name()
            elif menu == 4:
                doctor_manager.add_dr_to_file()
            elif menu == 5:
                doctor_manager.edit_doctor_info()
            elif menu == 6:
                break

    def patient_menu(self):
        '''Patient menu of the program'''
        from classes.patientManager import PatientManager
        patient_manager = PatientManager()
        '''import the PatientManager class from the patientManager file'''
        '''the user gives an input and the program will do the following based on the input'''
        while True:
            menu = self.inputcheck(1, 5, "\nPatients Menu:\n"
                         "1 - Display patients list\n"
                         "2 - Search for patient by ID\n"
                         "3 - Add patient\n"
                         "4 - Edit patient info\n"
                         "5 - Back to the Main Menu\n")
            # menu = input("\nPatients Menu:\n"
                        #  "1 - Display patients list\n"
                        #  "2 - Search for patient by ID\n"
                        #  "3 - Add patient\n"
                        #  "4 - Edit patient info\n"
                        #  "5 - Back to the Main Menu\n")
            if menu == 1:
                patient_manager.display_patient_list()
            elif menu == 2:
                patient_manager.search_patient_by_id()
            elif menu == 3:
                patient_manager.add_patient_to_file()
            elif menu == 4:
                patient_manager.edit_patient_info_by_id()
            elif menu == 5:
                break
    def inputcheck(self, min, max, text):
        '''checks if input is a number and if it is within the range of the min and max values'''
        while True:
            try:
                input_ = int(input(text))
                if min <= input_ <= max: #between the range min and max
                    return input_

                else:
                    print("Please enter a valid number")
            except ValueError: #if not a number
                print("Please enter a valid number")

'''the program starts here'''
if __name__ == "__main__":
    management = Management()
    management.main_menu()


