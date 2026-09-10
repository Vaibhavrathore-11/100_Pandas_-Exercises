import pandas as pd
df = pd.read_csv("raw_data.csv")
print(df)

df["country"] =df["country"].replace("USA","Udaipur") # use replace() function for replace any value of dataframe
print(df)