# Args --> Spread | splat operator (*args) :
"""
--> In python args in function is used to pass n number of arguments one at a time.
--> It allows us to have more number of arguments than the predefined status in parameter
--> Always use *args at the last so python is not confused, we can iterate over the same.
"""


def add(n1, n2, *args):
    print(f"n1 -> {n1}")
    print(f"n2 -> {n2}")
    print(f"n3 -> {args}")  # Return type will be tuple


add(10, 20, 30, "ANirudh", True, 55.55)
add(10, 20, 6, 77, 55)
