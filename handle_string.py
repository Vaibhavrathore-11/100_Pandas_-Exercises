#handle string 

#Lower()
import pandas as pd
df = pd.read_csv("students.csv")
print(df)
df = df["Name"].str.lower() # lower() fuction convert string into lower
print(df)

# Upper()
import pandas as pd
df1 = pd.read_csv("students.csv")
df1 = df1["Name"].str.upper() # upper fuction that is used to convert  string into upper case
print(df1)


#Capitalize
import pandas as pd
df2 = pd.read_csv("students.csv")
df2 = df2["Name"].str.capitalize()
print(df2)

#Example
import pandas as pd
df3 = pd.read_csv("students1.csv")

df3["Name"]= df3["Name"].str.capitalize()

df3 ["City"]= df3["City"].str.upper()


df3 ["Department"] = df3["Department"].str.lower()

print(df3)