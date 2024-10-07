# Create a function with different types of arguments with example.

def display(a=5,b=8):      # default argument 
    print(a,b)

def display1(a,b):       # positional argument
    print(a,b)

def display2(a,b,c):     # keyword argument
    print(a,b,c)

def display3(*arg):      #arbitrary argument
    print(arg)

display(3)   # calling default argument fn
display1(2,5) # calling positional argument fn
display2(b=2,a=1,c=3)  # calling trough keyword argument
display3(2,4,7,6)    # calling arbitry function
 

 #2. write a program that can simulate the rolling of dice. The program should randomly generate
# two numbers in the range of 1 through 6 and display them.
import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print(f"dice 1 =>{dice1} and dice 2 => {dice2}")

#3 Write program that simulate ten tosses, one after the other. Each time the program
# simulates a coin toss, it should randomly display either “Heads” or “Tails”.

l=("Head","Tail")

for i in range(10):
    print(f"No. of toss {i+1} and result is {random.choice(l)}")

#4. Write program demonstrates the sqrt function.
import math
print(math.sqrt(16))

#5. Write program calculates the length of a right triangle's hypotenuse using function andmodule.

def hypotenuse(base,height):
    return math.sqrt(base*base+height*height)

hyp = hypotenuse(3,4)
print( "hypotenuse of given tringle is",hyp)

#6. Create a function having different kinds of variables. ie. Local, global, and nonlocal variable.

name = "Geetanshi " #globle variable
def fun1():
    name = "jain"  # local variable
    print("local variable inside fun1 =>",name)
    def fun2():
        nonlocal name 
        name = "Geet"
        print( "non local variable inside fun2 =>",name)
    fun2()
    print("variable outside fun2 after modifying through nonlocal keyword =>",name)
fun1()
print("global variable =>",name)

#7. Write a program to calculate sum of n natural numbers using recursive function

def sum(n):
    if n<=0:
        return 0
    return n + sum(n-1)

print(sum(5))

#8. Write a program to find the factorial of a numbers using recursive function

def fact(n):
    if n<=0:
        return 1
    return n*fact(n-1)

print(fact(4))

#9. Write a program to print the Fibonacci series up to a given numbers using recursive function.

def fib(n,a=0,b=1):
    if n <= a:
        return
    print(a)
    c = a+b
    a=b
    b=c
    fib(n,a,b)

fib(10) # print fibonacci upto 10

# 10. Create a list to hold the sales for each day (number of days are 5) using function.

l=[] #empty list
def holdsell():
    day = int(input("enter no. of days for hold sell "))
    for i in range(day):
        l.append(int(input("enter sell amount ")))
    print("total sells day wise",l)

#holdsell()

# 11. Write program to append the elements until the user wants.
list=[]
def append_ele():
    while True:
        list.append(input("enter element for appending  "))
        if "y" != input("enter y for continue appending  "):
            break
    print("your elements are ",list)
#append_ele()

#12. Write a Python function to sum all the numbers in a list.
def sum_list(list):
    sum=0
    for i in list:
        sum+=i
    return sum

list = [4,5,1,5,7]
print("sum of list element is ",sum_list(list))

# 13 Write a Python function to calculate the factorial of a number (a non-negative integer). The
#function accepts the number as an argument.

def fact(n):
    if n<=0:
        return 1
    return n*fact(n-1)

n = int(input("enter positive integer for factorial "))
if n > 0:
    print(fact(n))
else:
    print("plz enter a valid number")


# 14 Write a Python program to access a function inside a function.
def outer():
    print("outer fun")
    def inner():
        print("inner fun")
    inner()
outer()