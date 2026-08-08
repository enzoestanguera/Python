import math
from turtle import *

def heart1(M):
    return 15 * math.sin(M) ** 3

def heart2(M):
    return (12 * math.cos(M)
            - 5 * math.cos(2 * M)
            - 2 * math.cos(3 * M)
            - math.cos(4 * M))

speed(0)
hideturtle()
bgcolor("black")
color("red")

for i in range(380):

    M = i * 2 * math.pi / 380

    x = heart1(M) * 18
    y = heart2(M) * 18

    goto(0, 0)
    goto(x, y)

done()