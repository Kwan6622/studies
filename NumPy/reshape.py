import numpy as np

# reshape()
# Changes the shape of an array w/o altering the shape
# .reshape(layers, rows, columns)

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Condition for reshape to work
# layers * rows * columns = amount of elements in the array
array = array.reshape(3, 2, 2)
print(array)

# The row or column dimension can be set to -1
# NumPy automatically calculates the missing dimension 
# Based on the specified size of the other dimension (4)
array = array.reshape(-1, 4)
print(array)