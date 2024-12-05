from classes.patient import Patient
class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()
    def format_patient_Info_for_file(self, patient):
        return self.patients.append(str(patient))
    def enter_patient_info(self):
        id = input("Enter the patient’s ID: ")
        for patient in self.patients:
            if patient.pid == id:
                print("The id is already taken")
                return None, None
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        return Patient(id, name, disease, gender, age), id
    def read_patients_file(self):
        try:
            temp = []
            with open('data/patients.txt', 'r') as file:
                for line in file:
                    temp.append(line)
            temp.pop(0)
            for line in temp:
                patient = Patient(*line.strip().split('_'))
                self.patients.append(patient)
        except FileNotFoundError:
            print("The file not found")
        except Exception as error:
            print(f"error: {error}")
    def search_patient_by_id(self):
        id = input("Enter the id of the patient: ")
        for patient in self.patients:
            if patient.pid == id:
                self.display_patient_info(patient)
                return
        return print("Can't find the patient with the same ID on the system")
    def display_patient_info(self, patient):
        print(f"ID   Name                   Disease         Gender          Age")
        print(f"\n{patient.pid:<4} {patient.name:<22} {patient.disease:<15} {patient.gender:<15} {patient.age:<10}")
    def edit_patient_info_by_id(self):
        id = input("Please enter the id of the patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.pid == id:
                patient.name = input("Enter new Name: ")
                patient.disease = input("Enter new disease: ")
                patient.gender = input("Enter new gender: ")
                patient.age = input("Enter new age: ")
                self.write_list_of_patients_to_file()
                return
        return print(f"Can't find the patient with the same ID ({id}) on the system")

    def display_patient_list(self):
        print(f"ID   Name                   Disease         Gender          Age")
        for patient in self.patients:
            print(f"\n{patient.pid:<4} {patient.name:<22} {patient.disease:<15} {patient.gender:<15} {patient.age:<10}\n") 
    def write_list_of_patients_to_file(self):
        with open('data/patients.txt', 'w') as file:
            file.write("id_Name_Disease_Gender_Age\n")
            for patient in self.patients:
                file.write(f"{patient}\n")
    def add_patient_to_file(self):
        class_, id = self.enter_patient_info()
        if class_ == None:
            return
        self.format_patient_Info_for_file(class_)
        self.write_list_of_patients_to_file()
        print(f"Patient with ID {id} has been added to the system")

# def main():
#     x = PatientManager()
#     # x.display_patient_list()
#     # x.edit_patient_info_by_id()
#     # x.search_patient_by_id()
#     # x.edit_patient_info_by_id()
#     # x.add_patient_to_file()
# main()