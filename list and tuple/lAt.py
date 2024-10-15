#list denoted by square brackets
#list - mutable ,ordered,allowed multiply duplicates 
#list methods- 

list =[1,2,3,4,5,6]
#  1. Modifying elements -

#1.1  append()- mth return none  ,it add element at last in the list 
list.append(12) 
print(list)
#1.2 extend()- mth used  to add iterable element like tuple , set , dic 
list.extend([1,2,3]) 
# 1.3  insert(). - mth add a singal element in specified index 
list.insert(1,23)
print(list)

# 2 Removing elements: You can remove items using methods like remove(), pop(), or clear().
# 2.1  remove(obj)
list.remove(1)
print(list)
#2.2 pop()
list.pop()
#2.3 clear()
list.clear()

#8 list.index(obj)- gives the particular index of the list,  it takes element as a argument 
list =[1,2,3,4,5,6]
print(list.index(6))

#9. list.count(obj)- return the total number  how many times a particular element present  in the  list    
print(list.count(3))
#10. list.sort([func]) -
list.sort()
##11. list.reverse()
list.reverse()

#list.slicing()-
 # 1. list[_:_] ,2 . list[0: ],3. list[3: ],4. list[-1:-4]
print(list[ : ])
print(list[1: ])
print(list[0: ])
print(list[4: ])

#Tuple -
# tuple = immutable  ,ordered collections of element means once a tuple is created we cannot modify this.
tuple=("rohan ","physics",32,12.2)
tuple1= (1,2,3,32,12.2)
print("Item at 0th index",tuple[0] )
print("Item at 0th index",tuple1[0] )
#accesing using negative index
print("Item at 0th index",tuple[-1] )
print("Item at 0th index",tuple1[-3])

#Accesing tuple  item using slicing 
tup1 =("a","b","d","c")
tup2= (23.90,True,-55,1+5j)

print ("Items from index 1 to last in tuple: ", tuple1[1:])
print ("Items from index 0 to 1 in tuple1: ",tuple1[:2])

#update a tuple
T1 = (10, 20, 30, 40)
# Tuple to be concatenated
T2 = ('one', 'two', 'three', 'four')
# Updating the tuple using the concatenation operator
T1 = T1 + T2
print(T1)
print(tuple.count(3))
print(tuple.index(2))












