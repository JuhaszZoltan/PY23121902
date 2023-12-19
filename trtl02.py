from turtle import *

bgcolor('black')
p = Pen()
p.speed(0)

cols = ['red', 'yellow', 'blue', 'green']
name = textinput("Írd be a neved", "Hogy hívnak?")

for x in range(100):
    p.pencolor(cols[x%4])
    p.penup()
    p.forward(x * 4)
    p.pendown()
    p.write(name, font = ('Arial', int((x + 4) / 4), 'bold'))
    p.left(92)
done()