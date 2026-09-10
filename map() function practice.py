#Map() function practice with the lhelp of dataframe

import pandas as pd
df2 = pd.read_csv("students1.csv")

department_map = {
    "HR":["Human Resources"],
    "IT": ["Information Technology"],
    "Finance":["Financial Services"],
    "salse":["Sales Department"]

}
df2["Department"] = df2["Department"].map(department_map)
print(df2.to_string())