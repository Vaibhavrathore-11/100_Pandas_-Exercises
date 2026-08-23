#Create a DataFrame using dictionary

import pandas as pd
data = {
    "Name": ["Krishna","Isha", "Vansh", "Harsh"],
    "Age": [19,20,21,22],
    "CGPA":[8.7,9.1,8.9,8.0]
}

df = pd. DataFrame(data)
print(df)
print(df.index)