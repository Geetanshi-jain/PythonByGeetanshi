""" Polymorphism in Python
Polymorphism means “many forms”.
In object-oriented programming, polymorphism allows the same function or method name to behave differently based on the object that calls it."""
class Vehicle:
    def run(self):
        print("Vehicle is running")

class Car(Vehicle):
    def run(self):
        print("Car is running")

v = Vehicle()
v.run()   # Vehicle is running

c = Car()
c.run()   # Car is running (overrides Vehicle)


class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student(85)
s2 = Student(90)

print(s1 + s2)  # Output: 175



