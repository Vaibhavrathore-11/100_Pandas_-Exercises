#Create table using Dictionary

import pandas as pd
dic = {"name":['python','c','c++','Java'], "Rank":[1,4,3,2]}
var = pd.Series(dict)
print(var)
print(type(var))
# if you used mixed type data than the series type is object
