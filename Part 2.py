specie = ("18", "19", "20", "21", "22", "23", "24")
penguin_mean = {
    'Yes': (25, 20, 28, 24, 19, 23, 21),
    'No': (12,10, 20, 16, 13, 25, 26)
}

x = np.arange(len(specie))  
width = 0.45 
multiplier = 0
fig, ax = plt.subplots()

for attribute, measurement in penguin_mean.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1
ax.set_ylabel('Number of People')
ax.set_xlabel('Age')
ax.set_title('Number of people suffering from Anxiety')
ax.set_xticks(x + width * 0.5)  # Adjusted position for ticks
ax.set_xticklabels(specie)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 40)
plt.show()
