"""
a) List comprehension in Python is a concise way to create lists by applying an expression
to each item in an iterable (like a list or range) and optionally filtering elements.
b) Faster than the traditional loops

Syntax : 
# [expression for item in iterable if condition]
expression: The expression or operation applied to each item.
item: The variable representing each element in the iterable.
iterable: The list, range, or any iterable object.
condition (optional): A filter applied to the items.
"""

# Basic List comprehension
my_list = [i for i in range(10, 0, -1)]
print(my_list)

squares = [x**2 for x in range(5)]
print(squares)

# List comprehension with condition check
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# List comprehension with nested loops
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)

# Print prime number from 1 to 50 using List comprehension


def prime_num(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


x = [prime for prime in range(1, 51) if prime_num(prime) and prime != 1]
print(f"Prime numbers from 1 to 50 are :{x}")

# Print "EVEN" OR "ODD" for range of numbers 1 to 20

my_list = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
print(f"Result list :{my_list}")


# Print even number from the given list of numbers

my_list = [34, 67, 45, 32, 89, 80, 97, 94]
# ans = [num for num in my_list if num % 2 == 0]
ans = [my_list[i] for i in range(0, len(my_list)) if my_list[i] % 2 == 0]
print(f"Even number List : {ans}")
