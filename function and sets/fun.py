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


