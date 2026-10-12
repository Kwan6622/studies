import pandas as pd

# Series = A Panda 1-Dimensional labeled array that can hold any data type 
# It's like a single column in a spreadsheet (1-D)

data = [100, 102, 104, 200, 202, 204]

series = pd.Series(data, index=['Apartment #1', 'Apartment #2', 'Apartment #3', 'Apartment #4', 'Apartment #5', 'Apartment #6'])
# The length of 'index' must be equal to length of the 'data' list

print(series.loc['Apartment #1'])
print()
# loc: location based on label (Label-based)

print(series.iloc[0])
print()
# iloc: location based on integer index (Integer position-based)
'''
series.loc['Apartment #3'] = 200 
print(series)
print()
'''

# Filtering 
print(series[series >= 202])
print()
print(series[series < 202])
