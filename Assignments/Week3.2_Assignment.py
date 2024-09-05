"""
Q.1 --> Make following pattern

1
1 2
1 2 3
1 2 3 4
"""


def pattern1(num: int):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


n = int(input("Enter input: "))
pattern1(n)

"""
Q.2 --> Make following pattern

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""


def pattern2(num: int):
    for i in range(1, num + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


n = int(input("Enter the input: "))
pattern2(n)


"""
Q.3 --> Make following pattern

5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
"""


def pattern3(num: int):
    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print()


n = int(input("Enter the input: "))
pattern3(n)


"""
Q.4 : Make the following pattern

5
5 4
5 4 3 
5 4 3 2
5 4 3 2 1
"""


def pattern4(num: int):
    for i in range(num, 0, -1):
        for j in range(5, i - 1, -1):
            print(j, end=" ")
        print()


n = int(input("Enter the input: "))
pattern4(n)

"""
Q.5 : Make the following pattern

5 4 3 2 1
5 4 3 2
5 4 3
5 4 
5
"""


def pattern5(n: int):
    for i in range(1, n + 1):
        for j in range(5, i - 1, -1):
            print(j, end=" ")
        print()


n = int(input("Enter the input: "))
pattern5(n)

"""
Q.6 -> Make the following pattern

1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""


def pattern6(n: int):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print()


n = int(input("Enter the input : "))
pattern6(n)


"""
Q.7 : Make following pattern

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""


def pattern7(n: int):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


n = int(input("Enter the input: "))
pattern7(n)


"""
Q.8 : Make following pattern

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""


def pattern8(n: int):
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()


n = int(input("Enter input: "))
pattern8(n)


"""
Q.9 Make following pattern

1
1 2
1 2 1
1 2 1 2
1 2 1 2 1
"""


def pattern9(n: int):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j % 2 != 0:
                print(1, end=" ")
            else:
                print(2, end=" ")
        print()


n = int(input("Enter input: "))
pattern9(n)

"""
Q.10 Make following pattern

1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
"""


def pattern10(n: int):
    for i in range(1, n + 1):
        for j in range(1, n - i + 2):
            print(j, end=" ")
        print()


n = int(input("Enter input: "))
pattern10(n)
