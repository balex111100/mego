# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculeta(self):
#         return radius**2 * math.pi
# radius = float(input("enter teh circle radios:"))
# callable(radius)
"""
class Song:
    def __init__(self, title , artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

# Getters and Setters

    def get_title(self):    # geter
        return self.title

    name = property(get_title)

s = Song("Menny M." ,  "Menny")
print(s.name)
"""

"""
class Player(object):
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self.level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, level: {0.level}, Score: {0.score}".format(self)
"""


class User:
    activ_users = 0

    @classmethod
    def display_activ_users(cls):
        return f"Ther are currently {cls.activ_users} activ users"

    @classmethod
    def from_string(cls, date_str):
        first, last, age = date_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.activ_users += 1

    def logout(self):
        User.activ_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.firset} {self.last}"

    def initials(self):
        return f"{self.firset[0]} . {self.last[0]}"

    def likes(self, thing):
        return f"{self.firset} likes {thing}"

    def is_senior(self):
        return self.age <= 65

    def birthday(self):
        self.age += 1
        return f"happy {self.firset}, {self.last}"

    def __repr__(self):
        return f"{self.firset} {self.last} is {self.age}"

    # def __str__(self):
    #     return f"who am i?"


tom = User.from_string("Tom,Jones,89")
tom = 
# print(tom)
j = User("Johan" , "sttele" , 18)
# print(j)

j = str(j)
print(j)
