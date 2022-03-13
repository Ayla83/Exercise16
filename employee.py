from person import Person


class Employee(Person):
    position = ""

    def __init__(self, _name, location, position):        # pass string to named variable.  This is a constructor
        super().__init__(_name, location)                # inheriting attributes from Person class
        self.position = position                        # attribute specific to Employee class

    def role(self):
        if self.position == "reception":
            print("Which service do you require?")
        elif self.position == "sales":
            print("Would you like to buy some paper?")
        elif self.position == "accounts":
            print("How would you like to pay?")

    def changerole(self, newposition):          # change the value - a "setter" method
        if len(newposition) > 4:
            self.position = newposition
