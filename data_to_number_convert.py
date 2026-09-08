

import pandas as pd 
df = pd.DataFrame({
     'salary': ['25000','32000','40000','abc']

})
print(df)
print(df.dtypes)

df["salary"] = pd.to_numeric(
  df["salary"],
  errors="coerce"

)

print(df)
print(df.dtypes)
