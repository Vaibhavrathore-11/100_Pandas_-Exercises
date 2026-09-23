#Returns only the rows that have matching values in both tables.
#Merging & joining data

import pandas as pd 

df_customer = pd.DataFrame({
    "customer_id": [1,2,3,4],
    "name": ["john","charli", "oggy","ben"]
})

df_order = pd.DataFrame({
    "order_id": [101,102,103,104],
    "customer_id": [2,1,4,5],
    "amount" : [200,432,552,748]
})

print(df_customer)
print(df_order)

val = pd.merge(df_customer,df_order,on="customer_id") # inner join
print(val)