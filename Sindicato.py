class Sindicato:
    def __init__(self, key):
        self.key = key
        self.fee = float(120.00)

    def incrementFee(self, increment):
        self.fee += increment

    def getFee(self):
        return self.fee

    def __str__(self):
        return 'ID Sindical: {}\nTaxa sindical: R${}'.format(self.key, self.fee)