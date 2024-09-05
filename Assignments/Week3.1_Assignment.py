# 1 : Print the following pattern
"""
1 1 1 1 1 
1 1 1 1 1 
1 1 1 1 1 
1 1 1 1 1 
1 1 1 1 1

n = 5
"""


def pattern1(n: int) -> None:
    for i in range(n):
        for j in range(5):
            print(1, end=" ")
        print()


n = int(input("Enter the input : "))
pattern1(n)

# 2 : Print the following pattern

"""
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1

n = 3
"""


def pattern2(n: int) -> None:
    for i in range(n):
        for j in range(5, 0, -1):
            print(j, end=" ")
        print()


n = int(input("Enter input: "))
pattern2(n)

# 3: Print the pattern , for following n and m input where n denotes rows and m denotes digits
"""
1 2 3 4
1 2 3 4
1 2 3 4

n = 3 , m = 4
"""


def pattern3(n: int, m: int) -> None:
    for i in range(n):
        for j in range(1, m + 1):
            print(j, end=" ")
        print()


n = int(input("Enter rows: "))
m = int(input("Enter the range of digits: "))
pattern3(n, m)
