import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)
print("Creating DataFrame:-")
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

print("Dataframe is:-")
print(df)

print("Displaying element of W colomn:-")
print(df['W'])

print("Displaying element of W colomn and B row is :-")
print(df['W']['B'])

print("Displaying elements of multiple columns:-")
print(df[['W','Z']])

print("Creating new column by adding another column:-")
df['new']=df['W']+df['Y']
print(df)

print("Removing column new from DF using drop():-")
df.drop('new', axis=1 , inplace=True)
print(df)

print("Displaying element of row 'A' using loc():- ")
print(df.loc['A'])

print("Displaying element of row 'A' by index using iloc():- ")
print(df.iloc[0])

print("Displaying  Column and Row value:-")
print(df.loc['A','Z'])

print("Displaying multiple Column and Row value:-")
print(df.loc[['A','B'],['W','Y']])

print("Checking Values greater than Zero:-")
bool_df= df>0
print(df[bool_df])

print("Displaying Df value 'W'column greater than zero:-")
# It will filter all rows less than Zero
print(df[df['W']>0])

print("Displaying Df value 'W' greater than zero anf 'Y' greater than 1:-")
print(df[(df['W']>0) & (df['Z']<1)])


print("Changing Index :-")
new_ind = "IND CA NY WY CO".split()
df['States']=new_ind
df.set_index('States')
