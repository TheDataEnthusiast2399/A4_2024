# Q.1 -->
a = 5
b = 10

print(a > 5 and b >= 10)  # False
print(a >= 5 or not b > 10)  # True
print(not (a > 5 and b > 5))  # True
print(not (a < 10 or not b < 10))  # False
print(not (not a <= 5 or not b >= 10))  # True

# Q.2 --> Km to m
k1 = int(input("Enter distance in Kilometres : "))
m1 = k1 * 1000  # 1 Km = 1000 m
print(f"Distance in metres is {m1}")

# Q.3 --> 3 num average
n1 = int(input("Enter First number : "))
n2 = int(input("Enter Second number :"))
n3 = int(input("Enter Third number: "))
total = n1 + n2 + n3
print(f"The average is {total/3}")

# Q.4 --> Rupees to Paise
rup = int(input("Enter the amount in rupees : "))
print(f"The amount in paise is {rup * 100}")  # 1 rs = 100 paise

# Q.5 --> Area of Square
s1 = int(input("Enter side of square: "))
print(s1**2)  # Area of square = side * side

# Q.6 --> Number of Games played in tournament
GamesPlayed = int(input("Enter number of games played : "))
GamesWon = int(input("Enter number of games won : "))
GamesLost = int(input("Enter number of games lost : "))

GamesTied = GamesPlayed - (GamesWon + GamesLost)  # Checks whether if any games tied
TotalPoints = (GamesWon * 4) + (GamesTied * 2)  # Won - 4 Points | Tied - 2 Points
print(f"Total Points scored: {TotalPoints}")

# Q.7 --> Number divisible by 3
num1 = int(input("Enter the number: "))
if num1 % 3 == 0:
    print("Number is divisble by 3")
else:
    print("Number is not divisible by 3")

# Q.8 --> Odd or Even
num2 = int(input("Enter the number: "))
if num2 % 2 == 0:
    print("Number is even")
else:
    print("Number is Odd")

# Q.9 --> Check whether square or not
Length = int(input("Enter the length of rectangle : "))
Breadth = int(input("Enter the Breadth of rectangle : "))

if Length == Breadth:
    print("It is a square")
else:
    print("It is not a square")
