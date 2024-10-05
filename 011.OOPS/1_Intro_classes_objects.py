"""
A class is a blueprint or template for creating objects. It defines the properties
(attributes) and behaviors (methods) that the objects created from it will have.
"""

"""
An object is an instance of a class. It represents a specific entity with the 
properties and behaviors defined in the class.

Every object is an independent entity, it cannot directly access another object 
in the class.
(until the mechanism is designed in the class for object to access other object)
"""


class Dog:
    def __init__(self, name, breed, color):  # Magic or dunder method
        self.name = name  # Attribute 1
        self.breed = breed  # Attribute 2
        self.color = color  # Attribute 3

    def bark(self):  # Method 1
        print(f"{self.name} says Woof!")

    def dog_color(self):
        print(f"{self.name} is {self.color} in color")


# Create an object of Dog class
my_dog1 = Dog("Enzo", "Golden Retriever", "White")
my_dog2 = Dog("Ginger", "Spaniel", "Golden Yellow")

# Accessing address of object
print(my_dog1)
print(my_dog2)
print()

# Access attributes and methods
print(f"Dog name : {my_dog1.name}")  # Accessing attribute1
print(f"Dog breed: {my_dog1.breed}")  # Accessing attribute2
print()

print(f"Dog name :{my_dog2.name}")  # Accessing attribute1
print(f"Dog breed:{my_dog2.breed}")  # Accessing attribute2
print()

my_dog1.bark()  # Accessing Method1
my_dog2.bark()  # Accessing Method1
print()

"""
a) self refers to the instance of the class in object-oriented programming (OOP).
b) It is used within class methods to access instance variables and methods. 
c) It acts as a reference to the object calling the method, allowing each instance to maintain its own data.
"""

my_dog1.dog_color()  # All the attributes of first object will access the respective class methods
my_dog2.dog_color()  # All the attributes of second object will access the respective class methods


class Student:
    def setDetails(self):  # Acts as a initializer which sets attributes
        self.idd = int(input("Enter the ID no : "))
        self.name = input("Enter the student name : ")
        self.age = int(input("Enter the age of student : "))
        self.gender = input("Enter the gender of student (M/F): ")
        self.location = input("Enter the location of student : ")
        grade = int(
            input("Enter class : ")
        )  # Local variable can't be accessed anywhere else

    def displayDetails(self):  # Method for displaying attributes
        print()
        print("---Student Information----")
        print(f"Student Id :{self.idd}")
        print(f"Student Name:{self.name}")
        print(f"Student age :{self.age}")
        print(f"Student gender :{self.gender}")
        print(f"Student location :{self.location}")


s1 = Student()  # First Object
s2 = Student()  # Second Object

# First object accessing class method
s1.setDetails()
s1.displayDetails()

# Second object accessing class method
s2.setDetails()
s2.displayDetails()
