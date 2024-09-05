# Q.1 -->
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a % b == 0:
    print(f"{a} is divisible by {b}")
else:
    print(f"{a} is not divisible by {b}")

# Q.2 -->
total_classes = int(input("Enter total number of classes held: "))
class_attended = int(input("Enter total classes attended: "))

total_Attendance = (class_attended / total_classes) * 100
print(f"Total attendance is {total_Attendance:.0f}%")
if total_Attendance >= 75:
    print("Allowed for exams")
else:
    print("Not allowed for exams")

# Q.3 --> Divisible by 2 and 3 but not 8
num1 = int(input("Enter the number: "))
if num1 % 2 == 0 and num1 % 3 == 0 and num1 % 8 != 0:
    print("Number is divisible by 2 and 3")

# Q.4 -->Grade
score = int(input("Enter the marks scored: "))
if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score <= 89:
    print("Grade B")
elif score >= 70 and score <= 79:
    print("Grade C")
elif score >= 60 and score <= 69:
    print("Grade D")
elif score <= 60:
    print("Grade F")
else:  # First Else Block
    print("Invalid Marks entered")

# Q.5 --> Bill calculation
amount = int(input("Enter the amount: "))
final_bill = 0

if amount >= 50000:
    final_bill = amount - amount * 0.30  # 30% discount
    print(final_bill)
elif amount >= 40000 and amount <= 49999:
    final_bill = amount - amount * 0.25  # 25% discount
    print(final_bill)
elif amount >= 30000 and amount <= 39999:
    final_bill = amount - amount * 0.20  # 20% discount
    print(final_bill)
elif amount >= 10000 and amount <= 29999:
    final_bill = amount - amount * 0.10  # 10% discount
    print(final_bill)
elif amount >= 1 and amount <= 9999:
    final_bill = amount  # no discount
    print(final_bill)
else:
    print("Invalid amount entered")

# Q.6 : Smallest number -->
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
n4 = int(input("Enter the fourth number: "))

if n1 < n2 and n1 < n3 and n1 < n4:
    print(f"{n1} is the smallest number.")
elif n2 < n3 and n3 < n4 and n2 < n1:
    print(f"{n2} is the smallest number.")
elif n3 < n4 and n3 < n2 and n3 < n1:
    print(f"{n3} is the smallest number.")
else:
    print(f"{n4} is the smallest number.")

# Q.7 : Salary of Employee --->

salary = int(input("Enter the salary: "))
if salary < 10000:
    hike = 0.05  # 5% hike
elif salary <= 20000:
    hike = 0.10  # 10% hike
elif salary <= 50000:
    hike = 0.15  # 15% hike
else:
    hike = 0.20  # 20% hike

Final_salary = salary + (salary * hike)
print(f"You get {hike:.0f}% increment. Updated salary = {Final_salary}")


# Q.8 : Leap Year ---->

year = int(input("Enter the year : "))

if year % 4 == 0:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


year = int(input())
if year % 4 == 0 and year % 100 == 0:
    print("It's not leap year")
elif year % 4 == 0 and year % 400 == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")
