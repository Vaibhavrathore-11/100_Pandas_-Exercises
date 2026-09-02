# sample value from the dataset
import pandas as pd 
df = pd.read_csv("students1.csv")
print(df.sample()) # random sample of rows from the dataset
