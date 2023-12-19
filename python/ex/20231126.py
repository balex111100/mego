# parrot = "Norwegian"
#
# print(parrot[:3] + parrot[5:])
# print(parrot[:])

# letters = "abcdefghijklmnopqrstuvwxyz"
# x = parrot[99]
# print(x)
# print(parrot[-4:2])
# print(parrot[-4:-2])  # gi
# print(parrot[-4:12])
# parrot = "Norwegian"
# print(parrot[-14:-8])

# parrot = "Norwegian Blue"
# print(parrot[0:6:2])  # Nre
# print(parrot[0:6:3])  # Nw
# print(parrot[6:0:-2]) # ier

# number = "9,223,372,036,854,775,807"
# print(number[1::4])
# number = "9,223;372:036 854,775;807"
# separators = number[1::4]
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])
 # list comprehension

# letters = "abcdefghijklmnopqrstuvwxyz"
# backwards = letters[::-1]
# print(backwards)
# idiom

# String Formatting (uses string replacement fields)
# {} - string interpolation
# for i in range(1, 13):
#     print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3))

# noam = "guide in migo"
#
# print(noam[-1:8:4])
# import string
# plain_text = "hello world"
# shift = 1
# alphabet = string.ascii_lowercase
# shifted = alphabet[shift:] + alphabet[:shift]
# table = str.maketrans(alphabet , shifted)
# encrypted = plain_text.translate(table)
#
# print(encrypted)
def encrypt(text, s):
    result = ""


# transverse the plain text
for i in range(len(text)):
    char = text[i]
    # Encrypt uppercase characters in plain text

    if (char.isupper()):
        result += chr((ord(char) + s - 65) % 26 + 65)
    # Encrypt lowercase characters in plain text
    else:
        result += chr((ord(char) + s - 97) % 26 + 97)
    return result
# check the above function
text = "CEASER CIPHER DEMO"
s = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text, s))


