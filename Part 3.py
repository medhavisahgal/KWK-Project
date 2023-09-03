import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({'Seek Treatment': [34.65, 65.35]},
                  index=['Yes', 'No'])
colors = ["#2a9d8f", "#264653"]
plot = df.plot.pie(y='Seek Treatment', figsize=(5, 5),colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Percentage of Female", bbox={'facecolor':'1.0', 'pad':4})
plt.show()
