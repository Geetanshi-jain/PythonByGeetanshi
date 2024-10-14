#conditional statemnt 
#if condition:
    # block of code
if(100>20):
    print("100 is greater than 20")
#if else
if(20>10):
    print("20 is grater than 10")
else:
    print("10 is less than 20")
#nested if else 
num = 10
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
else:
    print("The number is not positive")

#iterative statement - for ,while 
for i  in range(10):
    print(i)
    print()



#while loop 
num=0
while(num>10):
    print(num)
    num=num+1

#pythan has not contain any type of do while loop but it can be implemented using for and while loops
# Simulating a do-while loop in Python

while True:
    # Code block that runs at least once
    num = int(input("Enter a positive number (enter 0 to stop): "))
    
    # Condition to break out of the loop
    if num <= 0:
        break

    print(f"The number you entered is: {num}")

print("Loop has ended")

# -nested loops 
for i in range(10):
    for j in range(10):
        print("*")
    print()

#Control statement  -
#break statement 
while(num>10):
    print(num)
    num=num+1
    if(num==4):
        break
#continue statement 
for i in range(5):
    if i == 3:
        continue
    print(i)

#pass statement 
for i in range(5):
    if i == 3:
        pass
    print(i)





