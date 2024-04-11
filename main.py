import numpy as np
import matplotlib.pyplot as plt
from load_data import load_data
from sort import bubbleSort

# Anzahl der Einträge 1804 bei 30:05 min

data = load_data('activity.csv')
sorted_power_W = bubbleSort(data['PowerOriginal'])

# Plot the data
plt.plot(sorted_power_W[::-1])

plt.xlabel('Time/s')
plt.ylabel('Power/W')
plt.title('Power over Time')

plt.savefig('figures/power_over_time.png')
plt.show()
