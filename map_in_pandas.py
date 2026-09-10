# Map function use()

import pandas as pd
df2 = pd.read_csv("industry.csv" , sep="\t")
# use map () Function
gender_map = {"Male" : "M", "Female" : "F", "Unknown" : "U"}
df2["Gender"] = df2["Gender"].map(gender_map)
print(df2)
print(df2["Gender"].value_counts())



#Example

import pandas as pd 
df1 = pd.read_csv("students1.csv")
print(df1)
office = {"HR": "H", "IT" :"I", "Finance": "F","Marketing" : "M", "Sales":"S"}
df1["Department"] = df1["Department"].map(office)
print(df1.to_string())
print(df1.columns)
