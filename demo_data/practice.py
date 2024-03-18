import pandas as pd
import numpy as np

#read csv
df = pd.read_csv('adult.data.csv')

#people of each race
print(df['race'].value_counts())

#avg_age of men
c1 = df['sex'] == 'Male'
print(round(df.loc[c1,'age'].mean(),1))

#only bacherlors
c2 = df['education'] == 'Bachelors'
print(round((df[c2].shape[0]/df.shape[0])* 100,1))

#adv edu 
#h = df[df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
#l = df[~df['education'].isin(["Bachelors", "Masters", "Doctorate"])]

#50k+-
#print(round((h[h['salary'] == ">50k"].shape[0]/h.shape[0])*100,1))
#print(round((l[l['salary'] == ">50k"].shape[0]/l.shape[0])*100,1))

#min work hours
min_hrs = df['hours-per-week'].min()
print(min_hrs)

num_high_salary_per_country = df[df['salary'] == ">50K"]['native-country'].value_counts()
num_country = df['native-country'].value_counts()
percentage = num_high_salary_per_country/num_country*100

highest_earning_country = percentage.idxmax()
highest_earning_country_percentage = round(percentage.max(),1)
print(highest_earning_country)
print(highest_earning_country_percentage)

occ = df[(df['salary'] == ">50K") & (df['native-country'] == "India")]['occupation'].value_counts()
print(occ.idxmax())