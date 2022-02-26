# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 01:59:51 2022

@author: SAMSON
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
pf=pd.read_csv("C:/Users/SAMSON/gdp.csv",header=0,index_col=0)
print(pf)
df=pd.DataFrame(pf)
print(df)

x=np.array([[0,1],[5,1],[15,2],[25,5],[35,11],[45,15],[55,34],[60,35]])
y=np.array([4,5,20,14,32,22,38,43])
x=sm.add_constant(x)
model=sm.OLS(y,x)
results=model.fit()
print(results.summary())
    
    
    
    