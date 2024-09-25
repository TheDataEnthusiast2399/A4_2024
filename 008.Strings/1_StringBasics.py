"""
a) Strings are sequences of characters enclosed in either single quotes (' ') 
or double quotes (" "). 
b) Strings are immutable, meaning their content cannot be changed after 
they are created.
"""

"Single or double quotes"
str1 = "Hello"
str2 = "World"
print(str1, str2)

"Immutable data type"
str3 = "Amy Santiago"

# str3[0] = "z"  # Not allowed
print(str3)

"""Accessing characters of string:
String characters can be accessed through indexing or slicing 
"""
x = "This is Python strings."

print(x[3])
print(x[2:5])

"""
Iteration of strings :
Strings can be iterated through indexing or values.
"""
s = "Nanami Kento was the coolest character in JJK."
n = len(s)

# By Index
for index in range(0, n):
    print(s[index], end="")
print()

# By value
for ch in s[::-1]:  # Printing characters in reverse.
    print(ch, end="")
