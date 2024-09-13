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
print(f"{a = }")
print(f"{b = }")
print(f"{c = }")
