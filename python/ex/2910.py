# positional arguments - examples and problems

# def say_hello(name, age):
#     print(f"Hello {name}, you are {age} years old.")


# x = input("Say your name: ")
# y = input("Say your age: ")

# say_hello(y, x)


# keyword-arguments - examples and problems
# def func(a, b, c):
#     print(a)
# ex.
# func(2,1,3) #2
# func(b=2, a=1, c=3)#1

# conditions for using both positional-args. and keyword-args. combined:
# a. first use pos., and only then - keyword
# b. no duplicates are allowed
# ex. func(3,2,c=1)

# Exercise: Write a func. which gets a number from the user and prints whether it's a prime.

# def prime_check(num):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#
#     if not is_prime:
#         print(f"{num} is not a prime number")
#     else:
#         print(f"{num} is a prime number")

# num = int(input("Enter a number: "))
# prime_check(num)

# hangman - game flow
'''
0. The words will exist inside a list/dictionary the programmer will create. (at least 5 words)
1. Only 1 human player
a. The user is given number of underscores (_) -> same as the word length (e.g., "egg" = _ _ _)
b. There will be "pictures" (at least 3: logo, human parts, ending) -> in another module (file)
c. when the user loses the game, the program says he lost, and tells him what was the correct word.
d. if the user enters a correct letter, then the relevant underscore will be replaced with that letter.
e. if the same letter exists more than once, then the user will have to put it again.
F. USE ONLY COMMANDS/FUNCTIONS WE LEARNED IN CLASS
'''

student_scores = {"avi": "100", "haim": "75", "yossi": "70", "tal": "60", "eyal": "85"}

student_grades = {}
for score in student_scores:
    if int(student_scores[score]) >= 90:
        student_grades[score] = "amazing"
    elif int(student_scores[score]) >= 80:
        student_grades[score] = "beyond expectations"
    elif int(student_scores[score]) >= 70:
        student_grades[score] = "More is possible"
    else:
        student_grades[score] = "you failed"
    print(f" {score} {student_grades[score]}")

# Dictionaries
# "code": "programming instructions"
# {key: value}
# programming_dictionary = {"Bug": "An error in the program that prevents the program from "
#                                  "running as expected",
#                           "Function": "A piece of code that you can re-use",
#                           }
# retrieving items from a dict.
# print(programming_dictionary["Bug"])

# adding elements to an existing dict.
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary["Loop"])

# my_dict = {}
# my_dict["Car"] = "An automobile"
# print(my_dict["Car"])

# deleting a dict.
# my_dict = {}

# overwriting an existing item
# my_dict["Car"] = "A vehicle"
# print(my_dict["Car"])

# printing ONLY the keys
# for item in programming_dictionary:
#     print(item)

# printing the values of a given dict.?
# for key in programming_dictionary:
#     print(programming_dictionary[key])

# exercise
