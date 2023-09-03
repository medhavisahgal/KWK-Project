import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({'Seek Treatment': [32.82, 67.18]}, index=['Yes', 'No'])
colors = ["#023047", "#219ebc"]
plot = df.plot.pie(y='Seek Treatment', figsize=(5, 5), colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Percentage of Male", bbox={'facecolor': '1.0', 'pad': 4})
plt.show()
