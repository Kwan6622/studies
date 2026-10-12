import pandas as pd

# Reading a CSV, JSON file

df = pd.read_csv('data/pokemon.csv')
print(df) 
# This only display this first and last 5 entries of the dataset
# use .to_string() to print EVERY entries
print()

df = pd.read_json('data/pokemon.json')
print(df)