"""
a) Tuples in python are hashable in nature, that means object has a fixed hash for 
its lifetime and can be used as a key in dictionaries / sets.

b) Mutable types like lists and dictionaries are not hashable because their contents 
can change, which would affect their hash value.
"""

# Tuple with immutable elements (hashable)
t1 = (1, "apple", 3.14)
print(hash(t1))  # This will work because all elements are hashable

# Tuple with mutable elements (unhashable)
t2 = (1, [2, 3], "banana")  # Contains a list (mutable), so this will fail
print(hash(t2))  # TypeError: unhashable type: 'list'

"""
Tuples in Python have a few built-in methods since they are simple immutable collections. The most commonly used tuple methods are:

1. count() --> counts the occurrence of mentioned element, default zero if none found
2. index() --> return the index of the first occurrence of a specified element in a 
tuple, raises value error if not in tuple.
"""
my_tuple = (1, 2, 2, 3, 2, 4)
print(my_tuple.count(2))
print(my_tuple.index(4))
