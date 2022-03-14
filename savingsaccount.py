from bankaccount import Bankacc


class Savacc(Bankacc):
    rate = float

    def __init__(self, _name, balance, rate):        # pass string to named variable.  This is a constructor
        super().__init__(_name, balance)                # inheriting attributes from Person class
        self.rate = rate

    def applyinterest(self):
        multiplier = 1 + self.rate/100
        self.balance = self.balance * multiplier
        print("Account number:", self._name, "Interest rate applied:", self.rate, "%")
        self.statebalance()

    def changeinterest(self, newrate):          # "setter" method to change interest rate
        if 0 <= newrate <= 100:
            self.rate = newrate
            print("Account number:", self._name, "Your new interest rate is:", self.rate, "%")
            