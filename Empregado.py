from abc import ABC, abstractmethod


class Empregado(ABC):
    @abstractmethod
    def __init__(self, name, address,salary,bonus):
        self.name = name
        self.address = address
        self.salary = salary
        self.bonus = bonus

    def companyEmail(self):
        return '{}@company.com'.format(self.name)

    def __str__(self):
        return 'Dados do funcionário:\nNome: {}\nEndereco: {}\n'.format(self.name, self.address)