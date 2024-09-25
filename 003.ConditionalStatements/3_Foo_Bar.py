""" FOOBAR problem
Ask a number from user.
num is divisible by 3 -> FOO
num is divisible by 5 -> BAR
num is divisible by 3 and 5 -> FOOBAR
else
-> Invalid
"""

num1 = int(input("Enter the number: "))
if num1 % 3 == 0 and num1 % 5 == 0:  # Condition to Handle multiple of both 3 and 5
    print("FOOBAR")
elif num1 % 3 == 0:  # Condition to handle mulitple of 3
    print("FOO")
elif num1 % 5 == 0:  # Condition to handle mulitple of 5
    print("BAR")
else:
    print("INVALID")
