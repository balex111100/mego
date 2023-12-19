import img

print("Welcome to Master Chef!!!\n" + img.welcome)
age = int(input("enter your age>>> "))
if age < 18:
    print("Try in the future... or try Master Chef Junior\n" + img.junior)
elif age >= 18:
    experience = input("Do you have experience as a professional cook? y/n\n ")

    if experience == "y":
        print("Go to hell's kitchen\n" + img.hell)
    else:
        print("Welcome to the MasterChef auditions!\n")
        ready = input("Are you sure you are ready for the big challenge??? y/n ")
        if ready == "y":
            print("In order to be accepted to Master Chef, you must prepare your signature dish\n" + img.dish)
            signature_dish = input("What kind of dish do you want to make? vegetarian? y/n ")
            if signature_dish == "y":
                print("A serious mistake\n" + img.game_over)
            if signature_dish == "n":
                print("Excellent choice!\n" + img.thumb)
            signature_dish2 = (input("You only have 45 minutes to prepare the dish, Will you try baking? y/n "))
            if signature_dish2 == "y":
                print("Bad choice, not enough time" + img.game_over)
            else:
                print("Good choice! Well done" + img.thumb)
            signature_dish3 = int(
                input("What type of protein do you choose to use for the dish? Choose>>> 1.Meat 2.chicken 3.fish>>> "))
            if signature_dish3 == 1:
                print("good choice!!")
                signature_dish4 = int(
                    input("Which portion will you choose to make? 1.Tongue 2.Ribeye Steak  3.brisket "))
                if signature_dish4 == 2:
                    print("Excellent choice, now it remains to test your cooking skills")
                else:
                    print("bad choice. It takes 'forever' to cook" + img.game_over)
            if signature_dish3 == 2:
                print("Challenging but possible...")
            if signature_dish3 == 3:
                print("very delicate Protein , be careful not to spoil it.")


        elif ready == "n":
            print("Too bad... but don't stop cooking...\n")

'''
ccores = 0
for i in range (1,4):
    score = int(input())

'''
