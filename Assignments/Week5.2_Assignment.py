# Q.1--> Print dictionary with user inputs


def print_dict(n: int) -> dict[str, int]:
    res = {}

    for i in range(n):
        sub_name = input("Enter the name of subject : ")
        sub_marks = int(input("Enter the marks : "))
        res[sub_name] = sub_marks

    return res


sub_no = int(input("Enter the number of subjects: "))
print_dict(sub_no)

# Q.2 : Frequency of integers


def count_frequency(nums: list) -> None:
    res = {}
    max_count = 0
    max_digit = 0

    for i in nums:
        # if i in res:
        #     res[i] = res[i] + 1
        # else:
        #     res[i] = 1
        res[i] = res.get(i, 0) + 1

    for k, v in res.items():
        if v > max_count:
            max_count = v
            max_digit = k

    print(f"The maximum count integer is : {max_digit}")


lst = [4, 5, 6, 5, 4, 4, 7]
count_frequency(lst)


# Q.3 --> Dictionary from given lists


def dict_from_list(sub: list[str], grade: list[int]) -> dict[str, int]:
    res_dict = {}
    for i in sub:
        for j in grade:
            res_dict[i] = j
    return res_dict


subjects = ["history", "maths", "science", "english"]
marks = [45, 63, 16, 77]
print(dict_from_list(subjects, marks))

# Q.4 --> Return true if key is found else false


def find_keys(dicts: dict[str | int, str | int], key: int | str) -> bool:
    if key in dicts.keys():
        return True
    return False


my_dict = {4: 1, "Name": "Alex Hales", "Country": "England", "Strike-rate": 150.49}

k = 4
print(find_keys(my_dict, k))


# Q.5 --> Given two dictionaries, merge two dictionaries


def merge_dict(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    dict1.update(dict2)
    return dict1


dict1 = {"Apple": 3, "Orange": 5, "Banana": 9}
dict2 = {"Banana": 7, "Cherry": 6, "Apple": 11}
print(merge_dict(dict1, dict2))

# Q.6 --> Update value of value by value * user input factor only if values is integer


def update_val(user_dict: dict[str, int], n: int) -> dict[str, int]:

    for k, v in user_dict.items():
        if isinstance(v, int):
            user_dict[k] = v * n
    return user_dict


my_dict = {"a": 3, "b": "Hello", "c": 12, "d": 7.5}
factor = int(input("Enter the factor input: "))

print(update_val(my_dict, factor))

# Q.7 --> To print a dictionary with keys and values


def squares():
    res_dict = {}

    for i in range(1, 16):
        res_dict[i] = i**2
    print(res_dict)


squares()

# Q.8 --> Return string values dict


def str_dict(user_dict: dict[str, int]) -> dict[str, int]:
    res_dict = {}
    for k, v in user_dict.items():
        if isinstance(v, str):
            res_dict[k] = v
    return res_dict


my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "birthday": "May 5",
}

print(str_dict(my_dict))

# Q.9 --> String input -> store frequency -> Print max character


def max_freq_chr(user_str: str) -> None:
    res_dict = {}
    max_freq = 0
    max_chr = ""
    for i in user_str:
        res_dict[i] = res_dict.get(i, 0) + 1
    print(res_dict)

    for ch, f in res_dict.items():
        if f > max_freq:
            max_freq = f
            max_chr = ch
    print(f"The character with maximum frequency is {max_chr}")


my_string = input("Enter the input string : ")
max_freq_chr(my_string)

# Q.10 --> Combine dictionary by adding values


def add_value(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    res_dict = {}

    for key in d1.keys() or d2.keys():
        res_dict[key] = d1.get(key, 0) + d2.get(key, 0)
    return res_dict


dict1 = {"a": 100, "b": 200, "c": 300, "d": 350}
dict2 = {"a": 300, "b": 200, "c": 200, "d": 200}

print(add_value(dict1, dict2))


# Q.11 --> Remove values greater than K, (including mixed values.)


def remove_greater(d1: dict[str, int], k: int) -> dict[str, int]:
    res_dict = {}
    for i, j in d1.items():
        if isinstance(j, str) or isinstance(j, int) and j <= k:
            res_dict[i] = j
    return res_dict


test_dict = {"gfg": 3, "is": 5, "best": 6, "for": 8, "xyz": "CS"}

k = int(input("Enter the factor : "))
print(remove_greater(test_dict, k))
