# Check whether number is even or Odd
a = int(input("Enter the number"))
if a % 2 == 0:  # Checks the if conditional block
    print("Even")  # Indented Blocks: enters the condition if satisfies

else:
    print("Odd")  # Enters the else block whenever 'if' block condition fails

# Check whether adult or not

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult.")
else:
    print("Underage.")
