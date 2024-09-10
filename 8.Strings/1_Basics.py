# Q.1 -->
def isLower(chars: str) -> bool:
    for ch in chars:
        if "A" <= ch <= "Z":
            return False
        elif "a" <= ch <= "z":
            return True
    return False


my_string = "57439&%$(*)"
print(isLower(my_string))


# Q.2 -->


def countChar(user_Strings: str) -> None:
    alpha_count = 0
    digits_count = 0
    space_count = 0
    special_count = 0

    for ch in user_Strings:
        if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
            alpha_count += 1
        elif "0" <= ch <= "9":
            digits_count += 1
        elif ch == " ":
            space_count += 1
        else:
            special_count += 1

    print(f"Alphabet count : {alpha_count}")
    print(f"Digits count : {digits_count}")
    print(f"space count : {space_count}")
    print(f"special symbols count: {special_count}")


my_string = "dhaw43789HGDSAK&*(#$  HDK486/*-+daw)"
countChar(my_string)


# Q.3 -->


def ask_char() -> str:
    my_string = ""

    while True:
        user_str = input("Enter a char : ")
        if user_str == "q" or user_str == "Q":
            break
        my_string += user_str

    return my_string


print(ask_char())


# Q.4 -->


def conversion_chr(user_String: str) -> str:
    res = " "

    for ch in user_String:
        ascii_code = ord(ch)
        if ascii_code >= 97 and ascii_code <= 122:
            ascii_code -= 32
            res = res + chr(ascii_code)
        elif ascii_code >= 65 and ascii_code <= 90:
            ascii_code += 32
            res = res + chr(ascii_code)
        else:
            res = res + ch

    return res


my_string = "DHhdjka^&#$(*)$   ...///;;''DADWAHKjyuihdwakj"
print(conversion_chr(my_string))

