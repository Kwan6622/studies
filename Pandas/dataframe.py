import pandas as pd

# DataFrame is a tabular data structure with ROWS & COLUMNS (2-D)
# Similar to an Excel spreadsheet

data = {
    'Name': ['Spongebob', 'Patrick', 'Squidward'],
    'Age': [30, 35, 50],
    }

df = pd.DataFrame(data, index=['Employee 1', 'Employee 2', 'Employee 3'])

print(df)
print()

# Accessing data w/ loc & iloc
print(df.loc["Employee 1"])
print()
print(df.iloc[2])
print()

# Create a new column
df['Job'] = ['Fry Cook', 'N/A', 'Cashier']
print(df)
print()

# Create a new row
# Simplest way: Create a new df then Concatenate 
new_rows = pd.DataFrame([{'Name': 'Sandy', 'Age': 28, 'Job': 'Engineer'},
                        {'Name': 'Eugene', 'Age': 60, 'Job': 'Manager'}],
                        index = ['Employee 4', 'Employee 5']) # Add an Index to the new data
df = pd.concat([df, new_rows])
print(df)
print()