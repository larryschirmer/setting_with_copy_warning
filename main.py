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

top5 = df.head()
bottom3 = df.tail(3)

print('\ntop 5')
print(top5)

print('\nbottom 3')
print(bottom3)
