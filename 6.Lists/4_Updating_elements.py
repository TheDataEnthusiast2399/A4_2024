my_list1 = [4, 5, 3, 1, 7, 6, 5, 9, 100]
print(my_list1)

# Method 1 : Direct update on particular index
my_list1[-1] = 200
my_list1[0] = 50
print(my_list1)

# Method 2 : Updating through iteration
my_list2 = [44, 25, 3, 1, 7, 6, 5, 9, 100]

n = len(my_list2)
for i in range(n):
    if my_list2[i] % 2 == 0:
        my_list2[i] = my_list2[i] + 1
    else:
        my_list2[i] = my_list2[i] - 1

print(my_list2)
