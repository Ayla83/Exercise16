class Person:
    name = ""  # starting with underscore means it is a private attribute
    location = ""

    def __init__(self, _name, location):        # pass string to named variable.  This is a constructor
        self._name = _name
        self.location = location

    def sayyourname(self):              # reads the value - a "getter" method
        print("My name is", self._name)

    def statelocation(self):              # reads the value - a "getter" method
        print("My location is", self.location)
