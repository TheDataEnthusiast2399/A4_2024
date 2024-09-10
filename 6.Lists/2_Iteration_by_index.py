# Iterating over a list
# A) Iteration over index -->
my_list4 = [23, 45, "jack sparrow", 56]
n = len(my_list4)
# Iterating over list by index
for i in range(0, n):  # Elements from 0 to len
    print(my_list4[i], end=" ")
print()
for i in range(n - 1, -1, -1):  # Elements from len to 0
    print(my_list4[i], end=" ")
