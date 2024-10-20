#n Python, the set() method is used to create a set, which is a collection data type that is unordered, mutable, and does not allow duplicate elements. Here's how you can use sets and various methods associated with them:
# Creating a set with some elements
my_set = set([1, 2, 3, 4])
print(my_set)  # Output: {1, 2, 3, 4}
#add(element): Adds a single element to the set.
my_set.add(5)
print(my_set)  
#2 update([elements]): Adds multiple elements to the set.
my_set.update([6, 7, 8])
print(my_set)  
# 3 remove
my_set.remove(3)
print(my_set)  

#4.discard(element): Removes an element from the set without raising an error if the element is not found.
my_set.discard(3)  
# 5 pop(): Removes and returns a random element from the set
popped_element = my_set.pop()
print(popped_element)  
print(my_set)  

# 6 clear(): Removes all elements from the set. 
my_set.clear()
print(my_set)  
# 7 Union (|): Combines two sets, including all elements
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  
#Intersection (&): Elements common to both sets.
print(set1 & set2) 
#Difference (-): Elements in the first set but not in the second.
print(set1 - set2)  

#Symmetric Difference (^): Elements in either set, but not both
print(set1 ^ set2)  
#Union using union() Method:
#The union() method returns a new set that contains all unique elements from both sets.
# Using the inbuilt union() method
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print("Union:", union_set)  
#Intersection using intersection() Method:
#The intersection() method returns a new set that contains only the elements common to both sets.
# Using the inbuilt intersection() method
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)  
#The difference() method in Python returns a new set that contains the elements present in the first set but not in the second set.
# Using the inbuilt difference() method
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)  
#symmetric_difference():
#The symmetric_difference() method returns a new set with elements that are in either of the sets, but not in both.
# Using the inbuilt symmetric_difference() method
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set) 
# Example of issubset()
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}

is_subset = setA.issubset(setB)
print("Is setA a subset of setB?", is_subset)  # Output: True
# Example of issuperset()
is_superset = setB.issuperset(setA)
print("Is setB a superset of setA?", is_superset)  # Output: True
