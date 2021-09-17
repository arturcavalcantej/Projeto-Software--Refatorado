from abc import ABC, abstractmethod
from Assalariado import Assalariado
from Comissionado import Comissionado
from Horista import Horista


class Inserirtemplate(ABC):


    @abstractmethod
    def instantiate(self):
        pass

    def add(self):
        self.name = input("Digite o nome: ")
        self.address = input("Digite o endereço: ")
        self.salary = float(input("Digite o salario: "))
        return self.instantiate()

class cadhorista(Inserirtemplate):

    def instantiate(self):
        self.employee = Horista(self.name, self.address, self.salary)
        return self.employee

class cadassalariado(Inserirtemplate):

    def instantiate(self):
        self.employee = Assalariado(self.name, self.address, self.salary)
        return self.employee

class cadcomissionado(Inserirtemplate):

    def instantiate(self):
        self.bonus = float(input("Digite o bônus percentual (%): "))
        self.employee = Comissionado(self.name, self.address, self.salary, self.bonus)
        return self.employee