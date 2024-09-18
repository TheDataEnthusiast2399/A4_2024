"""
Similar to lists and tuples , we can have concatenation, repitition and membership
operation in python.
"""

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(f"After concatenation : {result}")  # Points different memory loc.

str3 = "Waku "
print(f"After repetition : {str3 * 3}")  # Points different memory loc.


str4 = "Leonard is my best friend"
print("best friend" in str4)  # Boolean value.


s = "A"
s = s * 5  # Operation 1 stored in s
b = s * 5  # Operation 2 stored in b
print(s, id(s))
print(b, id(b))
