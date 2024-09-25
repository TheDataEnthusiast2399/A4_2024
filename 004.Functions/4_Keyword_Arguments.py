# Keyword Arguments - Arguments passed at func call paired with parameter and value
# We need not to think about the order of arguments
# Keyword and required arguements can be both used while function call


def marks(sci, math, eng, hindi, computer):
    # ....
    print(sci, math, eng, hindi, computer)
    # total = sci + math + eng + hindi + computer
    # print(f"Your total marks = {total}")
    # percentage = total / 5
    # print(f"Your percentage = {percentage}")


marks(math=99, hindi=100, computer=33, sci=56, eng=91)  # All keywords arguments
marks(
    55, 96, computer=100, eng=99, hindi=77
)  # Combination of required and keyword arguements

print()
