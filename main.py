import numpy as np
import matplotlib.pyplot as plt
from load_data import load_data
from sort import bubbleSort
from save_path import save_path

# Anzahl der Einträge 1804 bei 30:05 min

# Daten für Plot laden und sortieren
data = load_data('activity.csv')
sorted_power_W = bubbleSort(data['PowerOriginal'])

# Plot the data
plt.plot(sorted_power_W[::-1])

plt.xlabel('Time/s')
plt.ylabel('Power/W')
plt.title('Power over Time')

#plt.savefig(r'figures/power_over_time.png') quick and dirty. also os independent
plt.savefig(save_path("figures", "power_over_time.png"))
plt.show()