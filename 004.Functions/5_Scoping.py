# Scoping
"""
Scoping variables --->
a) Local Variable : A variable created inside a function belongs to the local scope 
of that function, and can only be used inside that function.

b)If you operate with the same variable name inside and outside of a function, 
Python will treat them as two separate variables, one available in the global scope 
(outside the function) and one available in the local scope (inside the function):

"""


def info():
    # Local Variables
    num1 = 100
    num2 = 200
    total = num1 + num2
    print(total)


info()
# print(num1)  num1 cannot be accessed outside the scope of info()

"""
Function inside Function --> Nested Function
"""


def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myfunc()  # Recursive call to the myfunc()


myfunc()
