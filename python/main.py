'''
# nested if/else statements - משפטי תנאי מקוננים

if condition:              # בדיקה האם המשתמש מעל גיל 13
    if another condition:  # בדיקה האם הילד מעל גובה 120ס"מ
        do this            # נכנס לרכבת הרים המפחידה
    else:
        do that            # הוא מעל 13 אבל מתחת ל 120, אז תלך למכוניות המתנגשות
else:
    do something else      # לך לבריכת הכדורים לילדים

age = float(input("Enter your age >>> "))
if age > 13:
    height = float(input("Enter your height (in CM) >>> "))
    if height > 120:
        print("Enter the Anaconda")
    else:
        print("Enter the crazy cars")
else:
    print("Go back to your mom")


# elif   => else if
if condition1:
    do A
elif condition2:
    do B
else:
    do C


if cond1:
    do A
elif cond2:
    do B
else:
    do C

if cond1:
    do A
if cond2:
    do B
if cond3:
    do C

casefold()  # עובדת על מחרוזות

txt = "Hello, AND welcome to my luna park!"
x = txt.casefold()
print(x)

photo = input("Do you want your photo taken? yes/no")
YEssss@!!!!

'''