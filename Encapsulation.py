"""
Encapsulation is the process of wrapping data (variables) and methods (functions) into a single unit (class) and restricting direct access to some of the object’s components.
"""
"""
Achieved using private/protected variables (_var, __var).
Provides getter/setter methods to access or modify data."""

class Student:
    def __init__(self, name, marks):
        self.__name = name        # private variable
        self.__marks = marks

    def get_marks(self):         # getter
        return self.__marks

    def set_marks(self, marks):  # setter
        if marks >= 0:
            self.__marks = marks

s = Student("Geetanshi", 85)
print(s.get_marks())        # 85
s.set_marks(95)
print(s.get_marks())        # 95

""""
Abstraction means showing only relevant features and hiding the unnecessary implementation details.
Think of it as "what it does", not "how it does it."
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # abstract method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print(c.area())  # Output: 78.5

"""
Encapsulation	A pill capsule – medicine is hidden inside the shell.
Abstraction	Driving a car – you just use the steering, accelerator, brake without knowing the engine's inner workings.
"""
