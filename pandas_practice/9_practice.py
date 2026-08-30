# create a DataFrame using arrays 1D

import numpy as np 
import pandas as pd
arr =np.array([[1,2,3],
                [4,5,6]])
df =pd.DataFrame(arr,columns =["A","B","C"])

print(df)