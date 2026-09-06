import pandas as pd
data = {
    "Name": ["Rahul", "shyam","Ram","vaibhav","None"],
    "Age": [21, None , 22, None , 31],
    "City": ["indore","None","jabalpur", "Mumbai","goa"],
    "Marks": [78 , 88, None, 33, 98]
}
df = pd.DataFrame(data)

print(df)

print(df.isnull()) #Har cell check karta hai.

pf = df.isnull().sum() #Har column ke missing values count karta hai.
print(pf)

pf =df.isnull().sum().sum() #Pure dataset ke total missing values count karta hai.
print(pf)