class Doctor:
    '''doctor class with its attributes below'''
    def __init__ (self, Doctor_ID, Doctor_name, Doctor_speciality, Working_time, Qualification, Room_number):
        self.__Doctor_ID = Doctor_ID
        self.__Doctor_name = Doctor_name
        self.__Doctor_speciality = Doctor_speciality
        self.__Working_time = Working_time
        self.__Qualification = Qualification
        self.__Room_number = Room_number
    '''string representation of the doctor class'''
    def __str__(self):
        return f"{self.Doctor_ID}_{self.Doctor_name}_{self.Doctor_speciality}_{self.Working_time}_{self.Qualification}_{self.Room_number}"
    '''getter'''
    @property
    def Doctor_ID(self):
        return self.__Doctor_ID
    '''setter'''
    @Doctor_ID.setter
    def Doctor_ID(self, Doctor_ID):
        self.__Doctor_ID = Doctor_ID
    @property
    def Doctor_name(self):
        return self.__Doctor_name
    @Doctor_name.setter
    def Doctor_name(self, Doctor_name):
        self.__Doctor_name = Doctor_name
    @property
    def Doctor_speciality(self):
        return self.__Doctor_speciality
    @Doctor_speciality.setter
    def Doctor_speciality(self, Doctor_speciality):
        self.__Doctor_speciality = Doctor_speciality
    @property
    def Working_time(self):
        return self.__Working_time
    @Working_time.setter
    def Working_time(self, Working_time):
        self.__Working_time = Working_time
    @property
    def Qualification(self):
        return self.__Qualification
    @Qualification.setter
    def Qualification(self, Qualification):
        self.__Qualification = Qualification
    @property
    def Room_number(self):
        return self.__Room_number
    @Room_number.setter
    def Room_number(self, Room_number):
        self.__Room_number = Room_number