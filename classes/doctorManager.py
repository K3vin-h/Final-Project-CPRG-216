#import the doctor class from the doctor file
from classes.doctor import Doctor
'''doctor manager class'''
class doctorManager:
    def __init__(self):
        self.doctors = [] #list of the doctors classes
        '''read the doctors file, by calling the read doctors file function'''
        self.read_doctors_file()

    '''append the doctor class str output to the doctors list, the class str output does the formating of the doctor information'''
    def format_dr_info(self, doctor):
        return self.doctors.append(str(doctor))
    
    '''create a doctor object and return the class object and the id'''
    def enter_dr_info(self):
        id = input("Enter the doctor’s ID: ")
        for dr in self.doctors: #check if the id is already on the system
            if dr.Doctor_ID == id:
                print("The id is already taken")
                return None, None
        #if id does not exist, then create a doctor object
        name = input("Enter the doctor’s name: ")
        speciality = input("Enter the doctor’s specility: ")
        timing = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor’s qualification: ")
        room_number = input("Enter the doctor’s room number: ")
        return Doctor(id, name, speciality, timing, qualification, room_number), id
    
    '''read the doctor file, then create a doctor object and append it to the doctors list'''
    def read_doctors_file(self):
        try:
            temp = []
            with open('data/doctors.txt', 'r') as file: #read the doctor file
                for line in file:
                    temp.append(line) #append each line to the temp list
            temp.pop(0) #remove the first line
            for line in temp: #for each line in the temp list
                if len(line) > 5: #ensures that the line is not empty
                    doctor = Doctor(*line.strip().split('_'))
                    #split the line by each underscore, and each element that was split by the underscore will be passed as an argument for creating a doctor class
                    self.doctors.append(doctor) #append the doctor class to the doctors list
        except FileNotFoundError: #if the file is not found, display this error message
            print("The file not found")
        except Exception as error: #if there are any other errors, display error message with the error in it.
            print(f"error: {error}")

    '''search for a doctor by id, if the doctor is found, display the doctor information, else display an error message'''
    def search_doctor_by_id(self):
        id = input("Enter the id of the doctor: ")
        for dr in self.doctors: #for each doctor in the doctors list, check if the id provided is the same as one of the doctor id
            if dr.Doctor_ID == id:
                self.display_doctors_info(dr)
                return
        return print("Can't find the doctor with the same ID on the system")
    
    '''search for a doctor by name, if the doctor is found, display the doctor information, else display an error message'''
    def search_doctor_by_name(self):
        name = input("Enter the name of the doctor: ")
        for dr in self.doctors:
            if dr.Doctor_name in name: #check if the name provided is in the doctor name
                self.display_doctors_info(dr)
                return
        return print("Can't find the doctor with the same ID on the system")
    
    '''display the doctor information that was called'''
    def display_doctors_info(self,dr):
        print(f"Id   Name                   Speciality      Timing          Qualification   Room Number")
        print(f"\n{dr.Doctor_ID:<4} {dr.Doctor_name:<22} {dr.Doctor_speciality:<15} {dr.Working_time:<15} {dr.Qualification:<15} {dr.Room_number:<10}") #display the doctor information, using getters

    '''edit the doctor information'''
    def edit_doctor_info(self):
        id = input("Please enter the id of the doctor that you want to edit their information: ")
        for dr in self.doctors:
            if dr.Doctor_ID == id: #check if the id provided is the same as one of the doctor id, if it is the same edit the doctor information
                dr.Doctor_name = input("Enter new Name: ")
                dr.Doctor_speciality = input("Enter new Specilist in: ")
                dr.Working_time = input("Enter new Timing: ")
                dr.Qualification = input("Enter new Qualification: ")
                dr.Room_number = input("Enter new Room number: ")
                self.write_list_of_doctors_to_file()
                print(f"Doctor whose ID is {id} has been edited")
                return
        return print(f"Can't find the doctor with the same ID ({id}) on the system")
    
    '''display the list of all doctors'''
    def display_doctors_list(self):
        print(f"Id   Name                   Speciality      Timing          Qualification   Room Number")
        for dr in self.doctors: # for each doctor in the doctors list, display the doctor information
            print(f"\n{dr.Doctor_ID:<4} {dr.Doctor_name:<22} {dr.Doctor_speciality:<15} {dr.Working_time:<15} {dr.Qualification:<15} {dr.Room_number:<10}")

    '''write the list of doctors to the doctor txt file'''
    def write_list_of_doctors_to_file(self):
        with open('data/doctors.txt', 'w') as file: #open the doctor file with write permission
            file.write("id_name_specilist_timing_qualification_roomNb\n") #write this first line, since it was removed when reading the file
            for dr in self.doctors: #then write the doctor information to the file
                file.write(f"{dr}\n")
                
    '''add a doctor to the file, it calls on the write doctor to file function'''
    def add_dr_to_file(self):
       class_, id = self.enter_dr_info() 
       if class_ == None: #stops the program if the id is already taken
           return
       self.format_dr_info(class_) #format the new doctor information and append it to the doctors list
       self.write_list_of_doctors_to_file() #write the doctor information to the file
       print(f"Doctor whose ID is {id} has been added") 

#testing purposes 
# def main():
#     dr_manager = doctorManager()
#     # dr_manager.display_doctors_list()
#     # # dr_manager.search_doctor_by_id()
#     # dr_manager.search_doctor_by_name()
#     # dr_manager.edit_doctor_info()
#     dr_manager.add_dr_to_file()
#     # dr_manager.display_doctors_info()
# main()




