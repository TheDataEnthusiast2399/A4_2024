# Operations on List
a = [1, 2, 3]
print(id(a))
b = [6, 7, 8]
c = [True, False]


# Only addition and multiplication are the operations allowed in lists.
ans1 = a + b + c  # List concatentation
# ans = a * b     # Not allowed with sequence types
ans2 = a * 5
print(ans1)
print(id(ans1))
print(ans2)

# [-1,-1,-1,-1,-1]
a = [-1] * 5
print(a)
