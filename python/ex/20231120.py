# list
# my_list = [1, 2, 3]

# tuples
# my_tuple = (1, 3, 8)

# tuples are immutable

# import turtle as t
# import random
#
# tim = t.Turtle()

# event listeners

# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# screen.listen()
# bind
# keystroke
# event


# def move_forwards():
#     tim.forward(10)


# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()
#
# def function_a(something):
# do this with something
# then, do this
# finally, do that

# def function_b():
# do something_new

# function_a(function_b())

# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# def calculator(n1, n2, func):
#     return func(n1, n2)
#
#
# result = calculator(2, 3, divide)
# print(result)
# higher order functions

# for number in range(1, 101):
#     if number % 7 == 0 or number / 7 == 0:
#         print("b")
#     if number % 7 == 0:
#         print("7")
#     if number / 5 == 0:
#         print("b")
#     else:
#         print([number])
#
# Object State and Instances
# Turtle Coordinate System

from turtle import *
import random


screen = Screen()
screen.setup(width=600, height=600)

user_bet = screen.textinput(title="Make your bet!", prompt="Which color turtle will win the rice? (red , blue , orange, purpale , gray , black): ")
# print(f' you choose {user_bet}')
colors = ["red", "blue", "orange", "purple", "Gray", "black"]
# name = ["Raphael", "Leonardo", " Michelangelo", "Donatello", "Splinter", "Casey Jones"]
y_position = [250 ,150, 50, -50, -150  ,-250]
list = []



for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.shapesize(2, 2)
    tim.penup()


    tim.fd(80)
    tim.color(colors[turtle_index])

    tim.goto(x=-220, y=y_position[turtle_index])
    list.append(tim)

flag = 1
while flag:
    for i in range(0, 6):

        list[i].forward(random.randint(5, 30))
        if list[i].xcor() > 220:

            if list[i].pencolor() == user_bet:

                print(f"your {colors[0]} turtle is the winner")
            else:
                print(f"the winner is {colors[i]} unfortunately you chose {colors[0]} :( ")

            flag= 0
            break


screen.exitonclick()
