print('file: NeutrinosData.py')

import numpy as np
import matplotlib.pyplot as plt

# number of events (neutrinos in 10 s intervals)
k = np.arange(0, 10)

frequencies = np.array([1042, 860, 307, 78, 15, 3, 0, 0, 0, 1])

# Plot
plt.figure()
plt.plot(k, frequencies, 'o', color='black', markersize=4)

plt.xlabel('Number of events', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('')
plt.tick_params(axis='both', labelsize=12)

plt.show()