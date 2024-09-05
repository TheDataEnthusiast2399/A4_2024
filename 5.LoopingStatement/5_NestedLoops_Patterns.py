"""
1) Nested loops are basically loops nested or written within another loop
2) Basically it contains inner loop and outer loop.
"""

for i in range(1, 4):  # Outer loop
    print(i)
    for j in range(10, 13):  # Inner loop
        print(j)

# Q.1 : Print the following pattern for n input
"""
n = 5

*
**
***
****
*****
"""


def pattern1(n: int) -> None:
    i = 1
    while i <= n:
        print("*" * i)
        i += 1


num = int(input("Enter input -> "))
pattern1(num)

# Q.2: Print the following pattern for n input
"""
n = 5

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


"""


def pattern2(n: int) -> None:
    i = 1  # For rows
    # For columns

    while i <= n:
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1
        print()
        i += 1


num = int(input("Enter input -->"))
pattern2(num)

# Q.3 :Print the following pattern for n input
"""
n = 5

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
"""


def pattern3(n: int) -> None:
    i = n  # Row
    k = 0
    while i >= 1:
        j = 1  # Column
        k += 1
        while j <= i:
            print(k, end=" ")
            j += 1
        print()
        i -= 1


num = int(input("Enter the input -->"))
pattern3(5)


# Q.4 --> Print pattern for n input
"""
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
"""


def pattern4(n: int) -> None:
    i = n
    k = 5

    while i >= 1:
        j = 1
        while j <= i:
            print(k, end=" ")
            j += 1
        print()
        i -= 1


pattern4(5)


n = 368
i = 1

total = 0
while i <= n:
    if n % i == 0:
        total += i
    i += 1
print(total)

# Print the following pattern
"""
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
"""


def pattern5(n: int) -> None:
    i = 1

    while i <= n:
        j = 1
        while j <= i:
            print(i * j, end=" ")
            j += 1
        print()
        i += 1


pattern5(8)

# Print the following pattern
"""
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
"""


def pattern6(n: int) -> None:
    i = 1

    while i <= n:
        j = 1
        while j <= n:
            if j < i:
                print(i, end=" ")
            else:
                print(j, end=" ")
            j += 1
        print()
        i += 1


pattern6(5)

# Print the following pattern :
"""
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
"""


def pattern7(n: int) -> None:
    i = 1
    j = n

    while i <= n:

        k = 0

        while k <= j:
            print(k, end=" ")
            k += 1
        print()
        j -= 1
        i += 1


pattern7(5)
