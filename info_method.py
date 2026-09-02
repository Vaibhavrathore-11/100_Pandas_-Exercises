# info method to get the summary of the dataframe 
import pandas as pd
df = pd .read_json("test.json")
print(df)
print(df.info())

import pandas as pd 
df = pd .read_csv("students.csv")
print(df.info())