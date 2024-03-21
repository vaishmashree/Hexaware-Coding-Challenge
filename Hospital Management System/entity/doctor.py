""" a. doctorId
    b. firstName
    c. lastName
    d. specialization
    e. contactNumber; """

class doctor:

    def __init__(self):
        self.__doctorId=None
        self.__firstName=None
        self.__lastName=None
        self.__specialization=None
        self.__contactNumber=None

    def __init__(self,doctorId, firstName, lastName, specialization, contactNumber):
        self.__doctorId=doctorId
        self.__firstName=firstName
        self.__lastName=lastName
        self.__specialization=specialization
        self.__contactNumber=contactNumber

    def setdoctorId(self,doctorId):
        self.__doctorId=doctorId
    
    def setfirstName(self,firstName):
        self.__firstName=firstName
    
    def setlastName(self,lastName):
        self.__lastName=lastName
    
    def setspecialization(self,specialization):
        self.__specialization=specialization
    
    def setcontactNumber(self,contactNumber):
        self.__contactNumber=contactNumber

    def getdoctorId(self):
        return self.__doctorId
    
    def getfirstName(self):
        return self.__firstName
    
    def getlastName(self):
        return self.__lastName
    
    def getspecialization(self):
        return self.__specialization
    
    def getcontactNumber(self):
        return self.__contactNumber
    
    def __str__(self):
        return f"Doctor Id: {self.__doctorId}, First Name: {self.__firstName}, Last Name: {self.__lastName}, 
        Specialization: {self.__specialization}, Contact Number: {self.__contactNumber}"
    
    def printDetails(self):
        print(f"Doctor Id: {self.__doctorId}")
        print(f"First Name: {self.__firstName}")
        print(f"Last Name: {self.__lastName}")
        print(f"Specialization: {self.__specialization}")
        print(f"Contact Number: {self.__contactNumber}")