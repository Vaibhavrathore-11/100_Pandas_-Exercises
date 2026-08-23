#Change index value

import pandas as pd
S = [11,22,33,44,55]
var =pd.Series(S, index=['a','b','c','d','e'])
print(var)
print(type(var))