import matplotlib

import matplotlib.pyplot as plt
import numpy as np



print(matplotlib.__version__)
print("Hello World!")

ypoints = np.array([0, 2, -1, 2, 4])
ypoints2 = np.array([1, 2, 5, 3, 1])

plt.plot(ypoints, linewidth = 2, marker = 'o', linestyle = 'dotted', color = 'r', ms = 10, mec = 'r', mfc = 'r')
plt.plot(ypoints2,  linewidth = 2, marker = 'o', linestyle = 'dotted', color = 'orange', ms = 10, mec = 'orange', mfc = 'orange')
plt.grid()

plt.title("Food Data")
plt.xlabel("time taken")
plt.ylabel("food eaten")

# ms = markersize, mfc = markerfacecolor, mec = markeredgecolor
plt.show()
