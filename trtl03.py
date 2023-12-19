from turtle import *

p = Pen()
p.speed(0)
bgcolor('black')

cols = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

sides = int(numinput('oldalak száma', 'hány oldalú spirált szeretnél (2-6)?', 4, 2, 6))

for x in range(100):
    p.forward(x*4)
    ps = p.pos()
    hd = p.heading()
    print(ps, hd)
    for y in range(int(x / 2)):
        p.pendown()
        p.pencolor(cols[y%sides])
        p.forward(2*y)
        p.right(360/sides - 2)
        p.penup()
    p.goto(ps)
    p.setheading(hd)
    p.left(360/sides + 2)

done()
