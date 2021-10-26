import numpy as np
import pandas as pd

sal = pd.read_csv('Salaries.csv')

print("displaying df:-")
sal.head()

print("Display Info:-")
print(sal.info())

print("Average Base pay:-")
print(sal['BasePay'].mean())

print("Highest Amount of Overtime:-")
print(sal['OvertimePay'].max())

print("Job title of Joseph Driscoll:-")
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

print("How much Joseph Driscoll make:")
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])

print("Person with highest salary:-")
print(sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].max()] )

print(sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].min()])

print("Average Basepay of all employee per year")
print(sal.groupby('Year').mean()['BasePay'])

print("Unique Job title:-")
print(sal['JobTitle'].nunique())

print("Top Job Titles:-")
sal['JobTitle'].value_counts().head()

print("Unique job titles  in 2013")
print(sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1))

print("How many people have chief in job")

def chief_str(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
    
print(sum(sal['JobTitle'].apply(lambda x:chief_str(x))))
