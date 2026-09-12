import pandas as pd
df = pd.read_csv("students.csv")


#Age ascending order
df = df.sort_values("Age", ascending = True)
val_df = df.sort_values(["Marks","Age"], ascending = [True , True]).reset_index(drop = True)

print(val_df)

# reset (function) use for sahi indexing ke liye
sorted_df = df.reset_index(drop=True)
print(sorted_df)

#RANKING function() 
# Pandas ka function hai jo DataFrame ya Series ki values ko unki position ke according numerical rank assign karta hai.

sorted_df["Ranking"] = sorted_df["Marks"].rank()
sorted_df = df.fillna(0)
print(sorted_df)

sorted_df["ranking"] = sorted_df["Age"].rank()
print(sorted_df)

# rankig shorted index namw with column 
sorted_df[["City", "Marks","Age", "Name"]]
print(sorted_df)


