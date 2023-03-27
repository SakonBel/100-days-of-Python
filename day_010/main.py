from turtle import Turtle, Screen
from random import randint, choice

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
timmy.color("coral")
timmy.pensize(1)
screen.colormode(255)
timmy.speed(0)

angle = 3

# Drawing different shape using turtle
# for _ in range(8):
#     timmy.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
#     for _ in range(angle):
#         timmy.forward(90)
#         timmy.right(360/angle)
#     angle += 1

# Drawing random walk
# direction = [90, 180, 270, 360]
# for _ in range(100):
#     # side = randint(1, 2)
#     timmy.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
#     timmy.forward(randint(10, 70))
#     timmy.setheading(choice(direction))
#     # if side == 1:
#     #     # timmy.left(randint(1, 360))
#     #     timmy.left(90)
#     # else:
#     #     # timmy.right(randint(1, 360))
#     #     timmy.right(90)

# Drawing circle and spirograph
# for _ in range(60):
#     timmy.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
#     timmy.circle(100)
#     timmy.right(6)

screen.exitonclick()
