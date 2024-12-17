from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I'm a human and can walk and run on 2 legs")

class Lion(Animal):

    def move(self):
        print("I'm a lion and I walk and run on 4 legs")

class Cat(Animal):

    def move(self):
        print("I'm a cat and I can run and walk on 4 legs")

class Snake(Animal):

    def move(self):
        print("I'm a snake and I slither.")

obj1 = Human()
obj1.move()

obj2 = Lion()
obj2.move()

obj3 = Cat()
obj3.move()

obj4 = Snake()
obj4.move()