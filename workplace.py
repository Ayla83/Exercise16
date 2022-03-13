# Design at least 3 classes: person, employee and customer
# Consider appropriate constructors, properties and methods for these classes
# Demonstrate understanding of encapsulation, inheritance and polymorphism
# Create a client script and instantiate objects based on the above classes
# and call their methods and set their properties to demonstrate working functionality

from employee import Employee
from customer import Customer

worker1 = Employee("Pam", "Leeds,", "reception")        # instantiating Employee objects
worker2 = Employee("Jim", "Cardiff", "sales")
worker3 = Employee("Kevin", "Manchester", "accounts")

customer1 = Customer("David", "London", 9876)              # instantiating Customer objects
customer2 = Customer("Alexis", "Melbourne", 9877)

worker1.sayyourname()                           # calling method from person.py
worker1.statelocation()
worker1.role()                                  # calling method from employee.py

customer1.sayyourname()                         # method from person.py
customer1.statelocation()                       # method from person.py

worker2.sayyourname()
worker2.role()

customer1.report(5, "blue")                      # calling method from customer.py

worker3.sayyourname()
worker3.role()

customer2.sayyourname()                         # another example of methods, this time applied to customer2
customer2.report(7, "green")
customer2.newlocation("Sheffield")              # method to change value - a "setter" method
customer2.statelocation()
customer2.report(10, "purple")




