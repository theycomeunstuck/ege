from turtle import *

speed(100) #скорость черепахи
tracer(0) #скорость расставления точек
pu() #pen up
pd() #pen down)


left(90)
m = 20
for i in range(2):
    forward(13*m)
    right(90)
    forward(20*m)
    right(90)
pu() #pen up
forward(8*m)
right(90)
backward(3*m)
left(90)
pd() #pen down)
for i in range(2):
    forward(16*m)
    right(90)
    forward(20*m)
    right(90)
pu()


for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3)
done()


#кумир мне нравится больше. а вдруг на сисадмине мудак и кумир стоит неправильный?
