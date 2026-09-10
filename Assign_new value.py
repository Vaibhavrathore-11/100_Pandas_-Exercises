import pandas as pd
df = pd.read_csv("raw_data.csv")
print(df)
df["tax"] = df["income"].apply(lambda x: "20%" if x >= 60000 else "10%")
df["new_income"] = df["income"] *1.1
print(df)