import pandas as pd

df = pd.read_csv('data/pokemon.csv', index_col='Name')

while True:
    try:
        print(df.loc[input("Enter pokemon's name: ")])
        break
    except KeyError:
        print("Pokemon not found!")
        continue