import pandas as pd

df1 = pd.DataFrame({
    "name" : ["rahul","yoyo","sahil"],
    "python" : [67,78,85]
})

df2 = pd.DataFrame({
    "namee": ["rahul","shyam", "riya"],
    "sql": [23,45,78]
})
value = pd.concat([df1,df2], axis=1)
print(value)