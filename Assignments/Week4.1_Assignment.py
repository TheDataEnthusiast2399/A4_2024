# Q.1 --> 10 Integer input -> Store in a list -> Copy the list -> reverse the order
from typing import List


def reverse_copy():
    nums = []
    for inputs in range(10):
        inputs = int(input("Enter the number --> "))
        nums.append(inputs)
    print(nums)

    A = nums.copy()  # Copies the original list
    A.reverse()  # Reverse the copied list
    print(A)


reverse_copy()

# Q.2 -->
from typing import List


def add_list_elements(nums: List) -> int:
    result = nums[1] + nums[-2]
    return result


my_lst = [2, 3, 4, 5, 9, 12, 15, 19, 20]
print(add_list_elements(my_lst))

# Q.3 --> Ask 10 numbers -> Remove even from list

from typing import List


def remove_even() -> List[int]:
    nums = []
    for i in range(10):
        inputs = int(input("Enter the number --> "))
        nums.append(inputs)
    print(nums)

    odd_lst = []  # List will contain only odd elements
    for num in nums:
        if num % 2 != 0:
            odd_lst.append(num)
    return odd_lst


remove_even()


# Q.4 -->
from typing import List


def count_greater_than_three(nums: List) -> List[int]:
    res = []
    for num in nums:
        if (
            nums.count(num) > 3 and num not in res
        ):  # Prints the number whose count is greater than 3 by avoiding duplicate
            res.append(num)
    return res


my_lst2 = [2, 9, 4, 14, 9, 6, 24, 2, 7, 8, 9, 24, 23, 49, 24, 45, 24, 9, 21, 34]
print(count_greater_than_three(my_lst2))


# Q.5 --> remove nth index
from typing import List


def remove_index(nums: List[int], index: int) -> None:
    n = len(nums)

    if index > n or index < -n:  # Works for both positive and negative indices
        print("Index does not exists")
    else:
        res = nums.pop(index)
        print(f"List after removing {index} element : {res}")


my_lst3 = [24, 25, 57, 8, 9, 12]
index = 5
remove_index(my_lst3, index)


# Q.6 --> Addition of two lists
from typing import List


def add_two_lists(nums1: List[int], nums2: List[int]) -> List[int]:
    res = []

    n = len(nums1)

    for i in range(n):
        add = nums1[i] + nums2[i]
        res.append(add)
    return res


my_lst3 = [23, 4, 23, 21, 23]
my_lst4 = [41, 23, 4, 31, 21]

print(add_two_lists(my_lst3, my_lst4))


# Q.7 : Sum and average of lists

from typing import List


def sum_avg(nums: List[int]) -> None:
    Sum = 0
    avg = 0

    n = len(nums)

    for num in nums:
        Sum += num

    avg = Sum / n

    print(f"Sum of list is : {Sum}")
    print(f"Average of list is : {avg}")


my_lst = [23, 24, 98, 12]
sum_avg(my_lst)


# Q.9 --> Even and odd list

from typing import List


def odd_even_list(nums: List[int]) -> None:
    odd_lst = []
    even_lst = []

    for num in nums:
        if num % 2 != 0:
            odd_lst.append(num)
        else:
            even_lst.append(num)

    print(f"The odd list : {odd_lst}")
    print(f"The even list : {even_lst}")


my_lst5 = [23, 12, 1, 4, 56, 77, 23, 6, 7, 8, 90]
odd_even_list(my_lst5)
