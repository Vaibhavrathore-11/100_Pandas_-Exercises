#DataFrame in pandas

import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6]])
print(df)

df = pd.read_csv("students.csv")
print(df)
print(df.head())
print(df.tail())
print(df.sample())
print(df.info())
print(df.describe())
print(df.nunique())
