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



#string Transformation 

import pandas as pd 
data = {
    "Name" : ["amit", "Rahul", "shyam", "tenser"]
}
str = pd.DataFrame(data)
print(str)

str["Name"] = str["Name"].str.upper()
print(str)#upper case me convert ke liye


str["Name"] = str["Name"].str.lower()
print(str)#upper case me convert ke liye

str["Name"] = str["Name"].str.title()
print(str)#title case me convert ke liye

str["Name"] = str["Name"].str.capitalize()
print(str)#capitalize case me convert ke liye


#String replace
import pandas as pd
str1 = pd.read_csv("raw_data.csv")
print(str1)
str1["country"] = str1["country"].replace("USA","Russia")
str1["name"] = str1["name"].str.replace("John Doe", "Anii")
print(str1)
