from typing import Dict

marks: Dict[str, int] = {
    "history": 78,
    "science": 16,
    "computer": 99,
    "chemistry": 65,
    "sst": 25,
}
print(marks)

# To get the values of particular keys in dictionary
print(marks["history"])
print(marks.get("chemistry", 0))  # get() -> returns the value if present , otherwise 0

# removes the key-value from dictionary
marks.pop("history")
print(marks)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 1, "d": 4, "a": 100}

# Union of two dictionaries
res = dict1 | dict2
dict1.update(dict2)
print(res)
print(dict1)
