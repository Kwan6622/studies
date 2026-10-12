import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 50, 30, 40])
y2 = np.array([13, 23, 42, 10])
y3 = np.array([20, 28, 24, 32])

font_styles = dict(fontsize=20,
                    family='Calibri',
                    fontweight='bold',
                    color='#1fd8f0')

plt.title("Class size", **font_styles)

plt.xlabel('Year', **font_styles)
plt.ylabel('Count', **font_styles)

plt.tick_params(axis='both', colors='#03ff00')

plt.plot(x, y1)  
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x) # Show only values in the array that was passed in

plt.show()