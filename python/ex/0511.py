'''
Welcome to the cypher program

{logo}

Choose what would you like to do:
Encrypt (press 1)
decrypt (press 2)

---> 1
input -->"Hello"
OK, enter the offset >>>
input --> 2
Encrypted sentence: Jgnnq
Would you like to continue or quit? (C or Q)

--- 2
OK, enter the encrypted sentence >>> jgnnq
Enter the offset >>> -2
Decrypted sentence: Hello
Would you like to continue or quit? (C or Q)

# if the user chooses to quit, then the program exists. else, the screen will clear
and he will start over.


# find the ASCII value of a given character
# char = 'p'
# print("The ASCII value of " + char + " is ", ord(char))

# print(chr(97))

# additional requirement:
# if the user, for example, writes: 'zzz' and +1 then --> 'aaa'
# Same with upper-case letters!  (Z+1=A)

<END of Ceasar-Cypher Assignment>
'''


 # def add_func(a, b):
 #     return a * b
 #     print("bye")  # DEAD CODE :-(

# res = 3 +4 * 233 / 33  (compound expression --> process -> literal)
# add_func(2, 3)
# mult_result = add_func(2, 3)
# print(result)

# res = len("hi")
# def sayBy():
#     return
#
# print(sayBy)

# Write a function which gets a sentence from the user,  and converts it to
# title case (where each 1st letter is in upper-case
# e.g., hello sir  --> Hello Sir

# option 1:
# def upperTheSen(in_str):
#     return in_str.title()
#
#
# str = input("Enter something >>> ")
# res = upperTheSen(str)
#
# print(res)

# for Tuesday (before the lesson): The Calculator
'''
Hello, and welcome to the calculator!
{logo}
choose the first operand  --> 2
choose the second operand --> 3
choose the operator (+,-,*,/) --> *
The result of 2 * 3 is: 6  
* use print(f...)
* every operator must be coded into its own function
<END of Calculator program>
'''
"""
import img

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divaid(a,b):
    return a / b


print(img.cc + "Hello, and welcome to the calculator!")
a = float(input("Enter first number>>> "))
b = float(input("Enter second number>>> "))

choose = int(input("What math operation do you want?>>> choose: (1.add , 2. sub , 3.multiply , 4.div)"))
if choose == 1:
    print(f"the result is>>>  {add(a,b)}")
elif choose == 2:
    print(f"the result is {subtract(a,b)}")
elif choose == 3:
    print(f"the result is>>>  {multiply(a,b)}")
elif choose == 4:
    print(f"the result is {divaid(a,b)}")

"""
    # add=a + b
    # print(add)


# addition(x,y)

# scope

# local scope example
# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# def drink_potion():
#     potion_strenth = 1
#
# print(potion_strenth)
# drink_potion()

# global scope

# player_health = 10  # "global" variable
#
# def print_health():
#     print(player_health)

# player_health = 10
# def game():
#     def drink_potion():
#         potion_strenth = 2
#         print(player_health)
#
# drink_potion()

# block scope (not in Python!... )
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
# print(new_enemy)

# WILL THIS WORK?!

"""game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]  # local ONLY to the function
print(new_enemy)

"""
############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Best Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
"""
from turtle import Turtle, Screen
from random import randint

def drunk_walking(timmy, steps):
    for _ in range(steps):
        direction = randint(0, 3)  # 0: up, 1: down, 2: left, 3: right

        if direction == 0:
            timmy.setheading(90)  # up
        elif direction == 1:
            timmy.setheading(270)  # down
        elif direction == 2:
            timmy.setheading(180)  # left
        elif direction == 3:
            timmy.setheading(0)  # right

        distance = randint(10, 50)  # random distance
        timmy.forward(distance)
        timmy.color(random(), random(), random())  # random color

timmy = Turtle()
drunk_walking(timmy, 50)  # Adjust the number of steps as needed

screen = Screen()
screen.exitonclick()
"""
from turtle import Turtle, Screen
from random import randint

def drunk_walk(turtle, steps):
    for _ in range(steps):
        turtle.setheading(randint(0, 360))
        turtle.forward(randint(10, 50))
        turtle.color(randint(0, 255) / 255.0, randint(0, 255) / 255.0, randint(0, 255) / 255.0)

# יצירת צייר
timmy = Turtle()

# ביצוע הליכה שכורה עם 100 צעדים
drunk_walk(timmy, 100)

# הצגת הצייר
screen = Screen()
screen.exitonclick()