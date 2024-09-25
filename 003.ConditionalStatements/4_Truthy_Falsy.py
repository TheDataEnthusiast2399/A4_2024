# General values that are considered or treated as True or False
# Type casting (Implicit(Automatic) and Explicit(Mentioned))
"""
INT
1, 5, -9, 7, 100 -> Truthy
0 -> Falsy

FLOAT
1.1, 5.222, -9, 7, 100, 0.000002 -> Truthy
0.0 -> Falsy

STR
"abc", "123", " " "." -> Truthy
"" -> Falsy
"""
if 50 and 1:  # Implicit conversion takes place -> True and False --> False
    print("Yes")
else:
    print("No")
