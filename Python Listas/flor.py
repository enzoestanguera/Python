import turtle
import math

turtle.setup(width=800, height=800)
turtle.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

cores = ["#ff69b4", "#00ffff", "#ffffff"]

for i in range(120):

    angulo = i * math.pi / 60

    for j in range(3):

        raio = 180 + j * 15

        x = raio * math.cos(angulo)
        y = raio * math.sin(angulo)

        t.penup()
        t.goto(x, y)
        t.pendown()

        t.color(cores[j])
        t.circle(raio)

turtle.done()