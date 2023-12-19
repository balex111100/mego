# a = 3
# b = 6
# print(a.__add__(b))
# class Kettle(object):
#     def __init__(self, make, price):
#         self.make = make
#         self.price = price
#         self.on = False



#
# kenwood = Kettle("Kenwood", 8.99)
# # print(kenwood.make)
# # print(kenwood.price)
# kenwood.price = 12.75
# # print(kenwood.price)
# hemilton = Kettle("Hamilton", 14.55)
# # print(hemilton.on)
# # print(hemilton.make)
# # print(hemilton.price)
# hemilton.price = 14.99
# print("Models: {0.make} = {0.price} , {1.make} = {1.price}".format(kenwood, hemilton))
# # print(type(kenwood))
class Kettle(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

hemilton = Kettle("Hamilton", 14.55)
# print(hemilton.on)
hemilton.switch_on()
# print(hemilton.on)
hemilton.power = 1.5
print(hemilton.power)
