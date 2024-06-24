import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D array: \n", arr1)

# 2D array
arr2 = np.array([[1, 2, 3, 4], [2, 4, 6, 8]])
print('2D array: \n', arr2)

# creating an Array of zeros
zeros = np.zeros((3, 4)) # shape (3, 4)
print("Array of Zeros: \n", zeros)

# creating an Array of Ones
ones = np.ones((2, 3)) # shape (2, 3)
print("Array of Ones: \n", ones)

# Creating an Identity matrix
identity = np.eye(3) # 3 x 3 indentity matrix
print("Identity matrix: \n", identity)

# Arithmetic operations
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])

# Addition of elements
add = arr3 + arr4
print('Addition of arrays: \n', add)

# Multiplication of arrays
product = arr3 * arr4
print('Product of elements: \n', product)
print(arr3[1,1])
print(arr4[0])
print(arr3[:,1])
