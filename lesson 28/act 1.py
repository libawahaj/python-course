#making user input into all uppercase using classes

class sample:

    def __init__(self):
        self.str1 = ""

    def inp(self):
        self.str1 = input("Enter your name: ")
        print("The name you have entered is ", self.str1)

    def uppercase(self):
        uppercased = self.str1.upper()
        print("The uppercase version of this name is ", uppercased)


s1 = sample()
s1.inp()
s1.uppercase()