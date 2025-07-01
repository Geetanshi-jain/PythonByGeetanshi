#perform all method  on list 
#list denoted by square brackets
#list - mutable ,ordered,allowed multiply duplicates 
#list methods- 

list =[1,2,3,4,5,6]
#  1. Modifying elements -
print(len(list))
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
print(list[-1:-4])
print(list[ : ])

print(list[1: ])
print(list[0: ])
print(list[4: ])
print(len(list))
 # perform all methods on nested list - 

Neslist =[[1,1],[2,'a'],3,'c',['cde',2.5]]
#  1. Modifying elements -
print(len(list))

#1.1  append()- mth return none  ,it add element at last in the list 
Neslist.append(12) 
Neslist[0].append(3)
print(Neslist)

Neslist.extend([1,2,3]) 
# 1.3  insert(). - mth add a singal element in specified index 
Neslist[0].insert(0,23)
print(Neslist)
Neslist[0].remove(1)
print(Neslist)
#2.2 pop()
Neslist.pop()
#2.3 clear()
#Neslist.clear()

print(Neslist[0].index(1))

print(Neslist[0].count(1))


 

""" perform all list method on tuple or nested tuple"""
#Tuple -
# tuple = immutable  ,ordered collections of element means once a tuple is created we cannot modify this.
tuple=("rohan ","physics",32,12.2)
tuple1= (1,2,3,32,12.2,2)
print(tuple1)

print("Item at 0th index",tuple[0] )
print("Item at 0th index",tuple1[0] )
#accesing using negative index
print("Item at -1th index",tuple[-1] )
print("Item at -3th index",tuple1[-3])

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

print(len(tuple))







# NEsted Tuple -
# tuple = immutable  ,ordered collections of element means once a tuple is created we cannot modify this.
Nestuple=(("rohan ",123),("physics",32,12.2),9,(78,2),("abc"),12,4,3,21,1)

print("Item at 0th index",Nestuple[0][1])

#Accesing tuple  item using slicing 

print ("Items from index 1 to last in tuple: ", Nestuple[1:])

print ("Items from index 0 to 1 in tuple1: ",Nestuple[:2])


# Tuple to be concatenated
T2 = ('one', 'two', 'three', 'four')
# Updating the tuple using the concatenation operator
Nestuple = Nestuple  + T2
print(Nestuple)
print(Nestuple.count(3))

print(len(Nestuple))




"""perform all sets method in 3 sets""" 
# Creating a set with some elements
set1 = set([1, 2, 3, 4])
set2 ={1,2,3,4,5}
set3= {12,3,2,4,5,6,1}

print(set1)  # Output: {1, 2, 3, 4}
print(set2)
print(set3)



#4.discard(element): Removes an element from the set without raising an error if the element is not found.
set1.discard(3)  
# 5 pop(): Removes and returns a random element from the set
popped_element = set1.pop()
print(popped_element)  
print(set1)  


# 7 Union (|): Combines two sets, including all elements

print(set1 | set2|set3)  
#Intersection (&): Elements common to all  sets.
print(set1 & set2 & set3) 
#Difference (-): Elements in the first set but not in the second.
print(set1 - set2)  

#Symmetric Difference (^): Elements in either set, but not both
print(set1 ^ set2)  
#Union using union() Method:
#The union() method returns a new set that contains all unique elements from both sets.
# Using the inbuilt union() method

#The intersection() method returns a new set that contains only the elements common to both sets.
# Using the inbuilt intersection() method
set1 = set1.intersection(set2).intersection(set3)
print(set1)

#The difference() method in Python returns a new set that contains the elements present in the first set but not in the second set.
# Using the inbuilt difference() method

difference_set = set1.difference(set2).difference(set3)

print("Difference (set1 - set2):", difference_set)  
#symmetric_difference():
#The symmetric_difference() method returns a new set with elements that are in either of the sets, but not in both.
# Using the inbuilt symmetric_difference() method
symmetric_difference_set = set1.symmetric_difference(set2).symmetric_difference(set3)

print("Symmetric Difference:", symmetric_difference_set) 
# Example of issubset()
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}

is_subset = setA.issubset(setB)
print("Is setA a subset of setB?", is_subset)  # Output: True
# Example of issuperset()
is_superset = setB.issuperset(setA)
print("Is setB a superset of setA?", is_superset)  # Output: True



""" WAP to calculate total of items in list also calaculate avg using func"""

CalList =[1,2,3,4,5,55,4,3]
print("avg of list = ",)

def calculate_average(numbers):
    if len(numbers) == 0:
        return "List is empty"
    return sum(numbers) / len(numbers)

# Sample list
numbers = [10, 20, 30, 40, 50]

# Call the function and print the result
average = calculate_average(numbers)
print("Average of the list:", average)


#write the differnece b/w list and tuple -
#The random module in Python is used to generate random numbers and make random selections. Here are some common uses along with examples:

import random
#Generating a random integer within a range:
random_int = random.randint(1, 10) 
print("Random integer:", random_int)
#random_float = random.random()  # Generates a random float between 0.0 and 1.0
 # Generates a random float between 0.0 and 1.0
random_float = random.random()

print("Random float:", random_float)

#3 Choosing a random element from a list:
items = ['apple', 'banana', 'cherry', 'date']
random_item = random.choice(items)  # Picks a random element from the list
print("Random choice:", random_item)
items = ['apple', 'banana', 'cherry', 'date']
random_item = random.choice(items)  
# Picks a random element from the list
print("Random choice:", random_item)
#Generating a random sample from a list:
sample = random.sample(items, 2)  # Picks 2 unique random elements from the list
print("Random sample:", sample)

#repetation operator on list 
mylist = [1,2,3]
repeated_list= mylist*3
print(repeated_list)

#iteration over list with for and while loop 
# sorted list in desending order 

  
def sort_list_descending(lst):
    lst.sort(reverse=True)  # Sort the list in descending order
    return lst


l = [1, 2, 3, 3, 2, 4, 5, 6]
sorted_list = sort_list_descending(l)
print("Sorted list in descending order:", sorted_list)


#concatenate list 
T1= [1,2,3,4]
t2=[4,4,2,2,3]
l3= T1+t2
print(l3)
#copy list in another list 

original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()

print("Copied list using copy():", copied_list)







