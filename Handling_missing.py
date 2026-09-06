# Handle Duplicates
import pandas as pd

df = pd.read_csv("industry.csv", sep="\t")

print("Original Data:")
print(df)

print("\nDuplicate Check:")
print(df.duplicated())

print("\nTotal Duplicates:")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("\nAfter Removing Duplicates:")
print(df)
