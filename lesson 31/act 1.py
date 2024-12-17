from abc import ABC, abstractmethod

class BC:

    def display(self,x):
        print("The passed value is ", x)

    @abstractmethod
    def task(self):
        print("This is the abstract method inside the parent class")

class CC(BC):

    def task(self):
        print("This is the abstract method inside the child class.")

obj = CC()
obj.task()