import numpy as np

array = np.zeros((2, 3, 2))
print(array)
print()

array = np.ones((2, 2, 1))
print(array)
print()

array = np.full((2, 2, 1), 9)
print(array)
print()

array = np.eye(5)
print(array)
print()

array = np.empty((2, 3, 3))
print(array)
print()

array = np.arange(0, 100, 3) # argv: start, stop, step
print(array)
print()

array = np.linspace(0, 100, 5) # argv: start, stop, num
print(array)
print()