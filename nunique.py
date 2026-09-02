# nunique method to get the number of unique values in each column of the dataframe

import pandas as pd 

df = pd.read_csv("students1.csv")
print(df.nunique()) 

# returns the number of unique values in each column of the dataframe

#example
import pandas as pd 
df = pd.read_json("test.json")
print(df.nunique()) # returns