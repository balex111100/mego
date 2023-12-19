# Shadowing
# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# DON'T shadow if you can... or else...

# enemies = 1
#
# def increase_enemies():
#     enemies = 1 # sol.
    # enemies += 2 # enemies = enemies + 2
    # print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()


# enemies = 1

# def increase_enemies():
#     global enemies # listen to me... it's the same! don't be fooled!
#     global enemies += 2 # enemies = enemies + 2
    # enemies += 2
    # print(f"enemies inside function: {enemies}")


# increase_enemies()
# AVOID GLOBALS WHENEVER POSSIBLE!

# try: make the function call to inc. enemies by 2
# sol:
# enemies = 1
# def increase_enemies():
#     return enemies + 2
#
# enemies = increase_enemies()
# print(f"enemies outside func.: {enemies}")

# guessing game
'''
Welcome to the guessing game!
I'm thinking of a number between 1-100
choose difficulty: type 'easy' or 'hard'

---> hard
You have 5 attempts remaining to guess the game
--> guess > number --> "too high. guess again"
--> guess < number --> "too low. guess again"
--> guess is the number --> "Yes!"

--> every mistake? "you have 4 tries...3 2 1   game over you lose
the number was: ...

---> easy --> 10 tries

NOTES
* must use constants (file "globals")
* don't use shadowing
* use the return command in a correct way
* must document every function you write
* must use functions
* must use graphics
* must divide and conquer (use modules)
* date of submission: not later than 08.11 (0100 am)
* link to a working OnlineGDB code
'''
# בפייתון, מילונים הם מבני נתונים שמאפשרים לך לאחסן זוגות מפתח-ערך. הנה סיכום קצר של כל הפקודות הקשורות למילונים בפייתון:
#
# clear(): מוחק את כל הזוגות מהמילון.
# copy(): מחזיר עותק של המילון.
# fromkeys(): מחזיר מילון חדש עם מפתחות מסוימים וערכים נתונים.
# get(): מחזיר את הערך המתאים למפתח הנתון. אם המפתח לא נמצא, מחזיר את הערך המוגדר כברירת מחדל.
# items(): מחזיר רשימה של זוגות מפתח-ערך.
# keys(): מחזיר רשימה של כל המפתחות במילון.
# pop(): מוחק את הזוג מפתח-ערך המתאים למפתח הנתון ומחזיר את הערך המתאים למפתח הנתון.
# popitem(): מוחק את הזוג מפתח-ערך האחרון שהוכנס למילון ומחזיר את הזוג מפתח-ערך המתאים.
# setdefault(): מחזיר את הערך המתאים למפתח הנתון. אם המפתח לא נמצא, מכניס את המפתח והערך המוגדר כברירת מחדל למילון.
# update(): מעדכן את המילון עם זוגות מפתח-ערך חדשים.
# כדי לקצר את הפקודות, ניתן להשתמש בפקודות הקצרות הבאות:
#
# {}: מייצר מילון ריק.
# {key1: value1, key2: value2, ...}: מייצר מילון עם הזוגות מפתח-ערך הנתונים.בפייתון, מילונים הם מבני נתונים שמאפשרים לך לאחסן זוגות מפתח-ערך. הנה סיכום קצר של כל הפקודות הקשורות למילונים בפייתון:
#
# clear(): מוחק את כל הזוגות מהמילון.
# copy(): מחזיר עותק של המילון.
# fromkeys(): מחזיר מילון חדש עם מפתחות מסוימים וערכים נתונים.
# get(): מחזיר את הערך המתאים למפתח הנתון. אם המפתח לא נמצא, מחזיר את הערך המוגדר כברירת מחדל.
# items(): מחזיר רשימה של זוגות מפתח-ערך.
# keys(): מחזיר רשימה של כל המפתחות במילון.
# pop(): מוחק את הזוג מפתח-ערך המתאים למפתח הנתון ומחזיר את הערך המתאים למפתח הנתון.
# popitem(): מוחק את הזוג מפתח-ערך האחרון שהוכנס למילון ומחזיר את הזוג מפתח-ערך המתאים.
# setdefault(): מחזיר את הערך המתאים למפתח הנתון. אם המפתח לא נמצא, מכניס את המפתח והערך המוגדר כברירת מחדל למילון.
# update(): מעדכן את המילון עם זוגות מפתח-ערך חדשים.
# כדי לקצר את הפקודות, ניתן להשתמש בפקודות הקצרות הבאות:
#
# {}: מייצר מילון ריק.
# {key1: value1, key2: value2, ...}: מייצר מילון עם הזוגות מפתח-ערך הנתונים.