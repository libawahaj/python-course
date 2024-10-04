import turtle 

sc = turtle.Screen()

sc.bgcolor("pink")
sc.setup(500,500)

p = turtle.Turtle()

num_sides= 4
len = 70
angle= 90 #since its a suqare its angles is always 90 degrees

for i in range(num_sides):
    p.forward(len)
    p.right(angle)

turtle.done()