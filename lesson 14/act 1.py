import turtle 

sc = turtle.Screen()

sc.bgcolor("yellow")
sc.setup(600,600)

p = turtle.Turtle()

num_sides= 6
len = 70
angle= 360/num_sides

for i in range(num_sides):
    p.forward(len)
    p.right(angle)

turtle.done()

