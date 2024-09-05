# Print the factors of the user input
# Method 1- Brute Force
def print_factors(num: int) -> None:
    i = 1
    while i <= num:
        if num % i == 0:
            print(i, end=" ")
        i += 1


# Method 2 - A bit optimized
def print_factors2(num: int) -> None:
    i = 1
    while i <= num // 2:
        if num % i == 0:
            print(i, end=" ")
        i += 1
    print(num)


print_factors(20)
print()
print_factors2(45)


# Find the product from the range of 1 to n
def product_of_numbers(num: int) -> int:
    i = 1
    total = 1
    while i <= num:
        total = total * i
        i += 1
    return total


print(product_of_numbers(10))


# Check the number is prime or not:


def countfactors(num: int) -> int:
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    return count


def check_prime(n: int) -> bool:
    factors = countfactors(n)
    if factors == 2:
        return True
    return False


print(check_prime(10))
print(check_prime(11))
print(check_prime(17))

# Keep asking a number from user until he enters zero (0), Calculate total

total = 0
while True:
    num = int(input("Enter number = "))
    if num == 0:
        break
    total = total + num
print(total)
