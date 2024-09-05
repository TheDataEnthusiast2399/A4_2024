# Q.1 --> Print all the details in format
"""
Anirudh: 56, 78, 65
Sanjay: 58, 78, 56, 12, 33, 56, 78
Muskan: 87, 78, 65, 45
Nihar: 32, 78, 32, 98, 33
Akshay: 56, 40

"""


def print_details(d1: dict[str, list[int]]) -> None:
    for student, marks in d1.items():
        print(f"{student}: {', '.join(str(m) for m in marks)}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

print_details(details)


# Q.2 --> Print highest marks of the student


def display_highest(d1: dict[str, list[int]]) -> None:
    for student, marks in d1.items():
        highest_mark = 0
        for m in marks:
            if m > highest_mark:
                highest_mark = m
        print(f"{student} : {highest_mark}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

display_highest(details)


# Q.3 --> Print the highest scored by the student , multiple students can score highest, print all of them


def highest_score(d1: dict[str, list[int]]) -> None:
    highest_score = 0
    for marks in d1.values():
        for score in marks:  # Since values are in list
            if score > highest_score:
                highest_score = score
    for student, marks in d1.items():
        if highest_score in marks:
            print(f"The highest mark is {highest_score}, scored by {student}")


details = {
    "Anirudh": [56, 78, 65, 98],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40, 98],
}
highest_score(details)


# Q.4 --> Calculate and print average marks of each student


def average_score(d1: dict[str, list[int]]) -> None:
    for student, marks in d1.items():
        n = len(marks)
        total_marks = 0
        for score in marks:
            total_marks += score
        print(f"{student}: {total_marks/n:.2f}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

average_score(details)

# Q.5 --> Print the highest average marks.


def avg_score(marks: list[int]) -> float:
    total_score = 0
    count_scores = 0

    for score in marks:
        total_score += score
        count_scores += 1
    return total_score / count_scores


def highest_avg(d1: dict[str, list[int]]) -> None:
    highest_avg = 0
    highest_avg_student = ""
    for student, scores in d1.items():
        if avg_score(scores) > highest_avg:
            highest_avg = avg_score(scores)
            highest_avg_student = student
    print(f"The highest average is scored by {highest_avg_student} : {highest_avg}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

highest_avg(details)

# Q.6 --> Count the total number of marks entered for each student


def count_entries(d1: dict[str, list[int]]) -> None:
    for student, score in d1.items():
        count_scores = 0
        for marks in score:
            count_scores += 1
        print(f"{student} : {count_scores}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

count_entries(details)

# Q.7 -->Identify the students who have scored more than specified number of marks. Ask the threshold marks from user


def print_greater_than(d1: dict[str, list[int]]) -> None:
    x = int(input("Student who scored more than : "))
    for student, marks in d1.items():
        res_scores = []
        for score in marks:
            if score > x:
                res_scores.append(score)
        if res_scores:
            print(f"{student} : {res_scores}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

print_greater_than(details)


# Q.8 --> Print name and age of each student
def display_details(d1: dict[str, dict[str, int]]) -> None:
    x = "age"
    for name in d1:
        print(f"{name} : {d1[name][x]}")


details = {
    "Anirudh": {
        "age": 56,
        "gender": "Male",
        "marks": [3, 455, 64, 33],
        "adult": True,
    },
    "Muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [34, 89, 70, 99, 43],
        "adult": False,
    },
    "Nihar": {
        "age": 24,
        "gender": "Male",
        "marks": [99, 100],
        "adult": True,
    },
}

display_details(details)

# Q.9 --> Print the name of students who are adults


def display_adults(d1: dict[str, dict]) -> None:
    for name, record in d1.items():
        if d1[name]["age"] > 18:
            print(f"{name}")


details = {
    "Anirudh": {
        "age": 56,
        "gender": "Male",
        "marks": [3, 455, 64, 33],
        "adult": True,
    },
    "Muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [34, 89, 70, 99, 43],
        "adult": False,
    },
    "Nihar": {
        "age": 24,
        "gender": "Male",
        "marks": [99, 100],
        "adult": True,
    },
}

display_adults(details)

# Q.10--> Calculate average marks of each student


def avg2(d1: dict[str, dict]) -> None:

    for name, record in d1.items():
        total_marks = 0
        n = len(d1[name]["marks"])
        for score in d1[name]["marks"]:
            total_marks += score
        print(f"{name} : {total_marks/n}")


details = {
    "Anirudh": {
        "age": 56,
        "gender": "Male",
        "marks": [3, 455, 64, 33],
        "adult": True,
    },
    "Muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [34, 89, 70, 99, 43],
        "adult": False,
    },
    "Nihar": {
        "age": 24,
        "gender": "Male",
        "marks": [99, 100],
        "adult": True,
    },
}
avg2(details)


# Q.11 --> Print name and highest marks of each student


def highest_mark(d1: dict[str, dict]) -> None:

    for name, record in d1.items():
        highest_mark = 0
        for score in d1[name]["marks"]:
            if score > highest_mark:
                highest_mark = score
        print(f"{name}:{highest_mark}")


details = {
    "Anirudh": {
        "age": 56,
        "gender": "Male",
        "marks": [3, 455, 64, 33],
        "adult": True,
    },
    "Muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [34, 89, 70, 99, 43],
        "adult": False,
    },
    "Nihar": {
        "age": 24,
        "gender": "Male",
        "marks": [99, 100],
        "adult": True,
    },
}

highest_mark(details)

# Q.12 --> Find and print name of students with more than 3 marks entries


def greater_than(d1: dict[str, dict]) -> None:
    for name, records in d1.items():
        count = 0
        for score in d1[name]["marks"]:
            count += 1
        if count > 3:
            print(f"{name}")


details = {
    "Anirudh": {
        "age": 56,
        "gender": "Male",
        "marks": [3, 455, 64, 33],
        "adult": True,
    },
    "Muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [34, 89, 70, 99, 43],
        "adult": False,
    },
    "Nihar": {
        "age": 24,
        "gender": "Male",
        "marks": [99, 100],
        "adult": True,
    },
}

