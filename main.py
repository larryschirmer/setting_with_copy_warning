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

# assign misaligned indexes to dataframe
column1 = [1, 2, 3, 4, 5, 6]
indexes = pd.date_range('20130102', periods=6)
s1 = pd.Series(column1, indexes)

df['E'] = s1

print(df)

# assign value at labels
df.at[dates[0], 'A'] = 0
print(df)

# reassign column D to 5
df.loc[:, 'D'] = np.array([5] * len(df))
print(df)

# inverse values where a value greater than 0
df[df > 0] = -df
print(df)
