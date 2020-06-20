import numpy as np
import pandas as pd

# create a DatetimeIndex
dates = pd.date_range('20130101', periods=6)
print('\ndates')
print(dates)

# create a Dataframe
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print('\ndf')
print(df)

# boolean indexing
# use filtered column indexes to filter dataset
print(df[df['A'] > 0])

# select values were condition is true
print(df[df > 0])

# return rows where condition label is in row
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2[df2['E'].isin(['two', 'four'])])