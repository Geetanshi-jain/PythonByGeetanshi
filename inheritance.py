#inheritance -A class acquire the property of another class or creating its own is called inheritance .
class Parent:
    # parent class
    def display(self):
        print("This is the parent class.")

class Child(Parent):
    # child class inherits from Parent
    def show(self):
        print("This is the child class.")

c = Child()
c.display()  # Inherited method
c.show()     # Own method

"""types of inheritance """
#Single Inheritance -One child inherits from one parent
#Multiple Inheritance -	One child inherits from multiple parents
#Multilevel Inheritance -	Inheritance chain (A → B → C)

#Hierarchical Inheritance -One parent, multiple children
#Hybrid Inheritance -Combination of multiple types
#single inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()
# 2. Multiple Inheritance
class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Art")

class Child(Father, Mother):
    pass

c = Child()
c.skills()

#3. Multilevel Inheritance
class Grandparent:
    def house(self):
        print("Big house")

class Parent(Grandparent):
    def car(self):
        print("Family car")

class Child(Parent):
    def bike(self):
        print("Sports bike")

c = Child()
c.house()
c.car()
c.bike()
# 4. Hierarchical Inheritance
class Parent:
    def work(self):
        print("Parent's work")

class Child1(Parent):
    def play(self):
        print("Child1 plays")

class Child2(Parent):
    def read(self):
        print("Child2 reads")

c1 = Child1()
c2 = Child2()
c1.work()
c2.work()

#super() Keyword
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

c = Child()
c.greet()

# Base class
class A:
    def display(self):
        print("Class A")

# Single Inheritance
class B(A):
    def show(self):
        print("Class B")

# Another base class
class C:
    def info(self):
        print("Class C")

# Multiple Inheritance (B and C)
class D(B, C):
    def message(self):
        print("Class D")
