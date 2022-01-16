import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


my_file=pd.read_csv('tesla.csv')
dataset=my_file.copy()


dataset['Date']=dataset['Date'].astype('str')

dataset['Year']=dataset['Date'].str[0:4]
dataset['Month']=dataset['Date'].str[5:7]


dataset['Date']=pd.to_datetime(dataset['Date'])
dataset['Month']=pd.to_numeric(dataset['Month'])

year_group=dataset.groupby('Year').sum()
month_group=dataset.groupby('Month').sum()


plt.figure(figsize=(10,12),dpi=300)
plt.plot(dataset['Year'].unique(),year_group['Open'],label='open',color='black',linewidth=1,marker='.',markersize='12',markeredgecolor='green')
plt.bar(dataset['Year'].unique(),year_group['Open'],label='opening value for stocks sold ',color='yellow')
plt.title('opening value obtained  year by year (2010 - 2020)')
plt.xlabel('year')
plt.ylabel('sum of opening value of stocks sold ')
plt.legend()
plt.savefig('openingyearwise.png',dpi=300)


plt.figure(figsize=(10,12),dpi=300)
plt.plot(dataset['Year'].unique(),year_group['Close'],label='close',color='green',linewidth=1,marker='.',markersize='12',markeredgecolor='white')
plt.bar(dataset['Year'].unique(),year_group['Close'],label='closing value for stocks sold',color='blue')
plt.title('Closing  value obtained  year by year(2010 - 2020)')
plt.xlabel('year')
plt.ylabel('sum of closing value of stock sold ')
plt.legend()
plt.savefig('closingyearwise.png',dpi=300)


plt.figure(figsize=(10,12),dpi=300)
months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
plt.plot(months,month_group['Open'],label='open',color='black')
plt.bar(months,month_group['Open'],label='opening value obtained for stocks sold',color='yellow')
plt.title('Opening value obtained month wise(from 2010 to 2020)')
plt.xlabel('month')
plt.ylabel('sum of opening value of stock sold')
plt.legend()
plt.savefig('openingmonthwise.png',dpi=300)



plt.figure(figsize=(10,12),dpi=300)
plt.plot(months,month_group['Close'],label='close',color='green')
plt.bar(months,month_group['Close'],label='closing value obtained for stocks sold',color='blue')
plt.title('closing value obtained month wise(from 2010 to 2020)')
plt.xlabel('month')
plt.ylabel('sum of closing value of stock sold')
plt.legend()
plt.savefig('closingmonthwise.png',dpi=300)



plt.figure(figsize=(10,12),dpi=300)
plt.plot_date(dataset['Date'],dataset['Open'],color='red',label='opening stock value')
plt.title('Opening value for 10 years(2010 - 2020)')
plt.xlabel('years')
plt.ylabel(' opening value')
plt.legend()
plt.savefig('openingscatterplot.png',dpi=300)

#scatter plot for min value all years
plt.figure(figsize=(10,12),dpi=300)
plt.plot_date(dataset['Date'],dataset['Close'],color='red',label='closing stock value')
plt.title('closing value for 10 years(2010 - 2020)')
plt.xlabel('years')
plt.ylabel(' closing value')
plt.legend()
plt.savefig('closingscatterplot.png',dpi=300)

#comparison image on high and low 
#stack plot on high and low month-wise

plt.figure(figsize=(10,12),dpi=300)

plt.style.use("fivethirtyeight")

x=month_group['Open']
y=month_group['Close']

colors=['red','yellow']
labels=['Open','Close']

plt.stackplot(months,x,y,labels=labels,colors=colors)
plt.legend(loc='upper left')
plt.savefig('comparisonmonthwise.png',dpi=300)

#stackplot on high and low year-wise
plt.figure(figsize=(10,12),dpi=300)

plt.style.use("fivethirtyeight")

years_stackplot=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
x=year_group['Open']
y=year_group['Close']

plt.stackplot(years_stackplot,x,y,labels=labels,colors=colors)
plt.legend(loc='upper left')
plt.savefig('comparisonyearwise.png',dpi=300)

plt.show()

