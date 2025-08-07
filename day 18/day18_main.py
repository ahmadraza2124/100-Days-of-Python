import turtle as t
from turtle import Turtle,Screen
import  random

t.colormode(255)
timmy = Turtle()
timmy.pensize(5)


colors = ["red", "blue", "green", "orange", "purple", "yellow", "pink", "cyan", "magenta", "brown"]
directions = [0, 90, 180, 270]


# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side in range(3, 10):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final_color = (r, g, b)
    return final_color

def random_walk(steps):
    for _ in range(steps):
        timmy.color(random_color())
        timmy.setheading(random.choice(directions))
        timmy.forward(30)

random_walk(100)

screen = Screen()
screen.exitonclick()