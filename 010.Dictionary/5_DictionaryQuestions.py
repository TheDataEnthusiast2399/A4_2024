"""Find the maximum element repeated and it's frequency from the list."""

my_list = [1, 2, 3, 1, 5, 1, 7, 4, 5, 6, 7, 8, 9]
my_dict = {}

for num in my_list:
    my_dict[num] = my_dict.get(num, 0) + 1

print(my_dict)
max_freq = 0
max_element = 0
for key in my_dict:
    if my_dict[key] > max_freq:
        max_freq = my_dict[key]
        max_element = key

print(f"Maximum repeated integer : {max_element}")
print(f"Maximum frequency : {max_freq}")

"""Find the maximum element and it's frequency from the string"""

my_string = "ahgghgtzzhjsklhhhgaaaaaauaa"
my_dict = {}

for char in my_string:
    my_dict[char] = my_dict.get(char, 0) + 1

print(my_dict)
max_freq = 0
max_element = 0
for key in my_dict:
    if my_dict[key] > max_freq:
        max_freq = my_dict[key]
        max_element = key

print(f"Maximum repeated character : {max_element}")
print(f"Maximum frequency : {max_freq}")
