import pandas as pd
data = {
    "Name" :["heery", "somya", "Nandu"],
    "Age" :[21, 23, 11],
    "Salary" :[10000,20000,30000]
}
df = pd.DataFrame(data)
print(df)

df = df.rename(columns = {"Salary" : "income"}) # columns rename karna [df.rename(columns)] 

df = df.rename(columns = {"Name": "Employee_Name"})
print(df)

df = df.rename(index = {0:"zero"})
print(df)# index ka use karke label rename karte ha 
