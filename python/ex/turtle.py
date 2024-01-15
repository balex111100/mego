from turtle import *
import random

screen = Screen()
screen.setup(width=600, height=600)

user_bet = screen.textinput(title="Make your bet!",
                            prompt="Which color turtle will win the rice? (red , blue , orange, purpale , gray , black): ")
# print(f' you choose {user_bet}')
colors = ["red", "blue", "orange", "purple", "Gray", "black"]
# name = ["Raphael", "Leonardo", " Michelangelo", "Donatello", "Splinter", "Casey Jones"]
y_position = [250, 150, 50, -50, -150, -250]
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

            flag = 0
            break

screen.exitonclick()
