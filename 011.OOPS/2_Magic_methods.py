"""Magic Methods Or Dunder Methods (because they are surrounded by double 
underscores __), are special methods in Python that allow you to define 
how objects of your class behave in specific situations. 

They enable operator overloading and let you define the behavior of your 
objects for built-in operations, such as addition, comparison,
string representation, etc."""


class Person:
    # __init__ : Initializes the object's state.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Defines the string representation of an object
    def __str__(self):
        return f"{self.name} is {self.age} years old."


p1 = Person("Rachel", 30)  # Directly call init method to set the attributes
print(p1)  # When print is called on object, it calls str method.


class Rectangle:
    def __init__(self, length: float, breadth: float) -> None:
        self.length = length
        self.breadth = breadth

    def __str__(self) -> str:
        return f"Length = {self.length} Breadth = {self.breadth}"

    def area(self) -> float:
        return self.length * self.breadth

    def perimeter(self) -> float:
        return 2 * (self.length + self.breadth)

    def is_square(self) -> bool:
        return self.length == self.breadth


# calls init method
x = Rectangle(10, 10)
y = Rectangle(10, 20)

# calls str method
print(x)
print(y)

# calls area method
print(f"Area of rectangle: {x.area()}")
print(f"Area of rectangle: {y.area()}")

# calls perimeter method
print(f"Perimeter of rectangle: {x.perimeter()}")
print(f"Perimeter of rectangle: {y.perimeter()}")

# calls square method
print(f"Is it a square : {x.is_square()}")
print(f"Is it a square : {y.is_square()}")
