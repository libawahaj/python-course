class Roman:

    def __init__(self):
        self.numerals = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X"}

    def inp(self):
        number = int(input("Enter any number from 1-10: "))
        self.userinp = number
        print("The passed value is ", self.userinp)

    def converter(self):
        romanNum = self.numerals[self.userinp]
        print("This number in roman numerals is ", romanNum)

obj = Roman()
obj.inp()
obj.converter()
    
