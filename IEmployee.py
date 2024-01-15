from abc import ABCMeta, abstractmethod

class IEmployee(metaclass=ABCMeta):
    
    @abstractmethod
    def Age(self):
        pass

    @abstractmethod
    def Seniority(self):
        pass

    @abstractmethod
    def RetirementDate(self, retirement_age):
        pass