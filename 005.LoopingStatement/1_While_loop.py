# While Loop ->
"""
--> With while loop certain set of instructions are carried out as long as 
condition is true.
--> We can run an infinite loop and while loops are more flexible 
"""
# Q.1: Print 1 to 10 -->

a = 1  # Initialize
while a <= 10:  # Condition check enters the block while true
    print(a, end=" ")  # Statement1
    a += 1  # increment


# Q.2 --> Print all the numbers from 1 to n , Ask n from user


n = int(input("Enter the number: "))
i = 1

while i <= n:
    print(i, end=" ")
    i += 1

# Q.3 --> Print all the numbers from start to end, Ask start and end from user

start = int(input("Enter the start num: "))
end = int(input("Enter the start num: "))

i = start
j = end

while i <= j:
    print(i, end=" ")
    i += 1

# Q.4 --> Print all the numbers from start to end , Ask start and end from user
# If end < start , make sure to print all the num from end to start.

start = int(input("Enter the start num: "))
end = int(input("Enter the start num: "))

# Method 1: ---->

# if start < end:
#     i = start
#     j = end
#     while i <= j:
#         print(i, end=" ")
#         i += 1
# else:
#     i = end
#     j = start
#     while i <= j:
#         print(i, end=" ")
#         i += 1

# Method 2 :---->
if start > end:
    start, end = end, start  # Start = end , end = start
i = start
while i <= end:
    print(i, end=" ")
    i += 1

# Q.5 ---> Print even number from 1 to 20:

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1


# Q.6 ---> Print sum of all even numbers

start = int(input("Enter the start num: "))
end = int(input("Enter the start num: "))

i = start
j = end
total = 0
while i <= j:
    if i % 2 == 0:
        total += i
    i += 1
print(total)

# Q.7 --> Print the count of the numbers that are divisible by 3 and count of numbers
# that are divisible by 2 and 7 both in the range specified by users
i = int(input("Enter the start num ->"))
j = int(input("Enter the end num ->"))
count1 = 0
count2 = 0

while i <= j:
    if i % 3 == 0:
        count1 += 1
    if i % 2 == 0 and i % 7 == 0:
        count2 += 1
    i += 1
print(f"Number divisible by 3 is {count1}")
print(f"Number divisible by both 2 and 7 is {count2}")
