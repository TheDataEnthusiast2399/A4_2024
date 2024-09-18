"""Find the count of 'i' in the given string (upper/lowercase combined)."""

a = "BoohemiiiIIAN"

count = 0
for ch in a:
    if ch == "i" or ch == "I":
        count += 1

print(count)

"""Find vowels in the given string"""
my_string = "aeghbioudhANIOU"

total = 0
for ch in my_string:
    # for ch in my_string.lower():
    # if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    #     total += 1
    if ch in "aeiouAEIOU":
        total += 1

print(total)

"""Remove all the symbols,digits, spaces from a string."""

my_string = "_ASBabccrrhgja%b@c9d_e.fk)  921(ds!@#ffgtyzzZXCzz12hh"
result = ""

for ch in my_string:
    if (ord("a") <= ord(ch) <= ord("z")) or ord("A") <= ord(ch) <= ord("Z"):
        result += ch

print(result)
"""
Keep on asking characters from the user.

Stop it unitil he/she presses q


Enter char = r
Enter char = 1
Enter char = p
Enter char = l
Enter char = q
"""


def askchars() -> str:
    my_string = ""
    while True:
        char = input("Enter the character = ")
        if char == "q" or char == "Q":
            break
        my_string += char

    return my_string


"""Distinguish and count characters on the basis of alphabets, digits, symbols and whitespaces"""


def countchar(x: str) -> None:
    alphabets = 0
    digits = 0
    spaces = 0
    special_char = 0

    for chr in x:
        if 65 <= ord(chr) <= 90 or 97 <= ord(chr) <= 122:
            alphabets += 1
        elif ord("0") <= ord(chr) <= ord("9"):
            digits += 1
        elif ord(chr) == ord(" "):
            spaces += 1
        else:
            special_char += 1

    print(f"Alphabet count : {alphabets}")
    print(f"Digits count : {digits}")
    print(f"Spaces count : {spaces}")
    print(f"Special characters count : {special_char}")


my_string = "ASDDHhdjka^099&#$(*)$   ...///;;''99234DASADWAHKjyuihdwakj"
countchar(my_string)

"""Count the number of the words in a given string"""

my_string = "John wick is the best assasin in the generation."

# ans = my_string.split()
# print(ans)
# print(len(ans))

print(len(my_string.split()))

"""Reverse the given string"""

my_string = "python is a good language"

words = my_string.split()
# print(words)

# words.reverse() -> reverse() : reverse any given string.
words = words[::-1]
# print(words)

ans = " ".join(word for word in words)
print(ans)

"""Reverse the given string --> Reverse individual string and concatenate 
my_string = "python is a good language"
res = nohtyp si a doog egaugnal"""

my_string = "python is a good language"

words = my_string.split()
print(words)

print(" ".join(word[::-1] for word in words))
