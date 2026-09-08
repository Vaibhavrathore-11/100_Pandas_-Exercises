#change data type using-> astype() function  


import pandas as pd
df = pd.DataFrame({
    "Name": ["vai","shyam","om","sourabh"],
    "Age": [23,21,13,19],
    "Address":["Dubai", "london", "paries","viyatnaam"]
})

print(df)
print(df.dtypes)
df["Age"] = df["Age"].astype(float)
print(df.dtypes)
