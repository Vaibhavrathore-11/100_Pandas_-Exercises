#.apply() function use
import pandas as pd

df = pd.read_csv("raw_data.csv")
print(df)

df2 = df.copy()
df2["tax"] = df["income"].apply(lambda x: "20%" if x >= 50000 else "10%")
print(df2)


#Example 
import pandas as pd

data = {
    "Name": ["Amit","pihu","neel","bucher","John"],
    "Marks": [45,67,89,90,21]
}
df = pd.DataFrame(data)
print(df)
df["Result"] = df["Marks"].apply(lambda x:"pass" if x >= 40 else "Fail")
print(df)