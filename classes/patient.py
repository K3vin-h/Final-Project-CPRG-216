class Patient:
    '''patient class with the attribes below'''
    def __init__(self, pid, name, disease, gender, age):
        self.__pid = pid
        self.__name = name
        self.__disease = disease
        self.__gender = gender
        self.__age = age
    '''string representation of the patient class'''
    def __str__(self):
        return f"{self.__pid}_{self.__name}_{self.__disease}_{self.__gender}_{self.__age}"
    '''getter'''
    @property
    def pid(self):
        return self.__pid
    '''setter'''
    @pid.setter
    def pid(self, pid):
        self.__pid = pid
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def disease(self):
        return self.__disease
    @disease.setter
    def disease(self, disease):
        self.__disease = disease
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender):
        self.__gender = gender
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age