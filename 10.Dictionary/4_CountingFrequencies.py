my_list = [4, 5, 6, 4, 4, 3, 2, 3, 3, 10, 4, 8, 9, 9, 10]

my_dict1 = {}
my_dict2 = {}


for num in my_list:
    # Method 1 :
    if num in my_dict1:
        my_dict1[num] = my_dict1[num] + 1
    else:
        my_dict1[num] = 1

    # Method 2:
    my_dict2[num] = my_dict2.get(num, 0) + 1

print(my_dict1)
print(my_dict2)
