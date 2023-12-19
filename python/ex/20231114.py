# import turtle as t
# tim = t.Turtle()
#
# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.color("red")
# timmy.pencolor("red")
# timmy.shape("turtle")
# timmy.forward(100)
#
'''
Your mission (5 minutes) is to:
Draw a black square, and show an arrow instead of a turtle 
'''
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
#
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)
'''
Ass. 2:
Draw a dashed line

'''

"""
from turtle import Turtle, Screen
from random import random

timmy = Turtle()
timmy.shape("arrow")
timmy.color(random(), random(), random())


x =3
while x < 11:
    for _ in range(x):

       timmy.forward(100)
       timmy.left(360/x)
    timmy.color(random(), random(), random())
    x+=1


screen = Screen()
screen.exitonclick()
"""



'''from turtle import Turtle, Screen
from random import randint , random
def  drunk_walking():
    timmy = Turtle()
    # timmy.shape("turtle")
    timmy.color(randint(0, 255) / 255.0, randint(0, 255) / 255.0, randint(0, 255) / 255.0)
    timmy.width(7)
    timmy.speed('normal')
    kawabanga = 0
    while kawabanga < 1:

        timmy.circle(100)
        # timmy.position()
        timmy.right(10)

        # timmy.position()
    for _ in range(36):  # Repeat the following block 36 times to create a full circle
        timmy.circle(100)  # Draw a circle with radius 100
        timmy.right(10)

        timmy.color(randint(0, 255) / 255.0, randint(0, 255) / 255.0, randint(0, 255) / 255.0)



drunk_walking()
screen = Screen()
screen.exitonclick()
'''
"""

from turtle import Turtle, Screen
from random import randint, choice



def draw_spiral():
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.width(2)
    timmy.speed("fastest")


    colors = [(randint(0, 255) / 255.0, randint(0, 255) / 255.0, randint(0, 255) / 255.0) for _ in range(36)]

    count = 0
    while count < 36:

        timmy.color(randint(colors))  # Set a random color from the tuple
        timmy.circle(100)
        timmy.right(10)
        count += 1

    timmy.hideturtle()

def main():
    draw_spiral()

    screen = Screen()
    screen.exitonclick()

"""




"""


from turtle import Turtle, Screen
from random import randint, choice

def set_background_color():
    screen_color = (0, 1, 0)
    Screen.bgcolor(screen_color)

def draw_spiral():
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.width(5)
    timmy.speed("normal")

    colors = [(randint(0, 255) / 255.0, randint(0, 255) / 255.0, randint(0, 255) / 255.0) for _ in range(36)]

    count = 0
    while count < 36:
        color = choice(colors)
        timmy.color(color)
        timmy.circle(100)
        timmy.right(10)
        count += 1

    timmy.hideturtle()


def main():
    set_background_color()
    draw_spiral()
    screen = Screen()
    screen.exitonclick()

if __name__ == "__main__":
    main()
"""
from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
screen.listen()
# כדי לחבר (לקשור) בין לחיצת מקש לאירוע בקוד שלנו צריך להשתמש בevent
#צריך להשתמש בonkey
def move_forward():
    tim.forward(randit())
    #במקרה הזה כותבים את הפונקציה בלי סוגריים אחרי כי אין לה ארגומנטים (לא ממש הבנתי) הסבר נוסף בשורה הבאה
#רוצים שהפונקציה onkey  תפעל רק כאשר לוחצים מקש רווח , אם נשים סוגריים אחרי הפונקציה תפעל מיד

# screen.onkey(key="space" , fun=move_forward)
move_forward()
screen.exitonclick()
#איך משתמשים בפונקציות כאמצעי קלט לפוקציה אחרת , ז"א להשתמש בה כinput
# def fun(smsing):
    #do this
#ggg
    #העברת הפונקציה השניה לראשונה כאמצעי קלט
# def fun_b():
# fun(fun_b())

