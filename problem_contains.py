#Contains in Pandas: kisi text/string ke andar specific word ya character present hai ya nahi, ye check karne ke liye use hota hai.

import pandas as pd
df = pd.read_csv("globalAirQuality.csv")
result = df["country"].str.contains("US")
print(result)


df2 = pd.read_csv("students.csv")
vai = df["city"].str.contains("indore")
print(vai)
print(df2.columns)

#Example

df3 = pd.read_csv("students1.csv")
df4 = pd.read_csv("students1.csv")

df3["HR_Check"] = df3["Department"].str.contains("HR", case = False, na=False)
print(df3)
df4["City "]= df4["City"].str.contains("Bhopal", case = False)
print(df4)

