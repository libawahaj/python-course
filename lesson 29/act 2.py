class Person:

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("The name of the employee is ", self.name)
        print("The ID number of the employee is ", self.idnumber)

class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)

    def display(self):
    
        print("The salary of the employee is $", self.salary, " per month." )
        print("The position of the employee is ", self.post)

obj = Person("Bob", 1023)
obj.display()

employee = Employee("Bob", 1023, 800, "Intern")
employee.display()

