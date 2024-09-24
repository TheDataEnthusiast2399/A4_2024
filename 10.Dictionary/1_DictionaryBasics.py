"""
Dictionaries are mutable, unordered collections that store data in key-value pairs. 
"""

# Using curly braces
my_dict1 = {"name": "Alice", "age": 30, "city": "New York"}

# Using dict() function
my_dict2 = dict(name="Rhodeo", age=32, city="New York")

print(my_dict1)
print(my_dict2)

print(type(my_dict1))  # class dict

"""Keys are unique entities in dictionaries, if you enter duplicate keys,
last entered value for the key will only be recorded."""

my_dict1 = {"name": "Alice", "age": 30, "age": 38, "city": "New York"}
print(my_dict1)

"""Operations in dictionary """
# Accessing values :
"""We can access values through their keys"""
print(my_dict1["name"])
print(my_dict2["name"])

# Adding / Updating Key-value pairs:
my_dict1["age"] = 31  # Update existing value
my_dict2["job"] = "Engineer"  # Add new key-value pair

print(my_dict1)
print(my_dict2)

# Iterating in dictionary:
my_dict1 = {
    "roll_no": 1,
    "name": "Michael Theodore",
    "grade": "fourth",
    "school": "Disney school of entertainment",
}
# Iterating over keys:
"""
keys(): Iterate over keys.
values(): Iterate over values.
items(): Iterate over key-value pairs
"""
for key in my_dict1:
    print(key)

# Iterating over values
for value in my_dict1.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict1.items():
    print(f"{key}: {value}")


# Removing key-value in dictionary:

del my_dict2["city"]  # Remove 'city'
age = my_dict2.pop("age")  # Remove 'age' and return its value

# popitem() removes the last inserted key-value pair
last_item = my_dict2.popitem()

my_dict2.clear()  # Remove all key-value pairs
