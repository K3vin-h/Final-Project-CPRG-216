#import the patient class from the patient file
from classes.patient import Patient
'''patient manager class'''
class PatientManager:
    def __init__(self):
        self.patients = [] #list of the patients classes
        '''read the patients file by calling the read patients file function'''
        self.read_patients_file()

    '''append the patient class str output to the patients list'''
    def format_patient_Info_for_file(self, patient):
        return self.patients.append(str(patient))
    
    '''create a patient object and return the class object and the id'''
    def enter_patient_info(self):
        id = input("Enter the patient’s ID: ")
        for patient in self.patients:
            if patient.pid == id: #check if the patient id is already taken
                print("The id is already taken")
                return None, None
        name = input("Enter Patient name: ") #if not, then create a doctor object
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        return Patient(id, name, disease, gender, age), id
    
    '''read the patient file, and putting each line of the file in a list, then remove the first line, since it does not provide any patient information, then create a patient object and append it to the patients list'''
    def read_patients_file(self):
        try:
            temp = []
            with open('data/patients.txt', 'r') as file: #read the patient txt file
                for line in file:
                    temp.append(line) #append each line to the temp list
            temp.pop(0) #pop the first line
            for line in temp:
                if len(line) > 5: #ensure that the line is not empty
                    patient = Patient(*line.strip().split('_'))
                    #same method as the doctor file, see doctormanager file for explaination of the function
                    self.patients.append(patient)
        except FileNotFoundError: #error handling
            print("The file not found")
        except Exception as error:
            print(f"error: {error}")

    '''search for a patient by id, if the patient is found, display the patient information, else display an error message'''
    def search_patient_by_id(self):
        id = input("Enter the id of the patient: ")
        for patient in self.patients: #for each patient in the patients list, check if the id provided is the same as one of the patient id
            if patient.pid == id:
                self.display_patient_info(patient)
                return
        return print("Can't find the patient with the same ID on the system")
    
    '''display the patient information that is being called'''
    def display_patient_info(self, patient):
        print(f"ID   Name                   Disease         Gender          Age")
        print(f"\n{patient.pid:<4} {patient.name:<22} {patient.disease:<15} {patient.gender:<15} {patient.age:<10}") #done via getter methods 

    '''edit the patient information by id, if the patient is found, edit the patient information, else display an error message'''
    def edit_patient_info_by_id(self):
        id = input("Please enter the id of the patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.pid == id: #check if the id provided is the same as one of the patient id
                patient.name = input("Enter new Name: ")
                patient.disease = input("Enter new disease: ")
                patient.gender = input("Enter new gender: ")
                patient.age = input("Enter new age: ")
                self.write_list_of_patients_to_file()
                return
        return print(f"Can't find the patient with the same ID ({id}) on the system")
    
    '''display the all the patients information in a list'''
    def display_patient_list(self):
        print(f"ID   Name                   Disease         Gender          Age")
        for patient in self.patients: #for patients in the doctors list, display the patient information   
            print(f"\n{patient.pid:<4} {patient.name:<22} {patient.disease:<15} {patient.gender:<15} {patient.age:<10}\n") 
            
    '''write the patient information to the patient txt file'''
    def write_list_of_patients_to_file(self):
        with open('data/patients.txt', 'w') as file: #open the file with write
            file.write("id_Name_Disease_Gender_Age\n") # write the first line
            for patient in self.patients: #for each patient in the patients list, write the patient information to the file
                file.write(f"{patient}\n")
                
    '''add a patient to the file, uses the write list of patient to file function to write the patient to the file'''
    def add_patient_to_file(self):
        class_, id = self.enter_patient_info()
        if class_ == None: #if the class is none, then stop
            return
        self.format_patient_Info_for_file(class_) #format and append the patient information to the patients list
        self.write_list_of_patients_to_file() #write the patient information to the file
        print(f"Patient with ID {id} has been added to the system")

# testing purposes
# def main():
#     x = PatientManager()
#     # x.display_patient_list()
#     # x.edit_patient_info_by_id()
#     # x.search_patient_by_id()
#     # x.edit_patient_info_by_id()
#     # x.add_patient_to_file()
# main()