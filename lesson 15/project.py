#calculating the circumference of a circle

pi= 3.14

def circumference(pi, r): 
    return 2*pi*r

print("Calculating the circumference of a circle: ")
r = int(input("Enter the radius of your circle: "))

print("The circumference of your circle is ", circumference(pi,r))

