#using histogram method to plot a bar graph using histogram in pandas 

import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")
print(df)
df1 = df["Age"].hist()
print(df1)


#Question2 

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("students1.csv")
print(df)
df2 =df["City"].hist()
print(df2)
plt.show()
