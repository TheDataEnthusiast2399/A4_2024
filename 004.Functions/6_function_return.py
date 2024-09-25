# return () statement -->
"""
--> A return statement in python is used to end the execution of function call and returns
the desired value.
--> Any statements after return is not executed.
--> Cannot be used outside the function.
"""
# def fun():             Syntax
#     statements
#     .
#     .
#     return [expression]

# Q.1 ---> 5 int parameters | Marks of subject
# Return True if pass else False


def marks(
    s1: int, s2: int, s3: int, s4: int, s5: int
) -> bool:  # We can mention return type using annotations
    total = s1 + s2 + s3 + s4 + s5
    return total / 5 > 33


# With parameters and with return


def average(n1: int, n2: int, n3: int, n4: int) -> float:
    total = n1 + n2 + n3 + n4
    return total / 4


def add(n1, n2):
    total = n1 + n2
    return total


# x = add(100, 200)
# print(x)
print(add(10, 20))
