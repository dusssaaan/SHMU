#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
linear interpolation script

@author: p6001
"""

import numpy as np

def lin_interpol(x,y):
    
    x=np.array(x)
    y=np.array(y)
  
    n=x.shape[0]
    sumx=np.sum(x)
    sumy=np.sum(y)
    sumxy=np.sum(x*y)
    sumx2=np.sum(x*x)
    sumy2=np.sum(y*y)
  
    m=(n * sumxy - sumx * sumy)/(n * sumx2 -sumx**2)
    b=(sumy * sumx2 - sumx * sumxy)/(n * sumx2 -sumx**2)
    r=(sumxy - sumx * sumy / n)/np.sqrt((sumx2 - sumx**2/n)*(sumy2 - sumy**2/n))
    
    return m, b, r