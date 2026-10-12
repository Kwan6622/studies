import numpy as np

ages = np.array([
                [21, 17, 16, 20, 21, 65, 30, 19],
                [39, 23, 17, 41, 45, 29, 30, 69]
                ])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print(teenagers)
print(adults)
print(seniors)
print(evens)
print(odds)

print()

# Another way to filter while keeping the shape of the original array
# Slower than the previous way 

adults = np.where(ages >= 18, ages, -1)
print(adults)