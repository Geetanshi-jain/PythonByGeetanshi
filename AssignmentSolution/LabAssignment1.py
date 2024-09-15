"""
Python program to interchange first and last elements in a list
"""
"""list=[10,20,30,40]
l=len(list)
list[0],list[l-1]=list[l-1],list[0]
l= len(list)
print(list)


def swap(list,i,j):
    list[i],list[j]=list[j], list[i]
    return list
list =[10,20,30,40]
print(swap(list,2,3))
ways to find length"""
"""
def findlength():
    length=len(list)


print(findlength())

#Maximum of two numbers in Python
a=int(input("enter first number"))
b=int(input("enter secand number"))
#Ways to check if element exists in list
list =[12,2,3,4,1,1,2,5]
print(12 in list)
print(1 in list)

#Ways to clear a lis t in python
my_list = [1, 2, 3, 4, 5]
my_list = []
print(my_list)  

#reverse al list
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)  

#| Cloning or Copying a list
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print(copied_list)  # Output: [1, 2, 3, 4, 5]

#Count occurrences of an element in a list
mylist= [1,2,2,2,3,4,5,6]
count=mylist.count(2)
print(count)

#using a loop
mylist =[1,2,3,4,5,1,1]
count=0
for item in mylist:
    if item ==2:
        count+=1
        print(count)

#Python Program to find sum and average of List in Python
list =[12,2,3,4,3,2,1,5]
sum=0
for i in range(len(list)):
    sum=sum+i
print("sum = ",sum)

#| Sum of number digits in List

def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

def total_sum_of_digits(my_list):
    total_sum = 0
    for number in my_list:
        total_sum += sum_of_digits(number)
    return total_sum

# Example list
my_list = [12, 34, 56, 78]

# Calculate the sum of all digits
def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

def total_sum_of_digits(my_list):
    total_sum = 0
    for number in my_list:
        total_sum += sum_of_digits(number)
    return total_sum
"""
# Calculate the sum of all digits
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
def total_sum_of_all_digits(mylist):
    total_sum =0
    for  number in my_list:
        total_sum+=sum_of_digits(number)
    return total_sum

my_list =[12,2,3,2,1]
print(total_sum_of_all_digits(my_list))




#Multiply all numbers in the list

def multiply(mylist):
    mul=1
    for i in mylist:
        mul =mul*i
    return mul
print(multiply([12,1,1,2,1]))



#Python program to find smallest number in a list
def smallestNo(mylist):
    if not mylist:
     raise valueError("The list is empty")
    smallest =mylist[0]
    for number in mylist:
        if number<smallest:
            smallest =number
    return smallest

print(smallestNo([12,1,1,2,1]))

#Python program to find largest number in a list

def second_largest(mylist):
    if len(mylist) < 2:
        raise ValueError("The list must contain at least two elements")
    
    # Initialize the largest and second largest with very low values
    largest = second_largest = 0
    for number in mylist:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number
    if second_largest == 0:
        raise ValueError("There is no second largest element")
    return second_largest
print(second_largest([12, 1, 2, 3, 4, 2, 1]))  
#Python program to print even numbers in a list
def even(mylist):
    for i in mylist:
        if i%2==0:
            print(i)  

even([12,2,22,3,1,1])




#Python program to print odd numbers in a List
def even(mylist):
    for i in mylist:
        if i%2==0:
            print(i)  

even([12,2,22,3,1,1])


#Python program to print all even numbers in a range

a =int(input("enter first range"))
b= int(input("enter last range"))
if (a-b>0):
 for i in range(a,b):
    if i%2==0:
        print(i)
else:
    print("enter valid range in positive manner")

#Python program to print all odd numbers in a range

a =int(input("enter first range"))
b= int(input("enter last range"))
if(a-b>0):
 for i in range(a,b):
    if i%2!=0:
        print(i)
else:
    print("enter valid  range")
#Python program to count Even and Odd numbers in a List
a= int(input("enter first limit range"))
b= int(input("enter  last limit "))
l=[]
l1=[]
if(a-b<0):
    for i in range(a,b):
        if i%2==0:
            l.append(i)
        else:
            l1.append(i)
print(l)
print(l1)
#Python program to print positive numbers in a list
list= [12,-2,3,-2,-1,1,-12,19,5,-43,-21]
l1=[]
for i in list:
    if(i>0):
        l1.append(i)
    else:
        print(i)
    

#Python program to print negative numbers in a list



#Python program to print all positive numbers in a range

#Python program to print all negative numbers in a range

#Python program to count positive and negative numbers in a list