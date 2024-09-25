"""
 a) Tuple is an immutable sequence of values. Tuples are similar to lists, but unlike 
 lists, tuples cannot be modified after they are created (i.e., they are immutable).
 b) Key Features : 
    1) Ordered
    2) Immutable
    3) Duplicates allowed
    4) Indexed
"""

my_tuple = (1, 2, 3)
print(my_tuple)
# print(type(my_tuple))

"""
Accessing elements in tuple :
a) Similar to lists , indexed from 0 to len(tuple) - 1.
b) We can use indexing or slicing to access elements in the tuple.
"""

my_tuple1 = (10, 20, 30, 40)

print(my_tuple1[0])  # Output: 1
print(my_tuple1[-1])  # Output: 3 (last element)


"""
Common Operations :

Concatenation: You can combine two tuples using the + operator.
Repetition: You can repeat the elements of a tuple using the * operator.
Membership: Check if an item exists in a tuple using the in operator.
"""
my_tuple2 = (10, "Jake Peralta", 22.45, True)
print(f"Original Tuple locId:{id(my_tuple2)}")

concat_res = my_tuple2 + (50, 60)
print(concat_res)  # Refers to new location, doesn't change original tuple
print(f"After concat operation Tuple locId: {id(concat_res)}")

repeat_res = my_tuple * 3
print(repeat_res)  # Refers to new location, doesn't change original tuple
print(f"After repeat operation Tuple locId: {id(repeat_res)}")

print(20 in my_tuple2)
