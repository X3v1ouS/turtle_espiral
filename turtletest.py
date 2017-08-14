import turtle

colors = ["red", "white", "blue", "green", "yellow", "orange"]

pes = turtle.Pen()
pes.speed(5)
turtle.bgcolor("black")

for x in range(360):
    pes.pencolor(colors[x%len(colors)])
    pes.width(x/100+1)
    pes.forward(x)
    pes.left(59)

