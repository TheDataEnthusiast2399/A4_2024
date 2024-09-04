"""
Id() function is a built-in function that returns unique identifier of an object.
This identity has to be unique and constant for this object during its lifetime. 
Two objects with non-overlapping lifetimes may have the same id() value. 
"""

x = 42
y = x
z = 42

print(id(x))
print(id(y))  # (same as x)
print(id(z))  # (same as x and y)
