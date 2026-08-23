#Create a Dataframe
import pandas as pd

data = {

    "Name": ["Aman", "sita","om"],
    "Marks": [85, 90, 78]

}
df = pd.DataFrame(data)
print(df)