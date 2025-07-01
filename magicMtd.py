#Magic Methods in Python (also called Dunder methods)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student Name: {self.name}, Marks: {self.marks}"

    def __add__(self, other):
        return self.marks + other.marks
         
    def __del__(self):
     print("Object deleted")

s1 = Student("Alice", 85)
s2 = Student("Bob", 90)

print(s1)              # __str__
print(s1 + s2)         # __add__
del s1