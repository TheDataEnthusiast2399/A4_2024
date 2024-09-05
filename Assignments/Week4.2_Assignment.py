# Q.1 --> slice the list of numbers --> User input start and end


def slice1(nums: list[int], start: int, end: int) -> list[int]:
    if start >= 0 and end >= 0:
        return nums[start : end + 1 : 1]  # Left to right
    return nums[start : end - 1 : -1]  # Right to left


my_lst1 = [23, 24, 12, 13, 19, 90, 29, 12]
start = int(input("Enter the start index : "))
end = int(input("Enter the end index : "))
print(slice1(my_lst1, start, end))


# Q.2 --> slice the list of numbers --> User input start and end --> Return in different list


def slice2(nums: list[int], start: int, end: int) -> list[int]:
    res = []
    if start >= 0 and end >= 0:
        res = nums[start : end + 1 : 1]  # Left to right
    else:
        res = nums[start : end - 1 : -1]  # Right to left
    return res


my_lst2 = [23, 24, 12, 13, 19, 90, 29, 12]
start = int(input("Enter the start index : "))
end = int(input("Enter the end index : "))
print(slice2(my_lst2, start, end))

# Q.3 --> Slice the list of numbers --> with n last elements


def slice3(nums: list[int], end: int) -> list[int]:
    n = len(nums)
    res = nums[n - end :: 1]
    return res


my_lst3 = [2, 3, 4, 1, 0, 12, 18]
end = int(input("Enter number of last n elements : "))
print(slice3(my_lst3, end))

# Q.4 --> Slice the list of numbers --> with n last elements --> in reverse


def slice4(nums: list[int], end: int) -> list[int]:
    n = len(nums)
    res = nums[: -end - 1 : -1]
    return res


my_lst4 = [2, 3, 4, 1, 0, 12, 18]
end = int(input("Enter number of last n elements : "))
print(slice4(my_lst4, end))

# Q.5 --> Interchange first and last elements using slicing


def slice5(nums: list[int]) -> list[int]:
    n = len(nums)
    res = nums[-1:] + nums[1 : n - 1] + nums[:1]
    return res


my_lst5 = [2, 3, 4, 1, 0, 12, 18, 23, 12]
print(slice5(my_lst5))

# Q.6 --> For even length of list --> split into half


def slice6(nums: list[int]) -> None:
    n = len(nums)
    first_split = nums[: n // 2]
    second_split = nums[n // 2 :]
    print(f"First Half : {first_split}")
    print(f"Second Half : {second_split}")


my_lst6 = [2, 3, 4, 1, 0, 12, 18, 23, 12, 98]
slice6(my_lst6)

# Q.7 --> Using list comprehension --> Generate powers of 2 for n input


def powers_of_two(num: int) -> list[int]:
    res = [x**2 for x in range(1, num + 1)]
    return res


n = int(input("Enter the input --> "))
print(powers_of_two(n))

# Q.8 --> Using list comprehension --> Divisible by 3 and 6 in range (1,1000)


res = [i for i in range(1, 1001) if i % 3 == 0 and i % 6 == 0]
print(len(res))

# Q.9 --> Using list comprehension --> Prime number till n input


def isPrime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input("Enter the range : "))
prime_no = [x for x in range(1, n) if isPrime(x)]
print(prime_no)


# Q.10 --> Using list comprehension --> Divisible by 5

n = int(input("Enter the number : "))
res = [x for x in range(1, n) if x % 5 == 0]
print(res)
