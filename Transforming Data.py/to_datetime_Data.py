import pandas as pd
aqi_data = pd.read_csv("globalAirQuality.csv")
print(aqi_data)
aqi_data = pd.Series([pd.to_datetime("2025-11-04")])
print(type(aqi_data.dtypes))



#Example 

import pandas as pd

data = {
    'Name': ["vansh", "harshu", "rathore", "Dhakad"],
    'date' :["2026-01-19", "2026-02-20", "2005-02-14","2005-04-20"]

}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["date"])
print(df)

