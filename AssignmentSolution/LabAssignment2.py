
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()


#2. 
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
        j=j+1
    print()


#3.
a='A'
for i in range(1,6):
    for  j in range(1,i+1):
        print(a,end= " ")
       
    print()
    a=chr(ord(a)+1)
    
#4. 
for i in range(5,0,-1):
    for j in range(i):
        print("*",end= " ") 
    print()

#5.
ctn=1
for i in range(5,0,-1):
    for j in range(i):
        print(ctn,end= " ") 
        ctn=ctn+1
    print()
    ctn=1


#7.
#        * 
#      * * *
#    * * * * *
#  * * * * * * * 

for i in range(5):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

""" 7.
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 7 6 5 4





"""

n = 5  

for i in range(1, n + 1):
   
    print(' ' * (n - i), end='')

    
    for j in range(i, 2 * i):
        print(j, end=' ')

   
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end=' ')

    
    print()

# 7. * * * * * 
#      * * *
#        *

for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")

    for j in  range(2*i-1):
        print("*",end=" ")
    print()


#        * 
#      * * *
#    * * * * *
#  * * * * * * * 
#    * * * * *  
#      * * *
#        *


for i in range(5):
    for j in range(5-1-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")

    for j in  range(2*i-1):
        print("*",end=" ")
    print()

"""
9.
           1
         1   1
       1   2   1
     1   3   3    1
   1  4    6   4   1
 1  5   10   10  5   1 


"""

"""10.
1
2 3
4 5 6
7 8 9 10
"""
ctn=1
for i in range(1,5):
    for j in  range(i):
        print(ctn,end=" ")
        ctn+=1
    print()

"""
10. program to check prime no
  
    """
num= int(input("enter a number"))
flg=0
for i in range(2,num):
    if(num%i==0):
       flg =1
if(flg==1):
    print("print no is not prime ")
else:
    print("no is prime")

"""
11.
factorial of a number
"""
num =int(input("enter a number"))
if(num>0):
    fact=1
    for i in range(num):
     fact+=fact*i
    print("ans = ",fact)
else:
    print("invalid number pls put a positive number")



"""factorial using recursion"""
def factorial(num):
    if num==0 :
        return 1
    else:
        return num*factorial(num-1)
ans = factorial(9)
print("ans = ",ans)

"""
program to check palindrone no
"""
n = int(input("enter number"))
plnum=n
while(n>0):
    dig =n%10
    ans=10*dig+dig
    n=n/10
if(plnum==ans):
    print("Number  is palindrone")
else:
    print("number is not palindrone")

"""
program to print ASCII value
"""
def Asscii(ch):
    return int(ord(ch))
print(Asscii('C'))

""" Fibbonacci series"""
def fibbonacci(num):
    x = 0
    y = 1
    print(x,y,end=" ")
    for i in range(num - 2):
        z = x + y
        print(z, end=' ')
        x = y
        y = z
fibbonacci(5)

"""count no of digits"""
# Python code to count the number of digits in a number
num = int(input("Enter a number: "))
count = 0

# Ensure the input number is positive
if num == 0:
    count = 1
else:
    while num > 0:
        num //= 10  
        count += 1  
print("Number of digits:", count)


"""REverse an integer
"""
integer =int(input("enter a number"))
reversenum=0
remainder=0
while(integer>0):
    remainder=integer%10
    reversenum =reversenum*10+remainder
    integer//=10

print(reversenum)
"""check armstrong number of 3 digits"""

num=int(input("enter anumber"))
res=0
n=num
while num>0:
    rem=num%10
    res+=rem*rem*rem
    num/=10
if(res==n):
    print("number is armstrog")
else:
    print("no is not armstrong")

"power of a number using while loop"
base =2
exponent =3
res=1
while exponent!=0:
    res*=base
    exponent=exponent-1
print("Answer = ",res)

"pow() function used"
print(pow(12,2))