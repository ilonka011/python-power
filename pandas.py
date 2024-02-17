import pandas as pd
df = pd.read_csv('names.csv', index_col='Name')
df.head()
df.describe()
