"""
a) Unpacking in Python allows you to assign the elements of a tuple 
(or any iterable like a list) directly to variables. 

b This is a convenient way to extract multiple values at once.
"""

# Basic unpacking -->
my_tuple = (1, 2, 3)
a, b, c = my_tuple

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Unpacking with * (Extended Iterable Unpacking):
a, *b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"{a = }")  # a will hold first element
print(f"{b = }")  # b will hold middle elements upto second last
print(f"{c = }")  # c will hold last element

# Unpacking with Functions:
"""You can unpack arguments when passing them to a function using * for
tuples/lists and ** for dictionaries."""


def my_function(x, y, *z):
    print(f"x : {x}")
    print(f"y : {y}")
    print(f"z : {z}")


# Tuple unpacking
my_tuple = (1, 2, 3, 5)
my_function(*my_tuple)  # Output: 1 2 3
