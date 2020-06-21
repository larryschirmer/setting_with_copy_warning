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

# calculate mean of each column
print(df.mean())

# calculate mean of each row
print(df.mean(1))

# calculate subtraction by row
print(df - [0.5, 0.25, 0.12, 0.06])

# use function along a column
print(df.apply(lambda x: x.max() - x.min()))
