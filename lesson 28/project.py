class Circle:

    def __init__(self):
        self.radius = 0
        self.pi = 3.142

    def inp(self):
        r = int(input("Enter the radius of your circle in cm: "))
        self.radius = self.radius + r
    
    def area(self):
        area = self.pi * (self.radius**2)
        print("The area of your circle is ", area, "cm.")

    def perimeter(self):
        perimeter = 2 * self.pi * self.radius
        print("The circumference of your circle is ", perimeter, "cm.")

obj = Circle()
obj.inp()
obj.area()
obj.perimeter()