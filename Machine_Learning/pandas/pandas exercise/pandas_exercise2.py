import pandas as pd
ecom = pd.read_csv('Ecommerce Purchases')
ecom.head()
ecom.info()

print("Average Purchase Price:-")
print(ecom['Purchase Price'].mean())

print("Highest and Lowest Purchase Prices:- ")
print("Highest:-",ecom['Purchase Price'].max())
print("Lowest:-",ecom['Purchase Price'].min())

print("People having 'en' as language")
print(ecom[ecom['Language']=='en'].count())

print("How many people has job title as lawyer:-")
print(ecom[ecom['Job']=='Lawyer'].count())

print("How many people make purchase during 'AM' and 'PM':-")
print(ecom['AM or PM'].value_counts())

print("Five most common Job Titles:-")
print(ecom['Job'].value_counts().head(5))

print("Someone made a purchase that came from Lot: '90 WT' , what was the Purchase Price for this transaction?")
ecom[ecom['Lot']=='90 WT']['Purchase Price']

print("email of the person with the following Credit Card Number: 4926535242672853")
print(ecom[ecom['Credit Card']==4926535242672853]['Email'])

print("How many people have American Express as their Credit Card Provider *and made a purchase above $95 ?")
ecom[(ecom['CC Provider']=='American Express')&(ecom['Purchase Price']>95)].count()

print("How many people have a credit card that expires in 2025?")
sum(ecom['CC Exp Date'].apply(lambda x: x[3:]=='25'))

ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)



