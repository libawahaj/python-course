class Vehicle:
    
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity  

    def fare(self):
        return self.seating_capacity * 100  
    
class Bus(Vehicle):

    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)  

    def totalfare(self):
        inital_fare = super().fare()  
        maint_charge = 0.1 * inital_fare  
        return inital_fare + maint_charge  
    

vehicle = Bus(50)
print(vehicle.totalfare())  
