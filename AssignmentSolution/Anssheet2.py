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
 8  * * * * 
    * * * *
    * * * *
    * * * * 
 """
for i in range(4):
    for j in range(4):
        print(" *" ,end=" ")
    print()
"""
 *
 * * *
 * * * *
 * * * * *
 * * * * * *
 * * * * * 
 * * *
 *
"""
for i in range(6):
    for  j in range(i+1):
         print("*",end= " ")
    print()
for  k in range(3,0,-1):
    for l in range(2*k-1):
        print("*",end=" ")
    print()

"""
 1 1 1 1 1 
 2 2 2 2 2 
 3 3 3 3 3
 4 4 4 4 4
 5 5 5 5 5
 """
for i in range(1,6):
    for j in range(6):
        print(i,end=" ")
    print()

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()


"""
13.
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(1,6):
    for j in range(i):
        print(i)
    print()


#14.
"""
    1
    1 2
    1 2 3
    1 2 3 4 
    1 2 3 4 5
    
"""
ctn=1
for  i in range(1,6):
        ctn=1
        for j in range(i):
            
            print(ctn,end=" ")
            ctn=ctn+1
        print()

"""
15.
              1
             2 2
           3 3 3
         4 4 4 4
       5 5 5 5 5
"""

for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()


""" 
16.
      1 1 1 1 1
        2 2 2 2
          3 3 3
            4 4
              5
"""
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()
"""
18.
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""

for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print()
"""
18.
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""

for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print()

"""
19.
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
ctn=1
for i in range(1,5):
    for j in range(i):
        print(ctn,end=" ")
        ctn=ctn+1
    print()
"""

0 0 0 0 0
1 1 1 1
0 0 0
1 1 
0
"""
for i  in range(5,0,-1):
    for j in range(i):
        if(i%2==0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

""" 
 21.
 1 2 3 4 5
 1 2 3 4
 1 2 3
 1 2
 1 
"""
for i in range(6,0,-1):
    for j in  range(1,i):
        print(j,end=" ")
    print()

"""22.
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
"""23.
1
3 5 
7 9 11
13 15 17 19
21 23 25 27 29
"""
ctn=1
for i in range(5):
    for j in range(i):
        
         print(ctn,end=" ")
         ctn=ctn+2
    print()






""" 24
2
4 6
8 10 12
14 16 18 20
22 24 26 28 30
"""
k=1
for i in range(5):
    for j in range(i+1):
        print(2*k,end=" ")
        k=k+1
    print()









"""25
 A A A A A
 B B B B B
 C C C C C
 D D D D D 
 E E E E E
"""
ch ='A'
for i in range(5):
    for j in range(5):
        print(ch,end= " ")
    ch=  chr(ord(ch) +1)
    print()



"""26.
A B C D E
A B C D E
A B C D E
A B C D E
"""
ch ='A'
for i in range(5):
    ch='A'
    for j in range(5):
        print(ch,end= " ")
        ch=  chr(ord(ch) +1)
    print()   




"""27.
A
A B
A B C
A B C D
A B C D E
"""

for i in range(5):
    ch='A'
    for j in range(i+1):
        print(ch,end= " ")
        ch=chr(ord(ch)+1)
    print()
"""28
A
B B
C C C
D D D D
E E E E E 
"""
ch='A'
for i in range(5):
    for j in range(i+1):
        print(ch,end=" ")
    print()
    ch=chr(ord(ch)+1)




"""29
1 * * * *
2 2 * * *
3 3 3 * *
4 4 4 4 *
5 5 5 5 5  
"""
for i in range(1,6):
    for j in range(1,i+1):
            print(i,end=" ")
    for j in range(5-i):
        print("*",end=" ")

    print()




"""30
A 1 1 1 1 1
B B 2 2 2 2
C C C 3 3 3
D D D D 4 4
E E E E E 5
"""
ch='A'
print("________________")
for i in range(1,6):
    
    for j in range(1,i+1):
            print(ch,end=" ")
    for j in range(6-i):
        print(i,end=" ")
    ch=chr(ord(ch)+1)
    print()




