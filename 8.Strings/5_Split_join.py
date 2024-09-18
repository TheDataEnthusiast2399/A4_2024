"""split() --> Return a list of the substrings in the string, using sep as the separator string."""

x = "Python has past \nlibraries."
# print(x.split(" ")) # seperator -> whitespace
print(x.split("\n"))  # seperator -> \n

"""join() --> Concatenate any number of strings from the list of strings with seperator."""
y = ["P", "y", "t", "h", "o", "n"]
res = ("-").join(ch for ch in y)
# res = "-".join(ch + "5" for ch in y)

print(res)
