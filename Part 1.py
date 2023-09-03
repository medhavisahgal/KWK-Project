import matplotlib.pyplot as plt
import numpy as np

species = ("18", "19", "20", "21", "22", "23", "24")
penguin_means = {
    'Yes': (11, 14, 10, 15, 10, 9, 17),
    'No': (18,12, 8, 10, 8, 7, 15)
}
x = np.arange(len(species)) 
width = 0.45  
multiplier = 0
fig, ax = plt.subplots()
for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1
ax.set_ylabel('Number of People')
ax.set_xlabel('Age')
ax.set_title('Number of people suffering from Depression')
ax.set_xticks(x + width * 0.5)  
ax.set_xticklabels(species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 30)
plt.show() 
