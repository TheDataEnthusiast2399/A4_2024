"""Type check are basically the way to determine the data-type of the variable during 
runtime .
"""

a = 56

if type(a) == int:  # Method 1 using type()
    print("Yes")
else:
    print("No")

if isinstance(a, int):
    # Method 2 using isinstance() ---> checks if the object (first argument) is
    # the instance of the subclass (second argument)
    print("Yes")
else:
    print("No")
