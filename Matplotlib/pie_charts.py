import matplotlib.pyplot as plt
import numpy as np


# Pie chart: Circular chart divided into slices to show percentages of total
# Good for visualizing distribution among categories

categories = ['Freshman', 'Sophomores', 'Juniors', 'Seniors']
values = np.array([300, 290, 340, 400])
colors = ['red', 'green', 'blue', 'yellow']

plt.pie(values, labels=categories,
                autopct='%1.1f%%',
                colors=colors,
                explode=[0, 0, 0, 0.08],
                startangle=90)

plt.title('HCM College Student Distribution', fontsize=20)

plt.show()
