# Print 1 to n using recursive function:
def func1(i):
    if i < 1:
        return
    func1(i - 1)
    print(f"Recursion : {i}")


func1(10)


# Print n to 1 using recursive function
def func2(i):
    if i > 10:
        return
    func2(i + 1)
    print(f"Recursion : {i}")


func2(1)

# Parameterized way -->
# Print sum of n natural numbers


def sumfunc(i, total):
    if i < 1:
        print(f"Total sum of natural num : {total}")
        return
    sumfunc(i - 1, total + i)


x = 10
sumfunc(x, 0)


# Functional way -->
"""
1) Make the flow 
2) Calculate the base case
3) Look for exception (Optional)
"""


def sum_natural_num(num):
    if num == 1:
        return 1
    return num + sum_natural_num(num - 1)


print(sum_natural_num(10))


# Print factorial of a number


def fact(num):
    if num == 1 or num == 0:
        return 1
    return num * fact(num - 1)


print(fact(0))


# Calculate power with given base


def pow_num(base, power):
    if power == 1:
        return base
    return base * pow_num(base, power - 1)


print(pow_num(8, 19))

# Calculate fibonacci sequence
# TC --> O(2ⁿ) 
# SC --> O(2ⁿ) 

def fibo(num: int):

    if num == 0:
        return 0
    if num == 1:
        return 1

    return fibo(num - 1) + fibo(num - 2)


print(fibo(8))
