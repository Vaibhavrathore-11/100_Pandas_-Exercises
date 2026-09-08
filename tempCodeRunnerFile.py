df1["salary"] = df1["salary"].astype(int)
print(df1)

print(df1.dtypes)


#Example2
import pandas as pd
data = {
    "Age" : ["20", "21", "22"],
    "Marks":["80.4", "90.0", "67.8"]
}
df2 = pd.DataFrame(data)
print(df2.dtypes)

df2["Age"] = df2["Age"].astype(int)
print(df2,df2.dtypes)
df2["Marks"] = df2["Marks"].astype(float)
print(df2.dtypes)


#Example3
import pandas as pd
data = {
     "Marks":["80", "90", "absent", "75"]
}
df = pd.DataFrame(data)
print(df)
df["Marks"] = pd["Marks"].astype(int)
errors = "coerce"