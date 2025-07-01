"""
1. Instance Method (Most common)
Belongs to: An object (instance of a class).

First parameter: self (refers to the instance).

Can access: Instance variables and class variables.
"""
class Student:
    def __init__(self, name):
        self.name = name

    def user_name(self):  # instance method
        print(f"Hello, I am {self.name}")

s1 = Student("Geetanshi")
s1.user_name()  # Output: Hello, I am Geetanshi

""" 2. Class Method
Belongs to: The class.

First parameter: cls (refers to the class).

Can access: Class variables (but not instance variables directly).

Defined with: @classmethod decorator.
"""

class Student:
    school = "IIPS DAVV"

    @classmethod
    def get_school(cls):  # class method
        return cls.school

print(Student.get_school())  # Output: IIPS DAVV

"""Static Method
Belongs to: The class (but doesn't need class or instance).
Defined with: @staticmethod decorator.
No self or cls parameter.
"""
class Student:
    @staticmethod
    def is_adult(age):  # static method
        return age >= 18

print(Student.is_adult(20))  # Output: True

