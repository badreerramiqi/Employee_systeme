from Employe import Employee  # Assuming the correct filename is "employee.py"
from IR import IR

class Trainer(Employee, IR):
    """
    Class representing a Trainer, inheriting from Employee and IR.
    """

    def __init__(self, mtle=0, nom="El Kelkha", dateNaissance="31/03/2005", dateEmbauche="12/01/2024", salaireBase=7000):
        """
        Constructor for the Trainer class.
        Initializes the Trainer with specified parameters and sets default values for overtime hours and hourly rate.
        """
        super().__init__(mtle, nom, dateNaissance, dateEmbauche, salaireBase)
        self.__heureSup = 0
        self.__tarifHsup = 70
    
    @property
    def getheureSup(self):
        """
        Getter method for the number of overtime hours.
        """
        return self.__heureSup
    
    @property
    def gettarifHsup(self):
        """
        Getter method for the overtime hourly rate.
        """
        return self.__tarifHsup
    
    def setheureSup(self, hs1):
        """
        Setter method for the number of overtime hours.
        """
        self.__heureSup = hs1
    
    def settarifHsup(self, ths1):
        self.__tarifHsup = ths1
    
    def __str__(self):
        return super().__str__() + f"Number of overtime hours per month: {self.getheureSup} - Remuneration per overtime hour: {self.gettarifHsup}"

    def getIR(self, salaire):
        for i in range(0, len(IR._tranches), 2):
            if IR._tranches[i] <= salaire <= IR._tranches[i + 1]:
                y = int(i / 2)
                return IR._tauxIR[y]
        return IR._tauxIR[len(IR._tauxIR) - 1]

    def salaireAPayer(self):
        return (self.getsalaireBase + self.getheureSup * self.gettarifHsup) * (1 - self.getIR(self.getsalaireBase))