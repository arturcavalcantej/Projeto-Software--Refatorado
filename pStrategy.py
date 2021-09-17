from abc import ABC, abstractmethod


class Altera(ABC):

    @abstractmethod
    def alterapessoal(self, dictionary, key):
        pass


class Alteraum(Altera):

    def alterapessoal(self, dictionary, key):
        newName = input("Digite o novo nome: ")
        newAddress = input("Digite o novo endereço: ")
        newSalary = float(input("Digite o novo salário: "))
        dictionary[key]['worker'].Edit(newName, newAddress, newSalary)


class Alteradois(Altera):

    def alterapessoal(self, dictionary, key):
        newName = input("Digite o novo nome: ")
        newAddress = input("Digite o novo endereço: ")
        newSalary = float(input("Digite o novo salário: "))
        newBonus = float(input("Digite o novo bonus: "))
        dictionary[key]['worker'].Edit(newName, newAddress, newSalary, newBonus)
