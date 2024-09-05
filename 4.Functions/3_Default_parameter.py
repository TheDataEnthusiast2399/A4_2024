# Default Paramters -
"""--> If at the time of function call , argument is not passed then default value of parameter
will be taken into consideration.
--> Default parameters ; values are declared at func declaration.
"""


def marks(sci, math, eng, hindi=10, computer=20):  # Default values at func declaration
    # ....
    print(sci, math, eng, hindi, computer)
    # total = sci + math + eng + hindi + computer
    # print(f"Your total marks = {total}")
    # percentage = total / 5
    # print(f"Your percentage = {percentage}")


marks(30, 50, 60)  # We have not passed marks for hindi and computer
