"""
ASCII (American Standard Code for Information Interchange) is a character encoding 
standard used to represent text in computers and other devices that use text. 
It assigns a unique numerical code to each character, 
including letters, digits, punctuation marks, and control characters.
"""

"""
ord() -> To get ASCII value of character.
chr() -> To get character associated with an ASCII code.
"""

# Get the ASCII value of a A
print(ord("A"))

# Get the character from an ASCII value 65
print(chr(65))

"""Convert lowercase to uppercase using ASCII code"""


def upper(x: str) -> str:
    res = ""
    for i in x:
        if 97 <= ord(i) <= 122:  # Lower case 97-122 / Upper case 65-90
            res += chr(ord(i) - 32)
    return res


s1 = "obNoxioUSgroUPAthernaz"
print(upper(s1))


"""Swapcase from lowercase to uppercase and vice-versa"""


def swapcase(x: str) -> str:
    res = ""
    for i in x:
        if 97 <= ord(i) <= 122:  # Upper to lower
            res += chr(ord(i) - 32)
        elif 65 <= ord(i) <= 90:  # Lower to upper
            res += chr(ord(i) + 32)
        else:  # Special character, blankspaces.
            res += i
    return res


s1 = "DHhdjka^&#$(*)$   ...///;;''DADWAHKjyuihdwakj"
print(swapcase(s1))
