"""Elif statements are basically for more than one conditon check, it's basically justifies:
'if the previous conditions were not true, then try this condition'
"""

marks = int(input("Enter the marks: "))

if marks >= 91 and marks <= 100:  # First If Block
    print("A")
elif marks >= 81 and marks <= 90:  # First Elif Block
    print("B")
elif marks >= 71 and marks <= 80:  # Second Elif Block
    print("C")
elif marks >= 61 and marks <= 70:  # Third Elif Block
    print("D")
elif marks >= 0 and marks <= 60:  # Fourth Elif Block
    print("Fail")
else:  # First Else Block
    print("Invalid Marks entered")

"""Flow of execution is such whenever condition is satisfied the execution is stopped 
and doesn't check for any further conditions.
"""
