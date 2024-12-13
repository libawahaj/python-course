class Vehicle:

    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100
    
class Bus(Vehicle):

    def __init__(self, maint_charge):
        self.maint_charge = maint_charge

        
    def totalfare(self):
        Vehicle.__init__(self, self.seating_capacity)
        initialFare = super().fare()
        self.maint_charge = 0.1 * initialFare
        return self.maint_charge + self.maint_charge
    
vehicle = Bus(50)
print(vehicle.totalfare())