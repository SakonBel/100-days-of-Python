from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
timmy.color("coral")
timmy.pensize(4)
screen.colormode(255)
timmy.speed(2)

angle = 3

# Drawing different shape using turtle
for _ in range(8):
    timmy.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
    for _ in range(angle):
        timmy.forward(90)
        timmy.right(360/angle)
    angle += 1

screen.exitonclick()
