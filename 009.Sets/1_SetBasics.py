"""
Set is an unordered collection of unique elements.

Key Features of Sets:

Unordered: Elements in a set are not stored in any specific order.
Unique: Sets do not allow duplicate values.
Mutable: Sets can be changed (you can add or remove items).
Unindexed: You cannot access items in a set using an index, unlike lists or tuples.

"""

my_set = {1, 2, 3, 3, 3, 3, 3, 4, "Michael", 99.9988, 6, 7, 7, 7, 1}
print(my_set)
print(type(my_set))

"""Iteration is possible in sets only through values , iteration through indexes is 
not possible in sets."""

set1 = {76, 43, 19, 83, 41, 33, 33, 33, 33}

print(set1)

# Iteration by value :
for num in set1:
    print(num)

"""Sets are not hashable as they are mutable in nature, however frozensets are
hashable."""

"""
Operations in sets :

"""
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7, 8}

# Union : Returns a new set containing all unique elements from both sets.
# result = set1 | set2
# print(f"The union of two sets is : {result}")

# Difference : Returns a set containing elements that are in the first set but not in the second.
# result = set1 - set2
# print(f"The difference of two sets is : {result}")

# Intersection: Returns a set of elements that are common to both sets.
# result = set1 & set2
# print(f"The difference of two sets is : {result}")

# Symmetric Difference : Returns a set containing elements that are in either of the sets, but not in both.
result = set1 ^ set2
print(f"The symmetric difference of two sets are : {result}")
