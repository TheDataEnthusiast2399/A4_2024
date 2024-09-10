"""
A shallow copy is a copy of an object where the top-level elements are copied,
but any nested objects (like lists or dictionaries within the copied object) 
are not. Instead, the shallow copy references the original nested objects.
"""

"""
Deep copy (created using copy.deepcopy()) would fully duplicate the entire object, including all nested objects, 
so changes to any part of the copy would not affect the original.
"""
import copy

# Original list containing a nested list
my_list = [1, 2, [3, 4]]

# Shallow copy using slicing
shallow_copy = my_list[:]  # or copy.copy(my_list)

# Deep copy using copy.deepcopy()
deep_copy = copy.deepcopy(my_list)

# Print original, shallow, and deep copies before modifications
print(f"Original List: {my_list}")
print(f"Shallow Copy: {shallow_copy}")
print(f"Deep Copy: {deep_copy}")

# Modify top-level element in shallow and deep copies
shallow_copy[0] = 100
deep_copy[0] = 200

print("\nAfter modifying top-level element:")
print(f"Original List: {my_list}")
print(f"Shallow Copy: {shallow_copy}")
print(f"Deep Copy: {deep_copy}")

# Modify nested list in shallow and deep copies
shallow_copy[2][0] = 300  # Original list will get affected.
deep_copy[2][0] = 400  # Original list will not be affected.

print("\nAfter modifying nested element:")
print(f"Original List: {my_list}")
print(f"Shallow Copy: {shallow_copy}")
print(f"Deep Copy: {deep_copy}")
