import pandas as pd
df = pd.read_csv("students1.csv")
print(df)

#split() - method

df["Name"] = df["Name"].str.split()
print(df)


df1 = pd.read_csv("industry.csv", sep="\t")

#split data in diffrent seperator
df1["Email"] = df1["Email"].str.split("@")
print(df1)
print(df1.columns)

#Example
df2 = pd.read_csv("industry.csv",sep="\t")
df2["Name"] = df2["Name"].str.split()
print(df2) 
