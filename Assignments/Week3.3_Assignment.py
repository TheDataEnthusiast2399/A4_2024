"""
Q.1 Make following pattern ; ask user input 
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5 

"""


def pattern1(n: int):
    for i in range(1, n + 1):
        # To print spaces
        for j in range(1, (n - i) + 1):
            print(" ", end=" ")

        # To print digits
        for k in range(1, i + 1):
            print(k, end=" ")

        print()


n = int(input("Enter the input --> "))
pattern1(n)

"""
Q.2 Make following pattern ; ask user input 
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1 

"""


def pattern2(n: int):
    for i in range(1, n + 1):
        # To print spaces
        for j in range(1, n - i + 1):
            print(" ", end=" ")

        # To print digits:
        for k in range(i, 0, -1):
            print(k, end=" ")
        print()


n = int(input("Enter the input --> "))
pattern2(n)

"""
Q.3 Make following pattern ; ask user input 
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1

"""


def pattern3(n: int):
    for i in range(n, 0, -1):
        # To print spaces
        for j in range(1, i):
            print("#", end=" ")
        # To print digits
        for k in range(n, i - 1, -1):
            print(k, end=" ")
        print()


n = int(input("Enter the input --> "))
pattern3(n)

"""
Q.4 Make following pattern ; ask user input 
        5
      4 5
    3 4 5
  2 3 4 5
1 2 3 4 5

"""


def pattern4(n: int):
    for i in range(n, 0, -1):
        # To print spaces -->
        for j in range(1, i):
            print("#", end=" ")
        # To print digits -->
        for k in range(i, n + 1):
            print(k, end=" ")

        print()


n = int(input("Enter input : "))
pattern4(n)


"""
Q.5 : Make following pattern


        5
      4 4
    3 3 3
  2 2 2 2
1 1 1 1 1

"""


def pattern5(n: int):

    for i in range(n, 0, -1):
        # To print spaces
        for j in range(1, i):
            print("#", end=" ")
        # To print digits
        for k in range(i, n + 1):
            print(i, end=" ")
        print()


n = int(input("Enter the input --> "))
pattern5(n)


"""
Q.6 Make following pattern 

        *
      * * * 
    * * * * * 
  * * * * * * *
* * * * * * * * *

"""


def pattern6(n: int):
    for i in range(1, n + 1):

        # To print spaces ->
        for j in range(1, n - i + 1):
            print("#", end=" ")
        # To print stars ->
        for k in range(1, 2 * i):
            print("*", end=" ")

        print()


n = int(input("Enter the input --> "))
pattern6(n)


"""
Q.7 Make following pattern 
                      
        5             
      4 4 4           
    3 3 3 3 3         
  2 2 2 2 2 2 2       
1 1 1 1 1 1 1 1 1     

"""


def pattern7(n: int):

    for i in range(1, n + 1):
        # To print spaces
        for j in range(1, n - i + 1):
            print(" ", end=" ")

        # To print digits
        for k in range(1, 2 * i):
            print(n - i + 1, end=" ")
        print()


n = int(input("Enter the input --> "))
pattern7(n)

"""
Q.7 Make following pattern 
                      
        1            
      1 2 3           
    1 2 3 4 5        
  1 2 3 4 5 6 7       
1 2 3 4 5 6 7 8 9     

"""


def pattern8(n: int):
    for i in range(1, n + 1):
        num = 1
        # To print spaces:
        for j in range(1, n - i + 1):
            print(" ", end=" ")
        # To print digits :
        for k in range(1, 2 * i):
            print(num, end=" ")
            num += 1
        print()


n = int(input("Enter input --> "))
pattern8(n)


"""
Q.8: Make the following pattern
        *
      * * * 
    * * * * * 
  * * * * * * *
* * * * * * * * *
  * * * * * * * 
    * * * * * 
      * * *
        *

"""


def pattern9(n: int):

    # Upper half -->
    for i in range(1, n // 2 + 2):
        # To print spaces
        for j in range(1, n // 2 - i + 2):
            print(" ", end=" ")
        # To print digits
        for k in range(1, 2 * i):
            print("*", end=" ")
        print()

    # Lower half -->
    for i in range(n // 2, 0, -1):
        # To print spaces
        for j in range(1, n // 2 - i + 2):
            print(" ", end=" ")
        # To print digits
        for k in range(1, 2 * i):
            print("*", end=" ")
        print()


n = int(input("Enter input --> "))
pattern9(n)


"""
Q.10 : Make the following pattern
        1
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7 
    1 2 3 4 5 
      1 2 3
        1

"""


def pattern10(n: int):

    # Upper half -->
    for i in range(1, n // 2 + 2):
        num = 1
        # To print spaces
        for j in range(1, n // 2 - i + 2):
            print(" ", end=" ")
        # To print digits
        for k in range(1, 2 * i):
            print(num, end=" ")
            num += 1
        print()

    # Lower half -->
    for i in range(n // 2, 0, -1):
        num = 1
        # To print spaces
        for j in range(1, n // 2 - i + 2):
            print(" ", end=" ")
        # To print digits
        for k in range(1, 2 * i):
            print(num, end=" ")
            num += 1
        print()


n = int(input("Enter input --> "))
pattern10(n)
