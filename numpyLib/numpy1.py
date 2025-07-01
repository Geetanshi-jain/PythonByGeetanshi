#1. Array Creation Functions
#np.array(data): Creates an ndarray (Numpy array) from a list or tuple.
import numpy as np
#np.array(data): Creates an ndarray (Numpy array) from a list or tuple.
arr = np.array([1, 2, 3])
print(arr)  # Output: [1 2 3]

#np.zeros(shape): Creates an array filled with zeros of the specified shape.

Zeroes_arr= np.zeros((2,3))
print(Zeroes_arr)

# np.eye(N): Create an identity matrix of size N*n 
identity_matrix = np.eye(3)
print(identity_matrix)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

#np.full(shape, fill_value): Creates an array of the given shape, filled with a specified value.
full_array = np.full((2, 2), 5)
print(full_array)
# Output:
# [[5 5]
#  [5 5]]
#np.arrange(start,stop,step): crreate an array with a range of values from start to stop with a specifiedd step 
range_array = np.linspace(0,10,2)
print(range_array)
#np.linspace(start,stop,num):
#creates an array with num evenly spaced values between start and stop
linspace_array = np.linspace(0,1,5)
print(linspace_array)

#Basic array operations
#lement-wise Addition
#Syntax: np.add(array1, array2)
array1=np.array([1,2,3])
array2= np.array([4,5,6])
res= np.add(array1,array2)
print(res)
# Element wise substraction
#syntax- 
#np.substract(Array1,array2)
#Description: Subtracts the elements of array2 from array1, element by element. 
array1= np.array([5,6,7])
array2= np.array([1,2,3])
result= np.substract(array1,array2)
#Element wise multiplications
array1=np.array([1,2,4])
array2=np.array([5,6,7])
res= np.multiply(array1,array2)
print(res)
#4.element wise division 
np.divide()

#5. lement-wise Division
#Syntax: np.divide(array1, array2)
arr1= np.array([3,6,9])
arr2= np.array([2,3,4])
result= np.divide(arr1,arr2)



#Dot product (matrix multiple )
arr1= np.array([4,9,10])
arr2= np.array([2,3,4])
result= np.dot(arr1,arr2)
print(result)
