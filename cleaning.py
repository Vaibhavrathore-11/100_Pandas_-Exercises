#cleaning data - Handling missing values 

import pandas as pd
df = pd.read_csv("Diabetes Missing Data .csv")
print(df.isnull())
print(df.isnull().sum())# channing 
print(df.isna())
print(df.dropna()) # drop the missing valuees
print(df.dropna(axis = 1)) # rows

print(df.fillna(0))

age_mean = df["Age"].mean()

cleaned_data = df.copy()
cleaned_data["Age"] = cleaned_data["Age"].fillna(age_mean)
print(cleaned_data["Age"])


#  ***for practice***