from typing import List

# List Methods (Functions)
# my_list: list[int] = [52, 74, 89, 8, 74, 5, 4, 233] # Datatype list
my_list: List[int | str | float | bool] = [52, 233, "Anirudh", 77.67, True, False]
print(f"Original List : {my_list}")
"""Defined in typing module with expected datatype as 
list for type hints and code readability"""
# Adding elements in list -->
# insert() -> inserts element to the mentioned index, with original elements being pushed to right.
# my_list.insert(-1, 100) # Inserts element to the last index (already present last element gets pushed to right).
# my_list.insert(0, 100)  # Inserts element to zero index.
# my_list.insert(50, 100) # Inserts element to the last position.
# my_list.insert(-2, 100) # Inserts element to the second last position (already present last element gets pushed to right).

# Removing elements in list -->
# x = my_list.pop()       # Delete element by index
# del my_list[3]          # Delete element by index
# my_list.remove(77.67)   # Delete by value, if present
my_list.clear()  # Clears/empty lists.
print(f"After using methods: {my_list}")
