import pandas as pd

# aggregate functions = Reduces a set of values into a signle summary value
# Used to summarize and analyze data 
# Often used w/ groupby() func

df = pd.read_csv('data/pokemon.csv', index_col='Name')

# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# Single Column
'''
print(df['Attack'].mean())
print(df['HP'].sum())
print(df['Defense'].min())
print(df['Defense'].max())
print(df['Type 2'].count())
'''

#GROUPBY: group by something in common
group = df.groupby('Type 1')

# print(group['Attack'].mean())
# print(group['Speed'].sum())
# print(group['Defense'].min())
# print(group['Defense'].max())
print(group['HP'].count())