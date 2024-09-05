# Q.1 --> Print count of total odd no in a list


def count_odd(nums: list[int]) -> int:
    count = 0
    for i in nums:
        if i % 2 != 0:
            count += 1
    return count


my_list1 = [4, 8, 6, 5, 3, 12, 1, 3]
print(f"Total odd numbers = {count_odd(my_list1)}")

# Q.2 --> Print count of total odd and even no in a list


def count_evn_odd(nums: list[int]) -> None:
    count_even = 0
    count_odd = 0

    for i in nums:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    print(f"Total even numbers = {count_even}")
    print(f"Total odd numbers = {count_odd}")


my_list2 = [4, 8, 6, 5, 3, 12, 1, 3, 6]
count_evn_odd(my_list2)

# Q.3 --> Print prime numbers from given list


def isPrime1(nums: list[int]) -> list[int]:
    prime_num = []
    for i in nums:
        count_factors = 0
        for num in range(1, i + 1):
            if i % num == 0:
                count_factors += 1

        if count_factors == 2:
            prime_num.append(i)

    return prime_num


my_list3 = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]
print(isPrime1(my_list3))

# Q.4 --> Print sum of all prime numbers in list


def isPrime2(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


my_list4 = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]
sum_Prime = 0
for num in my_list4:
    if isPrime2(num):
        sum_Prime += num
print(f"Total of all prime numbers = {sum_Prime}")

# Q.5 --> Print sum and product of all elements in a list


def sum_and_prod(nums: list[int]) -> None:
    Sum = 0
    prod = 1

    for i in nums:
        Sum += i
        prod *= i

    print(f"Total sum = {Sum}")
    print(f"Total product = {prod}")


my_list5 = [4, 8, 6, 3, 5, 12, 1, 7, 6, 2]
sum_and_prod(my_list5)


# Q.6 --> Print all numbers divisible by 5 in reversed order


def divisible_by_five(nums: int) -> bool:

    if nums % 5 == 0:
        return True
    return False


my_list6 = [5, 8, 10, 15, 2, 4, 95, 34, 25]

n = len(my_list6)
for i in range(n - 1, -1, -1):
    if divisible_by_five(my_list6[i]):
        print(my_list6[i], end=" ")

# Q.7 --> Print maximum element in the given list


# Method 1 -->
def max_element(nums: list[int]) -> None:
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num = num
    print(f"Maximum number = {max_num}")


my_list7 = [5, -8, 10, 15, 2, -4, 95, -34, 25]
max_element(my_list7)

# Method2 --> Using max() :
my_list7 = [5, -8, 10, 15, 2, -4, 95, -34, 25]
max_num = float("-inf")
for num in my_list7:
    max_num = max(max_num, num)
print(f"Maximum number = {max_num}")


# Q.8 --> Print minimum element in the given list


# Method 1 -->
def min_element(nums: list[int]) -> None:
    min_num = float("inf")
    for num in nums:
        if num < min_num:
            min_num = num
    print(f"Minimum number = {min_num}")


my_list8 = [5, -8, 10, 15, 2, -4, 95, -34, 25]
min_element(my_list8)

# Method2 --> Using min() :
my_list8 = [5, -8, 10, 15, 2, -4, 95, -34, 25]
min_num = float("inf")
for num in my_list8:
    min_num = min(min_num, num)
print(f"Minimum number = {min_num}")


# Q.9 : Print largest prime number
def isPrime3(nums: int) -> bool:
    for i in range(2, nums):
        if nums % i == 0:
            return False
    return True


my_list9 = [4, 8, 6, 19, 3, 12, 1, 7, 6, 2]
largestPrime = 0
for i in my_list9:
    if isPrime3(i):
        largestPrime = max(largestPrime, i)
print(f"Largest prime number = {largestPrime}")
