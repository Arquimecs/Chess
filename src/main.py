import matplotlib

import matplotlib.pyplot as plt
import numpy as np



print(matplotlib.__version__)
print("Hello World!")

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints,'o--r')
plt.show()
