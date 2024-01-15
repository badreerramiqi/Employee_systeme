# Importing the Employe and IR classes
from Employe import Employee
from IR import IR

# Defining the Agent class, which inherits from Employe and IR
class Agent(Employee, IR):
    def __init__(self, mtle=0, nom="El Kelkha", dateNaissance="31/03/2005", dateEmbauche="12/01/2024", salaireBase=7000, primeResponsabilite=0):
        # Calling the constructor of the parent classes (Employe and IR)
        super().__init__(mtle, nom, dateNaissance, dateEmbauche, salaireBase)
        # Adding a new attribute specific to the Agent class
        self.primeResponsabilite = primeResponsabilite

    def getIR(self, salaire):
        # Calculating the income tax rate based on salary
        for i in range(0, len(IR._tranches), 2):
            if IR._tranches[i] <= salaire <= IR._tranches[i + 1]:
                y = int(i / 2)
                return IR._tauxIR[y]
        # If salary exceeds the last defined bracket, use the highest tax rate
        return IR._tauxIR[len(IR._tauxIR) - 1]

    def salaireAPayer(self):
        # Calculating the net salary to be paid
        return (self.getsalaireBase + self.primeResponsabilite) * (1 - self.getIR(self.getsalaireBase))