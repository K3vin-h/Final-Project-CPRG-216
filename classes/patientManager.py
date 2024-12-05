from patient import Patient
class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()
    def format_patient_Info_for_file(self, patient):
        return self.patients.append(str(patient))
    def enter_patient_info(self):
        pass
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
        print()
        print(f"{patient.pid:<4} {patient.name:<22} {patient.disease:<15} {patient.gender:<15} {patient.age:<10}")
    def edit_patient_info_by_id(self):
        pass
    def display_patient_list(self):
        print(f"ID   Name                   Disease         Gender          Age")
        print()
        for patient in self.patients:
            print(f"{patient.pid:<4} {patient.name:<22} {patient.disease:<15} {patient.gender:<15} {patient.age:<10}\n") 
    def write_list_of_patients_to_file(self):
        pass
    def add_patient_to_file(self, patient):
        self.patients.append(patient)
        self.write_list_of_patients_to_file()

def main():
    x = PatientManager()
    x.display_patient_list()
main()