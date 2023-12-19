import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

turtle.bgcolor('black')
pen = turtle.Pen()
pen.speed(0)

for x in range(360):
    pen.pencolor(colors[x % len(colors)])
    pen.width(x/100 + 1)
    pen.forward(x)
    pen.left(360 / len(colors) - 1)