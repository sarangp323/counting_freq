import pandas as pd
df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3'],
                   'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3']},index=[0,1,2,3])

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                   'B':['B4','B5','B6','B7'],
                   'C':['C4','C5','C6','C7'],
                   'D':['D4','D5','D6','D7']},index=[4,5,6,7])

df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                   'B':['B8','B9','B10','B11'],
                   'C':['C8','C9','C10','C11'],
                   'D':['D8','D9','D10','D11']},index=[8,9,10,11])

print("Dataframe 1 is:-")
print(df1)

print("Dataframe 2 is:-")
print(df2)

print("Dataframe 3 is:-")
print(df3)

print("CONCATENATION :-")
print(pd.concat([df1,df2,df3]))

left = pd.DataFrame({'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3'],
                   'key':['K0','K1','K2','K3']})
                     
right = pd.DataFrame({'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3'],
                   'key':['K0','K1','K2','K3']})

print("Left dataframe is:-")
print(left)

print("Right dataframe is:-")
print(right)

print("****************************************")
print("MERGING")
pd.merge(left,right,how='inner',on='key')

left = pd.DataFrame({'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3'],
                   'Key1':['K0','K0','K1','K2'],
                    'Key2':['K0','K1','K0','K1']})
                     
right = pd.DataFrame({'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3'],
                   'Key1':['K0','K1','K1','K2'],
                     'Key2':['K0','K0','K0','K0']})

print("Left dataframe is:-")
print(left)

print("Right dataframe is:-")
print(right)

print("Merging df on inner join bases on key1 and ley2:-")
print(pd.merge(left,right,how='inner', on=['Key1','Key2']))

print("************************************")
print("Joining")
left = pd.DataFrame({'A':['A0','A1','A2'],
                   'B':['B0','B1','B2']},
                   index=['K0','K1','K2']
                    )
                     
right = pd.DataFrame({'C':['C0','C2','C3'],
                   'D':['D0','D2','D3']},
                   index=['K0','K2','K3'],
                     )

print("Left dataframe is:-")
print(left)

print("Right dataframe is:-")
print(right)

print("joining right and left")

left.join(right)

print("Outer joining right and left")

left.join(right,how='outer')

