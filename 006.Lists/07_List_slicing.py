"""
List slicing is the process of accessing a specified portion or subset of a 
list for some action while leaving the rest of the list alone.

Syntax :
list[start: stop: step]

start -> indicates the starting index , default starts from zeroth index.
stop -> indicates the ending index / nth index , list slices upto n-1.
step -> parameter determining the jump of iterations, default is always 1 step.
"""

my_list = [43, 65, 12, 89, 67, 56, 49, 86, 111]
# Positive index slicing -->
# x = my_list[0:9]     # Slices list from index 0-8 / whole list
# x = my_list[3:]      # Slices list from index 3 to End of the list.
# x = my_list[:]       # Slices / returns whole list.
# x = my_list[::3]     # Slices from index 0 to 8 with jump 3, returns index 0, 3, 6.
# x = my_list[:4]      # Slices from index 0-3.
# print(x)

# Negative index slicing -->
# x = my_list[::-1]      # Slices from index 8 to 0 / returns reversed list.
# x = my_list[-3:-8:-1]  # Slices from index 6 to 2 in reversed manner.
# x = my_list[-6::-3]    # Slices from index 3 to 0 in reversed manner with jump of 3

# If there is any anomaly in indexes, list slicing will be empty.
# x = my_list[-1:-8:3]  # Negatives indexes with positive jumps is not possible.
# print(x)
