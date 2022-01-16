# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:53:59 2020

@author: jayasuriya
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

my_file=pd.read_csv('teslaproject.csv')

plt.scatter(my_file['Date'],my_file['High'],color='#b73fcc')
plt.title('high vs low',fontdict={'fontsize':20} )
plt.ylabel('date')
plt.xlabel('high and low')
plt.plot(my_file['Date'],my_file['Low'],color='black')
plt.savefig('projectimage1.png',dpi=300)
plt.show()