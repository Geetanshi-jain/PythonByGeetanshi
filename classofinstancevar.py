#Instance Variable
"""Belongs to: A specific object/instance of the class.

Defined in: Usually inside the __init__() method.

Unique for each instance."""

class Student:
    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Geetanshi")
s2 = Student("Shristi")

print(s1.name)  # Geetanshi
print(s2.name)  # Shristi

"""Class Variable
Belongs to: The class itself (shared by all instances).

Defined in: Directly inside the class, but outside any methods.
"""
class Student:
    school = "IIPS DAVV"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Geetanshi")
s2 = Student("Shristi")

print(s1.school)  # IIPS DAVV
print(s2.school)  # IIPS DAVV
