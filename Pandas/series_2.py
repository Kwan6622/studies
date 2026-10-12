import pandas as pd

calories = {
    'Day 1': 1750,
    'Day 2': 2400,
    'Day 3': 1234,
}

series = pd.Series(calories)
# No need to pass in index
# Cause it will use Dictionaries' keys as indexes

print(series)
print()
print(series.loc["Day 3"] + 300)
