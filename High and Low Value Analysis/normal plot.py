# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:49:24 2020

@author: jayasuriya
"""


import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
newfile=pd.read_csv('teslaproject.csv')
print(newfile)

### normal chart

plt.figure(figsize=(6,4),dpi=300)
plt.plot(newfile['Date'],newfile['High'],label='high',color='red',linewidth=1,marker='.',markersize='12',markeredgecolor='green')
plt.title('high vs low',fontdict={'fontsize':20} )
plt.ylabel('date')
plt.xlabel('high and low')
plt.plot(newfile['Date'],newfile['Low'],label='low',color='black',linewidth=1,marker='*',markersize='12',markeredgecolor='red')
plt.legend()

plt.savefig('projectimage.png',dpi=300)
plt.show()