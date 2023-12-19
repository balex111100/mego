# with open("C:\\Users\\Baruch\\OneDrive\\שולחן העבודה\\MeGo\\python\\pythonProject\\contact_list.txt", mode="r+") as file:
#     contents = file.read()
#     print(contents)
#     file.write("33")
#     print(contents)
# #

# try:
#     foobar
# except NameError as err:
#     print("problem")
# print("after the 'try'... ")
#  d = {"name": "bob"}
#  d["city"]
#  get(d, "city")
#  def get(d , key):
#      try:
#          return d[key]
#      except KeyError:
#          return None
#      get(d , "city")

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("plise dount ddo thet...")
    except TypeError as err:
        print("agein??")
        print(err)


print(div(1, 2))
print(div(1, 0))
print('a', 2)
print("bye")
