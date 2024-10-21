#sin cos tan program

import math

num_degrees = int(input("Enter the number you want the sin, cos, and tan value of: "))

num_radian = math.radians(num_degrees)

sine = math.sin(num_radian)
cos = math.cos(num_radian)
tan = math.tan(num_radian)

print("The value of sin ", num_degrees , " is ", sine)
print("The value of cos ", num_degrees , " is ", cos)
print("The value of tan ", num_degrees , " is ", tan)

