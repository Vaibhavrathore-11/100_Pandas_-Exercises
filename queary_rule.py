#Filtering data -> query rule

import pandas as pd 
df = pd.read_csv("netflix_titles.csv")
print(df.query('release_year > 2015 & type == "Movie"'))


