"""
--> A function is a block of code that is used to acheive some task
--> Repeats itself whenever called 
--> We can pass parameters and return any data from function.
--> To define any function we need to use def keyword in python.
--> Function name follows same rules as naming variables.
--> DRY :- Don't Repeat Yourself ; The aim is to reduce code redundancy and acheive certain set of 
task . Hence as a practice , every function should be maintained in such as way that it is defined
to perform unique set of operations and are called at the end."""


def my_func():  # Defining first function
    print("First function block")  # Set of operations
    print("First function ends")


def my_func2():  # Defining second function
    print("Second function block")  # Set of operations
    print("Second function ends")


# Function calls
my_func()
my_func2()


# Function named average; 3 num from user -> calculate average


def avg():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num1: "))
    num3 = int(input("Enter num1: "))

    total = num1 + num2 + num3
    print("Average is :", total / 3)


avg()
