import matplotlib.pyplot as plt
import numpy as np

# Bar chart: Compare categories of data by
# representing each category w/ a bar

categories = np.array(["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweet"])
values = np.array([4, 3, 1, 6, 4, 2])

plt.bar(categories, values, color="cyan")
# plt.barh(categories, values, color="cyan") | Horizontal bar chart

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel('Amount')

plt.show()