import turtle
turtle.Screen().bgcolor("lightgreen")
turtle.Screen().setup(800,800)
polygon=turtle.Turtle()
sides=6
side_length=200
angle=360/sides
for i in range(sides):
    polygon.forward(side_length)
    polygon.left(angle)
    turtle.done