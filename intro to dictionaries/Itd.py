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




# Nested list 2D list in python 
list =[[1,2],[3,'+'],[4,6]]
print([0][1])
# length of elements iside list 
print(list[1][0].append(5))

print(list[1][0].remove(1))

print(list[1].pop())

print(list.pop(2))

list.extends([2,3])

print(list.count(5))

print(list.index(3))




