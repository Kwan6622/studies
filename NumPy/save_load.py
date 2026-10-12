import numpy as np

# Save an array

"""
array = np.array([
                [1, 2, 3],
                [4, 5, 6]
                ])

np.save("data", array)

print("NumPy array was saved!")
"""
# Load an array

array = np.load("data.npy")
print(array)

# Save multiple Num{y array
'''
array1 = np.array([
                [1, 2, 3],
                [4, 5, 6]
                ])

array2 = np.array([1.1, 2.2, 3.3, 4.4])

array3 = np.array([2020, 2021, 2022, 2023, 2024])

np.savez("dataz", array1, array2)
print("NumPy arrays were saved!")

np.savez_compressed("dataz2", array1, array2, array3)
print("NumPy arrays were saved!")
'''
# Load multiple arrays

arrays = np.load("dataz.npz")
array1 = arrays["arr_0"]
array2 = arrays["arr_1"]

print(arrays)
print(array1)
print(array2)