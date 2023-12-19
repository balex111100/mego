# tuples are immutable
# my_tuple = (1, 2, 3)
# t = ('one', 2)

# print(type(t))
# print(t[-1])
# t = ('a', 'b', 'a', 'd')
# print(t.count('a'))
# print(t.index('a'))

# Unpacking a Tuple
# a = b = c= d = e = f = 12 # shorthand assignment
# c = 22
# print(d)
#
# a = "srer"
# b = a
# a = "sss"
# print(b)

# x, y, z = 1, 2, 76
# print(x)
# print(y)
# print(z)

# print("Unpacking a tuple")
# data = 1, 2, 76  # data represents a tuple
# print(type(data))
# x, y, z = data
# print(x)
# print(y)
# print(z)

# tuples are immutable

# print("Unpacking a list")
# data_list = [12, 13, 14]
# data_list.append(15)  # NO NO!!!
# p, q, r = data_list
# print(q)
# print(p)
# print(r)


# for i in "abfffd":
#     print(i)

# enumeration
# for index, character in enumerate("abcdefgh"):  # also unpacks the tuple
#     print(index, character)

# names = ["Alice", "Bob", "Charlie"]
# for index, name in enumerate(names):
#     print(f"{index + 1}. {name}")  # the tuples were unpacked

# for tutian in enumerate("abcdefgh"):
#     print(tutian)  # will show us tuples

for t in enumerate("abcdefgh"):
    index, character = t  # unpacking the tuple...
    print(index, character)
