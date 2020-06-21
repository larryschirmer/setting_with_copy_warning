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

# reindex dataframe
df1 = df.reindex(index=dates[0:4].append(pd.date_range(
    '20130107', periods=2)), columns=list(df.columns) + ['E'])
print(df1)

# fill in missing values
print(df1.fillna(value=1))
