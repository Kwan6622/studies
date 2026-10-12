import numpy as np

array = np.array([1.25, 2.98, 3.11])
# Scalar arithmetic
print(array + 1)
print(array - 2)
print(array * 5)
print(array / 3)
print(array ** 2)
print()

# Vectorized math funcs
print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))
print(np.pi)
print()

# EXERCISE
radii = np.array([1, 2, 3])
print(f'Area each circle:', np.pi * radii ** 2)
print()

# Element-wise arithmetic
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# Comparison operators
scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100)
print(scores >= 60)
print(scores < 60)

scores[scores < 60] = 0
print(scores)