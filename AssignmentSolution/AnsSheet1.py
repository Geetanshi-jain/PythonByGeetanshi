num1= int(input("enter first  number"))
num2= int(input("enter secand number"))
num3= int(input("enter third number"))
if(num1>num2 and num1>num3 ):
    print(" num1 is greatest number")
elif(num2>num1 and num2>num3):
    print("num2 is greates number")
else:
    print("num3 is gratest number")

# 2.	Write a python program whether a number is positive negative or zero. 

num=int(input("enter number"))
if(num>0):
    print("numbber is positive")
elif(num<0):
    print("number is negative")
else:
    print("number is Zero")

    #3.	Write a python program to check whether a number is divisible by 11 or not. 
    num =int(input("enter a number"))
    if(num%11==0):
        print("number is divisible by 11")
    else:
        print("number is not divisible by 11")

        #4 4.	Write a python program to check whether a number is even or odd using conditional statement and using for and while loop. 

num=int(input("enter a number"))
if(num%2==0):
    print("number is  even")
else:
    print("number is odd")
    #5.	Write a python program to check whether a year is a leap year or not. 
    num =int(input("enter a number"))
if((num%4==0 and num%100==0) or (num%400==0)):
    print("number is leap year")
else:
    print("number is not leap year ")
#6.	Write a python program to calculate profit or loss. 
    sp =int(input("enter selling price"))
    cp=int(input("enter cost price"))
    if(sp-cp>0):
        print("you are in profit your profit is"+(sp-cp))
    elif(sp-cp<0):
        print("you are in loss"+(cp-sp))
    else:
        print("you are in ideal condition no profit and loss")
    #7.	Write a python program to calculate grades of a student. 
marks =int (input("enter marks"))
if marks>90:
    print(" O grade")
elif(marks>=80 and marks<90):
    print("A+ grade")
elif(marks>=70 and marks<80):
    print("A grade")
elif(marks>=60 and marks<70):
    print(" B+ grade")
elif(marks>=50 and marks<60):
    print(" B grade")
elif(marks>=40 and marks<50):
    print(" c grade")
else:
    print("fail")
#8.	Write a python program to check whether a person is eligible for loan or not if he is having salary more than 50k and 3 years of experience. 
salary= int(input("enter a salary "))
experience = int(input("enter experience"))

if (salary>50000 and experience >3 ):
    print("you are eligible for   loan ")
else:
    print("not eligible for loan ")

    #9.	Write a python program to find the area and volume of sphere. 
r =int(input("enter radius"))
v=4/3*22/7*r**3
print("volume of sphere "+v)
#10.	Write a python program to display the data type.
a =12
b =1.2
c='str'
d=3+4
e = [1,2,3]
f=(1,2,3)
g= {"a":1}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

#11.	Write a python program to demonstrate all operators – 
#	Arithmetic Operators 
#	Assignment Operators 
#	Comparison Operators 
#	Logical Operators 
#	Bitwise Operators 
#	Special Operators 

#Arthmatic 
print(10+20)
print(10-20)
print(10*20)
print(10/20)
print(10//20)
print(10**20)
# Assignment
a=10 #simple
b=c=d=10 #chained
a+=10 #compound
b-=33
## Comparision operator
print(10==10)
print(10<20)
print(40>10)
#logical operator
print( 10>19 and 20<10)
print(10!=3)
print( 12>9 or 9<2)
# bit wise operator
print(10000&123)
print(1000|200)
print(~123)
#special operator 
#identity
a=12
b=12
print(a is 12)
print(b is 12)
#membership operator
list =[12,2,3,2,1,4]
print(12 in list)
print(12 not in list)
 #12 .	Write a python program to swap two numbers.
a=10
b=20
c =a 
a=b
b=a
print("a = "+a)
print("b =",b)
# without using third variable
a=5
b=10
a=a+b
b=a-b
a=a-b
print("a =  ",a ,"b  = ",b)
#13.	Write a python program to calculate simple interest. 
p =int("enter principal ")
r =int(input("enter rate"))
t=int(input("enter time"))
print(' si = ',(p*r*t)/100)

#14.	Write a python program to check whether a number is Armstrong or not.
number =int(input("enter number"))
armno =number
while(number<0):
    rem =number%10
    sum+=rem*rem*rem
    number= number/10

if(number==armno):
    print("number is armstrong")
else:
    print("not armstrong")

#15	Write a python program to calculate the sum of n natural numbers. 
n= int(input("enter number"))
print("sum = ",n*(n+1)/2)

#16.	Write a python program to print the Fibonacci sequence. 
a=0
b=1
c=1
print(a, b )
n=2
while(n<10):
    c=a+b
    print(c)
    a=b
    b=c
    n=n+1

# 17.	Write a python program to check whether a number is prime or not. 
no =int(input("enter anumber"))
flg=0
for i in range(2,no):
    if(no%i==0):
        flg =1
if(flg ==1):
    print("no is not prime number")
else:
    print("number is prime no")

   #18.	Write a python program to calculate the sum of first 50 odd and even numbers.
    print("sum of  odd number =",50*50)
    print("sum of  even number =",50*51)
#19. Write a python program to find a factorial of a number. 
factorial  =int(input("enter   the number which you have try to found out the factorial"))
fact=1
for i in range (factorial):
    fact+= fact*i
print(fact)

#20.	Write a python program to count number of digits in given number. 
a =int(input("enter a number"))
count= 0
while(a>0):
    dig =a%10
    count+=1
    a=a//10
print(count)
   #21.	Write a python program to find the sum of digits of a given number. 
    
a =int(input("enter a number"))
count= 0
sum=0
while(a>0):
    dig =a%10
    sum+=dig
    a=a/10

print("sum of number ="+sum)

#22.	Write a python program to print a table of a number using for and while loop. 
for i in range(1,11):
    print(4*i)
    print()

#23.	Write a python program to print a table of a number using for and while loop. 

for i in range(1,11):
    print(i)
    if(i==7):
        break

    def myfun():
        pass #for future reference

myfun()










