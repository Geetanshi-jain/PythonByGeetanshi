#Rcursion -
 #recursion is a technique  used to solve computer problems by creating a function that calls itself until our program does not achieve the desiered goal 
# function call limit -python1000
"""uses of recursion function -
code resusability 
divide and conquer 
simpler code ,
faster development 
Easy to divide task in team work 
Better testing 
"""

# Ex - calculate sum of natural number in python 
def Sum(n):
    if n==1:
        return 
    else:
        return n+Sum(n-1)
Sum(5)

#factorial of number 
f=0
f1=1
def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
    
    
