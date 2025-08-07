# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed('fastest')

colors_list = [(199, 158, 121), (64, 96, 128), (148, 86, 60), (136, 162, 187), (219, 208, 122),
               (186, 147, 160), (22, 39, 59), (120, 75, 92), (136, 178, 156), (52, 31, 22),
               (59, 118, 80), (172, 160, 44), (191, 98, 83), (59, 30, 41), (130, 25, 36),
               (145, 29, 21), (178, 99, 115), (24, 47, 41), (223, 172, 186), (224, 177, 169),
               (69, 159, 108), (111, 121, 161), (162, 208, 186), (30, 90, 53),
               (46, 62, 91), (180, 187, 212)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(colors_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()



