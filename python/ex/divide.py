def divide(a, b):
    try:
        # return a / b
    # except ZeroDivisionError:
    #     print("Don't divide by 0 pleaseeee!!!!")
    #     print("Something went wrong...")
    # except TypeError as err:
    #     print("a and b must both be either ints or floats!")
    #     print(err)
        result = a / b
    except (ZeroDivisionError, TypeError) as err:
        print("Something is wrong, let me explain: ")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

# print(divide(1, 2))  # 0.5
# print(divide(1, 0))  # will print None because we returned None (skipped Ln3)
# print(divide('a', 2))
divide('a', 0)
