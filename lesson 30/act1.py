class Sample:

    __privVar = 5

    def __init__(self):
        print("This is the constructor")

    def __privMeth(self):
        print("This is a private method")

    def hello(self):
        print("The value is ", Sample.__privVar)

obj = Sample()
obj.hello()
obj.__privVar