from Empregado import Empregado
from pStrategy import Alteraum

class Assalariado(Empregado):

    def __init__(self, name, address, salary, bonus=None):
        super().__init__(name, address, salary, bonus)
        self.kind = "Assalariado"
        self._salary = float(salary)
        self.paymentMethod = None
        self.wallet = []
        self.netIncome = float(0)

    def Edit(self, name, address, salary):
        self.name = name
        self.address = address
        self._salary = float(salary)

    def EditData(self, dictionary, key):
        Alteraum.alterapessoal(self, dictionary, key)

    def setPaymentMethod(self, method):
        self.paymentMethod = method

    def GetIncome(self):
        return self._salary

    def PutInWallet(self, payment):
        self.wallet.append(payment)

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

    def __str__(self):
        return super().__str__() + 'Tipo de empregado: {}'.format(self.kind)
