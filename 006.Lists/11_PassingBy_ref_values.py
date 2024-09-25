def modify_list(lst):
    lst.append(4)  # Modifying the passed list


my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
"""

Mutable objects (like lists | sets | dictionaries):

They can be modified in place. This gives the impression that they are passed by 
reference because changes to the object within a function will reflect outside 
the function.

"""


def modify_string(s):
    s = s + " world"  # Attempt to modify the string


my_string = "hello"
modify_string(my_string)
print(my_string)  # Output: "hello"

"""
Immutable objects (like strings, tuples, and numbers):

They cannot be modified in place. When you attempt to change the object, Python 
creates a new object and assigns it to the variable, leaving the original 
object unchanged.
"""

"""
However, in both cases, Python actually passes a reference to the object, and what 
happens depends on whether the object is mutable or immutable.
"""
