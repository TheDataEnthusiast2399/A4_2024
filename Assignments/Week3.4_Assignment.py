"""
Q.1: Make following pattern

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""


def pattern1(n: int):
    # Upper half
    for i in range(1, n // 2 + 2):
        # To print stars
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
    # Lower half
    for i in range(n // 2, 0, -1):
        # To print stars
        for j in range(1, i + 1):
            print("*", end=" ")
        print()


n = int(input("Enter input --> "))
pattern1(n)

"""
Q.2 : Make following pattern

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""


def pattern2(n: int):
    # Upper half
    for i in range(1, n // 2 + 2):
        num = 1
        # To print stars
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()
    # Lower half
    for i in range(n // 2, 0, -1):
        num = 1
        # To print stars
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()


n = int(input("Enter input --> "))
pattern2(n)

"""
Q.2 : Make following pattern

5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5

"""


def pattern3(n: int):
    # Upper half
    for i in range(n // 2 + 1, 0, -1):
        # To print digits
        for j in range(i, n // 2 + 2):
            print(j, end=" ")
        print()
    # Lower half
    for i in range(2, n // 2 + 2):
        # To print digits
        for j in range(i, n // 2 + 2):
            print(j, end=" ")
        print()


n = int(input("Enter input --> "))
pattern3(n)

"""
Q.4 Make following pattern

        *
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *
"""


def pattern4(n: int):

    # Upper half
    for i in range(1, n // 2 + 2):
        # To print spaces
        for j in range(1, n // 2 - i + 2):
            print(" ", end=" ")
        # To print digits
        for k in range(1, i + 1):
            print("*", end=" ")
        print()

    # Lower half
    for i in range(n // 2, 0, -1):
        # To print spaces
        for j in range(1, n // 2 - i + 2):
            print(" ", end=" ")
        # To print digits
        for k in range(1, i + 1):
            print("*", end=" ")
        print()


n = int(input("Enter input --> "))
pattern4(n)


"""
Q.5 Make following pattern

        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1
"""


def pattern5(n: int):
    # Upper half
    for i in range(1, n // 2 + 2):
        # To print spaces
        for j in range(1, n // 2 - i + 2):
            print(" ", end=" ")

        # To print digits
        for k in range(1, i + 1):
            print(k, end=" ")
        print()

    # Lower half
    for i in range(n // 2, 0, -1):
        # To print spaces
        for j in range(1, n // 2 - i + 2):
            print(" ", end=" ")

        # To print digits
        for k in range(1, i + 1):
            print(k, end=" ")
        print()


n = int(input("Enter input --> "))
pattern5(n)


"""
Q.6 Make following pattern

        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1
  4 3 2 1
    3 2 1
      3 1
        1
"""


def pattern6(n: int):
    # Upper half
    for i in range(1, n // 2 + 2):
        # To print spaces
        for j in range(1, n // 2 - i + 2):
            print(" ", end=" ")
        # To print digits
        for k in range(i, 0, -1):
            print(k, end=" ")

        print()

    for i in range(n // 2, 0, -1):
        # To print spaces
        for j in range(1, n // 2 - i + 2):
            print(" ", end=" ")
        # To print digits
        for k in range(i, 0, -1):
            print(k, end=" ")

        print()


n = int(input("Enter the input --> "))
pattern6(n)
