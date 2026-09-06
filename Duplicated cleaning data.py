#Duplicated cleaning data with the help of isnull & isnull.sum()

 
import pandas as pd
df = pd.read_csv("industry.csv" , sep="\t")
print(df)
df = df.isnull()
print(df)
df_sum =df.isnull().sum()
print(df_sum)




