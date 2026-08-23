#Create a DataFrame using dictionary

import pandas as pd
df = pd.DataFrame([["Vaibhav", 20], ["Isha",20], ["kashu" , 22], ["Aadi", 18]], columns = ["Name" , "Age"])
print(df)