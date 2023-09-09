import turtle
turtle.bgcolor("Black")
squary=turtle.Turtle()
squary.speed(150)
for x in range(160):
    for color in ["red","blue","yellow"]:
        squary.pencolor(color)
        squary.forward(x)
        squary.left(60)
        squary.right(12)
