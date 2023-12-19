# raise ValueError("invalid value")
# # throw an error
# print("hi")


def colorize(text, color):
    if type(text) is not str:
        raise TypeError("Text must be a string. (don't be an invalid)")
    else:
        print(f"Printed {text} in {color}")


colorize("3", "red")


# exception handling
# try-except blooks

try:
    foobar
except NameError as err:
    print("problem")