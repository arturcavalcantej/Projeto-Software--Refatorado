from Empregado import Empregado
from pStrategy import Alteradois


class Comissionado(Empregado):
    def __init__(self, name, address, salary, bonus):
        super().__init__(name, address, salary, bonus)
        self.kind = "Comissionado"
        self._bonus = float(bonus)
        self.paymentMethod = None
        self.wallet = []
        self.lastIndexPayed = 0
        self.netIncome = float(0)

    def Edit(self, name, address, salary, bonus):
        self.name = name
        self.address = address
        self.salary = salary
        self.bonus = bonus

    def EditData(self, dictionary, key):
        Alteradois.alterapessoal(self, dictionary, key)

    def SetLastIndex(self, index):
        self.lastIndexPayed = index

    def getLastIndex(self):
        return self.lastIndexPayed

    def setPaymentMethod(self, method):
        self.paymentMethod = method

    def GetIncome(self, sales):
        if (len(sales) == 0):
            return self.salary
        else:
            balance = 0
            for i in range(self.lastIndexPayed, len(sales)):
                balance += sales[i].value
            self.lastIndexPayed = len(sales)
            income = ((self._bonus) / 100) * balance + self.salary
            return income

    def GetSalary(self):
        return self.salary

    def GetBonus(self):
        return self._bonus

    def PutInWallet(self, payment):
        self.wallet.append(payment)

    def GetLastPaymentDay(self):
        if (len(self.wallet) == 0):
            return None
        else:
            return self.wallet[-1].date

    def GetNetIncome(self):
        if (len(self.wallet) > 0):
            for x in self.wallet:
                self.netIncome += x.value
        print("Saldo Bancário: R${}".format(self.netIncome))

    def PrintLastPayment(self):
        if (len(self.wallet) > 0):
            print(self.wallet[-1].date)
        else:
            print("Nenhum pagamento recebido")
