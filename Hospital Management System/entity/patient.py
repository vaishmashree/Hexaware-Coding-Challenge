""" a. patientId
    b. firstName
    c. lastName;
    d. dateOfBirth
    e. gender
    f. contactNumber
    g. address       """


class patient:

    def __init__(self):
        self.__patientId = None
        self.__firstName = None
        self.__lastName = None
        self.__dateOfBirth = None
        self.__gender = None
        self.__contactNumber = None
        self.__address = None

    def __init__(self,patientId,firstName,lastName,dateOfBirth,gender,contactNumber,address):
        self.__patientId=patientId
        self.__firstName=firstName
        self.__lastName=lastName
        self.__dateOfBirth=dateOfBirth
        self.__gender=gender
        self.__contactNumber=contactNumber
        self.__address=address

    def setpatientId(self,patientId):
        self.__patientId=patientId

    def setfirstName(self,firstName):
        self.__firstName=firstName

    def setlastName(self,lastName):
        self.__lastName=lastName

    def setdateOfBirth(self,dateOfBirth):
        self.__dateOfBirth=dateOfBirth

    def setgender(self,gender):
        self.__gender=gender

    def setcontactNumber(self,contactNumber):
        self.__contactNumber=contactNumber

    def setaddress(self,address):
        self.__address=address

    def getpatientId(self):
        return self.__patientId
    
    def getfirstName(self):
        return self.__firstName
    
    def getlastName(self):
        return self.__lastName
    
    def getdateOfBirth(self):
        return self.__dateOfBirth
    
    def getgender(self):
        return self.__gender
    
    def getcontactNumber(self):
        return self.__contactNumber
    
    def getaddress(self):
        return self.__address
    
    def __str__(self):
        return f"Patient ID: {self.__patientId}, First Name: {self.__firstName}, Last Name: {self.__lastName}, 
        Date of Birth: {self.__dateOfBirth}, Gender: {self.__gender}, Contact Number: {self.__contactNumber}, 
        Address: {self.__address}"
    
    def printDetails(self):
        print(f"Patient ID: {self.__patientId}")
        print(f"Name: {self.__firstName} {self.__lastName}")
        print(f"DOB: {self.__dateOfBirth}")
        print(f"Gender: {self.__gender}")
        print(f"Contact: {self.__contactNumber}")
        print(f"Address: {self.__address}")