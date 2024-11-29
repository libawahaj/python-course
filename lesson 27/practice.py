#This is how classes and objects are created
class Students:

    def __init__(self): 
        print("This is an initialization function.")

s1 = Students()

#creating the methods and attributes and accessing them outside of the class

class Students2:

    def __init__(self,name,age):
        self.name = name
        self.age = age #using self to make these attributes accessible outside of the innit function

    def print_details(self):
        print("The name is ", self.name)
        print("The age is ", self.age)

s2 = Students2("Sam", 17)

s2.print_details()

#accessing the attributes outside of the class

class Students3:

    def __init__(self,name,age):
        self.name = name
        self.age = age #using self to make these attributes accessible outside of the innit function


s3 = Students3("Umar", 10)
print(s3.name)
print(s3.age)