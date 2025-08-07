from turtle import Turtle, Screen
import random

screen = Screen()


# def move_forward():
#     timmy.forward(10)
#
# def rotate_left():
#     timmy.left(10)
#
# def rotate_right():
#     timmy.right(10)
#
# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
#
#
# screen.listen()
# screen.onkey(move_forward, 'w')
# screen.onkey(rotate_left, 'a')
# screen.onkey(rotate_right, 'd')
# screen.onkey(clear, 'c')

is_race_on = False

screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your choice", prompt='Which turtle will win the race? Enter a color: ')
colors = ["red", "blue", "yellow", "green", "black"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 5):
    new_turtles = Turtle(shape='turtle')
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtles)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You won! The winner is {winning_color}")
            else:
                print(f"You lose! The winner is {winning_color}")
        random_distant = random.randint(0, 10)
        turtle.forward(random_distant)


screen.exitonclick()
