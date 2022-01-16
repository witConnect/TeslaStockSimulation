# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:11:10 2020

@author: jayasuriya
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


my_file=pd.read_csv('teslaproject.csv')
dataset=my_file.copy()


dataset['Date']=dataset['Date'].astype('str')

dataset['Year']=dataset['Date'].str[0:4]
dataset['Month']=dataset['Date'].str[5:7]


dataset['Date']=pd.to_datetime(dataset['Date'])
dataset['Month']=pd.to_numeric(dataset['Month'])

year_group=dataset.groupby('Year').sum()
month_group=dataset.groupby('Month').sum()

#plot for maxvalue year wise
plt.figure(figsize=(10,12),dpi=300)

plt.plot(dataset['Year'].unique(),year_group['High'],label='high',color='#b73fcc',linewidth=1,marker='.',markersize='12',markeredgecolor='green')
plt.bar(dataset['Year'].unique(),year_group['High'],label='highest value for stocks sold ',color='#05e6ff')
plt.title('max value obtained  year by year (2010 - 2020)')
plt.xlabel('year')
plt.ylabel('maximum stocks sold ')
plt.legend()
plt.savefig('projectimagehighyearwise.png',dpi=300)

#plot for minimum value year wise
plt.figure(figsize=(10,12),dpi=300)

plt.plot(dataset['Year'].unique(),year_group['Low'],label='low',color='red',linewidth=1,marker='.',markersize='12',markeredgecolor='white')
plt.bar(dataset['Year'].unique(),year_group['Low'],label='lowest value for stocks sold',color='yellow')
plt.title('lowest value obtained  year by year(2010 - 2020)')
plt.xlabel('year')
plt.ylabel('minimum stock sold ')
plt.legend()
plt.savefig('projectimagelowyearwise.png',dpi=300)


#plot for max sold month wise all years
plt.figure(figsize=(10,12),dpi=300)

months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
plt.plot(months,month_group['High'],label='High',color='orange')
plt.bar(months,month_group['High'],label='maximum value obtained for stocks sold',color='#ff00bf')
plt.title('highest value obtained month wise(from 2010 to 2020)')
plt.xlabel('month')
plt.ylabel('amount of stocks sold')
plt.legend()
plt.savefig('projectimagehighmonthwise.png',dpi=300)

#plot for min sold month wise all years

plt.figure(figsize=(10,12),dpi=300)

plt.plot(months,month_group['Low'],label='Low',color='green')
plt.bar(months,month_group['Low'],label='lowest value obtained for stocks sold',color='#ff0000')
plt.title('lowest value obtained month wise(from 2010 to 2020)')
plt.xlabel('month')
plt.ylabel('amount of stocks sold')
plt.legend()
plt.savefig('projectimagelowmonthwise.png',dpi=300)


#scatter plot for max value all years

plt.figure(figsize=(10,12),dpi=300)

plt.plot_date(dataset['Date'],dataset['High'],color='violet',label='maximum stock value')
plt.title('maxx value for 10 years(2010 - 2020)')
plt.xlabel('years')
plt.ylabel(' units of stock sold')
plt.legend()
plt.savefig('projectimagehighplotdate.png',dpi=300)

#scatter plot for min value all years

plt.figure(figsize=(10,12),dpi=300)

plt.plot_date(dataset['Date'],dataset['Low'],color='#deb367',label='minimum stock value')
plt.title('minn value for 10 years(2010 - 2020)')
plt.xlabel('years')
plt.ylabel(' units of stock sold')
plt.legend()
plt.savefig('projectimagelowplotdate.png',dpi=300)

#comparison image on high and low 
#stack plot on high and low month-wise

plt.figure(figsize=(10,12),dpi=300)

plt.style.use("fivethirtyeight")

x=month_group['High']
y=month_group['Low']

colors=['#0088ff','#b1ebff']
labels=['high','low']

plt.stackplot(months,x,y,labels=labels,colors=colors)
plt.legend(loc='upper left')
plt.savefig('projectimagecomparisonmonthwise.png',dpi=300)

#stackplot on high and low year-wise
plt.figure(figsize=(10,12),dpi=300)

plt.style.use("fivethirtyeight")

years_stackplot=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
x=year_group['High']
y=year_group['Low']

colors=['pink','blue']
labels=['high','low']

plt.stackplot(years_stackplot,x,y,labels=labels,colors=colors)
plt.legend(loc='upper left')
plt.savefig('projectimagecomparisonyearwise.png',dpi=300)

plt.show()


