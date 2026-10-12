import pandas as pd

# Data cleaning = The process of fixing/removing
# Incomplete, incorrect, or irrelevant data
# ~75% work done w/ pandas is data cleaning

df = pd.read_csv('data/pokemon.csv')

# 1. Remove irrelevant columns
# df = df.drop(columns=['Legendary'])
# print(df)

# 2. Handle missing data
# df = df.dropna(subset=['Type 2']) -- Remove NaN values in a DF
df = df.fillna({'Type 2': 'None'}) # Fill NaN value using dictionary 
print(df)

# 3. Fix incosistent values
df['Type 1'] = df['Type 1'].replace({'Grass': 'GRASS', 
                                    'Fire': 'FIRE',
                                    'Water': "WATER"}
                                    )
# Replacing values in a column using dictionary
print(df)

# 4. Standarize text
df['Name'] = df['Name'].str.lower()
print(df)

# 5. Fix/change data type
df['Legendary'] = df['Legendary'].astype(bool)
print(df)

# 6. Remove duplicate
df = df.drop_duplicates()
print(df)