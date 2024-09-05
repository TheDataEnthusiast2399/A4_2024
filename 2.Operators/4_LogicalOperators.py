# Logical Operators:
"""Logical operators are used to operate on two or more conditional statements:
AND -->	Returns True if both statements are true 
C1  C2  Result
F   F   F
F   T   F
T   F   F
T   T   T	

OR --> Returns True if one of the statements is true	
C1  C2  Result
F   F   F
F   T   T
T   F   T
T   T   T

NOT	--> Reverse the result
C1  Result
F    T
T    F
"""

physics = 43
chemistry = 21

print(physics > 33 and chemistry > 33)  # True and False --> False
print(physics > 33 or chemistry > 33)  # True or False  --> True
print(not (physics > 33 and chemistry > 33))  # Not(True and False) --> True
print(not physics > 33 and chemistry > 33)  # False and False --> False
