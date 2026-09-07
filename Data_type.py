#Data Type
import pandas as pd
df = pd.read_csv("students.csv")
print(df)
print(df.dtypes)
df2 = df.copy()
df2 = df2.fillna(0)
print(df2)
df2 = df2["Age"].astype("int64").copy()
print(df2.dtype)


#Example
import pandas as pd

df1 = pd.DataFrame({
    'Name': ['Rahul', 'Aman', 'Neha'],
    'Age': ['20', '25', '22'],
    'Salary': [25000.5, 30000.0, 28000.5],
    'Passed': [True, False, True]
})

print(df1.dtypes)

df1["Age"] =df['Age'].astype(float)

print(df1.dtypes)

print(df1)