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

# select a single column
print('\n')
print(df['A'])

# select a slice of rows
print('\n')
print(df[0:3])
