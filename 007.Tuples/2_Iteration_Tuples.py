"""
Similar to lists we can traverse the contents of tuple by indexes or values.
"""

my_tuple1 = (23, 32, 12, 90.4, "Raymond Holt", False)

# Iteration by index
for i in range(len(my_tuple1)):
    print(my_tuple1[i], end=" ")
print()
# Iteration by value
for ele in my_tuple1:
    print(ele, end=" ")
