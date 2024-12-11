class Vehicle:

    def __init__(self, name, maxs, mileage):
        self.name = name
        self.maxs= maxs
        self.mileage= mileage

    def display(self):
        print("The name of the vehicle is ", self.name)
        print("The max speed of the vehicle is ", self.maxs, " km/h.")
        print("The mileage of the vehicle is ", self.mileage)

class Bus(Vehicle):
    pass

b = Bus("School Volvo", 450, 17)
b.display()