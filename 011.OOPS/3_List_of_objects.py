"""
We can directly create a list which will keep track of all the objects of the class.
"""

# Create a menu portal for student report information
from typing import List


class Student:

    def __init__(
        self, roll_no: int, name: str, age: int, gender: str, marks: List[int]
    ) -> None:
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks
        self.total = 0
        self.percent = 0.0

    def total_grade(self) -> int:
        if not self.marks:
            print(
                "No marks entered for this student. Please first choose menu 3 to enter marks"
            )
            return 0

        self.total = sum(self.marks)
        print(f"Total marks obtained: {self.total}")
        return self.total

    def percentage(self) -> float:
        if not self.marks:
            print(
                "No marks entered for this student. Please first choose menu 3 to enter marks"
            )
            return 0.0

        total_marks = self.total
        count_sub = len(self.marks)
        self.percent = (total_marks / (count_sub * 100)) * 100.0
        print(f"Percentage scored : {self.percent:.2f}")
        return self.percent

    def update_personal_details(self):
        self.name = input("Enter new name: ")
        self.age = int(input("Enter new age: "))
        self.gender = input("Enter new gender: ")

        update_mark_choice = input(
            "Do you wish to update marks for the following student (Y/N): "
        )
        if update_mark_choice == "Y":
            self.marks = list(map(int, input("Enter new marks: ").split()))
            print("Marks updated successfully!")
            print("<------------------------->")
        else:
            print("Marks update skipped.")

    def display_details(self):
        print("<--------------------------------->")
        print(f"Student Roll No : {self.roll_no}")
        print(f"Student Name : {self.name}")
        print(f"Student Age : {self.age}")
        print(f"Student Gender : {self.gender}")
        self.total_grade()
        self.percentage()
        if self.percent > 35:
            print("Promotion Status : Passed")
        else:
            print("Promotion Status: Fail")
        print("<--------------------------------->")


student_details: List[Student] = []
student_roll_no_details = set()

while True:
    print("<---Student Report Information Menu--->")
    print("1. Add a student.")
    print("2. Remove a student.")
    print("3. Update Student details.")
    print("4. Display all student details.")
    print("5. Exit Menu.")
    print("<------------------------------------->")
    print()

    choice = int(input("Enter your choice : "))
    if choice == 1:
        roll_no = int(input("Enter roll no = "))
        name = input("Enter name = ")
        age = int(input("Enter age = "))
        gender = input("Enter gender = ")
        marks = list(map(int, input("Enter the marks: ").split()))

        # Check if roll no already present in list of student detail
        if roll_no in student_roll_no_details:
            print("Student record already exists!")
            break
        else:
            # Add the student to the list and the roll number to the set
            x = Student(roll_no, name, age, gender, marks)
            student_details.append(x)
            student_roll_no_details.add(roll_no)
            print(f"Student added successfully.")
            print("<----------------------------->")

    elif choice == 2:
        roll_no = int(input("Enter roll no of student to be removed : "))
        student_index = -1
        for i in range(len(student_details)):
            if roll_no == student_details[i].roll_no:
                student_index = i
                break
        if student_index == -1:
            print("Student details not found in the records!!")
            print("<------------------------------------------->")
        else:
            student_details.pop(student_index)
            print("Student details successfully removed from the records")
            print("<------------------------------------------->")

    elif choice == 3:
        roll_no = int(
            input("Enter student roll number you want to update details for = ")
        )
        for student in student_details:
            if roll_no == student.roll_no:
                student.update_personal_details()
                print("Student details updated successfully")
                break
        else:
            print(
                "No student found with that roll number. Please add the student first"
            )
            print(
                "<-------------------------------------------------------------------->"
            )

    elif choice == 4:
        rno = int(input("Enter student roll number you want to search for = "))
        for student in student_details:
            if rno == student.roll_no:
                student.display_details()
                break
        else:
            print("No student found with that roll number")
            print("<------------------------------------->")

    elif choice == 5:
        break

    else:
        print("Invalid choice.")
        break
