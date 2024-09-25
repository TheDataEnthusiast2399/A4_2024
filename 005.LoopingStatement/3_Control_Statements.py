"""
--> Control statements are designed to serve the purpose of modifying 
a loop's execution from its default behaviour.

--> If-else statements: They are mostly used to control the behaviour of loops.
--> Break : Stops execution and bring control out of the loops.
--> Pass : Its simply empty loop. Pass statements are not ignored like comments, it just results
as no operation.
--> Continue: (skips the below part of the code and moves to next loop).
"""


def break_statements(n):
    i = 1

    while i <= n:
        if i == 5:
            break
        else:
            print(i)
        i += 1


break_statements(10)  # Stops execution once i = 5 and breaks out of the loop


def continue_statements(n):
    i = 1
    while i <= n:
        print("Print no", i)
        if i == 3:
            continue
        i += 1


continue_statements(
    10
)  # Skips statements under it once i = 3, hence making the program never ending


def pass_statements(n):
    pass
    print("This will execute")


pass_statements(3)
