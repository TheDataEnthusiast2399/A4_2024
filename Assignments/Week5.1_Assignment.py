# Q.1 --> Reverse the given string


def rev_str(users: str) -> str:
    my_string = ""
    n = len(users)
    for ch in range(n - 1, -1, -1):
        my_string += users[ch]

    return my_string


x = input("Enter the input : ")
print(rev_str(x))


# Q.2 --> Return the string in uppercase


def upper_Case(users: str) -> str:
    res_str = ""
    for ch in users:
        if "a" <= ch <= "z":
            ch = chr(ord(ch) - 32)
            res_str += ch
        else:
            res_str += ch
    return res_str


x = input("Enter the input string : ")
print(upper_Case(x))

# Q.3 --> Remove the vowels from the string


def no_vowels(users: str) -> str:
    res_str = ""
    for ch in users:
        if ch not in "aeiouAEIOU":
            res_str += ch
    return res_str


x = input("Enter the input string : ")
print(no_vowels(x))


# Q.4 --> Count number of words --> input string only contains alphabets and spaces


def word_count(users: str) -> int:
    count = 0
    for ch in users:
        count += 1
    return count


x = input("Enter the input string : ")
print(word_count(x))


# Q.5 --> Function that return longest word in a given string


def longest_word(users: str) -> str:
    longest_word = ""
    current_word = ""

    for ch in users:
        if "a" <= ch <= "z" or "A" <= ch < "Z":  # If characters --> add in current word
            current_word += ch
        else:
            if len(current_word) > len(longest_word):
                longest_word = current_word
            current_word = ""  # Reset current word

    if len(current_word) > len(longest_word):  # To compare the length of last word
        longest_word = current_word

    return longest_word


x = input("Enter the input string : ")
print(longest_word(x))


# Q.6 --> Capitalizes the first word in a given string


def capitalise_first(users: str) -> str:
    res_str = ""
    is_new = True

    for ch in users:
        if is_new and "a" <= ch <= "z":
            res_str += chr(ord(ch) - 32)
            is_new = False
        else:
            res_str += ch
        if ch == " ":
            is_new = True
    return res_str


x = input("Enter the input string: ")
print(capitalise_first(x))


# Q.7 --> To replace all consonants with aestricks(*)


def replace_consonants(users: str) -> str:
    res_str = ""
    for ch in users:
        if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
            if ch in "aeiouAEIOU":
                res_str += ch
            else:
                res_str += "*"
        else:
            res_str += ch
    return res_str


x = input("Enter the input string : ")
print(replace_consonants(x))


# Q.8 --> Function that removes non-alphabetic characters from the string


def remove_nonAlpha(users: str) -> str:
    res_str = ""
    for ch in users:
        if "a" <= ch <= "z" or "A" <= ch <= "Z":
            res_str += ch
    return res_str


x = input("Enter the input string : ")
print(remove_nonAlpha(x))

# Q.9 --> Function that counts no of digits


def count_digits(users: str) -> int:
    count = 0
    for ch in users:
        if "0" <= ch <= "9":
            count += 1
    return count


x = input("Enter the input string : ")
print(count_digits(x))

# Q.10 --> Function that removes duplicate character from a string


def remove_duplicates(users: str) -> str:
    res_str = ""
    for ch in users:
        if ch not in res_str:
            res_str += ch
    return res_str


x = input("Enter the input string: ")
print(remove_duplicates(x))

# Q.11 --> Function that checks only alphanumeric character from string


def alpha_num(users: str) -> bool:
    for ch in users:
        if not ("a" <= ch <= "z" or "A" <= ch <= "Z" or "0" <= ch <= "9"):
            return False
    return True


x = input("Enter the input string : ")
print(f"The given string is alphanumeric : {alpha_num(x)}")

# Q.12 --> Function that replaces all spaces with hyphen


def hyphen_spaced(users: str) -> str:
    res_str = ""

    for ch in users:
        if ch == " ":
            res_str += "-"
        else:
            res_str += ch

    return res_str


x = input("Enter the input string: ")
print(hyphen_spaced(x))
