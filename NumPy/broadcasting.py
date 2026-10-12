import numpy as np

# Broadcasting allows NumPy to perform operations on arrays
# w/ different shapes by virtually expanding dimensions
# so they match the larger array's shape

# The dimensions have the same size
# OR 
# One of the dimensions has a size of 1

# Same number of row/col or one of them is 1

array1 = np.array([
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11 ,12],
                [13, 14, 15, 16]
                ])

array2 = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6 ,7]])

print(array1.shape)
print(array2.shape)

print(array1 + array2)
print(array2 + array1)
print(array1 * array2)
print()
# (4,1) & (1,4) works 
# (3, 4) & (4, 1) don't
# (4, 4) & (4, 1) works
# (4, 4) & (4, 2) don't

array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)
