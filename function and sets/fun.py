def function(name):
    print("my name = ",name)
function("Geet")

# diffrent type of argument in py

# Positional argument 
def function(name,age):
    print("my name is ")

#keyword argument 
def keyargs(name = "xyz",age =20 ):
    print("my name is = "+name,"age = ",age)
function("geet",19)
keyargs(name= "abc",age= 18)

# value return in function 
def valuereturninFun():
    return "geetanshi jain"
print(valuereturninFun())


# types of variables in python 
#local variable - when we declare a function inside a function 
# we can call them a local varible we can not access them outside the function .
def  msg():
    msg= "hello"
    print(msg)

msg()

def msg():
    a= "hello"
    return a 
b= msg()
print(b)

# global varible - we can access a global variable inside a function and out side a function 
 # a variable declare outside a funtion is called as  global varible 
a="hello"
def msg():
    print("inside ",a)
msg()
print(a)
# using global variable we create a glb variable 
def msg():
    global a  # Declare 'a' as global
    a = "Mca"
    print("Inside function, a =", a)

print("Global a before function call:", a)  # Prints the global variable 'a'
msg()  # Modifies the global variable 'a'
print("Global a after function call:", a)  # Now 'a' has the value changed inside the function

"""
1.when we create a variable inside a function it is local by default.
2. when we define a variable outside a function it is global by defult 
3we use a gobal keyword to modify a global varible inside a function . 

"""
# Nonlocal variable 
def outer():
    a = "outer variable"

    def inner():
        nonlocal a  # Refers to 'a' in the outer function
        a = "inner variable"
        print("Inside inner, a =", a)

    print("Before calling inner, a =", a)
    inner()
    print("After calling inner, a =", a)

outer()


