import numpy as np

# 1. np.array(data): Creates an ndarray (Numpy array) from a list or tuple.
arr = np.array([1, 2, 3])
print("Array:", arr)

# 2. np.zeros(shape): Creates an array filled with zeros of the specified shape.
zeroes_arr = np.zeros((2, 3))
print("\nZeroes Array:\n", zeroes_arr)

# 3. np.eye(N): Create an identity matrix of size N x N
identity_matrix = np.eye(3)
print("\nIdentity Matrix:\n", identity_matrix)

# 4. np.full(shape, fill_value): Creates an array filled with a specific value.
full_array = np.full((2, 2), 5)
print("\nFull Array:\n", full_array)

# 5. np.arange(start, stop, step): Create array with range (Corrected from 'arrange')
range_array = np.arange(0, 10, 2)
print("\nRange Array (arange):", range_array)

# 6. np.linspace(start, stop, num): Evenly spaced numbers
linspace_array = np.linspace(0, 1, 5)
print("\nLinspace Array:", linspace_array)

# 7. Element-wise Addition
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
add_result = np.add(array1, array2)
print("\nElement-wise Addition:", add_result)

# 8. Element-wise Subtraction (Corrected spelling from 'substract' to 'subtract')
array1 = np.array([5, 6, 7])
array2 = np.array([1, 2, 3])
sub_result = np.subtract(array1, array2)
print("Element-wise Subtraction:", sub_result)

# 9. Element-wise Multiplication
array1 = np.array([1, 2, 4])
array2 = np.array([5, 6, 7])
mul_result = np.multiply(array1, array2)
print("Element-wise Multiplication:", mul_result)

