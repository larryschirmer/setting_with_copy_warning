import numpy as np
import pandas as pd

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print(df[:4])
print(df.loc[('bar', 'two'), 'B'])

stacked = df.stack()
print(stacked[:4])
print(stacked.loc[('bar', 'two', 'B')])
