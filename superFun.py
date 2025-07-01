#In Python, the super() function is used to call methods from a parent or superclass. It is especially useful in class inheritance
class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    def show(self):
        super().show()  # Call the parent class method
        print("This is the child class")

obj = Child()
obj.show()

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person name is {self.name}")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)  # Calls Person's constructor
        self.roll = roll
        print(f"Student roll number is {self.roll}")

s = Student("Geetanshi", 101)

#multiple inheritance
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")
        super().show()

class C(B):
    def show(self):
        print("Class C")
        super().show()

c = C()
c.show()
