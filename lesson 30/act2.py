class Computer:

    def __init__(self):
        self.__maxPrice= 500 
        print('This is a constructor')

    def sell(self):
        print('The Selling Price is ', self.__maxPrice)

    def setmaxprice(self,price):
        self.__maxPrice = price

obj = Computer()

obj.maxPrice = 1000
obj.sell()

obj.setmaxprice(1000)
obj.sell()