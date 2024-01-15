from abc import ABCMeta, abstractmethod

class IR(metaclass=ABCMeta):
    _tranches = [0, 30000, 30001, 50000, 50001, 60000, 60001, 80000, 80001, 180000]
    _tauxIR = [0, 10, 20, 30, 34, 38]

    @classmethod
    @abstractmethod
    def getIR(cls, salaire):
        pass