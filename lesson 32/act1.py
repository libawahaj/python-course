class A:

    def __init__(self, a):
        self.a = a

    def __It__(self,other):
        if(self.a > other.a):
            print("Obj1 is greater than obj2.")
        
        else:
            print("Obj2 is greater than obj1")

    def __equal__(self, other):
        if(self.a == other.a):
            print("Obj1 is equal to obj2.")

        else:
            print("Obj1 is not equal to obj2.")

obj1 = A(2)
obj2 = A(3)
print("The passed values are ", obj1.a ," and ", obj2.a)
print(obj1.a > obj2.a)

obj3 = A(4)
obj4 = A(4)
print("The passed values are ", obj3.a ," and ", obj4.a)
print(obj3.a == obj4.a)