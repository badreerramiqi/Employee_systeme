# Importing necessary modules
from datetime import datetime
from IEmploye import IEmployee
from abc import ABCMeta, abstractmethod

class Employee(IEmployee, metaclass=ABCMeta):
    # Class variable to keep track of the total number of employees
    _counter = 0

    def __init__(self, mtle=0, nom="Er-Ramiqi ", dateNaissance="20/10/2004", dateEmbauche="12/01/2024", salaireBase=7000):
        # Incrementing the class counter to assign a unique identifier to each employee
        Employee._counter += 1
        # Setting instance attributes for the employee
        self.__mtle = Employee._counter
        self.__nom = nom
        self.__dateNaissance = dateNaissance
        self.__dateEmbauche = dateEmbauche
        self.__salaireBase = salaireBase
    
    @property
    def getmtle(self): 
        return self.__mtle
    
    @property
    def getnom(self):
        return self.__nom
    
    @property
    def getdateNaissance(self):
        return self.__dateNaissance
    
    @property
    def getdateEmbauche(self):
        return self.__dateEmbauche
    
    @property
    def getsalaireBase(self):
        return self.__salaireBase
    
    def setmtle(self, mtle):
        self.__mtle = mtle
    
    def setnom(self, nom):
        self.__nom = nom
    
    def setdateNaissance(self, dateNaissance):
        self.__dateNaissance = dateNaissance
    
    def setsalaireBase(self, salaireBase):
        self.__salaireBase = salaireBase
    
    def setdateEmbauche(self, dateEmbauche):
        # Check if the employee is at least 20 years old before setting the employment date
        if self.Age(dateEmbauche) < 20:
            print("Unable to hire an employee who is not yet 20 years old")
        else:
            self.__dateEmbauche = dateEmbauche
    
    @abstractmethod
    def salaireAPayer(self):
        # Abstract method to calculate the salary to be paid (to be implemented by subclasses)
        pass

    def Age(self, dateEmbauche):
        dateNaissance = datetime.strptime(self.getdateNaissance, '%d/%m/%Y')
        dateEmbauche = datetime.strptime(dateEmbauche, '%d/%m/%Y')

        # Calculate the age based on the year of employment
        age = dateEmbauche.year - dateNaissance.year
        return age
    
    def Seniority(self):
        nowyear = datetime.now().year
        dateEmbauche = datetime.strptime(self.getdateEmbauche, '%d/%m/%Y')
        
        # Calculate the years of service
        return nowyear - dateEmbauche.year
    
    def RetirementDate(self, retirement_age):
        dateNaissance = datetime.strptime(self.getdateNaissance, '%d/%m/%Y')
        
        # Calculate the retirement date based on the retirement age
        return dateNaissance.year + retirement_age
    
    def __str__(self):
        # String representation of the employee
        return f"Employee ID: {self.getmtle} - Name: {self.getnom} - Date of Birth: {self.getdateNaissance} - Employment Date: {self.getdateEmbauche} - Base Salary: {self.getsalaireBase} - "
    
    def __eq__(self, other):
        # Check if two employees are equal based on their employee ID
        return self.getmtle == other.getmtle