print(f"Student with more than 3 marks entries:")
greater_than(details)

# Q.13 --> Print total marks scored by each student


def total_marks(d1: dict[str, dict]) -> None:

    for name, record in d1.items():
        total_marks = 0
        n = len(d1[name]["marks"])
        for score in d1[name]["marks"]:
            total_marks += score
        print(f"{name} : {total_marks}")


details = {
    "Anirudh": {
        "age": 56,
        "gender": "Male",
        "marks": [3, 455, 64, 33],
        "adult": True,
    },
    "Muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [34, 89, 70, 99, 43],
        "adult": False,
    },
    "Nihar": {
        "age": 24,
        "gender": "Male",
        "marks": [99, 100],
        "adult": True,
    },
}
total_marks(details)

# Q.14 --> Print the name of youngest student


def youngest_student(d1: dict[str, dict]):
    min_age = float("inf")
    min_age_student = ""
    for name, record in d1.items():
        x = d1[name]["age"]
        if x < min_age:
            min_age = x
            min_age_student = name
    print(f"The youngest student is {min_age_student}, age : {min_age}")


details = {
    "Anirudh": {
        "age": 56,
        "gender": "Male",
        "marks": [3, 455, 64, 33],
        "adult": True,
    },
    "Muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [34, 89, 70, 99, 43],
        "adult": False,
    },
    "Nihar": {
        "age": 24,
        "gender": "Male",
        "marks": [99, 100],
        "adult": True,
    },
}
youngest_student(details)

# Q.15 --> Print student with highest average marks


def highest_avg2(d1: dict[str, dict]) -> None:
    highest_avg = 0
    highest_avg_student = ""
    for name, record in d1.items():
        total_marks = 0
        n = len(d1[name]["marks"])
        for score in d1[name]["marks"]:
            total_marks += score
        avg_marks = total_marks / n
        if avg_marks > highest_avg:
            highest_avg = avg_marks
            highest_avg_student = name
    print(
        f"The student with highest average marks is {highest_avg_student} with an average of {highest_avg}"
    )


details = {
    "Anirudh": {
        "age": 56,
        "gender": "Male",
        "marks": [3, 455, 64, 33],
        "adult": True,
    },
    "Muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [34, 89, 70, 99, 43],
        "adult": False,
    },
    "Nihar": {
        "age": 24,
        "gender": "Male",
        "marks": [99, 100],
        "adult": True,
    },
}

highest_avg2(details)
