# Print sum of all number in a list

my_list1 = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]

total_by_index = 0
# Iteration by index
n = len(my_list1)
for i in range(0, n):
    total_by_index = total_by_index + my_list1[i]
print(f"Sum of all numbers :{total_by_index}")

# Iteration by value
total_by_value = 0
for i in my_list1:
    total_by_value = total_by_value + i
print(f"Sum of all numbers : {total_by_value}")

# Print sum of all even number from a list

my_list = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]
n = len(my_list)
total_by_index = 0

# Iteration by Index
for index in range(0, n):
    if my_list[index] % 2 == 0:
        total_by_index = total_by_index + my_list[index]
print(f"Sum of all even numbers: {total_by_index}")

# Iteration by value
total_by_value = 0
for num in my_list:
    if num % 2 == 0:
        total_by_value = total_by_value + num
print(f"Sum of all even numbers :{total_by_value}")


# Print sum of all odd numbers from a list
my_list = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]
n = len(my_list)
total_by_index = 0

# Iteration by index
for index in range(0, n):
    if my_list[index] % 2 != 0:
        total_by_index = total_by_index + my_list[index]

print(f"Sum of all odd numbers : {total_by_index}")

# Iteration by value
total_by_value = 0

for num in my_list:
    if num % 2 != 0:
        total_by_value += num

print(f"Sum of all odd numbers : {total_by_value}")

# Remove all the even numbers from the list

my_list = [5, 7, 4, 8, 10, 12, 14]
result = []
print(f"Original list : {my_list}")

n = len(my_list)

# Using append method
for i in range(0, n):
    if my_list[i] % 2 != 0:
        result.append(my_list[i])
print(f"Resultant list : {result}")

"""Using remove method will not work here as when iterating, it will skip the 
immediate number next to the removed number."""
# for num in my_list:
#     if num % 2 == 0:
#         my_list.remove(num)
# print(f"Resultant list : {my_list}") # Result --> [5, 7, 8, 12]

# Print all the prime numbers from the list

# Level easy -->


def is_prime_number(num: int) -> bool:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]

print(f"The prime numbers are : ")
for num in my_list:
    if is_prime_number(num) == True:
        print(num, end=" ")


# Level hard -->

my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]
for num in my_list:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        print(num, end=" ")
