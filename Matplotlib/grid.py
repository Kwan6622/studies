import matplotlib.pyplot as plt
import numpy as np 

# grid(): Helps make plots easier to read by adding reference lines

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.grid(lw=2,
        color='lightgray',
        ls='dashed'
        )

plt.plot(x,y)
plt.show()