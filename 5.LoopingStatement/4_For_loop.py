start = int(input("Enter the input = "))
end = int(input("Enter the input = "))
total = 0

# for i in range (start,end):
#     total += i

for i in range(start, end):
    if i % 7 == 0:
        total += i

print(total)

# Nested loops->
for i in range(1, 4):
    print(i)
    for j in range(10, 13):
        print(j)


"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()

"""
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1

"""
for i in range(1, 6):
    for j in range(5, 0, -1):
        print(j, end=" ")
    print()


"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
"""


def pattern(n: int):
    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print()


n = int(input())
pattern(n)
