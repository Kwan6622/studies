import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 50, 30, 40])
y2 = np.array([13, 23, 42, 10])
y3 = np.array([2, 18, 24, 32])

line_style = dict(marker='.', 
                markersize=20, #ms
                markerfacecolor='#03ff00', #mfc
                markeredgecolor='#000000', #mec
                linestyle='dashdot', #ls
                linewidth=3, #lw
                # line color
                )

#Read document for more customizations
plt.plot(x, y1, **line_style)  
#HEX color code/name 

plt.plot(x, y2, **line_style)
# ** used to unpack dictionary

plt.plot(x, y3, color='#ff0000', **line_style)

plt.show()