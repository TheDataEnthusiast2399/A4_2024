set1 = {76, 43, 19, 83, 41, 33, 33, 33, 33}
print(set1)

# add() -> adds the elements to existing set.
set1.add(100)
print(set1)

# remove() -> removes the element from existing set.
set1.remove(43)
print(set1)

# copy() -> creates a shallow copy of that set.
another_set = set1.copy()
another_set.add(1000)

print(set1)
print(another_set)

# clear() -> clears the content of that set.
set1.clear()
print(set1)
