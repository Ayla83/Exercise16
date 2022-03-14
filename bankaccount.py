class InsufficientFundsException(Exception):
    pass


class Bankacc:
    _name = ""                      # starting with underscore means it is a private attribute
    balance = float

    def __init__(self, _name, balance):        # pass string to named variable.  This is a constructor
        self._name = _name
        self.balance = balance

    def statebalance(self):
        print("Account number:", self._name, "Your current balance is: £", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account number:", self._name, "Paid in: £", amount)

# Write logic to ensure exception is raised if withdrawal results in account going overdrawn

    def withdraw(self, amount):
        try:
            self.balance = self.balance - amount
            if self.balance < 0:
                self.balance = self.balance + amount
                raise InsufficientFundsException()
        except InsufficientFundsException as err:
            print("Unable to withdraw £", amount, ", funds unavailable", err)
        else:
            print("Account number:", self._name, "Withdrawn: £", amount)
