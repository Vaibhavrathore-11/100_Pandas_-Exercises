import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students1.csv")
print(df)

df1 = df["Age"].hist()
print(df1)
df1 = df.plot(kind="scatter", x ="Age", y="Salary")
print(df1)
plt.show()