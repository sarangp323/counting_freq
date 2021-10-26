Print("PANDAS MISSING DATA AND GROUP BY")
Print("Pandas Missing Values")
import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)


print("Removing Missing Values:-")
print(df.dropna())

print("Removing Missing Values having min 2 missing values ")
print(df.dropna(thresh=2))

print("Removing Missing Values along Column:-")
print(df.dropna(axis=1))

print("Removing Missing Values along Column:-")
print(df.dropna(axis=1))

print("Filling missing values by mean of Column:-")
df.fillna(value=df.mean())


print("************************************************")
print("Pandas Group BY")
import pandas as pd
import numpy as np
data = {'Company':['GOOGLE','GOOGLE','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Chalie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
print("Dataframe is:-")
df1=pd.DataFrame(data)
print(df1)

print("Group by Company and finding mean:-")
bycomp = df1.groupby('Company')
bycomp.mean()

print("Group by Company and finding Standard Deviation:-")
bycomp = df1.groupby('Company')
bycomp.std()

print("Group by Company and finding Total sales of 'FB':-")
bycomp = df1.groupby('Company')
bycomp.sum().loc['FB']

print("Printing how many person works in Company:-")
df1.groupby('Company').count()

print("Printing maximum sales by a Company:-")
df1.groupby('Company').max()

print("Displaying All Information of a company:-")
df1.groupby('Company').describe().transpose()
