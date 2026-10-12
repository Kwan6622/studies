import pandas as pd

df = pd.read_csv('data/pokemon.csv', index_col='Name')

# Filtering = Keep rows that match a condition

# legendary_pokemon = df[df['Legendary']==True ]

'''
fire_pokemon = df[(df['Type 1'] == 'Fire') |
                    (df['Type 2'] == 'Fire')]

water_rock_pokemon = df[(df['Type 1'] == 'Water') &
                    (df['Type 2'] == 'Rock')]
'''

psychic_normal_pokemon = df[
                        (df['Type 1'].isin(['Psychic', 'Normal'])) &
                        (df['Type 2'].isin(['Psychic', 'Normal']))
                        ]

print([psychic_normal_pokemon])
