"""
class Grade:
    def __init__(self):
        self.math = 0
        self.english = 0
        self.hebrew = 0
        print(f"init{i}")

    def input_grades(self, i):
        print(f"input grade for student {i}:")
        self.math = int(input("input math grade>>> "))
        self.english = int(input("input english grade>>> "))
        self.hebrew = int(input("input hebrew grade>>> "))

    def find_average(self):
        return (self.math + self.hebrew + self.english) / 3


object_list = []
for i in range(1, 5):
    grade = Grade(i)
    grade.input_grades(i)
    object_list.append(grade)
max_of_grade = object_list[0].find_average()
for item in object_list:
    if item.find_average() > max_of_grade:
        max_of_grade = item.find_average()
print(max_of_grade)

"""

# print("open the box")
# a = 1 , 2 ,3
# d,b,f = a
# print(d)
# print(b)
# print(f)
for t in enumerate("abcdefg"):
    index , char =t
    print(index,char)

