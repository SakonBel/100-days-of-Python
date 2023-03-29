from turtle import Turtle, Screen
import random
# import colorgram


# all_colors = []
# colors = colorgram.extract("./day_010/hirst_painting/image.png", 80)

# for color in colors:
#     all_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

# print(all_colors)

color_list = [(233, 233, 232), (234, 230, 232), (226, 232, 228), (230, 232, 236), (207, 160, 84), (54, 89, 131), (145, 91, 39), (139, 26, 50), (221, 207, 107), (133, 176, 201), (45, 55, 103), (170, 158, 41), (157, 47, 83), (129, 188, 143), (83, 19, 42), (37, 43, 67), (185,
                                                                                                                                                                                                                                                                             92, 106), (185, 140, 170), (85, 121, 180), (58, 38, 31), (88, 155, 92), (78, 152, 164), (194, 78, 72), (79, 73, 44), (45, 74, 76), (161, 201, 218), (57, 128, 121), (43, 76, 75), (220, 181, 167), (217, 176, 188), (178, 188, 211), (170, 205, 178), (149, 36, 33), (37, 61, 61)]
screen = Screen()
screen.colormode(255)

timmy = Turtle()

timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)


for _ in range(10):
    for _ in range(10):
        timmy.pendown()
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)

    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

screen.exitonclick()
