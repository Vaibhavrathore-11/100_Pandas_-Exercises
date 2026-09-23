#Returns all rows from the left table and the matching rows from the right table; if there is no match, NaN/NULL is returned for the right table's columns.

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

value = pd.merge(df_customer,df_order,on="customer_id" , how="left") # left join 

print(value)


