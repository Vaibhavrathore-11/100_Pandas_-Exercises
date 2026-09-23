#List comrehesion
import pandas as pd
df = pd.read_csv("raw_data.csv")


df2 = df.copy()

new_col_order = [col for col in df2.columns if col!= "id"] + ["id"]
print(new_col_order)
print(df2[new_col_order])


'''example of list comrehsion
List comprehension is a concise way to create a new list by applying an expression to each item in an iterable.'''

import pandas as pd
df = pd.read_csv("students.csv")

df1 = df.copy()

new_col_order = [col for col in df1.columns if col!="Name"] + ["Name"]

print(new_col_order)
print(df1[new_col_order])


# Example 
import pandas as pd
df = pd.read_csv("students1.csv")

df3 =df.copy()

new_col_order = [col for col in df3.columns if col!="Employee_ID"] + ["Employee_ID"]

print(new_col_order)
print(df3[new_col_order])
print(df)
