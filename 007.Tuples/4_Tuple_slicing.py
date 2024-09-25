"""
Similar to lists , we can access the elements of tuple through slicing.
"""

my_tuple = (1, 2, 3, 5, "Anirudh", False, True, 3, 55.5)


print(my_tuple[0:4])  # Return the element from index 0 to 3
print(my_tuple[:])  # Return the whole tuple
print(my_tuple[::-1])  # Return the tuple in reverse
print(my_tuple[-2:-4:-1])  # Return the element from index 7 to 6 in reverse
