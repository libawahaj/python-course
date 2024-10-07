import turtle 

sc= turtle.Screen()

sc.bgcolor("maroon")
sc.setup(800,500)

p= turtle.Turtle()

p.color("white")

sides = 3
len = 80
angle= 360/sides

for i in range(sides):
    p.forward(len)
    p.right(angle)

turtle.done()