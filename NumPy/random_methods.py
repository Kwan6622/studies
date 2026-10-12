import numpy as np

# Setting a seed is useful when you need the same result
rng = np.random.default_rng() # argv -> seed=1

print(rng.integers(low=1, high=101, size=(6, 3)))
print()

# np.random.seed(seed=2)
print(np.random.uniform(low=-1, high=1, size=(2, 3)))
print()

array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)
print()

fruits = np.array(['apple', 'orange', 'watermelon', 'mango', 'grape'])
fruit = rng.choice(fruits, size=(3, 3))
print(fruit)