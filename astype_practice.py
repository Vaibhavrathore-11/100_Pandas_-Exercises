import pandas as pd
data = {
    "Tempreature": ["25.5" , "30.2" , "28.7" , "32.1"]
}

df = pd.DataFrame(data)
print(df.dtypes)

df["Tempreature"] = df["Tempreature"].astype(float)
print(df.dtypes)




# Example_1
import pandas as pd
data = {
    "salary":["25000","30000","45000","60000"]

}
df1 = pd.DataFrame(data)  
print(df1.dtypes)
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
df3= pd.DataFrame(data)

print(df3)

df3["Marks"] = pd.to_numeric(df3["Marks"],errors="coerce")

print(df3)

print(df3.dtypes)
