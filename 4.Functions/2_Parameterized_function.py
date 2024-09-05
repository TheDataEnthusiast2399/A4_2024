# Parameters and Arguments -->
"""--> We can pass parameters while defining the functions and the arguments at the 
 time of function calls.
 --> We need to maintain the order of parameters and arguments while passing."""


def avg(n1: int, n2: int, n3: int):  # Parameters
    total = n1 + n2 + n3
    print(f"Total of 3 numbers = {total}")


avg(10, 50, 80)
avg(100, 100, 100)  # Arguments
# avg("Hello", "Python", "abc")


# Function named marks
# 5 parameters --> total ---> percentage


def marks(m1: int, m2: int, m3: int, m4: int, m5: int):
    total = m1 + m2 + m3 + m4 + m5
    percent = (total / 500) * 100.0
    print("Total marks scored", total)
    print("Percentage scored", percent)


marks(80, 90, 100, 45, 60)
