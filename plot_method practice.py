import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("raw_data.csv")
df1 = df["age"].hist()
df.plot(kind= "scatter", x = "age" , y = "income")

plt.show()
print(df1)