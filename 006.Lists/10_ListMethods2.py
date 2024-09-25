from typing import List

# List Methods (Functions)
my_list: List = [5, 6, 7, 4, 4, 4, 6, 6, 7]
print(f"Original List:{my_list}")

# append()-> Adds to end of the original list as a single element whether single element or another list of elements
# my_list.append(100)
# my_list.append([1])
# my_list.append([5, 6, 7])

# extend() -> Adds all the elements of an iterable to the original list.
# my_list.extend([1, 2, 3])
# my_list.extend([4, 5, 6])

# count() -> counts the occurence of the mentioned element
# print(my_list.count(4))

# index() -> returns index of the mentioned element, if present
# print(my_list.index(99))

# sort() -> sorts element in ascending order by default
# my_list.sort() # reverse = True sets the list to be sorted in descending order.

# reverse() -> reverse the original list
# my_list.reverse()

print(f"After using methods:{my_list}")
