from person import Person


class Customer(Person):

    def __init__(self, _name, location, custref):        # pass string to named variable
        super().__init__(_name, location)                # inherit arguments from Person class
        self.custref= custref      # attribute specific to Customer class

    def report(self, quantity, colour):
        print("Hi", self._name, ", your order details are: \n",
              "Customer reference:", self.custref, "\n",
              quantity, "boxes of", colour, "paper \n"
                 "  ---------------\n"
              "Dispatching to:", self.location)

    def newlocation(self, newlocation):
        if len(newlocation) > 3:
            self.location = newlocation
