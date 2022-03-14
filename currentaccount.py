from bankaccount import Bankacc


class Curracc(Bankacc):

    def __init__(self, _name, balance):        # pass string to named variable.  This is a constructor
        super().__init__(_name, balance)                # inheriting attributes from Person class

    def directdebit(self, amount):
        if self.balance < amount:
            print("Sorry, funds unavailable")
        else:
            self.balance = self.balance - amount
            print("Account number:", self._name, "Direct debit paid: £", amount)
