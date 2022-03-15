from currentaccount import Curracc
from savingsaccount import Savacc

current1 = Curracc("1234", 200)         # instantiate a Curracc object
current1.statebalance()                 # call method from bankaccount.py

current1.directdebit(30)                # call method from currentaccount.py
current1.statebalance()

current1.deposit(25)
current1.statebalance()

current1.withdraw(60)
current1.statebalance()


current2 = Curracc("1235", 400)      # instantiate another Curracc object
current2.statebalance()

current2.withdraw(500)                     # method from bankaccount - attempt to withdraw too much and raise exception


savings1 = Savacc("2234", 1000, 2)         # instantiate a Savacc object
savings1.statebalance()

savings1.applyinterest()                    # call method from savingsaccount.py

savings1.changeinterest(3)                  # use a "setter" method to change attribute
savings1.applyinterest()


savings2 = Savacc("2235", 2000, 5)         # instantiate another Savacc object
savings2.statebalance()

savings2.applyinterest()

savings2.withdraw(3000)                     # method from bankaccount - attempt to withdraw too much and raise exception
