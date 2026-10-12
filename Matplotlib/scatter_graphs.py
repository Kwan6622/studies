import matplotlib.pyplot as plt
import numpy as np

# Scatter graph: Shows the relationship between 2 variables
# Helps to define correlation (+, -, None)
# Example: Study hours vs. Test scores

x1 = np.array([0, 1, 2, 1, 3, 4, 7, 8, 9 ,12])
y1 = np.array([42, 59, 63, 55, 70, 73, 82, 88, 92, 97])

x2 = np.array([0, 1, 2, 1, 3, 4, 7, 8, 9 ,12])
y2 = np.array([45, 50, 60, 49, 68, 77, 81, 83, 90, 100])


plt.scatter(x1, y1, color='orange', alpha=0.5, s=50, label='Class A') #transparency
plt.scatter(x2, y2, color='red', alpha=0.5, s=50, label='Class B')

plt.legend()

plt.xlabel('Hours studied')
plt.ylabel('Grade')

plt.show()
