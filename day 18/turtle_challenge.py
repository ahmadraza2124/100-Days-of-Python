import turtle as t
from turtle import Turtle,Screen
import  random

t.colormode(255)
timmy = Turtle()
timmy.pensize(1)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final_color = (r, g, b)
    return final_color

def draw_circle(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_circle(5)

screen = Screen()
screen.exitonclick()