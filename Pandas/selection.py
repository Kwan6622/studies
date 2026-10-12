import pandas as pd

df = pd.read_csv('data/pokemon.csv', index_col='Name')
# index_col makes the column the default index 
# Useful for searching instead of using Pandas default index

# SELECTION by COLUMN
# print(df['Name'].to_string())

print(df[['Attack', 'Defense', 'Speed']])
print()

# SELECTION by ROW
print(df.loc['Arceus']) 
print()
# Cause we set the index to Name
# We can access data using a Pokemon's name (label)

# Select COLUMNS that you want to display
print(df.loc['Pikachu', ['Speed', 'Sp. Atk']]) 
print()

# You can select a range of ROWS
# print(df.loc['Pikachu':'Charmander', ['Speed', 'Sp. Atk']]) WILL NOT WORK
# Cause 'Charmander' appear before 'Pikachu' in the dataset
print(df.loc['Charmander':'Pikachu', ['Speed', 'Sp. Atk']])
print()

print(df.iloc[0:11:2, 0:3])
# Choose what you want to display
# '0:11:2' Row 1-10, step = 2
# '0:3' Column 1-3
