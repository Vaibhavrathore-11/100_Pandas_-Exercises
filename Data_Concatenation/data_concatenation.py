#data concatenation row Wise
import pandas as pd

df1 = pd.DataFrame({
    "id" : [1,2,3],
    "name": ["vansh","franchi","billu",]
    })

df2 = pd.DataFrame({
    "id" : [4,5,6],
    "name":["sourabh","harry","porter"]
})

print(pd.concat([df1,df2]))# Raw (staking dataFrame on top of each other(rows))