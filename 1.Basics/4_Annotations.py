name: str = "Jack Brown"
age: int = 43
genre: str = "Murder Mystery"
print(type(name))
print(type(age))
print(type(genre))

"""Now we should not change the datatype of the above mentioned variables. Although python will
allow this due to its dynamic nature but it should not be practiced to maintain the 
"""

account: str | int = "aGJK43243"  # Combination of integer or string
print(type(account))  # Type -> str
account = 9988
print(type(account))  # Type > Integer

"""---> Just for code readability/practice we use annotations ; makes sure we don't change the datatype of 
variable while coding. 
"""
