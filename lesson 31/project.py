class Ferrari:

    def fuel_type(self):
        print("The fuel type for Ferrari is premium fuel.")

    def max_speed(self):
        print("The highest maximum speed for a Ferrari is 249 mph.")

class BMW:

    def fuel_type(self):
        print("The fuel type for BMW is premium gasoline.")

    def max_speed(self):
        print("The highest maximum speed for a BMW is 191 mph.")

obj_ferarri = Ferrari()
obj_bmw = BMW()

for car in (obj_ferarri, obj_bmw):
    car.fuel_type()
    car.max_speed()

