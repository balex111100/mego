'''
ENCAPSULATION - הכמסה
'''

# a = 12
# b = 4
# print(a + b)
# print(a.__add__(b))


# class Kettle(object):
#     def __init__(self, make, price):
#         self.make = make
#         self.price = price
#         self.on = False
#
#
# kenwood = Kettle("Kenwood", 8.99)
# print(kenwood.make)
# print(kenwood.price)

# kenwood.price = 12.75
# print(kenwood.price)

# hamilton = Kettle("Hamilton", 14.55)
# print(hamilton.on)

# data attributes/members / fields
# {} => (string) placeholders (for data interpolation purposes)
# notation
# . => dot object notation (object access)
# print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
# print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

'''
class => template for creating objects. all objects which are created from the same class,
will have the same characteristics.

Object => An instance of the class.

(to) instantiate => create an instance of the class (==object)

Method => A function defined in the class

Attribute => a variable bound to an instance of a class 
'''


# class Kettle(object):
#     def __init__(self, make, price):
#         self.make = make
#         self.price = price
#         self.on = False
#         self.power_source = "electricity"
    #
    # def switch_on(self):
    #     self.on = True
#
#
# hamilton = Kettle("Hamilton", 14.55)
# kenwood = Kettle("Kenwood", 23)
# print(hamilton.on)
# hamilton.switch_on()
# print(hamilton.on)
#
# power
# hamilton.power = 1.5  # instance variable (not a class variable/member)
# print(hamilton.power)

#print(kenwood.power)

# s = 2  # local variable

# print(vars(hamilton))
# subclassing
# power_source = "electricity"
# print(hamilton.power_source)

# namespaces
# print(Kettle.__dict__)
# print(hamilton.__dict__)

import datetime
import pytz

class Account:
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    ''' Simple account class with balance '''
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self.transaction_list.append((Account._current_time(), amount))
    def withdraw(self, amount):
        if self.balance >= amount:  # to avoid being a millionaire...
            self.balance -= amount
            # self.transaction_list.append((self._current_time(), -amount))אפשר גם ככה, אבל לא כדאי כי זה יקח לפייתון הרבה זמן למצוא את האובייקט
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be <= than the current balance, which is: {}".format(self.balance))

    def show_balance(self):
        print("Balance is: {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


chaim = Account("Chaim", 0)
chaim.deposit(100)
chaim.withdraw(200)
chaim.show_transactions()
chaim.show_balance()

shmuel = Account("Shmuel", 800)
shmuel.deposit(100)
shmuel.withdraw(200)
shmuel.show_transactions()
shmuel.balance = 800
shmuel.show_balance()
