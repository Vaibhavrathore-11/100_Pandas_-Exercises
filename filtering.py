#Filtering of data based on certain criteria
import pandas as pd 
df = pd.read_csv("globalAirQuality.csv")

#filtering operations 
df_filtered = df[df["aqi"] > 100]# filterbased ing rows 
print(df_filtered)

df_filtered2 = df[(df["aqi"] > 100) & (df["temperature"] > 30)]
print(df_filtered2)

df_filtered3 = df[(df["aqi"] > 100) & (df ["temperature"] < 30)]
print(df_filtered3)

df_filtered4 = df[df["aqi"] > 100] [["city", "aqi"]]
print(df_filtered4)

df_filtered5 = df[df["aqi"] < 100]
[["city", "aqi"]]
print(df_filtered5)

df_filtered6 =df[(df["aqi"] > 100) & (df["temperature"] > 90) ] [["city" , "aqi", "temperature"]]
print(df_filtered6)


aqi_data = df [(df["aqi"] > 100) & (df["temperature"] > 30) ] [["city", "aqi", "temperature"]]
print(aqi_data) 
print(aqi_data.iloc[0])
print(aqi_data.loc[7])

