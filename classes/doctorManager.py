from doctor import Doctor
class doctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    def format_dr_info(self, doctor):
        return self.doctors.append(str(doctor))
    
    def enter_dr_info(self):
        id = input("Enter the doctor’s ID: ")
        for dr in self.doctors:
            if dr.Doctor_ID == id:
                print("The id is already taken")
                return None, None
        name = input("Enter the doctor’s name: ")
        speciality = input("Enter the doctor’s specility: ")
        timing = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor’s qualification: ")
        room_number = input("Enter the doctor’s room number: ")
        return Doctor(id, name, speciality, timing, qualification, room_number), id
    
    def read_doctors_file(self):
        try:
            temp = []
            with open('data/doctors.txt', 'r') as file:
                for line in file:
                    temp.append(line)
            temp.pop(0)
            for line in temp:
                doctor = Doctor(*line.strip().split('_'))
                self.doctors.append(doctor)
        except FileNotFoundError:
            print("The file not found")
        except Exception as error:
            print(f"error: {error}")

    def search_doctor_by_id(self):
        id = input("Enter the id of the doctor: ")
        for dr in self.doctors:
            if dr.Doctor_ID == id:
                self.display_doctors_info(dr)
                return
        return print("Can't find the doctor with the same ID on the system")
    
    def search_doctor_by_name(self):
        name = input("Enter the name of the doctor: ")
        for dr in self.doctors:
            if dr.Doctor_name in name:
                self.display_doctors_info(dr)
                return
        return print("Can't find the doctor with the same ID on the system")
        
    def display_doctors_info(self,dr):
        print(f"Id   Name                   Speciality      Timing          Qualification   Room Number")
        print()
        print(f"{dr.Doctor_ID:<4} {dr.Doctor_name:<22} {dr.Doctor_speciality:<15} {dr.Working_time:<15} {dr.Qualification:<15} {dr.Room_number:<10}")

    def edit_doctor_info(self):
        id = input("Please enter the id of the doctor that you want to edit their information: ")
        for dr in self.doctors:
            if dr.Doctor_ID == id:
                dr.Doctor_name = input("Enter new Name: ")
                dr.Doctor_speciality = input("Enter new Specilist in: ")
                dr.Working_time = input("Enter new Timing: ")
                dr.Qualification = input("Enter new Qualification: ")
                dr.Room_number = input("Enter new Room number: ")
                self.write_list_of_doctors_to_file()
                return
        return print(f"Can't find the doctor with the same ID ({id}) on the system")
    
    def display_doctors_list(self):
        print(f"Id   Name                   Speciality      Timing          Qualification   Room Number")
        print()
        for dr in self.doctors:
            print(f"{dr.Doctor_ID:<4} {dr.Doctor_name:<22} {dr.Doctor_speciality:<15} {dr.Working_time:<15} {dr.Qualification:<15} {dr.Room_number:<10}\n")

    def write_list_of_doctors_to_file(self):
        with open('data/doctors.txt', 'w') as file:
            file.write("id_name_specilist_timing_qualification_roomNb\n")
            for dr in self.doctors:
                file.write(f"{dr}\n")

    def add_dr_to_file(self):
       class_, id = self.enter_dr_info()
       if class_ == None:
           return
       self.format_dr_info(class_)
       self.write_list_of_doctors_to_file()
       print(f"Doctor whose ID is {id} has been added")

def main():
    dr_manager = doctorManager()
    # dr_manager.display_doctors_list()
    # # dr_manager.search_doctor_by_id()
    # dr_manager.search_doctor_by_name()
    # dr_manager.edit_doctor_info()
    dr_manager.add_dr_to_file()
    # dr_manager.display_doctors_info()
main()



