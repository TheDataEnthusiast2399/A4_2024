# Lists --->
"""
-> Lists are type of sequence data type.
-> List is a collection which is ordered and changeable. 
-> Allows duplicate members.
-> Lists are ordered and changeable.
"""
my_list1 = [1, 2, 3, 4, "Mike", True, 55.56]
print(my_list1)
print(type(my_list1))


# Some inbuilt functions for lists
my_list2 = [1, 2, 5, 65, 432, 654, 55.66]
# For homogenous datatype elements in a list
print(sum(my_list2))  # To find sum of all elements in a list.
print(max(my_list2))  # To find maximum element in a list.
print(min(my_list2))  # To find minimum element in a list.

# To find the length of list , we use len()
n = len(my_list2)
print(f"Length = {n}")

# Indexing of elements in a list

my_list3 = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]

# Index starts from 0 to 8 [left to right]
print(my_list3[2])  # >> fetches second index elements

# List also allows negative indexing starting from -l to -len[right to left]
print(my_list3[-3])  # >> fetches third last index elements


# To find particular element at any index, we just pass index inside square brackets
print(my_list3[7])  # Positive index -> fetches last element
print(my_list3[-1])  # Negative index -> fetches last element
print(my_list3[n - 1])  # Generalised form to fetch last element
