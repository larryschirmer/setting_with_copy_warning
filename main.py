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

# select by label
print('\nOne Index')
print(df.loc[dates[0]])

# select by label
print('\nAll Indexes with two columns')
print(df.loc[:, ['A', 'C']])

# select by label
print('\nScalar at location')
print(df.at[dates[0], 'C'])
