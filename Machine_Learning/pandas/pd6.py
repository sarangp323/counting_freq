print("Operations in pandas")
import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],
                  'col2':[444,555,666,444],
                  'col3':['abc','def','ghi','xyz']})
df.head()

print("Unique element in col2:-")
df['col2'].unique()
print("count of unique value:-")
df['col2'].nunique()

print("Applying any func that we want:-")
def times2(x):
    return x*2

df['col1'].apply(times2)

print("Sorting Df Acc. col2 values")
df.sort_values('col2')

print("\n")
print("*******************************************")
data = {'A':['foo','foo','foo','bar','bar','bar'],
       'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}
df1 = pd.DataFrame(data)
print("dataframe is:-")
print(df1)

print("Creating pivot table:-")
print(df1.pivot_table(values='D',index=['A','B'],columns=['C']))
