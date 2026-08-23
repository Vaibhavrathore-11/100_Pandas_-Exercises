#vectorized operations in pandas

import pandas as pd
S1 = pd.Series([1,2,3,4,5,6])
S2 = pd.Series([10,20,30,40,50,60])
print(S1 + S2)
print(type(S1 + S2))