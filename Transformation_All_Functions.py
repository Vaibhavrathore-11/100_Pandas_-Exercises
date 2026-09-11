'''RAW DATA   # steps of transformation
   ↓
Transform
   ↓
CLEAN / USEFUL DATA
   ↓
ANALYSIS'''




#Increased employee salaries by 10% using vectorized mathematical operations in Pandas.


import pandas as pd
data = {
    "Name": ["vedu","Deva","Harsh","Atrain"],
    "Salary":[200000,40000,70000,90000]
}
df = pd.DataFrame(data)
print(df)
df["Salary"] = df["Salary"]*1.10
print(df)


#practice Question New column create karke transformation
#Original Salary ko change nahi karna ho:

import pandas as pd
df1 = pd.read_csv("students1.csv")
print(df1)
df1["new_Salary"] = df1["Salary"] * 1.20
print(df1)
print(df1[["Name", "Salary", "new_Salary"]])
print(df1)

#Transforming data using .apply() function use kARKE 20% salary increase karna
#ussi data me change karna ha bina koi dusara column banakar

import pandas as pd
df2 = pd.read_csv("students1.csv")
print(df2)

df2["Salary"] = df2["Salary"].apply(lambda x: x * 1.20)
print(df2)



#Conditional Transformation using apply() function⭐⭐⭐
import pandas as pd
df3 = pd.read_csv("students1.csv")
print(df3)
df3["Category"] = df3["Salary"].apply(lambda x: "High" if x >= 40000 else "Low")
print(df3)
print(df3[["Name" , "Salary", "Category"]])


#Multiple conditions
import pandas as pd
df4 = pd.read_csv("raw_data.csv")
print(df4)
df4["Category"] = df4["income"].apply(lambda x : "High" if x>=70000 else "Medium" if x >=50000 else "Low")
print(df4)



#map() se transformation ⭐⭐⭐

import pandas as pd
data  = {
    "Department":["HR","IT","CSE","Sales"]
}
df = pd.DataFrame(data)
print(df)

mapping = {
    "HR" : "Human Resources",
    "IT" : "Information Technology",
    "CSE": "Computer Science Engennering",
    "Sales": "Sales Department"

}

df["Departrment"] = df["Department"].map(mapping)
print(df)

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


#Numeric → Category transformation

import pandas as pd
data = {
    "Name" :["A", "B", "C", "D"],
    "Marks" : [85 , 72, 45, 30]
}

str2= pd.DataFrame(data)

str2["Grade"] = str2["Marks"].apply(lambda x: "A" if  x >= 80 else "B" if x >= 60 else "C")
print(str2)


# replace function used for transformatin
import pandas as pd
str3 = pd.read_csv("students.csv")
print(str3)
str3["City"] = str3["City"].replace({"indore" : "satna", "Gwalior": "panna"})
print(str3)
#map()     → mapping ke through values transform
#replace() → specific values replace

#Data Type Transformation (string -> integer)⭐⭐⭐
import pandas as pd
data = {
    "Age" : ["21","20","31"]
}
Data_Type = pd.DataFrame(data)
print(Data_Type.dtypes)

Data_Type["Age"] = Data_Type["Age"].astype(int)
print(Data_Type.dtypes)


#pd.to_numeric() function use for string and mixed data convert into numeric (int/float)

import pandas as pd
data = {
    "Marks": ["70","80","50" ,"absent","66"]
}
fa = pd.DataFrame(data)
print(fa)
 #fa["Marks"] = fa["Marks"].astype(int) To error aayega, kyunki "absent" ko integer mein convert nahi kar sakte.

 # use pd.to_numeric() ->(Function)
fa["Marks"] = pd.to_numeric(
    fa["Marks"],
    errors= "coerce"
)
print(fa)

#Example of pd.to_numeric()

import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohit"],
    "Salary": ["45000", "60000", "Not Available", "75000", "50000"]
}
fa1 = pd.DataFrame(data)
print(fa1)

fa1["Salary"] = pd.to_numeric(
    fa1["Salary"],
    errors = "coerce"
)
print(fa1)



#Example
import pandas as pd
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohit"],
    "Salary": ["45000", "60000", "Not Available", "75000", "50000"]
}
df3= pd.DataFrame(data)

df3["Salary"] = pd.to_numeric(
    df3["Salary"],
    errors = "coerce"
)
print(df3)
df3["Bonus"] = df3["Salary"] * 0.10
print(df3)
average_salary = df3["Salary"].mean()

df3["Salary"] = df3["Salary"].fillna(average_salary)
print(df3)