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


class Player(object):
    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.level = 1
        self.score = 0

    def _get_lives(self, lives):
        self._lives = lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("lives cannot be negative")
            self._lives = 0
        # self._lives = lives

    lives = property(_get_lives, _set_lives)
