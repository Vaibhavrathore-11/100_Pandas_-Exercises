#fillna , bfill , ffill

import pandas as pd
df = pd.read_csv("industry.csv" , sep="\t")
print(df)
#fillna
age_mean = df["Age"].mean()
df["Age"] = df["Age"].fillna(age_mean)
print(df[["Name" , "Age"]])


cleaned_data = df .copy()
age_mean = cleaned_data["Age"].mean()
cleaned_data["Age"]= cleaned_data["Age"].fillna(age_mean)
print(cleaned_data)


# ffill-> use for forward fill
df = df.ffill()
print(df)

# backwardfill
fill = df.bfill()
print(fill)