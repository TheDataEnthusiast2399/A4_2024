"""
a) Python's membership operators check if a value exists in a sequence, 
such as a list, string, tuple, or dictionary. 
b) The two membership operators are "in" and "not in":
---> in: Returns true if the item exists in the sequence.
---> not in: Returns true if the item does not exist in the sequence.
"""

# Membership - in / not in

my_list = [3, 6, 7, 5, 6, 6, 7, 8]

print(6 in my_list)  # Checks if element is available and returns boolean value.
print(5 not in my_list)  # Checks if element is not available and returns boolean value.


# Create a list with no duplicates
my_list2 = [1, 4, 5, 4, 4, 4, 3, 7, 8, 9, 9, 8, 9]

result = []

for num in my_list2:
    if num not in result:
        result.append(num)
    # if result.count(num) == 0: # Method 2 -> count() -> Counts occurrence of each elements.
    #     result.append(num)

print(result)
