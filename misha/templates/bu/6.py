from turtle import *

speed(100) #скорость черепахи
tracer(0) #скорость расставления точек
pu() #pen up
pd() #pen down

m = 20
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3)
done()

