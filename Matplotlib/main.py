import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data/pokemon.csv')

figure, axes = plt.subplots(2, 2) 

type_count = df['Type 1'].value_counts(ascending=True)

### Subplot 1

bars = axes[0,0].barh(
    type_count.index,
    type_count.values,
    color='cyan',
    edgecolor='black'
)

axes[0,0].bar_label(bars, padding=3)
axes[0,0].set_title('# of Pokemon by Primary Type')
axes[0,0].set_xlabel("Count")
axes[0,0].set_ylabel("Type")

### Subplot 2

percentage = type_count / type_count.sum() * 100

pie_data = type_count[percentage >= 5].copy()
pie_data['Other'] = type_count[percentage < 5].sum()

largest_type = pie_data.drop('Other').idxmax()
explode = [0.1 if t == largest_type else 0 for t in pie_data.index]

axes[0,1].pie(pie_data.values, labels=pie_data.index, 
                                autopct='%1.1f%%',
                                explode=explode,
                                startangle=90)
axes[0,1].set_title('Distribution of Pokemon by Primary Type')

### Subplot 3 

axes[1,0].scatter(type_count.index, type_count.values, color='green',
                                            edgecolor='black')
axes[1,0].set_title('Distribution of Pokemon by Primary Type')

### Subplot 4

bars = axes[1,1].bar(
    type_count.index,
    type_count.values,
    color='yellow',
    edgecolor='black'
)

axes[1,1].bar_label(bars, padding=3)
axes[1,1].set_title('Pokemon Count by Primary Type')
axes[1,1].set_xlabel('Primary Type')
axes[1,1].set_ylabel('Count')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()

plt.show()