a = "Strings are immutable in nature99!!"

"""isupper() -> Returns True if uppercase """
# print(a.isupper())

"""islower() -> Returns True if lowercase """
# print(a.islower())

"""isalpha() -> Returns True if every string is alphabetic"""
# print(a.isalpha())

"""isalnum() -> Returns True if string is alphanumeric(with atleast one alphabet and no special char and no whitespaces)"""
# print(a.isalnum())

"""isdigit() -> Returns True if every string is digit(0-9)"""
# print(a.isdigit())

"""upper() -> converts every string in uppercase."""
# x = a.upper()

"""lower() -> converts every string in lowercase."""
# x = a.lower()

"""title() -> capitalizes every first character after whitespace."""
# x = a.title()

"""capitalize() -> converts the first character have upper case and the rest lowercase."""
# x = a.capitalize()

"""startswith() -> Checks if the string starts with given arguments 
(start/end index optional), return boolean value."""
# x = a.startswith("s")
# x = a.startswith("t", 1, 4)

"""endswith() -> Checks if the string starts with given arguments 
(start/end index optional), return boolean value."""
# x = a.endswith("rld")
# x = a.endswith("a",8)

"""index() -> Returns the first index value of string if present"""
# x = a.index("i")

"""find() -> Returns the first index value of string/sequence if present """
x = a.find("immutable")
print(x)
x = a.find("!")
print(x)
