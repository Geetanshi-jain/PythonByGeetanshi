num1= int(input("enter 3 number"))
num2= int(input("enter 3 number"))
num3= int(input("enter 3 number"))
if(num1>num2 and num1>num3 ):
    print(" num1 is greatest number")
elif(num2>num1 and num2>num3):
    print("num2 is greates number")
else:
    print("num3 is gratest number")


#2.	Write a python program whether a number is positive negative or zero. 
num= int(input("enter a number"))
if(num>0):
    print("number is positive")
elif(num==0):
    print("number is Zero")
else:
    print("number is negative")
#3. 3.	Write a python program to check whether a number is divisible by 11 or not. 
num= int(input("divisible by 11 or not"))
if(num%11==0):
    print("number is divisible ")
else:
    print("number is not divisible by 11")

    #4.	Write a python program to check whether a number is even or odd using conditional statement and using for and while loop. 
    n=int(input("enter  a number"))
    if(n%2==0):
        print("number is even ")
    else:
        print("no is odd")


       # Check if a number is even or odd using a for loop
number = int(input("Enter a number: "))

# Using a for loop to iterate once
for i in range(1):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

 #using while loop
    a =int(input("entera number"))
    i=0
    while i<1:
        if a%2==0:
            print(f"{number } is even ")
        else:
            print(f"{number} is an odd")
            i+=1

#5.	Write a python program to check whether a year is a leap year or not. 
year =int(input("enter a year "))
if (year % 4 == 0 and year % 100 != 0 or year%400==0): ### if the remainder of dividing by four equals zero then it's a leap year. #### 
    print("it is a leap year")
else: print('This is not a leap year.')
    
    #6.	Write a python program to calculate profit or loss. 
sp =int(input("enter a number"))
cp =int(input("enter a cp"))
if(sp-cp>0):
    print("profit = "+(sp-cp))
else:
    print(" loss = "+(cp-sp))

#7.	Write a python program to calculate grades of a student.
    grade =int(input())
