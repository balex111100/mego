# כתוב מחלקה שמחשבת שכר של עובד.
# יש למחלקה 4 משתנים
# 1  שכר שעתי
# 2.  כמה שעות עבד בפועל
# 3. שעות נוספות (150%)
# 4. תעודת זהות
#
# פונקציה שמדפיסה כמה את המשתנים
# פונקציה שמחזירה את המשכורת.
#
# תיצור 5 עובדים ותמצא את העובד שמרוויח הכי הרבה
class Salary:
    def __init__(self,h = 0,a =0, o = 0, i = 0):
        print("constaractor")
        self.hourly_wage = h
        self.actual_hours = a
        self.overtime = o
        self.id = i


    def employees_name(self, i):
        print(f"enter the first name {i}>>> ")
        self.hourly_wage = int(input("enter the hourly wage>>> "))
        self.actual_hours = int(input("Enter the number of hours the employee actually worked>>> "))
        self.Overtime = int(input("Include overtime as well>>> "))
        self.id = int(input("enter id >>> "))

    def actual_salary(self):
        return (self.hourly_wage * self.actual_hours + (self.overtime * self.hourly_wage * 1.5))


print(s1.id)
#
# list = []
#
# for i in range(1, 5):
#     salary = Salary()
#     salary.employees_name(i)
#     list.append(salary)
#
# max_salary = list[0].actual_salary()
# for item in list:
#     if item.actual_salary() > max_salary:
#         max_salary = item.actual_salary()
# print(max_salary)
# parrot = "Norwegian Blue"
# print(parrot[0:10:2])

# number = "9,223,372,036,854,775,807"
# print(number[1::4])
# number = "9,223;372:036 854,775;807"
# separators  = number[1::4]
# # print(number[1::4])
# values = "".join(char if char not in separators else "  " for char in number).split()
# print([int(val) for val in values])
# letters = "abcdefghigklmnopqrstuvwxyz"
# letters_2 = "defghijklmnopqrstuvwxyzabc"
# cipher = letters[::1]
# cipher_2 = letters_2[::1]
# print(cipher)
# print(cipher_2)

# def add(a,b):
#     return a+b
# add(1)
# for i in range(1 , 13):
#     print("No , {0:2} squerd is {1:<3} and cubed is {2:^4}" .format(i , i**2 , i**3))
