import pandas as pd
import numpy as np
from numpy.random import randn

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]

hier_index= list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print("Creating Multi Index Dataframe:-")
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

print("Printing element associated with G1:-")
print(df.loc['G1'])

print("Printing element associated with G1 and index 1:-")
print(df.loc['G1'].loc[1])

print("Printing element associated with G2 and index 2 of column 'B':-")
print(df.loc['G2'].loc[2]['B'])
