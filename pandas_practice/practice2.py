#index position into label position name

import pandas as pd
s = pd .Series([19,24,33,46,54], index=["Vaibhav","divyansh","sourabh","om", "Rathore"])
print(s)
print(s["Vaibhav"])