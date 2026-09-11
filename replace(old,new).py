import pandas as pd
df = pd.read_csv("raw_data.csv")
print(df)

df["country"] =df["country"].replace("USA","Udaipur") # use replace() function for replace any value of dataframe
print(df)

df.columns = {"ID","Name","Age","Country","Gender", "Income"}
print(df)
df.rename(columns={"income":"Salary"})
df.rename(index={1:"First"})

#sort function using sort_values
df = df.sort_values("Income")
df = df.sort_values("Income","Age")# assending order sorting
df = df.sort_values("Income", assending= False) #dessending order
print(df)
