print("hello pythan")
# literals Constant in pythan 
#numerical literals -integer,floating,complex
a= 12
b=12.3
c= a+4j
print(a,b,c)
#character literals
A= 'a'
B='b'
print(A,B)
#string literal
abc= "khushbu"
print(abc)

#boolean literals
true =True
false =False
print(true,false)
#special literals
N =None
print(N)
#collection literal
list =[2,3,41,1]
tuple= ('a','b','c','d')
set ={12,13,13,15}
dictionary= {'name':"Geet",'lname':"jain"}
print(list ,set,tuple,dictionary)
# types of variable in python
#local and global variable 
b=10 #global var
def localvar():
    a=2
    print(a) #local variable

print(b)
localvar()
#Data types in pythan
"""
There are different types of data types in Python. Some built-in Python data types are:

Numeric data types: int, float, complex
String data types: str
Sequence types: list, tuple, range
Binary types: bytes, bytearray, memoryview
Mapping data type: dict
Boolean type: bool
Set data types: set, frozenset """
# numeric dT
a =10 # integer 
b=10.9 # float 
c= 1+2j # complex
print (a ,b, c)
# String DT 
str ="Geet"
print(str)
#sequance type 
list=[12,1,31,4,5]
tuple =(12,13,14,15,'abc','A')
set ={1,23,6,8}
#boolean types
bool =True
print(bool)
#binary type -A bytestring is what it says it is simply a string of bytes, for example ‘© ? ?’ in ‘utf-8’ is 

byte =b'\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83'.decode('utf-8')
print(byte)
#mapping DT
dic={"name: geet","lname:jain" }
print(dic)








