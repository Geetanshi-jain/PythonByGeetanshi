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

