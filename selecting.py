# selecting data 
import pandas as pd
df = pd.read_csv("globalAirQuality.csv")

# columns
city_data = df["city"]
print(city_data)
city_data = df[["city","aqi", "country"]]
print(city_data)
df.loc[0]

#rows 
print(df.loc[1])
print(df.loc[0:2]) # start idx : end idx (inclusive)
print(df.iloc[2])
print(df.iloc[0:3]) # start idx : end idx (exclusive)

#cells - row, col
print (df.loc[0:2,"city"])
print(df.columns)
print(df.iloc[0:2, 2])
print(df.loc[0:2, ["city", "country","longitude", "latitude"]])
print(df.iloc[0:3, 1:5])

# cell use at and iat
print(df.at[0, "city"])
print(df.iat[0, 2])

cities = df["city"] # view
print(cities[0])
cities[0] = "jaipur"
print(df["city"])